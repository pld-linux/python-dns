# NOTE: python3 version in separate package (python3-dns)

%define		module	dns

Summary:	dnspython - a DNS toolkit for Python
Summary(pl.UTF-8):	dnspython - zestaw narzędzi do DNS dla Pythona
Name:		python-%{module}
Version:	1.12.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://www.dnspython.org/kits/%{version}/dnspython-%{version}.tar.gz
# Source0-md5:	3f2601ef3c8b77fc6d21a9c77a81efeb
URL:		http://www.dnspython.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

%py_postclean

cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%{py_sitescriptdir}/dns
%{py_sitescriptdir}/dnspython-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
