%define name pavumeter
%define version 0.9.2
%define release %mkrel 2
%define title Pulseaudio Volume Meter
%define longtitle Volume meter for Pulseaudio sound server for Linux

Summary: Volume meter for Pulseaudio sound server for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: LGPL
Group: Sound
Url: http://0pointer.de/lennart/projects/pavumeter
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel
BuildRequires: libglademm2.4-devel
BuildRequires: libpulseaudio-devel
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
#export CPPFLAGS=-I%_includedir/alsa
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%_bindir/%name
%_datadir/applications/%name.desktop


