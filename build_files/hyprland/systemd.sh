#!/bin/bash

set -ouex pipefail

systemctl enable --global waybar.service

systemctl enable --global hypridle.service
systemctl enable --global hyprpaper.service
systemctl enable --global hyprpolkitagent.service
