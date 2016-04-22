%define		php_min_version 5.3.7
%include	/usr/lib/rpm/macros.php
Summary:	Eventum SCM integration
Summary(pl.UTF-8):	Integracja SCM dla Eventum
Name:		eventum-scm
Version:	3.1.0
Release:	0.2
License:	GPL v2+
Group:		Networking/Utilities
#Source0:	https://github.com/eventum/scm/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/eventum/scm/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	e772d15161474c1ec1c57c61d07d1f4c
Source1:	config.php
Patch0:		config.patch
URL:		https://github.com/eventum/scm
BuildRequires:	/usr/bin/php
BuildRequires:	php(core) >= %{php_min_version}
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	sed >= 4.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
Suggests:	cvs
Suggests:	git-core
Suggests:	php(openssl)
Suggests:	subversion
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/eventum

%description
This feature allows your software development teams to integrate your
Source Control Management system with your Issue Tracking System.

The integration is implemented in such a way that it will be forward
compatible with pretty much any SCM system, such as CVS.

For installation see
</eventum/help.php?topic=scm_integration_installation>.

%description -l pl.UTF-8
Ten pakiet pozwala zespołom programistów na integrację systemu
zarządzania źródłami (SCM - Source Control Management) z systemem
śledzenia spraw.

Integracja jest zaimplementowana tak, aby być kompatybilna w przód z
prawie każdym systemem SCM, jak np. CVS.

Szczegóły na temat instalacji można przeczytać pod
</eventum/help.php?topic=scm_integration_installation>.

%prep
%setup -qc
mv scm-*/* .
%patch0 -p2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/scm.php
cp -p helpers.php $RPM_BUILD_ROOT%{_sbindir}
for a in eventum-*-hook.php; do
	f=${a%.php}
	install -p $a $RPM_BUILD_ROOT%{_sbindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(751,root,root) %dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/scm.php
%attr(755,root,root) %{_sbindir}/eventum-cvs-hook
%attr(755,root,root) %{_sbindir}/eventum-git-hook
%attr(755,root,root) %{_sbindir}/eventum-svn-hook
%attr(755,root,root) %{_sbindir}/helpers.php
