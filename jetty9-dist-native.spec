Name:		jetty9-dist-native
Version:	9.1.0.v20131115
Release:	1%{?dist}
Summary:	Jetty 9 native libraries
Group:		System Environment/Daemons
License:	ASL 2.0 or EPL 1.0
URL:		http://www.eclipse.org/jetty/
Source0:	jetty-distribution-%{version}.tar.gz
Source1:	http://eclipse.org/downloads/download.php?file=/jetty/%{version}/dist/

Prefix:		/opt/jetty-%{version}
Requires:	jetty9-dist

ExclusiveArch:	x86_64
ExclusiveOS:	Linux


%description
Native libraries for Jetty 9.


%prep
%setup -q -n jetty-distribution-%{version}


%install
mkdir -p %{buildroot}%{prefix}/lib/setuid
cp lib/setuid/libsetuid-linux.so %{buildroot}%{prefix}/lib/setuid


%files
%defattr(-,root,root,0755)
%{prefix}/lib/setuid/libsetuid-linux.so


%changelog
