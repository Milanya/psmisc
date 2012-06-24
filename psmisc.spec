#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(es):	M�s herramientas de tipo ps para el sistema de archivos /proc
Summary(fr):	Autres outils du type ps pour le syst�me de fichiers /proc
Summary(ko):	�ý��ۿ��� ���μ����� �����ϴ� ����
Summary(pl):	Narz�dzia do kontroli proces�w
Summary(pt_BR):	Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(ru):	������� ������ � ����������
Summary(tr):	/proc dosya sistemi i�in ps tipi ara�lar
Summary(uk):	���̦�� ������ � ���������
Name:		psmisc
Version:	22.3
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
# Source0-md5:	0c44b995d068a221daf35d23e13db419
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9add7665e440bbd6b0b4f9293ba8b86d
Patch0:		%{name}-AM_INTL.patch
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-devel >= 0.14.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	ncurses-devel >= 5.0
Conflicts:	rc-scripts < 0.4.1.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%description -l de
Das psmisc-Paket enth�lt Utilities zum Verwalten vom Prozessen auf
Ihrem System: pstree, killall und fuser. Der pstree-Befehl zeigt eine
Baumstruktur von allen laufenden Prozessen an. killall schickt
angegebenen Programmen ein Signal (SIGTERM, falls nichts anderes
angegeben wird). fuser identifiziert die PIDs (Prozess-IDs) von
Prozessen, die bestimmte Dateien oder Dateisysteme benutzen.

%description -l es
Este paquete contiene programas para ense�ar un �rbol de procesos,
saber que usuarios tienen archivo abierto y mandar se�ales a los
procesos por nombre.

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo�liwiaj�ce wy�wietlenie drzewa
proces�w, znalezienie u�ytkownika, kt�ry otworzy� dany plik i wys�anie
sygna�u do procesu o zadanej nazwie.

%description -l pt_BR
Este pacote cont�m programas para mostrar uma �rvore de processos,
saber quais usu�rios t�m arquivo aberto e mandar sinais aos processos
por nome.

%description -l ru
� ���� ����� �������� ��������� ��� ����������� ������ ���������,
��������� ���������� � ���, ��� ������ ���� � ��� ������� ��������
��������� �� ����� ��������.

%description -l tr
Bu paket, s�re�lerin a�a� yap�s�n� g�stermek, hangi kullan�c�lar�n
a��k dosyas� oldu�unu bulmak ve s�re�lere isimleri ile sinyal
g�ndermek i�in gerekli programlar� i�erir.

%description -l uk
��� ����� ͦ����� �������� ��� צ���������� ������ �����Ӧ�, �������
�����̦� �������� �� ���Φ ������� �� ��������� �������æ� ��� ��, ���
צ����� ����.

%prep
%setup -q
%patch0 -p0

%build
%{__gettextize}
%{__aclocal}
%{__autoconf} -I m4
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I/usr/include/ncurses"
%configure \
	%{?with_selinux:--enable-selinux}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/README.psmisc-non-english-man-pages

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS Chang* NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
