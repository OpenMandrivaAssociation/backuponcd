%define name		backuponcd
%define version		0.9.1
%define release		%mkrel 8

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


