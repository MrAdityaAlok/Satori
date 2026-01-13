#!/usr/bin/bash

set -eoux pipefail

# Ensure Initramfs is generated:

KERNEL_VERSION="$(rpm -q --queryformat="%{evr}.%{arch}" kernel-cachyos-lto-core)"

export DRACUT_NO_XATTR=1
/usr/bin/dracut --no-hostonly --kver "${KERNEL_VERSION}" --reproducible -v --add ostree -f "/lib/modules/${KERNEL_VERSION}/initramfs.img"
chmod 0600 "/lib/modules/${KERNEL_VERSION}/initramfs.img"
