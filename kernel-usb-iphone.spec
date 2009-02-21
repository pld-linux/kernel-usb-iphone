#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)
#
%define		origname	iphone-module
%define		rel	1

Summary:	iPhone Linux Driver
Summary(de.UTF-8):	iPhone Linux Treiber
Summary(pl.UTF-8):	Sterownik dla Linuksa do iPhona
Name:		kernel%{_alt_kernel}-usb-iphone
Version:	0.3
Release:	%{rel}@%{_kernel_ver_str}
License:	GPL
Group:		Base/Kernel
Source0:	http://matt.colyer.name/projects/%{origname}/%{origname}-%{version}.tar.gz
# Source0-md5:	18d5f51b4c207c1378447c545023576a
URL:		http://matt.colyer.name/projects/iphone-module/
%{?with_dist_kernel:BuildRequires:	kernel-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A kernel module for Linux 2.6.x which allows your iPhone to charge while connected. 
(In the future it will hopefully allow you to access your data.)

%prep
%setup -q -n iphone-module-%{version}

%build
%build_kernel_modules -m iphone

%install
rm -rf $RPM_BUILD_ROOT
%install_kernel_modules -m iphone -d kernel/drivers/usb/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
%doc AUTHORS README HACKING
/lib/modules/%{_kernel_ver}/kernel/drivers/usb/misc/iphone.ko*
