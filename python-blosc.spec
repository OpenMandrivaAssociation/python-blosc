%define	module	blosc
%define name	python-%{module}
%define version 1.0.4
%define rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Blosc data compressor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/blosc/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel

%description
Blosc is a high performance compressor optimized for binary data.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSES/BLOSC.txt
%py_platsitedir/%{module}*


%changelog
* Fri Sep 14 2012 Lev Givon <lev@mandriva.org> 1.0.4-1
+ Revision: 816944
- Update to 1.0.4.

* Thu Dec 08 2011 Lev Givon <lev@mandriva.org> 1.0.3-1
+ Revision: 739181
- imported package python-blosc

