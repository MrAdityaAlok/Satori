#!/usr/bin/env bash

set -eou pipefail

# Hide Desktop Files (Hidden removes mime associations):
for file in fish btop; do
  if [[ -f "/usr/share/applications/$file.desktop" ]]; then
    sed -i 's@\[Desktop Entry\]@\[Desktop Entry\]\nHidden=true@g' /usr/share/applications/"$file".desktop
  fi
done
