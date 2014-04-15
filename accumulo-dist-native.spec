Name:		accumulo-dist-native
Version:	1.5.1
Release:	1%{?dist}
Summary:	Apache Accumulo native libraries
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		http://accumulo.apache.org/
Source: 	http://www.apache.org/dyn/closer.cgi/accumulo/%{version}/accumulo-%{version}-bin.tar.gz

Prefix:		/opt/accumulo-%{version}
Requires:	accumulo-dist

ExclusiveArch:	x86_64
ExclusiveOS:	Linux


%description
Native libraries for Apache Accumulo.


%prep
%setup -q -n accumulo-%{version}


%install
mkdir -p %{buildroot}%{prefix}/lib/native/map
cp lib/native/map/libNativeMap-Linux-amd64-64.so %{buildroot}%{prefix}/lib/native/map


%files
%defattr(-,root,root,0755)
%{prefix}/lib/native/map/libNativeMap-Linux-amd64-64.so


%changelog
