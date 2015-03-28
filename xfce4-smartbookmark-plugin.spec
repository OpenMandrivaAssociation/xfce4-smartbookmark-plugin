Summary:	Smart bookmarks for the Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.4.6
Release:	1
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{oname}/%{name}-%{version}.tar.bz2
Patch0:		smartbookmark-mdv-bugzilla.patch
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	perl(XML::Parser)
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-smartbookmark-plugin

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google. It allows you to send requests directly to your browser and perform 
custom searches.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/panel-plugins/*.desktop
