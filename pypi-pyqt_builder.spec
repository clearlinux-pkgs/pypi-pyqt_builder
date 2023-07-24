#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pyqt_builder
Version  : 1.15.2
Release  : 15
URL      : https://files.pythonhosted.org/packages/cb/f0/dc998da4a3358249a0e53927c831a52bfc2aa070a96e8164fffcf3dce349/PyQt-builder-1.15.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/f0/dc998da4a3358249a0e53927c831a52bfc2aa070a96e8164fffcf3dce349/PyQt-builder-1.15.2.tar.gz
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
%setup -q -n PyQt-builder-1.15.2
cd %{_builddir}/PyQt-builder-1.15.2
%patch -P 1 -p1
pushd ..
cp -a PyQt-builder-1.15.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690211955
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder
cp %{_builddir}/PyQt-builder-%{version}/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/2136dbc93e95a70deae070e44ff6b2702ec1599c || :
cp %{_builddir}/PyQt-builder-%{version}/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/34e9b06e7f12eaed676f57481de931ec91c6ce0a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
