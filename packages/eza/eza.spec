Name:           eza
Version:        0.23.4
Release:        %autorelease
Summary:        A modern replacement for ls

License:        EUPL-1.2
URL:            https://github.com/eza-community/eza
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pandoc

%description
eza is a modern, maintained replacement for ls with better defaults and
extra features. It uses colours to distinguish file types and metadata,
knows about symlinks, extended attributes, and Git.

%prep
%autosetup

%build
LIBGIT2_NO_VENDOR=1 cargo build --release --locked

%install
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Man pages:
mkdir target/man
for page in eza.1 eza_colors.5 eza_colors-explanation.5; do
    sed "s/\$version/v%{version}/g" "man/${page}.md" | pandoc --standalone -f markdown -t man > "target/man/${page}"
done
install -Dpm 0644 target/man/eza.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/man/eza_colors.5 -t %{buildroot}/%{_mandir}/man5/
install -Dpm 0644 target/man/eza_colors-explanation.5 -t %{buildroot}/%{_mandir}/man5/

# Shell completions:
install -Dpm 0644 completions/bash/%{name} -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 completions/fish/%{name}.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 completions/zsh/_%{name} -t %{buildroot}/%{zsh_completions_dir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/eza.1*
%{_mandir}/man5/eza_colors.5*
%{_mandir}/man5/eza_colors-explanation.5*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%changelog
%autochangelog