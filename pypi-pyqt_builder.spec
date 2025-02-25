#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v7
# autospec commit: f56f1fa18daa
#
Name     : pypi-pyqt_builder
Version  : 1.15.4
Release  : 24
URL      : https://files.pythonhosted.org/packages/c0/75/a3384eea8770c17e77821368618a5140c4ae0c37f9c05a84ef55f4807172/PyQt-builder-1.15.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/75/a3384eea8770c17e77821368618a5140c4ae0c37f9c05a84ef55f4807172/PyQt-builder-1.15.4.tar.gz
Summary  : The PEP 517 compliant PyQt build system
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: pypi-pyqt_builder-bin = %{version}-%{release}
Requires: pypi-pyqt_builder-license = %{version}-%{release}
Requires: pypi-pyqt_builder-python = %{version}-%{release}
Requires: pypi-pyqt_builder-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: deps.patch
Patch2: shared-python.patch

%description
PyQt-builder - The PEP 517 Compliant PyQt Build System
======================================================

%package bin
Summary: bin components for the pypi-pyqt_builder package.
Group: Binaries
Requires: pypi-pyqt_builder-license = %{version}-%{release}

%description bin
bin components for the pypi-pyqt_builder package.


%package license
Summary: license components for the pypi-pyqt_builder package.
Group: Default

%description license
license components for the pypi-pyqt_builder package.


%package python
Summary: python components for the pypi-pyqt_builder package.
Group: Default
Requires: pypi-pyqt_builder-python3 = %{version}-%{release}

%description python
python components for the pypi-pyqt_builder package.


%package python3
Summary: python3 components for the pypi-pyqt_builder package.
Group: Default
Requires: python3-core
Provides: pypi(pyqt_builder)
Requires: pypi(packaging)
Requires: pypi(sip)
Provides: pypi(pyqtbuild)

%description python3
python3 components for the pypi-pyqt_builder package.


%prep
%setup -q -n PyQt-builder-1.15.4
cd %{_builddir}/PyQt-builder-1.15.4
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a PyQt-builder-1.15.4 buildavx2
popd
pushd ..
cp -a PyQt-builder-1.15.4 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712092446
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd
pushd ../buildapx/
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder
cp %{_builddir}/PyQt-builder-%{version}/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/2136dbc93e95a70deae070e44ff6b2702ec1599c || :
cp %{_builddir}/PyQt-builder-%{version}/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/34e9b06e7f12eaed676f57481de931ec91c6ce0a || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
pushd ../buildapx/
CC=gcc-14
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -mapxf -mavx10.1 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-va dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-32/concrt140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-32/msvcp140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-32/msvcp140_1.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-32/msvcp140_2.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-32/vcruntime140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/concrt140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/msvcp140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/msvcp140_1.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/msvcp140_2.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/vcruntime140.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/msvc-64/vcruntime140_1.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/openssl-32/libcrypto-1_1.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/openssl-32/libssl-1_1.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/openssl-64/libcrypto-1_1-x64.dll
rm -f %{buildroot}*/usr/lib/python3.12/site-packages/pyqtbuild/bundle/dlls/openssl-64/libssl-1_1-x64.dll
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyqt-bundle
/usr/bin/pyqt-qt-wheel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyqt_builder/2136dbc93e95a70deae070e44ff6b2702ec1599c
/usr/share/package-licenses/pypi-pyqt_builder/34e9b06e7f12eaed676f57481de931ec91c6ce0a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
