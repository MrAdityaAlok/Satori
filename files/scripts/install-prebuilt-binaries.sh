#!/usr/bin/env bash

set -eou pipefail

_eza() {
  wget -O eza.tar.gz \
    https://github.com/eza-community/eza/releases/latest/download/eza_x86_64-unknown-linux-gnu.tar.gz
  tar xf eza.tar.gz

  install -m0755 ./eza /usr/bin/
}

_neovide() {
  wget -O neovide.tar.gz \
    https://github.com/neovide/neovide/releases/latest/download/neovide-linux-x86_64.tar.gz
  tar xf neovide.tar.gz

  wget -O neovide.desktop \
    https://raw.githubusercontent.com/neovide/neovide/refs/heads/main/assets/neovide.desktop

  wget -O neovide.svg \
    https://raw.githubusercontent.com/neovide/neovide/refs/heads/main/assets/neovide.svg

  install -m0755 ./neovide /usr/bin/
  install -m0644 ./neovide.desktop /usr/share/applications/
  install -m0644 ./neovide.svg /usr/share/icons/hicolor/scalable/apps/
}

_eza
_neovide
