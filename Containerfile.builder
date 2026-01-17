FROM fedora:43

RUN dnf install -y rpm-build rpmdevtools dnf-plugins-core git cmake gcc-c++ ninja-build meson \
    rust cargo golang wget rpmautospec rpmlint createrepo_c \
    # Common build deps to speed up:
    "pkgconfig(wayland-client)" "pkgconfig(wayland-protocols)" "pkgconfig(cairo)" \
    "pkgconfig(pango)" "pkgconfig(libdrm)" "pkgconfig(gbm)" \
    && dnf clean all

RUN mkdir -p /root/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
WORKDIR /packages

COPY packages/build.sh /usr/local/bin/build-packages
RUN chmod +x /usr/local/bin/build-packages
