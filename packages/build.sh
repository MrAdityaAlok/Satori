#!/bin/bash
set -oeux pipefail

mkdir -p /output
createrepo_c /output

cat <<-EOF >/etc/yum.repos.d/local-output.repo
	[local-output]
	name=Local Output
	baseurl=file:///output
	enabled=1
	gpgcheck=0
	priority=99
EOF

dnf -y copr enable mradityaalok/satori

for pkg in $TARGET_PKGS; do
	dir="/packages/$pkg"
	spec="$dir/$pkg.spec"

	[ ! -d "$dir" ] && echo "Skipping $pkg: not found" && continue
	[ ! -f "$spec" ] && echo "Skipping $pkg: no spec" && continue

	echo "=== Building $pkg ==="

	# Update local repo data before building:
	dnf clean metadata --repo local-output

	mkdir -p /root/rpmbuild/SOURCES
	cp -f "$dir"/* /root/rpmbuild/SOURCES/
	spectool -g -R --define '_sourcedir /root/rpmbuild/SOURCES' "$spec"

	dnf builddep -y --define '_topdir /root/rpmbuild' "$spec"
	rpmbuild --define '_topdir /root/rpmbuild' --define 'debug_package %{nil}' -bb "$spec"

	cp /root/rpmbuild/RPMS/*/*.rpm /output/

	rm -rf /root/rpmbuild/BUILD/* /root/rpmbuild/BUILDROOT/*
done

echo "Build complete."