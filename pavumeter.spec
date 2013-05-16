%define title Pulseaudio Volume Meter
%define longtitle Volume meter for Pulseaudio sound server for Linux

Summary:	Volume meter for Pulseaudio sound server for Linux
Name:		pavumeter
Version:	0.9.3
Release:	11
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
License:	LGPL
Group:		Sound
Url:		http://0pointer.de/lennart/projects/pavumeter
BuildRequires:	gtkmm2.4-devel
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	desktop-file-utils
BuildRequires:	lynx
BuildRequires:	desktop-file-utils
Requires:		pulseaudio
Provides:		pulseaudio-volume-meter

%description
Pulseaudio Volume Meter (pavumeter) is a simple GTK volume meter 
for the Pulseaudio sound server.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

sed -i "s/^Icon=.*/Icon=%{name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i "s/^Icon=.*/Icon=%{name}-record/" %{buildroot}%{_datadir}/applications/%{name}-record.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*.desktop

# Icons
install -D -m 0644 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 0644 %SOURCE2 %{buildroot}%{_iconsdir}/%{name}.png
ln -s %{name}.png %{buildroot}%{_miconsdir}/%{name}-record.png
ln -s %{name}.png %{buildroot}%{_iconsdir}/%{name}-record.png

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-record.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}-record.png
%{_iconsdir}/%{name}-record.png




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-8mdv2011.0
+ Revision: 666993
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-7mdv2011.0
+ Revision: 607076
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-6mdv2010.1
+ Revision: 523605
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.3-5mdv2010.0
+ Revision: 426357
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.3-4mdv2009.0
+ Revision: 218428
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 31 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.3-4mdv2008.1
+ Revision: 160894
- Fix %%postun (#37210)

* Wed Jan 16 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.3-3mdv2008.1
+ Revision: 153655
- Fix %%post[un] macros
- Add GTK category for consistency with the other pa apps

* Tue Jan 15 2008 Colin Guthrie <cguthrie@mandriva.org> 0.9.3-2mdv2008.1
+ Revision: 151973
- Add icons for x-desktop use (MDV#36579)
- Add BuildRequires on libpulse-devel >= 0.9.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.3-1mdv2008.1
+ Revision: 103915
- New version


* Mon Feb 05 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.2-2mdv2007.0
+ Revision: 116261
- Import pavumeter

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.0
- rebuild for new cairomm

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.0
- fix menu
- update deps
- New release 0.9.2

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-6mdv2007.0
- don't update the desktop database, as the menu contains no mime types
- fix menu
- fix buildrequires

* Fri Jun 16 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-5mdv2007.0
- fix buildrequires

* Sat Jun 10 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-4mdv2007.0
- fix deps

* Tue Jun 06 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-3mdv2007.0
- Fix title and longtitle
- Fix Provides

* Mon Jun 05 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-2mdv2007.0
- Fix URL

* Mon Jun 05 2006 Jerome Soyer <saispo@mandriva.org> 0.9.0-1mdv2007.0
- Initial Package for Mandriva

