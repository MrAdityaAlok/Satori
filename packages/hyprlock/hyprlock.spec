%if 0%{?fedora} < 43
%global use_vendored_sdbus 1
%else
%global use_vendored_sdbus 0
%endif

Name:           hyprlock
Version:        0.9.2
Release:        %autorelease
Summary:        Hyprland's GPU-accelerated screen locking utility

%if %{use_vendored_sdbus}
License:        BSD-3-Clause AND LGPL-2.1
%else
License:        BSD-3-Clause
%endif

URL:            https://github.com/hyprwm/hyprlock
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if %{use_vendored_sdbus}
Source1:        https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v2.1.0.tar.gz
%endif

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

%if %{use_vendored_sdbus}
BuildRequires:  pkgconfig(libsystemd)
%else
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0.1
%endif

%if %{use_vendored_sdbus}
Provides:       bundled(sdbus-cpp) = 2.0.1
%endif

%description
hyprlock is Hyprland's simple, yet multi-threaded and GPU-accelerated screen
locking utility. It uses the ext-session-lock protocol and features fractional
scaling support, GPU acceleration, blurred screenshots, etc.

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

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_datadir}/hypr/%{name}.conf

%changelog
%autochangelog
