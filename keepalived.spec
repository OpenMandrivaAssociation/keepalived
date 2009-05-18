%define name    keepalived
%define version 1.1.17
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: HA monitor built upon LVS, VRRP and services poller
License: GPL
Group: System/Cluster 
URL: http://www.keepalived.org/
Source0: %{name}_%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: libpopt-devel
BuildRequires: kernel-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The main goal of the keepalived project is to add a strong & robust keepalive
facility to the Linux Virtual Server project. This project is written in C with
multilayer TCP/IP stack checks. Keepalived implements a framework based on
three family checks : Layer3, Layer4 & Layer5/7. This framework gives the
daemon the ability to check the state of an LVS server pool. When one of the
servers of the LVS server pool is down, keepalived informs the linux kernel via
a setsockopt call to remove this server entry from the LVS topology. In
addition keepalived implements an independent VRRPv2 stack to handle director
failover. So in short keepalived is a userspace daemon for LVS cluster nodes
healthchecks and LVS directors failover.

%prep
%setup

%build
%configure 
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}
# Remove "samples", as we include them in %%doc
rm -rf %{buildroot}%{_sysconfdir}/%{name}/samples/

%post
%_post_service %{name}

%preun 
%_preun_service %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHOR ChangeLog CONTRIBUTORS COPYING README TODO
%doc doc/keepalived.conf.SYNOPSIS doc/samples/
%dir %{_sysconfdir}/keepalived/
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/keepalived/keepalived.conf
%attr(0600, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/keepalived
%{_sysconfdir}/rc.d/init.d/keepalived
%{_bindir}/genhash
%{_sbindir}/keepalived
%{_mandir}/man1/genhash.1*
%{_mandir}/man5/keepalived.conf.5*
%{_mandir}/man8/keepalived.8*

