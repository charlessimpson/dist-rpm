Name:		jetty8-dist
Version:	8.1.15.v20140411
Release:	1%{?dist}
Summary:	Jetty web server
Group:		System Environment/Daemons
License:	ASL 2.0 or EPL 1.0
URL:		http://www.eclipse.org/jetty/
Source:	        http://eclipse.org/downloads/download.php?r=1&file=/jetty/%{version}/dist/jetty-distribution-%{version}.tar.gz

BuildArch:	noarch
Prefix:		/opt/jetty-%{version}
Requires:	java >= 1.6.0
Provides:	jetty8


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
alternatives --install /etc/alternatives/jetty-8 jetty-8 %{prefix} 100


%postun
alternatives --remove jetty-8 %{prefix}


%files
%defattr(-,root,root,0755)

%dir %{prefix}

%{prefix}/bin
%{prefix}/contexts
%{prefix}/contexts-available
%{prefix}/etc
%{prefix}/lib
%{prefix}/logs
%{prefix}/overlays
%{prefix}/start.jar
%{prefix}/webapps

%doc %{prefix}/about.html
%doc %{prefix}/javadoc
%doc %{prefix}/LICENSE-APACHE-2.0.txt
%doc %{prefix}/LICENSE-ECLIPSE-1.0.html
%doc %{prefix}/notice.html
%doc %{prefix}/README.txt
%doc %{prefix}/VERSION.txt

%config %{prefix}/start.ini

%dir %{prefix}/resources
%config %{prefix}/resources/log4j.properties

%changelog
