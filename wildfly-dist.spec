Name:		wildfly-dist
Version:	8.2.0.Final
Release:	1%{?dist}
Summary:	WildFly Application Server
Group:		System Environment/Daemons
License:	LGPL 2.1
URL:		http://www.wildfly.org
Source:		http://download.jboss.org/wildfly/%{version}/wildfly-%{version}.tar.gz

ExclusiveArch:	x86_64 i686
ExclusiveOS:	Linux

Requires(pre):	shadow-utils
Requires:	java >= 1.7.0
Requires:	/etc/init.d/functions
Provides:	wildfly

%undefine _missing_build_ids_terminate_build
%define __arch_install_post QA_SKIP_RPATHS=2 %{__arch_install_post} 
%define __jar_repack 0

%description
WildFly Application Server packaged from the binary distribution.


%prep
%setup -q -n wildfly-%{version}


%install
mkdir -p %{buildroot}/opt/wildfly
cp -R . %{buildroot}/opt/wildfly
mkdir -p %{buildroot}/etc/init.d
ln -s /opt/wildfly/bin/init.d/wildfly-init-redhat.sh %{buildroot}/etc/init.d/wildfly
mkdir -p %{buildroot}/etc/default
cp bin/init.d/wildfly.conf %{buildroot}/etc/default/wildfly.conf

# The init script doesn't default the user and crashes. Might as well set the
# home dir since we know what it is.
sed -e 's/# JBOSS_HOME/JBOSS_HOME/' -i %{buildroot}/etc/default/wildfly.conf
sed -e 's/# JBOSS_USER/JBOSS_USER/' -i %{buildroot}/etc/default/wildfly.conf

mkdir -p %{buildroot}/var/log/wildfly
mkdir -p %{buildroot}/var/run/wildfly


%pre
getent group wildfly >/dev/null || groupadd -r wildfly
getent passwd wildfly >/dev/null || \
    useradd -r -g wildfly -d /opt/wildfly -s /sbin/nologin wildfly


%post
alternatives --install /etc/alternatives/wildfly wildfly /opt/wildfly 100


%postun
alternatives --remove wildfly /opt/wildfly


%files
%defattr(-,root,root,0755)


%files
%defattr(-,root,root,0755)
%config /etc/default/wildfly.conf
/etc/init.d/wildfly
%dir /opt/wildfly
/opt/wildfly/appclient
/opt/wildfly/bin
/opt/wildfly/domain
/opt/wildfly/jboss-modules.jar
/opt/wildfly/modules
%attr(-,wildfly,wildfly) /opt/wildfly/standalone
/opt/wildfly/welcome-content
%dir /var/log/wildfly
%dir /var/run/wildfly

%doc /opt/wildfly/copyright.txt
%doc /opt/wildfly/LICENSE.txt
%doc /opt/wildfly/README.txt
%doc /opt/wildfly/docs


%changelog
* Tue Jul 21 2015 Charles Simpson <csimpson@gmail.com>
- bump to 8.2.0.Final

* Tue Jul 21 2015 Charles Simpson <csimpson@gmail.com>
- eliminate split between wildfly-common and wildfly
- change location to /opt/wildfly (see bin/init.d/wildfly.conf for default)
- install init.d and configuration files

* Sun Jul 13 2014 Charles Simpson <csimpson@gmail.com>
- initial creation
