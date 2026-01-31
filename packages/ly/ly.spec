%global selinuxtype targeted
%bcond_without selinux

%global commit 7934060d3bd8d87acdf8eef38e3b0d01bc02a62b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260129

Name:           ly
Version:        1.3.1
Release:        %autorelease -s %{commitdate}git%{shortcommit}
Summary:        A lightweight TUI (ncurses-like) display manager

License:        WTFPL
URL:            https://codeberg.org/fairyglade/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz

Source1:        %{name}.te
Source2:        %{name}.fc

BuildRequires:  zig
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pam)

Requires:       brightnessctl
%if %{with selinux}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif


%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD.

%if %{with selinux}
%package selinux
Summary:        SELinux policy for Ly
BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildRequires:  checkpolicy
%{?selinux_requires}

%description selinux
SELinux policy for Ly display manager.
%endif

%prep
%autosetup -n %{name}
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
zig build \
    --build-id=sha1 \
    -Dinit_system=systemd \
    -Denable_x11_support=false \
    -Doptimize=ReleaseSafe

%if %{with selinux}
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%endif

%install
zig build installexe \
    -Dinit_system=systemd \
    -Denable_x11_support=false \
    -Doptimize=ReleaseSafe \
    -Ddest_directory=%{buildroot} \
    -Dprefix_directory=%{_prefix} \
    -Dconfig_directory=%{_sysconfdir}



%if %{with selinux}
install -D -m 644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%endif

%files
%license license.md
%doc readme.md
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/
%{_sysconfdir}/pam.d/%{name}
%{_sysconfdir}/pam.d/%{name}-autologin
%{_unitdir}/%{name}@.service

%if %{with selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/ly

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ $1 -le 1 ]; then
    restorecon -R %{_sysconfdir}/%{name} %{_bindir}/%{name} %{_sysconfdir}/pam.d/%{name}* 2>/dev/null || :
    [ -f /var/log/%{name}.log ] && restorecon /var/log/%{name}.log || :
fi

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%changelog
%autochangelog
