Name:           samarux-desktop-i3
Version:        0.1
Release:        15
Summary:        samarux-desktop-i3 meta package
License:        GPL
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Packager: 	Enrique Gil (mahoul@gmail.com)
Requires:	samarux-desktop-i3-session, samarux-desktop-lightdm, samarux-desktop-i3-skel, samarux-desktop-i3-scripts, dunst, feh, fira-code-fonts, galculator, gnome-flashback, gnome-session-xsession, gnome-terminal, guake, htop, i3, ImageMagick, lm_sensors, mc, mozilla-fira-sans-fonts, nemo, parcellite, pasystray, pavucontrol, picom, polybar, rofi, vim, xorg-x11-xinit-session
BuildArch:	noarch

%description
Samarux i3 desktop meta package that triggers installation of the rest 
of the required packages (session files and /etc/skel content).

%prep
[ -d %{name} ] && rm -Rfv %{name}
[ -d %{_topdir}/SOURCES ] && rsync -avP --exclude '.git' --delete %{_topdir}/SOURCES/ .


%install

%clean

%files
%defattr(-, root, root)

%changelog
* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-15
- Renamed package to samarux-desktop-i3 and deps

* Sun Apr 11 2021 Enrique Gil (mahoul@gmail.com) - 0.1-14
- Added nemo as dependency

* Sat Apr 10 2021 Enrique Gil (mahoul@gmail.com) - 0.1-13
- Renamed package to samarux-desktop and added galculator dep

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-12
- Removed some dependencies

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-11
- Added vim dependency

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-10
- Removed some dependencies

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-9
- Removed some dependencies

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-8
- Added vim as dependency

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-7
- Added samarux-desktop-scripts as dependency

* Mon Mar 29 2021 Enrique Gil (mahoul@gmail.com) - 0.1-6
- Added gnome-terminal as a dependency

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-5
- Added samarux-desktop-lightdm as dep

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-4
- Removed conflicts entry

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-3
- Added full required package list

* Sun Mar 28 2021 Enrique Gil (mahoul@gmail.com) - 0.1-2
- First package build

* Sat Mar 27 2021 Enrique Gil (mahoul@gmail.com) - 0.1-1
- Initial release.

