%define name pavumeter
%define version 0.9.3
%define release %mkrel 7
%define title Pulseaudio Volume Meter
%define longtitle Volume meter for Pulseaudio sound server for Linux

Summary: Volume meter for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-16.png
Source2: %{name}-32.png
License: LGPL
Group: Sound
Url: http://0pointer.de/lennart/projects/pavumeter
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel
BuildRequires: libglademm2.4-devel
BuildRequires: libpulseaudio-devel >= 0.9.7
BuildRequires: desktop-file-utils
BuildRequires: lynx
BuildRequires: desktop-file-utils
Requires: pulseaudio
Provides: pulseaudio-volume-meter

%description
Pulseaudio Volume Meter (pavumeter) is a simple GTK volume meter 
for the Pulseaudio sound server.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
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

%if %mdkversion < 200900
%post
%update_desktop_database
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_desktop_database
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-record.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}-record.png
%{_iconsdir}/%{name}-record.png


