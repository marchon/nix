Summary: The Nix software deployment system
Name: nix
Version: 0.5
Release: 1
License: GPL
Group: WeetNiet
URL: http://www.cs.uu.nl/groups/ST/twiki/bin/view/Trace/NixDeploymentSystem
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%define _prefix /nix
Prefix: %{_prefix}

%description

Nix is a software deployment system.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}/bin
%{_prefix}/libexec
%{_prefix}/var
%{_prefix}/share
%{_prefix}/man
%{_prefix}/store
%config
%{_prefix}/etc
#%doc
#%{_prefix}/share/nix/manual
