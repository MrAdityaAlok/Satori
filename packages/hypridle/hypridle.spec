%if 0%{?fedora} < 43
%global use_vendored_sdbus 1
%else
%global use_vendored_sdbus 0
%endif

Name:           hypridle
Version:        0.1.7
Release:        %autorelease
Summary:        Hyprland's idle daemon

%if %{use_vendored_sdbus}
License:        BSD-3-Clause AND LGPL-2.1
%else
License:        BSD-3-Clause
%endif

URL:            https://github.com/hyprwm/hypridle
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if %{use_vendored_sdbus}
Source1:        https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v2.1.0.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)

%if %{use_vendored_sdbus}
BuildRequires:  pkgconfig(libsystemd)
%else
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0.1
%endif

%if %{use_vendored_sdbus}
Provides:       bundled(sdbus-cpp) = 2.0.1
%endif

%description
hypridle is Hyprland's idle management daemon. It uses the ext-idle-notify-v1
Wayland protocol to monitor user activity and can trigger actions based on
idle/active events, such as dimming the screen or locking the session.

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
%{_datadir}/hypr/%{name}.conf

%changelog
%autochangelog
