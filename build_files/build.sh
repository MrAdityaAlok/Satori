##!/bin/bash

set -ouex pipefail

# Make root's home:
mkdir -p /var/roothome

# Missing (upstream bug):
mkdir -p /usr/local/sbin

# Needed for build:
dnf5 -y install dnf5-plugins rsync

# https://bugzilla.redhat.com/show_bug.cgi?id=2332429
dnf5 -y swap --repo='fedora' OpenCL-ICD-Loader ocl-icd

/ctx/common/packages.sh
/ctx/common/flatpaks.sh
/ctx/"$VARIANT"/build.sh
/ctx/common/kernel.sh

rsync -rvK /ctx/sys_files/common/ /

/ctx/common/systemd.sh
/ctx/common/os-release.sh
/ctx/common/finish.sh
