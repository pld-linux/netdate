Summary:	Allows setting system time from across a network
Summary(pl):	Pozwala na synchronizacjê czasu systemowego poprzez sieæ
Name:		netdate
Version:	1.16
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/netdate/%{name}-%{version}.tar.gz
Patch0:		%{name}-hurricane.patch
Patch1:		%{name}-nread.patch
Patch2:		%{name}-main-prototype.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for checking and setting the local system time from across a
network as specified by RFC 868.

%description -l pl
Pozwala na sprawdzenie i synchronizacjê czasu lokalnego systemu
poprzez sieæ zgodnie z RFC 868.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CC="%{__cc} %{rpmldflags} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install netdate.8 $RPM_BUILD_ROOT%{_mandir}/man8
install netdate $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
