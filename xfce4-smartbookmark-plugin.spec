%define _disable_rebuild_configure 1
%define url_ver %(echo %version | cut -d. -f1,2)

Summary:	Smart bookmarks for the Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.5.3
Release:	1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		https://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	https://archive.xfce.org/src/panel-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	perl(XML::Parser)
Requires:	xfce4-panel
Obsoletes:	xfce-smartbookmark-plugin

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google. It allows you to send requests directly to your browser and perform 
custom searches.

%prep
%autosetup -p1


%build
%configure \
	--disable-static
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README*
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
