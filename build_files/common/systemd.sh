#!/bin/bash

set -ouex pipefail

systemctl enable podman.socket
systemctl enable --global foot-server.socket
systemctl enable dconf-update.service
