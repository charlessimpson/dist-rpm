Name:		zookeeper-dist
Version:	3.4.5
Release:	1%{?dist}
Summary:	ZooKeeper server
BuildArch:	noarch

Group:		System Environment/Daemons
License:	ASL 2.0
URL:		http://zookeeper.apache.org/
Source:		http://www.apache.org/dyn/closer.cgi/zookeeper/zookeeper-%{version}/zookeeper-%{version}.tar.gz

Prefix:		/opt/zookeeper-%{version}
Requires:	java >= 1.6.0

%define __jar_repack 0

%description
ZooKeeper server packaged from the binary distribution.

ZooKeeper is a centralized service for maintaining configuration information,
naming, providing distributed synchronization, and providing group services. 


%prep
%setup -q -n zookeeper-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post
alternatives --install /etc/alternatives/zookeeper zookeeper %{prefix} 100


%postun
alternatives --remove zookeeper %{prefix}


%files
%defattr(-,root,root,0755)
%dir %{prefix}
%{prefix}/bin
%{prefix}/contrib
%{prefix}/dist-maven
%{prefix}/lib
%{prefix}/recipes
%{prefix}/src

%{prefix}/build.xml
%{prefix}/ivysettings.xml
%{prefix}/ivy.xml
%{prefix}/zookeeper-%{version}.jar
%{prefix}/zookeeper-%{version}.jar.asc
%{prefix}/zookeeper-%{version}.jar.md5
%{prefix}/zookeeper-%{version}.jar.sha1

%dir %{prefix}/conf
%config %{prefix}/conf/log4j.properties
%doc %{prefix}/conf/zoo_sample.cfg
%{prefix}/conf/configuration.xsl

%doc %{prefix}/docs
%doc %{prefix}/CHANGES.txt
%doc %{prefix}/LICENSE.txt
%doc %{prefix}/NOTICE.txt
%doc %{prefix}/README_packaging.txt
%doc %{prefix}/README.txt


%changelog
