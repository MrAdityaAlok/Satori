#!/bin/bash

set -ouex pipefail

dnf5 -y copr enable sdegler/hyprland

dnf5 -y install \
	uwsm \
	hyprland \
	hypridle \
	hyprlock \
	hyprpolkitagent \
	hyprsunset \
	hyprpaper \
	hyprshot \
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
