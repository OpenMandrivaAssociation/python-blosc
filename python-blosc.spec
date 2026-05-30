%define module blosc

Name:		python-blosc
Version:	1.11.4
Release:	1
Summary:	Blosc data compressor
License:	BSD
Group:		Development/Python
URL:		https://pypi.python.org/pypi/blosc/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(blosc)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(py-cpuinfo)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(scikit-build)
BuildRequires:	python%{pyver}dist(wheel)

%description
Blosc is a high performance compressor optimized for binary data.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build -p
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver}"
export BLOSC_DIR=%{_libdir}/blosc
export USE_SYSTEM_BLOSC=1

%files
%doc README.rst RELEASE_NOTES.rst
%{python_sitearch}/%{module}*



