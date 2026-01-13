##!/bin/bash

set -ouex pipefail

# Make root's home:
mkdir -p /var/roothome
# systemd-tempfile:
mkdir -p /usr/local/sbin

if ! rpm -q dnf5 >/dev/null; then
	rpm-ostree install dnf5
fi

# Needed for build:
dnf5 -y install dnf5-plugins rsync

# https://bugzilla.redhat.com/show_bug.cgi?id=2332429
dnf5 -y swap --repo='fedora' OpenCL-ICD-Loader ocl-icd

/ctx/common/kernel.sh
/ctx/common/packages.sh
/ctx/common/extra-packages.sh
/ctx/common/flatpaks.sh

# Copy system files after packages installation to overwrite some files:
rsync -rvK /ctx/sys_files/common/ /

/ctx/common/systemd.sh

# Now build the variant:
/ctx/"$VARIANT"/build.sh

/ctx/common/os-release.sh
/ctx/common/finish.sh

# use CoreOS' generator for emergency/rescue boot:
# see detail: https://github.com/ublue-os/main/issues/653
CSFG=/usr/lib/systemd/system-generators/coreos-sulogin-force-generator
curl -sSLo ${CSFG} https://raw.githubusercontent.com/coreos/fedora-coreos-config/refs/heads/stable/overlay.d/05core/usr/lib/systemd/system-generators/coreos-sulogin-force-generator
chmod +x ${CSFG}

/ctx/common/initramfs.sh
