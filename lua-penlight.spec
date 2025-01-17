Name:		lua-penlight
Version:	1.13.1
Release:	1
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/lunarmodules/Penlight
Source0:	https://github.com/lunarmodules/Penlight/archive/%{version}/Penlight-%{version}.tar.gz

%global luaver 5.4
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%bcond_with docs

BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
%if %{with docs}
BuildRequires:	lua-ldoc
%endif # with docs
Requires:	lua >= %{luaver}
Requires:	lua-filesystem

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global __requires_exclude_from %{_docdir}

%description
A set of pure Lua libraries focusing on input data handling (such as
reading configuration files), functional programming (such as map,
reduce, placeholder expressions, etc.), and OS path management. Much
of the functionality is inspired by the Python standard libraries.


%if %{with docs}
%package doc
Summary:	API docs for lua-penlight
Requires:	%{name} = %{version}-%{release}

%description doc
%{summary}
%endif # with docs


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

%if %{with docs}
# build and install docs
ldoc .
cp -av docs %{buildroot}%{_pkgdocdir}
%endif # with docs


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


%if %{with docs}
%files doc
%{_pkgdocdir}/docs
%endif # with docs


%files examples
%doc examples
