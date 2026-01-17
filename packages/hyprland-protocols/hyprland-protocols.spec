%global commit 3f3860b869014c00e8b9e0528c7b4ddc335c21ab
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           hyprland-protocols
Version:        0.6.2
Release:        %autorelease
Summary:        Wayland protocol extensions for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc

%description
Wayland protocols used by Hyprland and its ecosystem.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains XML protocol files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md

%files devel
%{_datadir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog