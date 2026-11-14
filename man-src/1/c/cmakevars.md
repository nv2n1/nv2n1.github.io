---
title: "cmakevars(1)"
name: "cmakevars"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmakevars/"
description: "cmakevars – Reference of CMake variables."
---

<h2>NAME</h2>
<p> cmakevars &#8211; Reference of CMake variables. </p>
<h2>VARIABLES THAT PROVIDE INFORMATION</h2>
<p> variables defined by cmake, that give information about the project, and cmake </p>
<dl>
<dt><code>CMAKE_AR</code></p>
<dd> Name of archiving tool for static libraries. </p>
<p> This specifies the name of the program that creates archive or static libraries. </p>
<dt><code>CMAKE_ARGC</code></p>
<dd> Number of command line arguments passed to CMake in script mode. </p>
<p> When run in -P script mode, CMake sets this variable to the number of command line arguments. See also CMAKE_ARGV0, 1, 2 &#8230; </p>
<dt><code>CMAKE_ARGV0</code></p>
<dd> Command line argument passed to CMake in script mode. </p>
<p> When run in -P script mode, CMake sets this variable to the first command line argument. It then also sets CMAKE_ARGV1, CMAKE_ARGV2, &#8230; and so on, up to the number of command line arguments given. See also CMAKE_ARGC. </p>
<dt><code>CMAKE_BINARY_DIR</code></p>
<dd> The path to the top level of the build tree. </p>
<p> This is the full path to the top level of the current CMake build tree. For an in-source build, this would be the same as CMAKE_SOURCE_DIR. </p>
<dt><code>CMAKE_BUILD_TOOL</code></p>
<dd> Tool used for the actual build process. </p>
<p> This variable is set to the program that will be needed to build the output of CMake. If the generator selected was Visual Studio 6, the CMAKE_BUILD_TOOL will be set to msdev, for Unix Makefiles it will be set to make or gmake, and for Visual Studio 7 it set to devenv. For NMake Makefiles the value is nmake. This can be useful for adding special flags and commands based on the final build environment. </p>
<dt><code>CMAKE_CACHEFILE_DIR</code></p>
<dd> The directory with the CMakeCache.txt file. </p>
<p> This is the full path to the directory that has the CMakeCache.txt file in it. This is the same as CMAKE_BINARY_DIR. </p>
<dt><code>CMAKE_CACHE_MAJOR_VERSION</code></p>
<dd> Major version of CMake used to create the CMakeCache.txt file </p>
<p> This stores the major version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CACHE_MINOR_VERSION</code></p>
<dd> Minor version of CMake used to create the CMakeCache.txt file </p>
<p> This stores the minor version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CACHE_PATCH_VERSION</code></p>
<dd> Patch version of CMake used to create the CMakeCache.txt file </p>
<p> This stores the patch version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CFG_INTDIR</code></p>
<dd> Build-time reference to per-configuration output subdirectory. </p>
<p> For native build systems supporting multiple configurations in the build tree (such as Visual Studio and Xcode), the value is a reference to a build-time variable specifying the name of the per-configuration output subdirectory. On Makefile generators this evaluates to &quot;.&quot; because there is only one configuration in a build tree. Example values: </p>
<pre>
  $(IntDir)        = Visual Studio 6
  $(OutDir)        = Visual Studio 7, 8, 9
  $(Configuration) = Visual Studio 10
  $(CONFIGURATION) = Xcode
  .                = Make-based tools
</pre>
<p> Since these values are evaluated by the native build system, this variable is suitable only for use in command lines that will be evaluated at build time. Example of intended usage: </p>
<pre><code>
add_executable(mytool mytool.c)
    add_custom_command(
        OUTPUT out.txt
            COMMAND ${CMAKE_CURRENT_BINARY_DIR} /
        ${CMAKE_CFG_INTDIR} / mytool ${CMAKE_CURRENT_SOURCE_DIR} / in.txt out.txt DEPENDS mytool in.txt)
        add_custom_target(drive ALL DEPENDS out.txt)
</code></pre>
<p> Note that CMAKE_CFG_INTDIR is no longer necessary for this purpose but has been left for compatibility with existing projects. Instead add_custom_command() recognizes executable target names in its COMMAND option, so &quot;${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool&quot; can be replaced by just &quot;mytool&quot;. </p>
<p> This variable is read-only. Setting it is undefined behavior. In multi-configuration build systems the value of this variable is passed as the value of preprocessor symbol &quot;CMAKE_INTDIR&quot; to the compilation of all source files. </p>
<dt><code>CMAKE_COMMAND</code></p>
<dd> The full path to the cmake executable. </p>
<p> This is the full path to the CMake executable cmake which is useful from custom commands that want to use the cmake -E option for portable system commands. (e.g. /usr/local/bin/cmake </p>
<dt><code>CMAKE_CROSSCOMPILING</code></p>
<dd> Is CMake currently cross compiling. </p>
<p> This variable will be set to true by CMake if CMake is cross compiling. Specifically if the build platform is different from the target platform. </p>
<dt><code>CMAKE_CTEST_COMMAND</code></p>
<dd> Full path to ctest command installed with cmake. </p>
<p> This is the full path to the CTest executable ctest which is useful from custom commands that want to use the cmake -E option for portable system commands. </p>
<dt><code>CMAKE_CURRENT_BINARY_DIR</code></p>
<dd> The path to the binary directory currently being processed. </p>
<p> This the full path to the build directory that is currently being processed by cmake. Each directory added by add_subdirectory will create a binary directory in the build tree, and as it is being processed this variable will be set. For in-source builds this is the current source directory being processed. </p>
<dt><code>CMAKE_CURRENT_LIST_DIR</code></p>
<dd> Full directory of the listfile currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the directory where the listfile which is currently being processed (CMAKE_CURRENT_LIST_FILE) is located. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the directory where this file is located. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the directory of the file invoking the bottom-most entry on the call stack, not the directory of the file containing the macro or function definition. </p>
<p> See also CMAKE_CURRENT_LIST_FILE. </p>
<dt><code>CMAKE_CURRENT_LIST_FILE</code></p>
<dd> Full path to the listfile currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the one currently being processed. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the location of the file. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the file invoking the bottom-most entry on the call stack, not the file containing the macro or function definition. </p>
<p> See also CMAKE_PARENT_LIST_FILE. </p>
<dt><code>CMAKE_CURRENT_LIST_LINE</code></p>
<dd> The line number of the current file being processed. </p>
<p> This is the line number of the file currently being processed by cmake. </p>
<dt><code>CMAKE_CURRENT_SOURCE_DIR</code></p>
<dd> The path to the source directory currently being processed. </p>
<p> This the full path to the source directory that is currently being processed by cmake. </p>
<dt><code>CMAKE_DL_LIBS</code></p>
<dd> Name of library containing dlopen and dlcose. </p>
<p> The name of the library that has dlopen and dlclose in it, usually -ldl on most UNIX machines. </p>
<dt><code>CMAKE_EDIT_COMMAND</code></p>
<dd> Full path to cmake-gui or ccmake. </p>
<p> This is the full path to the CMake executable that can graphically edit the cache. For example, cmake-gui, ccmake, or cmake -i. </p>
<dt><code>CMAKE_EXECUTABLE_SUFFIX</code></p>
<dd> The suffix for executables on this platform. </p>
<p> The suffix to use for the end of an executable filename if any, .exe on Windows. </p>
<p> CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_EXTRA_GENERATOR</code></p>
<dd> The extra generator used to build the project. </p>
<p> When using the Eclipse, CodeBlocks or KDevelop generators, CMake generates Makefiles (CMAKE_GENERATOR) and additionally project files for the respective IDE. This IDE project file generator is stored in CMAKE_EXTRA_GENERATOR (e.g. &quot;Eclipse CDT4&quot;). </p>
<dt><code>CMAKE_EXTRA_SHARED_LIBRARY_SUFFIXES</code></p>
<dd> Additional suffixes for shared libraries. </p>
<p> Extensions for shared libraries other than that specified by CMAKE_SHARED_LIBRARY_SUFFIX, if any. CMake uses this to recognize external shared library files during analysis of libraries linked by a target. </p>
<dt><code>CMAKE_GENERATOR</code></p>
<dd> The generator used to build the project. </p>
<p> The name of the generator that is being used to generate the build files. (e.g. &quot;Unix Makefiles&quot;, &quot;Visual Studio 6&quot;, etc.) </p>
<dt><code>CMAKE_GENERATOR_TOOLSET</code></p>
<dd> Native build system toolset name specified by user. </p>
<p> Some CMake generators support a toolset name to be given to the native build system to choose a compiler. If the user specifies a toolset name (e.g. via the cmake -T option) the value will be available in this variable. </p>
<dt><code>CMAKE_HOME_DIRECTORY</code></p>
<dd> Path to top of source tree. </p>
<p> This is the path to the top level of the source tree. </p>
<dt><code>CMAKE_IMPORT_LIBRARY_PREFIX</code></p>
<dd> The prefix for import libraries that you link to. </p>
<p> The prefix to use for the name of an import library if used on this platform. </p>
<p> CMAKE_IMPORT_LIBRARY_PREFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_IMPORT_LIBRARY_SUFFIX</code></p>
<dd> The suffix for import libraries that you link to. </p>
<p> The suffix to use for the end of an import library filename if used on this platform. </p>
<p> CMAKE_IMPORT_LIBRARY_SUFFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_LINK_LIBRARY_SUFFIX</code></p>
<dd> The suffix for libraries that you link to. </p>
<p> The suffix to use for the end of a library filename, .lib on Windows. </p>
<dt><code>CMAKE_MAJOR_VERSION</code></p>
<dd> The Major version of cmake (i.e. the 2 in 2.X.X) </p>
<p> This specifies the major version of the CMake executable being run. </p>
<dt><code>CMAKE_MAKE_PROGRAM</code></p>
<dd> See CMAKE_BUILD_TOOL. </p>
<p> This variable is around for backwards compatibility, see CMAKE_BUILD_TOOL. </p>
<dt><code>CMAKE_MINIMUM_REQUIRED_VERSION</code></p>
<dd> Version specified to cmake_minimum_required command </p>
<p> Variable containing the VERSION component specified in the cmake_minimum_required command. </p>
<dt><code>CMAKE_MINOR_VERSION</code></p>
<dd> The Minor version of cmake (i.e. the 4 in X.4.X). </p>
<p> This specifies the minor version of the CMake executable being run. </p>
<dt><code>CMAKE_PARENT_LIST_FILE</code></p>
<dd> Full path to the CMake file that included the current one. </p>
<p> While processing a CMake file loaded by include() or find_package() this variable contains the full path to the file including it. The top of the include stack is always the CMakeLists.txt for the current directory. See also CMAKE_CURRENT_LIST_FILE. </p>
<dt><code>CMAKE_PATCH_VERSION</code></p>
<dd> The patch version of cmake (i.e. the 3 in X.X.3). </p>
<p> This specifies the patch version of the CMake executable being run. </p>
<dt><code>CMAKE_PROJECT_NAME</code></p>
<dd> The name of the current project. </p>
<p> This specifies name of the current project from the closest inherited PROJECT command. </p>
<dt><code>CMAKE_RANLIB</code></p>
<dd> Name of randomizing tool for static libraries. </p>
<p> This specifies name of the program that randomizes libraries on UNIX, not used on Windows, but may be present. </p>
<dt><code>CMAKE_ROOT</code></p>
<dd> Install directory for running cmake. </p>
<p> This is the install root for the running CMake and the Modules directory can be found here. This is commonly used in this format: ${CMAKE_ROOT}/Modules </p>
<dt><code>CMAKE_SCRIPT_MODE_FILE</code></p>
<dd> Full path to the -P script file currently being processed. </p>
<p> When run in -P script mode, CMake sets this variable to the full path of the script file. When run to configure a CMakeLists.txt file, this variable is not set. </p>
<dt><code>CMAKE_SHARED_LIBRARY_PREFIX</code></p>
<dd> The prefix for shared libraries that you link to. </p>
<p> The prefix to use for the name of a shared library, lib on UNIX. </p>
<p> CMAKE_SHARED_LIBRARY_PREFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_SHARED_LIBRARY_SUFFIX</code></p>
<dd> The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a shared library filename, .dll on Windows. </p>
<p> CMAKE_SHARED_LIBRARY_SUFFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_SHARED_MODULE_PREFIX</code></p>
<dd> The prefix for loadable modules that you link to. </p>
<p> The prefix to use for the name of a loadable module on this platform. </p>
<p> CMAKE_SHARED_MODULE_PREFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_SHARED_MODULE_SUFFIX</code></p>
<dd> The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a loadable module filename on this platform </p>
<p> CMAKE_SHARED_MODULE_SUFFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_SIZEOF_VOID_P</code></p>
<dd> Size of a void pointer. </p>
<p> This is set to the size of a pointer on the machine, and is determined by a try compile. If a 64 bit size is found, then the library search path is modified to look for 64 bit libraries first. </p>
<dt><code>CMAKE_SKIP_RPATH</code></p>
<dd> If true, do not add run time path information. </p>
<p> If this is set to TRUE, then the rpath information is not added to compiled executables. The default is to add rpath information if the platform supports it. This allows for easy running from the build tree. To omit RPATH in the install step, but not the build step, use CMAKE_SKIP_INSTALL_RPATH instead. </p>
<dt><code>CMAKE_SOURCE_DIR</code></p>
<dd> The path to the top level of the source tree. </p>
<p> This is the full path to the top level of the current CMake source tree. For an in-source build, this would be the same as CMAKE_BINARY_DIR. </p>
<dt><code>CMAKE_STANDARD_LIBRARIES</code></p>
<dd> Libraries linked into every executable and shared library. </p>
<p> This is the list of libraries that are linked into all executables and libraries. </p>
<dt><code>CMAKE_STATIC_LIBRARY_PREFIX</code></p>
<dd> The prefix for static libraries that you link to. </p>
<p> The prefix to use for the name of a static library, lib on UNIX. </p>
<p> CMAKE_STATIC_LIBRARY_PREFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_STATIC_LIBRARY_SUFFIX</code></p>
<dd> The suffix for static libraries that you link to. </p>
<p> The suffix to use for the end of a static library filename, .lib on Windows. </p>
<p> CMAKE_STATIC_LIBRARY_SUFFIX_&lt;LANG&gt; overrides this for language &lt;LANG&gt;. </p>
<dt><code>CMAKE_TWEAK_VERSION</code></p>
<dd> The tweak version of cmake (i.e. the 1 in X.X.X.1). </p>
<p> This specifies the tweak version of the CMake executable being run. Releases use tweak &lt; 20000000 and development versions use the date format CCYYMMDD for the tweak level. </p>
<dt><code>CMAKE_VERBOSE_MAKEFILE</code></p>
<dd> Create verbose makefiles if on. </p>
<p> This variable defaults to false. You can set this variable to true to make CMake produce verbose makefiles that show each command line as it is used. </p>
<dt><code>CMAKE_VERSION</code></p>
<dd> The full version of cmake in major.minor.patch[.tweak[-id]] format. </p>
<p> This specifies the full version of the CMake executable being run. This variable is defined by versions 2.6.3 and higher. See variables CMAKE_MAJOR_VERSION, CMAKE_MINOR_VERSION, CMAKE_PATCH_VERSION, and CMAKE_TWEAK_VERSION for individual version components. The [-id] component appears in non-release versions and may be arbitrary text. </p>
<dt><code>CMAKE_VS_PLATFORM_TOOLSET</code></p>
<dd> Visual Studio Platform Toolset name. </p>
<p> VS 10 and above use MSBuild under the hood and support multiple compiler toolchains. CMake may specify a toolset explicitly, such as &quot;v110&quot; for VS 11 or &quot;Windows7.1SDK&quot; for 64-bit support in VS 10 Express. CMake provides the name of the chosen toolset in this variable. </p>
<dt><code>CMAKE_XCODE_PLATFORM_TOOLSET</code></p>
<dd> Xcode compiler selection. </p>
<p> Xcode supports selection of a compiler from one of the installed toolsets. CMake provides the name of the chosen toolset in this variable, if any is explicitly selected (e.g. via the cmake -T option). </p>
<dt><code>PROJECT_BINARY_DIR</code></p>
<dd> Full path to build directory for project. </p>
<p> This is the binary directory of the most recent PROJECT command. </p>
<dt><code>PROJECT_NAME</code></p>
<dd> Name of the project given to the project command. </p>
<p> This is the name given to the most recent PROJECT command. </p>
<dt><code>PROJECT_SOURCE_DIR</code></p>
<dd> Top level source directory for the current project. </p>
<p> This is the source directory of the most recent PROJECT command. </p>
<dt><code>[Project name]_BINARY_DIR</code></p>
<dd> Top level binary directory for the named project. </p>
<p> A variable is created with the name used in the PROJECT command, and is the binary directory for the project. This can be useful when SUBDIR is used to connect several projects. </p>
<dt><code>[Project name]_SOURCE_DIR</code></p>
<dd> Top level source directory for the named project. </p>
<p> A variable is created with the name used in the PROJECT command, and is the source directory for the project. This can be useful when add_subdirectory is used to connect several projects. </p>
</dl>
<h2>VARIABLES THAT CHANGE BEHAVIOR</h2>
<dl>
<dt><code>BUILD_SHARED_LIBS</code></p>
<dd> Global flag to cause add_library to create shared libraries if on. </p>
<p> If present and true, this will cause all libraries to be built shared unless the library was explicitly added as a static library. This variable is often added to projects as an OPTION so that each user of a project can decide if they want to build the project using shared or static libraries. </p>
<dt><code>CMAKE_ABSOLUTE_DESTINATION_FILES</code></p>
<dd> List of files which have been installed using an ABSOLUTE DESTINATION path. </p>
<p> This variable is defined by CMake-generated cmake_install.cmake scripts. It can be used (read-only) by programs or scripts that source those install scripts. This is used by some CPack generators (e.g. RPM). </p>
<dt><code>CMAKE_AUTOMOC_RELAXED_MODE</code></p>
<dd> Switch between strict and relaxed automoc mode. </p>
<p> By default, automoc behaves exactly as described in the documentation of the AUTOMOC target property. When set to TRUE, it accepts more input and tries to find the correct input file for moc even if it differs from the documented behaviour. In this mode it e.g. also checks whether a header file is intended to be processed by moc when a &quot;foo.moc&quot; file has been included. </p>
<p> Relaxed mode has to be enabled for KDE4 compatibility. </p>
<dt><code>CMAKE_BACKWARDS_COMPATIBILITY</code></p>
<dd> Version of cmake required to build project </p>
<p> From the point of view of backwards compatibility, this specifies what version of CMake should be supported. By default this value is the version number of CMake that you are running. You can set this to an older version of CMake to support deprecated commands of CMake in projects that were written to use older versions of CMake. This can be set by the user or set at the beginning of a CMakeLists file. </p>
<dt><code>CMAKE_BUILD_TYPE</code></p>
<dd> Specifies the build type on single-configuration generators. </p>
<p> This statically specifies what build type (configuration) will be built in this build tree. Possible values are empty, Debug, Release, RelWithDebInfo and MinSizeRel. This variable is only meaningful to single-configuration generators (such as make and Ninja) i.e. those which choose a single configuration when CMake runs to generate a build tree as opposed to multi-configuration generators which offer selection of the build configuration within the generated build environment. There are many per-config properties and variables (usually following clean SOME_VAR_&lt;CONFIG&gt; order conventions), such as CMAKE_C_FLAGS_&lt;CONFIG&gt;, specified as uppercase: CMAKE_C_FLAGS_[DEBUG|RELEASE|RELWITHDEBINFO|MINSIZEREL]. For example, in a build tree configured to build type Debug, CMake will see to having CMAKE_C_FLAGS_DEBUG settings get added to the CMAKE_C_FLAGS settings. See also CMAKE_CONFIGURATION_TYPES. </p>
<dt><code>CMAKE_COLOR_MAKEFILE</code></p>
<dd> Enables color output when using the Makefile generator. </p>
<p> When enabled, the generated Makefiles will produce colored output. Default is ON. </p>
<dt><code>CMAKE_CONFIGURATION_TYPES</code></p>
<dd> Specifies the available build types on multi-config generators. </p>
<p> This specifies what build types (configurations) will be available such as Debug, Release, RelWithDebInfo etc. This has reasonable defaults on most platforms, but can be extended to provide other build types. See also CMAKE_BUILD_TYPE for details of managing configuration data, and CMAKE_CFG_INTDIR. </p>
<dt><code>CMAKE_DEBUG_TARGET_PROPERTIES</code></p>
<dd> Enables tracing output for target properties. </p>
<p> This variable can be populated with a list of properties to generate debug output for when evaluating target properties. Currently it can only be used when evaluating the INCLUDE_DIRECTORIES, COMPILE_DEFINITIONS and COMPILE_OPTIONS target properties. In that case, it outputs a backtrace for each entry in the target property. Default is unset. </p>
<dt><code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code></p>
<dd> Variable for disabling find_package() calls. </p>
<p> Every non-REQUIRED find_package() call in a project can be disabled by setting the variable CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt; to TRUE. This can be used to build a project without an optional package, although that package is installed. </p>
<p> This switch should be used during the initial CMake run. Otherwise if the package has already been found in a previous CMake run, the variables which have been stored in the cache will still be there. In that case it is recommended to remove the cache variables for this package from the cache using the cache editor or cmake -U </p>
<dt><code>CMAKE_ERROR_DEPRECATED</code></p>
<dd> Whether to issue deprecation errors for macros and functions. </p>
<p> If TRUE, this can be used by macros and functions to issue fatal errors when deprecated macros or functions are used. This variable is FALSE by default. </p>
<dt><code>CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</code></p>
<dd> Ask cmake_install.cmake script to error out as soon as a file with absolute INSTALL DESTINATION is encountered. </p>
<p> The fatal error is emitted before the installation of the offending file takes place. This variable is used by CMake-generated cmake_install.cmake scripts. If one sets this variable to ON while running the script, it may get fatal error messages from the script. </p>
<dt><code>CMAKE_FIND_LIBRARY_PREFIXES</code></p>
<dd> Prefixes to prepend when looking for libraries. </p>
<p> This specifies what prefixes to add to library names when the find_library command looks for libraries. On UNIX systems this is typically lib, meaning that when trying to find the foo library it will look for libfoo. </p>
<dt><code>CMAKE_FIND_LIBRARY_SUFFIXES</code></p>
<dd> Suffixes to append when looking for libraries. </p>
<p> This specifies what suffixes to add to library names when the find_library command looks for libraries. On Windows systems this is typically .lib and .dll, meaning that when trying to find the foo library it will look for foo.dll etc. </p>
<dt><code>CMAKE_FIND_PACKAGE_WARN_NO_MODULE</code></p>
<dd> Tell find_package to warn if called without an explicit mode. </p>
<p> If find_package is called without an explicit mode option (MODULE, CONFIG or NO_MODULE) and no Find&lt;pkg&gt;.cmake module is in CMAKE_MODULE_PATH then CMake implicitly assumes that the caller intends to search for a package configuration file. If no package configuration file is found then the wording of the failure message must account for both the case that the package is really missing and the case that the project has a bug and failed to provide the intended Find module. If instead the caller specifies an explicit mode option then the failure message can be more specific. </p>
<p> Set CMAKE_FIND_PACKAGE_WARN_NO_MODULE to TRUE to tell find_package to warn when it implicitly assumes Config mode. This helps developers enforce use of an explicit mode in all calls to find_package within a project. </p>
<dt><code>CMAKE_IGNORE_PATH</code></p>
<dd> Path to be ignored by FIND_XXX() commands. </p>
<p> Specifies directories to be ignored by searches in FIND_XXX() commands. This is useful in cross-compiled environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine that modules like FindX11 (and others) would normally search. By default this is empty; it is intended to be set by the project. Note that CMAKE_IGNORE_PATH takes a list of directory names, NOT a list of prefixes. If you want to ignore paths under prefixes (bin, include, lib, etc.), you&#8217;ll need to specify them explicitly. See also CMAKE_PREFIX_PATH, CMAKE_LIBRARY_PATH, CMAKE_INCLUDE_PATH, CMAKE_PROGRAM_PATH. </p>
<dt><code>CMAKE_INCLUDE_PATH</code></p>
<dd> Path used for searching by FIND_FILE() and FIND_PATH(). </p>
<p> Specifies a path which will be used both by FIND_FILE() and FIND_PATH(). Both commands will check each of the contained directories for the existence of the file which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_INCLUDE_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_INSTALL_DEFAULT_COMPONENT_NAME</code></p>
<dd> Default component used in install() commands. </p>
<p> If an install() command is used without the COMPONENT argument, these files will be grouped into a default component. The name of this default install component will be taken from this variable. It defaults to &quot;Unspecified&quot;. </p>
<dt><code>CMAKE_INSTALL_PREFIX</code></p>
<dd> Install directory used by install. </p>
<p> If &quot;make install&quot; is invoked or INSTALL is built, this directory is prepended onto all install directories. This variable defaults to /usr/local on UNIX and c:/Program Files on Windows. </p>
<p> On UNIX one can use the DESTDIR mechanism in order to relocate the whole installation. DESTDIR means DESTination DIRectory. It is commonly used by makefile users in order to install software at non-default location. It is usually invoked like this: </p>
<pre>
 make DESTDIR=/home/john install
</pre>
<p> which will install the concerned software using the installation prefix, e.g. &quot;/usr/local&quot; prepended with the DESTDIR value which finally gives &quot;/home/john/usr/local&quot;. </p>
<p> WARNING: DESTDIR may not be used on Windows because installation prefix usually contains a drive letter like in &quot;C:/Program Files&quot; which cannot be prepended with some other prefix. </p>
<p> The installation prefix is also added to CMAKE_SYSTEM_PREFIX_PATH so that find_package, find_program, find_library, find_path, and find_file will search the prefix for other software. </p>
<dt><code>CMAKE_LIBRARY_PATH</code></p>
<dd> Path used for searching by FIND_LIBRARY(). </p>
<p> Specifies a path which will be used by FIND_LIBRARY(). FIND_LIBRARY() will check each of the contained directories for the existence of the library which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_MFC_FLAG</code></p>
<dd> Tell cmake to use MFC for an executable or dll. </p>
<p> This can be set in a CMakeLists.txt file and will enable MFC in the application. It should be set to 1 for the static MFC library, and 2 for the shared MFC library. This is used in Visual Studio 6 and 7 project files. The CMakeSetup dialog used MFC and the CMakeLists.txt looks like this: </p>
<pre>
  add_definitions(-D_AFXDLL)
  set(CMAKE_MFC_FLAG 2)
  add_executable(CMakeSetup WIN32 ${SRCS})
</pre>
<dt><code>CMAKE_MODULE_PATH</code></p>
<dd> List of directories to search for CMake modules. </p>
<p> Commands like include() and find_package() search for files in directories listed by this variable before checking the default modules that come with CMake. </p>
<dt><code>CMAKE_NOT_USING_CONFIG_FLAGS</code></p>
<dd> Skip _BUILD_TYPE flags if true. </p>
<p> This is an internal flag used by the generators in CMake to tell CMake to skip the _BUILD_TYPE flags. </p>
<dt><code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code></p>
<dd> Default for CMake Policy CMP&lt;NNNN&gt; when it is otherwise left unset. </p>
<p> Commands cmake_minimum_required(VERSION) and cmake_policy(VERSION) by default leave policies introduced after the given version unset. Set CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt; to OLD or NEW to specify the default for policy CMP&lt;NNNN&gt;, where &lt;NNNN&gt; is the policy number. </p>
<p> This variable should not be set by a project in CMake code; use cmake_policy(SET) instead. Users running CMake may set this variable in the cache (e.g. -DCMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;=&lt;OLD|NEW&gt;) to set a policy not otherwise set by the project. Set to OLD to quiet a policy warning while using old behavior or to NEW to try building the project with new behavior. </p>
<dt><code>CMAKE_PREFIX_PATH</code></p>
<dd> Path used for searching by FIND_XXX(), with appropriate suffixes added. </p>
<p> Specifies a path which will be used by the FIND_XXX() commands. It contains the &quot;base&quot; directories, the FIND_XXX() commands append appropriate subdirectories to the base directories. So FIND_PROGRAM() adds /bin to each of the directories in the path, FIND_LIBRARY() appends /lib to each of the directories, and FIND_PATH() and FIND_FILE() append /include . By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_PREFIX_PATH, CMAKE_INCLUDE_PATH, CMAKE_LIBRARY_PATH, CMAKE_PROGRAM_PATH. </p>
<dt><code>CMAKE_PROGRAM_PATH</code></p>
<dd> Path used for searching by FIND_PROGRAM(). </p>
<p> Specifies a path which will be used by FIND_PROGRAM(). FIND_PROGRAM() will check each of the contained directories for the existence of the program which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_PROGRAM_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_SKIP_INSTALL_ALL_DEPENDENCY</code></p>
<dd> Don&#8217;t make the install target depend on the all target. </p>
<p> By default, the &quot;install&quot; target depends on the &quot;all&quot; target. This has the effect, that when &quot;make install&quot; is invoked or INSTALL is built, first the &quot;all&quot; target is built, then the installation starts. If CMAKE_SKIP_INSTALL_ALL_DEPENDENCY is set to TRUE, this dependency is not created, so the installation process will start immediately, independent from whether the project has been completely built or not. </p>
<dt><code>CMAKE_SYSTEM_IGNORE_PATH</code></p>
<dd> Path to be ignored by FIND_XXX() commands. </p>
<p> Specifies directories to be ignored by searches in FIND_XXX() commands. This is useful in cross-compiled environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine that modules like FindX11 (and others) would normally search. By default this contains a list of directories containing incompatible binaries for the host system. See also CMAKE_SYSTEM_PREFIX_PATH, CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_SYSTEM_INCLUDE_PATH, and CMAKE_SYSTEM_PROGRAM_PATH. </p>
<dt><code>CMAKE_SYSTEM_INCLUDE_PATH</code></p>
<dd> Path used for searching by FIND_FILE() and FIND_PATH(). </p>
<p> Specifies a path which will be used both by FIND_FILE() and FIND_PATH(). Both commands will check each of the contained directories for the existence of the file which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_INCLUDE_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_SYSTEM_LIBRARY_PATH</code></p>
<dd> Path used for searching by FIND_LIBRARY(). </p>
<p> Specifies a path which will be used by FIND_LIBRARY(). FIND_LIBRARY() will check each of the contained directories for the existence of the library which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_LIBRARY_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dd> Path used for searching by FIND_XXX(), with appropriate suffixes added. </p>
<p> Specifies a path which will be used by the FIND_XXX() commands. It contains the &quot;base&quot; directories, the FIND_XXX() commands append appropriate subdirectories to the base directories. So FIND_PROGRAM() adds /bin to each of the directories in the path, FIND_LIBRARY() appends /lib to each of the directories, and FIND_PATH() and FIND_FILE() append /include . By default this contains the standard directories for the current system and the CMAKE_INSTALL_PREFIX. It is NOT intended to be modified by the project, use CMAKE_PREFIX_PATH for this. See also CMAKE_SYSTEM_INCLUDE_PATH, CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_SYSTEM_PROGRAM_PATH, and CMAKE_SYSTEM_IGNORE_PATH. </p>
<dt><code>CMAKE_SYSTEM_PROGRAM_PATH</code></p>
<dd> Path used for searching by FIND_PROGRAM(). </p>
<p> Specifies a path which will be used by FIND_PROGRAM(). FIND_PROGRAM() will check each of the contained directories for the existence of the program which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_PROGRAM_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_USER_MAKE_RULES_OVERRIDE</code></p>
<dd> Specify a CMake file that overrides platform information. </p>
<p> CMake loads the specified file while enabling support for each language from either the project() or enable_language() commands. It is loaded after CMake&#8217;s builtin compiler and platform information modules have been loaded but before the information is used. The file may set platform information variables to override CMake&#8217;s defaults. </p>
<p> This feature is intended for use only in overriding information variables that must be set before CMake builds its first test project to check that the compiler for a language works. It should not be used to load a file in cases that a normal include() will work. Use it only as a last resort for behavior that cannot be achieved any other way. For example, one may set CMAKE_C_FLAGS_INIT to change the default value used to initialize CMAKE_C_FLAGS before it is cached. The override file should NOT be used to set anything that could be set after languages are enabled, such as variables like CMAKE_RUNTIME_OUTPUT_DIRECTORY that affect the placement of binaries. Information set in the file will be used for try_compile and try_run builds too. </p>
<dt><code>CMAKE_WARN_DEPRECATED</code></p>
<dd> Whether to issue deprecation warnings for macros and functions. </p>
<p> If TRUE, this can be used by macros and functions to issue deprecation warnings. This variable is FALSE by default. </p>
<dt><code>CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</code></p>
<dd> Ask cmake_install.cmake script to warn each time a file with absolute INSTALL DESTINATION is encountered. </p>
<p> This variable is used by CMake-generated cmake_install.cmake scripts. If one sets this variable to ON while running the script, it may get warning messages from the script. </p>
</dl>
<h2>VARIABLES THAT DESCRIBE THE SYSTEM</h2>
<dl>
<dt><code>APPLE</code></p>
<dd> True if running on Mac OS X. </p>
<p> Set to true on Mac OS X. </p>
<dt><code>BORLAND</code></p>
<dd> True if the Borland compiler is being used. </p>
<p> This is set to true if the Borland compiler is being used. </p>
<dt><code>CMAKE_CL_64</code></p>
<dd> Using the 64 bit compiler from Microsoft </p>
<p> Set to true when using the 64 bit cl compiler from Microsoft. </p>
<dt><code>CMAKE_COMPILER_2005</code></p>
<dd> Using the Visual Studio 2005 compiler from Microsoft </p>
<p> Set to true when using the Visual Studio 2005 compiler from Microsoft. </p>
<dt><code>CMAKE_HOST_APPLE</code></p>
<dd> True for Apple OS X operating systems. </p>
<p> Set to true when the host system is Apple OS X. </p>
<dt><code>CMAKE_HOST_SYSTEM</code></p>
<dd> Name of system cmake is being run on. </p>
<p> The same as CMAKE_SYSTEM but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_NAME</code></p>
<dd> Name of the OS CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_NAME but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_PROCESSOR</code></p>
<dd> The name of the CPU CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_PROCESSOR but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_VERSION</code></p>
<dd> OS version CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_VERSION but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_UNIX</code></p>
<dd> True for UNIX and UNIX like operating systems. </p>
<p> Set to true when the host system is UNIX or UNIX like (i.e. APPLE and CYGWIN). </p>
<dt><code>CMAKE_HOST_WIN32</code></p>
<dd> True on windows systems, including win64. </p>
<p> Set to true when the host system is Windows and on Cygwin. </p>
<dt><code>CMAKE_LIBRARY_ARCHITECTURE</code></p>
<dd> Target architecture library directory name, if detected. </p>
<p> This is the value of CMAKE_&lt;lang&gt;_LIBRARY_ARCHITECTURE as detected for one of the enabled languages. </p>
<dt><code>CMAKE_LIBRARY_ARCHITECTURE_REGEX</code></p>
<dd> Regex matching possible target architecture library directory names. </p>
<p> This is used to detect CMAKE_&lt;lang&gt;_LIBRARY_ARCHITECTURE from the implicit linker search path by matching the &lt;arch&gt; name. </p>
<dt><code>CMAKE_OBJECT_PATH_MAX</code></p>
<dd> Maximum object file full-path length allowed by native build tools. </p>
<p> CMake computes for every source file an object file name that is unique to the source file and deterministic with respect to the full path to the source file. This allows multiple source files in a target to share the same name if they lie in different directories without rebuilding when one is added or removed. However, it can produce long full paths in a few cases, so CMake shortens the path using a hashing scheme when the full path to an object file exceeds a limit. CMake has a built-in limit for each platform that is sufficient for common tools, but some native tools may have a lower limit. This variable may be set to specify the limit explicitly. The value must be an integer no less than 128. </p>
<dt><code>CMAKE_SYSTEM</code></p>
<dd> Name of system cmake is compiling for. </p>
<p> This variable is the composite of CMAKE_SYSTEM_NAME and CMAKE_SYSTEM_VERSION, like this ${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_VERSION}. If CMAKE_SYSTEM_VERSION is not set, then CMAKE_SYSTEM is the same as CMAKE_SYSTEM_NAME. </p>
<dt><code>CMAKE_SYSTEM_NAME</code></p>
<dd> Name of the OS CMake is building for. </p>
<p> This is the name of the operating system on which CMake is targeting. On systems that have the uname command, this variable is set to the output of uname -s. Linux, Windows, and Darwin for Mac OS X are the values found on the big three operating systems. </p>
<dt><code>CMAKE_SYSTEM_PROCESSOR</code></p>
<dd> The name of the CPU CMake is building for. </p>
<p> On systems that support uname, this variable is set to the output of uname -p, on windows it is set to the value of the environment variable PROCESSOR_ARCHITECTURE </p>
<dt><code>CMAKE_SYSTEM_VERSION</code></p>
<dd> OS version CMake is building for. </p>
<p> A numeric version string for the system, on systems that support uname, this variable is set to the output of uname -r. On other systems this is set to major-minor version numbers. </p>
<dt><code>CYGWIN</code></p>
<dd> True for Cygwin. </p>
<p> Set to true when using Cygwin. </p>
<dt><code>ENV</code></p>
<dd> Access environment variables. </p>
<p> Use the syntax $ENV{VAR} to read environment variable VAR. See also the set() command to set ENV{VAR}. </p>
<dt><code>MSVC</code></p>
<dd> True when using Microsoft Visual C </p>
<p> Set to true when the compiler is some version of Microsoft Visual C. </p>
<dt><code>MSVC10</code></p>
<dd> True when using Microsoft Visual C 10.0 </p>
<p> Set to true when the compiler is version 10.0 of Microsoft Visual C. </p>
<dt><code>MSVC11</code></p>
<dd> True when using Microsoft Visual C 11.0 </p>
<p> Set to true when the compiler is version 11.0 of Microsoft Visual C. </p>
<dt><code>MSVC12</code></p>
<dd> True when using Microsoft Visual C 12.0 </p>
<p> Set to true when the compiler is version 12.0 of Microsoft Visual C. </p>
<dt><code>MSVC60</code></p>
<dd> True when using Microsoft Visual C 6.0 </p>
<p> Set to true when the compiler is version 6.0 of Microsoft Visual C. </p>
<dt><code>MSVC70</code></p>
<dd> True when using Microsoft Visual C 7.0 </p>
<p> Set to true when the compiler is version 7.0 of Microsoft Visual C. </p>
<dt><code>MSVC71</code></p>
<dd> True when using Microsoft Visual C 7.1 </p>
<p> Set to true when the compiler is version 7.1 of Microsoft Visual C. </p>
<dt><code>MSVC80</code></p>
<dd> True when using Microsoft Visual C 8.0 </p>
<p> Set to true when the compiler is version 8.0 of Microsoft Visual C. </p>
<dt><code>MSVC90</code></p>
<dd> True when using Microsoft Visual C 9.0 </p>
<p> Set to true when the compiler is version 9.0 of Microsoft Visual C. </p>
<dt><code>MSVC_IDE</code></p>
<dd> True when using the Microsoft Visual C IDE </p>
<p> Set to true when the target platform is the Microsoft Visual C IDE, as opposed to the command line compiler. </p>
<dt><code>MSVC_VERSION</code></p>
<dd> The version of Microsoft Visual C/C++ being used if any. </p>
<p> Known version numbers are: </p>
<pre>
  1200 = VS  6.0
  1300 = VS  7.0
  1310 = VS  7.1
  1400 = VS  8.0
  1500 = VS  9.0
  1600 = VS 10.0
  1700 = VS 11.0
  1800 = VS 12.0
</pre>
<dt><code>UNIX</code></p>
<dd> True for UNIX and UNIX like operating systems. </p>
<p> Set to true when the target system is UNIX or UNIX like (i.e. APPLE and CYGWIN). </p>
<dt><code>WIN32</code></p>
<dd> True on windows systems, including win64. </p>
<p> Set to true when the target system is Windows. </p>
<dt><code>XCODE_VERSION</code></p>
<dd> Version of Xcode (Xcode generator only). </p>
<p> Under the Xcode generator, this is the version of Xcode as specified in &quot;Xcode.app/Contents/version.plist&quot; (such as &quot;3.1.2&quot;). </p>
</dl>
<h2>VARIABLES THAT CONTROL THE BUILD</h2>
<dl>
<dt><code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code></p>
<dd> Default filename postfix for libraries under configuration &lt;CONFIG&gt;. </p>
<p> When a non-executable target is created its &lt;CONFIG&gt;_POSTFIX target property is initialized with the value of this variable if it is set. </p>
<dt><code>CMAKE_&lt;LANG&gt;_VISIBILITY_PRESET</code></p>
<dd> Default value for &lt;LANG&gt;_VISIBILITY_PRESET of targets. </p>
<p> This variable is used to initialize the &lt;LANG&gt;_VISIBILITY_PRESET property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_ARCHIVE_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the ARCHIVE targets when built. </p>
<p> This variable is used to initialize the ARCHIVE_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_AUTOMOC</code></p>
<dd> Whether to handle moc automatically for Qt targets. </p>
<p> This variable is used to initialize the AUTOMOC property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_AUTOMOC_MOC_OPTIONS</code></p>
<dd> Additional options for moc when using automoc (see CMAKE_AUTOMOC). </p>
<p> This variable is used to initialize the AUTOMOC_MOC_OPTIONS property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_BUILD_WITH_INSTALL_RPATH</code></p>
<dd> Use the install path for the RPATH </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with the install path for the RPATH and does not need to be relinked when installed. </p>
<dt><code>CMAKE_DEBUG_POSTFIX</code></p>
<dd> See variable CMAKE_&lt;CONFIG&gt;_POSTFIX. </p>
<p> This variable is a special case of the more-general CMAKE_&lt;CONFIG&gt;_POSTFIX variable for the DEBUG configuration. </p>
<dt><code>CMAKE_EXE_LINKER_FLAGS</code></p>
<dd> Linker flags to be used to create executables. </p>
<p> These flags will be used by the linker when creating an executable. </p>
<dt><code>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;</code></p>
<dd> Flags to be used when linking an executable. </p>
<p> Same as CMAKE_C_FLAGS_* but used by the linker when creating executables. </p>
<dt><code>CMAKE_Fortran_FORMAT</code></p>
<dd> Set to FIXED or FREE to indicate the Fortran source layout. </p>
<p> This variable is used to initialize the Fortran_FORMAT property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_Fortran_MODULE_DIRECTORY</code></p>
<dd> Fortran module output directory. </p>
<p> This variable is used to initialize the Fortran_MODULE_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_GNUtoMS</code></p>
<dd> Convert GNU import libraries (.dll.a) to MS format (.lib). </p>
<p> This variable is used to initialize the GNUtoMS property on targets when they are created. See that target property for additional information. </p>
<dt><code>CMAKE_INCLUDE_CURRENT_DIR</code></p>
<dd> Automatically add the current source- and build directories to the include path. </p>
<p> If this variable is enabled, CMake automatically adds in each directory ${CMAKE_CURRENT_SOURCE_DIR} and ${CMAKE_CURRENT_BINARY_DIR} to the include path for this directory. These additional include directories do not propagate down to subdirectories. This is useful mainly for out-of-source builds, where files generated into the build tree are included by files located in the source tree. </p>
<p> By default CMAKE_INCLUDE_CURRENT_DIR is OFF. </p>
<dt><code>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</code></p>
<dd> Automatically add the current source- and build directories to the INTERFACE_INCLUDE_DIRECTORIES. </p>
<p> If this variable is enabled, CMake automatically adds for each shared library target, static library target, module target and executable target, ${CMAKE_CURRENT_SOURCE_DIR} and ${CMAKE_CURRENT_BINARY_DIR} to the INTERFACE_INCLUDE_DIRECTORIES.By default CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE is OFF. </p>
<dt><code>CMAKE_INSTALL_NAME_DIR</code></p>
<dd> Mac OS X directory name for installed targets. </p>
<p> CMAKE_INSTALL_NAME_DIR is used to initialize the INSTALL_NAME_DIR property on all targets. See that target property for more information. </p>
<dt><code>CMAKE_INSTALL_RPATH</code></p>
<dd> The rpath to use for installed targets. </p>
<p> A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This is used to initialize the target property INSTALL_RPATH for all targets. </p>
<dt><code>CMAKE_INSTALL_RPATH_USE_LINK_PATH</code></p>
<dd> Add paths to linker search and installed rpath. </p>
<p> CMAKE_INSTALL_RPATH_USE_LINK_PATH is a boolean that if set to true will append directories in the linker search path and outside the project to the INSTALL_RPATH. This is used to initialize the target property INSTALL_RPATH_USE_LINK_PATH for all targets. </p>
<dt><code>CMAKE_LIBRARY_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the LIBRARY targets when built. </p>
<p> This variable is used to initialize the LIBRARY_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_LIBRARY_PATH_FLAG</code></p>
<dd> The flag to be used to add a library search path to a compiler. </p>
<p> The flag will be used to specify a library directory to the compiler. On most compilers this is &quot;-L&quot;. </p>
<dt><code>CMAKE_LINK_DEF_FILE_FLAG </code></p>
<dd> Linker flag to be used to specify a .def file for dll creation. </p>
<p> The flag will be used to add a .def file when creating a dll on Windows; this is only defined on Windows. </p>
<dt><code>CMAKE_LINK_DEPENDS_NO_SHARED</code></p>
<dd> Whether to skip link dependencies on shared library files. </p>
<p> This variable initializes the LINK_DEPENDS_NO_SHARED property on targets when they are created. See that target property for additional information. </p>
<dt><code>CMAKE_LINK_INTERFACE_LIBRARIES</code></p>
<dd> Default value for LINK_INTERFACE_LIBRARIES of targets. </p>
<p> This variable is used to initialize the LINK_INTERFACE_LIBRARIES property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_LINK_LIBRARY_FILE_FLAG</code></p>
<dd> Flag to be used to link a library specified by a path to its file. </p>
<p> The flag will be used before a library file path is given to the linker. This is needed only on very few platforms. </p>
<dt><code>CMAKE_LINK_LIBRARY_FLAG</code></p>
<dd> Flag to be used to link a library into an executable. </p>
<p> The flag will be used to specify a library to link to an executable. On most compilers this is &quot;-l&quot;. </p>
<dt><code>CMAKE_MACOSX_BUNDLE</code></p>
<dd> Default value for MACOSX_BUNDLE of targets. </p>
<p> This variable is used to initialize the MACOSX_BUNDLE property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_MODULE_LINKER_FLAGS</code></p>
<dd> Linker flags to be used to create modules. </p>
<p> These flags will be used by the linker when creating a module. </p>
<dt><code>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;</code></p>
<dd> Flags to be used when linking a module. </p>
<p> Same as CMAKE_C_FLAGS_* but used by the linker when creating modules. </p>
<dt><code>CMAKE_NO_BUILTIN_CHRPATH</code></p>
<dd> Do not use the builtin ELF editor to fix RPATHs on installation. </p>
<p> When an ELF binary needs to have a different RPATH after installation than it does in the build tree, CMake uses a builtin editor to change the RPATH in the installed copy. If this variable is set to true then CMake will relink the binary before installation instead of using its builtin editor. </p>
<dt><code>CMAKE_PDB_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the MS debug symbol files from linker. </p>
<p> This variable is used to initialize the PDB_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_POSITION_INDEPENDENT_CODE</code></p>
<dd> Default value for POSITION_INDEPENDENT_CODE of targets. </p>
<p> This variable is used to initialize the POSITION_INDEPENDENT_CODE property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_RUNTIME_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the RUNTIME targets when built. </p>
<p> This variable is used to initialize the RUNTIME_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_SHARED_LINKER_FLAGS</code></p>
<dd> Linker flags to be used to create shared libraries. </p>
<p> These flags will be used by the linker when creating a shared library. </p>
<dt><code>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;</code></p>
<dd> Flags to be used when linking a shared library. </p>
<p> Same as CMAKE_C_FLAGS_* but used by the linker when creating shared libraries. </p>
<dt><code>CMAKE_SKIP_BUILD_RPATH</code></p>
<dd> Do not include RPATHs in the build tree. </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with no RPATH. </p>
<dt><code>CMAKE_SKIP_INSTALL_RPATH</code></p>
<dd> Do not include RPATHs in the install tree. </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always installed without RPATH, even if RPATH is enabled when building. This can be useful for example to allow running tests from the build directory with RPATH enabled before the installation step. To omit RPATH in both the build and install steps, use CMAKE_SKIP_RPATH instead. </p>
<dt><code>CMAKE_STATIC_LINKER_FLAGS</code></p>
<dd> Linker flags to be used to create static libraries. </p>
<p> These flags will be used by the linker when creating a static library. </p>
<dt><code>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;</code></p>
<dd> Flags to be used when linking a static library. </p>
<p> Same as CMAKE_C_FLAGS_* but used by the linker when creating static libraries. </p>
<dt><code>CMAKE_TRY_COMPILE_CONFIGURATION</code></p>
<dd> Build configuration used for try_compile and try_run projects. </p>
<p> Projects built by try_compile and try_run are built synchronously during the CMake configuration step. Therefore a specific build configuration must be chosen even if the generated build system supports multiple configurations. </p>
<dt><code>CMAKE_USE_RELATIVE_PATHS</code></p>
<dd> Use relative paths (May not work!). </p>
<p> If this is set to TRUE, then CMake will use relative paths between the source and binary tree. This option does not work for more complicated projects, and relative paths are used when possible. In general, it is not possible to move CMake generated makefiles to a different location regardless of the value of this variable. </p>
<dt><code>CMAKE_VISIBILITY_INLINES_HIDDEN</code></p>
<dd> Default value for VISIBILITY_INLINES_HIDDEN of targets. </p>
<p> This variable is used to initialize the VISIBILITY_INLINES_HIDDEN property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_WIN32_EXECUTABLE</code></p>
<dd> Default value for WIN32_EXECUTABLE of targets. </p>
<p> This variable is used to initialize the WIN32_EXECUTABLE property on all the targets. See that target property for additional information. </p>
<dt><code>EXECUTABLE_OUTPUT_PATH</code></p>
<dd> Old executable location variable. </p>
<p> The target property RUNTIME_OUTPUT_DIRECTORY supercedes this variable for a target if it is set. Executable targets are otherwise placed in this directory. </p>
<dt><code>LIBRARY_OUTPUT_PATH</code></p>
<dd> Old library location variable. </p>
<p> The target properties ARCHIVE_OUTPUT_DIRECTORY, LIBRARY_OUTPUT_DIRECTORY, and RUNTIME_OUTPUT_DIRECTORY supercede this variable for a target if they are set. Library targets are otherwise placed in this directory. </p>
</dl>
<h2>VARIABLES FOR LANGUAGES</h2>
<dl>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code></p>
<dd> Rule variable to append to a static archive. </p>
<p> This is a rule variable that tells CMake how to append to a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE and CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH. </p>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code></p>
<dd> Rule variable to create a new static archive. </p>
<p> This is a rule variable that tells CMake how to create a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND and CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH. </p>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code></p>
<dd> Rule variable to finish an existing static archive. </p>
<p> This is a rule variable that tells CMake how to finish a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE and CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER</code></p>
<dd> The full path to the compiler for LANG. </p>
<p> This is the command that will be used as the &lt;LANG&gt; compiler. Once set, you can not change this variable. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_ABI</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code></p>
<dd> Compiler identification string. </p>
<p> A short string unique to the compiler vendor. Possible values include: </p>
<pre>
  Absoft = Absoft Fortran (absoft.com)
  ADSP = Analog VisualDSP++ (analog.com)
  Clang = LLVM Clang (clang.llvm.org)
  Cray = Cray Compiler (cray.com)
  Embarcadero, Borland = Embarcadero (embarcadero.com)
  G95 = G95 Fortran (g95.org)
  GNU = GNU Compiler Collection (gcc.gnu.org)
  HP = Hewlett-Packard Compiler (hp.com)
  Intel = Intel Compiler (intel.com)
  MIPSpro = SGI MIPSpro (sgi.com)
  MSVC = Microsoft Visual Studio (microsoft.com)
  PGI = The Portland Group (pgroup.com)
  PathScale = PathScale (pathscale.com)
  SDCC = Small Device C Compiler (sdcc.sourceforge.net)
  SunPro = Oracle Solaris Studio (oracle.com)
  TI = Texas Instruments (ti.com)
  TinyCC = Tiny C Compiler (tinycc.org)
  Watcom = Open Watcom (openwatcom.org)
  XL, VisualAge, zOS = IBM XL (ibm.com)
</pre>
<p> This variable is not guaranteed to be defined for all compilers or languages. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_LOADED</code></p>
<dd> Defined to true if the language is enabled. </p>
<p> When language &lt;LANG&gt; is enabled by project() or enable_language() this variable is defined to 1. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code></p>
<dd> Compiler version string. </p>
<p> Compiler version in major[.minor[.patch[.tweak]]] format. This variable is not guaranteed to be defined for all compilers or languages. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILE_OBJECT</code></p>
<dd> Rule variable to compile a single object file. </p>
<p> This is a rule variable that tells CMake how to compile a single object file for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_SHARED_LIBRARY</code></p>
<dd> Rule variable to create a shared library. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_SHARED_MODULE</code></p>
<dd> Rule variable to create a shared module. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code></p>
<dd> Rule variable to create a static library. </p>
<p> This is a rule variable that tells CMake how to create a static library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS</code></p>
<dd> Flags for all build types. </p>
<p> &lt;LANG&gt; flags used regardless of the value of CMAKE_BUILD_TYPE. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</code></p>
<dd> Flags for Debug build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is Debug. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_MINSIZEREL</code></p>
<dd> Flags for MinSizeRel build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is MinSizeRel.Short for minimum size release. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_RELEASE</code></p>
<dd> Flags for Release build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is Release </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_RELWITHDEBINFO</code></p>
<dd> Flags for RelWithDebInfo type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is RelWithDebInfo. Short for Release With Debug Information. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IGNORE_EXTENSIONS</code></p>
<dd> File extensions that should be ignored by the build. </p>
<p> This is a list of file extensions that may be part of a project for a given language but are not compiled. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IMPLICIT_INCLUDE_DIRECTORIES</code></p>
<dd> Directories implicitly searched by the compiler for header files. </p>
<p> CMake does not explicitly specify these directories on compiler command lines for language &lt;LANG&gt;. This prevents system include directories from being treated as user include directories on some compilers. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</code></p>
<dd> Implicit linker search path detected for language &lt;LANG&gt;. </p>
<p> Compilers typically pass directories containing language runtime libraries and default library search paths when they invoke a linker. These paths are implicit linker search directories for the compiler&#8217;s language. CMake automatically detects these directories for each language and reports the results in this variable. </p>
<p> When a library in one of these directories is given by full path to target_link_libraries() CMake will generate the -l&lt;name&gt; form on link lines to ensure the linker searches its implicit directories for the library. Note that some toolchains read implicit directories from an environment variable such as LIBRARY_PATH so keep its value consistent when operating in a given build tree. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES</code></p>
<dd> Implicit linker framework search path detected for language &lt;LANG&gt;. </p>
<p> These paths are implicit linker framework search directories for the compiler&#8217;s language. CMake automatically detects these directories for each language and reports the results in this variable. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</code></p>
<dd> Implicit link libraries and flags detected for language &lt;LANG&gt;. </p>
<p> Compilers typically pass language runtime library names and other flags when they invoke a linker. These flags are implicit link options for the compiler&#8217;s language. CMake automatically detects these libraries and flags for each language and reports the results in this variable. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</code></p>
<dd> Target architecture library directory name detected for &lt;lang&gt;. </p>
<p> If the &lt;lang&gt; compiler passes to the linker an architecture-specific system library search directory such as &lt;prefix&gt;/lib/&lt;arch&gt; this variable contains the &lt;arch&gt; name if/as detected by CMake. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</code></p>
<dd> Preference value for linker language selection. </p>
<p> The &quot;linker language&quot; for executable, shared library, and module targets is the language whose compiler will invoke the linker. The LINKER_LANGUAGE target property sets the language explicitly. Otherwise, the linker language is that whose linker preference value is highest among languages compiled and linked into the target. See also the CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES variable. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES</code></p>
<dd> True if CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE propagates across targets. </p>
<p> This is used when CMake selects a linker language for a target. Languages compiled directly into the target are always considered. A language compiled into static libraries linked by the target is considered if this variable is true. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LINK_EXECUTABLE </code></p>
<dd> Rule variable to link an executable. </p>
<p> Rule variable to link an executable for the given language. </p>
<dt><code>CMAKE_&lt;LANG&gt;_OUTPUT_EXTENSION</code></p>
<dd> Extension for the output of a compile for a single file. </p>
<p> This is the extension for an object file for the given &lt;LANG&gt;. For example .obj for C on Windows. </p>
<dt><code>CMAKE_&lt;LANG&gt;_PLATFORM_ID</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the platform and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_SIZEOF_DATA_PTR</code></p>
<dd> Size of pointer-to-data types for language &lt;LANG&gt;. </p>
<p> This holds the size (in bytes) of pointer-to-data types in the target platform ABI. It is defined for languages C and CXX (C++). </p>
<dt><code>CMAKE_&lt;LANG&gt;_SOURCE_FILE_EXTENSIONS</code></p>
<dd> Extensions of source files for the given language. </p>
<p> This is the list of extensions for a given language&#8217;s source files. </p>
<dt><code>CMAKE_COMPILER_IS_GNU&lt;LANG&gt;</code></p>
<dd> True if the compiler is GNU. </p>
<p> If the selected &lt;LANG&gt; compiler is the GNU compiler then this is TRUE, if not it is FALSE. Unlike the other per-language variables, this uses the GNU syntax for identifying languages instead of the CMake syntax. Recognized values of the &lt;LANG&gt; suffix are: </p>
<pre>
  CC = C compiler
  CXX = C++ compiler
  G77 = Fortran compiler
</pre>
<dt><code>CMAKE_Fortran_MODDIR_DEFAULT</code></p>
<dd> Fortran default module output directory. </p>
<p> Most Fortran compilers write .mod files to the current working directory. For those that do not, this is set to &quot;.&quot; and used when the Fortran_MODULE_DIRECTORY target property is not set. </p>
<dt><code>CMAKE_Fortran_MODDIR_FLAG</code></p>
<dd> Fortran flag for module output directory. </p>
<p> This stores the flag needed to pass the value of the Fortran_MODULE_DIRECTORY target property to the compiler. </p>
<dt><code>CMAKE_Fortran_MODOUT_FLAG</code></p>
<dd> Fortran flag to enable module output. </p>
<p> Most Fortran compilers write .mod files out by default. For others, this stores the flag needed to enable module output. </p>
<dt><code>CMAKE_INTERNAL_PLATFORM_ABI</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change. </p>
<dt><code>CMAKE_USER_MAKE_RULES_OVERRIDE_&lt;LANG&gt;</code></p>
<dd> Specify a CMake file that overrides platform information for &lt;LANG&gt;. </p>
<p> This is a language-specific version of CMAKE_USER_MAKE_RULES_OVERRIDE loaded only when enabling language &lt;LANG&gt;. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2000-2012 Kitware, Inc., Insight Software Consortium. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<p> Neither the names of Kitware, Inc., the Insight Software Consortium, nor the names of their contributors may be used to endorse or promote products derived from this software without specific prior written permission. </p>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<h2>SEE ALSO</h2>
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
<h2>Index</h2>
