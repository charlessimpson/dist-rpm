Name:		hadoop2-dist-native
Version:	2.2.0
Release:	1%{?dist}
Summary:	Hadoop 2 native components
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		http://hadoop.apache.org
Source: 	http://www.apache.org/dyn/closer.cgi/hadoop/hadoop-%{version}/hadoop-%{version}.tar.gz

Prefix:		/opt/hadoop-%{version}
Requires:	hadoop2-dist

ExclusiveArch:	i686
ExclusiveOS:	Linux

%define __arch_install_post QA_SKIP_RPATHS=2 %{__arch_install_post} 

%description
Native components for Hadoop 2.


%prep
%setup -q -n hadoop-%{version}


%install
mkdir -p %{buildroot}%{prefix}/bin
cp bin/container-executor %{buildroot}%{prefix}/bin
cp bin/test-container-executor %{buildroot}%{prefix}/bin

mkdir -p %{buildroot}%{prefix}/lib/native
cp lib/native/*.a %{buildroot}%{prefix}/lib/native
cp lib/native/libhadoop.so.1.0.0 %{buildroot}%{prefix}/lib/native
cp lib/native/libhdfs.so.0.0.0 %{buildroot}%{prefix}/lib/native
ln -s libhadoop.so.1.0.0 %{buildroot}%{prefix}/lib/native/libhadoop.so
ln -s libhdfs.so.0.0.0 %{buildroot}%{prefix}/lib/native/libhdfs.so


%files
%defattr(-,root,root,0755)
%{prefix}/bin/container-executor
%{prefix}/bin/test-container-executor
%{prefix}/lib


%changelog
