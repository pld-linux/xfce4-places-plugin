Summary:	A places plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka places dla panelu Xfce
Name:		xfce4-places-plugin
Version:	1.3.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-places-plugin/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	d075fffccf44bcf09a1bfcd4e0cd38a2
Patch0:		%{name}-position.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
BuildRequires:	Thunar-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.6.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.8.0
BuildRequires:	libxfce4util-devel >= 4.8.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
Requires:	gvfs
Requires:	xfce4-panel >= 4.8.0
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

%description -l pl.UTF-8
Wtyczka places przenosi dużą część funkcjonalności menu GNOME Places
do Xfce. Wtyczka wygląda w dużej mierze jak launcher z wieloma
elementami w menu. Główny przycisk otwiera Thunara z katalogiem
domowym użytkownika. Przycisk ze strzałką otwiera menu z dwiema
sekcjami: miejscami zdefiniowanymi przez system i użytkownika. Miejsca
zdefiniowane przez system są spójne z Thunarem (włącznie z ikonami).
Dla zakładek zdefiniowanych przez użytkownika odczytywany jest plik
~/.gtk-bookmarks, dzięki czemu są współdzielone z Thunarem,
Nautilusem, panelem GNOME itp.

%prep
%setup -q
# verify if still needed
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
#%attr(755,root,root) %{_bindir}/*
#%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-places-plugin
#%{_datadir}/xfce4/panel-plugins/places.desktop
