%if 0%{?fedora} < 43
%global use_vendored_xkbcommon 1
%else
%global use_vendored_xkbcommon 0
%endif

Name:           hyprland
Version:        0.53.1
Release:        %autorelease
Summary:        An independent, highly customizable, dynamic tiling Wayland compositor

%if %{use_vendored_xkbcommon}
License:        BSD-3-Clause AND MIT AND BSD-2-Clause AND HPND-sell-variant AND LGPL-2.1-or-later
%else
License:        BSD-3-Clause AND BSD-2-Clause AND HPND-sell-variant AND LGPL-2.1-or-later
%endif

URL:            https://github.com/hyprwm/Hyprland
Source0:        %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

%if %{use_vendored_xkbcommon}
Source1:        https://github.com/xkbcommon/libxkbcommon/archive/xkbcommon-1.11.0/libxkbcommon-1.11.0.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  glaze-devel
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(muparser)

%if %{use_vendored_xkbcommon}
BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  byacc
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  libxml2-devel
%else
BuildRequires:  pkgconfig(xkbcommon) >= 1.11.0
%endif

BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(hyprcursor)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprwire)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)

Requires:       polkit
Requires:       xorg-x11-server-Xwayland%{?_isa}

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice on
its looks. It supports multiple layouts, fancy effects, has a very flexible
IPC model allowing for a lot of customization, a powerful plugin system and
more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing plugins and tools for %{name}.

%prep
%autosetup -p1 -n %{name}-source

%if %{use_vendored_xkbcommon}
mkdir -p subprojects/libxkbcommon
tar -xf %{SOURCE1} -C subprojects/libxkbcommon --strip-components=1
%endif

%build
%if %{use_vendored_xkbcommon}
pushd subprojects/libxkbcommon
%meson \
    -Denable-tools=false \
    -Ddefault_library=static
%meson_build
DESTDIR="%{_builddir}/libxkbcommon" meson install -C %{_vpath_builddir} --no-rebuild
popd
export PKG_CONFIG_PATH="%{_builddir}/libxkbcommon/usr/lib64/pkgconfig:$PKG_CONFIG_PATH"
%global optflags %{optflags} -I%{_builddir}/libxkbcommon/%{_includedir} -L%{_builddir}/libxkbcommon/%{_libdir}
%endif

%cmake

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/[Hh]yprland
%{_bindir}/hyprctl
%{_bindir}/hyprpm
%{_bindir}/start-hyprland
%{_datadir}/hypr/
%{_datadir}/wayland-sessions/hyprland-uwsm.desktop
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/xdg-desktop-portal/hyprland-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel
%{_includedir}/hyprland/
%{_datadir}/pkgconfig/hyprland.pc

%changelog
%autochangelog
