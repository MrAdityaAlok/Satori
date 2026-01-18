Name:           hyprlock
Version:        0.9.2
Release:        %autorelease
Summary:        Hyprland's GPU-accelerated screen locking utility

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprlock
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)

%description
hyprlock is Hyprland's simple, yet multi-threaded and GPU-accelerated screen
locking utility. It uses the ext-session-lock protocol and features fractional
scaling support, GPU acceleration, blurred screenshots, native fingerprint
support via libfprint, and Hyprland's eyecandy features like gradient borders,
blur, animations, and shadows.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprlock
%config(noreplace) %{_sysconfdir}/pam.d/hyprlock
%{_datadir}/hypr/hyprlock.conf

%changelog
%autochangelog