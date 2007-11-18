%define oname xfce4-smartbookmark-plugin

Summary:	Smart bookmarks for the Xfce panel
Name:		xfce-smartbookmark-plugin
Version:	0.4.2
Release:	%mkrel 4
Group:		Graphical desktop/Xfce
License:	GPL
URL:		http://goodies.xfce.org/projects/panel-plugins/%{oname}
Source0:	http://goodies.xfce.org/releases/%{oname}/%{oname}-%{version}.tar.bz2
Patch0:		smartbookmark-mdv-bugzilla.patch
BuildRequires:	xfce-panel-devel >= 4.4.1
BuildRequires:	perl(XML::Parser)
Requires:	xfce-panel >= 4.4.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin which allows you to do a search directly on Internet on sites like 
Google. It allows you to send requests directly to your browser and perform 
custom searches.

%prep
%setup -qn %{oname}-%{version}
%patch0 -p1

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/panel-plugins/*.desktop
