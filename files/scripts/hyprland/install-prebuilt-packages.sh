#!/usr/bin/env bash

set -eou pipefail

_clipse() {
  latest_version="$(basename "$(curl -Ls -o /dev/null -w "%{url_effective}" https://github.com/savedra1/clipse/releases/latest)")"

  wget -O clipse.tar.gz \
    https://github.com/savedra1/clipse/releases/download/"$latest_version"/clipse_"${latest_version#v}"_linux_amd64.tar.gz
  tar xf clipse.tar.gz

  install -m0755 ./clipse /usr/bin/
}

_clipse
