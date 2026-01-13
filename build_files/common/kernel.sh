#!/usr/bin/bash

set -ouex pipefail

dnf5 -y copr enable bieszczaders/kernel-cachyos-lto
# dnf5 -y copr enable bieszczaders/kernel-cachyos-addons

# kernel-modules-extra is not installed in the base bootc. Confirm on each major bump.
for pkg in kernel kernel-core kernel-modules kernel-modules-core; do
	rpm --erase $pkg --nodeps
done

# On F43, during kernel install, dracut errors and fails:
# create a shims to bypass kernel install triggering dracut/rpm-ostree
# seems to be minimal impact, but allows progress on build:
cd /usr/lib/kernel/install.d &&
	mv 05-rpmostree.install 05-rpmostree.install.bak &&
	mv 50-dracut.install 50-dracut.install.bak &&
	printf '%s\n' '#!/bin/sh' 'exit 0' >05-rpmostree.install &&
	printf '%s\n' '#!/bin/sh' 'exit 0' >50-dracut.install &&
	chmod +x 05-rpmostree.install 50-dracut.install
# Instead of shims, could skip scriptlets: dnf install -y --setopt=tsflags=noscripts
# but skipping all scriptlets for kernel install may not be safe.

dnf5 -y install kernel-cachyos-lto

# TODO: configure scx-scheds.

# Restore kernel install:
mv -f 05-rpmostree.install.bak 05-rpmostree.install &&
	mv -f 50-dracut.install.bak 50-dracut.install
cd -
