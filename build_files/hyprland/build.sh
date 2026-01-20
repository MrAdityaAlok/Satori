#!/bin/bash

set -oeux pipefail

install_hyprcursor_themes() {
	echo "INFO: Installing hyprcursor themes ..."

	mkdir -p /usr/share/icons/rose-pine-hyprcursor/

	curl -fLsS --retry 5 --create-dirs \
		https://github.com/ndom91/rose-pine-hyprcursor/releases/download/v0.3.2/rose-pine-cursor-hyprcursor_0.3.2.tar.gz \
		-o /tmp/cursor/hyprcursor.tar.xz

	tar -xf /tmp/cursor/pine.tar.xz -C /usr/share/icons/rose-pine-hyprcursor/

	echo "INFO: Installed hyprcursor themes."
}

/ctx/utils/install-nerd-font "CodeNewRoman" # For waybar. Iosevka is already installed in common.
install_hyprcursor_themes

/ctx/hyprland/packages.sh
/ctx/hyprland/systemd.sh

rsync -rvK /ctx/sys_files/hyprland/ /
