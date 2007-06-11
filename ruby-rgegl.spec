Summary:	GEGL module for Ruby
Summary(pl.UTF-8):	Moduł GEGL dla języka Ruby
Name:		ruby-rgegl
Version:	0.0.0.1557
Release:	1
License:	GPL or custom (see COPYING)
Group:		Development/Languages
Source0:	rgegl-%{version}.tar.gz
# Source0-md5:	c4622a0cf604d4813d7d1ec3691f2fb7
URL:		http://gegl.org/rgegl
BuildRequires:	gegl-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEGL module for Ruby.

%description -l pl.UTF-8
Moduł GEGL dla języka Ruby.

%prep
%setup -q -n rgegl-%{version}

%build
ruby extconf.rb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{ruby_rubylibdir}/gegl-view.rb
%{ruby_rubylibdir}/gegl.rb
%attr(755,root,root) %{ruby_archdir}/gegl.so
%{_examplesdir}/%{name}-%{version}
