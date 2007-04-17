Summary:	A places plugin for the Xfce panel
Name:		xfce4-places-plugin
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-places-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	a000de4adc318337e5b118ecd7e7bc00
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libtool
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xfce4-places-plugin brings much of the functionality of the GNOME
Places menu to Xfce. The plugin looks a lot like a launcher with
multiple items in a menu. The main "launcher" button opens up Thunar
at the user's home directory. The arrow button opens up a menu with
two sections: system- and user-defined locations. The system-defined
locations are consistent with Thunar (including their icons). For
user-defined bookmarks, the ~/.gtk-bookmarks file is being read in
order to share bookmarks with Thunar, Nautilus, the GNOME Panel, etc.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-places-plugin
%{_datadir}/xfce4/panel-plugins/places.desktop
