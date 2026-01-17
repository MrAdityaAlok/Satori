Name:           glaze
Version:        6.1.0
Release:        %autorelease
Summary:        Extremely fast, in memory, JSON and reflection library for modern C++

License:        MIT
URL:            https://github.com/stephenberry/glaze
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Glaze is an extremely fast, in memory, JSON and reflection library for modern
C++. It supports BEVE, CBOR, CSV, MessagePack, TOML, and EETF formats with
compile time reflection for MSVC, Clang, and GCC.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Header-only development files for %{name}.

%prep
%autosetup -p1

%build
# Disable developer mode to avoid FetchContent for tests
# Override cmake install dir to standard location for find_package
%cmake -Dglaze_DEVELOPER_MODE:BOOL=OFF -DBUILD_TESTING:BOOL=OFF \
       -Dglaze_INSTALL_CMAKEDIR=%{_datadir}/cmake/glaze

%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/glaze/
%{_datadir}/cmake/glaze/

%changelog
%autochangelog