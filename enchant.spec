Name:           enchant
Version:        1.6.0
Release:        22
Epoch:          1
Summary:        Generic spell checking library

License:        LGPLv2+
URL:            https://github.com/AbiWord/enchant
Source0:        ftp://ftp.netbsd.org/pub/pkgsrc/distfiles/%{name}-%{version}.tar.gz

BuildRequires:  aspell-devel automake gcc-c++ hunspell-devel libtool libvoikko-devel
BuildRequires:  glib2-devel >= 2.6.0

%description
Enchant aims to provide a simple but comprehensive abstraction for dealing
with different spell checking libraries in a consistent way. A client, such
as a text editor or word processor, need not know anything about a specific
spell-checker, and since all back-ends are plugins, new spell-checkers can
be added without needing any change to the program using Enchant.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       glib2-devel

%description    devel
The %{name}-devel package contains libraries, header files and support files
for developing applications that use libenchant.

%package        aspell
Summary:        Aspell is integrated for libenchant
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    aspell
Applications need libraries integrated by using libenchant with aspell.

%package        voikko
Summary:        voikko is integrated for libenchant
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    voikko
Applications need libraries integrated by using libenchant with voikko.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --disable-ispell --disable-hspell --disable-zemberek --enable-myspell \
           --with-myspell-dir=/usr/share/myspell
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%delete_la
%ldconfig_scriptlets

%files
%doc COPYING.LIB AUTHORS
%{_bindir}/enchant
%{_bindir}/enchant-lsmod
%{_libdir}/libenchant.so.*
%{_libdir}/enchant/libenchant_myspell.so
%{_datadir}/enchant/enchant.ordering

%files devel
%{_libdir}/libenchant.so
%{_libdir}/pkgconfig/enchant.pc
%{_includedir}/enchant/*.h
%{_libdir}/*.a
%{_libdir}/%{name}/*.a

%files aspell
%{_libdir}/enchant/libenchant_aspell.so

%files voikko
%{_libdir}/enchant/libenchant_voikko.so

%files help
%doc README
%{_mandir}/man1/*.gz

%changelog
* Thu Aug 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:1.6.0-22
- Package Init

