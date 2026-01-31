Name:           impala
Version:        0.7.2
Release:        %autorelease
Summary:        TUI for managing wifi on Linux

License:        GPLv3
URL:            https://github.com/pythops/impala
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo

Requires:       iwd

%description
Impala is a TUI for managing wifi on Linux using iwd.

%prep
%autosetup -n impala-%{version}

%build
cargo build --release --locked

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc Readme.md
%{_bindir}/%{name}

%changelog
%autochangelog
