#!/bin/bash

set -ouex pipefail

IMAGE_NAME="Satori"
IMAGE_PRETTY_NAME="Satori OS - ${VARIANT^} Edition (Based on Fedora Atomic)"

HOME_URL=https://github.com/MrAdityaAlok/Satori
DOCUMENTATION_URL=https://github.com/MrAdityaAlok/Satori
SUPPORT_URL=https://github.com/MrAdityaAlok/Satori/issues
BUG_SUPPORT_URL=https://github.com/MrAdityaAlok/Satori/issues

sed -i "s|^NAME=.*|NAME=\"$IMAGE_NAME\"|" /usr/lib/os-release
sed -i "s|^PRETTY_NAME=.*|PRETTY_NAME=\"$IMAGE_PRETTY_NAME\"|" /usr/lib/os-release

sed -i "s|^DEFAULT_HOSTNAME=.*|DEFAULT_HOSTNAME=\"${IMAGE_NAME,}\"|" /usr/lib/os-release

sed -i "s|^HOME_URL=.*|HOME_URL=\"$HOME_URL\"|" /usr/lib/os-release
sed -i "s|^DOCUMENTATION_URL=.*|DOCUMENTATION_URL=\"$DOCUMENTATION_URL\"|" /usr/lib/os-release
sed -i "s|^SUPPORT_URL=.*|SUPPORT_URL=\"$SUPPORT_URL\"|" /usr/lib/os-release
sed -i "s|^BUG_REPORT_URL=.*|BUG_REPORT_URL=\"$BUG_SUPPORT_URL\"|" /usr/lib/os-release

echo -e "Satori OS \S \nKernel \r on an \m\n" >/etc/issue
