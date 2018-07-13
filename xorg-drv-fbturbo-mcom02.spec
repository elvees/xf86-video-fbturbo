Name:	 xorg-drv-fbturbo-mcom02
Version: 0.5.1.1
Release: alt1
ExclusiveArch: armh

Summary: Xorg DDX driver for ARM devices
Group:	 System/X11
License: MIT/X11

Source:  %name-%version.tar

BuildRequires(pre): xorg-sdk
BuildRequires: xorg-scrnsaverproto-devel
BuildRequires: xorg-resourceproto-devel
BuildRequires: xorg-xf86dgaproto-devel
BuildRequires: libdrm-devel
BuildRequires: libump-devel

%description
Video driver, primarily optimized for the devices powered by the Allwinner SoC.

%prep
%setup

%build
%autoreconf
%configure \
    --with-xorg-module-dir=%_x11modulesdir \
    --with-drm-module=vpout-drm
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_x11sysconfdir
cp -b -S %name-backup xorg.conf %buildroot%_x11sysconfdir/xorg.conf

%files
%config %_x11sysconfdir/xorg.conf
%_man4dir/fbturbo.4*
%_x11modulesdir/drivers/*.so

%changelog
* Fri Jul 20 2018 Andrey Solodovnikov <hepoh@altlinux.org> 0.5.1.1-alt1
Set version to 0.5.1.1
Rename package to xorg-drv-fbturbo-mcom02
Use vpout-drm.ko instead of mali_drm.ko

* Thu May 17 2018 Andrey Solodovnikov <hepoh@altlinux.org> 0.5.1.0-alt1
Initial build for ALT

