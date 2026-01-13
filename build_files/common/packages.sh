#!/bin/bash

set -ouex pipefail

if ! grep -q fedora-multimedia <(dnf5 repolist); then
	dnf5 config-manager setopt fedora-multimedia.enabled=1 ||
		dnf5 config-manager addrepo --from-repofile="https://negativo17.org/repos/fedora-multimedia.repo"
fi
dnf5 config-manager setopt fedora-multimedia.priority=90

# Multimedia codecs and proprietary packages:
dnf5 -y install \
	ffmpeg \
	ffmpeg-libs \
	ffmpegthumbnailer \
	pipewire \
	mesa-dri-drivers \
	mesa-libEGL \
	mesa-libGL \
	mesa-libgbm \
	mesa-filesystem \
	mesa-va-drivers \
	mesa-vulkan-drivers \
	libheif \
	libva

# Essential packages:
dnf5 -y install \
	NetworkManager-wifi \
	google-noto-color-emoji-fonts \
	podman \
	xdg-desktop-portal \
	xdg-desktop-portal-gtk \
	xdg-terminal-exec \
	gvfs-gphoto2 \
	gvfs-mtp \
	gvfs-fuse \
	gvfs-archive \
	nautilus \
	sushi \
	plymouth-theme-spinner \
	power-profiles-daemon

dnf5 -y copr enable atim/starship

# Other packages:
dnf5 -y install \
	starship \
	foot \
	fish \
	starship \
	fzf \
	zoxide \
	fastfetch \
	btop \
	neovim \
	wl-clipboard \
	git \
	android-tools \
	distrobox \
	toolbox \
	wget \
	nautilus \
	mpv \
	adw-gtk3-theme \
	papirus-icon-theme \
	yt-dlp
