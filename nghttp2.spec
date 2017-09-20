#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nghttp2
Version  : 1.26.0
Release  : 25
URL      : https://github.com/nghttp2/nghttp2/releases/download/v1.26.0/nghttp2-1.26.0.tar.xz
Source0  : https://github.com/nghttp2/nghttp2/releases/download/v1.26.0/nghttp2-1.26.0.tar.xz
Summary  : HTTP/2 C library
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: nghttp2-lib
Requires: nghttp2-doc
Requires: nghttp2-data
BuildRequires : boost-dev
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : go
BuildRequires : libevent-dev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
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
BuildRequires : python-dev
BuildRequires : xz-dev
BuildRequires : xz-dev32

%description


%package data
Summary: data components for the nghttp2 package.
Group: Data

%description data
data components for the nghttp2 package.


%package dev
Summary: dev components for the nghttp2 package.
Group: Development
Requires: nghttp2-lib
Requires: nghttp2-data
Provides: nghttp2-devel

%description dev
dev components for the nghttp2 package.


%package dev32
Summary: dev32 components for the nghttp2 package.
Group: Default
Requires: nghttp2-lib32
Requires: nghttp2-data
Requires: nghttp2-dev

%description dev32
dev32 components for the nghttp2 package.


%package doc
Summary: doc components for the nghttp2 package.
Group: Documentation

%description doc
doc components for the nghttp2 package.


%package lib
Summary: lib components for the nghttp2 package.
Group: Libraries
Requires: nghttp2-data

%description lib
lib components for the nghttp2 package.


%package lib32
Summary: lib32 components for the nghttp2 package.
Group: Default
Requires: nghttp2-data

%description lib32
lib32 components for the nghttp2 package.


%prep
%setup -q -n nghttp2-1.26.0
pushd ..
cp -a nghttp2-1.26.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505940194
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505940194
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

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
%defattr(-,root,root,-)
%doc /usr/share/doc/nghttp2/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnghttp2.so.14
/usr/lib64/libnghttp2.so.14.14.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnghttp2.so.14
/usr/lib32/libnghttp2.so.14.14.0
