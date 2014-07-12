Name:		jboss-as7-dist
Version:	7.1.1.Final
Release:	1%{?dist}
Summary:	JBoss Application Server
Group:		System Environment/Daemons
License:	LGPL 2.1
URL:		http://www.jboss.org/jbossas/
Source:		http://download.jboss.org/jbossas/7.1/jboss-as-%{version}/jboss-as-%{version}.tar.gz

ExclusiveArch:	x86_64 i686
ExclusiveOS:	Linux

Prefix:		/opt/jboss-as-%{version}
Requires:	java >= 1.6.0
Requires:	jboss-as7-dist-common
Provides:	jboss-as7

%undefine _missing_build_ids_terminate_build
%define __arch_install_post QA_SKIP_RPATHS=2 %{__arch_install_post} 
%define __jar_repack 0

%description
JBoss Application Server packaged from the binary distribution.


%package common
Summary:	JBoss Application Server common components
BuildArch:	noarch


%description common
Architecture-independent components of JBoss AS7.


%prep
%setup -q -n jboss-as-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post common
alternatives --install /etc/alternatives/jboss-as7 jboss-as7 %{prefix} 100


%postun common
alternatives --remove jboss-as7 %{prefix}


%files
%defattr(-,root,root,0755)
%{prefix}/modules/org/jboss/as/web/main/lib/%{_os}-%{_target_cpu}
%{prefix}/modules/org/hornetq/main/lib/%{_os}-%{_target_cpu}


%files common
%defattr(-,root,root,0755)
%dir %{prefix}
%{prefix}/appclient
%{prefix}/bin
%{prefix}/bundles
%{prefix}/domain
%{prefix}/jboss-modules.jar
%{prefix}/modules
%{prefix}/standalone
%{prefix}/welcome-content

%exclude %{prefix}/modules/org/jboss/as/web/main/lib/linux-i686
%exclude %{prefix}/modules/org/jboss/as/web/main/lib/linux-x86_64
%exclude %{prefix}/modules/org/jboss/as/web/main/lib/macosx-i686
%exclude %{prefix}/modules/org/jboss/as/web/main/lib/macosx-x86_64
%exclude %{prefix}/modules/org/jboss/as/web/main/lib/win-i686
%exclude %{prefix}/modules/org/jboss/as/web/main/lib/win-x86_64
%exclude %{prefix}/modules/org/hornetq/main/lib/linux-i686
%exclude %{prefix}/modules/org/hornetq/main/lib/linux-x86_64

%doc %{prefix}/copyright.txt
%doc %{prefix}/LICENSE.txt
%doc %{prefix}/README.txt
%doc %{prefix}/docs


%changelog

