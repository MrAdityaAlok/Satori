#!/bin/bash

set -ouex pipefail

_clipse() {
	latest_version="$(basename "$(curl -Ls -o /dev/null -w "%{url_effective}" https://github.com/savedra1/clipse/releases/latest)")"

	wget -O clipse.tar.gz \
		https://github.com/savedra1/clipse/releases/download/"$latest_version"/clipse_"${latest_version}"_linux_wayland_amd64.tar.gz
	tar xf clipse.tar.gz

	install -m0755 ./clipse-linux-wayland-amd64 /usr/bin/clipse
}

_app2unit() {
	git clone https://github.com/Vladimir-csp/app2unit.git
	dnf5 -y install scdoc
	make --directory=app2unit install
	dnf5 -y remove scdoc
}

(
	cd /tmp/
	_clipse
	_app2unit
)
