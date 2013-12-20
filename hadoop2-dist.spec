Name:		hadoop2-dist
Version:	2.2.0
Release:	1%{?dist}
Summary:	Hadoop distributed computing components
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		http://hadoop.apache.org
Source: 	http://www.apache.org/dyn/closer.cgi/hadoop/hadoop-%{version}/hadoop-%{version}.tar.gz

BuildArch:  noarch
Prefix:		/opt/hadoop-%{version}
Requires:	java >= 1.6.0
Provides:	hadoop

%define __jar_repack 0

%description
Hadoop packaged from the binary distribution.

The Apache Hadoop software library is a framework that allows for the
distributed processing of large data sets across clusters of computers using
simple programming models. It is designed to scale up from single servers to
thousands of machines, each offering local computation and storage. Rather than
rely on hardware to deliver high-availability, the library itself is designed
to detect and handle failures at the application layer, so delivering a
highly-available service on top of a cluster of computers, each of which may be
prone to failures.


%prep
%setup -q -n hadoop-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post
alternatives --install /etc/alternatives/hadoop-2 hadoop-2 %{prefix} 100


%postun
alternatives --remove hadoop-2 %{prefix}


%files
%defattr(-,root,root,0755)

%{prefix}/bin
%{prefix}/etc
%{prefix}/include
%{prefix}/libexec
%{prefix}/sbin
%{prefix}/share

%dir %{prefix}/lib
%dir %{prefix}/lib/native

%doc %{prefix}/LICENSE.txt
%doc %{prefix}/NOTICE.txt
%doc %{prefix}/README.txt

# Included in -native package
%exclude %{prefix}/bin/container-executor
%exclude %{prefix}/bin/test-container-executor
%exclude %{prefix}/lib/native/*

%changelog
