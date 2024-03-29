Summary:	Allows setting system time from across a network
Summary(pl.UTF-8):	Pozwala na synchronizację czasu systemowego poprzez sieć
Name:		netdate
Version:	1.16
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/sunacm/Other/netdate/%{name}-%{version}.tar.gz
# Source0-md5:	8bbc82a2df10088d75672b31a80f1a0f
Patch0:		%{name}-hurricane.patch
Patch1:		%{name}-nread.patch
Patch2:		%{name}-main-prototype.patch
Patch3:		%{name}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows for checking and setting the local system time from across a
network as specified by RFC 868.

%description -l pl.UTF-8
Pozwala na sprawdzenie i synchronizację czasu lokalnego systemu
poprzez sieć zgodnie z RFC 868.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

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
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
