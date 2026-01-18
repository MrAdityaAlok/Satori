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
Source1:        https://github.com/Kistler-Group/sdbus-cpp/archive/v2.0.1/sdbus-2.0.1.tar.gz
%endif

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
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)

%if %{use_vendored_sdbus}
BuildRequires:  pkgconfig(systemd)
%else
BuildRequires:  pkgconfig(sdbus-cpp) >= 2.0.1
%endif

%description
hyprlock is Hyprland's simple, yet multi-threaded and GPU-accelerated screen
locking utility. It uses the ext-session-lock protocol and features fractional
scaling support, GPU acceleration, blurred screenshots, native fingerprint
support via libfprint, and Hyprland's eyecandy features like gradient borders,
blur, animations, and shadows.

%prep
%autosetup -p1

%if %{use_vendored_sdbus}
mkdir -p vendor_sdbus
tar -xf %{SOURCE1} -C vendor_sdbus --strip-components=1
%endif

%build
%if %{use_vendored_sdbus}
pushd vendor_sdbus
cmake -B build -S . \
    -DCMAKE_INSTALL_PREFIX=$(pwd)/install \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Release
cmake --build build
cmake --install build
popd
export PKG_CONFIG_PATH="$(pwd)/vendor_sdbus/install/lib64/pkgconfig:$PKG_CONFIG_PATH"
%endif

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