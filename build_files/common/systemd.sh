#!/bin/bash

set -ouex pipefail

systemctl enable --global foot-server.socket
systemctl enable dconf-update.service
systemctl enable --global gpg-agent{,-ssh}.socket
