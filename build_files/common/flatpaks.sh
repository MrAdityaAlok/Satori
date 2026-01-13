#!/bin/bash

set -ouex pipefail

# TODO: remove when fedora shifts >= 1.17 on next release:
dnf5 copr enable -y ublue-os/flatpak-test
dnf5 install -y --allowerasing \
	flatpak \
	flatpak-libs \
	flatpak-session-helper

mkdir -p /etc/flatpak/remotes.d/
curl --retry 3 -Lo /etc/flatpak/remotes.d/flathub.flatpakrepo https://dl.flathub.org/repo/flathub.flatpakrepo

systemctl mask flatpak-add-fedora-repos.service
