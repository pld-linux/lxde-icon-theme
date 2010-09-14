Summary:	LXDE icon theme
Name:		lxde-icon-theme
Version:	0.0.1
Release:	1
License:	LGPL v3
Group:		Themes
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.bz2
# Source0-md5:	0c6ed34bb678f832345fc4495647a705
URL:		http://www.lxde.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXDE icon theme.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_iconsdir}/nuoveXT2