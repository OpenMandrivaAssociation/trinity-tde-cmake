%define tde_pkg tde-cmake

%define cmake_datadir %{_datadir}/cmake

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.5
Release:	5
Summary:	TDE CMake modules
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


BuildArch:	noarch

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/dependencies/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_ALL_OPTIONS=ON

BuildRequires:	desktop-file-utils

%description
TDE uses its own set of modules and macros to simplify CMake rules.

This also includes the TDEL10n module that is used to generate and
update templates for translations and the modified version of
intltool-merge used to merge translations into desktop files.

%files
%defattr(-,root,root,-)
%{cmake_datadir}/Modules/FindTDE.cmake
%{cmake_datadir}/Modules/FindTQt.cmake
%{cmake_datadir}/Modules/FindTQtQUI.cmake
%{cmake_datadir}/Modules/TDEL10n.cmake
%{cmake_datadir}/Modules/TDEMacros.cmake
%{cmake_datadir}/Modules/TDESetupPaths.cmake
%{cmake_datadir}/Modules/TDEVersion.cmake
%{cmake_datadir}/Modules/tde_automoc.cmake
%{cmake_datadir}/Modules/tde_l10n_merge.pl
%{cmake_datadir}/Modules/tde_uic.cmake
%{cmake_datadir}/Templates/tde_dummy_cpp.cmake
%{cmake_datadir}/Templates/tde_export_library.cmake
%{cmake_datadir}/Templates/tde_libtool_file.cmake
%{cmake_datadir}/Templates/tde_tdeinit_executable.cmake
%{cmake_datadir}/Templates/tde_tdeinit_module.cmake

