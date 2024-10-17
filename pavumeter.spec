Summary:	Volume meter for Pulseaudio sound server for Linux
Name:		pavumeter
Version:	0.9.3
Release:	22
License:	LGPLv2
Group:		Sound
Url:		https://0pointer.de/lennart/projects/pavumeter
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
BuildRequires:	desktop-file-utils
BuildRequires:	desktop-file-utils
BuildRequires:	lynx
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libpulse)
Requires:	pulseaudio
Provides:	pulseaudio-volume-meter

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
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*.desktop

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

