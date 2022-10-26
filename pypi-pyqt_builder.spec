#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyqt_builder
Version  : 1.12.2
Release  : 6
URL      : https://files.pythonhosted.org/packages/8b/5f/1bd49787262ddce37b826ef49dcccf5a9970facf0ed363dee5ee233e681d/PyQt-builder-1.12.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/8b/5f/1bd49787262ddce37b826ef49dcccf5a9970facf0ed363dee5ee233e681d/PyQt-builder-1.12.2.tar.gz
Summary  : The PEP 517 compliant PyQt build system
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: pypi-pyqt_builder-bin = %{version}-%{release}
Requires: pypi-pyqt_builder-license = %{version}-%{release}
Requires: pypi-pyqt_builder-python = %{version}-%{release}
Requires: pypi-pyqt_builder-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sip)
BuildRequires : pypi(wheel)

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

%description python3
python3 components for the pypi-pyqt_builder package.


%prep
%setup -q -n PyQt-builder-1.12.2
cd %{_builddir}/PyQt-builder-1.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643401833
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder
cp %{_builddir}/PyQt-builder-1.12.2/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/2136dbc93e95a70deae070e44ff6b2702ec1599c
cp %{_builddir}/PyQt-builder-1.12.2/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/pypi-pyqt_builder/34e9b06e7f12eaed676f57481de931ec91c6ce0a
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
