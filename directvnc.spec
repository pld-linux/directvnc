Summary:	DirectVNC - VNC client for DirectFB
Summary(pl):	DirectVNC - klient VNC dla DirectFB
Name:		directvnc
Version:	0.7.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://freesoftware.fsf.org/download/directvnc/%{name}-%{version}.tar.gz
URL:		http://www.adam-lilienthal.de/directvnc/
BuildRequires:	DirectFB-devel >= 0.9.16
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
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

%description -l pl
DirectVNC jest klientem zawieraj±cym implementacjê protoko³u zdalnego
framebuffera (rfb - remote framebuffer protocol), u¿ywanego przez
serwery VNC. Je¶li serwer VNC dzia³a na jakiej¶ maszynie, mo¿na siê
z ni± po³±czyæ przy u¿yciu tego klienta i widzieæ zawarto¶æ jego
ekranu na swoim. Zdarzenia z klawiatury i myszy s± wysy³ane do
serwera, wiêc mo¿na zdalnie kontrolowaæ serwer VNC. Istniej± serwery
(i inne klienty) dostêpne za darmo na wiele systemów operacyjnych.
DirectFB od innych uniksowych klientów VNC ró¿ni siê tym, ¿e u¿ywa
linuksowego framebuffera poprzez bibliotekê DirectFB, co pozwala na
pracê bez potrzeby uruchamiania X serwera. Jednym z zastosowañ s±
urz±dzenia wbudowane. DirectFB mo¿e nawet u¿ywaæ sprzêtowej
akceleracji na niektórych kartach graficznych.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
