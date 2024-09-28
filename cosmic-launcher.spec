%undefine _debugsource_packages

%define         appname com.system76.CosmicLauncher
Name:           cosmic-launcher
Version:        1.0.0
Release:        0.alpha2.0
Summary:        Layer Shell frontend
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-launcher
Source0:        https://github.com/pop-os/cosmic-launcher/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  just
BuildRequires:  mold
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
Layer Shell frontend for pop-launcher. Currently
the underlying protocol being used in the plugin for managing toplevels
in wayland is defined here but it will be switched to use wlr-foreign-toplevel-management
when it is ready.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.2 -a1 -p1
rm -rf .cargo
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
