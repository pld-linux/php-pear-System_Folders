%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Folders
%define		_status		beta
%define		_pearname	System_Folders

Summary:	%{_pearname} - Location of system folders
Summary(pl):	%{_pearname} - lokalizacja folderów systemowych
Name:		php-pear-%{_pearname}
Version:	0.1.6
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c438ffca39f9f0394b5a85f1346bfc74
URL:		http://pear.php.net/package/System_Folders/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Config >= 1.10.5
Requires:	php-pear-PEAR >= 1:1.4.-0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculates or guesses the location of system folders like temp,
desktop and others.

In PEAR status of this package is: %{_status}.

%description -l pl
Oblicza lub zgaduje po³o¿enie folderów systemów takich jak katalog
tymczasowy, pulpit czy inne.

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
%doc install.log docs/%{_pearname}/{examples/cached.php,examples/example.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/Folders
%{php_pear_dir}/System/Folders.php
