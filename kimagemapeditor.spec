%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:           kimagemapeditor
Version:	23.04.0
Release:	1
Summary:        HTML imagemap editor for KDE
License:        GPLv2+
Group:          Graphical desktop/KDE
Url:            https://www.kde.org/applications/development/kimagemapeditor/
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(openssl)

BuildRequires:  cmake(ECM)

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5WebEngineWidgets)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KDELibs4Support)

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
%_datadir/qlogging-categories5/kimagemapeditor.categories
%_bindir/kimagemapeditor
%{_libdir}/qt5/plugins/kf5/parts/kimagemapeditorpart.so
%_datadir/metainfo/org.kde.kimagemapeditor.appdata.xml
%_datadir/applications/org.kde.kimagemapeditor.desktop
%_kde5_iconsdir/*/*/*/*
%_datadir/kimagemapeditor/
%_datadir/kservices5/kimagemapeditorpart.desktop

#------------------------------------------------------------------------------

%package        handbook
Summary:        Kimagemapeditor handbook
Group:          Documentation
BuildArch:      noarch
Requires:       %{name} >= %{version}-%{release}

Conflicts:      kde-l10n-handbooks-ar < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ast < 17.12.0-1
Conflicts:      kde-l10n-handbooks-bg < 17.12.0-1
Conflicts:      kde-l10n-handbooks-bs < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ca < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ca-valencia < 17.12.0-1
Conflicts:      kde-l10n-handbooks-cs < 17.12.0-1
Conflicts:      kde-l10n-handbooks-da < 17.12.0-1
Conflicts:      kde-l10n-handbooks-de < 17.12.0-1
Conflicts:      kde-l10n-handbooks-el < 17.12.0-1
Conflicts:      kde-l10n-handbooks-en_GB < 17.12.0-1
Conflicts:      kde-l10n-handbooks-en_US < 17.12.0-1
Conflicts:      kde-l10n-handbooks-es < 17.12.0-1
Conflicts:      kde-l10n-handbooks-et < 17.12.0-1
Conflicts:      kde-l10n-handbooks-eu < 17.12.0-1
Conflicts:      kde-l10n-handbooks-fa < 17.12.0-1
Conflicts:      kde-l10n-handbooks-fi < 17.12.0-1
Conflicts:      kde-l10n-handbooks-fr < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ga < 17.12.0-1
Conflicts:      kde-l10n-handbooks-gl < 17.12.0-1
Conflicts:      kde-l10n-handbooks-he < 17.12.0-1
Conflicts:      kde-l10n-handbooks-hi < 17.12.0-1
Conflicts:      kde-l10n-handbooks-hr < 17.12.0-1
Conflicts:      kde-l10n-handbooks-hu < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ia < 17.12.0-1
Conflicts:      kde-l10n-handbooks-id < 17.12.0-1
Conflicts:      kde-l10n-handbooks-is < 17.12.0-1
Conflicts:      kde-l10n-handbooks-it < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ja < 17.12.0-1
Conflicts:      kde-l10n-handbooks-kk < 17.12.0-1
Conflicts:      kde-l10n-handbooks-km < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ko < 17.12.0-1
Conflicts:      kde-l10n-handbooks-lt < 17.12.0-1
Conflicts:      kde-l10n-handbooks-lv < 17.12.0-1
Conflicts:      kde-l10n-handbooks-mr < 17.12.0-1
Conflicts:      kde-l10n-handbooks-nb < 17.12.0-1
Conflicts:      kde-l10n-handbooks-nds < 17.12.0-1
Conflicts:      kde-l10n-handbooks-nl < 17.12.0-1
Conflicts:      kde-l10n-handbooks-nn < 17.12.0-1
Conflicts:      kde-l10n-handbooks-pa < 17.12.0-1
Conflicts:      kde-l10n-handbooks-pl < 17.12.0-1
Conflicts:      kde-l10n-handbooks-pt < 17.12.0-1
Conflicts:      kde-l10n-handbooks-pt_BR < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ro < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ru < 17.12.0-1
Conflicts:      kde-l10n-handbooks-sk < 17.12.0-1
Conflicts:      kde-l10n-handbooks-sl < 17.12.0-1
Conflicts:      kde-l10n-handbooks-sr < 17.12.0-1
Conflicts:      kde-l10n-handbooks-sv < 17.12.0-1
Conflicts:      kde-l10n-handbooks-tr < 17.12.0-1
Conflicts:      kde-l10n-handbooks-ug < 17.12.0-1
Conflicts:      kde-l10n-handbooks-uk < 17.12.0-1
Conflicts:      kde-l10n-handbooks-wa < 17.12.0-1
Conflicts:      kde-l10n-handbooks-zh_CN < 17.12.0-1
Conflicts:      kde-l10n-handbooks-zh_TW < 17.12.0-1

%description    handbook
This package provides kimagemapeditor handbook.

%files handbook
%doc %_kde5_docdir/HTML/*/kimagemapeditor

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %name --all-name
