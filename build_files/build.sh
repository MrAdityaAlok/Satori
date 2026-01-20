##!/bin/bash

set -ouex pipefail

# Make root's home:
mkdir -p /var/roothome

# Missing (upstream bug):
mkdir -p /usr/local/sbin

# Needed for build:
dnf5 -y install dnf5-plugins rsync fontconfig

# https://bugzilla.redhat.com/show_bug.cgi?id=2332429
dnf5 -y swap --repo='fedora' OpenCL-ICD-Loader ocl-icd

install_cursor_themes() {
	echo "INFO: Installing cursor themes ..."

	mkdir -p /usr/share/icons/BreezeX-RosePine-Linux/

	curl -fLsS --retry 5 --create-dirs \
		https://github.com/rose-pine/cursor/releases/latest/download/BreezeX-RosePine-Linux.tar.xz \
		-o /tmp/cursor/pine.tar.xz

	tar -xf /tmp/cursor/pine.tar.xz -C /usr/share/icons/BreezeX-RosePine-Linux/ --strip-components=1

	echo "INFO: Installed cursor themes."
}

/ctx/utils/install-nerd-font "Iosevka"
install_cursor_themes

/ctx/common/packages.sh
/ctx/common/flatpaks.sh
/ctx/"$VARIANT"/build.sh
/ctx/common/kernel.sh

rsync -rvK /ctx/sys_files/common/ /

/ctx/common/systemd.sh
/ctx/common/os-release.sh
/ctx/common/finish.sh
