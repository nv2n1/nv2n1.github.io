---
title: "ecm-modules(7)"
name: "ecm-modules"
section: "7"
letter: "e"
url: "/docs/linux/man/7-ecm-modules/"
description: "ecm-modules – ECM Modules Reference"
---

<p>ecm-modules &#8211; ECM Modules Reference</p>
<h2>Introduction</h2>
<p>Extra CMake Modules (ECM) provides various modules that provide useful functions for CMake scripts. ECM actually provides three types of modules that can be used from CMake scripts: those that extend the functionality of the <code>find_package</code> command are documented in <code><a href="/docs/linux/man/7-ecm-find-modules/">ecm-find-modules</a>(7)</code>; those that provide standard settings for software produced by the KDE community are documented in <code><a href="/docs/linux/man/7-ecm-kde-modules/">ecm-kde-modules</a>(7)</code>. The rest provide macros and functions for general use by CMake scripts and are documented here. </p>
<p> To use these modules, you need to tell CMake to find the ECM package, and then add either <code>${ECM_MODULE_PATH}</code> or <code>${ECM_MODULE_DIR}</code> to the <code>CMAKE_MODULE_PATH</code> variable: </p>
<pre>find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_DIR})</pre>
<p>Using <code>${ECM_MODULE_PATH}</code> will also make the find modules and KDE modules available. </p>
<p> Note that there are also toolchain modules, documented in <code><a href="/docs/linux/man/7-ecm-toolchains/">ecm-toolchains</a>(7)</code>, but these are used by users building the software rather than developers writing CMake scripts.</p>
<h2>All Modules</h2>
<h3>ECMAddAppIcon</h3>
<p>Add icons to executable files and packages. </p>
<pre>ecm_add_app_icon(&lt;sources_var&gt;
 ICONS &lt;icon&gt; [&lt;icon&gt; [...]])</pre>
<p>The given icons, whose names must match the pattern: </p>
<pre>&lt;size&gt;-&lt;other_text&gt;.png</pre>
<p>will be added to the executable target whose sources are specified by <code>&lt;sources_var&gt;</code> on platforms that support it (Windows and Mac OS X). Other icon files are ignored but on Mac SVG files can be supported and it is thus possible to mix those with png files in a single macro call. </p>
<p> <code>&lt;size&gt;</code> is a numeric pixel size (typically 16, 32, 48, 64, 128 or 256). <code>&lt;other_text&gt;</code> can be any other text. See the platform notes below for any recommendations about icon sizes.</p>
<dl>
<dt><code>Windows notes</code></p>
<dd>
<dt>&bull;</p>
<dd>Icons are compiled into the executable using a resource file.</p>
<dt>&bull;</p>
<dd>Icons may not show up in Windows Explorer if the executable target does not have the <code>WIN32_EXECUTABLE</code> property set.</p>
<dt>&bull;</p>
<dd>The tool png2ico is required. See <code>FindPng2Ico</code>.</p>
<dt>&bull;</p>
<dd>Supported sizes: 16, 32, 48, 64, 128.</p>
<dt><code>Mac OS X notes</code></p>
<dd>
<dt>&bull;</p>
<dd>The executable target must have the <code>MACOSX_BUNDLE</code> property set.</p>
<dt>&bull;</p>
<dd>Icons are added to the bundle.</p>
<dt>&bull;</p>
<dd>If the ksvg2icns tool from KIconThemes is available, .svg and .svgz files are accepted; the first that is converted successfully to .icns will provide the application icon. SVG files are ignored otherwise.</p>
<dt>&bull;</p>
<dd>The tool iconutil (provided by Apple) is required for bitmap icons.</p>
<dt>&bull;</p>
<dd>Supported sizes: 16, 32, 64, 128, 256 (and 512, 1024 after OS X 10.9).</p>
<dt>&bull;</p>
<dd>At least a 128x128px (or an SVG) icon is required.</p>
<dt>&bull;</p>
<dd>Larger sizes are automatically used to substitute for smaller sizes on &quot;Retina&quot; (high-resolution) displays. For example, a 32px icon, if provided, will be used as a 32px icon on standard-resolution displays, and as a 16px-equivalent icon (with an &quot;@2x&quot; tag) on high-resolution displays. ksvg2icns handles this internally.</p>
<dt>&bull;</p>
<dd>This function sets the <code>MACOSX_BUNDLE_ICON_FILE</code> variable to the name of the generated icns file, so that it will be used as the <code>MACOSX_BUNDLE_ICON_FILE</code> target property when you call <code>add_executable</code>. </p>
<p> Since 1.7.0.</dl>
<h3>ECMAddTests</h3>
<p>Convenience functions for adding tests. </p>
<pre>ecm_add_tests(&lt;sources&gt; LINK_LIBRARIES &lt;library&gt; [&lt;library&gt; [...]]
 [NAME_PREFIX &lt;prefix&gt;]
 [GUI]
 [TARGET_NAMES_VAR &lt;target_names_var&gt;]
 [TEST_NAMES_VAR &lt;test_names_var&gt;])</pre>
<p>A convenience function for adding multiple tests, each consisting of a single source file. For each file in &lt;sources&gt;, an executable target will be created (the name of which will be the basename of the source file). This will be linked against the libraries given with LINK_LIBRARIES. Each executable will be added as a test with the same name. </p>
<p> If NAME_PREFIX is given, this prefix will be prepended to the test names, but not the target names. As a result, it will not prevent clashes between tests with the same name in different parts of the project, but it can be used to give an indication of where to look for a failing test. </p>
<p> If the flag GUI is passed the test binaries will be GUI executables, otherwise the resulting binaries will be console applications (regardless of the value of CMAKE_WIN32_EXECUTABLE or CMAKE_MACOSX_BUNDLE). Be aware that this changes the executable entry point on Windows (although some frameworks, such as Qt, abstract this difference away). </p>
<p> The TARGET_NAMES_VAR and TEST_NAMES_VAR arguments, if given, should specify a variable name to receive the list of generated target and test names, respectively. This makes it convenient to apply properties to them as a whole, for example, using set_target_properties() or set_tests_properties(). </p>
<p> The generated target executables will have the effects of ecm_mark_as_test() (from the <code>ECMMarkAsTest</code> module) applied to it. </p>
<pre>ecm_add_test(&lt;sources&gt; LINK_LIBRARIES &lt;library&gt; [&lt;library&gt; [...]]
 [TEST_NAME &lt;name&gt;]
 [NAME_PREFIX &lt;prefix&gt;]
 [GUI])</pre>
<p>This is a single-test form of ecm_add_tests that allows multiple source files to be used for a single test. If using multiple source files, TEST_NAME must be given; this will be used for both the target and test names (and, as with ecm_add_tests(), the NAME_PREFIX argument will be prepended to the test name). </p>
<p> Since pre-1.0.0.</p>
<h3>ECMCoverageOption</h3>
<p>Allow users to easily enable GCov code coverage support. </p>
<p> Code coverage allows you to check how much of your codebase is covered by your tests. This module makes it easy to build with support for <i>GCov</i>. </p>
<p> When this module is included, a <code>BUILD_COVERAGE</code> option is added (default OFF). Turning this option on enables GCC&#8217;s coverage instrumentation, and links against <code>libgcov</code>. </p>
<p> Note that this will probably break the build if you are not using GCC. </p>
<p> Since 1.3.0.</p>
<h3>ECMCreateQmFromPoFiles</h3>
<p><code>WARNING:</code> This module is deprecated and will be removed by ECM 1.0. Use ECMPoQmTools instead. </p>
<p> Generate QTranslator (.qm) catalogs from Gettext (.po) catalogs. </p>
<pre>ecm_create_qm_from_po_files(PO_FILES &lt;file1&gt;... &lt;fileN&gt;
 [CATALOG_NAME &lt;catalog_name&gt;]
 [INSTALL_DESTINATION &lt;install_destination&gt;])</pre>
<p>Creates the necessary rules to compile .po files into .qm files, and install them. </p>
<p> The .qm files are installed in <code>&lt;install_destination&gt;/&lt;lang&gt;/LC_MESSAGES</code>, where &lt;install_destination&gt; is the INSTALL_DESTINATION argument and &lt;lang&gt; is extracted from the &quot;Language&quot; field inside the .po file. </p>
<p> INSTALL_DESTINATION defaults to <code>${LOCALE_INSTALL_DIR}</code> if defined, otherwise it uses <code>${CMAKE_INSTALL_LOCALEDIR}</code> if that is defined, otherwise it uses <code>share/locale</code>. </p>
<p> CATALOG_NAME defines the name of the installed .qm files. If set, .qm files will be installed as <code>&lt;catalog_name&gt;.qm</code>. If not set .qm files will be named after the name of their source .po file. </p>
<p> Setting the catalog name is useful when all .po files for a target are kept in a single source directory. For example, the &quot;mylib&quot; probject might keep all its translations in a &quot;po&quot; directory, like this: </p>
<pre>po/
 es.po
 fr.po</pre>
<p>Without setting CATALOG_NAME, those .po will be turned into .qm and installed as: </p>
<pre>share/locale/fr/LC_MESSAGES/fr.qm
share/locale/es/LC_MESSAGES/es.qm</pre>
<p>If CATALOG_NAME is set to &quot;mylib&quot;, they will be installed as: </p>
<pre>share/locale/fr/LC_MESSAGES/mylib.qm
share/locale/es/LC_MESSAGES/mylib.qm</pre>
<p>Which is what the loader created by ecm_create_qm_loader() expects. </p>
<p> ecm_create_qm_from_po_files() creates a &quot;translation&quot; target. This target builds all .po files into .qm files. </p>
<pre>ecm_create_qm_loader(&lt;source_files_var&gt; &lt;catalog_name&gt;)</pre>
<p>ecm_create_qm_loader() generates a C++ file which ensures translations are automatically loaded at startup. The path of the .cpp file is appended to &lt;source_files_var&gt;. Typical usage is like: </p>
<pre>set(mylib_SRCS foo.cpp bar.cpp)
ecm_create_qm_loader(mylib_SRCS mylib)
add_library(mylib ${mylib_SRCS})</pre>
<p>This generates a C++ file which loads &quot;mylib.qm&quot; at startup, assuming it has been installed by ecm_create_qm_from_po_files(), and compiles it into <code>mylib</code>. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMEnableSanitizers</h3>
<p>Enable compiler sanitizer flags. </p>
<p> The following sanitizers are supported:</p>
<dl>
<dt>&bull;</p>
<dd>Address Sanitizer</p>
<dt>&bull;</p>
<dd>Memory Sanitizer</p>
<dt>&bull;</p>
<dd>Thread Sanitizer</p>
<dt>&bull;</p>
<dd>Leak Sanitizer</p>
<dt>&bull;</p>
<dd>Undefined Behaviour Sanitizer </p>
<p> All of them are implemented in Clang, depending on your version, and there is an work in progress in GCC, where some of them are currently implemented. </p>
<p> This module will check your current compiler version to see if it supports the sanitizers that you want to enable</dl>
<h3>Usage</h3>
<p>Simply add: </p>
<pre>include(ECMEnableSanitizers)</pre>
<p>to your <code>CMakeLists.txt</code>. Note that this module is included in KDECompilerSettings, so projects using that module do not need to also include this one. </p>
<p> The sanitizers are not enabled by default. Instead, you must set <code>ECM_ENABLE_SANITIZERS</code> (either in your <code>CMakeLists.txt</code> or on the command line) to a semicolon-separated list of sanitizers you wish to enable. The options are:</p>
<dl>
<dt>&bull;</p>
<dd>address</p>
<dt>&bull;</p>
<dd>memory</p>
<dt>&bull;</p>
<dd>thread</p>
<dt>&bull;</p>
<dd>leak</p>
<dt>&bull;</p>
<dd>undefined </p>
<p> The sanitizers &quot;address&quot;, &quot;memory&quot; and &quot;thread&quot; are mutually exclusive. You cannot enable two of them in the same build. </p>
<p> &quot;leak&quot; requires the &quot;address&quot; sanitizer. </p>
<p> <code>NOTE:</code> To reduce the overhead induced by the instrumentation of the sanitizers, it is advised to enable compiler optimizations (<code>-O1</code> or higher).</dl>
<h3>Example</h3>
<p>This is an example of usage: </p>
<pre>mkdir build
cd build
cmake -DECM_ENABLE_SANITIZERS='address;leak;undefined' ..</pre>
<p><code>NOTE:</code> Most of the sanitizers will require Clang. To enable it, use: </p>
<pre>-DCMAKE_CXX_COMPILER=clang++</pre>
<p>Since 1.3.0.</p>
<h3>ECMFindModuleHelpers</h3>
<p>Helper macros for find modules: ecm_find_package_version_check(), ecm_find_package_parse_components() and ecm_find_package_handle_library_components(). </p>
<pre>ecm_find_package_version_check(&lt;name&gt;)</pre>
<p>Prints warnings if the CMake version or the project&#8217;s required CMake version is older than that required by extra-cmake-modules. </p>
<pre>ecm_find_package_parse_components(&lt;name&gt;
 RESULT_VAR &lt;variable&gt;
 KNOWN_COMPONENTS &lt;component1&gt; [&lt;component2&gt; [...]]
 [SKIP_DEPENDENCY_HANDLING])</pre>
<p>This macro will populate &lt;variable&gt; with a list of components found in &lt;name&gt;_FIND_COMPONENTS, after checking that all those components are in the list of KNOWN_COMPONENTS; if there are any unknown components, it will print an error or warning (depending on the value of &lt;name&gt;_FIND_REQUIRED) and call return(). </p>
<p> The order of components in &lt;variable&gt; is guaranteed to match the order they are listed in the KNOWN_COMPONENTS argument. </p>
<p> If SKIP_DEPENDENCY_HANDLING is not set, for each component the variable &lt;name&gt;_&lt;component&gt;_component_deps will be checked for dependent components. If &lt;component&gt; is listed in &lt;name&gt;_FIND_COMPONENTS, then all its (transitive) dependencies will also be added to &lt;variable&gt;. </p>
<pre>ecm_find_package_handle_library_components(&lt;name&gt;
 COMPONENTS &lt;component&gt; [&lt;component&gt; [...]]
 [SKIP_DEPENDENCY_HANDLING])
 [SKIP_PKG_CONFIG])</pre>
<p>Creates an imported library target for each component. The operation of this macro depends on the presence of a number of CMake variables. </p>
<p> The &lt;name&gt;_&lt;component&gt;_lib variable should contain the name of this library, and &lt;name&gt;_&lt;component&gt;_header variable should contain the name of a header file associated with it (whatever relative path is normally passed to &#8216;#include&#8217;). &lt;name&gt;_&lt;component&gt;_header_subdir variable can be used to specify which subdirectory of the include path the headers will be found in. ecm_find_package_components() will then search for the library and include directory (creating appropriate cache variables) and create an imported library target named &lt;name&gt;::&lt;component&gt;. </p>
<p> Additional variables can be used to provide additional information: </p>
<p> If SKIP_PKG_CONFIG, the &lt;name&gt;_&lt;component&gt;_pkg_config variable is set, and pkg-config is found, the pkg-config module given by &lt;name&gt;_&lt;component&gt;_pkg_config will be searched for and used to help locate the library and header file. It will also be used to set &lt;name&gt;_&lt;component&gt;_VERSION. </p>
<p> Note that if version information is found via pkg-config, &lt;name&gt;_&lt;component&gt;_FIND_VERSION can be set to require a particular version for each component. </p>
<p> If SKIP_DEPENDENCY_HANDLING is not set, the INTERFACE_LINK_LIBRARIES property of the imported target for &lt;component&gt; will be set to contain the imported targets for the components listed in &lt;name&gt;_&lt;component&gt;_component_deps. &lt;component&gt;_FOUND will also be set to false if any of the compoments in &lt;name&gt;_&lt;component&gt;_component_deps are not found. This requires the components in &lt;name&gt;_&lt;component&gt;_component_deps to be listed before &lt;component&gt; in the COMPONENTS argument. </p>
<p> The following variables will be set:</p>
<dl>
<dt><code>&lt;name&gt;_TARGETS</code></p>
<dd>the imported targets</p>
<dt><code>&lt;name&gt;_LIBRARIES</code></p>
<dd>the found libraries</p>
<dt><code>&lt;name&gt;_INCLUDE_DIRS</code></p>
<dd>the combined required include directories for the components</p>
<dt><code>&lt;name&gt;_DEFINITIONS</code></p>
<dd>the &quot;other&quot; CFLAGS provided by pkg-config, if any</p>
<dt><code>&lt;name&gt;_VERSION</code></p>
<dd>the value of <code>&lt;name&gt;_&lt;component&gt;_VERSION</code> for the first component that has this variable set (note that components are searched for in the order they are passed to the macro), although if it is already set, it will not be altered </p>
<p> Note that these variables are never cleared, so if ecm_find_package_handle_library_components() is called multiple times with different components (typically because of multiple find_package() calls) then <code>&lt;name&gt;_TARGETS</code>, for example, will contain all the targets found in any call (although no duplicates). </p>
<p> Since pre-1.0.0.</dl>
<h3>ECMGenerateHeaders</h3>
<p>Generate C/C++ CamelCase forwarding headers. </p>
<pre>ecm_generate_headers(&lt;camelcase_forwarding_headers_var&gt;
 HEADER_NAMES &lt;CamelCaseName&gt; [&lt;CamelCaseName&gt; [...]]
 [ORIGINAL &lt;CAMELCASE|LOWERCASE&gt;]
 [OUTPUT_DIR &lt;output_dir&gt;]
 [PREFIX &lt;prefix&gt;]
 [REQUIRED_HEADERS &lt;variable&gt;]
 [COMMON_HEADER &lt;HeaderName&gt;]
 [RELATIVE &lt;relative_path&gt;])</pre>
<p>For each CamelCase header name passed to HEADER_NAMES, a file of that name will be generated that will include a version with <code>.h</code> appended. For example, the generated header <code>ClassA</code> will include <code>classa.h</code> (or <code>ClassA.h</code>, see ORIGINAL). If a CamelCaseName consists of multiple comma-separated files, e.g. <code>ClassA,ClassB,ClassC</code>, then multiple camelcase header files will be generated which are redirects to the first header file. The file locations of these generated headers will be stored in &lt;camelcase_forwarding_headers_var&gt;. </p>
<p> ORIGINAL specifies how the name of the original header is written: lowercased or also camelcased. The default is LOWERCASE. Since 1.8.0. </p>
<p> PREFIX places the generated headers in subdirectories. This should be a CamelCase name like <code>KParts</code>, which will cause the CamelCase forwarding headers to be placed in the <code>KParts</code> directory (e.g. <code>KParts/Part</code>). It will also, for the convenience of code in the source distribution, generate forwarding headers based on the original names (e.g. <code>kparts/part.h</code>). This allows includes like <code>&quot;#include &lt;kparts/part.h&gt;&quot;</code> to be used before installation, as long as the include_directories are set appropriately. </p>
<p> OUTPUT_DIR specifies where the files will be generated; this should be within the build directory. By default, <code>${CMAKE_CURRENT_BINARY_DIR}</code> will be used. This option can be used to avoid file conflicts. </p>
<p> REQUIRED_HEADERS specifies an output variable name where all the required headers will be appended so that they can be installed together with the generated ones. This is mostly intended as a convenience so that adding a new header to a project only requires specifying the CamelCase variant in the CMakeLists.txt file; the original variant will then be added to this variable. </p>
<p> COMMON_HEADER generates an additional convenience header which includes all other header files. </p>
<p> The RELATIVE argument indicates where the original headers can be found relative to CMAKE_CURRENT_SOURCE_DIR. It does not affect the generated CamelCase forwarding files, but ecm_generate_headers() uses it when checking that the original header exists, and to generate originally named forwarding headers when PREFIX is set. </p>
<p> To allow other parts of the source distribution (eg: tests) to use the generated headers before installation, it may be desirable to set the INCLUDE_DIRECTORIES property for the library target to output_dir. For example, if OUTPUT_DIR is CMAKE_CURRENT_BINARY_DIR (the default), you could do </p>
<pre>target_include_directories(MyLib PUBLIC &quot;$&lt;BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}&gt;&quot;)</pre>
<p>Example usage (without PREFIX): </p>
<pre>ecm_generate_headers(
 MyLib_FORWARDING_HEADERS
 HEADERS
 MLFoo
 MLBar
 # etc
 REQUIRED_HEADERS MyLib_HEADERS
 COMMON_HEADER MLGeneral
)
install(FILES ${MyLib_FORWARDING_HEADERS} ${MyLib_HEADERS}
 DESTINATION ${CMAKE_INSTALL_PREFIX}/include
 COMPONENT Devel)</pre>
<p>Example usage (with PREFIX): </p>
<pre>ecm_generate_headers(
 MyLib_FORWARDING_HEADERS
 HEADERS
 Foo
 # several classes are contained in bar.h, so generate
 # additional files
 Bar,BarList
 # etc
 PREFIX MyLib
 REQUIRED_HEADERS MyLib_HEADERS
)
install(FILES ${MyLib_FORWARDING_HEADERS}
 DESTINATION ${CMAKE_INSTALL_PREFIX}/include/MyLib
 COMPONENT Devel)
install(FILES ${MyLib_HEADERS}
 DESTINATION ${CMAKE_INSTALL_PREFIX}/include/mylib
 COMPONENT Devel)</pre>
<p>Since pre-1.0.0.</p>
<h3>ECMGeneratePkgConfigFile</h3>
<p>Generate a <i>pkg-config</i> file for the benefit of <i>autotools</i>-based projects. </p>
<pre>ecm_generate_pkgconfig_file(BASE_NAME &lt;baseName&gt;
 [LIB_NAME &lt;libName&gt;]
 [DEPS &quot;&lt;dep&gt; [&lt;dep&gt; [...]]&quot;]
 [FILENAME_VAR &lt;filename_variable&gt;]
 [INCLUDE_INSTALL_DIR &lt;dir&gt;]
 [LIB_INSTALL_DIR &lt;dir&gt;]
 [DEFINES -D&lt;variable=value&gt;...]
 [INSTALL])</pre>
<p><code>BASE_NAME</code> is the name of the module. It&#8217;s the name projects will use to find the module. </p>
<p> <code>LIB_NAME</code> is the name of the library that is being exported. If undefined, it will default to the <code>BASE_NAME</code>. That means the <code>LIB_NAME</code> will be set as the name field as well as the library to link to. </p>
<p> <code>FILENAME_VAR</code> is specified with a variable name. This variable will receive the location of the generated file will be set, within the build directory. This way it can be used in case some processing is required. See also <code>INSTALL</code>. </p>
<p> <code>INCLUDE_INSTALL_DIR</code> specifies where the includes will be installed. If it&#8217;s not specified, it will default to <code>INSTALL_INCLUDEDIR</code>, <code>CMAKE_INSTALL_INCLUDEDIR</code> or just &quot;include/&quot; in case they are specified, with the BASE_NAME postfixed. </p>
<p> <code>LIB_INSTALL_DIR</code> specifies where the library is being installed. If it&#8217;s not specified, it will default to <code>LIB_INSTALL_DIR</code>, <code>CMAKE_INSTALL_LIBDIR</code> or just &quot;lib/&quot; in case they are specified. </p>
<p> <code>DEFINES</code> is a list of preprocessor defines that it is recommended users of the library pass to the compiler when using it. </p>
<p> <code>INSTALL</code> will cause the module to be installed to the <code>pkgconfig</code> subdirectory of <code>LIB_INSTALL_DIR</code>, unless the <code>ECM_PKGCONFIG_INSTALL_DIR</code> cache variable is set to something different. Note that the first call to ecm_generate_pkgconfig_file with the <code>INSTALL</code> argument will cause <code>ECM_PKGCONFIG_INSTALL_DIR</code> to be set to the cache, and will be used in any subsequent calls. </p>
<p> To properly use this macro a version needs to be set. To retrieve it, <code>ECM_PKGCONFIG_INSTALL_DIR</code> uses <code>PROJECT_VERSION</code>. To set it, use the project() command (only available since CMake 3.0) or the ecm_setup_version() macro. </p>
<p> Example usage: </p>
<pre>ecm_generate_pkgconfig_file(
 BASE_NAME KF5Archive
 DEPS Qt5Core
 FILENAME_VAR pkgconfig_filename
 INSTALL
)</pre>
<p>Since 1.3.0.</p>
<h3>ECMGeneratePriFile</h3>
<p>Generate a <code>.pri</code> file for the benefit of qmake-based projects. </p>
<p> As well as the function below, this module creates the cache variable <code>ECM_MKSPECS_INSTALL_DIR</code> and sets the default value to <code>mkspecs/modules</code>. This assumes Qt and the current project are both installed to the same non-system prefix. Packagers who use <code>-DCMAKE_INSTALL_PREFIX=/usr</code> will certainly want to set <code>ECM_MKSPECS_INSTALL_DIR</code> to something like <code>share/qt5/mkspecs/modules</code>. </p>
<p> The main thing is that this should be the <code>modules</code> subdirectory of either the default qmake <code>mkspecs</code> directory or of a directory that will be in the <code>$QMAKEPATH</code> environment variable when qmake is run. </p>
<pre>ecm_generate_pri_file(BASE_NAME &lt;baseName&gt;
 LIB_NAME &lt;libName&gt;
 [DEPS &quot;&lt;dep&gt; [&lt;dep&gt; [...]]&quot;]
 [FILENAME_VAR &lt;filename_variable&gt;]
 [INCLUDE_INSTALL_DIR &lt;dir&gt;]
 [LIB_INSTALL_DIR &lt;dir&gt;])</pre>
<p>If your CMake project produces a Qt-based library, you may expect there to be applications that wish to use it that use a qmake-based build system, rather than a CMake-based one. Creating a <code>.pri</code> file will make use of your library convenient for them, in much the same way that CMake config files make things convenient for CMake-based applications. </p>
<p> ecm_generate_pri_file() generates just such a file. It requires the <code>PROJECT_VERSION_STRING</code> variable to be set. This is typically set by <code>ECMSetupVersion</code>, although the project() command in CMake 3.0.0 and later can also set this. </p>
<p> BASE_NAME specifies the name qmake project (.pro) files should use to refer to the library (eg: KArchive). LIB_NAME is the name of the actual library to link to (ie: the first argument to add_library()). DEPS is a space-separated list of the base names of other libraries (for Qt libraries, use the same names you use with the <code>QT</code> variable in a qmake project file, such as &quot;core&quot; for QtCore). FILENAME_VAR specifies the name of a variable to store the path to the generated file in. </p>
<p> INCLUDE_INSTALL_DIR is the path (relative to <code>CMAKE_INSTALL_PREFIX</code>) that include files will be installed to. It defaults to <code>${INCLUDE_INSTALL_DIR}/&lt;baseName&gt;</code> if the <code>INCLUDE_INSTALL_DIR</code> variable is set. If that variable is not set, the <code>CMAKE_INSTALL_INCLUDEDIR</code> variable is used instead, and if neither are set <code>include</code> is used. LIB_INSTALL_DIR operates similarly for the installation location for libraries; it defaults to <code>${LIB_INSTALL_DIR}</code>, <code>${CMAKE_INSTALL_LIBDIR}</code> or <code>lib</code>, in that order. </p>
<p> Example usage: </p>
<pre>ecm_generate_pri_file(
 BASE_NAME KArchive
 LIB_NAME KF5KArchive
 DEPS &quot;core&quot;
 FILENAME_VAR pri_filename
)
install(FILES ${pri_filename} DESTINATION ${ECM_MKSPECS_INSTALL_DIR})</pre>
<p>A qmake-based project that wished to use this would then do: </p>
<pre>QT += KArchive</pre>
<p>in their <code>.pro</code> file. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMInstallIcons</h3>
<p>Installs icons, sorting them into the correct directories according to the FreeDesktop.org icon naming specification. </p>
<pre>ecm_install_icons(ICONS &lt;icon&gt; [&lt;icon&gt; [...]]
 DESTINATION &lt;icon_install_dir&gt;
 [LANG &lt;l10n_code&gt;]
 [THEME &lt;theme&gt;])</pre>
<p>The given icons, whose names must match the pattern: </p>
<pre>&lt;size&gt;-&lt;group&gt;-&lt;name&gt;.&lt;ext&gt;</pre>
<p>will be installed to the appropriate subdirectory of DESTINATION according to the FreeDesktop.org icon naming scheme. By default, they are installed to the &quot;hicolor&quot; theme, but this can be changed using the THEME argument. If the icons are localized, the LANG argument can be used to install them in a locale-specific directory. </p>
<p> <code>&lt;size&gt;</code> is a numeric pixel size (typically 16, 22, 32, 48, 64, 128 or 256) or <code>sc</code> for scalable (SVG) files, <code>&lt;group&gt;</code> is one of the standard FreeDesktop.org icon groups (actions, animations, apps, categories, devices, emblems, emotes, intl, mimetypes, places, status) and <code>&lt;ext&gt;</code> is one of <code>.png</code>, <code>.mng</code> or <code>.svgz</code>. </p>
<p> The typical installation directory is <code>share/icons</code>. </p>
<pre>ecm_install_icons(ICONS 22-actions-menu_new.png
 DESTINATION share/icons)</pre>
<p>The above code will install the file <code>22-actions-menu_new.png</code> as <code>${CMAKE_INSTALL_PREFIX}/share/icons/&lt;theme&gt;/22&#215;22/actions/menu_new.png</code> </p>
<p> Users of the <code>KDEInstallDirs</code> module would normally use <code>${ICON_INSTALL_DIR}</code> as the DESTINATION, while users of the GNUInstallDirs module should use <code>${CMAKE_INSTALL_DATAROOTDIR}/icons</code>. </p>
<p> An old form of arguments will also be accepted: </p>
<pre>ecm_install_icons(&lt;icon_install_dir&gt; [&lt;l10n_code&gt;])</pre>
<p>This matches files named like: </p>
<pre>&lt;theme&gt;&lt;size&gt;-&lt;group&gt;-&lt;name&gt;.&lt;ext&gt;</pre>
<p>where <code>&lt;theme&gt;</code> is one of * <code>hi</code> for hicolor * <code>lo</code> for locolor * <code>cr</code> for the Crystal icon theme * <code>ox</code> for the Oxygen icon theme * <code>br</code> for the Breeze icon theme </p>
<p> With this syntax, the file <code>hi22-actions-menu_new.png</code> would be installed into <code>&lt;icon_install_dir&gt;/hicolor/22&#215;22/actions/menu_new.png</code> </p>
<p> Since pre-1.0.0.</p>
<h3>ECMMarkAsTest</h3>
<p>Marks a target as only being required for tests. </p>
<pre>ecm_mark_as_test(&lt;target1&gt; [&lt;target2&gt; [...]])</pre>
<p>This will cause the specified targets to not be built unless either BUILD_TESTING is set to ON or the user invokes the <code>buildtests</code> target. </p>
<p> BUILD_TESTING is created as a cache variable by the CTest module and by the <code>KDECMakeSettings</code> module. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMMarkNonGuiExecutable</h3>
<p>Marks an executable target as not being a GUI application. </p>
<pre>ecm_mark_nongui_executable(&lt;target1&gt; [&lt;target2&gt; [...]])</pre>
<p>This will indicate to CMake that the specified targets should not be included in a MACOSX_BUNDLE and should not be WIN32_EXECUTABLEs. On platforms other than MacOS X or Windows, this will have no effect. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMOptionalAddSubdirectory</h3>
<p>Make subdirectories optional. </p>
<pre>ecm_optional_add_subdirectory(&lt;dir&gt;)</pre>
<p>This behaves like add_subdirectory(), except that it does not complain if the directory does not exist. Additionally, if the directory does exist, it creates an option to allow the user to skip it. </p>
<p> This is useful for &quot;meta-projects&quot; that combine several mostly-independent sub-projects. </p>
<p> If the CMake variable DISABLE_ALL_OPTIONAL_SUBDIRECTORIES is set to TRUE for the first CMake run on the project, all optional subdirectories will be disabled by default (but can of course be enabled via the respective options). For example, the following will disable all optional subdirectories except the one named &quot;foo&quot;: </p>
<pre>cmake -DDISABLE_ALL_OPTIONAL_SUBDIRECTORIES=TRUE -DBUILD_foo=TRUE myproject</pre>
<p>Since pre-1.0.0.</p>
<h3>ECMPackageConfigHelpers</h3>
<p>Helper macros for generating CMake package config files. </p>
<p> <code>write_basic_package_version_file()</code> is the same as the one provided by the <i>CMakePackageConfigHelpers</i> module in CMake; see that module&#8217;s documentation for more information. </p>
<pre>ecm_configure_package_config_file(&lt;input&gt; &lt;output&gt;
 INSTALL_DESTINATION &lt;path&gt;
 [PATH_VARS &lt;var1&gt; [&lt;var2&gt; [...]]
 [NO_SET_AND_CHECK_MACRO]
 [NO_CHECK_REQUIRED_COMPONENTS_MACRO])</pre>
<p>This behaves in the same way as configure_package_config_file() from CMake 2.8.12, except that it adds an extra helper macro: find_dependency(). It is highly recommended that you read the <i>documentation for CMakePackageConfigHelpers</i> for more information, particularly with regard to the PATH_VARS argument. </p>
<p> Note that there is no argument that will disable the find_dependency() macro; if you do not require this macro, you should use <code>configure_package_config_file</code> from the CMakePackageConfigHelpers module. </p>
<p> CMake 3.0 includes a CMakeFindDependencyMacro module that provides the find_dependency() macro (which you can <code>include()</code> in your package config file), so this file is only useful for projects wishing to provide config files that will work with CMake 2.8.12.</p>
<h3>Additional Config File Macros</h3>
<pre>find_dependency(&lt;dep&gt; [&lt;version&gt; [EXACT]])</pre>
<p>find_dependency() should be used instead of find_package() to find package dependencies. It forwards the correct parameters for EXACT, QUIET and REQUIRED which were passed to the original find_package() call. It also sets an informative diagnostic message if the dependency could not be found. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMPoQmTools</h3>
<p>This module provides the <code>ecm_process_po_files_as_qm</code> and <code>ecm_install_po_files_as_qm</code> functions for generating QTranslator (.qm) catalogs from Gettext (.po) catalogs, and the <code>ecm_create_qm_loader</code> function for generating the necessary code to load them in a Qt application or library. </p>
<pre>ecm_process_po_files_as_qm(&lt;lang&gt; [ALL]
 [INSTALL_DESTINATION &lt;install_destination&gt;]
 PO_FILES &lt;pofile&gt; [&lt;pofile&gt; [...]])</pre>
<p>Compile .po files into .qm files for the given language. </p>
<p> If INSTALL_DESTINATION is given, the .qm files are installed in <code>&lt;install_destination&gt;/&lt;lang&gt;/LC_MESSAGES</code>. Typically, <code>&lt;install_destination&gt;</code> is set to <code>share/locale</code>. </p>
<p> <code>ecm_process_po_files_as_qm</code> creates a &quot;translations&quot; target. This target builds all .po files into .qm files. If ALL is specified, these rules are added to the &quot;all&quot; target (and so the .qm files will be built by default). </p>
<pre>ecm_create_qm_loader(&lt;source_files_var&gt; &lt;catalog_name&gt;)</pre>
<p>Generates C++ code which ensures translations are automatically loaded at startup. The generated files are appended to <code>&lt;source_files_var&gt;</code>. </p>
<p> It assumes that the .qm file for the language code <code>&lt;lang&gt;</code> is installed as <code>&lt;sharedir&gt;/locale/&lt;lang&gt;/LC_MESSAGES/&lt;catalog_name&gt;.qm</code>, where <code>&lt;sharedir&gt;</code> is one of the directories given by the <code>GenericDataLocation</code> of <code>QStandardPaths</code>. </p>
<p> Typical usage is like: </p>
<pre>set(mylib_SRCS foo.cpp bar.cpp)
ecm_create_qm_loader(mylib_SRCS mylib)
add_library(mylib ${mylib_SRCS})</pre>
<pre>ecm_install_po_files_as_qm(&lt;podir&gt;)</pre>
<p>Searches for .po files and installs them to the standard location. </p>
<p> This is a convenience function which relies on all .po files being kept in <code>&lt;podir&gt;/&lt;lang&gt;/</code>, where <code>&lt;lang&gt;</code> is the language the .po files are written in. </p>
<p> For example, given the following directory structure: </p>
<pre>po/
 fr/
 mylib.po</pre>
<p><code>ecm_install_po_files_as_qm(po)</code> compiles <code>mylib.po</code> into <code>mylib.mo</code> and installs it in <code>&lt;install_destination&gt;/fr/LC_MESSAGES</code>. <code>&lt;install_destination&gt;</code> defaults to <code>${LOCALE_INSTALL_DIR}</code> if defined, otherwise it uses <code>${CMAKE_INSTALL_LOCALEDIR}</code> if that is defined, otherwise it uses <code>share/locale</code>. </p>
<p> Since pre-1.0.0.</p>
<h3>ECMQtDeclareLoggingCategory</h3>
<p>Generate declarations for logging categories in Qt5. </p>
<pre>ecm_qt_declare_logging_category(&lt;sources_var&gt;
 HEADER &lt;filename&gt;
 IDENTIFIER &lt;identifier&gt;
 CATEGORY_NAME &lt;category_name&gt;
 [DEFAULT_SEVERITY
 &lt;Debug|Info|Warning|
 Critical|Fatal&gt;])</pre>
<p>A header file, <code>&lt;filename&gt;</code>, will be generated along with a corresponding source file, which will be added to <code>&lt;sources_var&gt;</code>. These will provide a QLoggingCategory category that can be referred to from C++ code using <code>&lt;identifier&gt;</code>, and from the logging configuration using <code>&lt;category_name&gt;</code>. </p>
<p> If <code>&lt;filename&gt;</code> is not absolute, it will be taken relative to the current binary directory. </p>
<p> If the code is compiled against Qt 5.4 or later, by default it will only log output that is at least the severity specified by <code>DEFAULT_SEVERITY</code>, or &quot;Info&quot; level if <code>DEFAULT_SEVERITY</code> is not given. Note that, due to a bug in Qt 5.5, &quot;Info&quot; may be treated as more severe than &quot;Fatal&quot;. </p>
<p> <code>&lt;identifier&gt;</code> may include namespaces (eg: <code>foo::bar::IDENT</code>). </p>
<p> Since 5.14.0.</p>
<h3>ECMSetupVersion</h3>
<p>Handle library version information. </p>
<pre>ecm_setup_version(&lt;version&gt;
 VARIABLE_PREFIX &lt;prefix&gt;
 [SOVERSION &lt;soversion&gt;]
 [VERSION_HEADER &lt;filename&gt;]
 [PACKAGE_VERSION_FILE &lt;filename&gt; [COMPATIBILITY &lt;compat&gt;]] )</pre>
<p>This parses a version string and sets up a standard set of version variables. It can optionally also create a C version header file and a CMake package version file to install along with the library. </p>
<p> If the <code>&lt;version&gt;</code> argument is of the form <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;</code> (or <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;.&lt;tweak&gt;</code>), The following CMake variables are set: </p>
<pre>&lt;prefix&gt;_VERSION_MAJOR - &lt;major&gt;
&lt;prefix&gt;_VERSION_MINOR - &lt;minor&gt;
&lt;prefix&gt;_VERSION_PATCH - &lt;patch&gt;
&lt;prefix&gt;_VERSION - &lt;version&gt;
&lt;prefix&gt;_VERSION_STRING - &lt;version&gt; (for compatibility: use &lt;prefix&gt;_VERSION instead)
&lt;prefix&gt;_SOVERSION - &lt;soversion&gt;, or &lt;major&gt; if SOVERSION was not given</pre>
<p>If CMake policy CMP0048 is not NEW, the following CMake variables will also be set: PROJECT_VERSION_MAJOR &#8211; &lt;major&gt; PROJECT_VERSION_MINOR &#8211; &lt;minor&gt; PROJECT_VERSION_PATCH &#8211; &lt;patch&gt; PROJECT_VERSION &#8211; &lt;version&gt; PROJECT_VERSION_STRING &#8211; &lt;version&gt; (for compatibility: use PROJECT_VERSION instead) </p>
<p> If the VERSION_HEADER option is used, a simple C header is generated with the given filename. If filename is a relative path, it is interpreted as relative to CMAKE_CURRENT_BINARY_DIR. The generated header contains the following macros: </p>
<pre>&lt;prefix&gt;_VERSION_MAJOR - &lt;major&gt; as an integer
&lt;prefix&gt;_VERSION_MINOR - &lt;minor&gt; as an integer
&lt;prefix&gt;_VERSION_PATCH - &lt;patch&gt; as an integer
&lt;prefix&gt;_VERSION_STRING - &lt;version&gt; as a C string
&lt;prefix&gt;_VERSION - the version as an integer</pre>
<p><code>&lt;prefix&gt;_VERSION</code> has <code>&lt;patch&gt;</code> in the bottom 8 bits, <code>&lt;minor&gt;</code> in the next 8 bits and <code>&lt;major&gt;</code> in the remaining bits. Note that <code>&lt;patch&gt;</code> and <code>&lt;minor&gt;</code> must be less than 256. </p>
<p> If the PACKAGE_VERSION_FILE option is used, a simple CMake package version file is created using the write_basic_package_version_file() macro provided by CMake. It should be installed in the same location as the Config.cmake file of the library so that it can be found by find_package(). If the filename is a relative path, it is interpreted as relative to CMAKE_CURRENT_BINARY_DIR. The optional COMPATIBILITY option is forwarded to write_basic_package_version_file(), and defaults to AnyNewerVersion. </p>
<p> If CMake policy CMP0048 is NEW, an alternative form of the command is available: </p>
<pre>ecm_setup_version(PROJECT
 [VARIABLE_PREFIX &lt;prefix&gt;]
 [SOVERSION &lt;soversion&gt;]
 [VERSION_HEADER &lt;filename&gt;]
 [PACKAGE_VERSION_FILE &lt;filename&gt;] )</pre>
<p>This will use the version information set by the project() command. VARIABLE_PREFIX defaults to the project name. Note that PROJECT must be the first argument. In all other respects, it behaves like the other form of the command. </p>
<p> Since pre-1.0.0. </p>
<p> COMPATIBLITY option available since 1.6.0.</p>
<h3>ECMUninstallTarget</h3>
<p>Add an <code>uninstall</code> target. </p>
<p> By including this module, an <code>uninstall</code> target will be added to your CMake project. This will remove all files installed (or updated) by a previous invocation of the <code>install</code> target. It will not remove files created or modified by an <code>install(SCRIPT)</code> or <code>install(CODE)</code> command; you should create a custom uninstallation target for these and use <code>add_dependency</code> to make the <code>uninstall</code> target depend on it: </p>
<pre>include(ECMUninstallTarget)
install(SCRIPT install-foo.cmake)
add_custom_target(uninstall_foo COMMAND ${CMAKE_COMMAND} -P uninstall-foo.cmake)
add_dependency(uninstall uninstall_foo)</pre>
<p>The target will fail if the <code>install</code> target has not yet been run (so it is not possible to run CMake on the project and then immediately run the <code>uninstall</code> target). </p>
<p> <code>WARNING:</code> CMake deliberately does not provide an <code>uninstall</code> target by default on the basis that such a target has the potential to remove important files from a user&#8217;s computer. Use with caution. </p>
<p> Since 1.7.0.</p>
<h3>ECMUseFindModules</h3>
<p>Selectively use some of the find modules provided by extra-cmake-modules. </p>
<p> This module is automatically available once extra-cmake-modules has been found, so it is not necessary to <code>include(ECMUseFindModules)</code> explicitly. </p>
<pre>ecm_use_find_modules(DIR &lt;dir&gt;
 MODULES module1.cmake [module2.cmake [...]]
 [NO_OVERRIDE])</pre>
<p>This allows selective use of the find modules provided by ECM, including deferring to CMake&#8217;s versions of those modules if it has them. Rather than adding <code>${ECM_FIND_MODULE_DIR}</code> to <code>CMAKE_MODULE_PATH</code>, you use ecm_use_find_modules() to copy the modules you want to a local (build) directory, and add that to <code>CMAKE_MODULE_PATH</code>. </p>
<p> The find modules given to MODULES will be copied to the directory given by DIR (which should be located in <code>${CMAKE_BINARY_DIR}</code> and added to <code>CMAKE_MODULE_PATH</code>). If NO_OVERRIDE is given, only modules not also provided by CMake will be copied. </p>
<p> Example: </p>
<pre>find_package(ECM REQUIRED)
ecm_use_find_modules(
 DIR ${CMAKE_BINARY_DIR}/cmake
 MODULES FindEGL.cmake
 NO_OVERRIDE
)
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/cmake)</pre>
<p>This example will make <code>FindEGL.cmake</code> available in your project, but only as long as it is not yet part of CMake. Calls to <code>find_package(EGL)</code> will then make use of this copied module (or the CMake module if it exists). </p>
<p> Another possible use for this macro is to take copies of find modules that can be installed along with config files if they are required as a dependency (for example, if targets provided by the find module are in the link interface of a library). </p>
<p> Since pre-1.0.0.</p>
<h2>Copyright</h2>
<p>KDE Developers</p>
