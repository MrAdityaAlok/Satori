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

BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(pam)

BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(sdbus-c++)


%description
hyprlock is Hyprland's simple, yet multi-threaded and GPU-accelerated screen
locking utility. It uses the ext-session-lock protocol and features fractional
scaling support, GPU acceleration, blurred screenshots, etc.

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
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_datadir}/hypr/%{name}.conf

%changelog
%autochangelog
