Name:		jetty9-dist
Version:	9.2.2.v20140723
Release:	1%{?dist}
Summary:	Jetty web server
Group:		System Environment/Daemons
License:	ASL 2.0 or EPL 1.0
URL:		http://www.eclipse.org/jetty/
Source:	        http://eclipse.org/downloads/download.php?r=1&file=/jetty/%{version}/dist/jetty-distribution-%{version}.tar.gz

Prefix:		/opt/jetty-%{version}
Requires:	java-1.7.0
Provides:	jetty9

ExclusiveArch:	x86_64
ExclusiveOS:	Linux


%description
Jetty web server packaged from the binary distribution as a single RPM.

Jetty provides a Web server and javax.servlet container, plus support for SPDY,
WebSocket, OSGi, JMX, JNDI, JAAS and many other integrations.


%prep
%setup -q -n jetty-distribution-%{version}


%install
%define __jar_repack 0
mkdir -p %{buildroot}%{prefix}
cp -R . %{buildroot}%{prefix}


%post
alternatives --install /etc/alternatives/jetty-9 jetty-9 %{prefix} 100


%postun
alternatives --remove jetty-9 %{prefix}


%files
%defattr(-,root,root,0755)
%dir %{prefix}
%{prefix}/bin
%{prefix}/demo-base
%{prefix}/etc
%{prefix}/lib
%doc %{prefix}/license-eplv10-aslv20.html
%{prefix}/logs
%{prefix}/modules
%doc %{prefix}/notice.html
%doc %{prefix}/README.TXT
%dir %{prefix}/resources
%config %{prefix}/resources/log4j.properties
%dir %{prefix}/start.d
%config %{prefix}/start.d/http.ini
%config %{prefix}/start.d/jsp.ini
%config %{prefix}/start.d/jstl.ini
%doc %{prefix}/start.d/README.TXT
%config %{prefix}/start.ini
%{prefix}/start.jar
%doc %{prefix}/VERSION.txt
%{prefix}/webapps


%changelog
