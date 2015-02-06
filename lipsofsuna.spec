Summary:	Lips of Suna is a tongue-in-cheek dungeon crawl game
Name:		lipsofsuna
Version:	0.8.0
Release:	2
License:	LGPLv3+
Group:		Games/Arcade
Url:		http://sourceforge.net/projects/lipsofsuna/
Source0:	http://sourceforge.net/projects/%{name}/files/%name}/%{version}/%{name}-%{version}.tar.gz
Patch0:		lipsofsuna-0.8.0-linkage.patch
BuildRequires:	boost-devel
BuildRequires:	inotify-tools-devel
BuildRequires:	pkgconfig(bullet)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libenet)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(OGRE)
BuildRequires:	pkgconfig(OIS)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

%description
Lips of Suna is a tongue-in-cheek dungeon crawl game that takes place in the
chaotic dungeons of Suna. The five intelligent races of the world descend to
the dungeons with their goal to save the world from a conclusive disaster.

In your journey to the depths of the dungeons, you will, among other things,
have to fight creatures of different varieties, solve quests, explore new
places, and craft custom items. Luckily you don't need to do all this alone
since you can crawl the dungeons with your friends.

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
./waf configure --prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--bindir=%{_bindir} \
		--disable-relpath

%install
./waf install --destdir=%{buildroot}

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Lips of Suna
Comment=Lips of Suna is a tongue-in-cheek dungeon crawl game
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

