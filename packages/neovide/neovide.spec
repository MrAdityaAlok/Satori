Name:           neovide
Version:        0.15.2
Release:        %autorelease
Summary:        No Nonsense Neovim Client in Rust

License:        MIT
URL:            https://github.com/neovide/neovide
Source0:        %{url}/archive/%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(sdl2)

Requires:       neovim >= 0.10.0

%description
Neovide is a simple graphical user interface for Neovim. It provides a
snappy and feature-rich GUI for Neovim including ligatures, animated
cursor, smooth scrolling, and emoji support.

%prep
%autosetup

%build
cargo build --release --locked --features embed-fonts

%install
install -Dm755 target/release/neovide %{buildroot}%{_bindir}/neovide

install -Dm644 assets/neovide.desktop %{buildroot}%{_datadir}/applications/neovide.desktop

install -Dm644 assets/neovide.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/neovide.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications assets/neovide.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/neovide.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/neovide
%{_datadir}/applications/neovide.desktop
%{_datadir}/icons/hicolor/scalable/apps/neovide.svg

%changelog
%autochangelog