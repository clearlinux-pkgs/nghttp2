#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x7E8403D5D673C366 (tatsuhiro.t@gmail.com)
#
Name     : nghttp2
Version  : 1.57.0
Release  : 79
URL      : https://github.com/nghttp2/nghttp2/releases/download/v1.57.0/nghttp2-1.57.0.tar.xz
Source0  : https://github.com/nghttp2/nghttp2/releases/download/v1.57.0/nghttp2-1.57.0.tar.xz
Source1  : https://github.com/nghttp2/nghttp2/releases/download/v1.57.0/nghttp2-1.57.0.tar.xz.asc
Summary  : HTTP/2 C library
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: nghttp2-data = %{version}-%{release}
Requires: nghttp2-lib = %{version}-%{release}
Requires: nghttp2-license = %{version}-%{release}
Requires: nghttp2-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-configure
BuildRequires : c-ares-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libev-dev
BuildRequires : libevent-dev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : nghttp3-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32cunit)
BuildRequires : pkgconfig(32libevent_openssl)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(32openssl)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libevent_openssl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-cython
BuildRequires : python3-dev
BuildRequires : xz-dev
BuildRequires : xz-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package data
Summary: data components for the nghttp2 package.
Group: Data

%description data
data components for the nghttp2 package.


%package dev
Summary: dev components for the nghttp2 package.
Group: Development
Requires: nghttp2-lib = %{version}-%{release}
Requires: nghttp2-data = %{version}-%{release}
Provides: nghttp2-devel = %{version}-%{release}
Requires: nghttp2 = %{version}-%{release}

%description dev
dev components for the nghttp2 package.


%package dev32
Summary: dev32 components for the nghttp2 package.
Group: Default
Requires: nghttp2-lib32 = %{version}-%{release}
Requires: nghttp2-data = %{version}-%{release}
Requires: nghttp2-dev = %{version}-%{release}

%description dev32
dev32 components for the nghttp2 package.


%package doc
Summary: doc components for the nghttp2 package.
Group: Documentation
Requires: nghttp2-man = %{version}-%{release}

%description doc
doc components for the nghttp2 package.


%package lib
Summary: lib components for the nghttp2 package.
Group: Libraries
Requires: nghttp2-data = %{version}-%{release}
Requires: nghttp2-license = %{version}-%{release}

%description lib
lib components for the nghttp2 package.


%package lib32
Summary: lib32 components for the nghttp2 package.
Group: Default
Requires: nghttp2-data = %{version}-%{release}
Requires: nghttp2-license = %{version}-%{release}

%description lib32
lib32 components for the nghttp2 package.


%package license
Summary: license components for the nghttp2 package.
Group: Default

%description license
license components for the nghttp2 package.


%package man
Summary: man components for the nghttp2 package.
Group: Default

%description man
man components for the nghttp2 package.


%prep
%setup -q -n nghttp2-1.57.0
cd %{_builddir}/nghttp2-1.57.0
pushd ..
cp -a nghttp2-1.57.0 build32
popd
pushd ..
cp -a nghttp2-1.57.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697035248
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --disable-python-bindings
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --disable-python-bindings   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static --disable-python-bindings
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697035248
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nghttp2
cp %{_builddir}/nghttp2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nghttp2/7f6f3c0c08925232459e499d66231cb5da01d811 || :
cp %{_builddir}/nghttp2-%{version}/doc/_exts/rubydomain/LICENSE.rubydomain %{buildroot}/usr/share/package-licenses/nghttp2/2e3d96196666de3d8582c67fcdc7804f28e1fe0c || :
cp %{_builddir}/nghttp2-%{version}/third-party/mruby/LICENSE %{buildroot}/usr/share/package-licenses/nghttp2/9fefc4e028cc4f57e5c16215272cf6cc255782d0 || :
cp %{_builddir}/nghttp2-%{version}/third-party/mruby/mrbgems/mruby-set/LICENSE %{buildroot}/usr/share/package-licenses/nghttp2/0c4ccf74e38a75e48fd6907a13b1c386ca15404f || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/nghttp2/fetch-ocsp-response

%files dev
%defattr(-,root,root,-)
/usr/include/nghttp2/nghttp2.h
/usr/include/nghttp2/nghttp2ver.h
/usr/lib64/libnghttp2.so
/usr/lib64/pkgconfig/libnghttp2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnghttp2.so
/usr/lib32/pkgconfig/32libnghttp2.pc
/usr/lib32/pkgconfig/libnghttp2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/nghttp2/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libnghttp2.so.14.25.0
/usr/lib64/libnghttp2.so.14
/usr/lib64/libnghttp2.so.14.25.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnghttp2.so.14
/usr/lib32/libnghttp2.so.14.25.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nghttp2/0c4ccf74e38a75e48fd6907a13b1c386ca15404f
/usr/share/package-licenses/nghttp2/2e3d96196666de3d8582c67fcdc7804f28e1fe0c
/usr/share/package-licenses/nghttp2/7f6f3c0c08925232459e499d66231cb5da01d811
/usr/share/package-licenses/nghttp2/9fefc4e028cc4f57e5c16215272cf6cc255782d0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/h2load.1
/usr/share/man/man1/nghttp.1
/usr/share/man/man1/nghttpd.1
/usr/share/man/man1/nghttpx.1
