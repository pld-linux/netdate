Summary:	Allows setting system time from across a network
Summary(pl):	Pozwala na synchronizacjê czasu systemowego poprzez sieæ
Name:		netdate
Version:	1.16
Release:	1
License:	GPL
Group(pl):	Aplikacje/Internet
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/netdate/%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for checking and setting the local system time from across a network
as specified by RFC 868.

%description -l pl
Pozwala na sprawdzenie i synchronizacjê czasu lokalnego systemu poprzez 
sieæ zgodnie z RFC 868.

%prep
%setup
%patch0 -p1

%build
%{__make} CC="%{__cc} %{rpmcflags} -Wall"

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8

install -m 644 netdate.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -m 755 netdate $RPM_BUILD_ROOT%{_sbindir}
gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/*
%doc README.gz
