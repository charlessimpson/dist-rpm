Name:		accumulo-dist
Version:	1.5.1
Release:	1%{?dist}
Summary:	Apache Accumulo is a sorted, distributed key/value store based on Google's BigTable design.
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		http://accumulo.apache.org/
Source: 	http://www.apache.org/dyn/closer.cgi/accumulo/%{version}/accumulo-%{version}-bin.tar.gz

BuildArch:  noarch
Prefix:		/opt/accumulo-%{version}
Requires:   hadoop
Requires:   zookeeper >= 3
Requires:	java >= 1.6.0
Provides:   accumulo

%define __jar_repack 0

%description
Accumulo packaged from the binary distribution.

Apache Accumulo is a highly scalable structured store based on Google's
BigTable. Accumulo is written in Java and operates over the Hadoop Distributed
File System (HDFS), which is part of the popular Apache Hadoop project.
Accumulo supports efficient storage and retrieval of structured data, including
queries for ranges, and provides support for using Accumulo tables as input and
output for MapReduce jobs.

Accumulo features automatic load-balancing and partitioning, data compression
and fine-grained security labels.

%prep
%setup -q -n accumulo-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post
alternatives --install /etc/alternatives/accumulo accumulo %{prefix} 100


%postun
alternatives --remove accumulo %{prefix}


%files
%defattr(-,root,root,0755)

%{prefix}/bin
%{prefix}/conf
%{prefix}/examples
%{prefix}/lib
%{prefix}/logs
%{prefix}/proxy
%{prefix}/scripts
%{prefix}/server
%{prefix}/test

%dir %{prefix}/lib/native
%dir %{prefix}/lib/native/map

%doc %{prefix}/docs
%doc %{prefix}/CHANGES
%doc %{prefix}/LICENSE
%doc %{prefix}/NOTICE
%doc %{prefix}/README

# Included in -native package
%exclude %{prefix}/lib/native/map/libNativeMap-Linux-amd64-64.so

%changelog
