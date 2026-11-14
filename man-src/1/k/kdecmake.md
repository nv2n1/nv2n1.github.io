---
title: "kdecmake(1)"
name: "kdecmake"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kdecmake/"
description: "kdecmake – Reference of available CMake custom modules."
---

<h2>NAME</h2>
<p> kdecmake &#8211; Reference of available CMake custom modules. </p>
<h2>DESCRIPTION</h2>
<p> The &quot;cmake&quot; executable is the CMake command-line interface. It may be used to configure projects in scripts. Project configuration settings may be specified on the command line with the -D option. The -i option will cause cmake to interactively prompt for such settings. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform. </p>
<h2>CUSTOM MODULES</h2>
<p> The following modules are also available for CMake. They can be used with INCLUDE(ModuleName). </p>
<pre>
  Custom CMake Modules - Additional Modules for CMake.
</pre>
<p> This is the documentation for additional modules and scripts for CMake. Using these modules you can check the computer system for installed software packages, features of the compiler and the existance of headers to name just a few. </p>
<dl>
<dt><code>CheckCXXSourceCompiles</code></p>
<dd> macro which checks if the source code compiles </p>
<p> CHECK_CXX_SOURCE_COMPILES(SOURCE VAR) </p>
<pre>
  SOURCE - source code to try to compile
  VAR    - variable to store whether the source code compiled
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXSourceRuns</code></p>
<dd> Check if the C++ source code provided in the SOURCE argument compiles and runs. </p>
<p> CHECK_CXX_SOURCE_RUNS(SOURCE VAR) </p>
<pre>
  SOURCE - source code to try to compile
  VAR    - variable to store the result, 1 for success, empty for failure
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXSymbolExists</code></p>
<dd> Check if the symbol exists in include files, in C++ mode </p>
<p> Forked off cmake&#8217;s CheckSymbolExists.cmake CHECK_CXX_SYMBOL_EXISTS(SYMBOL FILES VARIABLE) </p>
<pre>
  SYMBOL   - symbol
  FILES    - include files to check
  VARIABLE - variable to return result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckPointerMember</code></p>
<dd> Check if the given struct or class has the specified member variable </p>
<p> CHECK_POINTER_MEMBER (POINTER MEMBER HEADER VARIABLE) </p>
<pre>
  POINTER - the name of the struct or class you are interested in
  MEMBER - the member which existence you want to check
  HEADER - the header(s) where the prototype should be declared
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckPrototypeExists</code></p>
<dd> Check if the prototype for a function exists. </p>
<p> CHECK_PROTOTYPE_EXISTS (FUNCTION HEADER VARIABLE) </p>
<pre>
  FUNCTION - the name of the function you are looking for
  HEADER - the header(s) where the prototype should be declared
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckStructMember</code></p>
<dd> Check if the given struct or class has the specified member variable </p>
<p> CHECK_STRUCT_MEMBER (STRUCT MEMBER HEADER VARIABLE) </p>
<pre>
  STRUCT - the name of the struct or class you are interested in
  MEMBER - the member which existence you want to check
  HEADER - the header(s) where the prototype should be declared
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>FindACL</code></p>
<dd> Try to find the ACL library </p>
<p> Once done this will define </p>
<pre>
  ACL_FOUND - system has the ACL library
  ACL_LIBS - The libraries needed to use ACL
</pre>
<dt><code>FindAGG</code></p>
<dd> Try to find the AGG graphics library </p>
<p> Once done this will define </p>
<pre>
  AGG_FOUND - system has AGG
  AGG_INCLUDE_DIR - the AGG include directory
  AGG_LIBRARIES - Link these to use AGG
  AGG_DEFINITIONS - Compiler switches required for using AGG
</pre>
<dt><code>FindAkode</code></p>
<dd> Try to find the aKode library </p>
<p> Once done this will define </p>
<pre>
  AKODE_FOUND - system has the aKode library
  AKODE_INCLUDE_DIR - the aKode include directory
  AKODE_LIBRARIES - The libraries needed to use aKode
</pre>
<dt><code>FindAlsa</code></p>
<dd>
<p> Alsa check, based on libkmid/configure.in.in. Only the support for Alsa &gt;= 0.9.x was included; 0.5.x was dropped (but feel free to re-add it if you need it) It defines &#8230; It offers the following macros: </p>
<pre>
  ALSA_CONFIGURE_FILE(config_header) - generate a config.h, typical usage: 
                                       ALSA_CONFIGURE_FILE(${CMAKE_BINARY_DIR}/config-alsa.h)
  ALSA_VERSION_STRING(version_string)  looks for alsa/version.h and reads the version string into
                                       the first argument passed to the macro
</pre>
<dt><code>FindAutomoc4</code></p>
<dd> Try to find automoc4 </p>
<p> Once done this will define </p>
<pre>
  AUTOMOC4_FOUND - automoc4 has been found
  AUTOMOC4_EXECUTABLE - the automoc4 tool
  AUTOMOC4_VERSION - the full version of automoc4
  AUTOMOC4_VERSION_MAJOR, AUTOMOC4_VERSION_MINOR, AUTOMOC4_VERSION_PATCH - AUTOMOC4_VERSION 
                     broken into its components
</pre>
<p> It also adds the following macros </p>
<pre>
  AUTOMOC4(&lt;target&gt; &lt;SRCS_VAR&gt;)
    Use this to run automoc4 on all files contained in the list &lt;SRCS_VAR&gt;.
</pre>
<pre>
  AUTOMOC4_MOC_HEADERS(&lt;target&gt; header1.h header2.h ...)
    Use this to add more header files to be processed with automoc4.
</pre>
<pre>
  AUTOMOC4_ADD_EXECUTABLE(&lt;target_NAME&gt; src1 src2 ...)
    This macro does the same as ADD_EXECUTABLE, but additionally
    adds automoc4 handling for all source files.
</pre>
<p> AUTOMOC4_ADD_LIBRARY(&lt;target_NAME&gt; src1 src2 &#8230;) </p>
<pre>
    This macro does the same as ADD_LIBRARY, but additionally
    adds automoc4 handling for all source files.
</pre>
<dt><code>FindAvahi</code></p>
<dd>
<p> Find Avahi. Only avahi-common/defs.h is really needed </p>
<dt><code>FindBerkeleyDB</code></p>
<dd> Try to find Berkeley DB </p>
<p> Once done this will define </p>
<pre>
  BERKELEY_DB_FOUND - system has Berkeley DB
  BERKELEY_DB_INCLUDE_DIR - the Berkeley DB include directory
  BERKELEY_DB_LIBRARIES - Link these to use Berkeley DB
  BERKELEY_DB_DEFINITIONS - Compiler switches required for using Berkeley DB
</pre>
<dt><code>FindBlitz</code></p>
<dd> Try to find blitz lib </p>
<p> ########################################################## ######## DEPRECATED, use FindQImageBlitz instead ######### ########################################################## Once done this will define </p>
<pre>
  BLITZ_FOUND - system has blitz lib
  BLITZ_INCLUDES - the blitz include directory
  BLITZ_LIBRARIES - The libraries needed to use blitz
</pre>
<dt><code>FindBlueZ</code></p>
<dd> Try to find BlueZ </p>
<p> Once done this will define </p>
<pre>
  BLUEZ_FOUND - system has BlueZ
  BLUEZ_INCLUDE_DIR - the BlueZ include directory
  BLUEZ_LIBRARIES - Link these to use BlueZ
  BLUEZ_DEFINITIONS - Compiler switches required for using BlueZ
</pre>
<p> Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<dt><code>FindBoost</code></p>
<dd> Try to find Boost include dirs and libraries </p>
<p> Please see the Documentation for Boost in the CMake Manual for details This module only forwards to the one included in cmake for compatibility reasons. </p>
<dt><code>FindCarbon</code></p>
<dd> Find Carbon on Mac </p>
<pre>
  CARBON_LIBRARY - the library to use Carbon
  CARBON_FOUND - true if Carbon has been found
</pre>
<dt><code>FindDNSSD</code></p>
<dd> Try to find DNSSD </p>
<p> Once done this will define </p>
<pre>
  DNSSD_FOUND - system has DNSSD
  DNSSD_INCLUDE_DIR - the DNSSD include directory
  DNSSD_LIBRARIES - Link these to use dnssd
  DNSSD_DEFINITIONS - Compiler switches required for using DNSSD
</pre>
<p> need more test: look at into dnssd/configure.in.in </p>
<dt><code>FindENCHANT</code></p>
<dd> Try to find the Enchant spell checker </p>
<p> Once done this will define </p>
<pre>
  ENCHANT_FOUND - system has ENCHANT
  ENCHANT_INCLUDE_DIR - the ENCHANT include directory
  ENCHANT_LIBRARIES - Link these to use ENCHANT
  ENCHANT_DEFINITIONS - Compiler switches required for using ENCHANT
</pre>
<dt><code>FindEigen</code></p>
<dd> Try to find Eigen1 library </p>
<p> Note that Eigen1 is deprecated in favor of Eigen2. So this file is deprecated in favor of FindEigen2.cmake. It is kept only for compatibility. </p>
<p> Once done this will define </p>
<pre>
  EIGEN_FOUND - system has eigen lib
  EIGEN_INCLUDE_DIR - the eigen include directory
</pre>
<dt><code>FindEigen2</code></p>
<dd> Try to find Eigen2 lib </p>
<p> This module supports requiring a minimum version, e.g. you can do </p>
<pre>
   find_package(Eigen2 2.0.3)
</pre>
<p> to require version 2.0.3 to newer of Eigen2. </p>
<p> Once done this will define </p>
<pre>
  EIGEN2_FOUND - system has eigen lib with correct version
  EIGEN2_INCLUDE_DIR - the eigen include directory
  EIGEN2_VERSION - eigen version
</pre>
<dt><code>FindExiv2</code></p>
<dd> Try to find the Exiv2 library </p>
<pre>
  EXIV2_MIN_VERSION - You can set this variable to the minimum version you need 
                      before doing FIND_PACKAGE(Exiv2). The default is 0.12.
</pre>
<p> Once done this will define </p>
<pre>
  EXIV2_FOUND - system has libexiv2
  EXIV2_INCLUDE_DIR - the libexiv2 include directory
  EXIV2_LIBRARIES - Link these to use libexiv2
  EXIV2_DEFINITIONS - Compiler switches required for using libexiv2
</pre>
<dt><code>FindFAM</code></p>
<dd> Try to find the FAM directory notification library </p>
<p> Once done this will define </p>
<pre>
  FAM_FOUND - system has FAM
  FAM_INCLUDE_DIR - the FAM include directory
  FAM_LIBRARIES - The libraries needed to use FAM
</pre>
<dt><code>FindFFmpeg</code></p>
<dd> Try to find ffmpeg </p>
<p> Once done this will define </p>
<pre>
  FFMPEG_FOUND - system has ffmpeg
  FFMPEG_INCLUDE_DIR - Include directory necessary for using the ffmpeg headers
  FFMPEG_LIBRARIES - Link these to use ffmpeg
  FFMPEG_DEFINITIONS - Compiler switches required for using ffmpeg
</pre>
<dt><code>FindFlac</code></p>
<dd> Try to find Flac, the Free Lossless Audio Codec </p>
<p> Once done this will define </p>
<pre>
  FLAC_FOUND - system has Flac
  FLAC_INCLUDE_DIR - the Flac include directory
  FLAC_LIBRARIES - Link these to use Flac
  FLAC_OGGFLAC_LIBRARIES - Link these to use OggFlac
</pre>
<p> No version checking is done &#8211; use FLAC_API_VERSION_CURRENT to conditionally compile version-dependent code </p>
<dt><code>FindFlex</code></p>
<dd> Try to find Flex </p>
<p> Once done this will define </p>
<pre>
  FLEX_FOUND - system has Flex
  FLEX_EXECUTABLE - path of the flex executable
  FLEX_VERSION - the version string, like &quot;2.5.31&quot;
</pre>
<dt><code>FindFontconfig</code></p>
<dd> Try to find the Fontconfig </p>
<p> Once done this will define </p>
<pre>
  FONTCONFIG_FOUND - system has Fontconfig
  FONTCONFIG_INCLUDE_DIR - The include directory to use for the fontconfig headers
  FONTCONFIG_LIBRARIES - Link these to use FONTCONFIG
  FONTCONFIG_DEFINITIONS - Compiler switches required for using FONTCONFIG
</pre>
<dt><code>FindFreetype</code></p>
<dd> Try to find the freetype library </p>
<p> Once done this will define </p>
<pre>
  FREETYPE_FOUND - system has Freetype
  FREETYPE_INCLUDE_DIRS - the FREETYPE include directories
  FREETYPE_LIBRARIES - Link these to use FREETYPE
  FREETYPE_INCLUDE_DIR - internal
</pre>
<dt><code>FindGIF</code></p>
<dd> Try to find GIF </p>
<p> Once done this will define </p>
<pre>
  GIF_FOUND - system has GIF
  GIF_INCLUDE_DIR - the GIF include directory
  GIF_LIBRARIES - Libraries needed to use GIF
  GIF_DEFINITIONS - Compiler switches required for using GIF
</pre>
<dt><code>FindGLIB2</code></p>
<dd> Try to find the GLIB2 libraries </p>
<p> Once done this will define </p>
<pre>
  GLIB2_FOUND - system has glib2
  GLIB2_INCLUDE_DIR - the glib2 include directory
  GLIB2_LIBRARIES - glib2 library
</pre>
<dt><code>FindGMP</code></p>
<dd>
<p> Try to find the GMP librairies </p>
<pre>
  GMP_FOUND - system has GMP lib
  GMP_INCLUDE_DIR - the GMP include directory
  GMP_LIBRARIES - Libraries needed to use GMP
</pre>
<dt><code>FindGObject</code></p>
<dd> Try to find GObject </p>
<p> Once done this will define </p>
<pre>
  GOBJECT_FOUND - system has GObject
  GOBJECT_INCLUDE_DIR - the GObject include directory
  GOBJECT_LIBRARIES - the libraries needed to use GObject
  GOBJECT_DEFINITIONS - Compiler switches required for using GObject
</pre>
<dt><code>FindGSSAPI</code></p>
<dd> Try to detect the GSSAPI support </p>
<p> Once done this will define </p>
<pre>
  GSSAPI_FOUND - system supports GSSAPI
  GSSAPI_INCS - the GSSAPI include directory
  GSSAPI_LIBS - the libraries needed to use GSSAPI
  GSSAPI_FLAVOR - the type of API - MIT or HEIMDAL
</pre>
<dt><code>FindGStreamer</code></p>
<dd> Try to find GStreamer </p>
<p> Once done this will define </p>
<pre>
  GSTREAMER_FOUND - system has GStreamer
  GSTREAMER_INCLUDE_DIR - the GStreamer include directory
  GSTREAMER_LIBRARIES - the libraries needed to use GStreamer
  GSTREAMER_DEFINITIONS - Compiler switches required for using GStreamer
</pre>
<dt><code>FindGettext</code></p>
<dd>
<p> Try to find Gettext functionality Once done this will define </p>
<pre>
  GETTEXT_FOUND - system has Gettext
  GETTEXT_INCLUDE_DIR - Gettext include directory
  GETTEXT_LIBRARIES - Libraries needed to use Gettext
</pre>
<dt><code>FindGphoto2</code></p>
<dd>
<p> cmake macro to test if we use gphoto2 </p>
<pre>
  GPHOTO2_FOUND - system has the GPHOTO2 library
  GPHOTO2_INCLUDE_DIR - the GPHOTO2 include directory
  GPHOTO2_LIBRARIES - The libraries needed to use GPHOTO2
</pre>
<dt><code>FindHUNSPELL</code></p>
<dd> Try to find HUNSPELL </p>
<p> Once done this will define </p>
<pre>
  HUNSPELL_FOUND - system has HUNSPELL
  HUNSPELL_INCLUDE_DIR - the HUNSPELL include directory
  HUNSPELL_LIBRARIES - The libraries needed to use HUNSPELL
  HUNSPELL_DEFINITIONS - Compiler switches required for using HUNSPELL
</pre>
<dt><code>FindIOKit</code></p>
<dd> Find IOKit on Mac </p>
<pre>
  IOKIT_LIBRARY - the library to use IOKit
  IOKIT_FOUND - true if IOKit has been found
</pre>
<dt><code>FindKDE4Internal</code></p>
<dd> Find the KDE4 include and library dirs, KDE preprocessors and define a some macros </p>
<p> This module defines the following variables: </p>
<pre>
  KDE4_FOUND               - set to TRUE if everything required for building KDE software has been found
</pre>
<pre><code>
  KDE4_DEFINITIONS         - compiler definitions required for compiling KDE software
  KDE4_INCLUDE_DIR         - the KDE 4 include directory
  KDE4_INCLUDES            - all include directories required for KDE, i.e.
                             KDE4_INCLUDE_DIR, but also the Qt4 include directories
                             and other platform specific include directories
  KDE4_LIB_DIR             - the directory where the KDE libraries are installed,
                             intended to be used with LINK_DIRECTORIES()
</code></pre>
<p> The following variables are defined for the various tools required to compile KDE software: </p>
<pre>
  KDE4_KCFGC_EXECUTABLE    - the kconfig_compiler4 executable
  KDE4_AUTOMOC_EXECUTABLE  - the kde4automoc executable, deprecated, use AUTOMOC4_EXECUTABLE instead
  KDE4_MEINPROC_EXECUTABLE - the meinproc4 executable
  KDE4_MAKEKDEWIDGETS_EXECUTABLE - the makekdewidgets4 executable
</pre>
<p> The following variables point to the location of the KDE libraries, but shouldn&#8217;t be used directly: </p>
<pre>
  KDE4_KDECORE_LIBRARY     - the kdecore library
  KDE4_KDEUI_LIBRARY       - the kdeui library
  KDE4_KIO_LIBRARY         - the kio library
  KDE4_KPARTS_LIBRARY      - the kparts library
  KDE4_KUTILS_LIBRARY      - the kutils library
  KDE4_KDE3SUPPORT_LIBRARY - the kde3support library
  KDE4_KFILE_LIBRARY       - the kfile library
  KDE4_KHTML_LIBRARY       - the khtml library
  KDE4_KJS_LIBRARY         - the kjs library
  KDE4_KJSAPI_LIBRARY      - the kjs public api library
  KDE4_KNEWSTUFF2_LIBRARY  - the knewstuff2 library
  KDE4_KNEWSTUFF3_LIBRARY  - the knewstuff3 library
  KDE4_KDNSSD_LIBRARY      - the kdnssd library
  KDE4_PHONON_LIBRARY      - the phonon library
  KDE4_THREADWEAVER_LIBRARY- the threadweaver library
  KDE4_SOLID_LIBRARY       - the solid library
  KDE4_KNOTIFYCONFIG_LIBRARY- the knotifyconfig library
  KDE4_KROSSCORE_LIBRARY   - the krosscore library
  KDE4_KTEXTEDITOR_LIBRARY - the ktexteditor library
  KDE4_NEPOMUK_LIBRARY     - the nepomuk library
  KDE4_PLASMA_LIBRARY      - the plasma library
  KDE4_KUNITCONVERSION_LIBRARY - the kunitconversion library
  KDE4_KDEWEBKIT_LIBRARY   - the kdewebkit library
</pre>
<pre>
  KDE4_PLASMA_OPENGL_FOUND  - TRUE if the OpenGL support of Plasma has been found, NOTFOUND otherwise
</pre>
<p> Compared to the variables above, the following variables also contain all of the depending libraries, so the variables below should be used instead of the ones above: </p>
<pre>
  KDE4_KDECORE_LIBS          - the kdecore library and all depending libraries
  KDE4_KDEUI_LIBS            - the kdeui library and all depending libraries
  KDE4_KIO_LIBS              - the kio library and all depending libraries
  KDE4_KPARTS_LIBS           - the kparts library and all depending libraries
  KDE4_KUTILS_LIBS           - the kutils library and all depending libraries
  KDE4_KDE3SUPPORT_LIBS      - the kde3support library and all depending libraries
  KDE4_KFILE_LIBS            - the kfile library and all depending libraries
  KDE4_KHTML_LIBS            - the khtml library and all depending libraries
  KDE4_KJS_LIBS              - the kjs library and all depending libraries
  KDE4_KJSAPI_LIBS           - the kjs public api library and all depending libraries
  KDE4_KNEWSTUFF2_LIBS       - the knewstuff2 library and all depending libraries
  KDE4_KNEWSTUFF3_LIBS       - the knewstuff3 library and all depending libraries
  KDE4_KDNSSD_LIBS           - the kdnssd library and all depending libraries
  KDE4_KDESU_LIBS            - the kdesu library and all depending libraries
  KDE4_KPTY_LIBS             - the kpty library and all depending libraries
  KDE4_PHONON_LIBS           - the phonon library and all depending librairies
  KDE4_THREADWEAVER_LIBRARIES- the threadweaver library and all depending libraries
  KDE4_SOLID_LIBS            - the solid library and all depending libraries
  KDE4_KNOTIFYCONFIG_LIBS    - the knotify config library and all depending libraries
  KDE4_KROSSCORE_LIBS        - the kross core library and all depending libraries
  KDE4_KROSSUI_LIBS          - the kross ui library which includes core and all depending libraries
  KDE4_KTEXTEDITOR_LIBS      - the ktexteditor library and all depending libraries
  KDE4_NEPOMUK_LIBS          - the nepomuk library and all depending libraries
  KDE4_PLASMA_LIBS           - the plasma library and all depending librairies
  KDE4_KUNITCONVERSION_LIBS  - the kunitconversion library and all depending libraries
  KDE4_KDEWEBKIT_LIBS        - the kdewebkit library and all depending libraries
</pre>
<p> This module defines a bunch of variables used as locations for install directories. They can be relative (to CMAKE_INSTALL_PREFIX) or absolute. Under Windows they are always relative. </p>
<p>  BIN_INSTALL_DIR          &#8211; the directory where executables will be installed (default is prefix/bin)<br />
  BUNDLE_INSTALL_DIR       &#8211; Mac only: the directory where application bundles will be installed (default is /Applications/KDE4 )<br />
  SBIN_INSTALL_DIR         &#8211; the directory where system executables will be installed (default is prefix/sbin)<br />
  LIB_INSTALL_DIR          &#8211; the directory where libraries will be installed (default is prefix/lib)<br />
  CONFIG_INSTALL_DIR       &#8211; the config file install dir<br />
  DATA_INSTALL_DIR         &#8211; the parent directory where applications can install their data<br />
  HTML_INSTALL_DIR         &#8211; the HTML install dir for documentation<br />
  ICON_INSTALL_DIR         &#8211; the icon install dir (default prefix/share/icons/)<br />
  INFO_INSTALL_DIR         &#8211; the kde info install dir (default prefix/info)<br />
  KCFG_INSTALL_DIR         &#8211; the install dir for kconfig files<br />
  LOCALE_INSTALL_DIR       &#8211; the install dir for translations<br />
  MAN_INSTALL_DIR          &#8211; the kde man page install dir (default prefix/man/)<br />
  MIME_INSTALL_DIR         &#8211; the install dir for the mimetype desktop files<br />
  PLUGIN_INSTALL_DIR       &#8211; the subdirectory relative to the install prefix where plugins will be installed (default is ${KDE4_LIB_INSTALL_DIR}/kde4)<br />
  SERVICES_INSTALL_DIR     &#8211; the install dir for service (desktop, protocol, &#8230;) files<br />
  SERVICETYPES_INSTALL_DIR &#8211; the install dir for servicestypes desktop files<br />
  SOUND_INSTALL_DIR        &#8211; the install dir for sound files<br />
  TEMPLATES_INSTALL_DIR    &#8211; the install dir for templates (Create new file&#8230;)<br />
  WALLPAPER_INSTALL_DIR    &#8211; the install dir for wallpapers<br />
  DEMO_INSTALL_DIR         &#8211; the install dir for demos<br />
  KCONF_UPDATE_INSTALL_DIR &#8211; the kconf_update install dir<br />
  XDG_APPS_INSTALL_DIR     &#8211; the XDG apps dir<br />
  XDG_DIRECTORY_INSTALL_DIR- the XDG directory<br />
  XDG_MIME_INSTALL_DIR     &#8211; the XDG mimetypes install dir<br />
  DBUS_INTERFACES_INSTALL_DIR &#8211; the directory where dbus interfaces be installed (default is prefix/share/dbus-1/interfaces)<br />
  DBUS_SERVICES_INSTALL_DIR        &#8211; the directory where dbus services be installed (default is prefix/share/dbus-1/services )<br />
  DBUS_SYSTEM_SERVICES_INSTALL_DIR        &#8211; the directory where dbus system services be installed (default is prefix/share/dbus-1/system-services )</p>
<p> The following variable is provided, but seem to be unused: </p>
<pre>
  LIBS_HTML_INSTALL_DIR    /share/doc/HTML            CACHE STRING &quot;Is this still used ?&quot;)
</pre>
<p> The following user adjustable options are provided: </p>
<pre>
  KDE4_ENABLE_FINAL - enable KDE-style enable-final all-in-one-compilation
  KDE4_BUILD_TESTS  - enable this to build the testcases
  KDE4_ENABLE_FPIE  - enable it to use gcc Position Independent Executables feature
  KDE4_USE_COMMON_CMAKE_PACKAGE_CONFIG_DIR - only present for CMake &gt;= 2.6.3, defaults to TRUE
                      If enabled, the package should install its &lt;package&gt;Config.cmake file to
                      lib/cmake/&lt;package&gt;/ instead to lib/&lt;package&gt;/cmake
</pre>
<p> It also adds the following macros and functions (from KDE4Macros.cmake) </p>
<pre>
  KDE4_ADD_UI_FILES (SRCS_VAR file1.ui ... fileN.ui)
    Use this to add Qt designer ui files to your application/library.
</pre>
<pre>
  KDE4_ADD_UI3_FILES (SRCS_VAR file1.ui ... fileN.ui)
    Use this to add Qt designer ui files from Qt version 3 to your application/library.
</pre>
<p>KDE4_ADD_KCFG_FILES(SRCS_VAR[GENERATE_MOC][USE_RELATIVE_PATH] file1.kcfgc&#8230; fileN.kcfgc)<br />
Use this to add KDE config compiler files to your application / library.Use optional GENERATE_MOC to generate moc if you use signals in your kcfg files.Use optional USE_RELATIVE_PATH to generate the classes in the build following the given<br />
                                                                    relative path to the file.</p>
<pre>
  KDE4_ADD_WIDGET_FILES (SRCS_VAR file1.widgets ... fileN.widgets)
    Use this to add widget description files for the makekdewidgets4 code generator
    for Qt Designer plugins.
</pre>
<p>KDE4_CREATE_FINAL_FILES(filename_CXX filename_C file1&#8230; fileN)<br />
    This macro is intended mainly for internal uses.<br />
    It is used for enable-final. It will generate two source files,<br />
    one for the C files and one for the C++ files.<br />
    These files will have the names given in filename_CXX and filename_C.</p>
<pre>
  KDE4_ADD_PLUGIN ( name [WITH_PREFIX] file1 ... fileN )
    Create a KDE plugin (KPart, kioslave, etc.) from the given source files.
    It supports KDE4_ENABLE_FINAL.
    If WITH_PREFIX is given, the resulting plugin will have the prefix &quot;lib&quot;, otherwise it won't.
</pre>
<p>KDE4_ADD_KDEINIT_EXECUTABLE(name[NOGUI][RUN_UNINSTALLED] file1&#8230; fileN)<br />
    Create a KDE application in the form of a module loadable via kdeinit.<br />
    A library named kdeinit_&lt;name&gt; will be created and a small executable which links to it.<br />
    It supports KDE4_ENABLE_FINAL<br />
    If the executable doesn&#8217;t have a GUI, use the option NOGUI. By default on OS X<br />
    application bundles are created, with the NOGUI option no bundles but simple executables<br />
    are created. Under Windows this flag is also necessary to separate between applications<br />
    with GUI and without. On other UNIX systems this flag has no effect.<br />
    RUN_UNINSTALLED is deprecated and is ignored, for details see the documentation for<br />
    KDE4_ADD_EXECUTABLE().</p>
<p>KDE4_ADD_EXECUTABLE(name[NOGUI][TEST][RUN_UNINSTALLED] file1&#8230; fileN)<br />
    Equivalent to ADD_EXECUTABLE(), but additionally adds some more features:<br />
    -support for KDE4_ENABLE_FINAL<br />
    -support for automoc<br />
    -automatic RPATH handling<br />
    If the executable doesn&#8217;t have a GUI, use the option NOGUI. By default on OS X<br />
    application bundles are created, with the NOGUI option no bundles but simple executables<br />
    are created. Under Windows this flag is also necessary to separate between applications<br />
    with GUI and without. On other UNIX systems this flag has no effect.<br />
    The option TEST is for internal use only.<br />
    The option RUN_UNINSTALLED is ignored. It was necessary with KDE 4.0 and 4.1<br />
    if the executable had to be run from the build tree. Since KDE 4.2 all<br />
    executables can be always run uninstalled (the RPATH of executables which are not<br />
    yet installed points since then into the buildtree and is changed<br />
    to the proper location when installing, so RUN_UNINSTALLED is not necessary anymore).</p>
<pre>
  KDE4_ADD_LIBRARY (name [STATIC | SHARED | MODULE ] file1 ... fileN)
    Equivalent to ADD_LIBRARY(), but additionally it supports KDE4_ENABLE_FINAL
    and under Windows it adds a -DMAKE_&lt;name&gt;_LIB definition to the compilation.
</pre>
<p>KDE4_ADD_UNIT_TEST(testname[TESTNAME targetname] file1&#8230; fileN)<br />
    add a unit test, which is executed when running make test<br />
    it will be built with RPATH poiting to the build dir<br />
    The targets are always created, but only built for the &#8220;all&#8221;<br />
    target if the option KDE4_BUILD_TESTS is enabled. Otherwise the rules for the target<br />
    are created but not built by default. You can build them by manually building the target.<br />
    The name of the target can be specified using TESTNAME &lt;targetname&gt;, if it is not given<br />
    the macro will default to the &lt;testname&gt;<br />
    KDESRCDIR is set to the source directory of the test, this can be used with<br />
    KGlobal::dirs()-&gt;addResourceDir( &#8220;data&#8221;, KDESRCDIR )</p>
<pre>
  KDE4_UPDATE_ICONCACHE()
    Notifies the icon cache that new icons have been installed by updating
    mtime of ${ICON_INSTALL_DIR}/hicolor directory.
</pre>
<pre>
  KDE4_INSTALL_ICONS( path theme)
    Installs all png and svgz files in the current directory to the icon
    directoy given in path, in the subdirectory for the given icon theme.
</pre>
<p>KDE4_CREATE_HANDBOOK(docbookfile[INSTALL_DESTINATION installdest][SUBDIR subdir])<br />
Create the handbook from the docbookfile(using meinproc4)<br />
    The resulting handbook will be installed to&lt;installdest&gt; when using INSTALL_DESTINATION&lt;installdest&gt;,<br />
    or to&lt;installdest&gt; / &lt;subdir&gt; if SUBDIR&lt;subdir&gt; is specified.</p>
<pre>
  KDE4_CREATE_MANPAGE( docbookfile section )
   Create the manpage for the specified section from the docbookfile (using meinproc4)
   The resulting manpage will be installed to &lt;installdest&gt; when using
   INSTALL_DESTINATION &lt;installdest&gt;, or to &lt;installdest&gt;/&lt;subdir&gt; if
   SUBDIR &lt;subdir&gt; is specified.
</pre>
<pre>
  KDE4_INSTALL_AUTH_ACTIONS( HELPER_ID ACTIONS_FILE )
   This macro generates an action file, depending on the backend used, for applications using KAuth.
   It accepts the helper id (the DBUS name) and a file containing the actions (check kdelibs/kdecore/auth/example
   for file format). The macro will take care of generating the file according to the backend specified, 
   and to install it in the right location. This (at the moment) means that on Linux (PolicyKit) a .policy
   file will be generated and installed into the policykit action directory (usually /usr/share/PolicyKit/policy/),
   and on Mac (Authorization Services) will be added to the system action registry using the native MacOS API during
   the install phase
</pre>
<p>KDE4_INSTALL_AUTH_HELPER_FILES(HELPER_TARGET HELPER_ID HELPER_USER)<br />
   This macro adds the needed files for an helper executable meant to be used by applications using KAuth.<br />
   It accepts the helper target, the helper ID (the DBUS name) and the user under which the helper will run on.<br />
   This macro takes care of generate the needed files, and install them in the right location. This boils down<br />
   to a DBus policy to let the helper register on the system bus, and a service file for letting the helper<br />
   being automatically activated by the system bus.<br />
   *WARNING* You have to install the helper in ${LIBEXEC_INSTALL_DIR} to make sure everything will work.</p>
<pre>
  A note on the possible values for CMAKE_BUILD_TYPE and how KDE handles
  the flags for those buildtypes. FindKDE4Internal supports the values
  Debug, Release, RelWithDebInfo, Profile and Debugfull:
</pre>
<pre>
  Release
          optimised for speed, qDebug/kDebug turned off, no debug symbols
  RelWithDebInfo (Release with debug info)
          optimised for speed, debugging symbols on (-g)
  Debug
          optimised but debuggable, debugging on (-g)
          (-fno-reorder-blocks -fno-schedule-insns -fno-inline)
  DebugFull
          no optimisation, full debugging on (-g3)
  Profile
          DebugFull + -ftest-coverage -fprofile-arcs
</pre>
<pre>
  It is expected that the &quot;Debug&quot; build type be still debuggable with gdb
  without going all over the place, but still produce better performance.
  It's also important to note that gcc cannot detect all warning conditions
  unless the optimiser is active.
</pre>
<pre>
  This module allows to depend on a particular minimum version of kdelibs.
  To acomplish that one should use the apropriate cmake syntax for
  find_package. For example to depend on kdelibs &gt;= 4.1.0 one should use
</pre>
<pre>
  find_package(KDE4 4.1.0 REQUIRED)
</pre>
<pre>
  In earlier versions of KDE you could use the variable KDE_MIN_VERSION to
  have such a dependency. This variable is deprecated with KDE 4.2.0, but
  will still work to make the module backwards-compatible.
</pre>
<dt><code>FindKDE4Workspace</code></p>
<dd>
<p> Find if we installed kdebase/workspaces. Once done this will define </p>
<pre>
  KDE4WORKSPACE_FOUND - system has KDE workspace installed
  KDE4WORKSPACE_INCLUDE_DIR - the KDE workspace include directory
</pre>
<p> It also sets variables for the following libraries: </p>
<pre>
   KDE4WORKSPACE_TASKMANAGER_LIBRARY, KDE4WORKSPACE_TASKMANAGER_LIBS
   KDE4WORKSPACE_KWORKSPACE_LIBRARY, KDE4WORKSPACE_KWORKSPACE_LIBS
   KDE4WORKSPACE_SOLIDCONTROLIFACES_LIBRARY, KDE4WORKSPACE_SOLIDCONTROLIFACES_LIBS
   KDE4WORKSPACE_SOLIDCONTROL_LIBRARY, KDE4WORKSPACE_SOLIDCONTROL_LIBS
   KDE4WORKSPACE_PROCESSUI_LIBRARY, KDE4WORKSPACE_PROCESSUI_LIBS
   KDE4WORKSPACE_LSOFUI_LIBRARY, KDE4WORKSPACE_LSOFUI_LIBS
   KDE4WORKSPACE_PLASMACLOCK_LIBRARY, KDE4WORKSPACE_PLASMACLOCK_LIBS
   KDE4WORKSPACE_NEPOMUKQUERYCLIENT_LIBRARY, KDE4WORKSPACE_NEPOMUKQUERYCLIENT_LIBS
   KDE4WORKSPACE_NEPOMUKQUERY_LIBRARY, KDE4WORKSPACE_NEPOMUKQUERY_LIBS
   KDE4WORKSPACE_KSCREENSAVER_LIBRARY, KDE4WORKSPACE_KSCREENSAVER_LIBS
   KDE4WORKSPACE_WEATHERION_LIBRARY, KDE4WORKSPACE_WEATHERION_LIBS
   KDE4WORKSPACE_KWINEFFECTS_LIBRARY, KDE4WORKSPACE_KWINEFFECTS_LIBS
   KDE4WORKSPACE_KDECORATIONS_LIBRARY, KDE4WORKSPACE_KDECORATIONS_LIBS
   KDE4WORKSPACE_KSGRD_LIBRARY, KDE4WORKSPACE_KSGRD_LIBS
   KDE4WORKSPACE_KEPHAL_LIBRARY, KDE4WORKSPACE_KEPHAL_LIBS
</pre>
<p> And the following locations: </p>
<pre>
   KDE4WORKSPACE_LIB_DIR
   KDE4WORKSPACE_LIBEXEC_DIR
   KDE4WORKSPACE_INCLUDE_DIR
   KDE4WORKSPACE_BIN_DIR
   KDE4WORKSPACE_SBIN_DIR
   KDE4WORKSPACE_DATA_DIR
   KDE4WORKSPACE_HTML_DIR
   KDE4WORKSPACE_CONFIG_DIR
   KDE4WORKSPACE_ICON_DIR
   KDE4WORKSPACE_KCFG_DIR
   KDE4WORKSPACE_LOCALE_DIR
   KDE4WORKSPACE_MIME_DIR
   KDE4WORKSPACE_SOUND_DIR
   KDE4WORKSPACE_TEMPLATES_DIR
   KDE4WORKSPACE_WALLPAPER_DIR
   KDE4WORKSPACE_KCONF_UPDATE_DIR
   KDE4WORKSPACE_AUTOSTART_DIR
   KDE4WORKSPACE_XDG_APPS_DIR
   KDE4WORKSPACE_XDG_DIRECTORY_DIR
   KDE4WORKSPACE_SYSCONF_DIR
   KDE4WORKSPACE_MAN_DIR
   KDE4WORKSPACE_INFO_DIR
   KDE4WORKSPACE_DBUS_INTERFACES_DIR
   KDE4WORKSPACE_DBUS_SERVICES_DIR
   KDE4WORKSPACE_SERVICES_DIR
   KDE4WORKSPACE_SERVICETYPES_DIR
</pre>
<dt><code>FindKDEWIN32</code></p>
<dd> Try to find the KDEWIN32 library &#8211; deprecated </p>
<p> Once done this will define </p>
<pre>
  KDEWIN32_FOUND - system has KDEWIN32
  KDEWIN32_INCLUDES - the KDEWIN32 include directories
  KDEWIN32_LIBRARIES - The libraries needed to use KDEWIN32
</pre>
<dt><code>FindKDEWIN_Packager</code></p>
<dd>
<p> KDEWIN packager <a rel="nofollow" href="http://www.winkde.org/pub/kde/ports/win32/installer">http://www.winkde.org/pub/kde/ports/win32/installer</a> </p>
<p> The kdewin packager is searched in the following pathes and order </p>
<pre>
    path specified by the environment dir KDEWIN_PACKAGER_DIR
    &lt;ProgramFiles&gt;/kdewin-packager 
    &lt;ProgramFiles&gt;/kdewin-installer
</pre>
<p> The macro KDEWIN_PACKAGER provides package building support and should be added to the top level CMakeLists.txt as shown below </p>
<p> if (KDEWIN_PACKAGER_FOUND) </p>
<pre>
    KDEWIN_PACKAGER(
       &quot;projectname&quot;
       &quot;version&quot;
       &quot;description&quot; 
       &quot;additional options&quot;
   )
</pre>
<p> endif (KDEWIN_PACKAGER_FOUND) </p>
<dt><code>FindKDEWin</code></p>
<dd> Try to find the KDEWIN library </p>
<p> Once done this will define </p>
<pre>
  KDEWIN_FOUND - system has KDEWIN
  KDEWIN_INCLUDES - the KDEWIN include directories
  KDEWIN_LIBRARIES - The libraries needed to use KDEWIN
</pre>
<dt><code>FindKDevPlatform</code></p>
<dd>
<p> Find the KDevelop Platform modules and sets various variables accordingly </p>
<p> Example usage of this module: find_package(KDevPlatform 1.0.0 REQUIRED) </p>
<p> The version number and REQUIRED flag are optional. You can set CMAKE_PREFIX_PATH variable to help it find the required files and directories </p>
<dt><code>FindKNepomuk</code></p>
<dd>
<p> Once done this will define </p>
<pre>
  KNEPOMUK_FOUND - system has the Nepomuk-KDE backbone lib KNep
  KNEPOMUK_INCLUDES - the libKNep include directory
  KNEPOMUK_LIBRARIES - Link these to use libKNep
</pre>
<dt><code>FindKdcraw</code></p>
<dd> Try to find the Kdcraw library </p>
<p> Once done this will define </p>
<pre>
  KDCRAW_FOUND - system has libkdcraw
  KDCRAW_INCLUDE_DIR - the libkdcraw include directory
  KDCRAW_LIBRARIES - Link these to use libkdcraw
  KDCRAW_DEFINITIONS - Compiler switches required for using libkdcraw
</pre>
<dt><code>FindKdeMultimedia</code></p>
<dd>
<p> Module to see if we have KDE4 kdemultimedia installed </p>
<p> This module defines </p>
<pre>
  KDEMULTIMEDIA_INCLUDE_DIR - the include dir
  KCDDB_LIBRARY - the kcddb library
  KCOMPACTDISC_LIBRARY - the kcompactdisk library
  KDEMULTIMEDIA_LIBRARIES - all of the KDE multimedia libraries together
  KDEMULTIMEDIA_FOUND - true if the above have been found
</pre>
<dt><code>FindKdepim</code></p>
<dd>
<p> Nothing should require kdepim. We&#8217;ll show a fatal error and an explanation. </p>
<dt><code>FindKdepimLibs</code></p>
<dd>
<p> Find if we installed kdepimlibs before to compile it Once done this will define </p>
<pre>
  KDEPIMLIBS_FOUND - system has KDE PIM Libraries
  KDEPIMLIBS_INCLUDE_DIR - the KDE PIM Libraries include directory
  KDEPIMLIBS_INCLUDE_DIRS - the KDE PIM Libraries include directory and CamelCase headers
</pre>
<p> It also sets variables for the following libraries: </p>
<pre>
   KDEPIMLIBS_AKONADI_LIBS
   KDEPIMLIBS_AKONADI_CONTACT_LIBS
   KDEPIMLIBS_AKONADI_KABC_LIBS
   KDEPIMLIBS_AKONADI_KMIME_LIBS
   KDEPIMLIBS_GPGMEPP_LIBS
   KDEPIMLIBS_KABC_LIBS
   KDEPIMLIBS_KBLOG_LIBS
   KDEPIMLIBS_KCAL_LIBS
   KDEPIMLIBS_KHOLIDAYS_LIBS
   KDEPIMLIBS_KIMAP_LIBS
   KDEPIMLIBS_KLDAP_LIBS
   KDEPIMLIBS_KMIME_LIBS
   KDEPIMLIBS_KONTACTINTERFACE_LIBS
   KDEPIMLIBS_KPIMIDENTITIES_LIBS
   KDEPIMLIBS_KPIMTEXTEDIT_LIBS
   KDEPIMLIBS_KPIMUTILS_LIBS
   KDEPIMLIBS_KRESOURCES_LIBS
   KDEPIMLIBS_KTNEF_LIBS
   KDEPIMLIBS_KXMLRPCCLIENT_LIBS
   KDEPIMLIBS_MAILTRANSPORT_LIBS
   KDEPIMLIBS_MICROBLOG_LIBS
   KDEPIMLIBS_QGPGME_LIBS
   KDEPIMLIBS_SYNDICATION_LIBS
</pre>
<p> And the following locations: </p>
<pre>
   KDEPIMLIBS_DATA_DIR
   KDEPIMLIBS_DBUS_INTERFACES_DIR
   KDEPIMLIBS_DBUS_SERVICES_DIR
   KDEPIMLIBS_INCLUDE_DIR
   KDEPIMLIBS_INCLUDE_DIRS
   KDEPIMLIBS_LIB_DIR
   KDEPIMLIBS_BIN_DIR
   KDEPIMLIBS_LIBEXEC_DIR
   KDEPIMLIBS_SBIN_DIR
   KDEPIMLIBS_HTML_DIR
   KDEPIMLIBS_CONFIG_DIR
   KDEPIMLIBS_ICON_DIR
   KDEPIMLIBS_KCFG_DIR
   KDEPIMLIBS_LOCALE_DIR
   KDEPIMLIBS_MIME_DIR
   KDEPIMLIBS_SOUND_DIR
   KDEPIMLIBS_TEMPLATES_DIR
   KDEPIMLIBS_KCONF_UPDATE_DIR
   KDEPIMLIBS_AUTOSTART_DIR
   KDEPIMLIBS_XDG_APPS_DIR
   KDEPIMLIBS_XDG_DIRECTORY_DIR
   KDEPIMLIBS_SYSCONF_DIR
   KDEPIMLIBS_MAN_DIR
   KDEPIMLIBS_INFO_DIR
   KDEPIMLIBS_SERVICES_DIR
   KDEPIMLIBS_SERVICETYPES_DIR
</pre>
<dt><code>FindKexiv2</code></p>
<dd> Try to find the KExiv2 library </p>
<p> Once done this will define </p>
<pre>
  KEXIV2_FOUND - system has libkexiv2
  KEXIV2_INCLUDE_DIR - the libkexiv2 include directory
  KEXIV2_LIBRARIES - Link these to use libkexiv2
  KEXIV2_DEFINITIONS - Compiler switches required for using libkexiv2
</pre>
<dt><code>FindKipi</code></p>
<dd> Try to find the Kipi library </p>
<p> Once done this will define </p>
<pre>
  KIPI_FOUND - system has libkipi
  KIPI_INCLUDE_DIR - the libkipi include directory
  KIPI_LIBRARIES - Link these to use libkipi
  KIPI_DEFINITIONS - Compiler switches required for using libkipi
</pre>
<dt><code>FindKonto</code></p>
<dd>
<p> Once done this will define </p>
<pre>
  KONTO_FOUND - system has the Nepomuk-KDE backbone lib Konto
  KONTO_INCLUDES - the libKonto include directory
  KONTO_LIBRARIES - Link these to use libKonto
</pre>
<dt><code>FindKopete</code></p>
<dd> Try to find the Kopete library </p>
<p> Once done this will define </p>
<pre>
  Kopete_FOUND - system has kopete
  KOPETE_INCLUDE_DIR - the kopete include directory
  KOPETE_LIBRARIES - Link these to use kopete
</pre>
<dt><code>FindKorundum</code></p>
<dd> Find Korundum &#8211; the KDE Ruby bindings </p>
<p> This module finds if Korundum is installed. It defines the following variables: </p>
<pre>
  KORUNDUM_PATH - the path to the korundum ruby file
  KORUNDUM_FOUND - true if it has been found
</pre>
<dt><code>FindLCMS</code></p>
<dd> Find LCMS </p>
<p> Find the LCMS includes and library This module defines </p>
<pre>
  LCMS_INCLUDE_DIR, where to find lcms.h
  LCMS_LIBRARIES, the libraries needed to use LCMS.
  LCMS_VERSION, The value of LCMS_VERSION defined in lcms.h
  LCMS_FOUND, If false, do not try to use LCMS.
</pre>
<dt><code>FindLibArt</code></p>
<dd> Try to find the LibArt 2D graphics library </p>
<p> Once done this will define </p>
<pre>
  LIBART_FOUND - system has the LibArt
  LIBART_INCLUDE_DIR - the LibArt include directory
  LIBART_LIBRARIES - The libraries needed to use LibArt
</pre>
<dt><code>FindLibAttica</code></p>
<dd>
<p> Try to find the Attica library Once done this will define </p>
<pre>
   LIBATTICA_FOUND          Indicates that Attica was found
   LIBATTICA_LIBRARIES      Libraries needed to use Attica
   LIBATTICA_LIBRARY_DIRS   Paths needed for linking against Attica
   LIBATTICA_INCLUDE_DIR    Path needed for finding Attica include files
</pre>
<p> Copyright (c) 2009 Frederik Gladhorn &lt;gladhorn [at] kde.org&gt; </p>
<p> Redistribution and use is allowed according to the terms of the BSD license. </p>
<dt><code>FindLibKonq</code></p>
<dd> Try to find konqueror library </p>
<p> Once done this will define </p>
<pre>
  LIBKONQ_FOUND - system has libkonq library
  LIBKONQ_INCLUDE_DIR - the LIBKONQ include directory
  LIBKONQ_LIBRARY - the libkonq library
</pre>
<dt><code>FindLibLZMA</code></p>
<dd> Find LibLZMA </p>
<p> Find LibLZMA headers and library </p>
<p>LIBLZMA_FOUND &#8211; True if liblzma is found.LIBLZMA_INCLUDE_DIRS &#8211; Directory where liblzma headers are located.LIBLZMA_LIBRARIES &#8211; Lzma libraries to link against.LIBLZMA_HAS_AUTO_DECODER &#8211; True if lzma_auto_decoder () is found(required).LIBLZMA_HAS_EASY_ENCODER &#8211; True if lzma_easy_encoder () is found(required).LIBLZMA_HAS_LZMA_PRESET &#8211; True if lzma_lzma_preset () is found(required).</p>
<dt><code>FindLibXml2</code></p>
<dd> Try to find LibXml2 </p>
<p> Once done this will define </p>
<pre>
  LIBXML2_FOUND - System has LibXml2
  LIBXML2_INCLUDE_DIR - The LibXml2 include directory
  LIBXML2_LIBRARIES - The libraries needed to use LibXml2
  LIBXML2_DEFINITIONS - Compiler switches required for using LibXml2
  LIBXML2_XMLLINT_EXECUTABLE - The XML checking tool xmllint coming with LibXml2
</pre>
<dt><code>FindLibXslt</code></p>
<dd> Try to find LibXslt </p>
<p> Once done this will define </p>
<pre>
  LIBXSLT_FOUND - system has LibXslt
  LIBXSLT_INCLUDE_DIR - the LibXslt include directory
  LIBXSLT_LIBRARIES - Link these to LibXslt
  LIBXSLT_DEFINITIONS - Compiler switches required for using LibXslt
  LIBXSLT_XSLTPROC_EXECUTABLE - path to the xsltproc tool
</pre>
<dt><code>FindLibintl</code></p>
<dd>
<p> Try to find Libintl functionality Once done this will define </p>
<pre>
  LIBINTL_FOUND - system has Libintl
  LIBINTL_INCLUDE_DIR - Libintl include directory
  LIBINTL_LIBRARIES - Libraries needed to use Libintl
</pre>
<p> TODO: This will enable translations only if Gettext functionality is present in libc. Must have more robust system for release, where Gettext functionality can also reside in standalone Gettext library, or the one embedded within kdelibs (cf. gettext.m4 from Gettext source). </p>
<dt><code>FindLibraryWithDebug</code></p>
<dd>
<pre>
  FIND_LIBRARY_WITH_DEBUG
  -&gt; enhanced FIND_LIBRARY to allow the search for an
     optional debug library with a WIN32_DEBUG_POSTFIX similar
     to CMAKE_DEBUG_POSTFIX when creating a shared lib
     it has to be the second and third argument
</pre>
<dt><code>FindLinuxWirelesstools</code></p>
<dd> Try to find wireless extensions support libraries </p>
<p> Once done this will define </p>
<pre>
  IW_FOUND - system has IW
  IW_INCLUDE_DIR - the IW include directory
  IW_LIBRARIES - Link to these to use IW
</pre>
<dt><code>FindMsgfmt</code></p>
<dd> Try to find msgfmt </p>
<p> Once done this will define </p>
<pre>
  MSGFMT_FOUND - system has msgfmt
</pre>
<dt><code>FindMusicBrainz</code></p>
<dd>
<p> Module to find the musicbrainz library </p>
<p> It defines </p>
<pre>
  MUSICBRAINZ_INCLUDE_DIR - the include dir 
  MUSICBRAINZ_LIBRARIES - the required libraries
  MUSICBRAINZ_FOUND - true if both of the above have been found
</pre>
<dt><code>FindMySQL</code></p>
<dd> Try to find MySQL / MySQL Embedded library </p>
<p> Find the MySQL includes and client library This module defines </p>
<pre>
  MYSQL_INCLUDE_DIR, where to find mysql.h
  MYSQL_LIBRARIES, the libraries needed to use MySQL.
  MYSQL_LIB_DIR, path to the MYSQL_LIBRARIES
  MYSQL_EMBEDDED_LIBRARIES, the libraries needed to use MySQL Embedded.
  MYSQL_EMBEDDED_LIB_DIR, path to the MYSQL_EMBEDDED_LIBRARIES
  MYSQL_FOUND, If false, do not try to use MySQL.
  MYSQL_EMBEDDED_FOUND, If false, do not try to use MySQL Embedded.
</pre>
<dt><code>FindNepomuk</code></p>
<dd>
<p> Once done this will define </p>
<pre>
  NEPOMUK_FOUND - system has Nepomuk
  NEPOMUK_INCLUDE_DIR - the Nepomuk include directory
  NEPOMUK_LIBRARIES - Link these to use Nepomuk
  NEPOMUK_QUERY_LIBRARIES - Link these to use Nepomuk query
  NEPOMUK_DEFINITIONS - Compiler switches required for using Nepomuk
</pre>
<p> Nepomuk requires Soprano, so this module checks for Soprano too. </p>
<dt><code>FindNetworkManager</code></p>
<dd> Try to find NetworkManager </p>
<p> Once done this will define </p>
<pre>
  NETWORKMANAGER_FOUND - system has NetworkManager
  NETWORKMANAGER_INCLUDE_DIRS - the NetworkManager include directories
  NETWORKMANAGER_LIBRARIES - the libraries needed to use NetworkManager
  NETWORKMANAGER_CFLAGS - Compiler switches required for using NetworkManager
  NETWORKMANAGER_VERSION - version number of NetworkManager
</pre>
<dt><code>FindOggVorbis</code></p>
<dd> Try to find the OggVorbis libraries </p>
<p> Once done this will define </p>
<pre>
  OGGVORBIS_FOUND - system has OggVorbis
  OGGVORBIS_VERSION - set either to 1 or 2
  OGGVORBIS_INCLUDE_DIR - the OggVorbis include directory
  OGGVORBIS_LIBRARIES - The libraries needed to use OggVorbis
  OGG_LIBRARY         - The Ogg library
  VORBIS_LIBRARY      - The Vorbis library
  VORBISFILE_LIBRARY  - The VorbisFile library
  VORBISENC_LIBRARY   - The VorbisEnc library
</pre>
<dt><code>FindOpenEXR</code></p>
<dd>
<p> Try to find the OpenEXR libraries This check defines: </p>
<pre>
  OPENEXR_FOUND - system has OpenEXR
  OPENEXR_INCLUDE_DIR - OpenEXR include directory
  OPENEXR_LIBRARIES - Libraries needed to use OpenEXR
  OPENEXR_DEFINITIONS - definitions required to use OpenEXR
</pre>
<dt><code>FindOpenSSL</code></p>
<dd> Try to find the OpenSSL encryption library </p>
<p> Once done this will define </p>
<pre>
  OPENSSL_FOUND - system has the OpenSSL library
  OPENSSL_INCLUDE_DIR - the OpenSSL include directory
  OPENSSL_LIBRARIES - The libraries needed to use OpenSSL
  OPENSSL_EAY_LIBRARIES - The additional libraries needed to use OpenSSL on windows
</pre>
<dt><code>FindPCRE</code></p>
<dd> Try to find the PCRE regular expression library </p>
<p> Once done this will define </p>
<pre>
  PCRE_FOUND - system has the PCRE library
  PCRE_INCLUDE_DIR - the PCRE include directory
  PCRE_LIBRARIES - The libraries needed to use PCRE
</pre>
<dt><code>FindPhonon</code></p>
<dd>
<p> Find libphonon Once done this will define </p>
<pre>
  PHONON_FOUND    - system has Phonon Library
  PHONON_INCLUDES - the Phonon include directory
  PHONON_LIBS     - link these to use Phonon
  PHONON_VERSION  - the version of the Phonon Library
</pre>
<dt><code>FindPkgConfig</code></p>
<dd> a pkg-config module for CMake </p>
<p> Usage: </p>
<p>   pkg_check_modules(&lt;PREFIX&gt; [REQUIRED] [QUIET] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for all the given modules</p>
<p>   pkg_search_module(&lt;PREFIX&gt; [REQUIRED] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for given modules and uses the first working one</p>
<p> When the &#8216;REQUIRED&#8217; argument was set, macros will fail with an error when module(s) could not be found </p>
<p> When the &#8216;QUIET&#8217; argument is set, no error message will be output if the package was not found. </p>
<p> It sets the following variables: </p>
<pre>
   PKG_CONFIG_FOUND         ... true if pkg-config works on the system
   PKG_CONFIG_EXECUTABLE    ... pathname of the pkg-config program
   &lt;PREFIX&gt;_FOUND           ... set to 1 if module(s) exist
</pre>
<p> For the following variables two sets of values exist; first one is the common one and has the given PREFIX. The second set contains flags which are given out when pkgconfig was called with the &#8216;&#8211;static&#8217; option. </p>
<pre>
   &lt;XPREFIX&gt;_LIBRARIES      ... only the libraries (w/o the '-l')
   &lt;XPREFIX&gt;_LIBRARY_DIRS   ... the paths of the libraries (w/o the '-L')
   &lt;XPREFIX&gt;_LDFLAGS        ... all required linker flags
   &lt;XPREFIX&gt;_LDFLAGS_OTHER  ... all other linker flags
   &lt;XPREFIX&gt;_INCLUDE_DIRS   ... the '-I' preprocessor flags (w/o the '-I')
   &lt;XPREFIX&gt;_CFLAGS         ... all required cflags
   &lt;XPREFIX&gt;_CFLAGS_OTHER   ... the other compiler flags
</pre>
<p>   &lt;XPREFIX&gt; = &lt;PREFIX&gt;        for common case<br />
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;_STATIC for static linking</p>
<p> There are some special variables whose prefix depends on the count of given modules. When there is only one module, &lt;PREFIX&gt; stays unchanged. When there are multiple modules, the prefix will be changed to &lt;PREFIX&gt;_&lt;MODNAME&gt;: </p>
<pre>
   &lt;XPREFIX&gt;_VERSION    ... version of the module
   &lt;XPREFIX&gt;_PREFIX     ... prefix-directory of the module
   &lt;XPREFIX&gt;_INCLUDEDIR ... include-dir of the module
   &lt;XPREFIX&gt;_LIBDIR     ... lib-dir of the module
</pre>
<pre>
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;  when |MODULES| == 1, else
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;_&lt;MODNAME&gt;
</pre>
<p> A &lt;MODULE&gt; parameter can have the following formats: </p>
<p>{MODNAME}&#8230; matches any version{MODNAME} &gt;= {VERSION}&#8230; at least version&lt;VERSION&gt; is required{MODNAME} = {VERSION}&#8230; exactly version&lt;VERSION&gt; is required{MODNAME} &lt;= {VERSION}&#8230; modules must not be newer than&lt;VERSION&gt;</p>
<p> Examples </p>
<pre>
   pkg_check_modules (GLIB2   glib-2.0)
</pre>
<pre>
   pkg_check_modules (GLIB2   glib-2.0&gt;=2.10)
     requires at least version 2.10 of glib2 and defines e.g.
       GLIB2_VERSION=2.10.3
</pre>
<pre>
   pkg_check_modules (FOO     glib-2.0&gt;=2.10 gtk+-2.0)
     requires both glib2 and gtk2, and defines e.g.
       FOO_glib-2.0_VERSION=2.10.3
       FOO_gtk+-2.0_VERSION=2.8.20
</pre>
<p>pkg_check_modules(XRENDER REQUIRED xrender)<br />
    defines e.g. : XRENDER_LIBRARIES = Xrender;<br />
X11<br />
    XRENDER_STATIC_LIBRARIES = Xrender;<br />
X11;<br />
pthread;<br />
Xau;<br />
Xdmcp</p>
<pre>
   pkg_search_module (BAR     libxml-2.0 libxml2 libxml&gt;=2)
</pre>
<dt><code>FindPolkitQt-1</code></p>
<dd> Try to find PolkitQt-1 </p>
<p> Once done this will define </p>
<pre>
  POLKITQT-1_FOUND - system has Polkit-qt
  POLKITQT-1_INCLUDE_DIR - the Polkit-qt include directory
  POLKITQT-1_LIBRARIES - Link these to use all Polkit-qt libs
  POLKITQT-1_CORE_LIBRARY - Link this to use the polkit-qt-core library only
  POLKITQT-1_GUI_LIBRARY - Link this to use GUI elements in polkit-qt (polkit-qt-gui)
  POLKITQT-1_AGENT_LIBRARY - Link this to use the agent wrapper in polkit-qt
  POLKITQT-1_DEFINITIONS - Compiler switches required for using Polkit-qt
</pre>
<dt><code>FindPolkitQt</code></p>
<dd> Try to find Polkit-qt </p>
<p> Once done this will define </p>
<pre>
  POLKITQT_FOUND - system has Polkit-qt
  POLKITQT_INCLUDE_DIR - the Polkit-qt include directory
  POLKITQT_LIBRARIES - Link these to use all Polkit-qt libs
  POLKITQT_CORE_LIBRARY - Link this to use the polkit-qt-core library only
  POLKITQT_GUI_LIBRARY - Link this to use GUI elements in polkit-qt (polkit-qt-gui)
  POLKITQT_DEFINITIONS - Compiler switches required for using Polkit-qt
  POLKITQT_POLICY_FILES_INSTALL_DIR - The directory where policy files should be installed to.
</pre>
<p> The minimum required version PolkitQt can be specified by setting the POLKITQT_MIN_VERSION variable. </p>
<dt><code>FindPopplerQt4</code></p>
<dd> Try to find the Qt4 binding of the Poppler library </p>
<p> Once done this will define </p>
<pre>
  POPPLER_QT4_FOUND - system has poppler-qt4
  POPPLER_QT4_INCLUDE_DIR - the poppler-qt4 include directory
  POPPLER_QT4_LIBRARIES - Link these to use poppler-qt4
  POPPLER_QT4_DEFINITIONS - Compiler switches required for using poppler-qt4
</pre>
<dt><code>FindPostgreSQL</code></p>
<dd> Find PostgreSQL </p>
<p> Find the PostgreSQL includes and client library This module defines </p>
<pre>
  POSTGRESQL_INCLUDE_DIR, where to find POSTGRESQL.h
  POSTGRESQL_LIBRARIES, the libraries needed to use POSTGRESQL.
  POSTGRESQL_FOUND, If false, do not try to use PostgreSQL.
</pre>
<dt><code>FindPulseAudio</code></p>
<dd>
<p> Try to find the PulseAudio library </p>
<p> Once done this will define: </p>
<pre>
  PULSEAUDIO_FOUND - system has the PulseAudio library
  PULSEAUDIO_INCLUDE_DIR - the PulseAudio include directory
  PULSEAUDIO_LIBRARY - the libraries needed to use PulseAudio
  PULSEAUDIO_MAINLOOP_LIBRARY - the libraries needed to use PulsAudio Mailoop
</pre>
<p> Copyright (c) 2008, Matthias Kretz, &lt;kretz [at] kde.org&gt; Copyright (c) 2009, Marcus Hufgard, &lt;Marcus.Hufgard [at] hufgard.de&gt; </p>
<p> Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<dt><code>FindPyKDE4</code></p>
<dd>
<p> FindPyKDE4 </p>
<p> Checks that Python and PyKDE4 are installed and defines a couple macros: </p>
<pre>
     * PYKDE4_INSTALL_PYTHON_FILES
     * PYKDE4_ADD_UI_FILES
     * PYKDE4_ADD_EXECUTABLE
</pre>
<dt><code>FindPyQt4</code></p>
<dd>
<p> Find PyQt4 ~~~~~~~~~~ Copyright (c) 2007-2008, Simon Edwards &lt;simon [at] simonzone.com&gt; Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<p> PyQt4 website: <a rel="nofollow" href="http://www.riverbankcomputing.co.uk/pyqt/index.php">http://www.riverbankcomputing.co.uk/pyqt/index.php</a> </p>
<p> Find the installed version of PyQt4. FindPyQt4 should only be called after Python has been found. </p>
<p> This file defines the following variables: </p>
<p> PYQT4_VERSION &#8211; The version of PyQt4 found expressed as a 6 digit hex number </p>
<pre>
     suitable for comparision as a string
</pre>
<p> PYQT4_VERSION_STR &#8211; The version of PyQt4 as a human readable string. </p>
<p> PYQT4_VERSION_TAG &#8211; The PyQt version tag using by PyQt&#8217;s sip files. </p>
<p> PYQT4_SIP_DIR &#8211; The directory holding the PyQt4 .sip files. </p>
<p> PYQT4_SIP_FLAGS &#8211; The SIP flags used to build PyQt. </p>
<dt><code>FindPythonLibrary</code></p>
<dd>
<p> Find Python ~~~~~~~~~~~ Find the Python interpreter and related Python directories. </p>
<p> This file defines the following variables: </p>
<p> PYTHON_EXECUTABLE &#8211; The path and filename of the Python interpreter. </p>
<p> PYTHON_SHORT_VERSION &#8211; The version of the Python interpreter found, </p>
<pre>
     excluding the patch version number. (e.g. 2.5 and not 2.5.1))
</pre>
<p> PYTHON_LONG_VERSION &#8211; The version of the Python interpreter found as a human </p>
<pre>
     readable string.
</pre>
<p> PYTHON_SITE_PACKAGES_DIR &#8211; Location of the Python site-packages directory. </p>
<p> PYTHON_INCLUDE_PATH &#8211; Directory holding the python.h include file. </p>
<p> PYTHON_LIBRARY, PYTHON_LIBRARIES- Location of the Python library. </p>
<dt><code>FindQCA2</code></p>
<dd> Try to find QCA2 (Qt Cryptography Architecture 2) </p>
<p> Once done this will define </p>
<pre>
  QCA2_FOUND - system has QCA2
  QCA2_INCLUDE_DIR - the QCA2 include directory
  QCA2_LIBRARIES - the libraries needed to use QCA2
  QCA2_DEFINITIONS - Compiler switches required for using QCA2
</pre>
<p> use pkg-config to get the directories and then use these values in the FIND_PATH() and FIND_LIBRARY() calls </p>
<dt><code>FindQImageBlitz</code></p>
<dd> Try to find the qimageblitz lib </p>
<p> Once done this will define </p>
<pre>
  QIMAGEBLITZ_FOUND - system has qimageblitz lib
  QIMAGEBLITZ_INCLUDES - the qimageblitz include directory
  QIMAGEBLITZ_LIBRARIES - The libraries needed to use qimageblitz
</pre>
<dt><code>FindQt4</code></p>
<dd> Find QT 4 </p>
<p> This module can be used to find Qt4. The most important issue is that the Qt4 qmake is available via the system path. This qmake is then used to detect basically everything else. This module defines a number of key variables and macros. The variable QT_USE_FILE is set which is the path to a CMake file that can be included to compile Qt 4 applications and libraries. It sets up the compilation environment for include directories, preprocessor defines and populates a QT_LIBRARIES variable. </p>
<p> Typical usage could be something like: </p>
<p>find_package(Qt4 4.4.3 COMPONENTS QtCore QtGui QtXml REQUIRED)<br />
    include(${QT_USE_FILE})<br />
        add_executable(myexe main.cpp)<br />
            target_link_libraries(myexe ${QT_LIBRARIES})</p>
<p> The minimum required version can be specified using the standard find_package()-syntax (see example above). For compatibility with older versions of FindQt4.cmake it is also possible to set the variable QT_MIN_VERSION to the minimum required version of Qt4 before the find_package(Qt4) command. If both are used, the version used in the find_package() command overrides the one from QT_MIN_VERSION. </p>
<p> When using the components argument, QT_USE_QT* variables are automatically set for the QT_USE_FILE to pick up. If one wishes to manually set them, the available ones to set include: </p>
<pre>
                    QT_DONT_USE_QTCORE
                    QT_DONT_USE_QTGUI
                    QT_USE_QT3SUPPORT
                    QT_USE_QTASSISTANT
                    QT_USE_QAXCONTAINER
                    QT_USE_QAXSERVER
                    QT_USE_QTDESIGNER
                    QT_USE_QTMOTIF
                    QT_USE_QTMAIN
                    QT_USE_QTMULTIMEDIA
                    QT_USE_QTNETWORK
                    QT_USE_QTNSPLUGIN
                    QT_USE_QTOPENGL
                    QT_USE_QTSQL
                    QT_USE_QTXML
                    QT_USE_QTSVG
                    QT_USE_QTTEST
                    QT_USE_QTUITOOLS
                    QT_USE_QTDBUS
                    QT_USE_QTSCRIPT
                    QT_USE_QTASSISTANTCLIENT
                    QT_USE_QTHELP
                    QT_USE_QTWEBKIT
                    QT_USE_QTXMLPATTERNS
                    QT_USE_PHONON
                    QT_USE_QTSCRIPTTOOLS
</pre>
<pre>
  QT_USE_IMPORTED_TARGETS 
        If this variable is set to TRUE, FindQt4.cmake will create imported
        library targets for the various Qt libraries and set the 
        library variables like QT_QTCORE_LIBRARY to point at these imported
        targets instead of the library file on disk. This provides much better 
        handling of the release and debug versions of the Qt libraries and is 
       also always backwards compatible, except for the case that dependencies
       of libraries are exported, these will then also list the names of the 
       imported targets as dependency and not the file location on disk. This
       is much more flexible, but requires that FindQt4.cmake is executed before
       such an exported dependency file is processed.
</pre>
<p> There are also some files that need processing by some Qt tools such as moc and uic. Listed below are macros that may be used to process those files. </p>
<pre>
  
  macro QT4_WRAP_CPP(outfiles inputfile ... OPTIONS ...)
        create moc code from a list of files containing Qt class with
        the Q_OBJECT declaration.  Per-direcotry preprocessor definitions 
        are also added.  Options may be given to moc, such as those found
        when executing &quot;moc -help&quot;.  
</pre>
<pre>
  macro QT4_WRAP_UI(outfiles inputfile ... OPTIONS ...)
        create code from a list of Qt designer ui files.
        Options may be given to uic, such as those found
        when executing &quot;uic -help&quot;
</pre>
<pre>
  macro QT4_ADD_RESOURCES(outfiles inputfile ... OPTIONS ...)
        create code from a list of Qt resource files.
        Options may be given to rcc, such as those found
        when executing &quot;rcc -help&quot;
</pre>
<pre>
  macro QT4_GENERATE_MOC(inputfile outputfile )
        creates a rule to run moc on infile and create outfile.
        Use this if for some reason QT4_WRAP_CPP() isn't appropriate, e.g.
        because you need a custom filename for the moc file or something similar.
</pre>
<p>  macro QT4_AUTOMOC(sourcefile1 sourcefile2 &#8230; )<br />
        This macro is still experimental.<br />
        It can be used to have moc automatically handled.<br />
        So if you have the files foo.h and foo.cpp, and in foo.h a<br />
        a class uses the Q_OBJECT macro, moc has to run on it. If you don&#8217;t<br />
        want to use QT4_WRAP_CPP() (which is reliable and mature), you can insert<br />
#include &#8220;foo.moc&#8221;<br />
        in foo.cpp and then give foo.cpp as argument to QT4_AUTOMOC(). This will the<br />
        scan all listed files at cmake-time for such included moc files and if it finds<br />
        them cause a rule to be generated to run moc at build time on the<br />
        accompanying header file foo.h.<br />
        If a source file has the SKIP_AUTOMOC property set it will be ignored by this macro.</p>
<pre>
  macro QT4_ADD_DBUS_INTERFACE(outfiles interface basename)
        create a the interface header and implementation files with the 
        given basename from the given interface xml file and add it to 
        the list of sources.
        To disable generating a namespace header, set the source file property 
        NO_NAMESPACE to TRUE on the interface file.
        To include a header in the interface header, set the source file property
        INCLUDE to the name of the header.
        To specify a class name to use, set the source file property CLASSNAME
        to the name of the class.
</pre>
<pre>
  macro QT4_ADD_DBUS_INTERFACES(outfiles inputfile ... )
        create the interface header and implementation files 
        for all listed interface xml files
        the name will be automatically determined from the name of the xml file
        To disable generating namespace headers, set the source file property 
        NO_NAMESPACE to TRUE for these inputfiles.
        To include a header in the interface header, set the source file property
        INCLUDE to the name of the header.
        To specify a class name to use, set the source file property CLASSNAME
        to the name of the class.
</pre>
<p>macro QT4_ADD_DBUS_ADAPTOR(outfiles xmlfile parentheader parentclassname[basename][classname])<br />
    create a dbus adaptor(header and implementation file) from the xml file<br />
    describing the interface,<br />
    and add it to the list of sources.The adaptor<br />
        forwards the calls to a parent class,<br />
    defined in parentheader and named<br />
    parentclassname.The name of the generated files will be&lt;basename&gt; adaptor.{cpp, h} where basename defaults to the basename of the xml file.If&lt;classname&gt; is provided,<br />
    then it will be used as the classname of the<br />
    adaptor itself.</p>
<pre>
  macro QT4_GENERATE_DBUS_INTERFACE( header [interfacename] OPTIONS ...)
        generate the xml interface file from the given header.
        If the optional argument interfacename is omitted, the name of the 
        interface file is constructed from the basename of the header with
        the suffix .xml appended.
        Options may be given to qdbuscpp2xml, such as those found when executing &quot;qdbuscpp2xml --help&quot;
</pre>
<pre>
  macro QT4_CREATE_TRANSLATION( qm_files directories ... sources ... 
                                ts_files ... OPTIONS ...)
        out: qm_files
        in:  directories sources ts_files
        options: flags to pass to lupdate, such as -extensions to specify
        extensions for a directory scan.
        generates commands to create .ts (vie lupdate) and .qm
        (via lrelease) - files from directories and/or sources. The ts files are 
        created and/or updated in the source tree (unless given with full paths).
        The qm files are generated in the build tree.
        Updating the translations can be done by adding the qm_files
        to the source list of your library/executable, so they are
        always updated, or by adding a custom target to control when
        they get updated/generated.
</pre>
<pre>
  macro QT4_ADD_TRANSLATION( qm_files ts_files ... )
        out: qm_files
        in:  ts_files
        generates commands to create .qm from .ts - files. The generated
        filenames can be found in qm_files. The ts_files
        must exists and are not updated in any way.
</pre>
<pre>
  Below is a detailed list of variables that FindQt4.cmake sets.
  QT_FOUND         If false, don't try to use Qt.
  QT4_FOUND        If false, don't try to use Qt 4.
</pre>
<pre>
  QT_VERSION_MAJOR The major version of Qt found.
  QT_VERSION_MINOR The minor version of Qt found.
  QT_VERSION_PATCH The patch version of Qt found.
</pre>
<p>QT_EDITION Set to the edition of Qt(i.e.DesktopLight)<br />
        QT_EDITION_DESKTOPLIGHT True if QT_EDITION<br />
    == DesktopLight<br />
       QT_QTCORE_FOUND True if QtCore was found.QT_QTGUI_FOUND True if QtGui was found.QT_QT3SUPPORT_FOUND True if Qt3Support was found.QT_QTASSISTANT_FOUND True if QtAssistant was found.QT_QTASSISTANTCLIENT_FOUND True if QtAssistantClient was found.QT_QAXCONTAINER_FOUND True if QAxContainer was found(Windows only)<br />
           .QT_QAXSERVER_FOUND True if QAxServer was found(Windows only)<br />
           .QT_QTDBUS_FOUND True if QtDBus was found.QT_QTDESIGNER_FOUND True if QtDesigner was found.QT_QTDESIGNERCOMPONENTS True if QtDesignerComponents was found.QT_QTHELP_FOUND True if QtHelp was found.QT_QTMOTIF_FOUND True if QtMotif was found.QT_QTMULTIMEDIA_FOUND True if QtMultimedia was found(since Qt 4.6.0)<br />
           .QT_QTNETWORK_FOUND True if QtNetwork was found.QT_QTNSPLUGIN_FOUND True if QtNsPlugin was found.QT_QTOPENGL_FOUND True if QtOpenGL was found.QT_QTSQL_FOUND True if QtSql was found.QT_QTSVG_FOUND True if QtSvg was found.QT_QTSCRIPT_FOUND True if QtScript was found.QT_QTSCRIPTTOOLS_FOUND True if QtScriptTools was found.QT_QTTEST_FOUND True if QtTest was found.QT_QTUITOOLS_FOUND True if QtUiTools was found.QT_QTWEBKIT_FOUND True if QtWebKit was found.QT_QTXML_FOUND True if QtXml was found.QT_QTXMLPATTERNS_FOUND True if QtXmlPatterns was found.QT_PHONON_FOUND True if phonon was found.</p>
<pre>
  QT_MAC_USE_COCOA    For Mac OS X, its whether Cocoa or Carbon is used.
                      In general, this should not be used, but its useful
                      when having platform specific code.
</pre>
<p>QT_DEFINITIONS Definitions to use when compiling code that uses Qt.You do not need to use this if you include QT_USE_FILE.The QT_USE_FILE will also define QT_DEBUG and QT_NO_DEBUG to fit your current build type.Those are not contained in QT_DEFINITIONS.</p>
<p>                                                                                                                                                                        QT_INCLUDES List of paths to all include directories of Qt4 QT_INCLUDE_DIR and<br />
    QT_QTCORE_INCLUDE_DIR are<br />
        always in this variable even if NOTFOUND,<br />
    all other INCLUDE_DIRS are<br />
        only added if they are found.You do not need to use this if you include QT_USE_FILE.</p>
<pre>
  Include directories for the Qt modules are listed here.
  You do not need to use these variables if you include QT_USE_FILE.
</pre>
<p>  QT_INCLUDE_DIR              Path to &#8220;include&#8221; of Qt4<br />
  QT_QT_INCLUDE_DIR           Path to &#8220;include/Qt&#8221;<br />
  QT_QT3SUPPORT_INCLUDE_DIR   Path to &#8220;include/Qt3Support&#8221;<br />
  QT_QTASSISTANT_INCLUDE_DIR  Path to &#8220;include/QtAssistant&#8221;<br />
  QT_QTASSISTANTCLIENT_INCLUDE_DIR       Path to &#8220;include/QtAssistant&#8221;<br />
  QT_QAXCONTAINER_INCLUDE_DIR Path to &#8220;include/ActiveQt&#8221; (Windows only)<br />
  QT_QAXSERVER_INCLUDE_DIR    Path to &#8220;include/ActiveQt&#8221; (Windows only)<br />
  QT_QTCORE_INCLUDE_DIR       Path to &#8220;include/QtCore&#8221;<br />
  QT_QTDBUS_INCLUDE_DIR       Path to &#8220;include/QtDBus&#8221;<br />
  QT_QTDESIGNER_INCLUDE_DIR   Path to &#8220;include/QtDesigner&#8221;<br />
  QT_QTDESIGNERCOMPONENTS_INCLUDE_DIR   Path to &#8220;include/QtDesigner&#8221;<br />
  QT_QTGUI_INCLUDE_DIR        Path to &#8220;include/QtGui&#8221;<br />
  QT_QTHELP_INCLUDE_DIR       Path to &#8220;include/QtHelp&#8221;<br />
  QT_QTMOTIF_INCLUDE_DIR      Path to &#8220;include/QtMotif&#8221;<br />
  QT_QTMULTIMEDIA_INCLUDE_DIR Path to &#8220;include/QtMultimedia&#8221;<br />
  QT_QTNETWORK_INCLUDE_DIR    Path to &#8220;include/QtNetwork&#8221;<br />
  QT_QTNSPLUGIN_INCLUDE_DIR   Path to &#8220;include/QtNsPlugin&#8221;<br />
  QT_QTOPENGL_INCLUDE_DIR     Path to &#8220;include/QtOpenGL&#8221;<br />
  QT_QTSCRIPT_INCLUDE_DIR     Path to &#8220;include/QtScript&#8221;<br />
  QT_QTSQL_INCLUDE_DIR        Path to &#8220;include/QtSql&#8221;<br />
  QT_QTSVG_INCLUDE_DIR        Path to &#8220;include/QtSvg&#8221;<br />
  QT_QTTEST_INCLUDE_DIR       Path to &#8220;include/QtTest&#8221;<br />
  QT_QTWEBKIT_INCLUDE_DIR     Path to &#8220;include/QtWebKit&#8221;<br />
  QT_QTXML_INCLUDE_DIR        Path to &#8220;include/QtXml&#8221;<br />
  QT_QTXMLPATTERNS_INCLUDE_DIR  Path to &#8220;include/QtXmlPatterns&#8221;<br />
  QT_PHONON_INCLUDE_DIR       Path to &#8220;include/phonon&#8221;<br />
  QT_QTSCRIPTTOOLS_INCLUDE_DIR       Path to &#8220;include/QtScriptTools&#8221;</p>
<p>  QT_BINARY_DIR               Path to &#8220;bin&#8221; of Qt4<br />
  QT_LIBRARY_DIR              Path to &#8220;lib&#8221; of Qt4<br />
  QT_PLUGINS_DIR              Path to &#8220;plugins&#8221; for Qt4<br />
  QT_TRANSLATIONS_DIR         Path to &#8220;translations&#8221; of Qt4<br />
  QT_DOC_DIR                  Path to &#8220;doc&#8221; of Qt4<br />
  QT_MKSPECS_DIR              Path to &#8220;mkspecs&#8221; of Qt4</p>
<p> For every library of Qt, a QT_QTFOO_LIBRARY variable is defined, with the full path to the library. </p>
<p> So there are the following variables: The Qt3Support library: QT_QT3SUPPORT_LIBRARY </p>
<p> The QtAssistant library: QT_QTASSISTANT_LIBRARY </p>
<p> The QtAssistantClient library: QT_QTASSISTANTCLIENT_LIBRARY </p>
<p> The QAxServer library: QT_QAXSERVER_LIBRARY </p>
<p> The QAxContainer library: QT_QAXCONTAINER_LIBRARY </p>
<p> The QtCore library: QT_QTCORE_LIBRARY </p>
<p> The QtDBus library: QT_QTDBUS_LIBRARY </p>
<p> The QtDesigner library: QT_QTDESIGNER_LIBRARY </p>
<p> The QtDesignerComponents library: QT_QTDESIGNERCOMPONENTS_LIBRARY </p>
<p> The QtGui library: QT_QTGUI_LIBRARY </p>
<p> The QtHelp library: QT_QTHELP_LIBRARY </p>
<p> The QtMotif library: QT_QTMOTIF_LIBRARY </p>
<p> The QtMultimedia library: QT_QTMULTIMEDIA_LIBRARY </p>
<p> The QtNetwork library: QT_QTNETWORK_LIBRARY </p>
<p> The QtNsPLugin library: QT_QTNSPLUGIN_LIBRARY </p>
<p> The QtOpenGL library: QT_QTOPENGL_LIBRARY </p>
<p> The QtScript library: QT_QTSCRIPT_LIBRARY </p>
<p> The QtScriptTools library: QT_QTSCRIPTTOOLS_LIBRARY </p>
<p> The QtSql library: QT_QTSQL_LIBRARY </p>
<p> The QtSvg library: QT_QTSVG_LIBRARY </p>
<p> The QtTest library: QT_QTTEST_LIBRARY </p>
<p> The QtUiTools library: QT_QTUITOOLS_LIBRARY </p>
<p> The QtWebKit library: QT_QTWEBKIT_LIBRARY </p>
<p> The QtXml library: QT_QTXML_LIBRARY </p>
<p> The QtXmlPatterns library: QT_QTXMLPATTERNS_LIBRARY </p>
<p> The qtmain library for Windows QT_QTMAIN_LIBRARY </p>
<p> The Phonon library: QT_PHONON_LIBRARY </p>
<p> also defined, but NOT for general use are </p>
<pre>
  QT_MOC_EXECUTABLE                   Where to find the moc tool.
  QT_UIC_EXECUTABLE                   Where to find the uic tool.
  QT_UIC3_EXECUTABLE                  Where to find the uic3 tool.
  QT_RCC_EXECUTABLE                   Where to find the rcc tool
  QT_DBUSCPP2XML_EXECUTABLE           Where to find the qdbuscpp2xml tool.
  QT_DBUSXML2CPP_EXECUTABLE           Where to find the qdbusxml2cpp tool.
  QT_LUPDATE_EXECUTABLE               Where to find the lupdate tool.
  QT_LRELEASE_EXECUTABLE              Where to find the lrelease tool.
  QT_QCOLLECTIONGENERATOR_EXECUTABLE  Where to find the qcollectiongenerator tool.
  QT_DESIGNER_EXECUTABLE              Where to find the Qt designer tool.
  QT_LINGUIST_EXECUTABLE              Where to find the Qt linguist tool.
  
</pre>
<p> These are around for backwards compatibility they will be set </p>
<pre>
  QT_WRAP_CPP  Set true if QT_MOC_EXECUTABLE is found
  QT_WRAP_UI   Set true if QT_UIC_EXECUTABLE is found
  
</pre>
<p> These variables do _NOT_ have any effect anymore (compared to FindQt.cmake) </p>
<pre>
  QT_MT_REQUIRED         Qt4 is now always multithreaded
  
</pre>
<p> These variables are set to &quot;&quot; Because Qt structure changed (They make no sense in Qt4) </p>
<pre>
  QT_QT_LIBRARY        Qt-Library is now split
</pre>
<dt><code>FindRUBY</code></p>
<dd> Find Ruby </p>
<p> This module finds if Ruby is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  RUBY_LIBRARY      = full path+file to the ruby library
  RUBY_INCLUDE_PATH = path to where ruby.h can be found
  RUBY_EXECUTABLE   = full path+file to the ruby binary
  RUBY_FOUND        = Ruby was found under system.
</pre>
<dt><code>FindSIP</code></p>
<dd>
<p> Find SIP ~~~~~~~~ </p>
<p> SIP website: <a rel="nofollow" href="http://www.riverbankcomputing.co.uk/sip/index.php">http://www.riverbankcomputing.co.uk/sip/index.php</a> </p>
<p> Find the installed version of SIP. FindSIP should be called after Python has been found. </p>
<p> This file defines the following variables: </p>
<p> SIP_VERSION &#8211; The version of SIP found expressed as a 6 digit hex number </p>
<pre>
     suitable for comparision as a string.
</pre>
<p> SIP_VERSION_STR &#8211; The version of SIP found as a human readable string. </p>
<p> SIP_EXECUTABLE &#8211; Path and filename of the SIP command line executable. </p>
<p> SIP_INCLUDE_DIR &#8211; Directory holding the SIP C++ header file. </p>
<p> SIP_DEFAULT_SIP_DIR &#8211; Default directory where .sip files should be installed </p>
<pre>
     into.
</pre>
<dt><code>FindSamba</code></p>
<dd> Try to find the samba directory library </p>
<p> Once done this will define </p>
<pre>
  SAMBA_FOUND - system has SAMBA
  SAMBA_INCLUDE_DIR - the SAMBA include directory
  SAMBA_LIBRARIES - The libraries needed to use SAMBA
  Set SAMBA_REQUIRE_SMBC_SET_CONTEXT to TRUE if you need a version of Samba
  which comes with smbc_set_context()
</pre>
<dt><code>FindSane</code></p>
<dd>
<p> cmake macro to test if we use sane </p>
<pre>
  SANE_FOUND - system has SANE libs
  SANE_INCLUDE_DIR - the SANE include directory
  SANE_LIBRARIES - The libraries needed to use SANE
</pre>
<dt><code>FindSasl2</code></p>
<dd> Try to find the sasl2 directory library </p>
<p> Once done this will define </p>
<pre>
  SASL2_FOUND - system has SASL2
  SASL2_INCLUDE_DIR - the SASL2 include directory
  SASL2_LIBRARIES - The libraries needed to use SASL2
</pre>
<dt><code>FindSharedDesktopOntologies</code></p>
<dd> Try to find shared-desktop-ontologies </p>
<p> The shared-desktop-ontologies package is a direct dependancy of the Nepomuk semantic desktop system and provides all necessary ontology files like RDF, RDFS, NRL, or NIE. </p>
<p> The package is created by the OSCAF project (<a rel="nofollow" href="http://oscaf.sourceforge.net">http://oscaf.sourceforge.net</a>). </p>
<p> Once done this will define </p>
<pre>
  SHAREDDESKTOPONTOLOGIES_FOUND         - system has shared-desktop-ontologies
  SHAREDDESKTOPONTOLOGIES_ROOT_DIR      - Folder where the ontologies are stored
  SHAREDDESKTOPONTOLOGIES_VERSION_MAJOR - The major version number, i.e. '1' in '1.2'
  SHAREDDESKTOPONTOLOGIES_VERSION_MINOR - The minor version number, i.e. '2' in '1.2'
  SHAREDDESKTOPONTOLOGIES_VERSION       - The complete version string, i.e. '1.2'
</pre>
<dt><code>FindSharedMimeInfo</code></p>
<dd> Try to find the shared-mime-info package </p>
<pre>
  SHARED_MIME_INFO_MINIMUM_VERSION - Set this to the minimum version you need, default is 0.18
</pre>
<p> Once done this will define </p>
<pre>
  SHARED_MIME_INFO_FOUND - system has the shared-mime-info package
  UPDATE_MIME_DATABASE_EXECUTABLE - the update-mime-database executable
</pre>
<dt><code>FindSoprano</code></p>
<dd>
<p> Find an installation of Soprano </p>
<p> Sets the following variables: </p>
<pre>
  Soprano_FOUND, SOPRANO_FOUND  - true is Soprano has been found
  SOPRANO_ONTO2VOCABULARYCLASS_EXECUTABLE - the onto2vocabularyclass program, required for adding ontologies
  SOPRANO_SOPRANOCMD_EXECUTABLE - the sopranocmd program
  SOPRANO_INCLUDE_DIR      - The include directory
  SOPRANO_LIBRARIES        - The Soprano core library to link to (libsoprano)
  SOPRANO_INDEX_LIBRARIES  - The Soprano index library (libsopranoindex)
  SOPRANO_CLIENT_LIBRARIES - The Soprano client library (libsopranoclient)
  SOPRANO_SERVER_LIBRARIES - The Soprano server library (libsopranoserver)
  SOPRANO_VERSION          - The Soprano version (string value)
</pre>
<p> SOPRANO_PLUGIN_NQUADPARSER_FOUND &#8211; true if the nquadparser plugin is found SOPRANO_PLUGIN_NQUADSERIALIZER_FOUND &#8211; true if the nquadserializer plugin is found SOPRANO_PLUGIN_RAPTORPARSER_FOUND &#8211; true if the raptorparser plugin is found SOPRANO_PLUGIN_RAPTORSERIALIZER_FOUND &#8211; true if the raptorserializer plugin is found SOPRANO_PLUGIN_REDLANDBACKEND_FOUND &#8211; true if the redlandbackend plugin is found SOPRANO_PLUGIN_SESAME2BACKEND_FOUND &#8211; true if the sesame2backend plugin is found SOPRANO_PLUGIN_VIRTUOSOBACKEND_FOUND &#8211; true if the virtuosobackend plugin is found </p>
<p> Options: </p>
<pre>
  Set SOPRANO_MIN_VERSION to set the minimum required Soprano version (default: 1.99)
</pre>
<p> FindSoprano.cmake supports the COMPONENTS keyword of find_package(). If the REQUIRED keyword is used and any of the specified components have not been found, SOPRANO_FOUND will be set to FALSE. </p>
<p> The following components are supported: </p>
<pre>
   PLUGIN_NQUADPARSER
   PLUGIN_NQUADSERIALIZER
   PLUGIN_RAPTORPARSER
   PLUGIN_RAPTORSERIALIZER
   PLUGIN_REDLANDBACKEND
   PLUGIN_SESAME2BACKEND
   PLUGIN_VIRTUOSOBACKEND
</pre>
<dt><code>FindSqlite</code></p>
<dd> Try to find Sqlite </p>
<p> Once done this will define </p>
<pre>
  SQLITE_FOUND - system has Sqlite
  SQLITE_INCLUDE_DIR - the Sqlite include directory
  SQLITE_LIBRARIES - Link these to use Sqlite
  SQLITE_DEFINITIONS - Compiler switches required for using Sqlite
</pre>
<p> Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<dt><code>FindStrigi</code></p>
<dd> Try to find Strigi, a fast and small desktop search program (<a rel="nofollow" href="http://strigi.sourceforge.net">http://strigi.sourceforge.net</a> ) </p>
<p> Once done this will define </p>
<pre>
  STRIGI_FOUND - system has Strigi
  STRIGI_INCLUDE_DIR - the Strigi include directory
  STRIGI_STREAMANALYZER_LIBRARY - Link these to use Strigi streamanalyzer
  STRIGI_STREAMS_LIBRARY - Link these to use Strigi streams
  STRIGI_LINE_ANALYZER_PREFIX - strigi plugin prefix
  STRIGI_THROUGH_ANALYZER_PREFIX - strigi plugin prefix
</pre>
<dt><code>FindTaglib</code></p>
<dd> Try to find the Taglib library </p>
<p> Once done this will define </p>
<pre>
  TAGLIB_FOUND - system has the taglib library
  TAGLIB_CFLAGS - the taglib cflags
  TAGLIB_LIBRARIES - The libraries needed to use taglib
</pre>
<dt><code>FindUSB</code></p>
<dd> Try to find the freetype library </p>
<p> Once done this defines </p>
<pre>
  LIBUSB_FOUND - system has libusb
  LIBUSB_INCLUDE_DIR - the libusb include directory
  LIBUSB_LIBRARIES - Link these to use libusb
</pre>
<dt><code>FindX11</code></p>
<dd> Find X11 installation </p>
<p> Try to find X11 on UNIX systems. The following values are defined </p>
<pre>
  X11_FOUND        - True if X11 is available
  X11_INCLUDE_DIR  - include directories to use X11
  X11_LIBRARIES    - link against these to use X11
</pre>
<p> and also the following more fine grained variables: </p>
<pre>
                X11_ICE_INCLUDE_PATH,          X11_ICE_LIB,        X11_ICE_FOUND
                X11_SM_INCLUDE_PATH,           X11_SM_LIB,         X11_SM_FOUND
                X11_X11_INCLUDE_PATH,          X11_X11_LIB
                X11_Xaccessrules_INCLUDE_PATH,                     X11_Xaccess_FOUND
                X11_Xaccessstr_INCLUDE_PATH,                       X11_Xaccess_FOUND
                X11_Xau_INCLUDE_PATH,          X11_Xau_LIB,        X11_Xau_FOUND
                X11_Xcomposite_INCLUDE_PATH,   X11_Xcomposite_LIB, X11_Xcomposite_FOUND
                X11_Xcursor_INCLUDE_PATH,      X11_Xcursor_LIB,    X11_Xcursor_FOUND
                X11_Xdamage_INCLUDE_PATH,      X11_Xdamage_LIB,    X11_Xdamage_FOUND
                X11_Xdmcp_INCLUDE_PATH,        X11_Xdmcp_LIB,      X11_Xdmcp_FOUND
                                               X11_Xext_LIB,       X11_Xext_FOUND
                X11_dpms_INCLUDE_PATH,         (in X11_Xext_LIB),  X11_dpms_FOUND
                X11_XShm_INCLUDE_PATH,         (in X11_Xext_LIB),  X11_XShm_FOUND
                X11_Xshape_INCLUDE_PATH,       (in X11_Xext_LIB),  X11_Xshape_FOUND
                X11_xf86misc_INCLUDE_PATH,     X11_Xxf86misc_LIB,  X11_xf86misc_FOUND
                X11_xf86vmode_INCLUDE_PATH,                        X11_xf86vmode_FOUND
                X11_Xfixes_INCLUDE_PATH,       X11_Xfixes_LIB,     X11_Xfixes_FOUND
                X11_Xft_INCLUDE_PATH,          X11_Xft_LIB,        X11_Xft_FOUND
                X11_Xinerama_INCLUDE_PATH,     X11_Xinerama_LIB,   X11_Xinerama_FOUND
                X11_Xinput_INCLUDE_PATH,       X11_Xinput_LIB,     X11_Xinput_FOUND
                X11_Xkb_INCLUDE_PATH,                              X11_Xkb_FOUND
                X11_Xkblib_INCLUDE_PATH,                           X11_Xkb_FOUND
                X11_Xkbfile_INCLUDE_PATH,      X11_Xkbfile_LIB,    X11_Xkbfile_FOUND
                X11_Xpm_INCLUDE_PATH,          X11_Xpm_LIB,        X11_Xpm_FOUND
                X11_XTest_INCLUDE_PATH,        X11_XTest_LIB,      X11_XTest_FOUND
                X11_Xrandr_INCLUDE_PATH,       X11_Xrandr_LIB,     X11_Xrandr_FOUND
                X11_Xrender_INCLUDE_PATH,      X11_Xrender_LIB,    X11_Xrender_FOUND
                X11_Xscreensaver_INCLUDE_PATH, X11_Xscreensaver_LIB, X11_Xscreensaver_FOUND
                X11_Xt_INCLUDE_PATH,           X11_Xt_LIB,         X11_Xt_FOUND
                X11_Xutil_INCLUDE_PATH,                            X11_Xutil_FOUND
                X11_Xv_INCLUDE_PATH,           X11_Xv_LIB,         X11_Xv_FOUND
                X11_XSync_INCLUDE_PATH,        (in X11_Xext_LIB),  X11_XSync_FOUND
</pre>
<dt><code>FindXine</code></p>
<dd> Try to find the XINE library </p>
<p> Once done this will define </p>
<pre>
  XINE_FOUND - system has the XINE library
  XINE_VERSION - XINE version
  XINE_BUGFIX_VERSION - the XINE bugfix version
  XINE_INCLUDE_DIR - the XINE include directory
  XINE_LIBRARY - The libraries needed to use XINE
  XINE_XCB_FOUND - libxine can use XCB for video output
</pre>
<dt><code>FindXmms</code></p>
<dd>
<p> Search xmms Once done this will define </p>
<pre>
  XMMS_FOUND        - system has xmms
  XMMS_INCLUDE_DIRS - the xmms include directory
  XMMS_LIBRARIES    - Link these to use xmms
  XMMS_LDFLAGS      - for compatibility only, same as XMMS_LIBRARIES
</pre>
<dt><code>KDE4Macros</code></p>
<dd>
<p> for documentation look at FindKDE4Internal.cmake </p>
<dt><code>MacroAddCompileFlags</code></p>
<dd> MACRO_ADD_COMPILE_FLAGS(&lt;_target&gt; &quot;flags&#8230;&quot;) </p>
<dt><code>MacroAddLinkFlags</code></p>
<dd> MACRO_ADD_LINK_FLAGS(&lt;_target&gt; &quot;flags&#8230;&quot;) </p>
<dt><code>MacroAdditionalCleanFiles</code></p>
<dd> MACRO_ADDITIONAL_CLEAN_FILES(files&#8230;) </p>
<p> MACRO_OPTIONAL_FIND_PACKAGE( &lt;name&gt; [QUIT] ) </p>
<dt><code>MacroAppendIf</code></p>
<dd>
<p> MACRO_APPEND_IF(CONDITION VAR VALUE1&#8230;VALUEN ) This convenience macro appends the values VALUE1 up to VALUEN to the list given in VAR, but only if the variable CONDITION is TRUE: </p>
<p> usage example: IF(SOMELIB_FOUND) </p>
<pre>
   SET(my_sources ${my_sources} somefile.c someotherfile.c)
</pre>
<p> ENDIF(SOMELIB_FOUND) </p>
<p> becomes: MACRO_APPEND_IF(SOMELIB_FOUND my_sources somefile.c someotherfile.c) </p>
<dt><code>MacroBoolTo01</code></p>
<dd>
<p> MACRO_BOOL_TO_01( VAR RESULT0 &#8230; RESULTN ) This macro evaluates its first argument and sets all the given vaiables either to 0 or 1 depending on the value of the first one </p>
<dt><code>MacroEnsureOutOfSourceBuild</code></p>
<dd> MACRO_ENSURE_OUT_OF_SOURCE_BUILD(&lt;errorMessage&gt;) </p>
<p> MACRO_ENSURE_OUT_OF_SOURCE_BUILD(&lt;errorMessage&gt;) </p>
<pre>
    Call this macro in your project if you want to enforce out-of-source builds.
    If an in-source build is detected, it will abort with the given error message.
    This macro works in any of the CMakeLists.txt of your project, but the recommended
    location to call this is close to the beginning of the top level CMakeLists.txt
</pre>
<dt><code>MacroEnsureVersion</code></p>
<dd>
<p> This file defines the following macros for developers to use in ensuring that installed software is of the right version: </p>
<p> MACRO_ENSURE_VERSION &#8211; test that a version number is greater than </p>
<pre>
                               or equal to some minimum
</pre>
<p> MACRO_ENSURE_VERSION_RANGE &#8211; test that a version number is greater than </p>
<pre>
                               or equal to some minimum and less than some
                               maximum
</pre>
<p> MACRO_ENSURE_VERSION2 &#8211; deprecated, do not use in new code </p>
<dt><code>MacroLibrary</code></p>
<dd> include MacroLibrary offers a collection of macros which extend the built-in cmake commands </p>
<dt><code>MacroLogFeature</code></p>
<dd>
<p> This file defines the Feature Logging macros. </p>
<p> MACRO_LOG_FEATURE(VAR FEATURE DESCRIPTION URL [REQUIRED [MIN_VERSION [COMMENTS]]]) </p>
<pre>
   Logs the information so that it can be displayed at the end
   of the configure run
   VAR : TRUE or FALSE, indicating whether the feature is supported
   FEATURE: name of the feature, e.g. &quot;libjpeg&quot;
   DESCRIPTION: description what this feature provides
   URL: home page
   REQUIRED: TRUE or FALSE, indicating whether the featue is required
   MIN_VERSION: minimum version number. empty string if unneeded
   COMMENTS: More info you may want to provide.  empty string if unnecessary
</pre>
<p> MACRO_DISPLAY_FEATURE_LOG() </p>
<pre>
   Call this to display the collected results.
   Exits CMake with a FATAL error message if a required feature is missing
</pre>
<p> Example: </p>
<p> INCLUDE(MacroLogFeature) </p>
<p> FIND_PACKAGE(JPEG) MACRO_LOG_FEATURE(JPEG_FOUND &quot;libjpeg&quot; &quot;Support JPEG images&quot; &quot;<a rel="nofollow" href="http://www.ijg.org">http://www.ijg.org</a>&quot; TRUE &quot;3.2a&quot; &quot;&quot;) &#8230; MACRO_DISPLAY_FEATURE_LOG() </p>
<dt><code>MacroOptionalAddSubdirectory</code></p>
<dd> MACRO_OPTIONAL_ADD_SUBDIRECTORY() combines ADD_SUBDIRECTORY() with an OPTION() </p>
<p> MACRO_OPTIONAL_ADD_SUBDIRECTORY( &lt;dir&gt; ) If you use MACRO_OPTIONAL_ADD_SUBDIRECTORY() instead of ADD_SUBDIRECTORY(), this will have two effects 1 &#8211; CMake will not complain if the directory doesn&#8217;t exist </p>
<pre>
     This makes sense if you want to distribute just one of the subdirs
     in a source package, e.g. just one of the subdirs in kdeextragear.
</pre>
<p> 2 &#8211; If the directory exists, it will offer an option to skip the </p>
<pre>
     subdirectory.
     This is useful if you want to compile only a subset of all
     directories.
</pre>
<p> If the CMake variable DISABLE_ALL_OPTIONAL_SUBDIRECTORIES is set to TRUE for the first CMake run on the project, all optional subdirectories will be disabled by default (but can of course be enabled via the respective options). E.g. the following will disable all optional subdirectories except the one named &quot;kcalc&quot;: </p>
<pre>
   $ cmake -DDISABLE_ALL_OPTIONAL_SUBDIRECTORIES=TRUE -DBUILD_kcalc=TRUE &lt;srcdir&gt;
</pre>
<dt><code>MacroOptionalDependPackage</code></p>
<dd>
<p> Search if cmake module is installed in computer cmake will not fail but signal that we must install depend package before. add as previously name of cmake module &quot;_name&quot; and define package needed &quot;_module_needed&quot; if return DEPEND_PACKAGE_${_name} </p>
<dt><code>MacroOptionalFindPackage</code></p>
<dd> MACRO_OPTIONAL_FIND_PACKAGE() combines FIND_PACKAGE() with an OPTION() </p>
<p> MACRO_OPTIONAL_FIND_PACKAGE( &lt;name&gt; [QUIT] ) This macro is a combination of OPTION() and FIND_PACKAGE(), it works like FIND_PACKAGE(), but additionally it automatically creates an option name WITH_&lt;name&gt;, which can be disabled via the cmake GUI. or via -DWITH_&lt;name&gt;=OFF The standard &lt;name&gt;_FOUND variables can be used in the same way as when using the normal FIND_PACKAGE() </p>
<dt><code>MacroPushRequiredVars</code></p>
<dd>
<p> this module defines two macros: MACRO_PUSH_REQUIRED_VARS() and MACRO_POP_REQUIRED_VARS() use these if you call cmake macros which use any of the CMAKE_REQUIRED_XXX variables </p>
<p> Usage: MACRO_PUSH_REQUIRED_VARS() SET(CMAKE_REQUIRED_DEFINITIONS ${CMAKE_REQUIRED_DEFINITIONS} -DSOME_MORE_DEF) CHECK_FUNCTION_EXISTS(&#8230;) MACRO_POP_REQUIRED_VARS() </p>
<dt><code>MacroWriteBasicCMakeVersionFile</code></p>
<dd>
<pre>
  MACRO_WRITE_BASIC_CMAKE_VERSION_FILE( _filename _major _minor _patch)
    Writes a file for use as &lt;package&gt;ConfigVersion.cmake file to &lt;_filename&gt;.
    See the documentation of FIND_PACKAGE() for details on this.
    _filename is the output filename, it should be in the build tree.
    _major is the major version number of the project to be installed
    _minor is the minor version number of the project to be installed
    _patch is the patch version number of the project to be installed
</pre>
<dt><code>NepomukAddOntologyClasses</code></p>
<dd>
<p> Use the Nepomuk resource class generator to generate convinient Resource subclasses from ontologies. </p>
<p> Usage: </p>
<pre><code>
NEPOMUK_ADD_ONTOLOGY_CLASSES(&lt;sources - var&gt;[FAST]
                                            [ONTOLOGIES]&lt;onto - file1&gt;[&lt;onto - file2&gt;...]
                                                                      [CLASSES&lt;class1&gt;[&lt;class2&gt;...]]
                                                                      [VISIBILITY&lt;visibility - name&gt;])
</code></pre>
<p> If FAST is specified the rcgen parameter &#8211;fast will be used which results in resource classes not based on Nepomuk::Resource but on a custom class which does not perform any checks and simply writes the data to Nepomuk (hence the name fast). </p>
<p> The optional CLASSES parameter allows to specify the classes to be generated (RDF URIs) in case one does not want all classes in the ontologies to be generated. </p>
<p> The optional VISIBILITY parameter can only be used in non-fast mode and allows to set the gcc visibility to make the generated classes usable in a publically exported API. The &lt;visibility-name&gt; is used to create the name of the export macro and the export include file. Thus, when using &quot;VISIBILITY foobar&quot; include file &quot;foobar_export.h&quot; needs to define FOOBAR_EXPORT. </p>
<p> Copyright (c) 2009 Sebastian Trueg &lt;trueg [at] kde.org&gt; </p>
<p> Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<dt><code>NepomukMacros</code></p>
<dd>
<p> This file contains the following macros: </p>
<p> NEPOMUK_GENERATE_FROM_ONTOLOGY Parameters: </p>
<pre>
   ontofile     - Path to the NRL ontology defining the resources to be generated.
   targetdir    - Folder to which the generated sources should be written.
   out_headers  - Variable which will be filled with the names of all generated headers.
   out_sources  - Variable which will be filled with the names of all generated sources.
   out_includes - Variable which will be filled with complete include statements of all 
                  generated resource classes.
</pre>
<p> In addition to the parameters an arbitrary number of template filenames can be set as arguments </p>
<p> In case of success NEPOMUK_RESOURCES_GENERATED is true, otherwise false </p>
<dt><code>PythonMacros</code></p>
<dd>
<p> Python macros ~~~~~~~~~~~~~ Copyright (c) 2007, Simon Edwards &lt;simon [at] simonzone.com&gt; </p>
<p> Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<p> This file defines the following macros: </p>
<p> PYTHON_INSTALL (SOURCE_FILE DESINATION_DIR) </p>
<pre>
     Install the SOURCE_FILE, which is a Python .py file, into the
     destination directory during install. The file will be byte compiled
     and both the .py file and .pyc file will be installed.
</pre>
<dt><code>Qt4ConfigDependentSettings</code></p>
<dd>
<p> This file is included by FindQt4.cmake, don&#8217;t include it directly. </p>
<dt><code>Qt4Macros</code></p>
<dd>
<p> This file is included by FindQt4.cmake, don&#8217;t include it directly. </p>
<dt><code>SIPMacros</code></p>
<dd>
<p> Macros for SIP ~~~~~~~~~~~~~~ Copyright (c) 2007, Simon Edwards &lt;simon [at] simonzone.com&gt; Redistribution and use is allowed according to the terms of the BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<p> SIP website: <a rel="nofollow" href="http://www.riverbankcomputing.co.uk/sip/index.php">http://www.riverbankcomputing.co.uk/sip/index.php</a> </p>
<p> This file defines the following macros: </p>
<p> ADD_SIP_PYTHON_MODULE (MODULE_NAME MODULE_SIP [library1, libaray2, &#8230;]) </p>
<pre>
     Specifies a SIP file to be built into a Python module and installed.
     MODULE_NAME is the name of Python module including any path name. (e.g.
     os.sys, Foo.bar etc). MODULE_SIP the path and filename of the .sip file
     to process and compile. libraryN are libraries that the Python module,
     which is typically a shared library, should be linked to. The built
     module will also be install into Python's site-packages directory.
</pre>
<p> The behaviour of the ADD_SIP_PYTHON_MODULE macro can be controlled by a number of variables: </p>
<p> SIP_INCLUDES &#8211; List of directories which SIP will scan through when looking </p>
<pre>
     for included .sip files. (Corresponds to the -I option for SIP.)
</pre>
<p> SIP_TAGS &#8211; List of tags to define when running SIP. (Corresponds to the -t </p>
<pre>
     option for SIP.)
</pre>
<p> SIP_CONCAT_PARTS &#8211; An integer which defines the number of parts the C++ code </p>
<pre>
     of each module should be split into. Defaults to 8. (Corresponds to the
     -j option for SIP.)
</pre>
<p> SIP_DISABLE_FEATURES &#8211; List of feature names which should be disabled </p>
<pre>
     running SIP. (Corresponds to the -x option for SIP.)
</pre>
<p> SIP_EXTRA_OPTIONS &#8211; Extra command line options which should be passed on to </p>
<pre>
     SIP.
</pre>
<dt><code>Win32Macros</code></p>
<dd>
<p> win32 macros </p>
<p> ADDEXPLORERWRAPPER(project) </p>
<p> Exists only under Win32 ! </p>
<p> addExplorerWrapper creates batch files for fast access to the build environment from the win32 explorer. </p>
<p> For mingw and nmake projects it opens a command shell, for Visual Studio IDE&#8217;s (at least tested with VS 8 2005) it opens the related .sln file with paths setting specified at configure time. </p>
<dt><code>create_exe_symlink</code></p>
<dd>
<p> Create an executable symlink to a Python script. This also sets the target script&#8217;s permission bits. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ccmake/">ccmake</a>(1), <a href="/docs/linux/man/1-cpack/">cpack</a>(1), <a href="/docs/linux/man/1-ctest/">ctest</a>(1), <a href="/docs/linux/man/1-cmakecommands/">cmakecommands</a>(1), <a href="/docs/linux/man/1-cmakecompat/">cmakecompat</a>(1), <a href="/docs/linux/man/1-cmakemodules/">cmakemodules</a>(1), <a href="/docs/linux/man/1-cmakeprops/">cmakeprops</a>(1), <a href="/docs/linux/man/1-cmakevars/">cmakevars</a>(1)</code> </p>
<p> The following resources are available to get help using CMake: </p>
<dl>
<dt><code>Home Page</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org">http://www.cmake.org</a> </p>
<p> The primary starting point for learning about CMake. </p>
<dt><code>Frequently Asked Questions</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake_FAQ">http://www.cmake.org/Wiki/CMake_FAQ</a> </p>
<p> A Wiki is provided containing answers to frequently asked questions. </p>
<dt><code>Online Documentation</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/HTML/Documentation.html">http://www.cmake.org/HTML/Documentation.html</a> </p>
<p> Links to available documentation may be found on this web page. </p>
<dt><code>Mailing List</code></p>
<dd> <a rel="nofollow" href="http://www.cmake.org/HTML/MailingLists.html">http://www.cmake.org/HTML/MailingLists.html</a> </p>
<p> For help and discussion about using cmake, a mailing list is provided at cmake [at] cmake.org. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <a rel="nofollow" href="http://www.cmake.org">http://www.cmake.org</a> before posting questions to the list. </p>
</dl>
<p> Summary of helpful links: </p>
<pre>
  Home: <a rel="nofollow" href="http://www.cmake.org">http://www.cmake.org</a>
  Docs: <a rel="nofollow" href="http://www.cmake.org/HTML/Documentation.html">http://www.cmake.org/HTML/Documentation.html</a>
  Mail: <a rel="nofollow" href="http://www.cmake.org/HTML/MailingLists.html">http://www.cmake.org/HTML/MailingLists.html</a>
  FAQ:  <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake_FAQ">http://www.cmake.org/Wiki/CMake_FAQ</a>
</pre>
<h2>Index</h2>
