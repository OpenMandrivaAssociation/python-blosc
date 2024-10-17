%define	module	blosc
%define rel		1
%if %mdkversion < 201100
%else
%endif

Summary:	Blosc data compressor

Name:		python-%{module}
Version:	1.2.3
Release:	2
Source0:	http://pypi.python.org/packages/source/b/blosc/blosc-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/blosc/
BuildRequires:	python-devel

%description
Blosc is a high performance compressor optimized for binary data.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc LICENSES/BLOSC.txt
%{py_platsitedir}/%{module}*



