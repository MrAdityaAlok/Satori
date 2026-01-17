#!/bin/bash

# Usage:
#   test_packages.sh                      # Run rpmlint on all RPMs in output/
#   test_packages.sh <package> <args...>  # Install package and run with args

set -eoux pipefail

setup_local_repo() {
	mkdir -p /tmp/local-repo
	cp /output/*.rpm /tmp/local-repo/

	if [ -z "$(ls /tmp/local-repo/*.rpm 2>/dev/null)" ]; then
		echo "No RPMs found in /output. Have you built them yet?"
		exit 1
	fi

	dnf install -y createrepo_c
	createrepo_c /tmp/local-repo

	cat <<-EOF >/etc/yum.repos.d/local-output.repo
		[local-output]
		name=Local Output
		baseurl=file:///tmp/local-repo
		enabled=1
		gpgcheck=0
		priority=1
	EOF
}

if [ $# -eq 0 ]; then
	echo "Running rpmlint on all RPMs..."
	dnf install -y rpmlint
	rpmlint /output/*.rpm || true
	exit 0
fi

PACKAGE="$1"
shift
ARGS="$*"

echo "Setting up local repository..."
setup_local_repo

echo "Installing $PACKAGE..."
dnf install -y "$PACKAGE"

echo "Running: $PACKAGE $ARGS"
$PACKAGE $ARGS

