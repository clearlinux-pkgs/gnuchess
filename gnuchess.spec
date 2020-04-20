#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x43AC7FF93CED5A6B (aceballos@gmail.com)
#
Name     : gnuchess
Version  : 6.2.6
Release  : 5
URL      : https://ftp.gnu.org/gnu/chess/gnuchess-6.2.6.tar.gz
Source0  : https://ftp.gnu.org/gnu/chess/gnuchess-6.2.6.tar.gz
Source1  : https://ftp.gnu.org/gnu/chess/gnuchess-6.2.6.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnuchess-bin = %{version}-%{release}
Requires: gnuchess-data = %{version}-%{release}
Requires: gnuchess-info = %{version}-%{release}
Requires: gnuchess-license = %{version}-%{release}
Requires: gnuchess-locales = %{version}-%{release}
Requires: gnuchess-man = %{version}-%{release}
BuildRequires : flex
BuildRequires : ncurses-dev
BuildRequires : readline-dev

%description
GNU Chess Project
For latest information visit:
http://www.gnu.org/software/chess/

%package bin
Summary: bin components for the gnuchess package.
Group: Binaries
Requires: gnuchess-data = %{version}-%{release}
Requires: gnuchess-license = %{version}-%{release}

%description bin
bin components for the gnuchess package.


%package data
Summary: data components for the gnuchess package.
Group: Data

%description data
data components for the gnuchess package.


%package info
Summary: info components for the gnuchess package.
Group: Default

%description info
info components for the gnuchess package.


%package license
Summary: license components for the gnuchess package.
Group: Default

%description license
license components for the gnuchess package.


%package locales
Summary: locales components for the gnuchess package.
Group: Default

%description locales
locales components for the gnuchess package.


%package man
Summary: man components for the gnuchess package.
Group: Default

%description man
man components for the gnuchess package.


%prep
%setup -q -n gnuchess-6.2.6
cd %{_builddir}/gnuchess-6.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587412854
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1587412854
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnuchess
cp %{_builddir}/gnuchess-6.2.6/COPYING %{buildroot}/usr/share/package-licenses/gnuchess/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang gnuchess

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnuchess
/usr/bin/gnuchessu
/usr/bin/gnuchessx

%files data
%defattr(-,root,root,-)
/usr/share/games/plugins/logos/gnuchess.png
/usr/share/games/plugins/xboard/gnuchess.eng
/usr/share/gnuchess/gnuchess.ini
/usr/share/gnuchess/smallbook.bin

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gnuchess.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnuchess/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnuchess.1

%files locales -f gnuchess.lang
%defattr(-,root,root,-)

