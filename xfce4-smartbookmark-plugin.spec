Summary:	Smart bookmarks for the Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.4.4
Release:	2
Group:		Graphical desktop/Xfce
License:	GPLv2+
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{oname}/%{name}-%{version}.tar.bz2
Patch0:		smartbookmark-mdv-bugzilla.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel
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
%configure2_5x \
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


%changelog
* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-1
+ Revision: 791179
- update to new version 0.4.4
- spec file clean

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added missing BR

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-12mdv2010.1
+ Revision: 543437
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.2-11mdv2010.0
+ Revision: 446134
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-10mdv2009.1
+ Revision: 349478
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-9mdv2009.1
+ Revision: 295027
- rebuild for new Xfce4.6 beta1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-7mdv2009.0
+ Revision: 256940
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-5mdv2008.1
+ Revision: 110137
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- use upstream name

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.4.2-4mdv2008.0
+ Revision: 36216
- rebuild with correct optflags

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - provide P0 (search in mandriva bugzilla)

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-2mdv2008.0
+ Revision: 34778
- correct requires

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.2-1mdv2008.0
+ Revision: 34696
- Import xfce-smartbookmark-plugin

