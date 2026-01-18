%global commit ba7877823a2fdf746e9ec7ca9bdd8f44fbb9fdc8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260104

Name:           matugen
Version:        3.1.0
Release:        %autorelease -s %{commitdate}git%{shortcommit}
Summary:        Material Design 3 color palette generator

License:        GPL-2.0
URL:            https://github.com/InioX/matugen
Source0:        %{url}/archive/%{commit}.tar.gz#/matugen-%{shortcommit}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo

%description
A tool to generate Material Design 3 color palette from an image.

%prep
%autosetup -n matugen-%{commit}

%build
cargo build --release --locked

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog