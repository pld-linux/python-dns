
%define		module	dns

Summary:	dnspython - A DNS toolkit for Python
Name:		python-%{module}
Version:	1.3.2
Release:	1
License:	distributable
Group:		Development/Languages/Python
Source0:	http://www.dnspython.org/kits/stable/dnspython-1.3.2.tar.gz
# Source0-md5:	8ee1fb516d3909a6826c402fc9bc099c
URL:		http://www.dnspython.org/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnspython is a DNS toolkit for Python. It supports almost all record types. It
can be used for queries, zone transfers, and dynamic updates. It supports TSIG
authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high level
classes perform queries for data of a given name, type, and class, and return
an answer set. The low level classes allow direct manipulation of DNS zones,
messages, names, and records. 

%prep
%setup -q -n dnspython-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE ChangeLog README TODO
%{py_sitescriptdir}/%{module}
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
