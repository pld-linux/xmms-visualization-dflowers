Summary:	Dual Flowers
Summary(pl):	Podwójny Kwiat
Name:		xmms-visualization-dflowers
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dflowers-v%{version}.tar.gz
# Source0-md5:	6d1d87b1f8dfb3485040d4c82b585481
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xmms_plugin_dir        %(xmms-config --visualization-plugin-dir)

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
install -d $RPM_BUILD_ROOT%{_xmms_plugin_dir}

install *.so $RPM_BUILD_ROOT%{_xmms_plugin_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
