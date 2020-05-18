#
# spec file for package yast2-squid
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-squid
Version:        4.3.0
Release:        0
Summary:        Configuration of squid
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-squid

Source0:        %{name}-%{version}.tar.bz2

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_regex-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
# Yast2::ServiceWidget
BuildRequires:  yast2 >= 4.1.0
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite

Requires:       yast2-ruby-bindings >= 1.0.0
# Yast2::ServiceWidget
Requires:       yast2 >= 4.1.0

%description
Configuration of squid

%prep
%setup -q

%build
%yast_build

%install
%yast_install
rm -rf %{buildroot}/%{yast_plugindir}/libpy2ag_squid.la
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%{yast_plugindir}
%{yast_scrconfdir}
%doc %{yast_docdir}
%license COPYING

%changelog
