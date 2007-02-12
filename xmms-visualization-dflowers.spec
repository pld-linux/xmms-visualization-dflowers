Summary:	Dual Flowers
Summary(pl.UTF-8):   Podwójny Kwiat
Name:		xmms-visualization-dflowers
Version:	1.2.1
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dflowers-v%{version}.tar.gz
# Source0-md5:	6d1d87b1f8dfb3485040d4c82b585481
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dual Flowers plugin for XMMS.

%description -l pl.UTF-8
Wtyczka Podwójny Kwiat dla XMMS-a.

%prep
%setup -q -n dflowers-v%{version}

%build
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_visualization_plugindir}

install *.so $RPM_BUILD_ROOT%{xmms_visualization_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
