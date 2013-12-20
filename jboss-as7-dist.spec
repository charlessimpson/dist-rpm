Name:		jboss-as7-dist
Version:	7.1.1.Final
Release:	1%{?dist}
Summary:	JBoss Application Server
Group:		System Environment/Daemons
License:	LGPL 2.1
URL:		http://www.jboss.org/jbossas/
Source:		http://download.jboss.org/jbossas/7.1/jboss-as-%{version}/jboss-as-%{version}.tar.gz

BuildArch:	noarch
Prefix:		/opt/jboss-as-%{version}
Requires:	java >= 1.6.0
Provides:	jboss-as7

%define __jar_repack 0

%description
JBoss Application Server packaged from the binary distribution.


%prep
%setup -q -n jboss-as-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%files
%defattr(-,root,root,0755)
%{prefix}/appclient
%{prefix}/bin
%{prefix}/bundles
%{prefix}/domain
%{prefix}/jboss-modules.jar
%{prefix}/standalone
%{prefix}/welcome-content

%{prefix}/modules
# Included in -native package
%exclude %{prefix}/modules/org/jboss/as/web/main/lib
%exclude %{prefix}/modules/org/hornetq/main/lib

%doc %{prefix}/copyright.txt
%doc %{prefix}/LICENSE.txt
%doc %{prefix}/README.txt
%doc %{prefix}/docs


%changelog

