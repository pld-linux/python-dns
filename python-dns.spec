
%define		module	dns

Summary:	dnspython - a DNS toolkit for Python
Summary(pl):	dnspython - zestaw narzêdzi do DNS dla Pythona
Name:		python-%{module}
Version:	1.3.5
Release:	2
License:	distributable
Group:		Development/Languages/Python
Source0:	http://www.dnspython.org/kits/stable/dnspython-%{version}.tar.gz
# Source0-md5:	d086b05b70f7ab1b6308f29f2427623b
URL:		http://www.dnspython.org/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%description -l pl
dnspython to zestaw narzêdzi do DNS dla Pythona. Obs³uguje prawie
wszystkie rodzaje rekordów. Mo¿e byæ u¿ywany do zapytañ, transferów
stref oraz dynamicznych uaktualnieñ. Obs³uguje uwierzytelnione
komunikaty TSIG oraz EDNS0.

dnspython dostarcza zarówno wysoko- jak i niskopoziomowy dostêp do
DNS-a. Klasy wysokopoziomowe wykonuj± zapytania o dane dla podanej
nazwy, rodzaju i klasy, a zwracaj± zbiór odpowiedzi. Klasy
niskopoziomowe umo¿liwiaj± bezpo¶rednie manipulacje na strefach,
komunikatach, nazwach i rekordach w DNS-ie.

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
