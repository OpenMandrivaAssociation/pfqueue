# compatability macros
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

%{?!_with_unstable: %{error:%(echo -e "\n\n\nYou are building package for a stable release, please see \nhttp://qa.mandrakesoft.com/twiki/bin/view/Main/DistroSpecificReleaseTag\nif you think this is incorrect\n\n\n ")}%(sleep 2)}

%define name pfqueue
%define version 0.5.2
%define release %mkrel 1
Summary:	Queue manager for the Postfix or Exim mail transport agent
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://pfqueue.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
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
%define __libtoolize %{nil}
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_sbindir}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun
[ $1 == 0 ] && /sbin/ldconfig

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/pfqueue.1*
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


