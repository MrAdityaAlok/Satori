Name:           app2unit
Version:        1.2.1
Release:        %autorelease
Summary:        Convert .desktop files to systemd units

License:        MIT
URL:            https://github.com/Vladimir-csp/app2unit
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  scdoc

Requires:       bash

%description
app2unit converts .desktop files to systemd units. It generates either
user or system units from XDG .desktop files, making it easy to run
graphical applications as systemd services.

%prep
%autosetup

%build
# Script-based package.

%install
make install prefix=%{_prefix} DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/app2unit
%{_bindir}/app2unit-open
%{_bindir}/app2unit-open-scope
%{_bindir}/app2unit-open-service
%{_bindir}/app2unit-term
%{_bindir}/app2unit-term-scope
%{_bindir}/app2unit-term-service
%{_mandir}/man1/app2unit.1.gz

%changelog
%autochangelog
