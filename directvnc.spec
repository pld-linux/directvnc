Summary:	DirectVNC - VNC client for DirectFB
Summary(pl.UTF-8):	DirectVNC - klient VNC dla DirectFB
Name:		directvnc
Version:	0.7.5
Release:	5
License:	GPL
Group:		Applications/Networking
Source0:	http://freesoftware.fsf.org/download/directvnc/%{name}-%{version}.tar.gz
# Source0-md5:	1fba84dc5450751bb402b68a9b9fb429
Patch0:		%{name}-caps.patch
Patch1:		%{name}-latin2.patch
Patch2:		%{name}-ctrl_alt_backspace.patch
Patch3:		%{name}-3.3.7-tight.patch
URL:		http://www.adam-lilienthal.de/directvnc/
BuildRequires:	DirectFB-devel >= 0.9.24
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectVNC is a client implementing the remote framebuffer protocol
(rfb) which is used by VNC servers. If a VNC server is running on a
machine you can connect to it using this client and have the contents
of its display shown on your screen. Keyboard and mouse events are
sent to the server, so you can basically control a VNC server
remotely. There are servers (and other clients) freely available for
all operating systems. What makes DirectVNC different from other unix
VNC clients is that it uses the linux framebuffer device through the
DirectFB library which enables it to run on anything that has a
framebuffer without the need for a running X server. This includes
embedded devices. DirectFB even uses acceleration features of certain
graphics cards.

%description -l pl.UTF-8
DirectVNC jest klientem zawierającym implementację protokołu zdalnego
framebuffera (rfb - remote framebuffer protocol), używanego przez
serwery VNC. Jeśli serwer VNC działa na jakiejś maszynie, można się
z nią połączyć przy użyciu tego klienta i widzieć zawartość jego
ekranu na swoim. Zdarzenia z klawiatury i myszy są wysyłane do
serwera, więc można zdalnie kontrolować serwer VNC. Istnieją serwery
(i inne klienty) dostępne za darmo na wiele systemów operacyjnych.
DirectFB od innych uniksowych klientów VNC różni się tym, że używa
linuksowego framebuffera poprzez bibliotekę DirectFB, co pozwala na
pracę bez potrzeby uruchamiania X serwera. Jednym z zastosowań są
urządzenia wbudowane. DirectFB może nawet używać sprzętowej
akceleracji na niektórych kartach graficznych.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
