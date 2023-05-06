Summary:	LXDE icon theme
Summary(pl.UTF-8):	Motyw ikon LXDE
Name:		lxde-icon-theme
Version:	0.5.1
Release:	1
License:	GPL v3
Group:		Themes
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	7467133275edbbcc79349379235d4411
URL:		http://www.lxde.org/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXDE icon theme.

%description -l pl.UTF-8
Motyw ikon LXDE.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_iconsdir}/nuoveXT2
