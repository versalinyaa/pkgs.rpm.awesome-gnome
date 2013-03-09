Summary:Gnome integration for awesome
Name: awesome-gnome
Version: 3.5
Release: 0chadv1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://awesomewm.org
BuildArch:noarch
Requires: gnome-session awesome gdm-control

%description
Gnome integration for the awesome window manager

%prep

%build

%install
install -D -m 755 %{_sourcedir}/bin/awesome-gnome $RPM_BUILD_ROOT%{_bindir}/awesome-gnome 
install -D -m 644 %{_sourcedir}/share/xsessions/awesome-gnome.desktop $RPM_BUILD_ROOT/usr/share/xsessions/awesome-gnome.desktop 
install -D -m 644 %{_sourcedir}/share/gnome-session/sessions/awesome-gnome.session $RPM_BUILD_ROOT/usr/share/gnome-session/sessions/awesome-gnome.session
install -D -m 644 %{_sourcedir}/share/applications/awesome-gnome.desktop $RPM_BUILD_ROOT/usr/share/applications/awesome-gnome.desktop 

%post -p /usr/bin/update-desktop-database -q
%postun -p /usr/bin/update-desktop-database -q

%files
%defattr(-,root,root,-)
%{_bindir}/awesome-gnome
/usr/share/applications/awesome-gnome.desktop
/usr/share/gnome-session/sessions/awesome-gnome.session
/usr/share/xsessions/awesome-gnome.desktop

%changelog
* Fri Mar 08 2013 Chad Versace <chad@chad-versace.us> 3.5-0chadv1
- Derive from https://aur.archlinux.org/packages/i3-gnome and
  git://pkgs.fedoraproject.org/openbox-gnome.git .
