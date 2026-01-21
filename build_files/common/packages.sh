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
dnf5 -y copr enable mradityaalok/satori

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
	neovide \
	eza \
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

# Flatpak:
# TODO: remove when fedora shifts to >= 1.17 on next release:
dnf5 install -y --allowerasing \
	flatpak \
	flatpak-libs \
	flatpak-session-helper

mkdir -p /etc/flatpak/remotes.d/
curl --retry 3 -Lo /etc/flatpak/remotes.d/flathub.flatpakrepo https://dl.flathub.org/repo/flathub.flatpakrepo

systemctl mask flatpak-add-fedora-repos.service
