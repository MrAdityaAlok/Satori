Name:           hyprqt6engine
Version:        0.1.0
Release:        %autorelease
Summary:        Qt6 Theme Provider for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprqt6engine
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         0001-fix-qt6-guiprivate.diff

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6BuildInternals)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)

%description
hyprqt6engine is a Qt6 QML rendering backend for Hyprland applications,
providing native Qt6/KF6 integration for Hyprland utilities.

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
%{_libdir}/lib%{name}-common.so
%{_qt6_plugindir}/platformthemes/lib%{name}.so
%{_qt6_plugindir}/styles/libhypr-style.so

%changelog
%autochangelog
