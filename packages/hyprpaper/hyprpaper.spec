Name:           hyprpaper
Version:        0.8.1
Release:        %autorelease
Summary:        A Wayland wallpaper utility with IPC controls

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpaper
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(glesv2)

BuildRequires:  pkgconfig(libmagic)

BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprtoolkit)
BuildRequires:  pkgconfig(hyprwire)
BuildRequires:  pkgconfig(hyprwayland-scanner)

%description
hyprpaper is a blazing fast wayland wallpaper utility with the ability to
dynamically change wallpapers through sockets. Features per-output wallpapers,
multiple fill modes (fill, tile, cover, contain), fractional scaling support,
and IPC for fast wallpaper switches.

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
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
