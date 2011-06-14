%define Werror_cflags %nil
%define	Summary	Lips of Suna is a tongue-in-cheek dungeon crawl game.

Summary:	%{Summary}
Name:		lipsofsuna
Version:	0.4.0
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/project/lipsofsuna/lipsofsuna/0.4.0/lipsofsuna-0.4.0.tar.gz
URL:		http://www.descent2.de/
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake SDL-devel desktop-file-utils ImageMagick sqlite3-devel bullet-devel
BuildRequires:	SDL_mixer-devel	GL-devel SDL_ttf-devel glew-devel openal-devel libflac-devel libvorbis-devel enet-devel 

%description
Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the chaotic dungeons of Suna. 
The five intelligent races of the world descend to the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things, have to fight creatures of different varieties, 
solve quests, explore new places, and craft custom items. Luckily you don't need to do all this alone since you can crawl the dungeons with your friends.

%prep 
%setup -q


%build
./waf configure build install \
	--relpath=false \
	--bindir=%{buildroot}/%{_gamesbindir} \
	--datadir=%{buildroot}%{_gamesdatadir} \
	--libdir=%{buildroot}%{_gameslibdir}

%install
rm -rf %{buildroot}

cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Lips of Suna
Comment=%{Summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

# install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
# convert -resize 16x16 lipsofsuna-ico-32x32.gif %{buildroot}%{_miconsdir}/%{name}.png
# convert -resize 32x32 lipsofsuna-ico-32x32.gif %{buildroot}%{_iconsdir}/%{name}.png
# convert -resize 48x48 lipsofsuna-ico-64x64.gif %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
# %{_datadir}/applications/mandriva-%{name}.desktop
# %{_miconsdir}/%{name}.png
# %{_iconsdir}/%{name}.png
# %{_liconsdir}/%{name}.png

