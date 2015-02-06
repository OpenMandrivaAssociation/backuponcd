%define name		backuponcd
%define version		0.9.1
%define release		13

%define summary		Multi-CD backup shell scripts
%define group		Archiving/Backup

Name:		%{name}
Summary:	%{summary}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		%{group}
URL:		http://www.tuxoncd.de/backuponcd/pub/backuponcd.html/
Source:		%{name}.tar.bz2
Patch1:		%{name}-rcmod.patch.bz2
Patch2:		%{name}-doc.patch.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
BackupOnCd is a set of shell scripts which make multi-volume backups on CD-RW
possible.  It also makes the backup faster using cdrecord in a parallel
subshell and minimizes the amount of temporary needed disk space.  Currently
supported: tar and afio.

Be sure to modify /etc/backuponcd/global.rc to suit your system!


%prep

%setup -c -q


# (pc) another dirty hack to clean out some temp files
for i in `find $RPM_BUILD_DIR/%name-%version -path '*~'`; do rm -f $i; done

# (pc) modify global.rc for more of a typical mdk setup
%patch1 -p0
# (pc) patch for documentation locations in backuponcd help message
%patch2 -p0


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_sbindir},%{_sysconfdir}/%{name}}
cp $RPM_BUILD_DIR/%name-%version/usr/local/sbin/* %{buildroot}%{_sbindir}
cp $RPM_BUILD_DIR/%name-%version/etc/%{name}/global.rc %{buildroot}%{_sysconfdir}/%{name}
cp $RPM_BUILD_DIR/%name-%version/usr/doc/%{name}/samples/excludelist %{buildroot}%{_sysconfdir}/%{name}

chmod 755 %{buildroot}%{_sbindir}/*

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/*


%files
%defattr(-,root,root)
%doc usr/doc/backuponcd/*
%{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/global.rc
%config(noreplace) %{_sysconfdir}/%{name}/excludelist




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-12mdv2011.0
+ Revision: 616705
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-11mdv2010.0
+ Revision: 424007
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-10mdv2009.0
+ Revision: 243146
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.9.1-8mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import backuponcd


* Mon Jul 31 2006 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-8mdv2007.0
- rebuild

* Thu Jul 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-7mdk
- rebuild

* Wed Jun 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-6mdk
- rebuild

* Mon Mar 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-5mdk
- typo ( thx Tarax )

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-4mdk
- rebuild

* Mon Jun 24 2002  Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-3mdk
- use setup -c 
- fix cleaning script (works only in buildir-name-version)

* Thu Feb 28 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-2mdk
- rebuild

* Tue Sep 11 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- added by Paul Cox <pcox@linux-mandrake.com> :
	- first Mandrake Linux release
	- added patch to modify global.rc to more of a typical mdk setup
	- added patch for documentation locations in backuponcd help message

# end of file
