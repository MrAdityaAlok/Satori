Name:           hyprpolkitagent
Version:        0.1.3
Release:        %autorelease
Summary:        A polkit authentication agent written in Qt/QML

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpolkitagent
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-qt6-1)

BuildRequires:  pkgconfig(hyprutils)

%description
hyprpolkitagent is a simple polkit authentication agent for Hyprland, written
in Qt6/QML. It provides a graphical interface for privilege escalation
requests, integrating seamlessly with the Hyprland desktop environment.

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
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.hyprland.%{name}.service
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
