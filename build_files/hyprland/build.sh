#!/bin/bash

set -oeux pipefail

/ctx/hyprland/packages.sh

rsync -rvK /ctx/sys_files/hyprland/ /

/ctx/hyprland/systemd.sh
