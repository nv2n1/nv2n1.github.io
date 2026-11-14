---
title: "ecm-kde-modules(7)"
name: "ecm-kde-modules"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecm-kde-modules/"
description: "ecm-kde-modules – ECM KDE Modules Reference"
---

<p>ecm-kde-modules &#8211; ECM KDE Modules Reference</p>
<h2>Introduction</h2>
<p>Extra CMake Modules (ECM) provides several modules that provide default settings (like installation directories, compiler flags and other CMake options) aimed at software produced by the KDE modules; these are documented here. ECM also provides modules with more general functionality, documented in <code><a href="/docs/linux/man/7-ecm-modules/">ecm-modules</a>(7)</code>, and ones that extend the functionality of the <code>find_package</code> command, documented in <code><a href="/docs/linux/man/7-ecm-find-modules/">ecm-find-modules</a>(7)</code>. </p>
<p> To use these modules, you need to tell CMake to find the ECM package, and then add either <code>${ECM_MODULE_PATH}</code> or <code>${ECM_KDE_MODULE_DIR}</code> to the <code>CMAKE_MODULE_PATH</code> variable: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_DIR})</pre>
<p>Using <code>${ECM_MODULE_PATH}</code> will also make the other types of modules available.</p>
<h2>All Kde Modules</h2>
<h3>KDECMakeSettings</h3>
<p>Changes various CMake settings to what the KDE community views as more sensible defaults. </p>
<p> It is recommended to include this module with the NO_POLICY_SCOPE flag, otherwise you may get spurious warnings with some versions of CMake. </p>
<p> It is split into three parts, which can be independently disabled if desired.</p>
<h3>Runtime Paths</h3>
<p>The default runtime path (used on Unix systems to search for dynamically-linked libraries) is set to include the location that libraries will be installed to (as set in LIB_INSTALL_DIR or, if the former is not set, KDE_INSTALL_LIBDIR), and also the linker search path. </p>
<p> Note that <code>LIB_INSTALL_DIR</code> or alternatively <code>KDE_INSTALL_LIBDIR</code> needs to be set before including this module. Typically, this is done by including the <code>KDEInstallDirs</code> module. </p>
<p> This section can be disabled by setting <code>KDE_SKIP_RPATH_SETTINGS</code> to TRUE before including this module.</p>
<h3>Testing</h3>
<p>Testing is enabled by default, and an option (BUILD_TESTING) is provided for users to control this. See the CTest module documentation in the CMake manual for more details. </p>
<p> This section can be disabled by setting <code>KDE_SKIP_TEST_SETTINGS</code> to TRUE before including this module.</p>
<h3>Build Settings</h3>
<p>Various CMake build defaults are altered, such as searching source and build directories for includes first and enabling automoc by default. </p>
<p> This section can be disabled by setting <code>KDE_SKIP_BUILD_SETTINGS</code> to TRUE before including this module. </p>
<p> This section also provides an &quot;uninstall&quot; target that can be individually disabled by setting <code>KDE_SKIP_UNINSTALL_TARGET</code> to TRUE before including this module. </p>
<p> By default on OS X, X11 and XCB related detections are disabled. However if the need would arise to use these technologies, the detection can be enabled by setting <code>APPLE_FORCE_X11</code> to <code>ON</code>. </p>
<p> A warning is printed for the developer to know that the detection is disabled on OS X. This message can be turned off by setting <code>APPLE_SUPPRESS_X11_WARNING</code> to <code>ON</code>. </p>
<p> Since pre-1.0.0. </p>
<p> <code>ENABLE_CLAZY</code> option is added (OFF by default) when clang is being used. Turning this option on will force clang to load the clazy plugins for richer warnings on Qt-related code. </p>
<p> If clang is not being used, this won&#8217;t have an effect. See <i><a rel="nofollow" href="https://commits.kde.org/clazy?path=README.md">https://commits.kde.org/clazy?path=README.md</a></i> </p>
<p> Since 5.17.0</p>
<dl>
<dt>&bull;</p>
<dd>Uninstall target functionality since 1.7.0.</p>
<dt>&bull;</p>
<dd><code>APPLE_FORCE_X11</code> option since 5.14.0 (detecting X11 was previously the default behavior)</p>
<dt>&bull;</p>
<dd><code>APPLE_SUPPRESS_X11_WARNING</code> option since 5.14.0</dl>
<h3>KDECompilerSettings</h3>
<p>Set useful compile and link flags for C++ (and C) code. </p>
<p> Enables many more warnings than the default, and sets stricter modes for some compiler features. By default, exceptions are disabled; kde_target_enable_exceptions() can be used to re-enable them for a specific target. </p>
<p> NB: it is recommended to include this module with the NO_POLICY_SCOPE flag, otherwise you may get spurious warnings with some versions of CMake. </p>
<p> This module provides the following functions: </p>
<pre>kde_source_files_enable_exceptions([file1 [file2 [...]]])</pre>
<p>Enables exceptions for specific source files. This should not be used on source files in a language other than C++. </p>
<pre>kde_target_enable_exceptions(target &lt;INTERFACE|PUBLIC|PRIVATE&gt;)</pre>
<p>Enables exceptions for a specific target. This should not be used on a target that has source files in a language other than C++. </p>
<pre>kde_enable_exceptions()</pre>
<p>Enables exceptions for C++ source files compiled for the CMakeLists.txt file in the current directory and all subdirectories. </p>
<p> Since pre-1.0.0.</p>
<h3>KDEFrameworkCompilerSettings</h3>
<p>Set stricter compile and link flags for KDE Frameworks modules. </p>
<p> The KDECompilerSettings module is included and, in addition, various defines that affect the Qt libraries are set to enforce certain conventions. </p>
<p> For example, constructions like QString(&quot;foo&quot;) are prohibited, instead forcing the use of QLatin1String or QStringLiteral, and some Qt-defined keywords like signals and slots will not be defined. </p>
<p> NB: it is recommended to include this module with the NO_POLICY_SCOPE flag, otherwise you may get spurious warnings with some versions of CMake. </p>
<p> Since pre-1.0.0.</p>
<h3>KDEInstallDirs</h3>
<p>Define KDE standard installation directories. </p>
<p> Note that none of the variables defined by this module provide any information about the location of already-installed KDE software. </p>
<p> Inclusion of this module defines the following variables:</p>
<dl>
<dt><code>KDE_INSTALL_&lt;dir&gt;</code></p>
<dd>destination for files of a given type</p>
<dt><code>KDE_INSTALL_FULL_&lt;dir&gt;</code></p>
<dd>corresponding absolute path </p>
<p> where <code>&lt;dir&gt;</code> is one of (default values in parentheses and alternative, deprecated variable name in square brackets):</p>
<dt><code>BUNDLEDIR</code></p>
<dd>application bundles (<code>/Applications/KDE</code>) [<code>BUNDLE_INSTALL_DIR</code>]</p>
<dt><code>EXECROOTDIR</code></p>
<dd>executables and libraries (<code>&lt;empty&gt;</code>) [<code>EXEC_INSTALL_PREFIX</code>]</p>
<dt><code>BINDIR</code></p>
<dd>user executables (<code>EXECROOTDIR/bin</code>) [<code>BIN_INSTALL_DIR</code>]</p>
<dt><code>SBINDIR</code></p>
<dd>system admin executables (<code>EXECROOTDIR/sbin</code>) [<code>SBIN_INSTALL_DIR</code>]</p>
<dt><code>LIBDIR</code></p>
<dd>object code libraries (<code>EXECROOTDIR/lib</code>, <code>EXECROOTDIR/lib64</code> or <code>EXECROOTDIR/lib/&lt;multiarch-tuple</code> on Debian) [<code>LIB_INSTALL_DIR</code>]</p>
<dt><code>LIBEXECDIR</code></p>
<dd>executables for internal use by programs and libraries (<code>BINDIR</code> on Windows, <code>LIBDIR/libexec</code> otherwise) [<code>LIBEXEC_INSTALL_DIR</code>]</p>
<dt><code>CMAKEPACKAGEDIR</code></p>
<dd>CMake packages, including config files (<code>LIBDIR/cmake</code>) [<code>CMAKECONFIG_INSTALL_PREFIX</code>]</p>
<dt><code>QTPLUGINDIR</code></p>
<dd>Qt plugins (<code>LIBDIR/plugins</code>) [<code>QT_PLUGIN_INSTALL_DIR</code>]</p>
<dt><code>PLUGINDIR</code></p>
<dd>Plugins (<code>QTPLUGINDIR</code>) [<code>PLUGIN_INSTALL_DIR</code>]</p>
<dt><code>QTQUICKIMPORTSDIR</code></p>
<dd>QtQuick1 imports (<code>QTPLUGINDIR/imports</code>) [<code>IMPORTS_INSTALL_DIR</code>]</p>
<dt><code>QMLDIR</code></p>
<dd>QtQuick2 imports (<code>LIBDIR/qml</code>) [<code>QML_INSTALL_DIR</code>]</p>
<dt><code>INCLUDEDIR</code></p>
<dd>C and C++ header files (<code>include</code>) [<code>INCLUDE_INSTALL_DIR</code>]</p>
<dt><code>LOCALSTATEDIR</code></p>
<dd>modifiable single-machine data (<code>var</code>)</p>
<dt><code>SHAREDSTATEDIR</code></p>
<dd>modifiable architecture-independent data (<code>com</code>)</p>
<dt><code>DATAROOTDIR</code></p>
<dd>read-only architecture-independent data root (<code>share</code>) [<code>SHARE_INSTALL_PREFIX</code>]</p>
<dt><code>DATADIR</code></p>
<dd>read-only architecture-independent data (<code>DATAROOTDIR</code>) [<code>DATA_INSTALL_DIR</code>]</p>
<dt><code>DOCBUNDLEDIR</code></p>
<dd>documentation bundles generated using kdoctools (<code>DATAROOTDIR/doc/HTML</code>) [<code>HTML_INSTALL_DIR</code>]</p>
<dt><code>KCFGDIR</code></p>
<dd>kconfig description files (<code>DATAROOTDIR/config.kcfg</code>) [<code>KCFG_INSTALL_DIR</code>]</p>
<dt><code>KCONFUPDATEDIR</code></p>
<dd>kconf_update scripts (<code>DATAROOTDIR/kconf_update</code>) [<code>KCONF_UPDATE_INSTALL_DIR</code>]</p>
<dt><code>KSERVICES5DIR</code></p>
<dd>services for KDE Frameworks 5 (<code>DATAROOTDIR/kservices5</code>) [<code>SERVICES_INSTALL_DIR</code>]</p>
<dt><code>KSERVICETYPES5DIR</code></p>
<dd>service types for KDE Frameworks 5 (<code>DATAROOTDIR/kservicetypes5</code>) [<code>SERVICETYPES_INSTALL_DIR</code>]</p>
<dt><code>KXMLGUI5DIR</code></p>
<dd>knotify description files (<code>DATAROOTDIR/kxmlgui5</code>) [<code>KXMLGUI_INSTALL_DIR</code>]</p>
<dt><code>KTEMPLATESDIR</code></p>
<dd>Kapptemplate and Kdevelop templates (<code>kdevappwizard/templates</code>)</p>
<dt><code>KNOTIFY5RCDIR</code></p>
<dd>knotify description files (<code>DATAROOTDIR/knotifications5</code>) [<code>KNOTIFYRC_INSTALL_DIR</code>]</p>
<dt><code>ICONDIR</code></p>
<dd>icons (<code>DATAROOTDIR/icons</code>) [<code>ICON_INSTALL_DIR</code>]</p>
<dt><code>LOCALEDIR</code></p>
<dd>knotify description files (<code>DATAROOTDIR/locale</code>) [<code>LOCALE_INSTALL_DIR</code>]</p>
<dt><code>SOUNDDIR</code></p>
<dd>sound files (<code>DATAROOTDIR/sounds</code>) [<code>SOUND_INSTALL_DIR</code>]</p>
<dt><code>TEMPLATEDIR</code></p>
<dd>templates (<code>DATAROOTDIR/templates</code>) [<code>TEMPLATES_INSTALL_DIR</code>]</p>
<dt><code>WALLPAPERDIR</code></p>
<dd>desktop wallpaper images (<code>DATAROOTDIR/wallpapers</code>) [<code>WALLPAPER_INSTALL_DIR</code>]</p>
<dt><code>APPDIR</code></p>
<dd>application desktop files (<code>DATAROOTDIR/applications</code>) [<code>XDG_APPS_INSTALL_DIR</code>]</p>
<dt><code>DESKTOPDIR</code></p>
<dd>desktop directories (<code>DATAROOTDIR/desktop-directories</code>) [<code>XDG_DIRECTORY_INSTALL_DIR</code>]</p>
<dt><code>MIMEDIR</code></p>
<dd>mime description files (<code>DATAROOTDIR/mime/packages</code>) [<code>XDG_MIME_INSTALL_DIR</code>]</p>
<dt><code>METAINFODIR</code></p>
<dd>AppStream component metadata files (<code>DATAROOTDIR/metainfo</code>)</p>
<dt><code>MANDIR</code></p>
<dd>man documentation (<code>DATAROOTDIR/man</code>) [<code>MAN_INSTALL_DIR</code>]</p>
<dt><code>INFODIR</code></p>
<dd>info documentation (<code>DATAROOTDIR/info</code>)</p>
<dt><code>DBUSDIR</code></p>
<dd>D-Bus (<code>DATAROOTDIR/dbus-1</code>)</p>
<dt><code>DBUSINTERFACEDIR</code></p>
<dd>D-Bus interfaces (<code>DBUSDIR/interfaces</code>) [<code>DBUS_INTERFACES_INSTALL_DIR</code>]</p>
<dt><code>DBUSSERVICEDIR</code></p>
<dd>D-Bus session services (<code>DBUSDIR/services</code>) [<code>DBUS_SERVICES_INSTALL_DIR</code>]</p>
<dt><code>DBUSSYSTEMSERVICEDIR</code></p>
<dd>D-Bus system services (<code>DBUSDIR/system-services</code>) [<code>DBUS_SYSTEM_SERVICES_INSTALL_DIR</code>]</p>
<dt><code>SYSCONFDIR</code></p>
<dd>read-only single-machine data (<code>etc</code>, or <code>/etc</code> if <code>CMAKE_INSTALL_PREFIX</code> is <code>/usr</code>) [<code>SYSCONF_INSTALL_DIR</code>]</p>
<dt><code>CONFDIR</code></p>
<dd>application configuration files (<code>SYSCONFDIR/xdg</code>) [<code>CONFIG_INSTALL_DIR</code>]</p>
<dt><code>AUTOSTARTDIR</code></p>
<dd>autostart files (<code>CONFDIR/autostart</code>) [<code>AUTOSTART_INSTALL_DIR</code>] </p>
<p> If <code>KDE_INSTALL_DIRS_NO_DEPRECATED</code> is set to TRUE before including this module, the deprecated variables (listed in the square brackets above) are not defined. </p>
<p> In addition, for each <code>KDE_INSTALL_*</code> variable, an equivalent <code>CMAKE_INSTALL_*</code> variable is defined. If <code>KDE_INSTALL_DIRS_NO_DEPRECATED</code> is set to TRUE, only those variables defined by the <code>GNUInstallDirs</code> module (shipped with CMake) are defined. If <code>KDE_INSTALL_DIRS_NO_CMAKE_VARIABLES</code> is set to TRUE, no variables with a <code>CMAKE_</code> prefix will be defined by this module (other than CMAKE_INSTALL_DEFAULT_COMPONENT_NAME &#8211; see below). </p>
<p> The <code>KDE_INSTALL_&lt;dir&gt;</code> variables (or their <code>CMAKE_INSTALL_&lt;dir&gt;</code> or deprecated counterparts) may be passed to the DESTINATION options of <code>install()</code> commands for the corresponding file type. They are set in the CMake cache, and so the defaults above can be overridden by users. </p>
<p> Note that the <code>KDE_INSTALL_&lt;dir&gt;</code>, <code>CMAKE_INSTALL_&lt;dir&gt;</code> or deprecated form of the variable can be changed using CMake command line variable definitions; in either case, all forms of the variable will be affected. The effect of passing multiple forms of the same variable on the command line (such as <code>KDE_INSTALL_BINDIR</code> and <code>CMAKE_INSTALL_BINDIR</code> is undefined. </p>
<p> The variable <code>KDE_INSTALL_TARGETS_DEFAULT_ARGS</code> is also defined (along with the deprecated form <code>INSTALL_TARGETS_DEFAULT_ARGS</code>). This should be used when libraries or user-executable applications are installed, in the following manner: </p>
<pre>install(TARGETS mylib myapp ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})</pre>
<p>It MUST NOT be used for installing plugins, system admin executables or executables only intended for use internally by other code. Those should use <code>KDE_INSTALL_PLUGINDIR</code>, <code>KDE_INSTALL_SBINDIR</code> or <code>KDE_INSTALL_LIBEXECDIR</code> respectively. </p>
<p> Additionally, <code>CMAKE_INSTALL_DEFAULT_COMPONENT_NAME</code> will be set to <code>${PROJECT_NAME}</code> to provide a sensible default for this CMake option. </p>
<p> Note that mixing absolute and relative paths, particularly for <code>BINDIR</code>, <code>LIBDIR</code> and <code>INCLUDEDIR</code>, can cause issues with exported targets. Given that the default values for these are relative paths, relative paths should be used on the command line when possible (eg: use <code>-DKDE_INSTALL_LIBDIR=lib64</code> instead of <code>-DKDE_INSTALL_LIBDIR=/usr/lib/lib64</code> to override the library directory). </p>
<p> Since pre-1.0.0. </p>
<p> NB: The variables starting <code>KDE_INSTALL_</code> are only available since 1.6.0. The <code>APPDIR</code> install variable is available since 1.1.0.</dl>
<h3>KDETemplateGenerator</h3>
<p>Packages KApptemplate/KDevelop compatible application templates </p>
<p> This module provides a functionality to package in a tarball and install project templates compatible with the format used by KApptemplate and KDevelop. Useful for providing minimal examples for the usage of the KDE Frameworks. </p>
<p> This module provides the following function: </p>
<p> kde_package_app_templates( TEMPLATES template1 [template2] [&#8230;] INSTALL_DIR directory) </p>
<p> INSTALL_DIR is the directory to install the template package to. In most cases you will want to use the variable KDE_INSTALL_KTEMPLATESDIR from <code>KDEInstallDirs</code>. </p>
<p> TEMPLATES lists subdirectories containing template files; each <code>&lt;template&gt;</code> directory will be packaged into a file named <code>&lt;template&gt;.tar.bz2</code> and installed to the appropriate location. </p>
<p> The template is a minimal source tree of an application as if it was an application project by itself, with names (file names or text inside) the text files replaced by the following placeholders when needed:</p>
<dl>
<dt><code>%{PROJECTDIRNAME}</code></p>
<dd>%{APPNAMELC}-%{VERSION} for KAppTemplate</p>
<dt><code>%{APPNAME}</code></p>
<dd>project name as entered by user ex: MyKApp</p>
<dt><code>%{APPNAMELC}</code></p>
<dd>project name in lower case ex: mykapp</p>
<dt><code>%{APPNAMEUC}</code></p>
<dd>project name in upper case ex: MYKAPP</p>
<dt><code>%{CPP_TEMPLATE}</code></p>
<dd>license header for cpp file</p>
<dt><code>%{H_TEMPLATE}</code></p>
<dd>license header for h file</p>
<dt><code>%{AUTHOR}</code></p>
<dd>author name ex: George Ignacious</p>
<dt><code>%{EMAIL}</code></p>
<dd>author email ex: <i>foo [at] bar.org</i></p>
<dt><code>%{VERSION}</code></p>
<dd>project version ex: 0.1</p>
<dt><code>%{dest}</code></p>
<dd>used in .kdevtemplate</p>
<dt><code>%{src}</code></p>
<dd>used in .kdevtemplate </p>
<p> Multiple templates can be passed at once. </p>
<p> Since 5.18</dl>
<h2>Copyright</h2>
<p>KDE Developers</p>
