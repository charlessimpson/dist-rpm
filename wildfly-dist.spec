Name:		wildfly-dist
Version:	8.1.0.Final
Release:	1%{?dist}
Summary:	WildFly Application Server
Group:		System Environment/Daemons
License:	LGPL 2.1
URL:		http://www.wildfly.org
Source:		http://download.jboss.org/wildfly/%{version}/wildfly-%{version}.tar.gz

ExclusiveArch:	x86_64 i686
ExclusiveOS:	Linux

Prefix:		/opt/wildfly-%{version}
Requires:	java >= 1.7.0
Requires:	wildfly-dist-common
Provides:	wildfly

%undefine _missing_build_ids_terminate_build
%define __arch_install_post QA_SKIP_RPATHS=2 %{__arch_install_post} 
%define __jar_repack 0

%description
WildFly Application Server packaged from the binary distribution.


%package common
Summary:	WildFly Application Server common components
BuildArch:	noarch


%description common
Architecture-independent components of WildFly.


%prep
%setup -q -n wildfly-%{version}


%install
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post common
alternatives --install /etc/alternatives/wildfly wildfly %{prefix} 100


%postun common
alternatives --remove wildfly %{prefix}


%files
%defattr(-,root,root,0755)
%{prefix}/modules/system/layers/base/org/hornetq/main/lib/%{_os}-%{_target_cpu}


%files common
%defattr(-,root,root,0755)
%dir %{prefix}
%{prefix}/appclient
%{prefix}/bin
%{prefix}/domain
%{prefix}/jboss-modules.jar
%{prefix}/modules
%{prefix}/standalone
%{prefix}/welcome-content

%exclude %{prefix}/modules/system/layers/base/org/hornetq/main/lib/linux-i686
%exclude %{prefix}/modules/system/layers/base/org/hornetq/main/lib/linux-x86_64

%doc %{prefix}/copyright.txt
%doc %{prefix}/LICENSE.txt
%doc %{prefix}/README.txt
%doc %{prefix}/docs


%changelog

