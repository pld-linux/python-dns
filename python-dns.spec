%define		module	dns
Summary:	dnspython - a DNS toolkit for Python 2
Summary(pl.UTF-8):	dnspython - zestaw narzędzi do DNS dla Pythona 2
Name:		python-%{module}
Version:	1.16.0
Release:	6
License:	MIT
Group:		Development/Languages/Python
Source0:	https://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
# Source0-md5:	5691e0fbb280ed4eaf182ebedccf3462
URL:		https://www.dnspython.org/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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

%description -l pl.UTF-8
dnspython to zestaw narzędzi do DNS dla Pythona. Obsługuje prawie
wszystkie rodzaje rekordów. Może być używany do zapytań, transferów
stref oraz dynamicznych uaktualnień. Obsługuje uwierzytelnione
komunikaty TSIG oraz EDNS0.

dnspython dostarcza zarówno wysoko- jak i niskopoziomowy dostęp do
DNS-a. Klasy wysokopoziomowe wykonują zapytania o dane dla podanej
nazwy, rodzaju i klasy, a zwracają zbiór odpowiedzi. Klasy
niskopoziomowe umożliwiają bezpośrednie manipulacje na strefach,
komunikatach, nazwach i rekordach w DNS-ie.

%prep
%setup -q -n dnspython-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python}\1,' -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python}\1,' \
      $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/dns
%{py_sitescriptdir}/dnspython-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
