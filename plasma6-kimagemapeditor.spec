#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:           plasma6-kimagemapeditor
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
Summary:        HTML imagemap editor for KDE
License:        GPLv2+
Group:          Graphical desktop/KDE
Url:            https://www.kde.org/applications/development/kimagemapeditor/
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/kimagemapeditor/-/archive/%{gitbranch}/kimagemapeditor-%{gitbranchd}.tar.bz2#/kimagemapeditor-%{git}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/kimagemapeditor-%{version}.tar.xz
%endif

BuildRequires:  pkgconfig(openssl)

BuildRequires:  cmake(ECM)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

Conflicts:      kde-l10n-ar < 17.12.0-1
Conflicts:      kde-l10n-ast < 17.12.0-1
Conflicts:      kde-l10n-bg < 17.12.0-1
Conflicts:      kde-l10n-bs < 17.12.0-1
Conflicts:      kde-l10n-ca < 17.12.0-1
Conflicts:      kde-l10n-ca-valencia < 17.12.0-1
Conflicts:      kde-l10n-cs < 17.12.0-1
Conflicts:      kde-l10n-da < 17.12.0-1
Conflicts:      kde-l10n-de < 17.12.0-1
Conflicts:      kde-l10n-el < 17.12.0-1
Conflicts:      kde-l10n-en_GB < 17.12.0-1
Conflicts:      kde-l10n-en_US < 17.12.0-1
Conflicts:      kde-l10n-es < 17.12.0-1
Conflicts:      kde-l10n-et < 17.12.0-1
Conflicts:      kde-l10n-eu < 17.12.0-1
Conflicts:      kde-l10n-fa < 17.12.0-1
Conflicts:      kde-l10n-fi < 17.12.0-1
Conflicts:      kde-l10n-fr < 17.12.0-1
Conflicts:      kde-l10n-ga < 17.12.0-1
Conflicts:      kde-l10n-gl < 17.12.0-1
Conflicts:      kde-l10n-he < 17.12.0-1
Conflicts:      kde-l10n-hi < 17.12.0-1
Conflicts:      kde-l10n-hr < 17.12.0-1
Conflicts:      kde-l10n-hu < 17.12.0-1
Conflicts:      kde-l10n-ia < 17.12.0-1
Conflicts:      kde-l10n-id < 17.12.0-1
Conflicts:      kde-l10n-is < 17.12.0-1
Conflicts:      kde-l10n-it < 17.12.0-1
Conflicts:      kde-l10n-ja < 17.12.0-1
Conflicts:      kde-l10n-kk < 17.12.0-1
Conflicts:      kde-l10n-km < 17.12.0-1
Conflicts:      kde-l10n-ko < 17.12.0-1
Conflicts:      kde-l10n-lt < 17.12.0-1
Conflicts:      kde-l10n-lv < 17.12.0-1
Conflicts:      kde-l10n-mr < 17.12.0-1
Conflicts:      kde-l10n-nb < 17.12.0-1
Conflicts:      kde-l10n-nds < 17.12.0-1
Conflicts:      kde-l10n-nl < 17.12.0-1
Conflicts:      kde-l10n-nn < 17.12.0-1
Conflicts:      kde-l10n-pa < 17.12.0-1
Conflicts:      kde-l10n-pl < 17.12.0-1
Conflicts:      kde-l10n-pt < 17.12.0-1
Conflicts:      kde-l10n-pt_BR < 17.12.0-1
Conflicts:      kde-l10n-ro < 17.12.0-1
Conflicts:      kde-l10n-ru < 17.12.0-1
Conflicts:      kde-l10n-sk < 17.12.0-1
Conflicts:      kde-l10n-sl < 17.12.0-1
Conflicts:      kde-l10n-sr < 17.12.0-1
Conflicts:      kde-l10n-sv < 17.12.0-1
Conflicts:      kde-l10n-tr < 17.12.0-1
Conflicts:      kde-l10n-ug < 17.12.0-1
Conflicts:      kde-l10n-uk < 17.12.0-1
Conflicts:      kde-l10n-wa < 17.12.0-1
Conflicts:      kde-l10n-zh_CN < 17.12.0-1
Conflicts:      kde-l10n-zh_TW < 17.12.0-1

Recommends:     %{name}-handbook
Obsoletes:     kdewebdev < 2:16.08.3-3
Provides:     kdewebdev = 2:16.08.3-2

%description
KImageMapEditor is an HTML imagemap editor for KDE. It allows you to create and
modify HTML imagemaps.

%files -f %name.lang
%_datadir/qlogging-categories6/kimagemapeditor.categories
%_bindir/kimagemapeditor
%{_libdir}/qt6/plugins/kf6/parts/kimagemapeditorpart.so
%_datadir/metainfo/org.kde.kimagemapeditor.appdata.xml
%_datadir/applications/org.kde.kimagemapeditor.desktop
%_iconsdir/*/*/*/*
%_datadir/kimagemapeditor/

#------------------------------------------------------------------------------

%package        handbook
Summary:        Kimagemapeditor handbook
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} >= %{version}-%{release}

%description    handbook
This package provides kimagemapeditor handbook.

%files handbook
%doc %_docdir/HTML/*/kimagemapeditor

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kimagemapeditor-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %name --all-name
