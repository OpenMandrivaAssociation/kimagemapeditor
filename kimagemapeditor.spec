#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:           kimagemapeditor
Version:	25.12.1
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

Recommends:     %{name}-handbook
Obsoletes:     kdewebdev < 2:16.08.3-3
Provides:     kdewebdev = 2:16.08.3-2

%rename plasma6-kimagemapeditor

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

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
