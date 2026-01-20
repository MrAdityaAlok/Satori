Name:           xdg-desktop-portal-hyprland
Version:        1.3.11
Release:        %autorelease
Summary:        xdg-desktop-portal backend for Hyprland

License:        BSD-3-Clause

URL:            https://github.com/hyprwm/xdg-desktop-portal-hyprland
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
# hyprland-share-picker:
BuildRequires:  pkgconfig(Qt6Widgets)

BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(sdbus-c++)

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

%build
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
