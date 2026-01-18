Name:           hyprtoolkit
Version:        0.5.2
Release:        %autorelease
Summary:        A modern C++ Wayland-native GUI toolkit

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprtoolkit
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary} for Hyprland.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(aquamarine)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(hyprgraphics)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.5

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
