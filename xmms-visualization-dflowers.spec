Summary:	Dual Flowers
Summary(pl):	Podwójny Kwiat
Name:		xmms-visualization-dflowers
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dflowers-v%{version}.tar.gz
URL:		http://www.shell.linux.se/bm/index.php
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Dual Flowers plugin for XMMS.

%description -l pl
Plugin Podwójny Kwiat dla XMMS.

%prep
%setup -q -n dflowers-v%{version}

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/

install *.so	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_libdir}/xmms/*/*.so
