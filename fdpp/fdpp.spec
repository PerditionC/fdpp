#
# spec file for package fdpp
#

Name: fdpp
Version: 0.1
Release: 1%{?dist}
Summary: DOS compatibility layer

Group: System/Emulator

License: GPL-3.0+
URL: www.github.com/stsp/fdpp
Source0: %{name}-%{version}.tar.gz

BuildRequires: bison
BuildRequires: flex
BuildRequires: sed
BuildRequires: bash
BuildRequires: clang
BuildRequires: libstdc++-devel

%description
fdpp provides the DOS compatibility layer.
It is a FreeDOS port to modern C++.

%prep
%setup -q

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%check

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} install

%files
%defattr(-,root,root)
%{_libdir}/libfdpp.so
%{_includedir}/fdpp/thunks.h
%{_datadir}/fdpp/fdppkrnl.sys

%changelog
