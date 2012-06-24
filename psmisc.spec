Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(fr):	Autres outils du type ps pour le syst�me de fichiers /proc
Summary(pl):	Narz�dzia do kontroli proces�w
Summary(tr):	/proc dosya sistemi i�in ps tipi ara�lar
Name:		psmisc
Version:	18
Release:	6
Copyright:	distributable
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source:		ftp://lrcftp.epfl.ch/pub/linux/local/psmisc/%{name}-%{version}.tar.gz
Patch0:		psmisc-opt.patch
Patch1:		psmisc-ncurses.patch
BuildRequires:	ncurses-devel >= 5.0
Buildroot:	/tmp/%{name}-%{version}-root

%define		_sbindir	/sbin

%description
The psmisc package contains utilities for managing processes on your system:
pstree, killall and fuser. The pstree command displays a tree structure of
all of the running processes on your system. The killall command sends a
specified signal (SIGTERM if nothing is specified) to processes identified
by name. The fuser command identifies the PIDs of processes that are using
specified files or filesystems.

%description -l de
Das psmisc-Paket enth�lt Utilities zum Verwalten vom Prozessen auf Ihrem
System: pstree, killall und fuser. Der pstree-Befehl zeigt eine Baumstruktur
von allen laufenden Prozessen an. killall schickt angegebenen Programmen ein
Signal (SIGTERM, falls nichts anderes angegeben wird). fuser identifiziert
die PIDs (Prozess-IDs) von Prozessen, die bestimmte Dateien oder
Dateisysteme benutzen.

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo�liwiaj�ce wy�wietlienie drzewa proces�w, 
znalezienie u�ytkownika, kt�ry otworzy� dany plik i wys�anie sygna�u do
procesu o zadanej nazwie.

%description -l tr
Bu paket, s�re�lerin a�a� yap�s�n� g�stermek, hangi kullan�c�lar�n a��k
dosyas� oldu�unu bulmak ve s�re�lere isimleri ile sinyal g�ndermek i�in
gerekli programlar� i�erir.

%prep
%setup  -q -n %{name}
%patch0 -p1 
%patch1 -p1

%build
make LDFLAGS="-s" OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,%{_sbindir},%{_bindir},%{_mandir}/man1}

install -s fuser $RPM_BUILD_ROOT%{_sbindir}
install -s {killall,pstree} $RPM_BUILD_ROOT%{_bindir}

install {fuser,killall,pstree}.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_sbindir}/fuser
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
