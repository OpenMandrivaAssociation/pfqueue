%define name pfqueue
%define version 0.5.6
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Queue manager for the Postfix or Exim mail transport agent
License:	GPL
Group:		Monitoring
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://pfqueue.sourceforge.net/
BuildRequires:	ncurses-devel


%description
Pfqueue is a simple console tool for managing MTA (Mail Transfer Agent)
message queues. It handles queues through  'backends',  libraries  that
interact  with  the  MTA,  and displays informations through a console,
ncurses based 'frontend'.
Currently, pfqueue has backends for Postfix (both 1.x and 2.x) and Exim
(both version 3 and 4).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_mandir}/man1/pfqueue.1*
%{_mandir}/man5/pfqueue.conf.5*
%{_sbindir}/pfqueue
%{_sbindir}/spfqueue
%exclude %{_libdir}/libpfq*.a
%exclude %{_libdir}/libpfq*.la
%exclude %{_libdir}/libpfq*.so
%exclude %{_libdir}/libpfq*.so.?
%exclude %{_libdir}/libpfq_postfix1.so.*
%{_libdir}/libpfq_exim.so.*
%{_libdir}/libpfq_postfix2.so.*
%{_libdir}/libpfq_socket.so.*
%{_libdir}/libpfqueue.so.*


