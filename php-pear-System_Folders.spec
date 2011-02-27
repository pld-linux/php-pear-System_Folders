%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	System_Folders
Summary:	%{_pearname} - Location of system folders
Summary(pl.UTF-8):	%{_pearname} - lokalizacja folderów systemowych
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f5b17a2fafcc5dffd0883f6baba96fe6
URL:		http://pear.php.net/package/System_Folders/
BuildRequires:	php-pear-PEAR >= 1:1.4.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Config >= 1.10.5
Requires:	php-pear-PEAR-core >= 1:1.4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculates or guesses the location of system folders like temp,
desktop and others.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Oblicza lub zgaduje położenie folderów systemów takich jak katalog
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
