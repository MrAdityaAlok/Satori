#!/bin/bash

set -ouex pipefail

dnf5 -y copr enable mradityaalok/satori

dnf5 -y install \
	uwsm \
	app2unit \
	hyprland \
	hypridle \
	hyprlock \
	hyprpolkitagent \
	hyprsunset \
	hyprpaper \
	grimblast \
	clipse \
	xdg-desktop-portal-hyprland \
	qt5-qtwayland \
	qt6-qtwayland \
	gnome-keyring \
	fuzzel \
	dunst \
	waybar \
	brightnessctl \
	matugen \
	cava
