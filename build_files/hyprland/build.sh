#!/bin/bash

set -oeux pipefail

/ctx/hyprland/packages.sh
/ctx/hyprland/systemd.sh

rsync -rvK /ctx/sys_files/hyprland/ /
