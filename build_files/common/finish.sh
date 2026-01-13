#!/bin/bash

set -ouex pipefail

# Disable negativo17 repo:
sed -i 's@enabled=1@enabled=0@g' "/etc/yum.repos.d/fedora-multimedia.repo"

# Disable all COPR repos:
for i in /etc/yum.repos.d/_copr:*.repo; do
	if [[ -f "$i" ]]; then
		sed -i 's@enabled=1@enabled=0@g' "$i"
	fi
done

# Compile the gschemas:
glib-compile-schemas /usr/share/glib-2.0/schemas

# Make fish default shell for new users:
sed -i "s|^SHELL=.*|SHELL=/usr/bin/fish|" /etc/default/useradd

# Default systemd target:
systemctl set-default graphical.target
