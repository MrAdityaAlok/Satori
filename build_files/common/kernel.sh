#!/usr/bin/bash

set -ouex pipefail

dnf5 -y copr enable bieszczaders/kernel-cachyos-lto
dnf5 -y copr enable bieszczaders/kernel-cachyos-addons

# kernel-modules-extra is not installed in the base bootc. Confirm on each major bump.
for pkg in kernel kernel-core kernel-modules kernel-modules-core; do
	rpm --erase $pkg --nodeps
done

# Addons:
dnf5 -y swap zram-generator-defaults cachyos-settings # NOTE: needs initramfs regeneration. So install before kernel.
dnf5 -y install scx-scheds scx-tools

systemctl enable scx_loader.service

# Fix kernel install:
cp /usr/lib/kernel/install.d/50-depmod.install /usr/lib/kernel/install.d/04-depmod.install
mkdir -p /var/tmp/
TMPDIR=/var/tmp/ dnf5 -y install kernel-cachyos-lto
