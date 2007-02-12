%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	OpenSearch
%define		_status		beta
%define		_pearname	Services_OpenSearch

Summary:	%{_pearname} - Search A9 OpenSearch compatible engines
Summary(pl.UTF-8):   %{_pearname} - wyszukiwanie w silnikach kompatybilnych z A9 OpenSearch
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bff686fc6586146e33b64cfb478dc902
URL:		http://pear.php.net/package/Services_OpenSearch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR
Requires:	php-pear-XML_RSS
Requires:	php-pear-XML_Serializer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides access to A9 OpenSearch compatible search engines. This is
porting Perl modules WWW::OpenSearch.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Umożliwia dostęp do wyszukiwarek kompatybilnych z A9 OpenSearch. Jest
to port modułu Perla WWW::OpenSearch.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/OpenSearch.php
