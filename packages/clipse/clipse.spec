Name:           clipse
Version:        1.2.0
Release:        %autorelease
Summary:        Clipboard manager for Wayland

License:        MIT
URL:            https://github.com/savedra1/clipse
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  git

%description
Clipse is a configurable clipboard manager for Wayland. It stores your
clipboard history and lets you quickly access it with an interactive TUI.

%prep
%autosetup

%build
CGO_ENABLED=0 go build -tags "wayland" -o %{name} .

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
