%if 0%{?fedora} < 43
%global use_vendored_sdbus 1
%else
%global use_vendored_sdbus 0
%endif

Name:           xdg-desktop-portal-hyprland
Version:        1.3.11
Release:        %autorelease
Summary:        xdg-desktop-portal backend for Hyprland

%if %{use_vendored_sdbus}
License:        BSD-3-Clause AND LGPL-2.1
%else
License:        BSD-3-Clause
%endif

URL:            https://github.com/hyprwm/xdg-desktop-portal-hyprland
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if %{use_vendored_sdbus}
Source1:        https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v2.1.0.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)

%if %{use_vendored_sdbus}
BuildRequires:  pkgconfig(libsystemd)
%else
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0.1
%endif

Requires:       dbus
Requires:       grim
Requires:       xdg-desktop-portal
Requires:       slurp
Requires:       qt6-qtwayland

%description
xdg-desktop-portal-hyprland is a backend implementation for xdg-desktop-portal
for Hyprland. It provides screencasting, screen sharing, and other desktop
portal functionalities using PipeWire and Wayland protocols.

%prep
%autosetup -p1

%if %{use_vendored_sdbus}
mkdir -p vendor_sdbus
tar -xf %{SOURCE1} -C vendor_sdbus --strip-components=1
%endif

%build
%if %{use_vendored_sdbus}
pushd vendor_sdbus
%cmake \
    -DCMAKE_INSTALL_PREFIX="%{_builddir}/sdbus" \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
cmake --install %{__cmake_builddir}
popd
export PKG_CONFIG_PATH="%{_builddir}/sdbus/lib64/pkgconfig:$PKG_CONFIG_PATH"
%endif

%cmake
%cmake_build

%install
%cmake_install

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprland-share-picker
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal
%{_libexecdir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
