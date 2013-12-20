Name:		jboss-as7-dist-native
Version:	7.1.1.Final
Release:	1%{?dist}
Summary:	JBoss AS7 native libraries

Group:		System Environment/Daemons
License:	LGPL 2.1
URL:		http://www.jboss.org/jbossas/
Source:		http://download.jboss.org/jbossas/7.1/jboss-as-%{version}/jboss-as-%{version}.tar.gz

Prefix:		/opt/jboss-as-%{version}
Requires:	jboss-as7-dist

# There are native libraries for OS X and Windows, they're of limited use in an
# RPM.
ExclusiveArch:	x86_64 i686
ExclusiveOS:	Linux

%undefine _missing_build_ids_terminate_build
%define __arch_install_post QA_SKIP_RPATHS=2 %{__arch_install_post} 


%description
Native libraries for JBoss AS7.


%prep
%setup -q -n jboss-as-%{version}


%install
mkdir -p %{buildroot}%{prefix}/modules/org/jboss/as/web/main/lib/%{_os}-%{_target_cpu}
install -D ./modules/org/jboss/as/web/main/lib/%{_os}-%{_target_cpu}/* %{buildroot}%{prefix}/modules/org/jboss/as/web/main/lib/%{_os}-%{_target_cpu}
mkdir -p %{buildroot}%{prefix}/modules/org/hornetq/main/lib/%{_os}-%{_target_cpu}
install -D ./modules/org/hornetq/main/lib/%{_os}-%{_target_cpu}/* %{buildroot}%{prefix}/modules/org/hornetq/main/lib/%{_os}-%{_target_cpu}


%files
%defattr(-,root,root,0755)
%{prefix}/modules/org/jboss/as/web/main/lib/%{_os}-%{_target_cpu}
%{prefix}/modules/org/hornetq/main/lib/%{_os}-%{_target_cpu}


%changelog

