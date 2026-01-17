%global commit 541628cebe42792ddf5063c4abd6402c2f1bd68f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20260114

Name:           grimblast
Version:        0.1.0
Release:        %autorelease -s %{date}git%{shortcommit}
Summary:        A screenshot utility for Hyprland

License:        MIT
URL:            https://github.com/hyprwm/contrib
Source0:        %{url}/raw/%{commit}/grimblast/grimblast

BuildArch:      noarch

Requires:       grim
Requires:       slurp
Requires:       wl-clipboard
Requires:       jq
Requires:       libnotify

%description
Grimblast is an easy-to-use screenshot utility for Hyprland.
It provides a wrapper for grim and slurp with added functionality
like copying to clipboard, saving to file, and notifications.

%prep
%setup -c -T
cp %{SOURCE0} grimblast

%build
# Shell script.

%install
install -Dm755 grimblast %{buildroot}%{_bindir}/grimblast

%files
%{_bindir}/grimblast

%changelog
%autochangelog