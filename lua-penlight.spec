Name:		lua-penlight
Version:	1.13.1
Release:	1
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/lunarmodules/Penlight
Source0:	https://github.com/lunarmodules/Penlight/archive/%{version}/Penlight-%{version}.tar.gz

%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
Requires:	lua >= %{luaver}
Requires:	lua-filesystem

%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions, etc.), and OS path management. Much
of the functionality is inspired by the Python standard libraries.


%package examples
Summary:	Examples of lua-penlight usage
Requires:	%{name} = %{version}-%{release}

%description examples
%{summary}


%prep
%setup -q -n Penlight-%{version}


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}

# fix scripts
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua


%check
# currently disabled: missing luacov
# LUA_PATH="%%{buildroot}%%{luapkgdir}/?/init.lua;%%{buildroot}%%{luapkgdir}/?.lua;;" \
# lua run.lua tests


%files
%license LICENSE.md
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%{luapkgdir}/pl


%files examples
%doc examples
