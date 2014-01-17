Name:		maven
Version:	3.1.1
Release:	1%{?dist}
Summary:	Maven software project management and comprehension tool
Group:		Development/Tools
License:	ASL 2.0
URL:		http://maven.apache.org
Source0:	apache-maven-3.1.1-bin.tar.gz
Source1:	http://maven.apache.org/download.cgi

BuildArch:	noarch
Prefix:		/opt/maven-%{version}
Requires:	java >= 1.5.0


%description
Apache Maven is a software project management and comprehension tool. Based on
the concept of a project object model (POM), Maven can manage a project's
build, reporting and documentation from a central piece of information. 


%prep
%setup -q -n apache-maven-%{version}


%install
%define __jar_repack 0
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post
alternatives --install /etc/alternatives/maven-3 maven-3 %{prefix} 100
alternatives --install /etc/alternatives/maven maven %{prefix} 100


%postun
alternatives --remove maven-3 %{prefix}
alternatives --remove maven %{prefix}


%files
%defattr(-,root,root,0755)

%dir %{prefix}

%{prefix}/bin
%{prefix}/boot
%{prefix}/lib

%doc %{prefix}/LICENSE
%doc %{prefix}/NOTICE
%doc %{prefix}/README.txt

%dir %{prefix}/conf
%config %{prefix}/conf/settings.xml
%dir %{prefix}/conf/logging
%config %{prefix}/conf/logging/simplelogger.properties

%changelog
