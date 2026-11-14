---
title: "cmakemodules(1)"
name: "cmakemodules"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmakemodules/"
description: "cmakemodules – Reference of available CMake modules."
---

<h2>NAME</h2>
<p> cmakemodules &#8211; Reference of available CMake modules. </p>
<h2>DESCRIPTION</h2>
<p> The &quot;cmake&quot; executable is the CMake command-line interface. It may be used to configure projects in scripts. Project configuration settings may be specified on the command line with the -D option. The -i option will cause cmake to interactively prompt for such settings. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform. </p>
<h2>MODULES</h2>
<p> The following modules are provided with CMake. They can be used with INCLUDE(ModuleName). </p>
<pre>
  CMake Modules - Modules coming with CMake, the Cross-Platform Makefile Generator.
</pre>
<p> This is the documentation for the modules and scripts coming with CMake. Using these modules you can check the computer system for installed software packages, features of the compiler and the existence of headers to name just a few. </p>
<dl>
<dt><code>AddFileDependencies</code></p>
<dd> ADD_FILE_DEPENDENCIES(source_file depend_files&#8230;) </p>
<p> Adds the given files as dependencies to source_file </p>
<dt><code>BundleUtilities</code></p>
<dd> Functions to help assemble a standalone bundle application. </p>
<p> A collection of CMake utility functions useful for dealing with .app bundles on the Mac and bundle-like directories on any OS. </p>
<p> The following functions are provided by this module: </p>
<pre>
   fixup_bundle
   copy_and_fixup_bundle
   verify_app
   get_bundle_main_executable
   get_dotapp_dir
   get_bundle_and_executable
   get_bundle_all_executables
   get_item_key
   clear_bundle_keys
   set_bundle_key_values
   get_bundle_keys
   copy_resolved_item_into_bundle
   copy_resolved_framework_into_bundle
   fixup_bundle_item
   verify_bundle_prerequisites
   verify_bundle_symlinks
</pre>
<p> Requires CMake 2.6 or greater because it uses function, break and PARENT_SCOPE. Also depends on GetPrerequisites.cmake. </p>
<pre>
  FIXUP_BUNDLE(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt;)
</pre>
<p> Fix up a bundle in-place and make it standalone, such that it can be drag-n-drop copied to another machine and run on that machine as long as all of the system libraries are compatible. </p>
<p> If you pass plugins to fixup_bundle as the libs parameter, you should install them or copy them into the bundle before calling fixup_bundle. The &quot;libs&quot; parameter is a list of libraries that must be fixed up, but that cannot be determined by otool output analysis. (i.e., plugins) </p>
<p> Gather all the keys for all the executables and libraries in a bundle, and then, for each key, copy each prerequisite into the bundle. Then fix each one up according to its own list of prerequisites. </p>
<p> Then clear all the keys and call verify_app on the final bundle to ensure that it is truly standalone. </p>
<pre>
  COPY_AND_FIXUP_BUNDLE(&lt;src&gt; &lt;dst&gt; &lt;libs&gt; &lt;dirs&gt;)
</pre>
<p> Makes a copy of the bundle &lt;src&gt; at location &lt;dst&gt; and then fixes up the new copied bundle in-place at &lt;dst&gt;&#8230; </p>
<pre>
  VERIFY_APP(&lt;app&gt;)
</pre>
<p> Verifies that an application &lt;app&gt; appears valid based on running analysis tools on it. Calls &quot;message(FATAL_ERROR&quot; if the application is not verified. </p>
<pre>
  GET_BUNDLE_MAIN_EXECUTABLE(&lt;bundle&gt; &lt;result_var&gt;)
</pre>
<p> The result will be the full path name of the bundle&#8217;s main executable file or an &quot;error:&quot; prefixed string if it could not be determined. </p>
<pre>
  GET_DOTAPP_DIR(&lt;exe&gt; &lt;dotapp_dir_var&gt;)
</pre>
<p> Returns the nearest parent dir whose name ends with &quot;.app&quot; given the full path to an executable. If there is no such parent dir, then simply return the dir containing the executable. </p>
<p> The returned directory may or may not exist. </p>
<pre>
  GET_BUNDLE_AND_EXECUTABLE(&lt;app&gt; &lt;bundle_var&gt; &lt;executable_var&gt; &lt;valid_var&gt;)
</pre>
<p> Takes either a &quot;.app&quot; directory name or the name of an executable nested inside a &quot;.app&quot; directory and returns the path to the &quot;.app&quot; directory in &lt;bundle_var&gt; and the path to its main executable in &lt;executable_var&gt; </p>
<pre>
  GET_BUNDLE_ALL_EXECUTABLES(&lt;bundle&gt; &lt;exes_var&gt;)
</pre>
<p> Scans the given bundle recursively for all executable files and accumulates them into a variable. </p>
<pre>
  GET_ITEM_KEY(&lt;item&gt; &lt;key_var&gt;)
</pre>
<p> Given a file (item) name, generate a key that should be unique considering the set of libraries that need copying or fixing up to make a bundle standalone. This is essentially the file name including extension with &quot;.&quot; replaced by &quot;_&quot; </p>
<p> This key is used as a prefix for CMake variables so that we can associate a set of variables with a given item based on its key. </p>
<pre>
  CLEAR_BUNDLE_KEYS(&lt;keys_var&gt;)
</pre>
<p> Loop over the list of keys, clearing all the variables associated with each key. After the loop, clear the list of keys itself. </p>
<p> Caller of get_bundle_keys should call clear_bundle_keys when done with list of keys. </p>
<pre>
  SET_BUNDLE_KEY_VALUES(&lt;keys_var&gt; &lt;context&gt; &lt;item&gt; &lt;exepath&gt; &lt;dirs&gt;
                        &lt;copyflag&gt;)
</pre>
<p> Add a key to the list (if necessary) for the given item. If added, also set all the variables associated with that key. </p>
<pre>
  GET_BUNDLE_KEYS(&lt;app&gt; &lt;libs&gt; &lt;dirs&gt; &lt;keys_var&gt;)
</pre>
<p> Loop over all the executable and library files within the bundle (and given as extra &lt;libs&gt;) and accumulate a list of keys representing them. Set values associated with each key such that we can loop over all of them and copy prerequisite libs into the bundle and then do appropriate install_name_tool fixups. </p>
<pre>
  COPY_RESOLVED_ITEM_INTO_BUNDLE(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)
</pre>
<p> Copy a resolved item into the bundle if necessary. Copy is not necessary if the resolved_item is &quot;the same as&quot; the resolved_embedded_item. </p>
<pre>
  COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE(&lt;resolved_item&gt; &lt;resolved_embedded_item&gt;)
</pre>
<p> Copy a resolved framework into the bundle if necessary. Copy is not necessary if the resolved_item is &quot;the same as&quot; the resolved_embedded_item. </p>
<p> By default, BU_COPY_FULL_FRAMEWORK_CONTENTS is not set. If you want full frameworks embedded in your bundles, set BU_COPY_FULL_FRAMEWORK_CONTENTS to ON before calling fixup_bundle. By default, COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE copies the framework dylib itself plus the framework Resources directory. </p>
<pre>
  FIXUP_BUNDLE_ITEM(&lt;resolved_embedded_item&gt; &lt;exepath&gt; &lt;dirs&gt;)
</pre>
<p> Get the direct/non-system prerequisites of the resolved embedded item. For each prerequisite, change the way it is referenced to the value of the _EMBEDDED_ITEM keyed variable for that prerequisite. (Most likely changing to an &quot;@executable_path&quot; style reference.) </p>
<p> This function requires that the resolved_embedded_item be &quot;inside&quot; the bundle already. In other words, if you pass plugins to fixup_bundle as the libs parameter, you should install them or copy them into the bundle before calling fixup_bundle. The &quot;libs&quot; parameter is a list of libraries that must be fixed up, but that cannot be determined by otool output analysis. (i.e., plugins) </p>
<p> Also, change the id of the item being fixed up to its own _EMBEDDED_ITEM value. </p>
<p> Accumulate changes in a local variable and make *one* call to install_name_tool at the end of the function with all the changes at once. </p>
<p> If the BU_CHMOD_BUNDLE_ITEMS variable is set then bundle items will be marked writable before install_name_tool tries to change them. </p>
<pre>
  VERIFY_BUNDLE_PREREQUISITES(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)
</pre>
<p> Verifies that the sum of all prerequisites of all files inside the bundle are contained within the bundle or are &quot;system&quot; libraries, presumed to exist everywhere. </p>
<pre>
  VERIFY_BUNDLE_SYMLINKS(&lt;bundle&gt; &lt;result_var&gt; &lt;info_var&gt;)
</pre>
<p> Verifies that any symlinks found in the bundle point to other files that are already also in the bundle&#8230; Anything that points to an external file causes this function to fail the verification. </p>
<dt><code>CMakeAddFortranSubdirectory</code></p>
<dd> Use MinGW gfortran from VS if a fortran compiler is not found. </p>
<p> The &#8216;add_fortran_subdirectory&#8217; function adds a subdirectory to a project that contains a fortran only sub-project. The module will check the current compiler and see if it can support fortran. If no fortran compiler is found and the compiler is MSVC, then this module will find the MinGW gfortran. It will then use an external project to build with the MinGW tools. It will also create imported targets for the libraries created. This will only work if the fortran code is built into a dll, so BUILD_SHARED_LIBS is turned on in the project. In addition the CMAKE_GNUtoMS option is set to on, so that the MS .lib files are created. Usage is as follows: </p>
<pre>
  cmake_add_fortran_subdirectory(
   &lt;subdir&gt;                # name of subdirectory
   PROJECT &lt;project_name&gt;  # project name in subdir top CMakeLists.txt
   ARCHIVE_DIR &lt;dir&gt;       # dir where project places .lib files
   RUNTIME_DIR &lt;dir&gt;       # dir where project places .dll files
   LIBRARIES &lt;lib&gt;...      # names of library targets to import
   LINK_LIBRARIES          # link interface libraries for LIBRARIES
    [LINK_LIBS &lt;lib&gt; &lt;dep&gt;...]...
   CMAKE_COMMAND_LINE ...  # extra command line flags to pass to cmake
   NO_EXTERNAL_INSTALL     # skip installation of external project
   )
</pre>
<p> Relative paths in ARCHIVE_DIR and RUNTIME_DIR are interpreted with respect to the build directory corresponding to the source directory in which the function is invoked. </p>
<p> Limitations: </p>
<p> NO_EXTERNAL_INSTALL is required for forward compatibility with a future version that supports installation of the external project binaries during &quot;make install&quot;. </p>
<dt><code>CMakeBackwardCompatibilityCXX</code></p>
<dd> define a bunch of backwards compatibility variables </p>
<pre><code>
  CMAKE_ANSI_CXXFLAGS - flag for ansi c++
  CMAKE_HAS_ANSI_STRING_STREAM - has &lt;strstream&gt;
  include(TestForANSIStreamHeaders)
  include(CheckIncludeFileCXX)
  include(TestForSTDNamespace)
  include(TestForANSIForScope)
</code></pre>
<dt><code>CMakeDependentOption</code></p>
<dd> Macro to provide an option dependent on other options. </p>
<p> This macro presents an option to the user only if a set of other conditions are true. When the option is not presented a default value is used, but any value set by the user is preserved for when the option is presented again. Example invocation: </p>
<pre>
  CMAKE_DEPENDENT_OPTION(USE_FOO &quot;Use Foo&quot; ON
                         &quot;USE_BAR;NOT USE_ZOT&quot; OFF)
</pre>
<p> If USE_BAR is true and USE_ZOT is false, this provides an option called USE_FOO that defaults to ON. Otherwise, it sets USE_FOO to OFF. If the status of USE_BAR or USE_ZOT ever changes, any value for the USE_FOO option is saved so that when the option is re-enabled it retains its old value. </p>
<dt><code>CMakeDetermineVSServicePack</code></p>
<dd> Determine the Visual Studio service pack of the &#8216;cl&#8217; in use. </p>
<p> The functionality of this module has been superseded by the platform variable CMAKE_&lt;LANG&gt;_COMPILER_VERSION that contains the compiler version number. </p>
<p> Usage: </p>
<p>if (MSVC)<br />
include(CMakeDetermineVSServicePack)<br />
    DetermineVSServicePack(my_service_pack) if (my_service_pack)<br />
        message(STATUS &#8220;Detected: ${my_service_pack}&#8221;)<br />
            endif()<br />
                endif()</p>
<p> Function DetermineVSServicePack sets the given variable to one of the following values or an empty string if unknown: </p>
<pre>
  vc80, vc80sp1
  vc90, vc90sp1
  vc100, vc100sp1
  vc110, vc110sp1, vc110sp2
</pre>
<dt><code>CMakeExpandImportedTargets</code></p>
<dd>
<p> CMAKE_EXPAND_IMPORTED_TARGETS(&lt;var&gt; LIBRARIES lib1 lib2&#8230;libN </p>
<pre>
                                     [CONFIGURATION &lt;config&gt;] )
</pre>
<p> CMAKE_EXPAND_IMPORTED_TARGETS() takes a list of libraries and replaces all imported targets contained in this list with their actual file paths of the referenced libraries on disk, including the libraries from their link interfaces. If a CONFIGURATION is given, it uses the respective configuration of the imported targets if it exists. If no CONFIGURATION is given, it uses the first configuration from ${CMAKE_CONFIGURATION_TYPES} if set, otherwise ${CMAKE_BUILD_TYPE}. This macro is used by all Check*.cmake files which use try_compile() or try_run() and support CMAKE_REQUIRED_LIBRARIES , so that these checks support imported targets in CMAKE_REQUIRED_LIBRARIES: </p>
<p>cmake_expand_imported_targets(expandedLibs LIBRARIES ${CMAKE_REQUIRED_LIBRARIES} CONFIGURATION &#8220;${CMAKE_TRY_COMPILE_CONFIGURATION}&#8221;)</p>
<dt><code>CMakeFindFrameworks</code></p>
<dd> helper module to find OSX frameworks </p>
<dt><code>CMakeFindPackageMode</code></p>
<dd>
<p> This file is executed by cmake when invoked with &#8211;find-package. It expects that the following variables are set using -D: </p>
<p>   NAME = name of the package<br />
   COMPILER_ID = the CMake compiler ID for which the result is, i.e. GNU/Intel/Clang/MSVC, etc.<br />
   LANGUAGE = language for which the result will be used, i.e. C/CXX/Fortan/ASM<br />
   MODE = EXIST : only check for existence of the given package<br />
          COMPILE : print the flags needed for compiling an object file which uses the given package<br />
          LINK : print the flags needed for linking when using the given package<br />
   QUIET = if TRUE, don&#8217;t print anything</p>
<dt><code>CMakeForceCompiler</code></p>
<dd>
<p> This module defines macros intended for use by cross-compiling toolchain files when CMake is not able to automatically detect the compiler identification. </p>
<p> Macro CMAKE_FORCE_C_COMPILER has the following signature: </p>
<pre>
   CMAKE_FORCE_C_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)
</pre>
<p> It sets CMAKE_C_COMPILER to the given compiler and the cmake internal variable CMAKE_C_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro CMAKE_FORCE_CXX_COMPILER has the following signature: </p>
<pre>
   CMAKE_FORCE_CXX_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)
</pre>
<p> It sets CMAKE_CXX_COMPILER to the given compiler and the cmake internal variable CMAKE_CXX_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro CMAKE_FORCE_Fortran_COMPILER has the following signature: </p>
<pre>
   CMAKE_FORCE_Fortran_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)
</pre>
<p> It sets CMAKE_Fortran_COMPILER to the given compiler and the cmake internal variable CMAKE_Fortran_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> So a simple toolchain file could look like this: </p>
<pre>
   include (CMakeForceCompiler)
   set(CMAKE_SYSTEM_NAME Generic)
   CMAKE_FORCE_C_COMPILER   (chc12 MetrowerksHicross)
   CMAKE_FORCE_CXX_COMPILER (chc12 MetrowerksHicross)
</pre>
<dt><code>CMakeGraphVizOptions</code></p>
<dd> The builtin graphviz support of CMake. </p>
<p> CMake can generate graphviz files, showing the dependencies between the targets in a project and also external libraries which are linked against. When CMake is run with the &#8211;graphiz=foo option, it will produce </p>
<pre>
    * a foo.dot file showing all dependencies in the project
    * a foo.dot.&lt;target&gt; file for each target, file showing on which other targets the respective target depends
    * a foo.dot.&lt;target&gt;.dependers file, showing which other targets depend on the respective target
</pre>
<p> This can result in huge graphs. Using the file CMakeGraphVizOptions.cmake the look and content of the generated graphs can be influenced. This file is searched first in ${CMAKE_BINARY_DIR} and then in ${CMAKE_SOURCE_DIR}. If found, it is read and the variables set in it are used to adjust options for the generated graphviz files. </p>
<p>  GRAPHVIZ_GRAPH_TYPE &#8211; The graph type<br />
     Mandatory : NO<br />
     Default   : &#8220;digraph&#8221;<br />
  GRAPHVIZ_GRAPH_NAME &#8211; The graph name.<br />
     Mandatory : NO<br />
     Default   : &#8220;GG&#8221;<br />
  GRAPHVIZ_GRAPH_HEADER &#8211; The header written at the top of the graphviz file.<br />
     Mandatory : NO<br />
     Default   : &#8220;node [n  fontsize = &#8220;12&#8221;];&#8221;<br />
  GRAPHVIZ_NODE_PREFIX &#8211; The prefix for each node in the graphviz file.<br />
     Mandatory : NO<br />
     Default   : &#8220;node&#8221;<br />
  GRAPHVIZ_EXECUTABLES &#8211; Set this to FALSE to exclude executables from the generated graphs.<br />
     Mandatory : NO<br />
     Default   : TRUE<br />
  GRAPHVIZ_STATIC_LIBS &#8211; Set this to FALSE to exclude static libraries from the generated graphs.<br />
     Mandatory : NO<br />
     Default   : TRUE<br />
  GRAPHVIZ_SHARED_LIBS &#8211; Set this to FALSE to exclude shared libraries from the generated graphs.<br />
     Mandatory : NO<br />
     Default   : TRUE<br />
  GRAPHVIZ_MODULE_LIBS &#8211; Set this to FALSE to exclude static libraries from the generated graphs.<br />
     Mandatory : NO<br />
     Default   : TRUE<br />
  GRAPHVIZ_EXTERNAL_LIBS &#8211; Set this to FALSE to exclude external libraries from the generated graphs.<br />
     Mandatory : NO<br />
     Default   : TRUE<br />
  GRAPHVIZ_IGNORE_TARGETS &#8211; A list of regular expressions for ignoring targets.<br />
     Mandatory : NO<br />
     Default   : empty</p>
<dt><code>CMakePackageConfigHelpers</code></p>
<dd> CONFIGURE_PACKAGE_CONFIG_FILE(), WRITE_BASIC_PACKAGE_VERSION_FILE() </p>
<p>CONFIGURE_PACKAGE_CONFIG_FILE(&lt;input&gt;&lt;output&gt; INSTALL_DESTINATION&lt;path&gt;[PATH_VARS&lt;var1&gt;&lt;var2&gt;&#8230;&lt;varN&gt;]<br />
                                                                       [NO_SET_AND_CHECK_MACRO]<br />
                                                                       [NO_CHECK_REQUIRED_COMPONENTS_MACRO])</p>
<p> CONFIGURE_PACKAGE_CONFIG_FILE() should be used instead of the plain configure_file() command when creating the &lt;Name&gt;Config.cmake or &lt;Name&gt;-config.cmake file for installing a project or library. It helps making the resulting package relocatable by avoiding hardcoded paths in the installed Config.cmake file. </p>
<p> In a FooConfig.cmake file there may be code like this to make the install destinations know to the using project: </p>
<pre>
   set(FOO_INCLUDE_DIR   &quot;@CMAKE_INSTALL_FULL_INCLUDEDIR@&quot; )
   set(FOO_DATA_DIR   &quot;@CMAKE_INSTALL_PREFIX@/@RELATIVE_DATA_INSTALL_DIR@&quot; )
   set(FOO_ICONS_DIR   &quot;@CMAKE_INSTALL_PREFIX@/share/icons&quot; )
   ...logic to determine installedPrefix from the own location...
   set(FOO_CONFIG_DIR  &quot;${installedPrefix}/@CONFIG_INSTALL_DIR@&quot; )
</pre>
<p> All 4 options shown above are not sufficient, since the first 3 hardcode the absolute directory locations, and the 4th case works only if the logic to determine the installedPrefix is correct, and if CONFIG_INSTALL_DIR contains a relative path, which in general cannot be guaranteed. This has the effect that the resulting FooConfig.cmake file would work poorly under Windows and OSX, where users are used to choose the install location of a binary package at install time, independent from how CMAKE_INSTALL_PREFIX was set at build/cmake time. </p>
<p> Using CONFIGURE_PACKAGE_CONFIG_FILE() helps. If used correctly, it makes the resulting FooConfig.cmake file relocatable. Usage: </p>
<pre>
   1. write a FooConfig.cmake.in file as you are used to
   2. insert a line containing only the string &quot;@PACKAGE_INIT@&quot;
   3. instead of set(FOO_DIR &quot;@SOME_INSTALL_DIR@&quot;), use set(FOO_DIR &quot;@PACKAGE_SOME_INSTALL_DIR@&quot;)
      (this must be after the @PACKAGE_INIT@ line)
   4. instead of using the normal configure_file(), use CONFIGURE_PACKAGE_CONFIG_FILE()
</pre>
<p> The &lt;input&gt; and &lt;output&gt; arguments are the input and output file, the same way as in configure_file(). </p>
<p> The &lt;path&gt; given to INSTALL_DESTINATION must be the destination where the FooConfig.cmake file will be installed to. This can either be a relative or absolute path, both work. </p>
<p> The variables &lt;var1&gt; to &lt;varN&gt; given as PATH_VARS are the variables which contain install destinations. For each of them the macro will create a helper variable PACKAGE_&lt;var&#8230;&gt;. These helper variables must be used in the FooConfig.cmake.in file for setting the installed location. They are calculated by CONFIGURE_PACKAGE_CONFIG_FILE() so that they are always relative to the installed location of the package. This works both for relative and also for absolute locations. For absolute locations it works only if the absolute location is a subdirectory of CMAKE_INSTALL_PREFIX. </p>
<p> By default configure_package_config_file() also generates two helper macros, set_and_check() and check_required_components() into the FooConfig.cmake file. </p>
<p> set_and_check() should be used instead of the normal set() command for setting directories and file locations. Additionally to setting the variable it also checks that the referenced file or directory actually exists and fails with a FATAL_ERROR otherwise. This makes sure that the created FooConfig.cmake file does not contain wrong references. When using the NO_SET_AND_CHECK_MACRO, this macro is not generated into the FooConfig.cmake file. </p>
<p> check_required_components(&lt;package_name&gt;) should be called at the end of the FooConfig.cmake file if the package supports components. This macro checks whether all requested, non-optional components have been found, and if this is not the case, sets the Foo_FOUND variable to FALSE, so that the package is considered to be not found. It does that by testing the Foo_&lt;Component&gt;_FOUND variables for all requested required components. When using the NO_CHECK_REQUIRED_COMPONENTS option, this macro is not generated into the FooConfig.cmake file. </p>
<p> For an example see below the documentation for WRITE_BASIC_PACKAGE_VERSION_FILE(). </p>
<pre>
  WRITE_BASIC_PACKAGE_VERSION_FILE( filename VERSION major.minor.patch COMPATIBILITY (AnyNewerVersion|SameMajorVersion|ExactVersion) )
</pre>
<p> Writes a file for use as &lt;package&gt;ConfigVersion.cmake file to &lt;filename&gt;. See the documentation of find_package() for details on this. </p>
<pre>
    filename is the output filename, it should be in the build tree.
    major.minor.patch is the version number of the project to be installed
</pre>
<p> The COMPATIBILITY mode AnyNewerVersion means that the installed package version will be considered compatible if it is newer or exactly the same as the requested version. This mode should be used for packages which are fully backward compatible, also across major versions. If SameMajorVersion is used instead, then the behaviour differs from AnyNewerVersion in that the major version number must be the same as requested, e.g. version 2.0 will not be considered compatible if 1.0 is requested. This mode should be used for packages which guarantee backward compatibility within the same major version. If ExactVersion is used, then the package is only considered compatible if the requested version matches exactly its own version number (not considering the tweak version). For example, version 1.2.3 of a package is only considered compatible to requested version 1.2.3. This mode is for packages without compatibility guarantees. If your project has more elaborated version matching rules, you will need to write your own custom ConfigVersion.cmake file instead of using this macro. </p>
<p> Internally, this macro executes configure_file() to create the resulting version file. Depending on the COMPATIBLITY, either the file BasicConfigVersion-SameMajorVersion.cmake.in or BasicConfigVersion-AnyNewerVersion.cmake.in is used. Please note that these two files are internal to CMake and you should not call configure_file() on them yourself, but they can be used as starting point to create more sophisticted custom ConfigVersion.cmake files. </p>
<p> Example using both configure_package_config_file() and write_basic_package_version_file(): CMakeLists.txt: </p>
<p>set(INCLUDE_INSTALL_DIR include / &#8230; CACHE)<br />
    set(LIB_INSTALL_DIR lib / &#8230; CACHE)<br />
        set(SYSCONFIG_INSTALL_DIR etc / foo / &#8230; CACHE)&#8230; include(CMakePackageConfigHelpers)<br />
            configure_package_config_file(FooConfig.cmake.in ${CMAKE_CURRENT_BINARY_DIR} / FooConfig.cmake INSTALL_DESTINATION ${LIB_INSTALL_DIR} / Foo / cmake PATH_VARS INCLUDE_INSTALL_DIR SYSCONFIG_INSTALL_DIR)<br />
                write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR} / FooConfigVersion.cmake<br />
                                                                                   VERSION 1.2.3 COMPATIBILITY SameMajorVersion)<br />
                    install(FILES ${CMAKE_CURRENT_BINARY_DIR} / FooConfig.cmake ${CMAKE_CURRENT_BINARY_DIR} / FooConfigVersion.cmake DESTINATION ${LIB_INSTALL_DIR} / Foo / cmake)</p>
<p> With a FooConfig.cmake.in: </p>
<pre>
   set(FOO_VERSION x.y.z)
   ...
   @PACKAGE_INIT@
   ...
   set_and_check(FOO_INCLUDE_DIR &quot;@PACKAGE_INCLUDE_INSTALL_DIR@&quot;)
   set_and_check(FOO_SYSCONFIG_DIR &quot;@PACKAGE_SYSCONFIG_INSTALL_DIR@&quot;)
</pre>
<pre>
   check_required_components(Foo)
</pre>
<dt><code>CMakeParseArguments</code></p>
<dd>
<p> CMAKE_PARSE_ARGUMENTS(&lt;prefix&gt; &lt;options&gt; &lt;one_value_keywords&gt; &lt;multi_value_keywords&gt; args&#8230;) </p>
<p> CMAKE_PARSE_ARGUMENTS() is intended to be used in macros or functions for parsing the arguments given to that macro or function. It processes the arguments and defines a set of variables which hold the values of the respective options. </p>
<p> The &lt;options&gt; argument contains all options for the respective macro, i.e. keywords which can be used when calling the macro without any value following, like e.g. the OPTIONAL keyword of the install() command. </p>
<p> The &lt;one_value_keywords&gt; argument contains all keywords for this macro which are followed by one value, like e.g. DESTINATION keyword of the install() command. </p>
<p> The &lt;multi_value_keywords&gt; argument contains all keywords for this macro which can be followed by more than one value, like e.g. the TARGETS or FILES keywords of the install() command. </p>
<p> When done, CMAKE_PARSE_ARGUMENTS() will have defined for each of the keywords listed in &lt;options&gt;, &lt;one_value_keywords&gt; and &lt;multi_value_keywords&gt; a variable composed of the given &lt;prefix&gt; followed by &quot;_&quot; and the name of the respective keyword. These variables will then hold the respective value from the argument list. For the &lt;options&gt; keywords this will be TRUE or FALSE. </p>
<p> All remaining arguments are collected in a variable &lt;prefix&gt;_UNPARSED_ARGUMENTS, this can be checked afterwards to see whether your macro was called with unrecognized parameters. </p>
<p> As an example here a my_install() macro, which takes similar arguments as the real install() command: </p>
<p>function(MY_INSTALL)<br />
    set(options OPTIONAL FAST)<br />
        set(oneValueArgs DESTINATION RENAME)<br />
            set(multiValueArgs TARGETS CONFIGURATIONS)<br />
                cmake_parse_arguments(MY_INSTALL &#8220;${options}&#8221;<br />
                                                 &#8220;${oneValueArgs}&#8221;<br />
                                                 &#8220;${multiValueArgs}&#8221; ${ARGN})&#8230;</p>
<p> Assume my_install() has been called like this: </p>
<pre>
   my_install(TARGETS foo bar DESTINATION bin OPTIONAL blub)
</pre>
<p> After the cmake_parse_arguments() call the macro will have set the following variables: </p>
<pre>
   MY_INSTALL_OPTIONAL = TRUE
   MY_INSTALL_FAST = FALSE (this option was not used when calling my_install()
   MY_INSTALL_DESTINATION = &quot;bin&quot;
   MY_INSTALL_RENAME = &quot;&quot; (was not used)
   MY_INSTALL_TARGETS = &quot;foo;bar&quot;
   MY_INSTALL_CONFIGURATIONS = &quot;&quot; (was not used)
   MY_INSTALL_UNPARSED_ARGUMENTS = &quot;blub&quot; (no value expected after &quot;OPTIONAL&quot;
</pre>
<p> You can then continue and process these variables. </p>
<p> Keywords terminate lists of values, e.g. if directly after a one_value_keyword another recognized keyword follows, this is interpreted as the beginning of the new option. E.g. my_install(TARGETS foo DESTINATION OPTIONAL) would result in MY_INSTALL_DESTINATION set to &quot;OPTIONAL&quot;, but MY_INSTALL_DESTINATION would be empty and MY_INSTALL_OPTIONAL would be set to TRUE therefor. </p>
<dt><code>CMakePrintHelpers</code></p>
<dd> Convenience macros for printing properties and variables, useful e.g. for debugging. </p>
<p> CMAKE_PRINT_PROPERTIES([TARGETS target1 .. targetN] </p>
<p>                        [SOURCES source1 .. sourceN]<br />
                        [DIRECTORIES dir1 .. dirN]<br />
                        [TESTS test1 .. testN]<br />
                        [CACHE_ENTRIES entry1 .. entryN]<br />
                        PROPERTIES prop1 .. propN )</p>
<p> This macro prints the values of the properties of the given targets, source files, directories, tests or cache entries. Exactly one of the scope keywords must be used. Example: </p>
<pre>
   cmake_print_properties(TARGETS foo bar PROPERTIES LOCATION INTERFACE_INCLUDE_DIRS)
</pre>
<p> This will print the LOCATION and INTERFACE_INCLUDE_DIRS properties for both targets foo and bar. </p>
<p> CMAKE_PRINT_VARIABLES(var1 var2 .. varN) </p>
<p> This macro will print the name of each variable followed by its value. Example: </p>
<pre>
   cmake_print_variables(CMAKE_C_COMPILER CMAKE_MAJOR_VERSION THIS_ONE_DOES_NOT_EXIST)
</pre>
<p> Gives: </p>
<pre>
   -- CMAKE_C_COMPILER=&quot;/usr/bin/gcc&quot; ; CMAKE_MAJOR_VERSION=&quot;2&quot; ; THIS_ONE_DOES_NOT_EXIST=&quot;&quot;
</pre>
<dt><code>CMakePrintSystemInformation</code></p>
<dd> print system information </p>
<p> This file can be used for diagnostic purposes just include it in a project to see various internal CMake variables. </p>
<dt><code>CMakePushCheckState</code></p>
<dd>
<p> This module defines three macros: CMAKE_PUSH_CHECK_STATE() CMAKE_POP_CHECK_STATE() and CMAKE_RESET_CHECK_STATE() These macros can be used to save, restore and reset (i.e., clear contents) the state of the variables CMAKE_REQUIRED_FLAGS, CMAKE_REQUIRED_DEFINITIONS, CMAKE_REQUIRED_LIBRARIES and CMAKE_REQUIRED_INCLUDES used by the various Check-files coming with CMake, like e.g. check_function_exists() etc. The variable contents are pushed on a stack, pushing multiple times is supported. This is useful e.g. when executing such tests in a Find-module, where they have to be set, but after the Find-module has been executed they should have the same value as they had before. </p>
<p> CMAKE_PUSH_CHECK_STATE() macro receives optional argument RESET. Whether it&#8217;s specified, CMAKE_PUSH_CHECK_STATE() will set all CMAKE_REQUIRED_* variables to empty values, same as CMAKE_RESET_CHECK_STATE() call will do. </p>
<p> Usage: </p>
<pre>
   cmake_push_check_state(RESET)
   set(CMAKE_REQUIRED_DEFINITIONS -DSOME_MORE_DEF)
   check_function_exists(...)
   cmake_reset_check_state()
   set(CMAKE_REQUIRED_DEFINITIONS -DANOTHER_DEF)
   check_function_exists(...)
   cmake_pop_check_state()
</pre>
<dt><code>CMakeVerifyManifest</code></p>
<dd>
<p> CMakeVerifyManifest.cmake </p>
<p> This script is used to verify that embeded manifests and side by side manifests for a project match. To run this script, cd to a directory and run the script with cmake -P. On the command line you can pass in versions that are OK even if not found in the .manifest files. For example, cmake -Dallow_versions=8.0.50608.0 -PCmakeVerifyManifest.cmake could be used to allow an embeded manifest of 8.0.50608.0 to be used in a project even if that version was not found in the .manifest file. </p>
<dt><code>CPack</code></p>
<dd> Build binary and source package installers. </p>
<p> The CPack module generates binary and source installers in a variety of formats using the cpack program. Inclusion of the CPack module adds two new targets to the resulting makefiles, package and package_source, which build the binary and source installers, respectively. The generated binary installers contain everything installed via CMake&#8217;s INSTALL command (and the deprecated INSTALL_FILES, INSTALL_PROGRAMS, and INSTALL_TARGETS commands). </p>
<p> For certain kinds of binary installers (including the graphical installers on Mac OS X and Windows), CPack generates installers that allow users to select individual application components to install. See CPackComponent module for that. </p>
<p> The CPACK_GENERATOR variable has different meanings in different contexts. In your CMakeLists.txt file, CPACK_GENERATOR is a *list of generators*: when run with no other arguments, CPack will iterate over that list and produce one package for each generator. In a CPACK_PROJECT_CONFIG_FILE, though, CPACK_GENERATOR is a *string naming a single generator*. If you need per-cpack- generator logic to control *other* cpack settings, then you need a CPACK_PROJECT_CONFIG_FILE. </p>
<p> The CMake source tree itself contains a CPACK_PROJECT_CONFIG_FILE. See the top level file CMakeCPackOptions.cmake.in for an example. </p>
<p> If set, the CPACK_PROJECT_CONFIG_FILE is included automatically on a per-generator basis. It only need contain overrides. </p>
<p> Here&#8217;s how it works: </p>
<pre>
  - cpack runs
  - it includes CPackConfig.cmake
  - it iterates over the generators listed in that file's
    CPACK_GENERATOR list variable (unless told to use just a
    specific one via -G on the command line...)
</pre>
<pre>
  - foreach generator, it then
    - sets CPACK_GENERATOR to the one currently being iterated
    - includes the CPACK_PROJECT_CONFIG_FILE
    - produces the package for that generator
</pre>
<p> This is the key: For each generator listed in CPACK_GENERATOR in CPackConfig.cmake, cpack will *reset* CPACK_GENERATOR internally to *the one currently being used* and then include the CPACK_PROJECT_CONFIG_FILE. </p>
<p> Before including this CPack module in your CMakeLists.txt file, there are a variety of variables that can be set to customize the resulting installers. The most commonly-used variables are: </p>
<pre>
  CPACK_PACKAGE_NAME - The name of the package (or application). If
  not specified, defaults to the project name.
</pre>
<pre>
  CPACK_PACKAGE_VENDOR - The name of the package vendor. (e.g.,
  &quot;Kitware&quot;).
</pre>
<pre>
  CPACK_PACKAGE_DIRECTORY - The directory in which CPack is doing its
  packaging. If it is not set then this will default (internally) to the
  build dir. This variable may be defined in CPack config file or from
  the cpack command line option &quot;-B&quot;. If set the command line option
  override the value found in the config file.
</pre>
<pre>
  CPACK_PACKAGE_VERSION_MAJOR - Package major Version
</pre>
<pre>
  CPACK_PACKAGE_VERSION_MINOR - Package minor Version
</pre>
<pre>
  CPACK_PACKAGE_VERSION_PATCH - Package patch Version
</pre>
<pre>
  CPACK_PACKAGE_DESCRIPTION_FILE - A text file used to describe the
  project. Used, for example, the introduction screen of a
  CPack-generated Windows installer to describe the project.
</pre>
<pre>
  CPACK_PACKAGE_DESCRIPTION_SUMMARY - Short description of the
  project (only a few words).
</pre>
<pre>
  CPACK_PACKAGE_FILE_NAME - The name of the package file to generate,
  not including the extension. For example, cmake-2.6.1-Linux-i686.
  The default value is
</pre>
<p>${CPACK_PACKAGE_NAME} &#8211; ${CPACK_PACKAGE_VERSION} &#8211; ${CPACK_SYSTEM_NAME}.</p>
<pre>
  CPACK_PACKAGE_INSTALL_DIRECTORY - Installation directory on the
  target system. This may be used by some CPack generators
  like NSIS to create an installation directory e.g., &quot;CMake 2.5&quot;
  below the installation prefix. All installed element will be
  put inside this directory.
</pre>
<pre>
   CPACK_PACKAGE_ICON - A branding image that will be displayed inside
   the installer (used by GUI installers).
</pre>
<pre>
  CPACK_PROJECT_CONFIG_FILE - CPack-time project CPack configuration
  file. This file included at cpack time, once per
  generator after CPack has set CPACK_GENERATOR to the actual generator
  being used. It allows per-generator setting of CPACK_* variables at
  cpack time.
</pre>
<pre>
  CPACK_RESOURCE_FILE_LICENSE - License to be embedded in the installer. It
  will typically be displayed to the user by the produced installer
  (often with an explicit &quot;Accept&quot; button, for graphical installers)
  prior to installation. This license file is NOT added to installed
  file but is used by some CPack generators like NSIS. If you want
  to install a license file (may be the same as this one)
  along with your project you must add an appropriate CMake INSTALL
  command in your CMakeLists.txt.
</pre>
<pre>
  CPACK_RESOURCE_FILE_README - ReadMe file to be embedded in the installer. It
  typically describes in some detail the purpose of the project
  during the installation. Not all CPack generators uses
  this file.
</pre>
<pre>
  CPACK_RESOURCE_FILE_WELCOME - Welcome file to be embedded in the
  installer. It welcomes users to this installer.
  Typically used in the graphical installers on Windows and Mac OS X.
</pre>
<pre>
  CPACK_MONOLITHIC_INSTALL - Disables the component-based
  installation mechanism. When set the component specification is ignored
  and all installed items are put in a single &quot;MONOLITHIC&quot; package.
  Some CPack generators do monolithic packaging by default and
  may be asked to do component packaging by setting
  CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL to 1/TRUE.
</pre>
<pre>
  CPACK_GENERATOR - List of CPack generators to use. If not
  specified, CPack will create a set of options CPACK_BINARY_&lt;GENNAME&gt; (e.g.,
  CPACK_BINARY_NSIS) allowing the user to enable/disable individual
  generators. This variable may be used on the command line
  as well as in:
</pre>
<pre>
    cpack -D CPACK_GENERATOR=&quot;ZIP;TGZ&quot; /path/to/build/tree
</pre>
<pre>
  CPACK_OUTPUT_CONFIG_FILE - The name of the CPack binary configuration
  file. This file is the CPack configuration generated by the CPack module
  for binary installers. Defaults to CPackConfig.cmake.
</pre>
<pre>
  CPACK_PACKAGE_EXECUTABLES - Lists each of the executables and associated
  text label to be used to create Start Menu shortcuts. For example,
  setting this to the list ccmake;CMake will
  create a shortcut named &quot;CMake&quot; that will execute the installed
  executable ccmake. Not all CPack generators use it (at least NSIS and
  OSXX11 do).
</pre>
<pre>
  CPACK_STRIP_FILES - List of files to be stripped. Starting with
  CMake 2.6.0 CPACK_STRIP_FILES will be a boolean variable which
  enables stripping of all files (a list of files evaluates to TRUE
  in CMake, so this change is compatible).
</pre>
<p> The following CPack variables are specific to source packages, and will not affect binary packages: </p>
<pre>
  CPACK_SOURCE_PACKAGE_FILE_NAME - The name of the source package. For
  example cmake-2.6.1.
</pre>
<pre>
  CPACK_SOURCE_STRIP_FILES - List of files in the source tree that
  will be stripped. Starting with CMake 2.6.0
  CPACK_SOURCE_STRIP_FILES will be a boolean variable which enables
  stripping of all files (a list of files evaluates to TRUE in CMake,
  so this change is compatible).
</pre>
<pre>
  CPACK_SOURCE_GENERATOR - List of generators used for the source
  packages. As with CPACK_GENERATOR, if this is not specified then
  CPack will create a set of options (e.g., CPACK_SOURCE_ZIP)
  allowing users to select which packages will be generated.
</pre>
<pre>
  CPACK_SOURCE_OUTPUT_CONFIG_FILE - The name of the CPack source
  configuration file. This file is the CPack configuration generated by the
  CPack module for source installers. Defaults to CPackSourceConfig.cmake.
</pre>
<pre>
  CPACK_SOURCE_IGNORE_FILES - Pattern of files in the source tree
  that won't be packaged when building a source package. This is a
  list of regular expression patterns (that must be properly escaped),
  e.g., /CVS/;/\.svn/;\.swp$;\.#;/#;.*~;cscope.*
</pre>
<p> The following variables are for advanced uses of CPack: </p>
<pre>
  CPACK_CMAKE_GENERATOR - What CMake generator should be used if the
  project is CMake project. Defaults to the value of CMAKE_GENERATOR
  few users will want to change this setting.
</pre>
<pre>
  CPACK_INSTALL_CMAKE_PROJECTS - List of four values that specify
  what project to install. The four values are: Build directory,
  Project Name, Project Component, Directory. If omitted, CPack will
  build an installer that installers everything.
</pre>
<pre>
  CPACK_SYSTEM_NAME - System name, defaults to the value of
  ${CMAKE_SYSTEM_NAME}.
</pre>
<pre>
  CPACK_PACKAGE_VERSION - Package full version, used internally. By
  default, this is built from CPACK_PACKAGE_VERSION_MAJOR,
  CPACK_PACKAGE_VERSION_MINOR, and CPACK_PACKAGE_VERSION_PATCH.
</pre>
<pre>
  CPACK_TOPLEVEL_TAG - Directory for the installed files.
</pre>
<pre>
  CPACK_INSTALL_COMMANDS - Extra commands to install components.
</pre>
<pre>
  CPACK_INSTALLED_DIRECTORIES - Extra directories to install.
</pre>
<pre>
   CPACK_PACKAGE_INSTALL_REGISTRY_KEY - Registry key used when
   installing this project. This is only used by installer for Windows.
   The default value is based on the installation directory.
   CPACK_CREATE_DESKTOP_LINKS - List of desktop links to create.
</pre>
<dt><code>CPackBundle</code></p>
<dd> CPack Bundle generator (Mac OS X) specific options </p>
<p> Installers built on Mac OS X using the Bundle generator use the aforementioned DragNDrop (CPACK_DMG_xxx) variables, plus the following Bundle-specific parameters (CPACK_BUNDLE_xxx). </p>
<pre>
  CPACK_BUNDLE_NAME - The name of the generated bundle. This
  appears in the OSX finder as the bundle name. Required.
</pre>
<pre>
  CPACK_BUNDLE_PLIST - Path to an OSX plist file that will be used
  for the generated bundle. This assumes that the caller has generated
  or specified their own Info.plist file. Required.
</pre>
<pre>
  CPACK_BUNDLE_ICON - Path to an OSX icon file that will be used as
  the icon for the generated bundle. This is the icon that appears in the
  OSX finder for the bundle, and in the OSX dock when the bundle is opened.
  Required.
</pre>
<pre>
  CPACK_BUNDLE_STARTUP_COMMAND - Path to a startup script. This is a path to
  an executable or script that will be run whenever an end-user double-clicks
  the generated bundle in the OSX Finder. Optional.
</pre>
<dt><code>CPackComponent</code></p>
<dd> Build binary and source package installers </p>
<p> The CPackComponent module is the module which handles the component part of CPack. See CPack module for general information about CPack. </p>
<p> For certain kinds of binary installers (including the graphical installers on Mac OS X and Windows), CPack generates installers that allow users to select individual application components to install. The contents of each of the components are identified by the COMPONENT argument of CMake&#8217;s INSTALL command. These components can be annotated with user-friendly names and descriptions, inter-component dependencies, etc., and grouped in various ways to customize the resulting installer. See the cpack_add_* commands, described below, for more information about component-specific installations. </p>
<p> Component-specific installation allows users to select specific sets of components to install during the install process. Installation components are identified by the COMPONENT argument of CMake&#8217;s INSTALL commands, and should be further described by the following CPack commands: </p>
<pre>
  CPACK_COMPONENTS_ALL - The list of component to install.
</pre>
<p> The default value of this variable is computed by CPack and contains all components defined by the project. The user may set it to only include the specified components. </p>
<pre>
  CPACK_&lt;GENNAME&gt;_COMPONENT_INSTALL - Enable/Disable component install for
  CPack generator &lt;GENNAME&gt;.
</pre>
<p> Each CPack Generator (RPM, DEB, ARCHIVE, NSIS, DMG, etc&#8230;) has a legacy default behavior. e.g. RPM builds monolithic whereas NSIS builds component. One can change the default behavior by setting this variable to 0/1 or OFF/ON. </p>
<pre>
  CPACK_COMPONENTS_GROUPING - Specify how components are grouped for multi-package
  component-aware CPack generators.
</pre>
<p> Some generators like RPM or ARCHIVE family (TGZ, ZIP, &#8230;) generates several packages files when asked for component packaging. They group the component differently depending on the value of this variable: </p>
<pre>
  - ONE_PER_GROUP (default): creates one package file per component group
  - ALL_COMPONENTS_IN_ONE : creates a single package with all (requested) component
  - IGNORE : creates one package per component, i.e. IGNORE component group
</pre>
<p> One can specify different grouping for different CPack generator by using a CPACK_PROJECT_CONFIG_FILE. </p>
<pre>
  CPACK_COMPONENT_&lt;compName&gt;_DISPLAY_NAME - The name to be displayed for a component.
  CPACK_COMPONENT_&lt;compName&gt;_DESCRIPTION - The description of a component.
  CPACK_COMPONENT_&lt;compName&gt;_GROUP - The group of a component.
  CPACK_COMPONENT_&lt;compName&gt;_DEPENDS - The dependencies (list of components)
  on which this component depends.
  CPACK_COMPONENT_&lt;compName&gt;_REQUIRED - True is this component is required.
</pre>
<p> cpack_add_component &#8211; Describes a CPack installation component named by the COMPONENT argument to a CMake INSTALL command. </p>
<p>cpack_add_component(compname<br />
                        [DISPLAY_NAME name]<br />
                        [DESCRIPTION description]<br />
                        [HIDDEN | REQUIRED | DISABLED]<br />
                        [GROUP group]<br />
                        [DEPENDS comp1 comp2&#8230;]<br />
                        [INSTALL_TYPES type1 type2&#8230;]<br />
                        [DOWNLOADED]<br />
                        [ARCHIVE_FILE filename])</p>
<p> The cmake_add_component command describes an installation component, which the user can opt to install or remove as part of the graphical installation process. compname is the name of the component, as provided to the COMPONENT argument of one or more CMake INSTALL commands. </p>
<p> DISPLAY_NAME is the displayed name of the component, used in graphical installers to display the component name. This value can be any string. </p>
<p> DESCRIPTION is an extended description of the component, used in graphical installers to give the user additional information about the component. Descriptions can span multiple lines using &quot;
&quot; as the line separator. Typically, these descriptions should be no more than a few lines long. </p>
<p> HIDDEN indicates that this component will be hidden in the graphical installer, so that the user cannot directly change whether it is installed or not. </p>
<p> REQUIRED indicates that this component is required, and therefore will always be installed. It will be visible in the graphical installer, but it cannot be unselected. (Typically, required components are shown greyed out). </p>
<p> DISABLED indicates that this component should be disabled (unselected) by default. The user is free to select this component for installation, unless it is also HIDDEN. </p>
<p> DEPENDS lists the components on which this component depends. If this component is selected, then each of the components listed must also be selected. The dependency information is encoded within the installer itself, so that users cannot install inconsistent sets of components. </p>
<p> GROUP names the component group of which this component is a part. If not provided, the component will be a standalone component, not part of any component group. Component groups are described with the cpack_add_component_group command, detailed below. </p>
<p> INSTALL_TYPES lists the installation types of which this component is a part. When one of these installations types is selected, this component will automatically be selected. Installation types are described with the cpack_add_install_type command, detailed below. </p>
<p> DOWNLOADED indicates that this component should be downloaded on-the-fly by the installer, rather than packaged in with the installer itself. For more information, see the cpack_configure_downloads command. </p>
<p> ARCHIVE_FILE provides a name for the archive file created by CPack to be used for downloaded components. If not supplied, CPack will create a file with some name based on CPACK_PACKAGE_FILE_NAME and the name of the component. See cpack_configure_downloads for more information. </p>
<p> cpack_add_component_group &#8211; Describes a group of related CPack installation components. </p>
<p>cpack_add_component_group(groupname<br />
                              [DISPLAY_NAME name]<br />
                              [DESCRIPTION description]<br />
                              [PARENT_GROUP parent]<br />
                              [EXPANDED]<br />
                              [BOLD_TITLE])</p>
<p> The cpack_add_component_group describes a group of installation components, which will be placed together within the listing of options. Typically, component groups allow the user to select/deselect all of the components within a single group via a single group-level option. Use component groups to reduce the complexity of installers with many options. groupname is an arbitrary name used to identify the group in the GROUP argument of the cpack_add_component command, which is used to place a component in a group. The name of the group must not conflict with the name of any component. </p>
<p> DISPLAY_NAME is the displayed name of the component group, used in graphical installers to display the component group name. This value can be any string. </p>
<p> DESCRIPTION is an extended description of the component group, used in graphical installers to give the user additional information about the components within that group. Descriptions can span multiple lines using &quot;
&quot; as the line separator. Typically, these descriptions should be no more than a few lines long. </p>
<p> PARENT_GROUP, if supplied, names the parent group of this group. Parent groups are used to establish a hierarchy of groups, providing an arbitrary hierarchy of groups. </p>
<p> EXPANDED indicates that, by default, the group should show up as &quot;expanded&quot;, so that the user immediately sees all of the components within the group. Otherwise, the group will initially show up as a single entry. </p>
<p> BOLD_TITLE indicates that the group title should appear in bold, to call the user&#8217;s attention to the group. </p>
<p> cpack_add_install_type &#8211; Add a new installation type containing a set of predefined component selections to the graphical installer. </p>
<pre>
  cpack_add_install_type(typename
                         [DISPLAY_NAME name])
</pre>
<p> The cpack_add_install_type command identifies a set of preselected components that represents a common use case for an application. For example, a &quot;Developer&quot; install type might include an application along with its header and library files, while an &quot;End user&quot; install type might just include the application&#8217;s executable. Each component identifies itself with one or more install types via the INSTALL_TYPES argument to cpack_add_component. </p>
<p> DISPLAY_NAME is the displayed name of the install type, which will typically show up in a drop-down box within a graphical installer. This value can be any string. </p>
<p> cpack_configure_downloads &#8211; Configure CPack to download selected components on-the-fly as part of the installation process. </p>
<p>cpack_configure_downloads(site<br />
                              [UPLOAD_DIRECTORY dirname]<br />
                              [ALL]<br />
                              [ADD_REMOVE | NO_ADD_REMOVE])</p>
<p> The cpack_configure_downloads command configures installation-time downloads of selected components. For each downloadable component, CPack will create an archive containing the contents of that component, which should be uploaded to the given site. When the user selects that component for installation, the installer will download and extract the component in place. This feature is useful for creating small installers that only download the requested components, saving bandwidth. Additionally, the installers are small enough that they will be installed as part of the normal installation process, and the &quot;Change&quot; button in Windows Add/Remove Programs control panel will allow one to add or remove parts of the application after the original installation. On Windows, the downloaded-components functionality requires the ZipDLL plug-in for NSIS, available at: </p>
<pre>
  <a rel="nofollow" href="http://nsis.sourceforge.net/ZipDLL_plug-in">http://nsis.sourceforge.net/ZipDLL_plug-in</a>
</pre>
<p> On Mac OS X, installers that download components on-the-fly can only be built and installed on system using Mac OS X 10.5 or later. </p>
<p> The site argument is a URL where the archives for downloadable components will reside, e.g., <a rel="nofollow" href="http://www.cmake.org/files/2.6.1/installer/">http://www.cmake.org/files/2.6.1/installer/</a> All of the archives produced by CPack should be uploaded to that location. </p>
<p> UPLOAD_DIRECTORY is the local directory where CPack will create the various archives for each of the components. The contents of this directory should be uploaded to a location accessible by the URL given in the site argument. If omitted, CPack will use the directory CPackUploads inside the CMake binary directory to store the generated archives. </p>
<p> The ALL flag indicates that all components be downloaded. Otherwise, only those components explicitly marked as DOWNLOADED or that have a specified ARCHIVE_FILE will be downloaded. Additionally, the ALL option implies ADD_REMOVE (unless NO_ADD_REMOVE is specified). </p>
<p> ADD_REMOVE indicates that CPack should install a copy of the installer that can be called from Windows&#8217; Add/Remove Programs dialog (via the &quot;Modify&quot; button) to change the set of installed components. NO_ADD_REMOVE turns off this behavior. This option is ignored on Mac OS X. </p>
<dt><code>CPackCygwin</code></p>
<dd> Cygwin CPack generator (Cygwin). </p>
<p> The following variable is specific to installers build on and/or for Cygwin: </p>
<pre>
   CPACK_CYGWIN_PATCH_NUMBER - The Cygwin patch number.
   FIXME: This documentation is incomplete.
   CPACK_CYGWIN_PATCH_FILE - The Cygwin patch file.
   FIXME: This documentation is incomplete.
   CPACK_CYGWIN_BUILD_SCRIPT - The Cygwin build script.
   FIXME: This documentation is incomplete.
</pre>
<dt><code>CPackDMG</code></p>
<dd> DragNDrop CPack generator (Mac OS X). </p>
<p> The following variables are specific to the DragNDrop installers built on Mac OS X: </p>
<pre>
  CPACK_DMG_VOLUME_NAME - The volume name of the generated disk
  image. Defaults to CPACK_PACKAGE_FILE_NAME.
</pre>
<pre>
  CPACK_DMG_FORMAT - The disk image format. Common values are UDRO
  (UDIF read-only), UDZO (UDIF zlib-compressed) or UDBZ (UDIF
  bzip2-compressed). Refer to <a href="//www.systutorials.com/docs/linux/man/1-hdiutil/">hdiutil</a>(1) for more information on
  other available formats.
</pre>
<pre>
  CPACK_DMG_DS_STORE - Path to a custom DS_Store file. This .DS_Store
  file e.g. can be used to specify the Finder window
  position/geometry and layout (such as hidden toolbars, placement of the
  icons etc.). This file has to be generated by the Finder (either manually or
  through OSA-script) using a normal folder from which the .DS_Store
  file can then be extracted.
</pre>
<pre>
  CPACK_DMG_BACKGROUND_IMAGE - Path to a background image file. This
  file will be used as the background for the Finder Window when the disk
  image is opened.  By default no background image is set. The background
  image is applied after applying the custom .DS_Store file.
</pre>
<pre>
  CPACK_COMMAND_HDIUTIL - Path to the <a href="//www.systutorials.com/docs/linux/man/1-hdiutil/">hdiutil</a>(1) command used to
  operate on disk image files on Mac OS X. This variable can be used
  to override the automatically detected command (or specify its
  location if the auto-detection fails to find it.)
</pre>
<pre>
  CPACK_COMMAND_SETFILE - Path to the <a href="//www.systutorials.com/docs/linux/man/1-SetFile/">SetFile</a>(1) command used to set
  extended attributes on files and directories on Mac OS X. This
  variable can be used to override the automatically detected
  command (or specify its location if the auto-detection fails to
  find it.)
</pre>
<pre>
  CPACK_COMMAND_REZ - Path to the <a href="//www.systutorials.com/docs/linux/man/1-Rez/">Rez</a>(1) command used to compile
  resources on Mac OS X. This variable can be used to override the
  automatically detected command (or specify its location if the
  auto-detection fails to find it.)
</pre>
<dt><code>CPackDeb</code></p>
<dd> The builtin (binary) CPack Deb generator (Unix only) </p>
<p> CPackDeb may be used to create Deb package using CPack. CPackDeb is a CPack generator thus it uses the CPACK_XXX variables used by CPack : <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake:CPackConfiguration.">http://www.cmake.org/Wiki/CMake:CPackConfiguration.</a> CPackDeb generator should work on any linux host but it will produce better deb package when Debian specific tools &#8216;dpkg-xxx&#8217; are usable on the build system. </p>
<p> CPackDeb has specific features which are controlled by the specifics CPACK_DEBIAN_XXX variables.You&#8217;ll find a detailed usage on the wiki: </p>
<pre>
  <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake:CPackPackageGenerators#DEB_.28UNIX_only.29">http://www.cmake.org/Wiki/CMake:CPackPackageGenerators#DEB_.28UNIX_only.29</a>
</pre>
<p> However as a handy reminder here comes the list of specific variables: </p>
<p> CPACK_DEBIAN_PACKAGE_NAME </p>
<pre>
     Mandatory : YES
     Default   : CPACK_PACKAGE_NAME (lower case)
     The debian package summary
</pre>
<p> CPACK_DEBIAN_PACKAGE_VERSION </p>
<pre>
     Mandatory : YES
     Default   : CPACK_PACKAGE_VERSION
     The debian package version
</pre>
<p> CPACK_DEBIAN_PACKAGE_ARCHITECTURE </p>
<pre>
     Mandatory : YES
     Default   : Output of dpkg --print-architecture (or i386 if dpkg is not found)
     The debian package architecture
</pre>
<p> CPACK_DEBIAN_PACKAGE_DEPENDS </p>
<pre>
     Mandatory : NO
     Default   : -
     May be used to set deb dependencies.
</pre>
<p> CPACK_DEBIAN_PACKAGE_MAINTAINER </p>
<pre>
     Mandatory : YES
     Default   : CPACK_PACKAGE_CONTACT
     The debian package maintainer
</pre>
<p> CPACK_DEBIAN_PACKAGE_DESCRIPTION </p>
<pre>
     Mandatory : YES
     Default   : CPACK_PACKAGE_DESCRIPTION_SUMMARY
     The debian package description
</pre>
<p> CPACK_DEBIAN_PACKAGE_SECTION </p>
<pre>
     Mandatory : YES
     Default   : 'devel'
     The debian package section
</pre>
<p> CPACK_DEBIAN_PACKAGE_PRIORITY </p>
<pre>
     Mandatory : YES
     Default   : 'optional'
     The debian package priority
</pre>
<p> CPACK_DEBIAN_PACKAGE_HOMEPAGE </p>
<pre>
     Mandatory : NO
     Default   : -
     The URL of the web site for this package, preferably (when applicable) the
     site from which the original source can be obtained and any additional
     upstream documentation or information may be found.
     The content of this field is a simple URL without any surrounding
     characters such as &lt;&gt;.
</pre>
<p> CPACK_DEBIAN_PACKAGE_SHLIBDEPS </p>
<pre>
     Mandatory : NO
     Default   : OFF
     May be set to ON in order to use dpkg-shlibdeps to generate
     better package dependency list.
     You may need set CMAKE_INSTALL_RPATH toi appropriate value
     if you use this feature, because if you don't dpkg-shlibdeps
     may fail to find your own shared libs.
     See <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake_RPATH_handling.">http://www.cmake.org/Wiki/CMake_RPATH_handling.</a>
</pre>
<p> CPACK_DEBIAN_PACKAGE_DEBUG </p>
<pre>
     Mandatory : NO
     Default   : -
     May be set when invoking cpack in order to trace debug information
     during CPackDeb run.
</pre>
<p> CPACK_DEBIAN_PACKAGE_PREDEPENDS </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     This field is like Depends, except that it also forces dpkg to complete installation of
     the packages named before even starting the installation of the package which declares
     the pre-dependency.
</pre>
<p> CPACK_DEBIAN_PACKAGE_ENHANCES </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     This field is similar to Suggests but works in the opposite direction.
     It is used to declare that a package can enhance the functionality of another package.
</pre>
<p> CPACK_DEBIAN_PACKAGE_BREAKS </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     When one binary package declares that it breaks another, dpkg will refuse to allow the
     package which declares Breaks be installed unless the broken package is deconfigured first,
     and it will refuse to allow the broken package to be reconfigured.
</pre>
<p> CPACK_DEBIAN_PACKAGE_CONFLICTS </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     When one binary package declares a conflict with another using a Conflicts field,
     dpkg will refuse to allow them to be installed on the system at the same time.
</pre>
<p> CPACK_DEBIAN_PACKAGE_PROVIDES </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     A virtual package is one which appears in the Provides control field of another package.
</pre>
<p> CPACK_DEBIAN_PACKAGE_REPLACES </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     Packages can declare in their control file that they should overwrite
     files in certain other packages, or completely replace other packages.
</pre>
<p> CPACK_DEBIAN_PACKAGE_RECOMMENDS </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     Allows packages to declare a strong, but not absolute, dependency on other packages.
</pre>
<p> CPACK_DEBIAN_PACKAGE_SUGGESTS </p>
<pre>
     Mandatory : NO
     Default   : -
     see <a rel="nofollow" href="http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps">http://www.debian.org/doc/debian-policy/ch-relationships.html#s-binarydeps</a>
     Allows packages to declare a suggested package install grouping.
</pre>
<p> CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA </p>
<p>     Mandatory : NO<br />
     Default   : &#8211;<br />
     This variable allow advanced user to add custom script to the control.tar.gz<br />
     Typical usage is for conffiles, postinst, postrm, prerm.<br />
     Usage: set(CPACK_DEBIAN_PACKAGE_CONTROL_EXTRA<br />
            &#8220;${CMAKE_CURRENT_SOURCE_DIR/prerm;${CMAKE_CURRENT_SOURCE_DIR}/postrm&#8221;)</p>
<dt><code>CPackNSIS</code></p>
<dd> CPack NSIS generator specific options </p>
<p> The following variables are specific to the graphical installers built on Windows using the Nullsoft Installation System. </p>
<p>CPACK_NSIS_INSTALL_ROOT &#8211; The default installation directory presented<br />
                                  to the end user by the NSIS installer is under this root dir.The full<br />
                                      directory presented to the end user is : ${CPACK_NSIS_INSTALL_ROOT} /<br />
                              $<br />
{<br />
    CPACK_PACKAGE_INSTALL_DIRECTORY<br />
}</p>
<pre>
   CPACK_NSIS_MUI_ICON - An icon filename.
   The name of a *.ico file used as the main icon for the generated
   install program.
</pre>
<pre>
   CPACK_NSIS_MUI_UNIICON - An icon filename.
   The name of a *.ico file used as the main icon for the generated
   uninstall program.
</pre>
<pre>
   CPACK_NSIS_INSTALLER_MUI_ICON_CODE - undocumented.
</pre>
<pre>
   CPACK_NSIS_EXTRA_PREINSTALL_COMMANDS - Extra NSIS commands that
   will be added to the beginning of the install Section, before your
   install tree is available on the target system.
</pre>
<pre>
   CPACK_NSIS_EXTRA_INSTALL_COMMANDS - Extra NSIS commands that
   will be added to the end of the install Section, after your
   install tree is available on the target system.
</pre>
<pre>
   CPACK_NSIS_EXTRA_UNINSTALL_COMMANDS - Extra NSIS commands that will
   be added to the uninstall Section, before your install tree is
   removed from the target system.
</pre>
<pre>
   CPACK_NSIS_COMPRESSOR - The arguments that will be passed to the
   NSIS SetCompressor command.
</pre>
<pre>
   CPACK_NSIS_ENABLE_UNINSTALL_BEFORE_INSTALL - Ask about uninstalling
   previous versions first.
   If this is set to &quot;ON&quot;, then an installer will look for previous
   installed versions and if one is found, ask the user whether to
   uninstall it before proceeding with the install.
</pre>
<pre>
   CPACK_NSIS_MODIFY_PATH - Modify PATH toggle.
   If this is set to &quot;ON&quot;, then an extra page
   will appear in the installer that will allow the user to choose
   whether the program directory should be added to the system PATH
   variable.
</pre>
<pre>
   CPACK_NSIS_DISPLAY_NAME - The display name string that appears in
   the Windows Add/Remove Program control panel
</pre>
<pre>
   CPACK_NSIS_PACKAGE_NAME - The title displayed at the top of the
   installer.
</pre>
<pre>
   CPACK_NSIS_INSTALLED_ICON_NAME - A path to the executable that
   contains the installer icon.
</pre>
<pre>
   CPACK_NSIS_HELP_LINK - URL to a web site providing assistance in
   installing your application.
</pre>
<pre>
   CPACK_NSIS_URL_INFO_ABOUT - URL to a web site providing more
   information about your application.
</pre>
<pre>
   CPACK_NSIS_CONTACT - Contact information for questions and comments
   about the installation process.
</pre>
<pre>
   CPACK_NSIS_CREATE_ICONS_EXTRA - Additional NSIS commands for
   creating start menu shortcuts.
</pre>
<pre>
   CPACK_NSIS_DELETE_ICONS_EXTRA -Additional NSIS commands to
   uninstall start menu shortcuts.
</pre>
<pre>
   CPACK_NSIS_EXECUTABLES_DIRECTORY - Creating NSIS start menu links
   assumes that they are in 'bin' unless this variable is set.
   For example, you would set this to 'exec' if your executables are
   in an exec directory.
</pre>
<p>CPACK_NSIS_MUI_FINISHPAGE_RUN &#8211; Specify an executable to add an option to run on the finish page of the NSIS installer.CPACK_NSIS_MENU_LINKS &#8211; Specify links in[application] menu.This should contain a list of pair &#8220;link&#8221;<br />
                                                                                                                                                                                                                     &#8220;link name&#8221;.The link may be an URL or<br />
    a path relative to installation prefix.Like : set(CPACK_NSIS_MENU_LINKS<br />
                                                      &#8220;doc/cmake- [at] CMake_VERSION_MAJOR@.@CMake_VERSION_MINOR@/cmake.html&#8221;<br />
                                                      &#8220;CMake Help&#8221;<br />
                                                      &#8220;http://www.cmake.org&#8221;<br />
                                                      &#8220;CMake Web Site&#8221;)</p>
<dt><code>CPackPackageMaker</code></p>
<dd> PackageMaker CPack generator (Mac OS X). </p>
<p> The following variable is specific to installers built on Mac OS X using PackageMaker: </p>
<pre>
  CPACK_OSX_PACKAGE_VERSION - The version of Mac OS X that the
  resulting PackageMaker archive should be compatible with. Different
  versions of Mac OS X support different
  features. For example, CPack can only build component-based
  installers for Mac OS X 10.4 or newer, and can only build
  installers that download component son-the-fly for Mac OS X 10.5
  or newer. If left blank, this value will be set to the minimum
  version of Mac OS X that supports the requested features. Set this
  variable to some value (e.g., 10.4) only if you want to guarantee
  that your installer will work on that version of Mac OS X, and
  don't mind missing extra features available in the installer
  shipping with later versions of Mac OS X.
</pre>
<dt><code>CPackRPM</code></p>
<dd> The builtin (binary) CPack RPM generator (Unix only) </p>
<p> CPackRPM may be used to create RPM package using CPack. CPackRPM is a CPack generator thus it uses the CPACK_XXX variables used by CPack : <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake:CPackConfiguration">http://www.cmake.org/Wiki/CMake:CPackConfiguration</a> </p>
<p> However CPackRPM has specific features which are controlled by the specifics CPACK_RPM_XXX variables. CPackRPM is a component aware generator so when CPACK_RPM_COMPONENT_INSTALL is ON some more CPACK_RPM_&lt;ComponentName&gt;_XXXX variables may be used in order to have component specific values. Note however that &lt;componentName&gt; refers to the **grouping name**. This may be either a component name or a component GROUP name. Usually those vars correspond to RPM spec file entities, one may find information about spec files here <a rel="nofollow" href="http://www.rpm.org/wiki/Docs.">http://www.rpm.org/wiki/Docs.</a> You&#8217;ll find a detailed usage of CPackRPM on the wiki: </p>
<pre>
  <a rel="nofollow" href="http://www.cmake.org/Wiki/CMake:CPackPackageGenerators#RPM_.28Unix_Only.29">http://www.cmake.org/Wiki/CMake:CPackPackageGenerators#RPM_.28Unix_Only.29</a>
</pre>
<p> However as a handy reminder here comes the list of specific variables: </p>
<p>CPACK_RPM_PACKAGE_SUMMARY &#8211; The RPM package summary.Mandatory : YES Default : CPACK_PACKAGE_DESCRIPTION_SUMMARY CPACK_RPM_PACKAGE_NAME &#8211; The RPM package name.Mandatory : YES Default : CPACK_PACKAGE_NAME CPACK_RPM_PACKAGE_VERSION &#8211; The RPM package version.Mandatory : YES Default : CPACK_PACKAGE_VERSION CPACK_RPM_PACKAGE_ARCHITECTURE &#8211; The RPM package architecture.Mandatory : NO Default : -This may be set to &#8220;noarch&#8221; if you know you are building a noarch package.CPACK_RPM_PACKAGE_RELEASE &#8211; The RPM package release.Mandatory : YES Default : 1 This is the numbering of the RPM package itself, i.e.the version of the packaging and not the version of the content(see CPACK_RPM_PACKAGE_VERSION).One may change the default value if the previous packaging was buggy and / or you want to put here a fancy Linux distro specific numbering.CPACK_RPM_PACKAGE_LICENSE &#8211; The RPM package license policy.Mandatory : YES Default : &#8220;unknown&#8221; CPACK_RPM_PACKAGE_GROUP &#8211; The RPM package group.Mandatory : YES Default : &#8220;unknown&#8221; CPACK_RPM_PACKAGE_VENDOR &#8211; The RPM package vendor.Mandatory : YES Default : CPACK_PACKAGE_VENDOR if set or &#8220;unknown&#8221; CPACK_RPM_PACKAGE_URL &#8211; The projects URL.Mandatory : NO Default : -CPACK_RPM_PACKAGE_DESCRIPTION &#8211; RPM package description.Mandatory : YES Default : CPACK_PACKAGE_DESCRIPTION_FILE if set or &#8220;no package description available&#8221; CPACK_RPM_COMPRESSION_TYPE &#8211; RPM compression type.Mandatory : NO Default : -May be used to override RPM compression type to be used to build the RPM.For example some Linux distribution now default to lzma or xz compression whereas older cannot use such RPM.Using this one can enforce compression type to be used.Possible value are : lzma, xz, bzip2 and gzip.CPACK_RPM_PACKAGE_REQUIRES &#8211; RPM spec requires field.Mandatory : NO Default : -May be used to set RPM dependencies(requires).Note that you must enclose the complete requires string between quotes,<br />
     for example:<br />
     set(CPACK_RPM_PACKAGE_REQUIRES &#8220;python &gt;= 2.5.0, cmake &gt;= 2.8&#8221;)<br />
     The required package list of an RPM file could be printed with<br />
     rpm -qp &#8211;requires file.rpm<br />
  CPACK_RPM_PACKAGE_SUGGESTS &#8211; RPM spec suggest field.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to set weak RPM dependencies (suggests).<br />
     Note that you must enclose the complete requires string between quotes.<br />
  CPACK_RPM_PACKAGE_PROVIDES &#8211; RPM spec provides field.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to set RPM dependencies (provides).<br />
     The provided package list of an RPM file could be printed with<br />
     rpm -qp &#8211;provides file.rpm<br />
  CPACK_RPM_PACKAGE_OBSOLETES &#8211; RPM spec obsoletes field.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to set RPM packages that are obsoleted by this one.<br />
  CPACK_RPM_PACKAGE_RELOCATABLE &#8211; build a relocatable RPM.<br />
     Mandatory : NO<br />
     Default   : CPACK_PACKAGE_RELOCATABLE<br />
     If this variable is set to TRUE or ON CPackRPM will try<br />
     to build a relocatable RPM package. A relocatable RPM may<br />
     be installed using rpm &#8211;prefix or &#8211;relocate in order to<br />
     install it at an alternate place see rpm(8).<br />
     Note that currently this may fail if CPACK_SET_DESTDIR is set to ON.<br />
     If CPACK_SET_DESTDIR is set then you will get a warning message<br />
     but if there is file installed with absolute path you&#8217;ll get<br />
     unexpected behavior.<br />
  CPACK_RPM_SPEC_INSTALL_POST &#8211; [deprecated].<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     This way of specifying post-install script is deprecated use<br />
     CPACK_RPM_POST_INSTALL_SCRIPT_FILE<br />
     May be used to set an RPM post-install command inside the spec file.<br />
     For example setting it to &#8220;/bin/true&#8221; may be used to prevent<br />
     rpmbuild to strip binaries.<br />
  CPACK_RPM_SPEC_MORE_DEFINE &#8211; RPM extended spec definitions lines.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to add any %define lines to the generated spec file.<br />
  CPACK_RPM_PACKAGE_DEBUG &#8211; Toggle CPackRPM debug output.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be set when invoking cpack in order to trace debug information<br />
     during CPack RPM run. For example you may launch CPack like this<br />
     cpack -D CPACK_RPM_PACKAGE_DEBUG=1 -G RPM<br />
  CPACK_RPM_USER_BINARY_SPECFILE &#8211; A user provided spec file.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be set by the user in order to specify a USER binary spec file<br />
     to be used by CPackRPM instead of generating the file.<br />
     The specified file will be processed by configure_file( @ONLY).<br />
     One can provide a component specific file by setting<br />
     CPACK_RPM_&lt;componentName&gt;_USER_BINARY_SPECFILE.<br />
  CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE &#8211; Spec file template.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     If set CPack will generate a template for USER specified binary<br />
     spec file and stop with an error. For example launch CPack like this<br />
     cpack -D CPACK_RPM_GENERATE_USER_BINARY_SPECFILE_TEMPLATE=1 -G RPM<br />
     The user may then use this file in order to hand-craft is own<br />
     binary spec file which may be used with CPACK_RPM_USER_BINARY_SPECFILE.<br />
  CPACK_RPM_PRE_INSTALL_SCRIPT_FILE<br />
  CPACK_RPM_PRE_UNINSTALL_SCRIPT_FILE<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to embed a pre (un)<br />
     installation script in the spec file.The refered script file(s)<br />
     will be read and directly<br />
                 put after the %<br />
             pre or<br />
         % preun section<br />
                 If CPACK_RPM_COMPONENT_INSTALL is set to ON<br />
                 the(un)install script for<br />
     each component can be overridden with<br />
     CPACK_RPM_&lt;COMPONENT&gt;_PRE_INSTALL_SCRIPT_FILE and<br />
     CPACK_RPM_&lt;COMPONENT&gt;_PRE_UNINSTALL_SCRIPT_FILE<br />
     One may verify which scriptlet has been included with<br />
      rpm -qp &#8211;scripts  package.rpm<br />
  CPACK_RPM_POST_INSTALL_SCRIPT_FILE<br />
  CPACK_RPM_POST_UNINSTALL_SCRIPT_FILE<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to embed a post (un)<br />
     installation script in the spec file.The refered script file(s)<br />
     will be read and directly<br />
                 put after the %<br />
             post or<br />
         % postun section<br />
                 If CPACK_RPM_COMPONENT_INSTALL is set to ON<br />
                 the(un)install script for<br />
     each component can be overridden with<br />
     CPACK_RPM_&lt;COMPONENT&gt;_POST_INSTALL_SCRIPT_FILE and<br />
     CPACK_RPM_&lt;COMPONENT&gt;_POST_UNINSTALL_SCRIPT_FILE<br />
     One may verify which scriptlet has been included with<br />
      rpm -qp &#8211;scripts  package.rpm<br />
  CPACK_RPM_USER_FILELIST<br />
  CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to explicitly specify %(&lt;directive&gt;) file line<br />
     in the spec file. Like %config(noreplace) or any other directive<br />
     that be found in the %files section. Since CPackRPM is generating<br />
     the list of files (and directories) the user specified files of<br />
     the CPACK_RPM_&lt;COMPONENT&gt;_USER_FILELIST list will be removed from the generated list.<br />
  CPACK_RPM_CHANGELOG_FILE &#8211; RPM changelog file.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to embed a changelog in the spec file.<br />
     The refered file will be read and directly put after the %changelog<br />
     section.<br />
  CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST &#8211; list of path to be excluded.<br />
     Mandatory : NO<br />
     Default   : /etc /etc/init.d /usr /usr/share /usr/share/doc /usr/bin /usr/lib /usr/lib64 /usr/include<br />
     May be used to exclude path (directories or files) from the auto-generated<br />
     list of paths discovered by CPack RPM. The defaut value contains a reasonable<br />
     set of values if the variable is not defined by the user. If the variable<br />
     is defined by the user then CPackRPM will NOT any of the default path.<br />
     If you want to add some path to the default list then you can use<br />
     CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION variable.<br />
  CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST_ADDITION &#8211; additional list of path to be excluded.<br />
     Mandatory : NO<br />
     Default   : &#8211;<br />
     May be used to add more exclude path (directories or files) from the initial<br />
     default list of excluded paths. See CPACK_RPM_EXCLUDE_FROM_AUTO_FILELIST.</p>
<dt><code>CPackWIX</code></p>
<dd> CPack WiX generator specific options </p>
<p> The following variables are specific to the installers built on Windows using WiX. </p>
<pre>
  CPACK_WIX_UPGRADE_GUID - Upgrade GUID (Product/@UpgradeCode)
</pre>
<p> Will be automatically generated unless explicitly provided. </p>
<p> It should be explicitly set to a constant generated gloabally unique identifier (GUID) to allow your installers to replace existing installations that use the same GUID. </p>
<p> You may for example explicitly set this variable in your CMakeLists.txt to the value that has been generated per default. You should not use GUIDs that you did not generate yourself or which may belong to other projects. </p>
<p> A GUID shall have the following fixed length syntax: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX </p>
<pre>
  (each X represents an uppercase hexadecimal digit)
  CPACK_WIX_PRODUCT_GUID - Product GUID (Product/@Id)
</pre>
<p> Will be automatically generated unless explicitly provided. </p>
<p> If explicitly provided this will set the Product Id of your installer. </p>
<p> The installer will abort if it detects a pre-existing installation that uses the same GUID. </p>
<p> The GUID shall use the syntax described for CPACK_WIX_UPGRADE_GUID. </p>
<pre>
  CPACK_WIX_LICENSE_RTF - RTF License File
</pre>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .rtf extension it is used as-is. </p>
<p> If CPACK_RESOURCE_FILE_LICENSE has an .txt extension it is implicitly converted to RTF by the WiX Generator. </p>
<p> With CPACK_WIX_LICENSE_RTF you can override the license file used by the WiX Generator in case CPACK_RESOURCE_FILE_LICENSE is in an unsupported format or the .txt -&gt; .rtf conversion does not work as expected. </p>
<p> CPACK_WIX_PRODUCT_ICON &#8211; The Icon shown next to the program name in Add/Remove programs. </p>
<p> If set, this icon is used in place of the default icon. </p>
<p> CPACK_WIX_UI_BANNER &#8211; The bitmap will appear at the top of all installer pages other than the welcome and completion dialogs. </p>
<p> If set, this image will replace the default banner image. </p>
<p> This image must be 493 by 58 pixels. </p>
<p> CPACK_WIX_UI_DIALOG &#8211; Background bitmap used on the welcome and completion dialogs. </p>
<p> If this variable is set, the installer will replace the default dialog image. </p>
<p> This image must be 493 by 312 pixels. </p>
<p> CPACK_WIX_PROGRAM_MENU_FOLDER &#8211; Start menu folder name for launcher. </p>
<p> If this variable is not set, it will be initialized with CPACK_PACKAGE_NAME </p>
<p> CPACK_WIX_CULTURES &#8211; Language(s) of the installer </p>
<p> Languages are compiled into the WixUI extension library. To use them, simply provide the name of the culture. If you specify more than one culture identifier in a comma or semicolon delimited list, the first one that is found will be used. You can find a list of supported languages at: <a rel="nofollow" href="http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm">http://wix.sourceforge.net/manual-wix3/WixUI_localization.htm</a> </p>
<p> CPACK_WIX_TEMPLATE &#8211; Template file for WiX generation </p>
<p> If this variable is set, the specified template will be used to generate the WiX wxs file. This should be used if further customization of the output is required. </p>
<p> If this variable is not set, the default MSI template included with CMake will be used. </p>
<dt><code>CTest</code></p>
<dd> Configure a project for testing with CTest/CDash </p>
<p> Include this module in the top CMakeLists.txt file of a project to enable testing with CTest and dashboard submissions to CDash: </p>
<pre>
   project(MyProject)
   ...
   include(CTest)
</pre>
<p> The module automatically creates a BUILD_TESTING option that selects whether to enable testing support (ON by default). After including the module, use code like </p>
<pre>
   if(BUILD_TESTING)
     # ... CMake code to create tests ...
   endif()
</pre>
<p> to creating tests when testing is enabled. </p>
<p> To enable submissions to a CDash server, create a CTestConfig.cmake file at the top of the project with content such as </p>
<pre>
   set(CTEST_PROJECT_NAME &quot;MyProject&quot;)
   set(CTEST_NIGHTLY_START_TIME &quot;01:00:00 UTC&quot;)
   set(CTEST_DROP_METHOD &quot;http&quot;)
   set(CTEST_DROP_SITE &quot;my.cdash.org&quot;)
   set(CTEST_DROP_LOCATION &quot;/submit.php?project=MyProject&quot;)
   set(CTEST_DROP_SITE_CDASH TRUE)
</pre>
<p> (the CDash server can provide the file to a project administrator who configures &#8216;MyProject&#8217;). Settings in the config file are shared by both this CTest module and the CTest command-line tool&#8217;s dashboard script mode (ctest -S). </p>
<p> While building a project for submission to CDash, CTest scans the build output for errors and warnings and reports them with surrounding context from the build log. This generic approach works for all build tools, but does not give details about the command invocation that produced a given problem. One may get more detailed reports by adding </p>
<pre>
   set(CTEST_USE_LAUNCHERS 1)
</pre>
<p> to the CTestConfig.cmake file. When this option is enabled, the CTest module tells CMake&#8217;s Makefile generators to invoke every command in the generated build system through a CTest launcher program. (Currently the CTEST_USE_LAUNCHERS option is ignored on non-Makefile generators.) During a manual build each launcher transparently runs the command it wraps. During a CTest-driven build for submission to CDash each launcher reports detailed information when its command fails or warns. (Setting CTEST_USE_LAUNCHERS in CTestConfig.cmake is convenient, but also adds the launcher overhead even for manual builds. One may instead set it in a CTest dashboard script and add it to the CMake cache for the build tree.) </p>
<dt><code>CTestScriptMode</code></p>
<dd>
<p> This file is read by ctest in script mode (-S) </p>
<dt><code>CTestUseLaunchers</code></p>
<dd> Set the RULE_LAUNCH_* global properties when CTEST_USE_LAUNCHERS is on. </p>
<p> CTestUseLaunchers is automatically included when you include(CTest). However, it is split out into its own module file so projects can use the CTEST_USE_LAUNCHERS functionality independently. </p>
<p> To use launchers, set CTEST_USE_LAUNCHERS to ON in a ctest -S dashboard script, and then also set it in the cache of the configured project. Both cmake and ctest need to know the value of it for the launchers to work properly. CMake needs to know in order to generate proper build rules, and ctest, in order to produce the proper error and warning analysis. </p>
<p> For convenience, you may set the ENV variable CTEST_USE_LAUNCHERS_DEFAULT in your ctest -S script, too. Then, as long as your CMakeLists uses include(CTest) or include(CTestUseLaunchers), it will use the value of the ENV variable to initialize a CTEST_USE_LAUNCHERS cache variable. This cache variable initialization only occurs if CTEST_USE_LAUNCHERS is not already defined. </p>
<dt><code>CheckCCompilerFlag</code></p>
<dd> Check whether the C compiler supports a given flag. </p>
<p> CHECK_C_COMPILER_FLAG(&lt;flag&gt; &lt;var&gt;) </p>
<pre>
  &lt;flag&gt; - the compiler flag
  &lt;var&gt;  - variable to store the result
</pre>
<p> This internally calls the check_c_source_compiles macro and sets CMAKE_REQUIRED_DEFINITIONS to &lt;flag&gt;. See help for CheckCSourceCompiles for a listing of variables that can otherwise modify the build. The result only tells that the compiler does not give an error message when it encounters the flag. If the flag has any effect or even a specific one is beyond the scope of this module. </p>
<dt><code>CheckCSourceCompiles</code></p>
<dd> Check if given C source compiles and links into an executable </p>
<p> CHECK_C_SOURCE_COMPILES(&lt;code&gt; &lt;var&gt; [FAIL_REGEX &lt;fail-regex&gt;]) </p>
<pre>
  &lt;code&gt;       - source code to try to compile, must define 'main'
  &lt;var&gt;        - variable to store whether the source code compiled
  &lt;fail-regex&gt; - fail if test output matches this regex
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCSourceRuns</code></p>
<dd> Check if the given C source code compiles and runs. </p>
<p> CHECK_C_SOURCE_RUNS(&lt;code&gt; &lt;var&gt;) </p>
<pre>
  &lt;code&gt;   - source code to try to compile
  &lt;var&gt;    - variable to store the result
             (1 for success, empty for failure)
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXCompilerFlag</code></p>
<dd> Check whether the CXX compiler supports a given flag. </p>
<p> CHECK_CXX_COMPILER_FLAG(&lt;flag&gt; &lt;var&gt;) </p>
<pre>
  &lt;flag&gt; - the compiler flag
  &lt;var&gt;  - variable to store the result
</pre>
<p> This internally calls the check_cxx_source_compiles macro and sets CMAKE_REQUIRED_DEFINITIONS to &lt;flag&gt;. See help for CheckCXXSourceCompiles for a listing of variables that can otherwise modify the build. The result only tells that the compiler does not give an error message when it encounters the flag. If the flag has any effect or even a specific one is beyond the scope of this module. </p>
<dt><code>CheckCXXSourceCompiles</code></p>
<dd> Check if given C++ source compiles and links into an executable </p>
<p> CHECK_CXX_SOURCE_COMPILES(&lt;code&gt; &lt;var&gt; [FAIL_REGEX &lt;fail-regex&gt;]) </p>
<pre>
  &lt;code&gt;       - source code to try to compile, must define 'main'
  &lt;var&gt;        - variable to store whether the source code compiled
  &lt;fail-regex&gt; - fail if test output matches this regex
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXSourceRuns</code></p>
<dd> Check if the given C++ source code compiles and runs. </p>
<p> CHECK_CXX_SOURCE_RUNS(&lt;code&gt; &lt;var&gt;) </p>
<pre>
  &lt;code&gt;   - source code to try to compile
  &lt;var&gt;    - variable to store the result
             (1 for success, empty for failure)
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXSymbolExists</code></p>
<dd> Check if a symbol exists as a function, variable, or macro in C++ </p>
<p> CHECK_CXX_SYMBOL_EXISTS(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;symbol&gt; is available after including given header &lt;files&gt; and store the result in a &lt;variable&gt;. Specify the list of files in one argument as a semicolon-separated list. CHECK_CXX_SYMBOL_EXISTS() can be used to check in C++ files, as opposed to CHECK_SYMBOL_EXISTS(), which works only for C. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking. If the symbol is a type or enum value it will not be recognized (consider using CheckTypeSize or CheckCSourceCompiles). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckFortranFunctionExists</code></p>
<dd> macro which checks if the Fortran function exists </p>
<p> CHECK_FORTRAN_FUNCTION_EXISTS(FUNCTION VARIABLE) </p>
<pre>
  FUNCTION - the name of the Fortran function
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckFunctionExists</code></p>
<dd> Check if a C function can be linked </p>
<p> CHECK_FUNCTION_EXISTS(&lt;function&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;function&gt; is provided by libraries on the system and store the result in a &lt;variable&gt;. This does not verify that any system header file declares the function, only that it can be found at link time (consider using CheckSymbolExists). </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckIncludeFile</code></p>
<dd> macro which checks the include file exists. </p>
<p> CHECK_INCLUDE_FILE(INCLUDE VARIABLE) </p>
<pre>
  INCLUDE  - name of include file
  VARIABLE - variable to return result
</pre>
<p> an optional third argument is the CFlags to add to the compile line or you can use CMAKE_REQUIRED_FLAGS </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckIncludeFileCXX</code></p>
<dd> Check if the include file exists. </p>
<pre>
  CHECK_INCLUDE_FILE_CXX(INCLUDE VARIABLE)
</pre>
<pre>
  INCLUDE  - name of include file
  VARIABLE - variable to return result
</pre>
<p> An optional third argument is the CFlags to add to the compile line or you can use CMAKE_REQUIRED_FLAGS. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckIncludeFiles</code></p>
<dd> Check if the files can be included </p>
<p> CHECK_INCLUDE_FILES(INCLUDE VARIABLE) </p>
<pre>
  INCLUDE  - list of files to include
  VARIABLE - variable to return result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckLanguage</code></p>
<dd> Check if a language can be enabled </p>
<p> Usage: </p>
<pre>
  check_language(&lt;lang&gt;)
</pre>
<p> where &lt;lang&gt; is a language that may be passed to enable_language() such as &quot;Fortran&quot;. If CMAKE_&lt;lang&gt;_COMPILER is already defined the check does nothing. Otherwise it tries enabling the language in a test project. The result is cached in CMAKE_&lt;lang&gt;_COMPILER as the compiler that was found, or NOTFOUND if the language cannot be enabled. </p>
<p> Example: </p>
<pre>
  check_language(Fortran)
  if(CMAKE_Fortran_COMPILER)
    enable_language(Fortran)
  else()
    message(STATUS &quot;No Fortran support&quot;)
  endif()
</pre>
<dt><code>CheckLibraryExists</code></p>
<dd> Check if the function exists. </p>
<p> CHECK_LIBRARY_EXISTS (LIBRARY FUNCTION LOCATION VARIABLE) </p>
<pre>
  LIBRARY  - the name of the library you are looking for
  FUNCTION - the name of the function
  LOCATION - location where the library should be found
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckPrototypeDefinition</code></p>
<dd> Check if the protoype we expect is correct. </p>
<p> check_prototype_definition(FUNCTION PROTOTYPE RETURN HEADER VARIABLE) </p>
<pre>
  FUNCTION - The name of the function (used to check if prototype exists)
  PROTOTYPE- The prototype to check.
  RETURN - The return value of the function.
  HEADER - The header files required.
  VARIABLE - The variable to store the result.
</pre>
<p> Example: </p>
<p>check_prototype_definition(getpwent_r<br />
                           &#8220;struct passwd *getpwent_r(struct passwd *src, char *buf, int buflen)&#8221;<br />
                           &#8220;NULL&#8221;<br />
                           &#8220;unistd.h;pwd.h&#8221; SOLARIS_GETPWENT_R)</p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckStructHasMember</code></p>
<dd> Check if the given struct or class has the specified member variable </p>
<p> CHECK_STRUCT_HAS_MEMBER (STRUCT MEMBER HEADER VARIABLE) </p>
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
<p> Example: CHECK_STRUCT_HAS_MEMBER(&quot;struct timeval&quot; tv_sec sys/select.h HAVE_TIMEVAL_TV_SEC) </p>
<dt><code>CheckSymbolExists</code></p>
<dd> Check if a symbol exists as a function, variable, or macro </p>
<p> CHECK_SYMBOL_EXISTS(&lt;symbol&gt; &lt;files&gt; &lt;variable&gt;) </p>
<p> Check that the &lt;symbol&gt; is available after including given header &lt;files&gt; and store the result in a &lt;variable&gt;. Specify the list of files in one argument as a semicolon-separated list. </p>
<p> If the header files define the symbol as a macro it is considered available and assumed to work. If the header files declare the symbol as a function or variable then the symbol must also be available for linking. If the symbol is a type or enum value it will not be recognized (consider using CheckTypeSize or CheckCSourceCompiles). If the check needs to be done in C++, consider using CHECK_CXX_SYMBOL_EXISTS(), which does the same as CHECK_SYMBOL_EXISTS(), but in C++. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckTypeSize</code></p>
<dd> Check sizeof a type </p>
<pre>
  CHECK_TYPE_SIZE(TYPE VARIABLE [BUILTIN_TYPES_ONLY])
</pre>
<p> Check if the type exists and determine its size. On return, &quot;HAVE_${VARIABLE}&quot; holds the existence of the type, and &quot;${VARIABLE}&quot; holds one of the following: </p>
<pre>
   &lt;size&gt; = type has non-zero size &lt;size&gt;
   &quot;0&quot;    = type has arch-dependent size (see below)
   &quot;&quot;     = type does not exist
</pre>
<p> Furthermore, the variable &quot;${VARIABLE}_CODE&quot; holds C preprocessor code to define the macro &quot;${VARIABLE}&quot; to the size of the type, or leave the macro undefined if the type does not exist. </p>
<p> The variable &quot;${VARIABLE}&quot; may be &quot;0&quot; when CMAKE_OSX_ARCHITECTURES has multiple architectures for building OS X universal binaries. This indicates that the type size varies across architectures. In this case &quot;${VARIABLE}_CODE&quot; contains C preprocessor tests mapping from each architecture macro to the corresponding type size. The list of architecture macros is stored in &quot;${VARIABLE}_KEYS&quot;, and the value for each key is stored in &quot;${VARIABLE}-${KEY}&quot;. </p>
<p> If the BUILTIN_TYPES_ONLY option is not given, the macro checks for headers &lt;sys/types.h&gt;, &lt;stdint.h&gt;, and &lt;stddef.h&gt;, and saves results in HAVE_SYS_TYPES_H, HAVE_STDINT_H, and HAVE_STDDEF_H. The type size check automatically includes the available headers, thus supporting checks of types defined in the headers. </p>
<p> Despite the name of the macro you may use it to check the size of more complex expressions, too. To check e.g. for the size of a struct member you can do something like this: </p>
<pre>
  check_type_size(&quot;((struct something*)0)-&gt;member&quot; SIZEOF_MEMBER)
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
  CMAKE_EXTRA_INCLUDE_FILES = list of extra headers to include
</pre>
<dt><code>CheckVariableExists</code></p>
<dd> Check if the variable exists. </p>
<pre>
  CHECK_VARIABLE_EXISTS(VAR VARIABLE)
</pre>
<pre>
  VAR      - the name of the variable
  VARIABLE - variable to store the result
</pre>
<p> This macro is only for C variables. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>Dart</code></p>
<dd> Configure a project for testing with CTest or old Dart Tcl Client </p>
<p> This file is the backwards-compatibility version of the CTest module. It supports using the old Dart 1 Tcl client for driving dashboard submissions as well as testing with CTest. This module should be included in the CMakeLists.txt file at the top of a project. Typical usage: </p>
<pre>
  include(Dart)
  if(BUILD_TESTING)
    # ... testing related CMake code ...
  endif()
</pre>
<p> The BUILD_TESTING option is created by the Dart module to determine whether testing support should be enabled. The default is ON. </p>
<dt><code>DeployQt4</code></p>
<dd> Functions to help assemble a standalone Qt4 executable. </p>
<p> A collection of CMake utility functions useful for deploying Qt4 executables. </p>
<p> The following functions are provided by this module: </p>
<pre>
   write_qt4_conf
   resolve_qt4_paths
   fixup_qt4_executable
   install_qt4_plugin_path
   install_qt4_plugin
   install_qt4_executable
</pre>
<p> Requires CMake 2.6 or greater because it uses function and PARENT_SCOPE. Also depends on BundleUtilities.cmake. </p>
<pre>
  WRITE_QT4_CONF(&lt;qt_conf_dir&gt; &lt;qt_conf_contents&gt;)
</pre>
<p> Writes a qt.conf file with the &lt;qt_conf_contents&gt; into &lt;qt_conf_dir&gt;. </p>
<pre>
  RESOLVE_QT4_PATHS(&lt;paths_var&gt; [&lt;executable_path&gt;])
</pre>
<p> Loop through &lt;paths_var&gt; list and if any don&#8217;t exist resolve them relative to the &lt;executable_path&gt; (if supplied) or the CMAKE_INSTALL_PREFIX. </p>
<pre>
  FIXUP_QT4_EXECUTABLE(&lt;executable&gt; [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt;])
</pre>
<p> Copies Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. </p>
<p> &lt;executable&gt; should point to the executable to be fixed-up. </p>
<p> &lt;qtplugins&gt; should contain a list of the names or paths of any Qt plugins to be installed. </p>
<p> &lt;libs&gt; will be passed to BundleUtilities and should be a list of any already installed plugins, libraries or executables to also be fixed-up. </p>
<p> &lt;dirs&gt; will be passed to BundleUtilities and should contain and directories to be searched to find library dependencies. </p>
<p> &lt;plugins_dir&gt; allows an custom plugins directory to be used. </p>
<p> &lt;request_qt_conf&gt; will force a qt.conf file to be written even if not needed. </p>
<pre>
  INSTALL_QT4_PLUGIN_PATH(plugin executable copy installed_plugin_path_var &lt;plugins_dir&gt; &lt;component&gt; &lt;configurations&gt;)
</pre>
<p> Install (or copy) a resolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. </p>
<p> If &lt;copy&gt; is set to TRUE then the plugins will be copied rather than installed. This is to allow this module to be used at CMake time rather than install time. </p>
<p> If &lt;component&gt; is set then anything installed will use this COMPONENT. </p>
<pre>
  INSTALL_QT4_PLUGIN(plugin executable copy installed_plugin_path_var &lt;plugins_dir&gt; &lt;component&gt;)
</pre>
<p> Install (or copy) an unresolved &lt;plugin&gt; to the default plugins directory (or &lt;plugins_dir&gt;) relative to &lt;executable&gt; and store the result in &lt;installed_plugin_path_var&gt;. See documentation of INSTALL_QT4_PLUGIN_PATH. </p>
<pre>
  INSTALL_QT4_EXECUTABLE(&lt;executable&gt; [&lt;qtplugins&gt; &lt;libs&gt; &lt;dirs&gt; &lt;plugins_dir&gt; &lt;request_qt_conf&gt; &lt;component&gt;])
</pre>
<p> Installs Qt plugins, writes a Qt configuration file (if needed) and fixes up a Qt4 executable using BundleUtilities so it is standalone and can be drag-and-drop copied to another machine as long as all of the system libraries are compatible. The executable will be fixed-up at install time. &lt;component&gt; is the COMPONENT used for bundle fixup and plugin installation. See documentation of FIXUP_QT4_BUNDLE. </p>
<dt><code>Documentation</code></p>
<dd> DocumentationVTK.cmake </p>
<p> This file provides support for the VTK documentation framework. It relies on several tools (Doxygen, Perl, etc). </p>
<dt><code>ExternalData</code></p>
<dd> Manage data files stored outside source tree </p>
<p> Use this module to unambiguously reference data files stored outside the source tree and fetch them at build time from arbitrary local and remote content-addressed locations. Functions provided by this module recognize arguments with the syntax &quot;DATA{&lt;name&gt;}&quot; as references to external data, replace them with full paths to local copies of those data, and create build rules to fetch and update the local copies. </p>
<p> The DATA{} syntax is literal and the &lt;name&gt; is a full or relative path within the source tree. The source tree must contain either a real data file at &lt;name&gt; or a &quot;content link&quot; at &lt;name&gt;&lt;ext&gt; containing a hash of the real file using a hash algorithm corresponding to &lt;ext&gt;. For example, the argument &quot;DATA{img.png}&quot; may be satisfied by either a real &quot;img.png&quot; file in the current source directory or a &quot;img.png.md5&quot; file containing its MD5 sum. </p>
<p> The &#8216;ExternalData_Expand_Arguments&#8217; function evaluates DATA{} references in its arguments and constructs a new list of arguments: </p>
<p>ExternalData_Expand_Arguments(<br />
    &lt;target&gt; #Name of data management target&lt;outVar&gt; #Output variable<br />
        [args&#8230;] #Input arguments,<br />
    DATA {} allowed)</p>
<p> It replaces each DATA{} reference in an argument with the full path of a real data file on disk that will exist after the &lt;target&gt; builds. </p>
<p> The &#8216;ExternalData_Add_Test&#8217; function wraps around the CMake add_test() command but supports DATA{} references in its arguments: </p>
<pre>
  ExternalData_Add_Test(
    &lt;target&gt;   # Name of data management target
    ...        # Arguments of add_test(), DATA{} allowed
    )
</pre>
<p> It passes its arguments through ExternalData_Expand_Arguments and then invokes add_test() using the results. </p>
<p> The &#8216;ExternalData_Add_Target&#8217; function creates a custom target to manage local instances of data files stored externally: </p>
<pre>
  ExternalData_Add_Target(
    &lt;target&gt;   # Name of data management target
    )
</pre>
<p> It creates custom commands in the target as necessary to make data files available for each DATA{} reference previously evaluated by other functions provided by this module. A list of URL templates must be provided in the variable ExternalData_URL_TEMPLATES using the placeholders &quot;%(algo)&quot; and &quot;%(hash)&quot; in each template. Data fetch rules try each URL template in order by substituting the hash algorithm name for &quot;%(algo)&quot; and the hash value for &quot;%(hash)&quot;. </p>
<p> The following hash algorithms are supported: </p>
<p>% (algo)&lt;ext&gt; Description<br />
        &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; -MD5.md5 Message<br />
    &#8211; Digest Algorithm 5,<br />
    RFC 1321 SHA1.sha1 US Secure Hash Algorithm 1, RFC 3174 SHA224.sha224 US Secure Hash Algorithms, RFC 4634 SHA256.sha256 US Secure Hash Algorithms, RFC 4634 SHA384.sha384 US Secure Hash Algorithms, RFC 4634 SHA512.sha512 US Secure Hash Algorithms, RFC 4634</p>
<p> Note that the hashes are used only for unique data identification and download verification. This is not security software. </p>
<p> Example usage: </p>
<pre>
   include(ExternalData)
   set(ExternalData_URL_TEMPLATES &quot;file:///local/%(algo)/%(hash)&quot;
                                  &quot;<a rel="nofollow" href="http://data.org/%(algo)/%(hash)">http://data.org/%(algo)/%(hash)</a>&quot;)
   ExternalData_Add_Test(MyData
     NAME MyTest
     COMMAND MyExe DATA{MyInput.png}
     )
   ExternalData_Add_Target(MyData)
</pre>
<p> When test &quot;MyTest&quot; runs the &quot;DATA{MyInput.png}&quot; argument will be replaced by the full path to a real instance of the data file &quot;MyInput.png&quot; on disk. If the source tree contains a content link such as &quot;MyInput.png.md5&quot; then the &quot;MyData&quot; target creates a real &quot;MyInput.png&quot; in the build tree. </p>
<p> The DATA{} syntax can be told to fetch a file series using the form &quot;DATA{&lt;name&gt;,:}&quot;, where the &quot;:&quot; is literal. If the source tree contains a group of files or content links named like a series then a reference to one member adds rules to fetch all of them. Although all members of a series are fetched, only the file originally named by the DATA{} argument is substituted for it. The default configuration recognizes file series names ending with &quot;#.ext&quot;, &quot;_#.ext&quot;, &quot;.#.ext&quot;, or &quot;-#.ext&quot; where &quot;#&quot; is a sequence of decimal digits and &quot;.ext&quot; is any single extension. Configure it with a regex that parses &lt;number&gt; and &lt;suffix&gt; parts from the end of &lt;name&gt;: </p>
<pre>
  ExternalData_SERIES_PARSE = regex of the form (&lt;number&gt;)(&lt;suffix&gt;)$
</pre>
<p> For more complicated cases set: </p>
<pre>
  ExternalData_SERIES_PARSE = regex with at least two () groups
  ExternalData_SERIES_PARSE_PREFIX = &lt;prefix&gt; regex group number, if any
  ExternalData_SERIES_PARSE_NUMBER = &lt;number&gt; regex group number
  ExternalData_SERIES_PARSE_SUFFIX = &lt;suffix&gt; regex group number
</pre>
<p> Configure series number matching with a regex that matches the &lt;number&gt; part of series members named &lt;prefix&gt;&lt;number&gt;&lt;suffix&gt;: </p>
<pre>
  ExternalData_SERIES_MATCH = regex matching &lt;number&gt; in all series members
</pre>
<p> Note that the &lt;suffix&gt; of a series does not include a hash-algorithm extension. </p>
<p> The DATA{} syntax can alternatively match files associated with the named file and contained in the same directory. Associated files may be specified by options using the syntax DATA{&lt;name&gt;,&lt;opt1&gt;,&lt;opt2&gt;,&#8230;}. Each option may specify one file by name or specify a regular expression to match file names using the syntax REGEX:&lt;regex&gt;. For example, the arguments </p>
<p>DATA{MyData / MyInput.mhd, MyInput.img} #File pair<br />
    DATA<br />
{<br />
    MyData / MyFrames00.png, REGEX : MyFrames[0 &#8211; 9] +\.png<br />
}<br />
#Series</p>
<p> will pass MyInput.mha and MyFrames00.png on the command line but ensure that the associated files are present next to them. </p>
<p> The DATA{} syntax may reference a directory using a trailing slash and a list of associated files. The form DATA{&lt;name&gt;/,&lt;opt1&gt;,&lt;opt2&gt;,&#8230;} adds rules to fetch any files in the directory that match one of the associated file options. For example, the argument DATA{MyDataDir/,REGEX:.*} will pass the full path to a MyDataDir directory on the command line and ensure that the directory contains files corresponding to every file or content link in the MyDataDir source directory. </p>
<p> The variable ExternalData_LINK_CONTENT may be set to the name of a supported hash algorithm to enable automatic conversion of real data files referenced by the DATA{} syntax into content links. For each such &lt;file&gt; a content link named &quot;&lt;file&gt;&lt;ext&gt;&quot; is created. The original file is renamed to the form &quot;.ExternalData_&lt;algo&gt;_&lt;hash&gt;&quot; to stage it for future transmission to one of the locations in the list of URL templates (by means outside the scope of this module). The data fetch rule created for the content link will use the staged object if it cannot be found using any URL template. </p>
<p> The variable ExternalData_OBJECT_STORES may be set to a list of local directories that store objects using the layout &lt;dir&gt;/%(algo)/%(hash). These directories will be searched first for a needed object. If the object is not available in any store then it will be fetched remotely using the URL templates and added to the first local store listed. If no stores are specified the default is a location inside the build tree. </p>
<p> The variable ExternalData_SOURCE_ROOT may be set to the highest source directory containing any path named by a DATA{} reference. The default is CMAKE_SOURCE_DIR. ExternalData_SOURCE_ROOT and CMAKE_SOURCE_DIR must refer to directories within a single source distribution (e.g. they come together in one tarball). </p>
<p> The variable ExternalData_BINARY_ROOT may be set to the directory to hold the real data files named by expanded DATA{} references. The default is CMAKE_BINARY_DIR. The directory layout will mirror that of content links under ExternalData_SOURCE_ROOT. </p>
<p> Variables ExternalData_TIMEOUT_INACTIVITY and ExternalData_TIMEOUT_ABSOLUTE set the download inactivity and absolute timeouts, in seconds. The defaults are 60 seconds and 300 seconds, respectively. Set either timeout to 0 seconds to disable enforcement. </p>
<dt><code>ExternalProject</code></p>
<dd> Create custom targets to build projects in external trees </p>
<p> The &#8216;ExternalProject_Add&#8217; function creates a custom target to drive download, update/patch, configure, build, install and test steps of an external project: </p>
<p>  ExternalProject_Add(&lt;name&gt;    # Name for custom target<br />
    [DEPENDS projects&#8230;]       # Targets on which the project depends<br />
    [PREFIX dir]                # Root dir for entire project<br />
    [LIST_SEPARATOR sep]        # Sep to be replaced by ; in cmd lines<br />
    [TMP_DIR dir]               # Directory to store temporary files<br />
    [STAMP_DIR dir]             # Directory to store step timestamps<br />
#&#8211; Download step &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
    [DOWNLOAD_NAME fname]       # File name to store (if not end of URL)<br />
    [DOWNLOAD_DIR dir]          # Directory to store downloaded files<br />
    [DOWNLOAD_COMMAND cmd&#8230;]   # Command to download source tree<br />
    [CVS_REPOSITORY cvsroot]    # CVSROOT of CVS repository<br />
    [CVS_MODULE mod]            # Module to checkout from CVS repo<br />
    [CVS_TAG tag]               # Tag to checkout from CVS repo<br />
    [SVN_REPOSITORY url]        # URL of Subversion repo<br />
    [SVN_REVISION rev]          # Revision to checkout from Subversion repo<br />
    [SVN_USERNAME john ]        # Username for Subversion checkout and update<br />
    [SVN_PASSWORD doe ]         # Password for Subversion checkout and update<br />
    [SVN_TRUST_CERT 1 ]         # Trust the Subversion server site certificate<br />
    [GIT_REPOSITORY url]        # URL of git repo<br />
    [GIT_TAG tag]               # Git branch name, commit id or tag<br />
    [HG_REPOSITORY url]         # URL of mercurial repo<br />
    [HG_TAG tag]                # Mercurial branch name, commit id or tag<br />
    [URL /&#8230;/src.tgz]          # Full path or URL of source<br />
    [URL_HASH ALGO=value]       # Hash of file at URL<br />
    [URL_MD5 md5]               # Equivalent to URL_HASH MD5=md5<br />
    [TLS_VERIFY bool]           # Should certificate for https be checked<br />
    [TLS_CAINFO file]           # Path to a certificate authority file<br />
    [TIMEOUT seconds]           # Time allowed for file download operations<br />
#&#8211; Update / Patch step &#8212; &#8212; &#8212; &#8212; &#8212;<br />
    [UPDATE_COMMAND cmd&#8230;]     # Source work-tree update command<br />
    [PATCH_COMMAND cmd&#8230;]      # Command to patch downloaded source<br />
#&#8211; Configure step &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    [SOURCE_DIR dir]            # Source dir to be used for build<br />
    [CONFIGURE_COMMAND cmd&#8230;]  # Build tree configuration command<br />
    [CMAKE_COMMAND /&#8230;/cmake]  # Specify alternative cmake executable<br />
    [CMAKE_GENERATOR gen]       # Specify generator for native build<br />
    [CMAKE_GENERATOR_TOOLSET t] # Generator-specific toolset name<br />
    [CMAKE_ARGS args&#8230;]        # Arguments to CMake command line<br />
    [CMAKE_CACHE_ARGS args&#8230;]  # Initial cache arguments, of the form -Dvar:string=on<br />
#&#8211; Build step &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    [BINARY_DIR dir]            # Specify build dir location<br />
    [BUILD_COMMAND cmd&#8230;]      # Command to drive the native build<br />
    [BUILD_IN_SOURCE 1]         # Use source dir for build dir<br />
#&#8211; Install step &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    [INSTALL_DIR dir]           # Installation prefix<br />
    [INSTALL_COMMAND cmd&#8230;]    # Command to drive install after build<br />
#&#8211; Test step &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;<br />
    [TEST_BEFORE_INSTALL 1]     # Add test step executed before install step<br />
    [TEST_AFTER_INSTALL 1]      # Add test step executed after install step<br />
    [TEST_COMMAND cmd&#8230;]       # Command to drive test<br />
#&#8211; Output logging &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    [LOG_DOWNLOAD 1]            # Wrap download in script to log output<br />
    [LOG_UPDATE 1]              # Wrap update in script to log output<br />
    [LOG_CONFIGURE 1]           # Wrap configure in script to log output<br />
    [LOG_BUILD 1]               # Wrap build in script to log output<br />
    [LOG_TEST 1]                # Wrap test in script to log output<br />
    [LOG_INSTALL 1]             # Wrap install in script to log output<br />
#&#8211; Custom targets &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
    [STEP_TARGETS st1 st2 &#8230;]  # Generate custom targets for these steps<br />
    )</p>
<p> The *_DIR options specify directories for the project, with default directories computed as follows. If the PREFIX option is given to ExternalProject_Add() or the EP_PREFIX directory property is set, then an external project is built and installed under the specified prefix: </p>
<pre>
   TMP_DIR      = &lt;prefix&gt;/tmp
   STAMP_DIR    = &lt;prefix&gt;/src/&lt;name&gt;-stamp
   DOWNLOAD_DIR = &lt;prefix&gt;/src
   SOURCE_DIR   = &lt;prefix&gt;/src/&lt;name&gt;
   BINARY_DIR   = &lt;prefix&gt;/src/&lt;name&gt;-build
   INSTALL_DIR  = &lt;prefix&gt;
</pre>
<p> Otherwise, if the EP_BASE directory property is set then components of an external project are stored under the specified base: </p>
<pre>
   TMP_DIR      = &lt;base&gt;/tmp/&lt;name&gt;
   STAMP_DIR    = &lt;base&gt;/Stamp/&lt;name&gt;
   DOWNLOAD_DIR = &lt;base&gt;/Download/&lt;name&gt;
   SOURCE_DIR   = &lt;base&gt;/Source/&lt;name&gt;
   BINARY_DIR   = &lt;base&gt;/Build/&lt;name&gt;
   INSTALL_DIR  = &lt;base&gt;/Install/&lt;name&gt;
</pre>
<p> If no PREFIX, EP_PREFIX, or EP_BASE is specified then the default is to set PREFIX to &quot;&lt;name&gt;-prefix&quot;. Relative paths are interpreted with respect to the build directory corresponding to the source directory in which ExternalProject_Add is invoked. </p>
<p> If SOURCE_DIR is explicitly set to an existing directory the project will be built from it. Otherwise a download step must be specified using one of the DOWNLOAD_COMMAND, CVS_*, SVN_*, or URL options. The URL option may refer locally to a directory or source tarball, or refer to a remote tarball (e.g. <a rel="nofollow" href="http://.../src.tgz">http://&#8230;/src.tgz</a>). </p>
<p> The &#8216;ExternalProject_Add_Step&#8217; function adds a custom step to an external project: </p>
<p>  ExternalProject_Add_Step(&lt;name&gt; &lt;step&gt; # Names of project and custom step<br />
    [COMMAND cmd&#8230;]        # Command line invoked by this step<br />
    [COMMENT &#8220;text&#8230;&#8221;]     # Text printed when step executes<br />
    [DEPENDEES steps&#8230;]    # Steps on which this step depends<br />
    [DEPENDERS steps&#8230;]    # Steps that depend on this step<br />
    [DEPENDS files&#8230;]      # Files on which this step depends<br />
    [ALWAYS 1]              # No stamp file, step always runs<br />
    [WORKING_DIRECTORY dir] # Working directory for command<br />
    [LOG 1]                 # Wrap step in script to log output<br />
    )</p>
<p> The command line, comment, and working directory of every standard and custom step is processed to replace tokens &lt;SOURCE_DIR&gt;, &lt;BINARY_DIR&gt;, &lt;INSTALL_DIR&gt;, and &lt;TMP_DIR&gt; with corresponding property values. </p>
<p> Any builtin step that specifies a &quot;&lt;step&gt;_COMMAND cmd&#8230;&quot; or custom step that specifies a &quot;COMMAND cmd&#8230;&quot; may specify additional command lines using the form &quot;COMMAND cmd&#8230;&quot;. At build time the commands will be executed in order and aborted if any one fails. For example: </p>
<pre>
  ... BUILD_COMMAND make COMMAND echo done ...
</pre>
<p> specifies to run &quot;make&quot; and then &quot;echo done&quot; during the build step. Whether the current working directory is preserved between commands is not defined. Behavior of shell operators like &quot;&amp;&amp;&quot; is not defined. </p>
<p> The &#8216;ExternalProject_Get_Property&#8217; function retrieves external project target properties: </p>
<p>ExternalProject_Get_Property(&lt;name&gt;[prop1[prop2[&#8230;]]])</p>
<p> It stores property values in variables of the same name. Property names correspond to the keyword argument names of &#8216;ExternalProject_Add&#8217;. </p>
<p> The &#8216;ExternalProject_Add_StepTargets&#8217; function generates custom targets for the steps listed: </p>
<p>ExternalProject_Add_StepTargets(&lt;name&gt;[step1[step2[&#8230;]]])</p>
<p> If STEP_TARGETS is set then ExternalProject_Add_StepTargets is automatically called at the end of matching calls to ExternalProject_Add_Step. Pass STEP_TARGETS explicitly to individual ExternalProject_Add calls, or implicitly to all ExternalProject_Add calls by setting the directory property EP_STEP_TARGETS. </p>
<p> If STEP_TARGETS is not set, clients may still manually call ExternalProject_Add_StepTargets after calling ExternalProject_Add or ExternalProject_Add_Step. </p>
<p> This functionality is provided to make it easy to drive the steps independently of each other by specifying targets on build command lines. For example, you may be submitting to a sub-project based dashboard, where you want to drive the configure portion of the build, then submit to the dashboard, followed by the build portion, followed by tests. If you invoke a custom target that depends on a step halfway through the step dependency chain, then all the previous steps will also run to ensure everything is up to date. </p>
<p> For example, to drive configure, build and test steps independently for each ExternalProject_Add call in your project, write the following line prior to any ExternalProject_Add calls in your CMakeLists file: </p>
<pre>
   set_property(DIRECTORY PROPERTY EP_STEP_TARGETS configure build test)
</pre>
<dt><code>FeatureSummary</code></p>
<dd> Macros for generating a summary of enabled/disabled features </p>
<p> This module provides the macros feature_summary(), set_package_properties() and add_feature_info(). For compatibility it also still provides set_package_info(), set_feature_info(), print_enabled_features() and print_disabled_features(). </p>
<p> These macros can be used to generate a summary of enabled and disabled packages and/or feature for a build tree: </p>
<pre>
    -- The following OPTIONAL packages have been found:
    LibXml2 (required version &gt;= 2.4) , XML processing library. , &lt;<a rel="nofollow" href="http://xmlsoft.org">http://xmlsoft.org</a>&gt;
       * Enables HTML-import in MyWordProcessor
       * Enables odt-export in MyWordProcessor
    PNG , A PNG image library. , &lt;<a rel="nofollow" href="http://www.libpng.org/pub/png/">http://www.libpng.org/pub/png/</a>&gt;
       * Enables saving screenshots
    -- The following OPTIONAL packages have not been found:
    Lua51 , The Lua scripting language. , &lt;<a rel="nofollow" href="http://www.lua.org">http://www.lua.org</a>&gt;
       * Enables macros in MyWordProcessor
    Foo , Foo provides cool stuff.
</pre>
<p>    FEATURE_SUMMARY( [FILENAME &lt;file&gt;]<br />
                     [APPEND]<br />
                     [VAR &lt;variable_name&gt;]<br />
                     [INCLUDE_QUIET_PACKAGES]<br />
                     [FATAL_ON_MISSING_REQUIRED_PACKAGES]<br />
                     [DESCRIPTION &#8220;Found packages:&#8221;]<br />
                     WHAT (ALL | PACKAGES_FOUND | PACKAGES_NOT_FOUND<br />
                          | ENABLED_FEATURES | DISABLED_FEATURES]<br />
                   )</p>
<p> The FEATURE_SUMMARY() macro can be used to print information about enabled or disabled packages or features of a project. By default, only the names of the features/packages will be printed and their required version when one was specified. Use SET_PACKAGE_PROPERTIES() to add more useful information, like e.g. a download URL for the respective package or their purpose in the project. </p>
<p> The WHAT option is the only mandatory option. Here you specify what information will be printed: </p>
<pre>
    ALL: print everything
    ENABLED_FEATURES: the list of all features which are enabled
    DISABLED_FEATURES: the list of all features which are disabled
    PACKAGES_FOUND: the list of all packages which have been found
    PACKAGES_NOT_FOUND: the list of all packages which have not been found
    OPTIONAL_PACKAGES_FOUND: only those packages which have been found which have the type OPTIONAL
    OPTIONAL_PACKAGES_NOT_FOUND: only those packages which have not been found which have the type OPTIONAL
    RECOMMENDED_PACKAGES_FOUND: only those packages which have been found which have the type RECOMMENDED
    RECOMMENDED_PACKAGES_NOT_FOUND: only those packages which have not been found which have the type RECOMMENDED
    REQUIRED_PACKAGES_FOUND: only those packages which have been found which have the type REQUIRED
    REQUIRED_PACKAGES_NOT_FOUND: only those packages which have not been found which have the type REQUIRED
    RUNTIME_PACKAGES_FOUND: only those packages which have been found which have the type RUNTIME
    RUNTIME_PACKAGES_NOT_FOUND: only those packages which have not been found which have the type RUNTIME
</pre>
<p> If a FILENAME is given, the information is printed into this file. If APPEND is used, it is appended to this file, otherwise the file is overwritten if it already existed. If the VAR option is used, the information is &quot;printed&quot; into the specified variable. If FILENAME is not used, the information is printed to the terminal. Using the DESCRIPTION option a description or headline can be set which will be printed above the actual content. If INCLUDE_QUIET_PACKAGES is given, packages which have been searched with find_package(&#8230; QUIET) will also be listed. By default they are skipped. If FATAL_ON_MISSING_REQUIRED_PACKAGES is given, CMake will abort if a package which is marked as REQUIRED has not been found. </p>
<p> Example 1, append everything to a file: </p>
<pre>
   feature_summary(WHAT ALL
                   FILENAME ${CMAKE_BINARY_DIR}/all.log APPEND)
</pre>
<p> Example 2, print the enabled features into the variable enabledFeaturesText, including QUIET packages: </p>
<pre>
   feature_summary(WHAT ENABLED_FEATURES
                   INCLUDE_QUIET_PACKAGES
                   DESCRIPTION &quot;Enabled Features:&quot;
                   VAR enabledFeaturesText)
   message(STATUS &quot;${enabledFeaturesText}&quot;)
</pre>
<p>SET_PACKAGE_PROPERTIES(&lt;name&gt; PROPERTIES[URL&lt;url&gt;]<br />
                                        [DESCRIPTION&lt;description&gt;]<br />
                                        [TYPE(RUNTIME | OPTIONAL | RECOMMENDED | REQUIRED)]<br />
                                        [PURPOSE&lt;purpose&gt;])</p>
<p> Use this macro to set up information about the named package, which can then be displayed via FEATURE_SUMMARY(). This can be done either directly in the Find-module or in the project which uses the module after the find_package() call. The features for which information can be set are added automatically by the find_package() command. </p>
<p> URL: this should be the homepage of the package, or something similar. Ideally this is set already directly in the Find-module. </p>
<p> DESCRIPTION: A short description what that package is, at most one sentence. Ideally this is set already directly in the Find-module. </p>
<p> TYPE: What type of dependency has the using project on that package. Default is OPTIONAL. In this case it is a package which can be used by the project when available at buildtime, but it also work without. RECOMMENDED is similar to OPTIONAL, i.e. the project will build if the package is not present, but the functionality of the resulting binaries will be severly limited. If a REQUIRED package is not available at buildtime, the project may not even build. This can be combined with the FATAL_ON_MISSING_REQUIRED_PACKAGES argument for feature_summary(). Last, a RUNTIME package is a package which is actually not used at all during the build, but which is required for actually running the resulting binaries. So if such a package is missing, the project can still be built, but it may not work later on. If set_package_properties() is called multiple times for the same package with different TYPEs, the TYPE is only changed to higher TYPEs ( RUNTIME &lt; OPTIONAL &lt; RECOMMENDED &lt; REQUIRED ), lower TYPEs are ignored. The TYPE property is project-specific, so it cannot be set by the Find-module, but must be set in the project. </p>
<p> PURPOSE: This describes which features this package enables in the project, i.e. it tells the user what functionality he gets in the resulting binaries. If set_package_properties() is called multiple times for a package, all PURPOSE properties are appended to a list of purposes of the package in the project. As the TYPE property, also the PURPOSE property is project-specific, so it cannot be set by the Find-module, but must be set in the project. </p>
<p> Example for setting the info for a package: </p>
<pre>
   find_package(LibXml2)
   set_package_properties(LibXml2 PROPERTIES DESCRIPTION &quot;A XML processing library.&quot;
                                             URL &quot;<a rel="nofollow" href="http://xmlsoft.org/">http://xmlsoft.org/</a>&quot;)
</pre>
<pre>
   set_package_properties(LibXml2 PROPERTIES TYPE RECOMMENDED
                                             PURPOSE &quot;Enables HTML-import in MyWordProcessor&quot;)
   ...
   set_package_properties(LibXml2 PROPERTIES TYPE OPTIONAL
                                             PURPOSE &quot;Enables odt-export in MyWordProcessor&quot;)
</pre>
<pre>
   find_package(DBUS)
   set_package_properties(DBUS PROPERTIES TYPE RUNTIME
                                             PURPOSE &quot;Necessary to disable the screensaver during a presentation&quot; )
</pre>
<pre>
    ADD_FEATURE_INFO(&lt;name&gt; &lt;enabled&gt; &lt;description&gt;)
</pre>
<p> Use this macro to add information about a feature with the given &lt;name&gt;. &lt;enabled&gt; contains whether this feature is enabled or not, &lt;description&gt; is a text describing the feature. The information can be displayed using feature_summary() for ENABLED_FEATURES and DISABLED_FEATURES respectively. </p>
<p> Example for setting the info for a feature: </p>
<pre>
   option(WITH_FOO &quot;Help for foo&quot; ON)
   add_feature_info(Foo WITH_FOO &quot;The Foo feature provides very cool stuff.&quot;)
</pre>
<p> The following macros are provided for compatibility with previous CMake versions: </p>
<p>SET_PACKAGE_INFO(&lt;name&gt;&lt;description&gt;[&lt;url&gt;[&lt;purpose&gt;]])</p>
<p> Use this macro to set up information about the named package, which can then be displayed via FEATURE_SUMMARY(). This can be done either directly in the Find-module or in the project which uses the module after the find_package() call. The features for which information can be set are added automatically by the find_package() command. </p>
<pre>
    PRINT_ENABLED_FEATURES()
</pre>
<p> Does the same as FEATURE_SUMMARY(WHAT ENABLED_FEATURES DESCRIPTION &quot;Enabled features:&quot;) </p>
<pre>
    PRINT_DISABLED_FEATURES()
</pre>
<p> Does the same as FEATURE_SUMMARY(WHAT DISABLED_FEATURES DESCRIPTION &quot;Disabled features:&quot;) </p>
<pre>
    SET_FEATURE_INFO(&lt;name&gt; &lt;description&gt; [&lt;url&gt;] )
</pre>
<p> Does the same as SET_PACKAGE_INFO(&lt;name&gt; &lt;description&gt; &lt;url&gt; ) </p>
<dt><code>FindALSA</code></p>
<dd> Find alsa </p>
<p> Find the alsa libraries (asound) </p>
<pre>
  This module defines the following variables:
     ALSA_FOUND       - True if ALSA_INCLUDE_DIR &amp; ALSA_LIBRARY are found
     ALSA_LIBRARIES   - Set when ALSA_LIBRARY is found
     ALSA_INCLUDE_DIRS - Set when ALSA_INCLUDE_DIR is found
</pre>
<pre>
     ALSA_INCLUDE_DIR - where to find asoundlib.h, etc.
     ALSA_LIBRARY     - the asound library
     ALSA_VERSION_STRING - the version of alsa found (since CMake 2.8.8)
</pre>
<dt><code>FindASPELL</code></p>
<dd> Try to find ASPELL </p>
<p> Once done this will define </p>
<pre>
  ASPELL_FOUND - system has ASPELL
  ASPELL_EXECUTABLE - the ASPELL executable
  ASPELL_INCLUDE_DIR - the ASPELL include directory
  ASPELL_LIBRARIES - The libraries needed to use ASPELL
  ASPELL_DEFINITIONS - Compiler switches required for using ASPELL
</pre>
<dt><code>FindAVIFile</code></p>
<dd> Locate AVIFILE library and include paths </p>
<p> AVIFILE (<a rel="nofollow" href="http://avifile.sourceforge.net/)is">http://avifile.sourceforge.net/)is</a> a set of libraries for i386 machines to use various AVI codecs. Support is limited beyond Linux. Windows provides native AVI support, and so doesn&#8217;t need this library. This module defines </p>
<pre>
  AVIFILE_INCLUDE_DIR, where to find avifile.h , etc.
  AVIFILE_LIBRARIES, the libraries to link against
  AVIFILE_DEFINITIONS, definitions to use when compiling
  AVIFILE_FOUND, If false, don't try to use AVIFILE
</pre>
<dt><code>FindArmadillo</code></p>
<dd> Find Armadillo </p>
<p> Find the Armadillo C++ library </p>
<p> Using Armadillo: </p>
<p>find_package(Armadillo REQUIRED)<br />
    include_directories(${ARMADILLO_INCLUDE_DIRS})<br />
        add_executable(foo foo.cc)<br />
            target_link_libraries(foo ${ARMADILLO_LIBRARIES})</p>
<p> This module sets the following variables: </p>
<pre>
  ARMADILLO_FOUND - set to true if the library is found
  ARMADILLO_INCLUDE_DIRS - list of required include directories
  ARMADILLO_LIBRARIES - list of libraries to be linked
  ARMADILLO_VERSION_MAJOR - major version number
  ARMADILLO_VERSION_MINOR - minor version number
  ARMADILLO_VERSION_PATCH - patch version number
  ARMADILLO_VERSION_STRING - version number as a string (ex: &quot;1.0.4&quot;)
  ARMADILLO_VERSION_NAME - name of the version (ex: &quot;Antipodean Antileech&quot;)
</pre>
<dt><code>FindBISON</code></p>
<dd> Find bison executable and provides macros to generate custom build rules </p>
<p> The module defines the following variables: </p>
<pre>
  BISON_EXECUTABLE - path to the bison program
  BISON_VERSION - version of bison
  BISON_FOUND - true if the program was found
</pre>
<p> The minimum required version of bison can be specified using the standard CMake syntax, e.g. find_package(BISON 2.1.3) </p>
<p> If bison is found, the module defines the macros: </p>
<p>BISON_TARGET(&lt;Name&gt;&lt;YaccInput&gt;&lt;CodeOutput&gt;[VERBOSE&lt;file&gt;]<br />
                                          [COMPILE_FLAGS&lt;string&gt;])</p>
<p> which will create a custom rule to generate a parser. &lt;YaccInput&gt; is the path to a yacc file. &lt;CodeOutput&gt; is the name of the source file generated by bison. A header file is also be generated, and contains the token list. If COMPILE_FLAGS option is specified, the next parameter is added in the bison command line. if VERBOSE option is specified, &lt;file&gt; is created and contains verbose descriptions of the grammar and parser. The macro defines a set of variables: </p>
<p>  BISON_${Name}_DEFINED &#8211; true is the macro ran successfully<br />
  BISON_${Name}_INPUT &#8211; The input source file, an alias for &lt;YaccInput&gt;<br />
  BISON_${Name}_OUTPUT_SOURCE &#8211; The source file generated by bison<br />
  BISON_${Name}_OUTPUT_HEADER &#8211; The header file generated by bison<br />
  BISON_${Name}_OUTPUTS &#8211; The sources files generated by bison<br />
  BISON_${Name}_COMPILE_FLAGS &#8211; Options used in the bison command line</p>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
    Example:</p>
<p>find_package(BISON)<br />
        BISON_TARGET(MyParser parser.y ${CMAKE_CURRENT_BINARY_DIR} / parser.cpp)<br />
            add_executable(Foo main.cpp ${BISON_MyParser_OUTPUTS}) == ==<br />
    == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==</p>
<dt><code>FindBLAS</code></p>
<dd> Find BLAS library </p>
<p> This module finds an installed fortran library that implements the BLAS linear-algebra interface (see <a rel="nofollow" href="http://www.netlib.org/blas/">http://www.netlib.org/blas/</a>). The list of libraries searched for is taken from the autoconf macro file, acx_blas.m4 (distributed at <a href="http://ac-archive.sourceforge.net/ac-archive/acx_blas.html">http://ac-archive.sourceforge.net/ac-archive/acx_blas.html</a>). </p>
<p> This module sets the following variables: </p>
<p>  BLAS_FOUND &#8211; set to true if a library implementing the BLAS interface<br />
    is found<br />
  BLAS_LINKER_FLAGS &#8211; uncached list of required linker flags (excluding -l<br />
    and -L).<br />
  BLAS_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use BLAS<br />
  BLAS95_LIBRARIES &#8211; uncached list of libraries (using full path name)<br />
    to link against to use BLAS95 interface<br />
  BLAS95_FOUND &#8211; set to true if a library implementing the BLAS f95 interface<br />
    is found<br />
  BLA_STATIC  if set on this determines what kind of linkage we do (static)<br />
  BLA_VENDOR  if set checks only the specified vendor, if not set checks<br />
     all the possibilities<br />
  BLA_F95     if set on tries to find the f95 interfaces for BLAS/LAPACK</p>
<p> C/CXX should be enabled to use Intel mkl </p>
<dt><code>FindBZip2</code></p>
<dd> Try to find BZip2 </p>
<p> Once done this will define </p>
<pre>
  BZIP2_FOUND - system has BZip2
  BZIP2_INCLUDE_DIR - the BZip2 include directory
  BZIP2_LIBRARIES - Link these to use BZip2
  BZIP2_NEED_PREFIX - this is set if the functions are prefixed with BZ2_
  BZIP2_VERSION_STRING - the version of BZip2 found (since CMake 2.8.8)
</pre>
<dt><code>FindBoost</code></p>
<dd> Find Boost include dirs and libraries </p>
<p> Use this module by invoking find_package with the form: </p>
<p>  find_package(Boost<br />
    [version] [EXACT]      # Minimum or EXACT version e.g. 1.36.0<br />
    [REQUIRED]             # Fail with error if Boost is not found<br />
    [COMPONENTS &lt;libs&gt;&#8230;] # Boost libraries by their canonical name<br />
    )                      # e.g. &#8220;date_time&#8221; for &#8220;libboost_date_time&#8221;</p>
<p> This module finds headers and requested component libraries OR a CMake package configuration file provided by a &quot;Boost CMake&quot; build. For the latter case skip to the &quot;Boost CMake&quot; section below. For the former case results are reported in variables: </p>
<p>  Boost_FOUND            &#8211; True if headers and requested libraries were found<br />
  Boost_INCLUDE_DIRS     &#8211; Boost include directories<br />
  Boost_LIBRARY_DIRS     &#8211; Link directories for Boost libraries<br />
  Boost_LIBRARIES        &#8211; Boost component libraries to be linked<br />
  Boost_&lt;C&gt;_FOUND        &#8211; True if component &lt;C&gt; was found (&lt;C&gt; is upper-case)<br />
  Boost_&lt;C&gt;_LIBRARY      &#8211; Libraries to link for component &lt;C&gt; (may include<br />
                           target_link_libraries debug/optimized keywords)<br />
  Boost_VERSION          &#8211; BOOST_VERSION value from boost/version.hpp<br />
  Boost_LIB_VERSION      &#8211; Version string appended to library filenames<br />
  Boost_MAJOR_VERSION    &#8211; Boost major version number (X in X.y.z)<br />
  Boost_MINOR_VERSION    &#8211; Boost minor version number (Y in x.Y.z)<br />
  Boost_SUBMINOR_VERSION &#8211; Boost subminor version number (Z in x.y.Z)<br />
  Boost_LIB_DIAGNOSTIC_DEFINITIONS (Windows)<br />
                         &#8211; Pass to add_definitions() to have diagnostic<br />
                           information about Boost&#8217;s automatic linking<br />
                           displayed during compilation</p>
<p> This module reads hints about search locations from variables: </p>
<pre>
  BOOST_ROOT             - Preferred installation prefix
   (or BOOSTROOT)
  BOOST_INCLUDEDIR       - Preferred include directory e.g. &lt;prefix&gt;/include
  BOOST_LIBRARYDIR       - Preferred library directory e.g. &lt;prefix&gt;/lib
  Boost_NO_SYSTEM_PATHS  - Set to ON to disable searching in locations not
                           specified by these hint variables. Default is OFF.
  Boost_ADDITIONAL_VERSIONS
                         - List of Boost versions not known to this module
                           (Boost install locations may contain the version)
</pre>
<p> and saves search results persistently in CMake cache entries: </p>
<pre>
  Boost_INCLUDE_DIR         - Directory containing Boost headers
  Boost_LIBRARY_DIR         - Directory containing Boost libraries
  Boost_&lt;C&gt;_LIBRARY_DEBUG   - Component &lt;C&gt; library debug variant
  Boost_&lt;C&gt;_LIBRARY_RELEASE - Component &lt;C&gt; library release variant
</pre>
<p> Users may set these hints or results as cache entries. Projects should not read these entries directly but instead use the above result variables. Note that some hint names start in upper-case &quot;BOOST&quot;. One may specify these as environment variables if they are not specified as CMake variables or cache entries. </p>
<p> This module first searches for the Boost header files using the above hint variables (excluding BOOST_LIBRARYDIR) and saves the result in Boost_INCLUDE_DIR. Then it searches for requested component libraries using the above hints (excluding BOOST_INCLUDEDIR and Boost_ADDITIONAL_VERSIONS), &quot;lib&quot; directories near Boost_INCLUDE_DIR, and the library name configuration settings below. It saves the library directory in Boost_LIBRARY_DIR and individual library locations in Boost_&lt;C&gt;_LIBRARY_DEBUG and Boost_&lt;C&gt;_LIBRARY_RELEASE. When one changes settings used by previous searches in the same build tree (excluding environment variables) this module discards previous search results affected by the changes and searches again. </p>
<p> Boost libraries come in many variants encoded in their file name. Users or projects may tell this module which variant to find by setting variables: </p>
<p>  Boost_USE_MULTITHREADED  &#8211; Set to OFF to use the non-multithreaded<br />
                             libraries (&#8216;mt&#8217; tag).  Default is ON.<br />
  Boost_USE_STATIC_LIBS    &#8211; Set to ON to force the use of the static<br />
                             libraries.  Default is OFF.<br />
  Boost_USE_STATIC_RUNTIME &#8211; Set to ON or OFF to specify whether to use<br />
                             libraries linked statically to the C++ runtime<br />
                             (&#8216;s&#8217; tag).  Default is platform dependent.<br />
  Boost_USE_DEBUG_PYTHON   &#8211; Set to ON to use libraries compiled with a<br />
                             debug Python build (&#8216;y&#8217; tag). Default is OFF.<br />
  Boost_USE_STLPORT        &#8211; Set to ON to use libraries compiled with<br />
                             STLPort (&#8216;p&#8217; tag).  Default is OFF.<br />
  Boost_USE_STLPORT_DEPRECATED_NATIVE_IOSTREAMS<br />
                           &#8211; Set to ON to use libraries compiled with<br />
                             STLPort deprecated &#8220;native iostreams&#8221;<br />
                             (&#8216;n&#8217; tag).  Default is OFF.<br />
  Boost_COMPILER           &#8211; Set to the compiler-specific library suffix<br />
                             (e.g. &#8220;-gcc43&#8221;).  Default is auto-computed<br />
                             for the C++ compiler in use.<br />
  Boost_THREADAPI          &#8211; Suffix for &#8220;thread&#8221; component library name,<br />
                             such as &#8220;pthread&#8221; or &#8220;win32&#8221;.  Names with<br />
                             and without this suffix will both be tried.</p>
<p> Other variables one may set to control this module are: </p>
<pre>
  Boost_DEBUG              - Set to ON to enable debug output from FindBoost.
                             Please enable this before filing any bug report.
  Boost_DETAILED_FAILURE_MSG
                           - Set to ON to add detailed information to the
                             failure message even when the REQUIRED option
                             is not given to the find_package call.
  Boost_REALPATH           - Set to ON to resolve symlinks for discovered
                             libraries to assist with packaging.  For example,
                             the &quot;system&quot; component library may be resolved to
                             &quot;/usr/lib/libboost_system.so.1.42.0&quot; instead of
                             &quot;/usr/lib/libboost_system.so&quot;.  This does not
                             affect linking and should not be enabled unless
                             the user needs this information.
</pre>
<p> On Visual Studio and Borland compilers Boost headers request automatic linking to corresponding libraries. This requires matching libraries to be linked explicitly or available in the link library search path. In this case setting Boost_USE_STATIC_LIBS to OFF may not achieve dynamic linking. Boost automatic linking typically requests static libraries with a few exceptions (such as Boost.Python). Use </p>
<pre>
  add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})
</pre>
<p> to ask Boost to report information about automatic linking requests. </p>
<p> Example to find Boost headers only: </p>
<p>find_package(Boost 1.36.0) if (Boost_FOUND)<br />
    include_directories(${Boost_INCLUDE_DIRS})<br />
        add_executable(foo foo.cc)<br />
            endif()</p>
<p> Example to find Boost headers and some libraries: </p>
<p>set(Boost_USE_STATIC_LIBS ON)<br />
    set(Boost_USE_MULTITHREADED ON)<br />
        set(Boost_USE_STATIC_RUNTIME OFF)<br />
            find_package(Boost 1.36.0 COMPONENTS date_time filesystem system&#8230;) if (Boost_FOUND)<br />
                include_directories(${Boost_INCLUDE_DIRS})<br />
                    add_executable(foo foo.cc)<br />
                        target_link_libraries(foo ${Boost_LIBRARIES})<br />
                            endif()</p>
<p> Boost CMake &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;- </p>
<p> If Boost was built using the boost-cmake project it provides a package configuration file for use with find_package&#8217;s Config mode. This module looks for the package configuration file called BoostConfig.cmake or boost-config.cmake and stores the result in cache entry &quot;Boost_DIR&quot;. If found, the package configuration file is loaded and this module returns with no further action. See documentation of the Boost CMake package configuration for details on what it provides. </p>
<p> Set Boost_NO_BOOST_CMAKE to ON to disable the search for boost-cmake. </p>
<dt><code>FindBullet</code></p>
<dd> Try to find the Bullet physics engine </p>
<pre>
  This module defines the following variables
</pre>
<pre>
  BULLET_FOUND - Was bullet found
  BULLET_INCLUDE_DIRS - the Bullet include directories
  BULLET_LIBRARIES - Link to this, by default it includes
                     all bullet components (Dynamics,
                     Collision, LinearMath, &amp; SoftBody)
</pre>
<pre>
  This module accepts the following variables
</pre>
<pre>
  BULLET_ROOT - Can be set to bullet install path or Windows build path
</pre>
<dt><code>FindCABLE</code></p>
<dd> Find CABLE </p>
<p> This module finds if CABLE is installed and determines where the include files and libraries are. This code sets the following variables: </p>
<pre>
  CABLE             the path to the cable executable
  CABLE_TCL_LIBRARY the path to the Tcl wrapper library
  CABLE_INCLUDE_DIR the path to the include directory
</pre>
<p> To build Tcl wrappers, you should add shared library and link it to ${CABLE_TCL_LIBRARY}. You should also add ${CABLE_INCLUDE_DIR} as an include directory. </p>
<dt><code>FindCUDA</code></p>
<dd> Tools for building CUDA C files: libraries and build dependencies. </p>
<p> This script locates the NVIDIA CUDA C tools. It should work on linux, windows, and mac and should be reasonably up to date with CUDA C releases. </p>
<p> This script makes use of the standard find_package arguments of &lt;VERSION&gt;, REQUIRED and QUIET. CUDA_FOUND will report if an acceptable version of CUDA was found. </p>
<p> The script will prompt the user to specify CUDA_TOOLKIT_ROOT_DIR if the prefix cannot be determined by the location of nvcc in the system path and REQUIRED is specified to find_package(). To use a different installed version of the toolkit set the environment variable CUDA_BIN_PATH before running cmake (e.g. CUDA_BIN_PATH=/usr/local/cuda1.0 instead of the default /usr/local/cuda) or set CUDA_TOOLKIT_ROOT_DIR after configuring. If you change the value of CUDA_TOOLKIT_ROOT_DIR, various components that depend on the path will be relocated. </p>
<p> It might be necessary to set CUDA_TOOLKIT_ROOT_DIR manually on certain platforms, or to use a cuda runtime not installed in the default location. In newer versions of the toolkit the cuda library is included with the graphics driver- be sure that the driver version matches what is needed by the cuda runtime version. </p>
<p> The following variables affect the behavior of the macros in the script (in alphebetical order). Note that any of these flags can be changed multiple times in the same directory before calling CUDA_ADD_EXECUTABLE, CUDA_ADD_LIBRARY, CUDA_COMPILE, CUDA_COMPILE_PTX or CUDA_WRAP_SRCS. </p>
<pre>
  CUDA_64_BIT_DEVICE_CODE (Default matches host bit size)
  -- Set to ON to compile for 64 bit device code, OFF for 32 bit device code.
     Note that making this different from the host code when generating object
     or C files from CUDA code just won't work, because size_t gets defined by
     nvcc in the generated source.  If you compile to PTX and then load the
     file yourself, you can mix bit sizes between device and host.
</pre>
<pre>
  CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE (Default ON)
  -- Set to ON if you want the custom build rule to be attached to the source
     file in Visual Studio.  Turn OFF if you add the same cuda file to multiple
     targets.
</pre>
<p>This allows the user to build the target from the CUDA file; however, bad<br />
     things can happen if the CUDA source file is added to multiple targets.<br />
     When performing parallel builds it is possible for the custom build<br />
     command to be run more than once and in parallel causing cryptic build<br />
     errors.  VS runs the rules for every source file in the target, and a<br />
     source can have only one rule no matter how many projects it is added to.<br />
     When the rule is run from multiple targets race conditions can occur on<br />
     the generated file.  Eventually everything will get built, but if the user<br />
     is unaware of this behavior, there may be confusion.  It would be nice if<br />
     this script could detect the reuse of source files across multiple targets<br />
     and turn the option off for the user, but no good solution could be found.</p>
<pre>
  CUDA_BUILD_CUBIN (Default OFF)
  -- Set to ON to enable and extra compilation pass with the -cubin option in
     Device mode. The output is parsed and register, shared memory usage is
     printed during build.
</pre>
<p>  CUDA_BUILD_EMULATION (Default OFF for device mode)<br />
  &#8212; Set to ON for Emulation mode. -D_DEVICEEMU is defined for CUDA C files<br />
     when CUDA_BUILD_EMULATION is TRUE.</p>
<pre>
  CUDA_GENERATED_OUTPUT_DIR (Default CMAKE_CURRENT_BINARY_DIR)
  -- Set to the path you wish to have the generated files placed.  If it is
     blank output files will be placed in CMAKE_CURRENT_BINARY_DIR.
     Intermediate files will always be placed in
     CMAKE_CURRENT_BINARY_DIR/CMakeFiles.
</pre>
<pre>
  CUDA_HOST_COMPILATION_CPP (Default ON)
  -- Set to OFF for C compilation of host code.
</pre>
<p>  CUDA_HOST_COMPILER (Default CMAKE_C_COMPILER, $(VCInstallDir)/bin for VS)<br />
  &#8211;Set the host compiler to be used by nvcc.Ignored if &#8211; ccbin or<br />
      &#8211;compiler &#8211; bindir is already present in the CUDA_NVCC_FLAGS or<br />
      CUDA_NVCC_FLAGS_&lt;CONFIG&gt; variables.For Visual Studio targets<br />
          $(VCInstallDir) /<br />
          bin is a special value that expands out to the path when<br />
          the command is run from withing VS.</p>
<pre>
  CUDA_NVCC_FLAGS
  CUDA_NVCC_FLAGS_&lt;CONFIG&gt;
  -- Additional NVCC command line arguments.  NOTE: multiple arguments must be
     semi-colon delimited (e.g. --compiler-options;-Wall)
</pre>
<p>CUDA_PROPAGATE_HOST_FLAGS(Default ON)<br />
  &#8212; Set to ON to propagate CMAKE_{C,CXX}_FLAGS and their configuration<br />
     dependent counterparts (e.g. CMAKE_C_FLAGS_DEBUG) automatically to the<br />
     host compiler through nvcc&#8217;s -Xcompiler flag.  This helps make the<br />
     generated host code match the rest of the system better.  Sometimes<br />
     certain flags give nvcc problems, and this will help you turn the flag<br />
     propagation off.  This does not affect the flags supplied directly to nvcc<br />
     via CUDA_NVCC_FLAGS or through the OPTION flags specified through<br />
     CUDA_ADD_LIBRARY, CUDA_ADD_EXECUTABLE, or CUDA_WRAP_SRCS.  Flags used for<br />
     shared library compilation are not affected by this flag.</p>
<pre>
  CUDA_SEPARABLE_COMPILATION (Default OFF)
  -- If set this will enable separable compilation for all CUDA runtime object
     files.  If used outside of CUDA_ADD_EXECUTABLE and CUDA_ADD_LIBRARY
     (e.g. calling CUDA_WRAP_SRCS directly),
     CUDA_COMPUTE_SEPARABLE_COMPILATION_OBJECT_FILE_NAME and
     CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS should be called.
</pre>
<pre>
  CUDA_VERBOSE_BUILD (Default OFF)
  -- Set to ON to see all the commands used when building the CUDA file.  When
     using a Makefile generator the value defaults to VERBOSE (run make
     VERBOSE=1 to see output), although setting CUDA_VERBOSE_BUILD to ON will
     always print the output.
</pre>
<p> The script creates the following macros (in alphebetical order): </p>
<pre>
  CUDA_ADD_CUFFT_TO_TARGET( cuda_target )
  -- Adds the cufft library to the target (can be any target).  Handles whether
     you are in emulation mode or not.
</pre>
<pre>
  CUDA_ADD_CUBLAS_TO_TARGET( cuda_target )
  -- Adds the cublas library to the target (can be any target).  Handles
     whether you are in emulation mode or not.
</pre>
<p>CUDA_ADD_EXECUTABLE(cuda_target file0 file1&#8230;<br />
                        [WIN32][MACOSX_BUNDLE][EXCLUDE_FROM_ALL][OPTIONS&#8230;])<br />
&#8211;Creates an executable &#8220;cuda_target&#8221; which is made up of the files<br />
      specified.All of the non CUDA C files are compiled using the standard<br />
          build rules specified by CMAKE and the cuda files are compiled to object<br />
              files using nvcc and the host compiler.In addition CUDA_INCLUDE_DIRS is<br />
                  added automatically to<br />
                  include_directories()<br />
                      .Some standard CMake target<br />
  calls can be used on the target after calling this macro(e.g.set_target_properties and target_link_libraries),<br />
    but setting<br />
    properties that adjust compilation flags will not affect code compiled by<br />
    nvcc.Such flags should be modified before calling CUDA_ADD_EXECUTABLE,<br />
    CUDA_ADD_LIBRARY or CUDA_WRAP_SRCS.</p>
<p>CUDA_ADD_LIBRARY(cuda_target file0 file1&#8230;<br />
                     [STATIC | SHARED | MODULE][EXCLUDE_FROM_ALL][OPTIONS&#8230;])<br />
&#8211;Same as CUDA_ADD_EXECUTABLE except that a library is created.</p>
<pre>
  CUDA_BUILD_CLEAN_TARGET()
  -- Creates a convience target that deletes all the dependency files
     generated.  You should make clean after running this target to ensure the
     dependency files get regenerated.
</pre>
<p>CUDA_COMPILE(generated_files file0 file1&#8230;[STATIC | SHARED | MODULE]<br />
                                           [OPTIONS&#8230;])<br />
&#8211;Returns a list of generated files from the input source files to be used<br />
        with ADD_LIBRARY or<br />
    ADD_EXECUTABLE.</p>
<pre>
  CUDA_COMPILE_PTX( generated_files file0 file1 ... [OPTIONS ...] )
  -- Returns a list of PTX files generated from the input source files.
</pre>
<pre>
  CUDA_COMPUTE_SEPARABLE_COMPILATION_OBJECT_FILE_NAME( output_file_var
                                                       cuda_target
                                                       object_files )
  -- Compute the name of the intermediate link file used for separable
     compilation.  This file name is typically passed into
     CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS.  output_file_var is produced
     based on cuda_target the list of objects files that need separable
     compilation as specified by object_files.  If the object_files list is
     empty, then output_file_var will be empty.  This function is called
     automatically for CUDA_ADD_LIBRARY and CUDA_ADD_EXECUTABLE.  Note that
     this is a function and not a macro.
</pre>
<pre>
  CUDA_INCLUDE_DIRECTORIES( path0 path1 ... )
  -- Sets the directories that should be passed to nvcc
     (e.g. nvcc -Ipath0 -Ipath1 ... ). These paths usually contain other .cu
     files.
</pre>
<pre>
  CUDA_LINK_SEPARABLE_COMPILATION_OBJECTS( output_file_var cuda_target
                                           nvcc_flags object_files)
</pre>
<pre>
  -- Generates the link object required by separable compilation from the given
     object files.  This is called automatically for CUDA_ADD_EXECUTABLE and
     CUDA_ADD_LIBRARY, but can be called manually when using CUDA_WRAP_SRCS
     directly.  When called from CUDA_ADD_LIBRARY or CUDA_ADD_EXECUTABLE the
     nvcc_flags passed in are the same as the flags passed in via the OPTIONS
     argument.  The only nvcc flag added automatically is the bitness flag as
     specified by CUDA_64_BIT_DEVICE_CODE.  Note that this is a function
     instead of a macro.
</pre>
<p>CUDA_WRAP_SRCS(cuda_target format generated_files file0 file1&#8230;<br />
                   [STATIC | SHARED | MODULE][OPTIONS&#8230;])<br />
&#8211;This is where all the magic happens.CUDA_ADD_EXECUTABLE,<br />
    CUDA_ADD_LIBRARY, CUDA_COMPILE, and CUDA_COMPILE_PTX all call this function under the hood.</p>
<pre>
     Given the list of files (file0 file1 ... fileN) this macro generates
     custom commands that generate either PTX or linkable objects (use &quot;PTX&quot; or
     &quot;OBJ&quot; for the format argument to switch).  Files that don't end with .cu
     or have the HEADER_FILE_ONLY property are ignored.
</pre>
<pre>
     The arguments passed in after OPTIONS are extra command line options to
     give to nvcc.  You can also specify per configuration options by
     specifying the name of the configuration followed by the options.  General
     options must preceed configuration specific options.  Not all
     configurations need to be specified, only the ones provided will be used.
</pre>
<p>OPTIONS &#8211; DFLAG = 2 &#8220;-DFLAG_OTHER=space in flag&#8221; DEBUG &#8211; g<br />
                                                             RELEASE&#8211; use_fast_math<br />
                                                                 RELWITHDEBINFO&#8211; use_fast_math;<br />
&#8211; g<br />
    MINSIZEREL&#8211; use_fast_math</p>
<pre>
     For certain configurations (namely VS generating object files with
     CUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE set to ON), no generated file will
     be produced for the given cuda file.  This is because when you add the
     cuda file to Visual Studio it knows that this file produces an object file
     and will link in the resulting object file automatically.
</pre>
<pre>
     This script will also generate a separate cmake script that is used at
     build time to invoke nvcc.  This is for several reasons.
</pre>
<pre>
       1. nvcc can return negative numbers as return values which confuses
       Visual Studio into thinking that the command succeeded.  The script now
       checks the error codes and produces errors when there was a problem.
</pre>
<pre>
       2. nvcc has been known to not delete incomplete results when it
       encounters problems.  This confuses build systems into thinking the
       target was generated when in fact an unusable file exists.  The script
       now deletes the output files if there was an error.
</pre>
<pre>
       3. By putting all the options that affect the build into a file and then
       make the build rule dependent on the file, the output files will be
       regenerated when the options change.
</pre>
<pre>
     This script also looks at optional arguments STATIC, SHARED, or MODULE to
     determine when to target the object compilation for a shared library.
     BUILD_SHARED_LIBS is ignored in CUDA_WRAP_SRCS, but it is respected in
     CUDA_ADD_LIBRARY.  On some systems special flags are added for building
     objects intended for shared libraries.  A preprocessor macro,
     &lt;target_name&gt;_EXPORTS is defined when a shared library compilation is
     detected.
</pre>
<pre>
     Flags passed into add_definitions with -D or /D are passed along to nvcc.
</pre>
<p> The script defines the following variables: </p>
<pre>
  CUDA_VERSION_MAJOR    -- The major version of cuda as reported by nvcc.
  CUDA_VERSION_MINOR    -- The minor version.
  CUDA_VERSION
  CUDA_VERSION_STRING   -- CUDA_VERSION_MAJOR.CUDA_VERSION_MINOR
</pre>
<p>  CUDA_TOOLKIT_ROOT_DIR &#8212; Path to the CUDA Toolkit (defined if not set).<br />
  CUDA_SDK_ROOT_DIR     &#8212; Path to the CUDA SDK.  Use this to find files in the<br />
                           SDK.  This script will not directly support finding<br />
                           specific libraries or headers, as that isn&#8217;t<br />
                           supported by NVIDIA.  If you want to change<br />
                           libraries when the path changes see the<br />
                           FindCUDA.cmake script for an example of how to clear<br />
                           these variables.  There are also examples of how to<br />
                           use the CUDA_SDK_ROOT_DIR to locate headers or<br />
                           libraries, if you so choose (at your own risk).<br />
  CUDA_INCLUDE_DIRS     &#8212; Include directory for cuda headers.  Added automatically<br />
                           for CUDA_ADD_EXECUTABLE and CUDA_ADD_LIBRARY.<br />
  CUDA_LIBRARIES        &#8212; Cuda RT library.<br />
  CUDA_CUFFT_LIBRARIES  &#8212; Device or emulation library for the Cuda FFT<br />
                           implementation (alternative to:<br />
                           CUDA_ADD_CUFFT_TO_TARGET macro)<br />
  CUDA_CUBLAS_LIBRARIES &#8212; Device or emulation library for the Cuda BLAS<br />
                           implementation (alterative to:<br />
                           CUDA_ADD_CUBLAS_TO_TARGET macro).<br />
  CUDA_cupti_LIBRARY    &#8212; CUDA Profiling Tools Interface library.<br />
                           Only available for CUDA version 4.0+.<br />
  CUDA_curand_LIBRARY   &#8212; CUDA Random Number Generation library.<br />
                           Only available for CUDA version 3.2+.<br />
  CUDA_cusparse_LIBRARY &#8212; CUDA Sparse Matrix library.<br />
                           Only available for CUDA version 3.2+.<br />
  CUDA_npp_LIBRARY      &#8212; NVIDIA Performance Primitives library.<br />
                           Only available for CUDA version 4.0+.<br />
  CUDA_nppc_LIBRARY      &#8212; NVIDIA Performance Primitives library (core).<br />
                           Only available for CUDA version 5.5+.<br />
  CUDA_nppi_LIBRARY      &#8212; NVIDIA Performance Primitives library (image processing).<br />
                           Only available for CUDA version 5.5+.<br />
  CUDA_npps_LIBRARY      &#8212; NVIDIA Performance Primitives library (signal processing).<br />
                           Only available for CUDA version 5.5+.<br />
  CUDA_nvcuvenc_LIBRARY &#8212; CUDA Video Encoder library.<br />
                           Only available for CUDA version 3.2+.<br />
                           Windows only.<br />
  CUDA_nvcuvid_LIBRARY  &#8212; CUDA Video Decoder library.<br />
                           Only available for CUDA version 3.2+.<br />
                           Windows only.</p>
<pre>
  James Bigler, NVIDIA Corp (nvidia.com - jbigler)
  Abe Stephens, SCI Institute -- <a rel="nofollow" href="http://www.sci.utah.edu/~abe/FindCuda.html">http://www.sci.utah.edu/~abe/FindCuda.html</a>
</pre>
<pre>
  Copyright (c) 2008 - 2009 NVIDIA Corporation.  All rights reserved.
</pre>
<pre>
  Copyright (c) 2007-2009
  Scientific Computing and Imaging Institute, University of Utah
</pre>
<pre>
  This code is licensed under the MIT License.  See the FindCUDA.cmake script
  for the text of the license.
</pre>
<dt><code>FindCURL</code></p>
<dd> Find curl </p>
<p> Find the native CURL headers and libraries. </p>
<pre>
  CURL_INCLUDE_DIRS   - where to find curl/curl.h, etc.
  CURL_LIBRARIES      - List of libraries when using curl.
  CURL_FOUND          - True if curl found.
  CURL_VERSION_STRING - the version of curl found (since CMake 2.8.8)
</pre>
<dt><code>FindCVS</code></p>
<dd>
<p> The module defines the following variables: </p>
<pre>
   CVS_EXECUTABLE - path to cvs command line client
   CVS_FOUND - true if the command line client was found
</pre>
<p> Example usage: </p>
<p>find_package(CVS) if (CVS_FOUND)<br />
    message(&#8220;CVS found: ${CVS_EXECUTABLE}&#8221;)<br />
        endif()</p>
<dt><code>FindCoin3D</code></p>
<dd> Find Coin3D (Open Inventor) </p>
<p> Coin3D is an implementation of the Open Inventor API. It provides data structures and algorithms for 3D visualization <a rel="nofollow" href="http://www.coin3d.org/">http://www.coin3d.org/</a> </p>
<p> This module defines the following variables </p>
<pre>
  COIN3D_FOUND         - system has Coin3D - Open Inventor
  COIN3D_INCLUDE_DIRS  - where the Inventor include directory can be found
  COIN3D_LIBRARIES     - Link to this to use Coin3D
</pre>
<dt><code>FindCups</code></p>
<dd> Try to find the Cups printing system </p>
<p> Once done this will define </p>
<pre>
  CUPS_FOUND - system has Cups
  CUPS_INCLUDE_DIR - the Cups include directory
  CUPS_LIBRARIES - Libraries needed to use Cups
  CUPS_VERSION_STRING - version of Cups found (since CMake 2.8.8)
  Set CUPS_REQUIRE_IPP_DELETE_ATTRIBUTE to TRUE if you need a version which
  features this function (i.e. at least 1.1.19)
</pre>
<dt><code>FindCurses</code></p>
<dd> Find the curses include file and library </p>
<p>  CURSES_FOUND &#8211; system has Curses<br />
  CURSES_INCLUDE_DIR &#8211; the Curses include directory<br />
  CURSES_LIBRARIES &#8211; The libraries needed to use Curses<br />
  CURSES_HAVE_CURSES_H &#8211; true if curses.h is available<br />
  CURSES_HAVE_NCURSES_H &#8211; true if ncurses.h is available<br />
  CURSES_HAVE_NCURSES_NCURSES_H &#8211; true if ncurses/ncurses.h is available<br />
  CURSES_HAVE_NCURSES_CURSES_H &#8211; true if ncurses/curses.h is available<br />
  CURSES_LIBRARY &#8211; set for backwards compatibility with 2.4 CMake</p>
<p> Set CURSES_NEED_NCURSES to TRUE before the find_package() command if NCurses functionality is required. </p>
<dt><code>FindCxxTest</code></p>
<dd> Find CxxTest </p>
<p> Find the CxxTest suite and declare a helper macro for creating unit tests and integrating them with CTest. For more details on CxxTest see <a rel="nofollow" href="http://cxxtest.tigris.org">http://cxxtest.tigris.org</a> </p>
<p> INPUT Variables </p>
<p>   CXXTEST_USE_PYTHON [deprecated since 1.3]<br />
       Only used in the case both Python &amp; Perl<br />
       are detected on the system to control<br />
       which CxxTest code generator is used.<br />
       Valid only for CxxTest version 3.</p>
<pre>
       NOTE: In older versions of this Find Module,
       this variable controlled if the Python test
       generator was used instead of the Perl one,
       regardless of which scripting language the
       user had installed.
</pre>
<pre>
   CXXTEST_TESTGEN_ARGS (since CMake 2.8.3)
       Specify a list of options to pass to the CxxTest code
       generator.  If not defined, --error-printer is
       passed.
</pre>
<p> OUTPUT Variables </p>
<pre>
   CXXTEST_FOUND
       True if the CxxTest framework was found
   CXXTEST_INCLUDE_DIRS
       Where to find the CxxTest include directory
   CXXTEST_PERL_TESTGEN_EXECUTABLE
       The perl-based test generator
   CXXTEST_PYTHON_TESTGEN_EXECUTABLE
       The python-based test generator
   CXXTEST_TESTGEN_EXECUTABLE (since CMake 2.8.3)
       The test generator that is actually used (chosen using user preferences
       and interpreters found in the system)
   CXXTEST_TESTGEN_INTERPRETER (since CMake 2.8.3)
       The full path to the Perl or Python executable on the system
</pre>
<p> MACROS for optional use by CMake users: </p>
<pre>
    CXXTEST_ADD_TEST(&lt;test_name&gt; &lt;gen_source_file&gt; &lt;input_files_to_testgen...&gt;)
       Creates a CxxTest runner and adds it to the CTest testing suite
       Parameters:
           test_name               The name of the test
           gen_source_file         The generated source filename to be
                                   generated by CxxTest
           input_files_to_testgen  The list of header files containing the
                                   CxxTest::TestSuite's to be included in
                                   this runner
</pre>
<p>#== == == == == == ==<br />
Example Usage:</p>
<pre>
           find_package(CxxTest)
           if(CXXTEST_FOUND)
               include_directories(${CXXTEST_INCLUDE_DIR})
               enable_testing()
</pre>
<pre>
               CXXTEST_ADD_TEST(unittest_foo foo_test.cc
                                 ${CMAKE_CURRENT_SOURCE_DIR}/foo_test.h)
               target_link_libraries(unittest_foo foo) # as needed
           endif()
</pre>
<pre>
              This will (if CxxTest is found):
              1. Invoke the testgen executable to autogenerate foo_test.cc in the
                 binary tree from &quot;foo_test.h&quot; in the current source directory.
              2. Create an executable and test called unittest_foo.
</pre>
<p>#== == == == == == =<br />
Example foo_test.h:</p>
<p>#include &lt;cxxtest/TestSuite.h&gt;</p>
<p>class MyTestSuite : public CxxTest::TestSuite<br />
{<br />
  public:<br />
    void testAddition(void)<br />
    {<br />
        TS_ASSERT(1 + 1 &gt; 1);<br />
        TS_ASSERT_EQUALS(1 + 1, 2);<br />
    }<br />
};</p>
<dt><code>FindCygwin</code></p>
<dd> this module looks for Cygwin </p>
<dt><code>FindDCMTK</code></p>
<dd> find DCMTK libraries and applications </p>
<dt><code>FindDart</code></p>
<dd> Find DART </p>
<p> This module looks for the dart testing software and sets DART_ROOT to point to where it found it. </p>
<dt><code>FindDevIL</code></p>
<dd>
<p> This module locates the developer&#8217;s image library. <a rel="nofollow" href="http://openil.sourceforge.net/">http://openil.sourceforge.net/</a> </p>
<p> This module sets: </p>
<p>   IL_LIBRARIES &#8211;   the name of the IL library. These include the full path to<br />
                    the core DevIL library. This one has to be linked into the<br />
                    application.<br />
   ILU_LIBRARIES &#8211;  the name of the ILU library. Again, the full path. This<br />
                    library is for filters and effects, not actual loading. It<br />
                    doesn&#8217;t have to be linked if the functionality it provides<br />
                    is not used.<br />
   ILUT_LIBRARIES &#8211; the name of the ILUT library. Full path. This part of the<br />
                    library interfaces with OpenGL. It is not strictly needed<br />
                    in applications.<br />
   IL_INCLUDE_DIR &#8211; where to find the il.h, ilu.h and ilut.h files.<br />
   IL_FOUND &#8211;       this is set to TRUE if all the above variables were set.<br />
                    This will be set to false if ILU or ILUT are not found,<br />
                    even if they are not needed. In most systems, if one<br />
                    library is found all the others are as well. That&#8217;s the<br />
                    way the DevIL developers release it.</p>
<dt><code>FindDoxygen</code></p>
<dd> This module looks for Doxygen and the path to Graphviz&#8217;s dot </p>
<p> Doxygen is a documentation generation tool. Please see <a rel="nofollow" href="http://www.doxygen.org">http://www.doxygen.org</a> </p>
<p> This module accepts the following optional variables: </p>
<pre>
   DOXYGEN_SKIP_DOT       = If true this module will skip trying to find Dot
                            (an optional component often used by Doxygen)
</pre>
<p> This modules defines the following variables: </p>
<pre>
   DOXYGEN_EXECUTABLE     = The path to the doxygen command.
   DOXYGEN_FOUND          = Was Doxygen found or not?
   DOXYGEN_VERSION        = The version reported by doxygen --version
</pre>
<pre>
   DOXYGEN_DOT_EXECUTABLE = The path to the dot program used by doxygen.
   DOXYGEN_DOT_FOUND      = Was Dot found or not?
   DOXYGEN_DOT_PATH       = The path to dot not including the executable
</pre>
<dt><code>FindEXPAT</code></p>
<dd> Find expat </p>
<p> Find the native EXPAT headers and libraries. </p>
<pre>
  EXPAT_INCLUDE_DIRS - where to find expat.h, etc.
  EXPAT_LIBRARIES    - List of libraries when using expat.
  EXPAT_FOUND        - True if expat found.
</pre>
<dt><code>FindFLEX</code></p>
<dd> Find flex executable and provides a macro to generate custom build rules </p>
<p> The module defines the following variables: </p>
<pre>
  FLEX_FOUND - true is flex executable is found
  FLEX_EXECUTABLE - the path to the flex executable
  FLEX_VERSION - the version of flex
  FLEX_LIBRARIES - The flex libraries
  FLEX_INCLUDE_DIRS - The path to the flex headers
</pre>
<p> The minimum required version of flex can be specified using the standard syntax, e.g. find_package(FLEX 2.5.13) </p>
<p> If flex is found on the system, the module provides the macro: </p>
<pre>
  FLEX_TARGET(Name FlexInput FlexOutput [COMPILE_FLAGS &lt;string&gt;])
</pre>
<p> which creates a custom command to generate the &lt;FlexOutput&gt; file from the &lt;FlexInput&gt; file. If COMPILE_FLAGS option is specified, the next parameter is added to the flex command line. Name is an alias used to get details of this custom command. Indeed the macro defines the following variables: </p>
<p>  FLEX_${Name}_DEFINED &#8211; true is the macro ran successfully<br />
  FLEX_${Name}_OUTPUTS &#8211; the source file generated by the custom rule, an<br />
  alias for FlexOutput<br />
  FLEX_${Name}_INPUT &#8211; the flex source file, an alias for $<br />
  {<br />
      FlexInput<br />
  }</p>
<p> Flex scanners oftenly use tokens defined by Bison: the code generated by Flex depends of the header generated by Bison. This module also defines a macro: </p>
<pre>
  ADD_FLEX_BISON_DEPENDENCY(FlexTarget BisonTarget)
</pre>
<p> which adds the required dependency between a scanner and a parser where &lt;FlexTarget&gt; and &lt;BisonTarget&gt; are the first parameters of respectively FLEX_TARGET and BISON_TARGET macros. </p>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
    Example:</p>
<pre>
   find_package(BISON)
   find_package(FLEX)
</pre>
<p>BISON_TARGET(MyParser parser.y ${CMAKE_CURRENT_BINARY_DIR} / parser.cpp)<br />
FLEX_TARGET(MyScanner lexer.l ${CMAKE_CURRENT_BINARY_DIR} / lexer.cpp)<br />
ADD_FLEX_BISON_DEPENDENCY(MyScanner MyParser)</p>
<p>include_directories(${CMAKE_CURRENT_BINARY_DIR})<br />
        add_executable(Foo<br />
                           Foo.cc<br />
                               ${BISON_MyParser_OUTPUTS} ${FLEX_MyScanner_OUTPUTS}) == ==<br />
    == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==</p>
<dt><code>FindFLTK</code></p>
<dd> Find the native FLTK includes and library </p>
<p> By default FindFLTK.cmake will search for all of the FLTK components and add them to the FLTK_LIBRARIES variable. </p>
<pre>
   You can limit the components which get placed in FLTK_LIBRARIES by
   defining one or more of the following three options:
</pre>
<pre>
     FLTK_SKIP_OPENGL, set to true to disable searching for opengl and
                       the FLTK GL library
     FLTK_SKIP_FORMS, set to true to disable searching for fltk_forms
     FLTK_SKIP_IMAGES, set to true to disable searching for fltk_images
</pre>
<pre>
     FLTK_SKIP_FLUID, set to true if the fluid binary need not be present
                      at build time
</pre>
<p> The following variables will be defined: </p>
<pre>
     FLTK_FOUND, True if all components not skipped were found
     FLTK_INCLUDE_DIR, where to find include files
     FLTK_LIBRARIES, list of fltk libraries you should link against
     FLTK_FLUID_EXECUTABLE, where to find the Fluid tool
     FLTK_WRAP_UI, This enables the FLTK_WRAP_UI command
</pre>
<p> The following cache variables are assigned but should not be used. See the FLTK_LIBRARIES variable instead. </p>
<pre>
     FLTK_BASE_LIBRARY   = the full path to fltk.lib
     FLTK_GL_LIBRARY     = the full path to fltk_gl.lib
     FLTK_FORMS_LIBRARY  = the full path to fltk_forms.lib
     FLTK_IMAGES_LIBRARY = the full path to fltk_images.lib
</pre>
<dt><code>FindFLTK2</code></p>
<dd> Find the native FLTK2 includes and library </p>
<p> The following settings are defined </p>
<pre>
  FLTK2_FLUID_EXECUTABLE, where to find the Fluid tool
  FLTK2_WRAP_UI, This enables the FLTK2_WRAP_UI command
  FLTK2_INCLUDE_DIR, where to find include files
  FLTK2_LIBRARIES, list of fltk2 libraries
  FLTK2_FOUND, Don't use FLTK2 if false.
</pre>
<p> The following settings should not be used in general. </p>
<pre>
  FLTK2_BASE_LIBRARY   = the full path to fltk2.lib
  FLTK2_GL_LIBRARY     = the full path to fltk2_gl.lib
  FLTK2_IMAGES_LIBRARY = the full path to fltk2_images.lib
</pre>
<dt><code>FindFreetype</code></p>
<dd> Locate FreeType library </p>
<p> This module defines </p>
<pre>
  FREETYPE_LIBRARIES, the library to link against
  FREETYPE_FOUND, if false, do not try to link to FREETYPE
  FREETYPE_INCLUDE_DIRS, where to find headers.
  FREETYPE_VERSION_STRING, the version of freetype found (since CMake 2.8.8)
  This is the concatenation of the paths:
  FREETYPE_INCLUDE_DIR_ft2build
  FREETYPE_INCLUDE_DIR_freetype2
</pre>
<p> $FREETYPE_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$FREETYPE_DIR used in building FREETYPE. </p>
<dt><code>FindGCCXML</code></p>
<dd> Find the GCC-XML front-end executable. </p>
<p> This module will define the following variables: </p>
<pre>
  GCCXML - the GCC-XML front-end executable.
</pre>
<dt><code>FindGDAL</code></p>
<dd>
<p> Locate gdal </p>
<p> This module accepts the following environment variables: </p>
<pre>
    GDAL_DIR or GDAL_ROOT - Specify the location of GDAL
</pre>
<p> This module defines the following CMake variables: </p>
<pre>
    GDAL_FOUND - True if libgdal is found
    GDAL_LIBRARY - A variable pointing to the GDAL library
    GDAL_INCLUDE_DIR - Where to find the headers
</pre>
<dt><code>FindGIF</code></p>
<dd>
<p> This module searches giflib and defines GIF_LIBRARIES &#8211; libraries to link to in order to use GIF GIF_FOUND, if false, do not try to link GIF_INCLUDE_DIR, where to find the headers GIF_VERSION, reports either version 4 or 3 (for everything before version 4) </p>
<p> The minimum required version of giflib can be specified using the standard syntax, e.g. find_package(GIF 4) </p>
<p> $GIF_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$GIF_DIR </p>
<dt><code>FindGLEW</code></p>
<dd> Find the OpenGL Extension Wrangler Library (GLEW) </p>
<p> This module defines the following variables: </p>
<pre>
  GLEW_INCLUDE_DIRS - include directories for GLEW
  GLEW_LIBRARIES - libraries to link against GLEW
  GLEW_FOUND - true if GLEW has been found and can be used
</pre>
<dt><code>FindGLUT</code></p>
<dd> try to find glut library and include files </p>
<pre>
  GLUT_INCLUDE_DIR, where to find GL/glut.h, etc.
  GLUT_LIBRARIES, the libraries to link against
  GLUT_FOUND, If false, do not try to use GLUT.
</pre>
<p> Also defined, but not for general use are: </p>
<pre>
  GLUT_glut_LIBRARY = the full path to the glut library.
  GLUT_Xmu_LIBRARY  = the full path to the Xmu library.
  GLUT_Xi_LIBRARY   = the full path to the Xi Library.
</pre>
<dt><code>FindGTK</code></p>
<dd> try to find GTK (and glib) and GTKGLArea </p>
<pre>
  GTK_INCLUDE_DIR   - Directories to include to use GTK
  GTK_LIBRARIES     - Files to link against to use GTK
  GTK_FOUND         - GTK was found
  GTK_GL_FOUND      - GTK's GL features were found
</pre>
<dt><code>FindGTK2</code></p>
<dd> FindGTK2.cmake </p>
<p> This module can find the GTK2 widget libraries and several of its other optional components like gtkmm, glade, and glademm. </p>
<p> NOTE: If you intend to use version checking, CMake 2.6.2 or later is </p>
<pre>
       required.
</pre>
<p> Specify one or more of the following components as you call this find module. See example below. </p>
<pre>
   gtk
   gtkmm
   glade
   glademm
</pre>
<p> The following variables will be defined for your use </p>
<pre>
   GTK2_FOUND - Were all of your specified components found?
   GTK2_INCLUDE_DIRS - All include directories
   GTK2_LIBRARIES - All libraries
   GTK2_DEFINITIONS - Additional compiler flags
</pre>
<pre>
   GTK2_VERSION - The version of GTK2 found (x.y.z)
   GTK2_MAJOR_VERSION - The major version of GTK2
   GTK2_MINOR_VERSION - The minor version of GTK2
   GTK2_PATCH_VERSION - The patch version of GTK2
</pre>
<p> Optional variables you can define prior to calling this module: </p>
<pre>
   GTK2_DEBUG - Enables verbose debugging of the module
   GTK2_ADDITIONAL_SUFFIXES - Allows defining additional directories to
                              search for include files
</pre>
<p> ================= Example Usage: </p>
<pre>
   Call find_package() once, here are some examples to pick from:
</pre>
<pre>
   Require GTK 2.6 or later
       find_package(GTK2 2.6 REQUIRED gtk)
</pre>
<pre>
   Require GTK 2.10 or later and Glade
       find_package(GTK2 2.10 REQUIRED gtk glade)
</pre>
<pre>
   Search for GTK/GTKMM 2.8 or later
       find_package(GTK2 2.8 COMPONENTS gtk gtkmm)
</pre>
<p>if (GTK2_FOUND)<br />
include_directories(${GTK2_INCLUDE_DIRS})<br />
    add_executable(mygui mygui.cc)<br />
        target_link_libraries(mygui ${GTK2_LIBRARIES})<br />
            endif()</p>
<dt><code>FindGTest</code></p>
<dd> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<p> Locate the Google C++ Testing Framework. </p>
<p> Defines the following variables: </p>
<pre>
   GTEST_FOUND - Found the Google Testing framework
   GTEST_INCLUDE_DIRS - Include directories
</pre>
<p> Also defines the library variables below as normal variables. These contain debug/optimized keywords when a debugging library is found. </p>
<pre>
   GTEST_BOTH_LIBRARIES - Both libgtest &amp; libgtest-main
   GTEST_LIBRARIES - libgtest
   GTEST_MAIN_LIBRARIES - libgtest-main
</pre>
<p> Accepts the following variables as input: </p>
<pre>
   GTEST_ROOT - (as a CMake or environment variable)
                The root directory of the gtest install prefix
</pre>
<pre>
   GTEST_MSVC_SEARCH - If compiling with MSVC, this variable can be set to
                       &quot;MD&quot; or &quot;MT&quot; to enable searching a GTest build tree
                       (defaults: &quot;MD&quot;)
</pre>
<p> Example Usage: </p>
<pre>
    enable_testing()
    find_package(GTest REQUIRED)
    include_directories(${GTEST_INCLUDE_DIRS})
</pre>
<pre>
    add_executable(foo foo.cc)
    target_link_libraries(foo ${GTEST_BOTH_LIBRARIES})
</pre>
<pre>
    add_test(AllTestsInFoo foo)
</pre>
<p> If you would like each Google test to show up in CTest as a test you may use the following macro. NOTE: It will slow down your tests by running an executable for each test and test fixture. You will also have to rerun CMake after adding or removing tests or test fixtures. </p>
<p> GTEST_ADD_TESTS(executable extra_args ARGN) </p>
<pre>
    executable = The path to the test executable
    extra_args = Pass a list of extra arguments to be passed to
                 executable enclosed in quotes (or &quot;&quot; for none)
    ARGN =       A list of source files to search for tests &amp; test
                 fixtures.
</pre>
<p>Example : set(FooTestArgs&#8211; foo 1 &#8211;bar 2)<br />
              add_executable(FooTest FooUnitTest.cc)<br />
                  GTEST_ADD_TESTS(FooTest &#8220;${FooTestArgs}&#8221; FooUnitTest.cc)</p>
<dt><code>FindGettext</code></p>
<dd> Find GNU gettext tools </p>
<p> This module looks for the GNU gettext tools. This module defines the following values: </p>
<pre>
  GETTEXT_MSGMERGE_EXECUTABLE: the full path to the msgmerge tool.
  GETTEXT_MSGFMT_EXECUTABLE: the full path to the msgfmt tool.
  GETTEXT_FOUND: True if gettext has been found.
  GETTEXT_VERSION_STRING: the version of gettext found (since CMake 2.8.8)
</pre>
<p> Additionally it provides the following macros: GETTEXT_CREATE_TRANSLATIONS ( outputFile [ALL] file1 &#8230; fileN ) </p>
<pre>
    This will create a target &quot;translations&quot; which will convert the
    given input po files into the binary output mo file. If the
    ALL option is used, the translations will also be created when
    building the default target.
</pre>
<p> GETTEXT_PROCESS_POT( &lt;potfile&gt; [ALL] [INSTALL_DESTINATION &lt;destdir&gt;] LANGUAGES &lt;lang1&gt; &lt;lang2&gt; &#8230; ) </p>
<pre>
     Process the given pot file to mo files.
     If INSTALL_DESTINATION is given then automatically install rules will be created,
     the language subdirectory will be taken into account (by default use share/locale/).
     If ALL is specified, the pot file is processed when building the all traget.
     It creates a custom target &quot;potfile&quot;.
</pre>
<p> GETTEXT_PROCESS_PO_FILES( &lt;lang&gt; [ALL] [INSTALL_DESTINATION &lt;dir&gt;] PO_FILES &lt;po1&gt; &lt;po2&gt; &#8230; ) </p>
<pre>
     Process the given po files to mo files for the given language.
     If INSTALL_DESTINATION is given then automatically install rules will be created,
     the language subdirectory will be taken into account (by default use share/locale/).
     If ALL is specified, the po files are processed when building the all traget.
     It creates a custom target &quot;pofiles&quot;.
</pre>
<dt><code>FindGit</code></p>
<dd>
<p> The module defines the following variables: </p>
<pre>
   GIT_EXECUTABLE - path to git command line client
   GIT_FOUND - true if the command line client was found
   GIT_VERSION_STRING - the version of git found (since CMake 2.8.8)
</pre>
<p> Example usage: </p>
<p>find_package(Git) if (GIT_FOUND)<br />
    message(&#8220;git found: ${GIT_EXECUTABLE}&#8221;)<br />
        endif()</p>
<dt><code>FindGnuTLS</code></p>
<dd> Try to find the GNU Transport Layer Security library (gnutls) </p>
<p> Once done this will define </p>
<pre>
  GNUTLS_FOUND - System has gnutls
  GNUTLS_INCLUDE_DIR - The gnutls include directory
  GNUTLS_LIBRARIES - The libraries needed to use gnutls
  GNUTLS_DEFINITIONS - Compiler switches required for using gnutls
</pre>
<dt><code>FindGnuplot</code></p>
<dd> this module looks for gnuplot </p>
<p> Once done this will define </p>
<pre>
  GNUPLOT_FOUND - system has Gnuplot
  GNUPLOT_EXECUTABLE - the Gnuplot executable
  GNUPLOT_VERSION_STRING - the version of Gnuplot found (since CMake 2.8.8)
</pre>
<p> GNUPLOT_VERSION_STRING will not work for old versions like 3.7.1. </p>
<dt><code>FindHDF5</code></p>
<dd> Find HDF5, a library for reading and writing self describing array data. </p>
<p> This module invokes the HDF5 wrapper compiler that should be installed alongside HDF5. Depending upon the HDF5 Configuration, the wrapper compiler is called either h5cc or h5pcc. If this succeeds, the module will then call the compiler with the -show argument to see what flags are used when compiling an HDF5 client application. </p>
<p> The module will optionally accept the COMPONENTS argument. If no COMPONENTS are specified, then the find module will default to finding only the HDF5 C library. If one or more COMPONENTS are specified, the module will attempt to find the language bindings for the specified components. The only valid components are C, CXX, Fortran, HL, and Fortran_HL. If the COMPONENTS argument is not given, the module will attempt to find only the C bindings. </p>
<p> On UNIX systems, this module will read the variable HDF5_USE_STATIC_LIBRARIES to determine whether or not to prefer a static link to a dynamic link for HDF5 and all of it&#8217;s dependencies. To use this feature, make sure that the HDF5_USE_STATIC_LIBRARIES variable is set before the call to find_package. </p>
<p> To provide the module with a hint about where to find your HDF5 installation, you can set the environment variable HDF5_ROOT. The Find module will then look in this path when searching for HDF5 executables, paths, and libraries. </p>
<p> In addition to finding the includes and libraries required to compile an HDF5 client application, this module also makes an effort to find tools that come with the HDF5 distribution that may be useful for regression testing. </p>
<p> This module will define the following variables: </p>
<p>  HDF5_INCLUDE_DIRS &#8211; Location of the hdf5 includes<br />
  HDF5_INCLUDE_DIR &#8211; Location of the hdf5 includes (deprecated)<br />
  HDF5_DEFINITIONS &#8211; Required compiler definitions for HDF5<br />
  HDF5_C_LIBRARIES &#8211; Required libraries for the HDF5 C bindings.<br />
  HDF5_CXX_LIBRARIES &#8211; Required libraries for the HDF5 C++ bindings<br />
  HDF5_Fortran_LIBRARIES &#8211; Required libraries for the HDF5 Fortran bindings<br />
  HDF5_HL_LIBRARIES &#8211; Required libraries for the HDF5 high level API<br />
  HDF5_Fortran_HL_LIBRARIES &#8211; Required libraries for the high level Fortran<br />
                              bindings.<br />
  HDF5_LIBRARIES &#8211; Required libraries for all requested bindings<br />
  HDF5_FOUND &#8211; true if HDF5 was found on the system<br />
  HDF5_LIBRARY_DIRS &#8211; the full set of library directories<br />
  HDF5_IS_PARALLEL &#8211; Whether or not HDF5 was found with parallel IO support<br />
  HDF5_C_COMPILER_EXECUTABLE &#8211; the path to the HDF5 C wrapper compiler<br />
  HDF5_CXX_COMPILER_EXECUTABLE &#8211; the path to the HDF5 C++ wrapper compiler<br />
  HDF5_Fortran_COMPILER_EXECUTABLE &#8211; the path to the HDF5 Fortran wrapper compiler<br />
  HDF5_DIFF_EXECUTABLE &#8211; the path to the HDF5 dataset comparison tool</p>
<dt><code>FindHSPELL</code></p>
<dd> Try to find Hspell </p>
<p> Once done this will define </p>
<pre>
  HSPELL_FOUND - system has Hspell
  HSPELL_INCLUDE_DIR - the Hspell include directory
  HSPELL_LIBRARIES - The libraries needed to use Hspell
  HSPELL_DEFINITIONS - Compiler switches required for using Hspell
</pre>
<pre>
  HSPELL_VERSION_STRING - The version of Hspell found (x.y)
  HSPELL_MAJOR_VERSION  - the major version of Hspell
  HSPELL_MINOR_VERSION  - The minor version of Hspell
</pre>
<dt><code>FindHTMLHelp</code></p>
<dd> This module looks for Microsoft HTML Help Compiler </p>
<p> It defines: </p>
<pre>
   HTML_HELP_COMPILER     : full path to the Compiler (hhc.exe)
   HTML_HELP_INCLUDE_PATH : include path to the API (htmlhelp.h)
   HTML_HELP_LIBRARY      : full path to the library (htmlhelp.lib)
</pre>
<dt><code>FindHg</code></p>
<dd>
<p> The module defines the following variables: </p>
<pre>
   HG_EXECUTABLE - path to mercurial command line client (hg)
   HG_FOUND - true if the command line client was found
   HG_VERSION_STRING - the version of mercurial found
</pre>
<p> Example usage: </p>
<p>find_package(Hg) if (HG_FOUND)<br />
    message(&#8220;hg found: ${HG_EXECUTABLE}&#8221;)<br />
        endif()</p>
<dt><code>FindITK</code></p>
<dd> Find an ITK installation or build tree. </p>
<dt><code>FindIcotool</code></p>
<dd> Find icotool </p>
<p> This module looks for icotool. This module defines the following values: </p>
<pre>
  ICOTOOL_EXECUTABLE: the full path to the icotool tool.
  ICOTOOL_FOUND: True if icotool has been found.
  ICOTOOL_VERSION_STRING: the version of icotool found.
</pre>
<dt><code>FindImageMagick</code></p>
<dd> Find the ImageMagick binary suite. </p>
<p> This module will search for a set of ImageMagick tools specified as components in the FIND_PACKAGE call. Typical components include, but are not limited to (future versions of ImageMagick might have additional components not listed here): </p>
<pre>
  animate
  compare
  composite
  conjure
  convert
  display
  identify
  import
  mogrify
  montage
  stream
</pre>
<p> If no component is specified in the FIND_PACKAGE call, then it only searches for the ImageMagick executable directory. This code defines the following variables: </p>
<pre>
  ImageMagick_FOUND                  - TRUE if all components are found.
  ImageMagick_EXECUTABLE_DIR         - Full path to executables directory.
  ImageMagick_&lt;component&gt;_FOUND      - TRUE if &lt;component&gt; is found.
  ImageMagick_&lt;component&gt;_EXECUTABLE - Full path to &lt;component&gt; executable.
  ImageMagick_VERSION_STRING         - the version of ImageMagick found
                                       (since CMake 2.8.8)
</pre>
<p> ImageMagick_VERSION_STRING will not work for old versions like 5.2.3. </p>
<p> There are also components for the following ImageMagick APIs: </p>
<pre>
  Magick++
  MagickWand
  MagickCore
</pre>
<p> For these components the following variables are set: </p>
<p>ImageMagick_FOUND &#8211; TRUE if all components are found.ImageMagick_INCLUDE_DIRS &#8211; Full paths to all include dirs.ImageMagick_LIBRARIES &#8211; Full paths to all libraries.ImageMagick_&lt;component&gt; _FOUND &#8211; TRUE if&lt;component&gt; is found.ImageMagick_&lt;component&gt; _INCLUDE_DIRS &#8211; Full path to&lt;component&gt; include dirs.ImageMagick_&lt;component&gt; _LIBRARIES &#8211; Full path to&lt;component&gt; libraries.</p>
<p> Example Usages: </p>
<pre>
  find_package(ImageMagick)
  find_package(ImageMagick COMPONENTS convert)
  find_package(ImageMagick COMPONENTS convert mogrify display)
  find_package(ImageMagick COMPONENTS Magick++)
  find_package(ImageMagick COMPONENTS Magick++ convert)
</pre>
<p> Note that the standard FIND_PACKAGE features are supported (i.e., QUIET, REQUIRED, etc.). </p>
<dt><code>FindJNI</code></p>
<dd> Find JNI java libraries. </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<p>JNI_INCLUDE_DIRS = the include dirs to use<br />
    JNI_LIBRARIES = the libraries to use<br />
        JNI_FOUND = TRUE if JNI headers and libraries were found.JAVA_AWT_LIBRARY = the path to the jawt library<br />
            JAVA_JVM_LIBRARY = the path to the jvm library<br />
                JAVA_INCLUDE_PATH = the include path to jni.h<br />
                                        JAVA_INCLUDE_PATH2 = the include path to jni_md.h<br />
                                                                 JAVA_AWT_INCLUDE_PATH = the include path to jawt.h</p>
<dt><code>FindJPEG</code></p>
<dd> Find JPEG </p>
<p> Find the native JPEG includes and library This module defines </p>
<pre>
  JPEG_INCLUDE_DIR, where to find jpeglib.h, etc.
  JPEG_LIBRARIES, the libraries needed to use JPEG.
  JPEG_FOUND, If false, do not try to use JPEG.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  JPEG_LIBRARY, where to find the JPEG library.
</pre>
<dt><code>FindJasper</code></p>
<dd> Try to find the Jasper JPEG2000 library </p>
<p> Once done this will define </p>
<pre>
  JASPER_FOUND - system has Jasper
  JASPER_INCLUDE_DIR - the Jasper include directory
  JASPER_LIBRARIES - the libraries needed to use Jasper
  JASPER_VERSION_STRING - the version of Jasper found (since CMake 2.8.8)
</pre>
<dt><code>FindJava</code></p>
<dd> Find Java </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. This code sets the following variables: </p>
<pre>
  Java_JAVA_EXECUTABLE    = the full path to the Java runtime
  Java_JAVAC_EXECUTABLE   = the full path to the Java compiler
  Java_JAVAH_EXECUTABLE   = the full path to the Java header generator
  Java_JAVADOC_EXECUTABLE = the full path to the Java documention generator
  Java_JAR_EXECUTABLE     = the full path to the Java archiver
  Java_VERSION_STRING     = Version of the package found (java version), eg. 1.6.0_12
  Java_VERSION_MAJOR      = The major version of the package found.
  Java_VERSION_MINOR      = The minor version of the package found.
  Java_VERSION_PATCH      = The patch version of the package found.
  Java_VERSION_TWEAK      = The tweak version of the package found (after '_')
  Java_VERSION            = This is set to: $major.$minor.$patch(.$tweak)
</pre>
<p> The minimum required version of Java can be specified using the standard CMake syntax, e.g. find_package(Java 1.5) </p>
<p> NOTE: ${Java_VERSION} and ${Java_VERSION_STRING} are not guaranteed to be identical. For example some java version may return: Java_VERSION_STRING = 1.5.0_17 and Java_VERSION = 1.5.0.17 </p>
<p> another example is the Java OEM, with: Java_VERSION_STRING = 1.6.0-oem and Java_VERSION = 1.6.0 </p>
<p> For these components the following variables are set: </p>
<pre>
  Java_FOUND                    - TRUE if all components are found.
  Java_INCLUDE_DIRS             - Full paths to all include dirs.
  Java_LIBRARIES                - Full paths to all libraries.
  Java_&lt;component&gt;_FOUND        - TRUE if &lt;component&gt; is found.
</pre>
<p> Example Usages: </p>
<pre>
  find_package(Java)
  find_package(Java COMPONENTS Runtime)
  find_package(Java COMPONENTS Development)
</pre>
<dt><code>FindKDE3</code></p>
<dd> Find the KDE3 include and library dirs, KDE preprocessors and define a some macros </p>
<p> This module defines the following variables: </p>
<p>  KDE3_DEFINITIONS         &#8211; compiler definitions required for compiling KDE software<br />
  KDE3_INCLUDE_DIR         &#8211; the KDE include directory<br />
  KDE3_INCLUDE_DIRS        &#8211; the KDE and the Qt include directory, for use with include_directories()<br />
  KDE3_LIB_DIR             &#8211; the directory where the KDE libraries are installed, for use with link_directories()<br />
  QT_AND_KDECORE_LIBS      &#8211; this contains both the Qt and the kdecore library<br />
  KDE3_DCOPIDL_EXECUTABLE  &#8211; the dcopidl executable<br />
  KDE3_DCOPIDL2CPP_EXECUTABLE &#8211; the dcopidl2cpp executable<br />
  KDE3_KCFGC_EXECUTABLE    &#8211; the kconfig_compiler executable<br />
  KDE3_FOUND               &#8211; set to TRUE if all of the above has been found</p>
<p> The following user adjustable options are provided: </p>
<pre>
  KDE3_BUILD_TESTS - enable this to build KDE testcases
</pre>
<p> It also adds the following macros (from KDE3Macros.cmake) SRCS_VAR is always the variable which contains the list of source files for your application or library. </p>
<p> KDE3_AUTOMOC(file1 &#8230; fileN) </p>
<pre>
    Call this if you want to have automatic moc file handling.
    This means if you include &quot;foo.moc&quot; in the source file foo.cpp
    a moc file for the header foo.h will be created automatically.
    You can set the property SKIP_AUTOMAKE using set_source_files_properties()
    to exclude some files in the list from being processed.
</pre>
<p> KDE3_ADD_MOC_FILES(SRCS_VAR file1 &#8230; fileN ) </p>
<pre>
    If you don't use the KDE3_AUTOMOC() macro, for the files
    listed here moc files will be created (named &quot;foo.moc.cpp&quot;)
</pre>
<p> KDE3_ADD_DCOP_SKELS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>
    Use this to generate DCOP skeletions from the listed headers.
</pre>
<p> KDE3_ADD_DCOP_STUBS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>
     Use this to generate DCOP stubs from the listed headers.
</pre>
<p> KDE3_ADD_UI_FILES(SRCS_VAR file1.ui &#8230; fileN.ui ) </p>
<pre>
    Use this to add the Qt designer ui files to your application/library.
</pre>
<p> KDE3_ADD_KCFG_FILES(SRCS_VAR file1.kcfgc &#8230; fileN.kcfgc ) </p>
<pre>
    Use this to add KDE kconfig compiler files to your application/library.
</pre>
<p> KDE3_INSTALL_LIBTOOL_FILE(target) </p>
<pre>
    This will create and install a simple libtool file for the given target.
</pre>
<p> KDE3_ADD_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>
    Currently identical to add_executable(), may provide some advanced features in the future.
</pre>
<p> KDE3_ADD_KPART(name [WITH_PREFIX] file1 &#8230; fileN ) </p>
<pre>
    Create a KDE plugin (KPart, kioslave, etc.) from the given source files.
    If WITH_PREFIX is given, the resulting plugin will have the prefix &quot;lib&quot;, otherwise it won't.
    It creates and installs an appropriate libtool la-file.
</pre>
<p> KDE3_ADD_KDEINIT_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>
    Create a KDE application in the form of a module loadable via kdeinit.
    A library named kdeinit_&lt;name&gt; will be created and a small executable which links to it.
</pre>
<p> The option KDE3_ENABLE_FINAL to enable all-in-one compilation is no longer supported. </p>
<p> Author: Alexander Neundorf &lt;neundorf [at] kde.org&gt; </p>
<dt><code>FindKDE4</code></p>
<dd>
<p> Find KDE4 and provide all necessary variables and macros to compile software for it. It looks for KDE 4 in the following directories in the given order: </p>
<pre>
  CMAKE_INSTALL_PREFIX
  KDEDIRS
  /opt/kde4
</pre>
<p> Please look in FindKDE4Internal.cmake and KDE4Macros.cmake for more information. They are installed with the KDE 4 libraries in $KDEDIRS/share/apps/cmake/modules/. </p>
<p> Author: Alexander Neundorf &lt;neundorf [at] kde.org&gt; </p>
<dt><code>FindLAPACK</code></p>
<dd> Find LAPACK library </p>
<p> This module finds an installed fortran library that implements the LAPACK linear-algebra interface (see <a rel="nofollow" href="http://www.netlib.org/lapack/">http://www.netlib.org/lapack/</a>). </p>
<p> The approach follows that taken for the autoconf macro file, acx_lapack.m4 (distributed at <a rel="nofollow" href="http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html">http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html</a>). </p>
<p> This module sets the following variables: </p>
<p>  LAPACK_FOUND &#8211; set to true if a library implementing the LAPACK interface<br />
    is found<br />
  LAPACK_LINKER_FLAGS &#8211; uncached list of required linker flags (excluding -l<br />
    and -L).<br />
  LAPACK_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use LAPACK<br />
  LAPACK95_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use LAPACK95<br />
  LAPACK95_FOUND &#8211; set to true if a library implementing the LAPACK f95<br />
    interface is found<br />
  BLA_STATIC  if set on this determines what kind of linkage we do (static)<br />
  BLA_VENDOR  if set checks only the specified vendor, if not set checks<br />
     all the possibilities<br />
  BLA_F95     if set on tries to find the f95 interfaces for BLAS/LAPACK</p>
<dt><code>FindLATEX</code></p>
<dd> Find Latex </p>
<p> This module finds if Latex is installed and determines where the executables are. This code sets the following variables: </p>
<pre>
  LATEX_COMPILER:       path to the LaTeX compiler
  PDFLATEX_COMPILER:    path to the PdfLaTeX compiler
  BIBTEX_COMPILER:      path to the BibTeX compiler
  MAKEINDEX_COMPILER:   path to the MakeIndex compiler
  DVIPS_CONVERTER:      path to the DVIPS converter
  PS2PDF_CONVERTER:     path to the PS2PDF converter
  LATEX2HTML_CONVERTER: path to the LaTeX2Html converter
</pre>
<dt><code>FindLibArchive</code></p>
<dd> Find libarchive library and headers </p>
<p> The module defines the following variables: </p>
<pre>
  LibArchive_FOUND        - true if libarchive was found
  LibArchive_INCLUDE_DIRS - include search path
  LibArchive_LIBRARIES    - libraries to link
  LibArchive_VERSION      - libarchive 3-component version number
</pre>
<dt><code>FindLibLZMA</code></p>
<dd> Find LibLZMA </p>
<p> Find LibLZMA headers and library </p>
<p>LIBLZMA_FOUND &#8211; True if liblzma is found.LIBLZMA_INCLUDE_DIRS &#8211; Directory where liblzma headers are located.LIBLZMA_LIBRARIES &#8211; Lzma libraries to link against.LIBLZMA_HAS_AUTO_DECODER &#8211; True if lzma_auto_decoder () is found(required).LIBLZMA_HAS_EASY_ENCODER &#8211; True if lzma_easy_encoder () is found(required).LIBLZMA_HAS_LZMA_PRESET &#8211; True if lzma_lzma_preset () is found(required).LIBLZMA_VERSION_MAJOR &#8211; The major version of lzma LIBLZMA_VERSION_MINOR &#8211; The minor version of lzma LIBLZMA_VERSION_PATCH &#8211; The patch version of lzma LIBLZMA_VERSION_STRING &#8211; version number as a string(ex<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        : &#8220;5.0.3&#8221;)</p>
<dt><code>FindLibXml2</code></p>
<dd> Try to find the LibXml2 xml processing library </p>
<p> Once done this will define </p>
<pre>
  LIBXML2_FOUND - System has LibXml2
  LIBXML2_INCLUDE_DIR - The LibXml2 include directory
  LIBXML2_LIBRARIES - The libraries needed to use LibXml2
  LIBXML2_DEFINITIONS - Compiler switches required for using LibXml2
  LIBXML2_XMLLINT_EXECUTABLE - The XML checking tool xmllint coming with LibXml2
  LIBXML2_VERSION_STRING - the version of LibXml2 found (since CMake 2.8.8)
</pre>
<dt><code>FindLibXslt</code></p>
<dd> Try to find the LibXslt library </p>
<p> Once done this will define </p>
<pre>
  LIBXSLT_FOUND - system has LibXslt
  LIBXSLT_INCLUDE_DIR - the LibXslt include directory
  LIBXSLT_LIBRARIES - Link these to LibXslt
  LIBXSLT_DEFINITIONS - Compiler switches required for using LibXslt
  LIBXSLT_VERSION_STRING - version of LibXslt found (since CMake 2.8.8)
</pre>
<p> Additionally, the following two variables are set (but not required for using xslt): </p>
<pre>
  LIBXSLT_EXSLT_LIBRARIES - Link to these if you need to link against the exslt library
  LIBXSLT_XSLTPROC_EXECUTABLE - Contains the full path to the xsltproc executable if found
</pre>
<dt><code>FindLua50</code></p>
<dd>
<p> Locate Lua library This module defines </p>
<pre>
  LUA50_FOUND, if false, do not try to link to Lua
  LUA_LIBRARIES, both lua and lualib
  LUA_INCLUDE_DIR, where to find lua.h and lualib.h (and probably lauxlib.h)
</pre>
<p> Note that the expected include convention is </p>
<p>#include &#8220;lua.h&#8221;</p>
<p> and not </p>
<p>#include &lt;lua/lua.h&gt;</p>
<p> This is because, the lua location is not standardized and may exist in locations other than lua/ </p>
<dt><code>FindLua51</code></p>
<dd>
<p> Locate Lua library This module defines </p>
<pre>
  LUA51_FOUND, if false, do not try to link to Lua
  LUA_LIBRARIES
  LUA_INCLUDE_DIR, where to find lua.h
  LUA_VERSION_STRING, the version of Lua found (since CMake 2.8.8)
</pre>
<p> Note that the expected include convention is </p>
<p>#include &#8220;lua.h&#8221;</p>
<p> and not </p>
<p>#include &lt;lua/lua.h&gt;</p>
<p> This is because, the lua location is not standardized and may exist in locations other than lua/ </p>
<dt><code>FindMFC</code></p>
<dd> Find MFC on Windows </p>
<p> Find the native MFC &#8211; i.e. decide if an application can link to the MFC libraries. </p>
<pre>
  MFC_FOUND - Was MFC support found
</pre>
<p> You don&#8217;t need to include anything or link anything to use it. </p>
<dt><code>FindMPEG</code></p>
<dd> Find the native MPEG includes and library </p>
<p> This module defines </p>
<pre>
  MPEG_INCLUDE_DIR, where to find MPEG.h, etc.
  MPEG_LIBRARIES, the libraries required to use MPEG.
  MPEG_FOUND, If false, do not try to use MPEG.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  MPEG_mpeg2_LIBRARY, where to find the MPEG library.
  MPEG_vo_LIBRARY, where to find the vo library.
</pre>
<dt><code>FindMPEG2</code></p>
<dd> Find the native MPEG2 includes and library </p>
<p> This module defines </p>
<pre>
  MPEG2_INCLUDE_DIR, path to mpeg2dec/mpeg2.h, etc.
  MPEG2_LIBRARIES, the libraries required to use MPEG2.
  MPEG2_FOUND, If false, do not try to use MPEG2.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  MPEG2_mpeg2_LIBRARY, where to find the MPEG2 library.
  MPEG2_vo_LIBRARY, where to find the vo library.
</pre>
<dt><code>FindMPI</code></p>
<dd> Find a Message Passing Interface (MPI) implementation </p>
<p> The Message Passing Interface (MPI) is a library used to write high-performance distributed-memory parallel applications, and is typically deployed on a cluster. MPI is a standard interface (defined by the MPI forum) for which many implementations are available. All of them have somewhat different include paths, libraries to link against, etc., and this module tries to smooth out those differences. </p>
<p> === Variables === </p>
<p> This module will set the following variables per language in your project, where &lt;lang&gt; is one of C, CXX, or Fortran: </p>
<p>   MPI_&lt;lang&gt;_FOUND           TRUE if FindMPI found MPI flags for &lt;lang&gt;<br />
   MPI_&lt;lang&gt;_COMPILER        MPI Compiler wrapper for &lt;lang&gt;<br />
   MPI_&lt;lang&gt;_COMPILE_FLAGS   Compilation flags for MPI programs<br />
   MPI_&lt;lang&gt;_INCLUDE_PATH    Include path(s) for MPI header<br />
   MPI_&lt;lang&gt;_LINK_FLAGS      Linking flags for MPI programs<br />
   MPI_&lt;lang&gt;_LIBRARIES       All libraries to link MPI programs against</p>
<p> Additionally, FindMPI sets the following variables for running MPI programs from the command line: </p>
<pre>
   MPIEXEC                    Executable for running MPI programs
   MPIEXEC_NUMPROC_FLAG       Flag to pass to MPIEXEC before giving
                              it the number of processors to run on
   MPIEXEC_PREFLAGS           Flags to pass to MPIEXEC directly
                              before the executable to run.
   MPIEXEC_POSTFLAGS          Flags to pass to MPIEXEC after other flags
</pre>
<p> === Usage === </p>
<p> To use this module, simply call FindMPI from a CMakeLists.txt file, or run find_package(MPI), then run CMake. If you are happy with the auto- detected configuration for your language, then you&#8217;re done. If not, you have two options: </p>
<pre>
   1. Set MPI_&lt;lang&gt;_COMPILER to the MPI wrapper (mpicc, etc.) of your
      choice and reconfigure.  FindMPI will attempt to determine all the
      necessary variables using THAT compiler's compile and link flags.
   2. If this fails, or if your MPI implementation does not come with
      a compiler wrapper, then set both MPI_&lt;lang&gt;_LIBRARIES and
      MPI_&lt;lang&gt;_INCLUDE_PATH.  You may also set any other variables
      listed above, but these two are required.  This will circumvent
      autodetection entirely.
</pre>
<p> When configuration is successful, MPI_&lt;lang&gt;_COMPILER will be set to the compiler wrapper for &lt;lang&gt;, if it was found. MPI_&lt;lang&gt;_FOUND and other variables above will be set if any MPI implementation was found for &lt;lang&gt;, regardless of whether a compiler was found. </p>
<p> When using MPIEXEC to execute MPI applications, you should typically use all of the MPIEXEC flags as follows: </p>
<p>${MPIEXEC} ${MPIEXEC_NUMPROC_FLAG} PROCS<br />
    ${MPIEXEC_PREFLAGS} EXECUTABLE ${MPIEXEC_POSTFLAGS} ARGS</p>
<p> where PROCS is the number of processors on which to execute the program, EXECUTABLE is the MPI program, and ARGS are the arguments to pass to the MPI program. </p>
<p> === Backward Compatibility === </p>
<p> For backward compatibility with older versions of FindMPI, these variables are set, but deprecated: </p>
<pre>
   MPI_FOUND           MPI_COMPILER        MPI_LIBRARY
   MPI_COMPILE_FLAGS   MPI_INCLUDE_PATH    MPI_EXTRA_LIBRARY
   MPI_LINK_FLAGS      MPI_LIBRARIES
</pre>
<p> In new projects, please use the MPI_&lt;lang&gt;_XXX equivalents. </p>
<dt><code>FindMatlab</code></p>
<dd> this module looks for Matlab </p>
<p> Defines: </p>
<pre>
  MATLAB_INCLUDE_DIR: include path for mex.h, engine.h
  MATLAB_LIBRARIES:   required libraries: libmex, etc
  MATLAB_MEX_LIBRARY: path to libmex.lib
  MATLAB_MX_LIBRARY:  path to libmx.lib
  MATLAB_ENG_LIBRARY: path to libeng.lib
</pre>
<dt><code>FindMotif</code></p>
<dd> Try to find Motif (or lesstif) </p>
<p> Once done this will define: </p>
<pre>
  MOTIF_FOUND        - system has MOTIF
  MOTIF_INCLUDE_DIR  - include paths to use Motif
  MOTIF_LIBRARIES    - Link these to use Motif
</pre>
<dt><code>FindOpenAL</code></p>
<dd>
<p> Locate OpenAL This module defines OPENAL_LIBRARY OPENAL_FOUND, if false, do not try to link to OpenAL OPENAL_INCLUDE_DIR, where to find the headers </p>
<p> $OPENALDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENALDIR used in building OpenAL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module. </p>
<dt><code>FindOpenGL</code></p>
<dd> Try to find OpenGL </p>
<p> Once done this will define </p>
<pre>
  OPENGL_FOUND        - system has OpenGL
  OPENGL_XMESA_FOUND  - system has XMESA
  OPENGL_GLU_FOUND    - system has GLU
  OPENGL_INCLUDE_DIR  - the GL include directory
  OPENGL_LIBRARIES    - Link these to use OpenGL and GLU
</pre>
<p> If you want to use just GL you can use these values </p>
<pre>
  OPENGL_gl_LIBRARY   - Path to OpenGL Library
  OPENGL_glu_LIBRARY  - Path to GLU Library
</pre>
<p> On OSX default to using the framework version of opengl People will have to change the cache values of OPENGL_glu_LIBRARY and OPENGL_gl_LIBRARY to use OpenGL with X11 on OSX </p>
<dt><code>FindOpenMP</code></p>
<dd> Finds OpenMP support </p>
<p> This module can be used to detect OpenMP support in a compiler. If the compiler supports OpenMP, the flags required to compile with OpenMP support are returned in variables for the different languages. The variables may be empty if the compiler does not need a special flag to support OpenMP. </p>
<p> The following variables are set: </p>
<pre>
   OpenMP_C_FLAGS - flags to add to the C compiler for OpenMP support
   OpenMP_CXX_FLAGS - flags to add to the CXX compiler for OpenMP support
   OPENMP_FOUND - true if openmp is detected
</pre>
<p> Supported compilers can be found at <a rel="nofollow" href="http://openmp.org/wp/openmp-compilers/">http://openmp.org/wp/openmp-compilers/</a> </p>
<dt><code>FindOpenSSL</code></p>
<dd> Try to find the OpenSSL encryption library </p>
<p> Once done this will define </p>
<pre>
  OPENSSL_ROOT_DIR - Set this variable to the root installation of OpenSSL
</pre>
<p> Read-Only variables: </p>
<pre>
  OPENSSL_FOUND - system has the OpenSSL library
  OPENSSL_INCLUDE_DIR - the OpenSSL include directory
  OPENSSL_LIBRARIES - The libraries needed to use OpenSSL
  OPENSSL_VERSION - This is set to $major.$minor.$revision$path (eg. 0.9.8s)
</pre>
<dt><code>FindOpenSceneGraph</code></p>
<dd> Find OpenSceneGraph </p>
<p> This module searches for the OpenSceneGraph core &quot;osg&quot; library as well as OpenThreads, and whatever additional COMPONENTS (nodekits) that you specify. </p>
<pre>
    See <a rel="nofollow" href="http://www.openscenegraph.org">http://www.openscenegraph.org</a>
</pre>
<p> NOTE: To use this module effectively you must either require CMake &gt;= 2.6.3 with cmake_minimum_required(VERSION 2.6.3) or download and place FindOpenThreads.cmake, Findosg_functions.cmake, Findosg.cmake, and Find&lt;etc&gt;.cmake files into your CMAKE_MODULE_PATH. </p>
<p> ================================== </p>
<p> This module accepts the following variables (note mixed case) </p>
<pre>
    OpenSceneGraph_DEBUG - Enable debugging output
</pre>
<pre>
    OpenSceneGraph_MARK_AS_ADVANCED - Mark cache variables as advanced
                                      automatically
</pre>
<p> The following environment variables are also respected for finding the OSG and it&#8217;s various components. CMAKE_PREFIX_PATH can also be used for this (see find_library() CMake documentation). </p>
<pre>
    &lt;MODULE&gt;_DIR (where MODULE is of the form &quot;OSGVOLUME&quot; and there is a FindosgVolume.cmake file)
    OSG_DIR
    OSGDIR
    OSG_ROOT
</pre>
<p> [CMake 2.8.10]: The CMake variable OSG_DIR can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
<p> This module defines the following output variables: </p>
<pre>
    OPENSCENEGRAPH_FOUND - Was the OSG and all of the specified components found?
</pre>
<pre>
    OPENSCENEGRAPH_VERSION - The version of the OSG which was found
</pre>
<pre>
    OPENSCENEGRAPH_INCLUDE_DIRS - Where to find the headers
</pre>
<pre>
    OPENSCENEGRAPH_LIBRARIES - The OSG libraries
</pre>
<p> ================================== Example Usage: </p>
<pre>
  find_package(OpenSceneGraph 2.0.0 REQUIRED osgDB osgUtil)
      # libOpenThreads &amp; libosg automatically searched
  include_directories(${OPENSCENEGRAPH_INCLUDE_DIRS})
</pre>
<pre>
  add_executable(foo foo.cc)
  target_link_libraries(foo ${OPENSCENEGRAPH_LIBRARIES})
</pre>
<dt><code>FindOpenThreads</code></p>
<dd>
<p> OpenThreads is a C++ based threading library. Its largest userbase seems to OpenSceneGraph so you might notice I accept OSGDIR as an environment path. I consider this part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. </p>
<p> Locate OpenThreads This module defines OPENTHREADS_LIBRARY OPENTHREADS_FOUND, if false, do not try to link to OpenThreads OPENTHREADS_INCLUDE_DIR, where to find the headers </p>
<p> $OPENTHREADS_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENTHREADS_DIR used in building osg. </p>
<p> [CMake 2.8.10]: The CMake variables OPENTHREADS_DIR or OSG_DIR can now be used as well to influence detection, instead of needing to specify an environment variable. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindPHP4</code></p>
<dd> Find PHP4 </p>
<p> This module finds if PHP4 is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PHP4_INCLUDE_PATH       = path to where php.h can be found
  PHP4_EXECUTABLE         = full path to the php4 binary
</pre>
<dt><code>FindPNG</code></p>
<dd> Find the native PNG includes and library </p>
<p> This module searches libpng, the library for working with PNG images. </p>
<p> It defines the following variables </p>
<pre>
  PNG_INCLUDE_DIRS, where to find png.h, etc.
  PNG_LIBRARIES, the libraries to link against to use PNG.
  PNG_DEFINITIONS - You should add_definitons(${PNG_DEFINITIONS}) before compiling code that includes png library files.
  PNG_FOUND, If false, do not try to use PNG.
  PNG_VERSION_STRING - the version of the PNG library found (since CMake 2.8.8)
</pre>
<p> Also defined, but not for general use are </p>
<pre>
  PNG_LIBRARY, where to find the PNG library.
</pre>
<p> For backward compatiblity the variable PNG_INCLUDE_DIR is also set. It has the same value as PNG_INCLUDE_DIRS. </p>
<p> Since PNG depends on the ZLib compression library, none of the above will be defined unless ZLib can be found. </p>
<dt><code>FindPackageHandleStandardArgs</code></p>
<dd>
<p> FIND_PACKAGE_HANDLE_STANDARD_ARGS(&lt;name&gt; &#8230; ) </p>
<p> This function is intended to be used in FindXXX.cmake modules files. It handles the REQUIRED, QUIET and version-related arguments to find_package(). It also sets the &lt;packagename&gt;_FOUND variable. The package is considered found if all variables &lt;var1&gt;&#8230; listed contain valid results, e.g. valid filepaths. </p>
<p> There are two modes of this function. The first argument in both modes is the name of the Find-module where it is called (in original casing). </p>
<p> The first simple mode looks like this: </p>
<pre>
    FIND_PACKAGE_HANDLE_STANDARD_ARGS(&lt;name&gt; (DEFAULT_MSG|&quot;Custom failure message&quot;) &lt;var1&gt;...&lt;varN&gt; )
</pre>
<p> If the variables &lt;var1&gt; to &lt;varN&gt; are all valid, then &lt;UPPERCASED_NAME&gt;_FOUND will be set to TRUE. If DEFAULT_MSG is given as second argument, then the function will generate itself useful success and error messages. You can also supply a custom error message for the failure case. This is not recommended. </p>
<p> The second mode is more powerful and also supports version checking: </p>
<p>FIND_PACKAGE_HANDLE_STANDARD_ARGS(NAME[FOUND_VAR&lt;resultVar&gt;]<br />
                                      [REQUIRED_VARS&lt;var1&gt;&#8230;&lt;varN&gt;]<br />
                                      [VERSION_VAR&lt;versionvar&gt;]<br />
                                      [HANDLE_COMPONENTS]<br />
                                      [CONFIG_MODE]<br />
                                      [FAIL_MESSAGE &#8220;Custom failure message&#8221;])</p>
<p> In this mode, the name of the result-variable can be set either to either &lt;UPPERCASED_NAME&gt;_FOUND or &lt;OriginalCase_Name&gt;_FOUND using the FOUND_VAR option. Other names for the result-variable are not allowed. So for a Find-module named FindFooBar.cmake, the two possible names are FooBar_FOUND and FOOBAR_FOUND. It is recommended to use the original case version. If the FOUND_VAR option is not used, the default is &lt;UPPERCASED_NAME&gt;_FOUND. </p>
<p> As in the simple mode, if &lt;var1&gt; through &lt;varN&gt; are all valid, &lt;packagename&gt;_FOUND will be set to TRUE. After REQUIRED_VARS the variables which are required for this package are listed. Following VERSION_VAR the name of the variable can be specified which holds the version of the package which has been found. If this is done, this version will be checked against the (potentially) specified required version used in the find_package() call. The EXACT keyword is also handled. The default messages include information about the required version and the version which has been actually found, both if the version is ok or not. If the package supports components, use the HANDLE_COMPONENTS option to enable handling them. In this case, find_package_handle_standard_args() will report which components have been found and which are missing, and the &lt;packagename&gt;_FOUND variable will be set to FALSE if any of the required components (i.e. not the ones listed after OPTIONAL_COMPONENTS) are missing. Use the option CONFIG_MODE if your FindXXX.cmake module is a wrapper for a find_package(&#8230; NO_MODULE) call. In this case VERSION_VAR will be set to &lt;NAME&gt;_VERSION and the macro will automatically check whether the Config module was found. Via FAIL_MESSAGE a custom failure message can be specified, if this is not used, the default message will be displayed. </p>
<p> Example for mode 1: </p>
<pre>
    find_package_handle_standard_args(LibXml2  DEFAULT_MSG  LIBXML2_LIBRARY LIBXML2_INCLUDE_DIR)
</pre>
<p> LibXml2 is considered to be found, if both LIBXML2_LIBRARY and LIBXML2_INCLUDE_DIR are valid. Then also LIBXML2_FOUND is set to TRUE. If it is not found and REQUIRED was used, it fails with FATAL_ERROR, independent whether QUIET was used or not. If it is found, success will be reported, including the content of &lt;var1&gt;. On repeated Cmake runs, the same message won&#8217;t be printed again. </p>
<p> Example for mode 2: </p>
<pre>
    find_package_handle_standard_args(LibXslt FOUND_VAR LibXslt_FOUND
                                             REQUIRED_VARS LibXslt_LIBRARIES LibXslt_INCLUDE_DIRS
                                             VERSION_VAR LibXslt_VERSION_STRING)
</pre>
<p> In this case, LibXslt is considered to be found if the variable(s) listed after REQUIRED_VAR are all valid, i.e. LibXslt_LIBRARIES and LibXslt_INCLUDE_DIRS in this case. The result will then be stored in LibXslt_FOUND . Also the version of LibXslt will be checked by using the version contained in LibXslt_VERSION_STRING. Since no FAIL_MESSAGE is given, the default messages will be printed. </p>
<p> Another example for mode 2: </p>
<pre>
    find_package(Automoc4 QUIET NO_MODULE HINTS /opt/automoc4)
    find_package_handle_standard_args(Automoc4  CONFIG_MODE)
</pre>
<p> In this case, FindAutmoc4.cmake wraps a call to find_package(Automoc4 NO_MODULE) and adds an additional search directory for automoc4. Here the result will be stored in AUTOMOC4_FOUND. The following FIND_PACKAGE_HANDLE_STANDARD_ARGS() call produces a proper success/error message. </p>
<dt><code>FindPackageMessage</code></p>
<dd>
<p> FIND_PACKAGE_MESSAGE(&lt;name&gt; &quot;message for user&quot; &quot;find result details&quot;) </p>
<p> This macro is intended to be used in FindXXX.cmake modules files. It will print a message once for each unique find result. This is useful for telling the user where a package was found. The first argument specifies the name (XXX) of the package. The second argument specifies the message to display. The third argument lists details about the find result so that if they change the message will be displayed again. The macro also obeys the QUIET argument to the find_package command. </p>
<p> Example: </p>
<p>if (X11_FOUND)<br />
    FIND_PACKAGE_MESSAGE(X11 &#8220;Found X11: ${X11_X11_LIB}&#8221;<br />
                             &#8220;[${X11_X11_LIB}][${X11_INCLUDE_DIR}]&#8221;)<br />
else<br />
    ()&#8230; endif()</p>
<dt><code>FindPerl</code></p>
<dd> Find perl </p>
<p> this module looks for Perl </p>
<pre>
  PERL_EXECUTABLE     - the full path to perl
  PERL_FOUND          - If false, don't attempt to use perl.
  PERL_VERSION_STRING - version of perl found (since CMake 2.8.8)
</pre>
<dt><code>FindPerlLibs</code></p>
<dd> Find Perl libraries </p>
<p> This module finds if PERL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PERLLIBS_FOUND    = True if perl.h &amp; libperl were found
  PERL_INCLUDE_PATH = path to where perl.h is found
  PERL_LIBRARY      = path to libperl
  PERL_EXECUTABLE   = full path to the perl binary
</pre>
<p> The minimum required version of Perl can be specified using the standard syntax, e.g. find_package(PerlLibs 6.0) </p>
<pre>
  The following variables are also available if needed
  (introduced after CMake 2.6.4)
</pre>
<pre>
  PERL_SITESEARCH    = path to the sitesearch install dir
  PERL_SITELIB       = path to the sitelib install directory
  PERL_VENDORARCH    = path to the vendor arch install directory
  PERL_VENDORLIB     = path to the vendor lib install directory
  PERL_ARCHLIB       = path to the arch lib install directory
  PERL_PRIVLIB       = path to the priv lib install directory
  PERL_EXTRA_C_FLAGS = Compilation flags used to build perl
</pre>
<dt><code>FindPhysFS</code></p>
<dd>
<p> Locate PhysFS library This module defines PHYSFS_LIBRARY, the name of the library to link against PHYSFS_FOUND, if false, do not try to link to PHYSFS PHYSFS_INCLUDE_DIR, where to find physfs.h </p>
<p> $PHYSFSDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PHYSFSDIR used in building PHYSFS. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindPike</code></p>
<dd> Find Pike </p>
<p> This module finds if PIKE is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PIKE_INCLUDE_PATH       = path to where program.h is found
  PIKE_EXECUTABLE         = full path to the pike binary
</pre>
<dt><code>FindPkgConfig</code></p>
<dd> a pkg-config module for CMake </p>
<p> Usage: </p>
<p>   pkg_check_modules(&lt;PREFIX&gt; [REQUIRED] [QUIET] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for all the given modules</p>
<p>   pkg_search_module(&lt;PREFIX&gt; [REQUIRED] [QUIET] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for given modules and uses the first working one</p>
<p> When the &#8216;REQUIRED&#8217; argument was set, macros will fail with an error when module(s) could not be found </p>
<p> When the &#8216;QUIET&#8217; argument is set, no status messages will be printed. </p>
<p> It sets the following variables: </p>
<pre>
   PKG_CONFIG_FOUND          ... if pkg-config executable was found
   PKG_CONFIG_EXECUTABLE     ... pathname of the pkg-config program
   PKG_CONFIG_VERSION_STRING ... the version of the pkg-config program found
                                 (since CMake 2.8.8)
</pre>
<p> For the following variables two sets of values exist; first one is the common one and has the given PREFIX. The second set contains flags which are given out when pkgconfig was called with the &#8216;&#8211;static&#8217; option. </p>
<pre>
   &lt;XPREFIX&gt;_FOUND          ... set to 1 if module(s) exist
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
<dt><code>FindPostgreSQL</code></p>
<dd> Find the PostgreSQL installation. </p>
<p> In Windows, we make the assumption that, if the PostgreSQL files are installed, the default directory will be C:\Program Files\PostgreSQL. </p>
<p> This module defines </p>
<pre>
  PostgreSQL_LIBRARIES - the PostgreSQL libraries needed for linking
  PostgreSQL_INCLUDE_DIRS - the directories of the PostgreSQL headers
  PostgreSQL_VERSION_STRING - the version of PostgreSQL found (since CMake 2.8.8)
</pre>
<dt><code>FindProducer</code></p>
<dd>
<p> Though Producer isn&#8217;t directly part of OpenSceneGraph, its primary user is OSG so I consider this part of the Findosg* suite used to find OpenSceneGraph components. You&#8217;ll notice that I accept OSGDIR as an environment path. </p>
<p> Each component is separate and you must opt in to each module. You must also opt into OpenGL (and OpenThreads?) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate Producer This module defines PRODUCER_LIBRARY PRODUCER_FOUND, if false, do not try to link to Producer PRODUCER_INCLUDE_DIR, where to find the headers </p>
<p> $PRODUCER_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PRODUCER_DIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindProtobuf</code></p>
<dd>
<p> Locate and configure the Google Protocol Buffers library. </p>
<p> The following variables can be set and are optional: </p>
<pre>
   PROTOBUF_SRC_ROOT_FOLDER - When compiling with MSVC, if this cache variable is set
                              the protobuf-default VS project build locations
                              (vsprojects/Debug &amp; vsprojects/Release) will be searched
                              for libraries and binaries.
</pre>
<pre>
   PROTOBUF_IMPORT_DIRS     - List of additional directories to be searched for
                              imported .proto files. (New in CMake 2.8.8)
</pre>
<p> Defines the following variables: </p>
<pre>
   PROTOBUF_FOUND - Found the Google Protocol Buffers library (libprotobuf &amp; header files)
   PROTOBUF_INCLUDE_DIRS - Include directories for Google Protocol Buffers
   PROTOBUF_LIBRARIES - The protobuf libraries
</pre>
<p> [New in CMake 2.8.5] </p>
<pre>
   PROTOBUF_PROTOC_LIBRARIES - The protoc libraries
   PROTOBUF_LITE_LIBRARIES - The protobuf-lite libraries
</pre>
<p> The following cache variables are also available to set or use: </p>
<pre>
   PROTOBUF_LIBRARY - The protobuf library
   PROTOBUF_PROTOC_LIBRARY   - The protoc library
   PROTOBUF_INCLUDE_DIR - The include directory for protocol buffers
   PROTOBUF_PROTOC_EXECUTABLE - The protoc compiler
</pre>
<p> [New in CMake 2.8.5] </p>
<pre>
   PROTOBUF_LIBRARY_DEBUG - The protobuf library (debug)
   PROTOBUF_PROTOC_LIBRARY_DEBUG   - The protoc library (debug)
   PROTOBUF_LITE_LIBRARY - The protobuf lite library
   PROTOBUF_LITE_LIBRARY_DEBUG - The protobuf lite library (debug)
</pre>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
    Example:</p>
<pre>
   find_package(Protobuf REQUIRED)
   include_directories(${PROTOBUF_INCLUDE_DIRS})
</pre>
<p>include_directories(${CMAKE_CURRENT_BINARY_DIR})<br />
    PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS foo.proto)<br />
        add_executable(bar bar.cc ${PROTO_SRCS} ${PROTO_HDRS})<br />
            target_link_libraries(bar ${PROTOBUF_LIBRARIES})</p>
<p> NOTE: You may need to link against pthreads, depending </p>
<pre>
       on the platform.
</pre>
<p> NOTE: The PROTOBUF_GENERATE_CPP macro &amp; add_executable() or add_library() </p>
<pre>
       calls only work properly within the same directory.
</pre>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==</p>
<p> PROTOBUF_GENERATE_CPP (public function) </p>
<pre>
   SRCS = Variable to define with autogenerated
          source files
   HDRS = Variable to define with autogenerated
          header files
   ARGN = proto files
</pre>
<p>== == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==</p>
<dt><code>FindPythonInterp</code></p>
<dd> Find python interpreter </p>
<p> This module finds if Python interpreter is installed and determines where the executables are. This code sets the following variables: </p>
<pre>
  PYTHONINTERP_FOUND         - Was the Python executable found
  PYTHON_EXECUTABLE          - path to the Python interpreter
</pre>
<pre>
  PYTHON_VERSION_STRING      - Python version found e.g. 2.5.2
  PYTHON_VERSION_MAJOR       - Python major version found e.g. 2
  PYTHON_VERSION_MINOR       - Python minor version found e.g. 5
  PYTHON_VERSION_PATCH       - Python patch version found e.g. 2
</pre>
<p> The Python_ADDITIONAL_VERSIONS variable can be used to specify a list of version numbers that should be taken into account when searching for Python. You need to set this variable before calling find_package(PythonInterp). </p>
<dt><code>FindPythonLibs</code></p>
<dd> Find python libraries </p>
<p> This module finds if Python is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PYTHONLIBS_FOUND           - have the Python libs been found
  PYTHON_LIBRARIES           - path to the python library
  PYTHON_INCLUDE_PATH        - path to where Python.h is found (deprecated)
  PYTHON_INCLUDE_DIRS        - path to where Python.h is found
  PYTHON_DEBUG_LIBRARIES     - path to the debug library (deprecated)
  PYTHONLIBS_VERSION_STRING  - version of the Python libs found (since CMake 2.8.8)
</pre>
<p> The Python_ADDITIONAL_VERSIONS variable can be used to specify a list of version numbers that should be taken into account when searching for Python. You need to set this variable before calling find_package(PythonLibs). </p>
<p> If you&#8217;d like to specify the installation of Python to use, you should modify the following cache variables: </p>
<pre>
  PYTHON_LIBRARY             - path to the python library
  PYTHON_INCLUDE_DIR         - path to where Python.h is found
</pre>
<dt><code>FindQt</code></p>
<dd> Searches for all installed versions of Qt. </p>
<p> This should only be used if your project can work with multiple versions of Qt. If not, you should just directly use FindQt4 or FindQt3. If multiple versions of Qt are found on the machine, then The user must set the option DESIRED_QT_VERSION to the version they want to use. If only one version of qt is found on the machine, then the DESIRED_QT_VERSION is set to that version and the matching FindQt3 or FindQt4 module is included. Once the user sets DESIRED_QT_VERSION, then the FindQt3 or FindQt4 module is included. </p>
<pre>
  QT_REQUIRED if this is set to TRUE then if CMake can
              not find Qt4 or Qt3 an error is raised
              and a message is sent to the user.
</pre>
<pre>
  DESIRED_QT_VERSION OPTION is created
  QT4_INSTALLED is set to TRUE if qt4 is found.
  QT3_INSTALLED is set to TRUE if qt3 is found.
</pre>
<dt><code>FindQt3</code></p>
<dd> Locate Qt include paths and libraries </p>
<p> This module defines: </p>
<pre>
  QT_INCLUDE_DIR    - where to find qt.h, etc.
  QT_LIBRARIES      - the libraries to link against to use Qt.
  QT_DEFINITIONS    - definitions to use when
                      compiling code that uses Qt.
  QT_FOUND          - If false, don't try to use Qt.
  QT_VERSION_STRING - the version of Qt found
</pre>
<p> If you need the multithreaded version of Qt, set QT_MT_REQUIRED to TRUE </p>
<p> Also defined, but not for general use are: </p>
<pre>
  QT_MOC_EXECUTABLE, where to find the moc tool.
  QT_UIC_EXECUTABLE, where to find the uic tool.
  QT_QT_LIBRARY, where to find the Qt library.
  QT_QTMAIN_LIBRARY, where to find the qtmain
   library. This is only required by Qt3 on Windows.
</pre>
<dt><code>FindQt4</code></p>
<dd> Find Qt 4 </p>
<p> This module can be used to find Qt4. The most important issue is that the Qt4 qmake is available via the system path. This qmake is then used to detect basically everything else. This module defines a number of key variables and macros. The variable QT_USE_FILE is set which is the path to a CMake file that can be included to compile Qt 4 applications and libraries. It sets up the compilation environment for include directories, preprocessor defines and populates a QT_LIBRARIES variable. </p>
<p> Typical usage could be something like: </p>
<p>find_package(Qt4 4.4.3 REQUIRED QtCore QtGui QtXml)<br />
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
                    QT_USE_QTDECLARATIVE
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
<pre>
       Note that if using IMPORTED targets, the qtmain.lib static library is
       automatically linked on Windows. To disable that globally, set the
       QT4_NO_LINK_QTMAIN variable before finding Qt4. To disable that for a
       particular executable, set the QT4_NO_LINK_QTMAIN target property to
       True on the executable.
</pre>
<pre>
  QT_INCLUDE_DIRS_NO_SYSTEM
        If this variable is set to TRUE, the Qt include directories
        in the QT_USE_FILE will NOT have the SYSTEM keyword set.
</pre>
<p> There are also some files that need processing by some Qt tools such as moc and uic. Listed below are macros that may be used to process those files. </p>
<pre>
  macro QT4_WRAP_CPP(outfiles inputfile ... OPTIONS ...)
        create moc code from a list of files containing Qt class with
        the Q_OBJECT declaration.  Per-directory preprocessor definitions
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
        The qt4_automoc macro is obsolete.  Use the CMAKE_AUTOMOC feature instead.<br />
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
        You should have a look on the AUTOMOC property for targets to achieve the same results.
</pre>
<pre>
  macro QT4_ADD_DBUS_INTERFACE(outfiles interface basename)
        Create the interface header and implementation files with the
        given basename from the given interface xml file and add it to
        the list of sources.
</pre>
<pre>
        You can pass additional parameters to the qdbusxml2cpp call by setting
        properties on the input file:
</pre>
<pre>
        INCLUDE the given file will be included in the generate interface header
</pre>
<pre>
        CLASSNAME the generated class is named accordingly
</pre>
<pre>
        NO_NAMESPACE the generated class is not wrapped in a namespace
</pre>
<pre>
  macro QT4_ADD_DBUS_INTERFACES(outfiles inputfile ... )
        Create the interface header and implementation files
        for all listed interface xml files.
        The basename will be automatically determined from the name of the xml file.
</pre>
<pre>
        The source file properties described for QT4_ADD_DBUS_INTERFACE also apply here.
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
        must exist and are not updated in any way.
</pre>
<p> function QT4_USE_MODULES( target [link_type] modules&#8230;) </p>
<pre>
        This function is obsolete. Use target_link_libraries with IMPORTED targets instead.
        Make &lt;target&gt; use the &lt;modules&gt; from Qt. Using a Qt module means
        to link to the library, add the relevant include directories for the module,
        and add the relevant compiler defines for using the module.
        Modules are roughly equivalent to components of Qt4, so usage would be
        something like:
         qt4_use_modules(myexe Core Gui Declarative)
        to use QtCore, QtGui and QtDeclarative. The optional &lt;link_type&gt; argument can
        be specified as either LINK_PUBLIC or LINK_PRIVATE to specify the same argument
        to the target_link_libraries call.
</pre>
<pre>
  Below is a detailed list of variables that FindQt4.cmake sets.
  QT_FOUND         If false, don't try to use Qt.
  Qt4_FOUND        If false, don't try to use Qt 4.
  QT4_FOUND        If false, don't try to use Qt 4. This variable is for compatibility only.
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
           .QT_QTNETWORK_FOUND True if QtNetwork was found.QT_QTNSPLUGIN_FOUND True if QtNsPlugin was found.QT_QTOPENGL_FOUND True if QtOpenGL was found.QT_QTSQL_FOUND True if QtSql was found.QT_QTSVG_FOUND True if QtSvg was found.QT_QTSCRIPT_FOUND True if QtScript was found.QT_QTSCRIPTTOOLS_FOUND True if QtScriptTools was found.QT_QTTEST_FOUND True if QtTest was found.QT_QTUITOOLS_FOUND True if QtUiTools was found.QT_QTWEBKIT_FOUND True if QtWebKit was found.QT_QTXML_FOUND True if QtXml was found.QT_QTXMLPATTERNS_FOUND True if QtXmlPatterns was found.QT_PHONON_FOUND True if phonon was found.QT_QTDECLARATIVE_FOUND True if QtDeclarative was found.</p>
<pre>
  QT_MAC_USE_COCOA    For Mac OS X, its whether Cocoa or Carbon is used.
                      In general, this should not be used, but its useful
                      when having platform specific code.
</pre>
<pre>
  QT_DEFINITIONS   Definitions to use when compiling code that uses Qt.
                   You do not need to use this if you include QT_USE_FILE.
                   The QT_USE_FILE will also define QT_DEBUG and QT_NO_DEBUG
                   to fit your current build type.  Those are not contained
                   in QT_DEFINITIONS.
</pre>
<pre>
  QT_INCLUDES      List of paths to all include directories of
                   Qt4 QT_INCLUDE_DIR and QT_QTCORE_INCLUDE_DIR are
                   always in this variable even if NOTFOUND,
                   all other INCLUDE_DIRS are
                   only added if they are found.
                   You do not need to use this if you include QT_USE_FILE.
</pre>
<pre>
  Include directories for the Qt modules are listed here.
  You do not need to use these variables if you include QT_USE_FILE.
</pre>
<p>QT_INCLUDE_DIR Path to &#8220;include&#8221; of Qt4<br />
    QT_QT3SUPPORT_INCLUDE_DIR Path to &#8220;include/Qt3Support&#8221; QT_QTASSISTANT_INCLUDE_DIR Path to &#8220;include/QtAssistant&#8221; QT_QTASSISTANTCLIENT_INCLUDE_DIR Path to &#8220;include/QtAssistant&#8221; QT_QAXCONTAINER_INCLUDE_DIR Path to &#8220;include/ActiveQt&#8221;(Windows only)<br />
        QT_QAXSERVER_INCLUDE_DIR Path to &#8220;include/ActiveQt&#8221;(Windows only)<br />
            QT_QTCORE_INCLUDE_DIR Path to &#8220;include/QtCore&#8221; QT_QTDBUS_INCLUDE_DIR Path to &#8220;include/QtDBus&#8221; QT_QTDESIGNER_INCLUDE_DIR Path to &#8220;include/QtDesigner&#8221; QT_QTDESIGNERCOMPONENTS_INCLUDE_DIR Path to &#8220;include/QtDesigner&#8221; QT_QTGUI_INCLUDE_DIR Path to &#8220;include/QtGui&#8221; QT_QTHELP_INCLUDE_DIR Path to &#8220;include/QtHelp&#8221; QT_QTMOTIF_INCLUDE_DIR Path to &#8220;include/QtMotif&#8221; QT_QTMULTIMEDIA_INCLUDE_DIR Path to &#8220;include/QtMultimedia&#8221; QT_QTNETWORK_INCLUDE_DIR Path to &#8220;include/QtNetwork&#8221; QT_QTNSPLUGIN_INCLUDE_DIR Path to &#8220;include/QtNsPlugin&#8221; QT_QTOPENGL_INCLUDE_DIR Path to &#8220;include/QtOpenGL&#8221; QT_QTSCRIPT_INCLUDE_DIR Path to &#8220;include/QtScript&#8221; QT_QTSQL_INCLUDE_DIR Path to &#8220;include/QtSql&#8221; QT_QTSVG_INCLUDE_DIR Path to &#8220;include/QtSvg&#8221; QT_QTTEST_INCLUDE_DIR Path to &#8220;include/QtTest&#8221; QT_QTWEBKIT_INCLUDE_DIR Path to &#8220;include/QtWebKit&#8221; QT_QTXML_INCLUDE_DIR Path to &#8220;include/QtXml&#8221; QT_QTXMLPATTERNS_INCLUDE_DIR Path to &#8220;include/QtXmlPatterns&#8221; QT_PHONON_INCLUDE_DIR Path to &#8220;include/phonon&#8221; QT_QTSCRIPTTOOLS_INCLUDE_DIR Path to &#8220;include/QtScriptTools&#8221; QT_QTDECLARATIVE_INCLUDE_DIR Path to &#8220;include/QtDeclarative&#8221;</p>
<pre>
  QT_BINARY_DIR               Path to &quot;bin&quot; of Qt4
  QT_LIBRARY_DIR              Path to &quot;lib&quot; of Qt4
  QT_PLUGINS_DIR              Path to &quot;plugins&quot; for Qt4
  QT_TRANSLATIONS_DIR         Path to &quot;translations&quot; of Qt4
  QT_IMPORTS_DIR              Path to &quot;imports&quot; of Qt4
  QT_DOC_DIR                  Path to &quot;doc&quot; of Qt4
  QT_MKSPECS_DIR              Path to &quot;mkspecs&quot; of Qt4
</pre>
<p> The Qt toolkit may contain both debug and release libraries. In that case, the following library variables will contain both. You do not need to use these variables if you include QT_USE_FILE, and use QT_LIBRARIES. </p>
<pre>
  QT_QT3SUPPORT_LIBRARY            The Qt3Support library
  QT_QTASSISTANT_LIBRARY           The QtAssistant library
  QT_QTASSISTANTCLIENT_LIBRARY     The QtAssistantClient library
  QT_QAXCONTAINER_LIBRARY           The QAxContainer library (Windows only)
  QT_QAXSERVER_LIBRARY                The QAxServer library (Windows only)
  QT_QTCORE_LIBRARY                The QtCore library
  QT_QTDBUS_LIBRARY                The QtDBus library
  QT_QTDESIGNER_LIBRARY            The QtDesigner library
  QT_QTDESIGNERCOMPONENTS_LIBRARY  The QtDesignerComponents library
  QT_QTGUI_LIBRARY                 The QtGui library
  QT_QTHELP_LIBRARY                The QtHelp library
  QT_QTMOTIF_LIBRARY               The QtMotif library
  QT_QTMULTIMEDIA_LIBRARY          The QtMultimedia library
  QT_QTNETWORK_LIBRARY             The QtNetwork library
  QT_QTNSPLUGIN_LIBRARY            The QtNsPLugin library
  QT_QTOPENGL_LIBRARY              The QtOpenGL library
  QT_QTSCRIPT_LIBRARY              The QtScript library
  QT_QTSQL_LIBRARY                 The QtSql library
  QT_QTSVG_LIBRARY                 The QtSvg library
  QT_QTTEST_LIBRARY                The QtTest library
  QT_QTUITOOLS_LIBRARY             The QtUiTools library
  QT_QTWEBKIT_LIBRARY              The QtWebKit library
  QT_QTXML_LIBRARY                 The QtXml library
  QT_QTXMLPATTERNS_LIBRARY         The QtXmlPatterns library
  QT_QTMAIN_LIBRARY                The qtmain library for Windows
  QT_PHONON_LIBRARY                The phonon library
  QT_QTSCRIPTTOOLS_LIBRARY         The QtScriptTools library
</pre>
<p> The QtDeclarative library: QT_QTDECLARATIVE_LIBRARY </p>
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
<dt><code>FindQuickTime</code></p>
<dd>
<p> Locate QuickTime This module defines QUICKTIME_LIBRARY QUICKTIME_FOUND, if false, do not try to link to gdal QUICKTIME_INCLUDE_DIR, where to find the headers </p>
<p> $QUICKTIME_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$QUICKTIME_DIR </p>
<p> Created by Eric Wing. </p>
<dt><code>FindRTI</code></p>
<dd> Try to find M&amp;S HLA RTI libraries </p>
<p> This module finds if any HLA RTI is installed and locates the standard RTI include files and libraries. </p>
<p> RTI is a simulation infrastructure standardized by IEEE and SISO. It has a well defined C++ API that assures that simulation applications are independent on a particular RTI implementation. </p>
<pre>
  <a rel="nofollow" href="http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)">http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)</a>
</pre>
<p> This code sets the following variables: </p>
<pre>
  RTI_INCLUDE_DIR = the directory where RTI includes file are found
  RTI_LIBRARIES = The libraries to link against to use RTI
  RTI_DEFINITIONS = -DRTI_USES_STD_FSTREAM
  RTI_FOUND = Set to FALSE if any HLA RTI was not found
</pre>
<p> Report problems to &lt;certi-devel [at] nongnu.org&gt; </p>
<dt><code>FindRuby</code></p>
<dd> Find Ruby </p>
<p> This module finds if Ruby is installed and determines where the include files and libraries are. Ruby 1.8 and 1.9 are supported. </p>
<p> The minimum required version of Ruby can be specified using the standard syntax, e.g. find_package(Ruby 1.8) </p>
<p> It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  RUBY_EXECUTABLE   = full path to the ruby binary
  RUBY_INCLUDE_DIRS = include dirs to be used when using the ruby library
  RUBY_LIBRARY      = full path to the ruby library
  RUBY_VERSION      = the version of ruby which was found, e.g. &quot;1.8.7&quot;
  RUBY_FOUND        = set to true if ruby ws found successfully
</pre>
<pre>
  RUBY_INCLUDE_PATH = same as RUBY_INCLUDE_DIRS, only provided for compatibility reasons, don't use it
</pre>
<dt><code>FindSDL</code></p>
<dd> Locate SDL library </p>
<p> This module defines </p>
<pre>
  SDL_LIBRARY, the name of the library to link against
  SDL_FOUND, if false, do not try to link to SDL
  SDL_INCLUDE_DIR, where to find SDL.h
  SDL_VERSION_STRING, human-readable string containing the version of SDL
</pre>
<p> This module responds to the the flag: </p>
<pre>
  SDL_BUILDING_LIBRARY
    If this is defined, then no SDL_main will be linked in because
    only applications need main().
    Otherwise, it is assumed you are building an application and this
    module will attempt to locate and set the the proper link flags
    as part of the returned SDL_LIBRARY variable.
</pre>
<p> Don&#8217;t forget to include SDLmain.h and SDLmain.m your project for the OS X framework based version. (Other versions link to -lSDLmain which this module will try to find on your behalf.) Also for OS X, this module will automatically add the -framework Cocoa on your behalf. </p>
<p> Additional Note: If you see an empty SDL_LIBRARY_TEMP in your configuration and no SDL_LIBRARY, it means CMake did not find your SDL library (SDL.dll, libsdl.so, SDL.framework, etc). Set SDL_LIBRARY_TEMP to point to your SDL library, and configure again. Similarly, if you see an empty SDLMAIN_LIBRARY, you should set this value as appropriate. These values are used to generate the final SDL_LIBRARY variable, but when these values are unset, SDL_LIBRARY does not get created. </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. l.e.galup 9-20-02 </p>
<p> Modified by Eric Wing. Added code to assist with automated building by using environmental variables and providing a more controlled/consistent search behavior. Added new modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). Also corrected the header search path to follow &quot;proper&quot; SDL guidelines. Added a search for SDLmain which is needed by some platforms. Added a search for threads which is needed by some platforms. Added needed compile switches for MinGW. </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selection or set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths. </p>
<p> Note that the header path has changed from SDL/SDL.h to just SDL.h This needed to change because &quot;proper&quot; SDL convention is #include &quot;SDL.h&quot;, not &lt;SDL/SDL.h&gt;. This is done for portability reasons because not all systems place things in SDL/ (see FreeBSD). </p>
<dt><code>FindSDL_image</code></p>
<dd> Locate SDL_image library </p>
<p> This module defines: </p>
<pre>
  SDL_IMAGE_LIBRARIES, the name of the library to link against
  SDL_IMAGE_INCLUDE_DIRS, where to find the headers
  SDL_IMAGE_FOUND, if false, do not try to link against
  SDL_IMAGE_VERSION_STRING - human-readable string containing the version of SDL_image
</pre>
<p> For backward compatiblity the following variables are also set: </p>
<pre>
  SDLIMAGE_LIBRARY (same value as SDL_IMAGE_LIBRARIES)
  SDLIMAGE_INCLUDE_DIR (same value as SDL_IMAGE_INCLUDE_DIRS)
  SDLIMAGE_FOUND (same value as SDL_IMAGE_FOUND)
</pre>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_mixer</code></p>
<dd> Locate SDL_mixer library </p>
<p> This module defines: </p>
<pre>
  SDL_MIXER_LIBRARIES, the name of the library to link against
  SDL_MIXER_INCLUDE_DIRS, where to find the headers
  SDL_MIXER_FOUND, if false, do not try to link against
  SDL_MIXER_VERSION_STRING - human-readable string containing the version of SDL_mixer
</pre>
<p> For backward compatiblity the following variables are also set: </p>
<pre>
  SDLMIXER_LIBRARY (same value as SDL_MIXER_LIBRARIES)
  SDLMIXER_INCLUDE_DIR (same value as SDL_MIXER_INCLUDE_DIRS)
  SDLMIXER_FOUND (same value as SDL_MIXER_FOUND)
</pre>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_net</code></p>
<dd> Locate SDL_net library </p>
<p> This module defines: </p>
<pre>
  SDL_NET_LIBRARIES, the name of the library to link against
  SDL_NET_INCLUDE_DIRS, where to find the headers
  SDL_NET_FOUND, if false, do not try to link against
  SDL_NET_VERSION_STRING - human-readable string containing the version of SDL_net
</pre>
<p> For backward compatiblity the following variables are also set: </p>
<pre>
  SDLNET_LIBRARY (same value as SDL_NET_LIBRARIES)
  SDLNET_INCLUDE_DIR (same value as SDL_NET_INCLUDE_DIRS)
  SDLNET_FOUND (same value as SDL_NET_FOUND)
</pre>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_sound</code></p>
<dd> Locates the SDL_sound library </p>
<p> This module depends on SDL being found and must be called AFTER FindSDL.cmake is called. </p>
<p> This module defines </p>
<pre>
  SDL_SOUND_INCLUDE_DIR, where to find SDL_sound.h
  SDL_SOUND_FOUND, if false, do not try to link to SDL_sound
  SDL_SOUND_LIBRARIES, this contains the list of libraries that you need
    to link against. This is a read-only variable and is marked INTERNAL.
  SDL_SOUND_EXTRAS, this is an optional variable for you to add your own
    flags to SDL_SOUND_LIBRARIES. This is prepended to SDL_SOUND_LIBRARIES.
    This is available mostly for cases this module failed to anticipate for
    and you must add additional flags. This is marked as ADVANCED.
  SDL_SOUND_VERSION_STRING, human-readable string containing the version of SDL_sound
</pre>
<p> This module also defines (but you shouldn&#8217;t need to use directly) </p>
<pre>
   SDL_SOUND_LIBRARY, the name of just the SDL_sound library you would link
   against. Use SDL_SOUND_LIBRARIES for you link instructions and not this one.
</pre>
<p> And might define the following as needed </p>
<pre>
   MIKMOD_LIBRARY
   MODPLUG_LIBRARY
   OGG_LIBRARY
   VORBIS_LIBRARY
   SMPEG_LIBRARY
   FLAC_LIBRARY
   SPEEX_LIBRARY
</pre>
<p> Typically, you should not use these variables directly, and you should use SDL_SOUND_LIBRARIES which contains SDL_SOUND_LIBRARY and the other audio libraries (if needed) to successfully compile on your system. </p>
<p> Created by Eric Wing. This module is a bit more complicated than the other FindSDL* family modules. The reason is that SDL_sound can be compiled in a large variety of different ways which are independent of platform. SDL_sound may dynamically link against other 3rd party libraries to get additional codec support, such as Ogg Vorbis, SMPEG, ModPlug, MikMod, FLAC, Speex, and potentially others. Under some circumstances which I don&#8217;t fully understand, there seems to be a requirement that dependent libraries of libraries you use must also be explicitly linked against in order to successfully compile. SDL_sound does not currently have any system in place to know how it was compiled. So this CMake module does the hard work in trying to discover which 3rd party libraries are required for building (if any). This module uses a brute force approach to create a test program that uses SDL_sound, and then tries to build it. If the build fails, it parses the error output for known symbol names to figure out which libraries are needed. </p>
<p> Responds to the $SDLDIR and $SDLSOUNDDIR environmental variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selectionor set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths. </p>
<dt><code>FindSDL_ttf</code></p>
<dd> Locate SDL_ttf library </p>
<p> This module defines: </p>
<pre>
  SDL_TTF_LIBRARIES, the name of the library to link against
  SDL_TTF_INCLUDE_DIRS, where to find the headers
  SDL_TTF_FOUND, if false, do not try to link against
  SDL_TTF_VERSION_STRING - human-readable string containing the version of SDL_ttf
</pre>
<p> For backward compatiblity the following variables are also set: </p>
<pre>
  SDLTTF_LIBRARY (same value as SDL_TTF_LIBRARIES)
  SDLTTF_INCLUDE_DIR (same value as SDL_TTF_INCLUDE_DIRS)
  SDLTTF_FOUND (same value as SDL_TTF_FOUND)
</pre>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSWIG</code></p>
<dd> Find SWIG </p>
<p> This module finds an installed SWIG. It sets the following variables: </p>
<pre>
  SWIG_FOUND - set to true if SWIG is found
  SWIG_DIR - the directory where swig is installed
  SWIG_EXECUTABLE - the path to the swig executable
  SWIG_VERSION   - the version number of the swig executable
</pre>
<p> The minimum required version of SWIG can be specified using the standard syntax, e.g. find_package(SWIG 1.1) </p>
<p> All information is collected from the SWIG_EXECUTABLE so the version to be found can be changed from the command line by means of setting SWIG_EXECUTABLE </p>
<dt><code>FindSelfPackers</code></p>
<dd> Find upx </p>
<p> This module looks for some executable packers (i.e. software that compress executables or shared libs into on-the-fly self-extracting executables or shared libs. Examples: </p>
<pre>
  UPX: <a rel="nofollow" href="http://wildsau.idv.uni-linz.ac.at/mfx/upx.html">http://wildsau.idv.uni-linz.ac.at/mfx/upx.html</a>
</pre>
<dt><code>FindSquish</code></p>
<dd> &#8212; Typical Use </p>
<p> This module can be used to find Squish. Currently Squish versions 3 and 4 are supported. </p>
<pre>
  SQUISH_FOUND                    If false, don't try to use Squish
  SQUISH_VERSION                  The full version of Squish found
  SQUISH_VERSION_MAJOR            The major version of Squish found
  SQUISH_VERSION_MINOR            The minor version of Squish found
  SQUISH_VERSION_PATCH            The patch version of Squish found
</pre>
<pre>
  SQUISH_INSTALL_DIR              The Squish installation directory (containing bin, lib, etc)
  SQUISH_SERVER_EXECUTABLE        The squishserver executable
  SQUISH_CLIENT_EXECUTABLE        The squishrunner executable
</pre>
<pre>
  SQUISH_INSTALL_DIR_FOUND        Was the install directory found?
  SQUISH_SERVER_EXECUTABLE_FOUND  Was the server executable found?
  SQUISH_CLIENT_EXECUTABLE_FOUND  Was the client executable found?
</pre>
<p> It provides the function squish_v4_add_test() for adding a squish test to cmake using Squish 4.x: </p>
<p>squish_v4_add_test(cmakeTestName AUT targetName SUITE suiteName TEST squishTestName<br />
                       [SETTINGSGROUP group][PRE_COMMAND command][POST_COMMAND command])</p>
<p> The arguments have the following meaning: </p>
<pre>
   cmakeTestName: this will be used as the first argument for add_test()
   AUT targetName: the name of the cmake target which will be used as AUT, i.e. the
                   executable which will be tested.
   SUITE suiteName: this is either the full path to the squish suite, or just the
                    last directory of the suite, i.e. the suite name. In this case
                    the CMakeLists.txt which calls squish_add_test() must be located
                    in the parent directory of the suite directory.
   TEST squishTestName: the name of the squish test, i.e. the name of the subdirectory
                        of the test inside the suite directory.
   SETTINGSGROUP group: if specified, the given settings group will be used for executing the test.
                        If not specified, the groupname will be &quot;CTest_&lt;username&gt;&quot;
   PRE_COMMAND command:  if specified, the given command will be executed before starting the squish test.
   POST_COMMAND command: same as PRE_COMMAND, but after the squish test has been executed.
</pre>
<p>enable_testing()<br />
    find_package(Squish 4.0) if (SQUISH_FOUND)<br />
        squish_v4_add_test(myTestName AUT myApp SUITE ${CMAKE_SOURCE_DIR} / tests / mySuite TEST someSquishTest SETTINGSGROUP myGroup)<br />
            endif()</p>
<p> For users of Squish version 3.x the macro squish_v3_add_test() is provided: </p>
<pre>
   squish_v3_add_test(testName applicationUnderTest testCase envVars testWrapper)
   Use this macro to add a test using Squish 3.x.
</pre>
<pre>
  enable_testing()
  find_package(Squish)
  if (SQUISH_FOUND)
    squish_v3_add_test(myTestName myApplication testCase envVars testWrapper)
  endif ()
</pre>
<p> macro SQUISH_ADD_TEST(testName applicationUnderTest testCase envVars testWrapper) </p>
<pre>
   This is deprecated. Use SQUISH_V3_ADD_TEST() if you are using Squish 3.x instead.
</pre>
<dt><code>FindSubversion</code></p>
<dd> Extract information from a subversion working copy </p>
<p> The module defines the following variables: </p>
<pre>
  Subversion_SVN_EXECUTABLE - path to svn command line client
  Subversion_VERSION_SVN - version of svn command line client
  Subversion_FOUND - true if the command line client was found
  SUBVERSION_FOUND - same as Subversion_FOUND, set for compatiblity reasons
</pre>
<p> The minimum required version of Subversion can be specified using the standard syntax, e.g. find_package(Subversion 1.4) </p>
<p> If the command line client executable is found two macros are defined: </p>
<pre>
  Subversion_WC_INFO(&lt;dir&gt; &lt;var-prefix&gt;)
  Subversion_WC_LOG(&lt;dir&gt; &lt;var-prefix&gt;)
</pre>
<p> Subversion_WC_INFO extracts information of a subversion working copy at a given location. This macro defines the following variables: </p>
<pre>
  &lt;var-prefix&gt;_WC_URL - url of the repository (at &lt;dir&gt;)
  &lt;var-prefix&gt;_WC_ROOT - root url of the repository
  &lt;var-prefix&gt;_WC_REVISION - current revision
  &lt;var-prefix&gt;_WC_LAST_CHANGED_AUTHOR - author of last commit
  &lt;var-prefix&gt;_WC_LAST_CHANGED_DATE - date of last commit
  &lt;var-prefix&gt;_WC_LAST_CHANGED_REV - revision of last commit
  &lt;var-prefix&gt;_WC_INFO - output of command `svn info &lt;dir&gt;'
</pre>
<p> Subversion_WC_LOG retrieves the log message of the base revision of a subversion working copy at a given location. This macro defines the variable: </p>
<pre>
  &lt;var-prefix&gt;_LAST_CHANGED_LOG - last log of base revision
</pre>
<p> Example usage: </p>
<p>find_package(Subversion) if (SUBVERSION_FOUND)<br />
    Subversion_WC_INFO(${PROJECT_SOURCE_DIR} Project)<br />
        message(&#8220;Current revision is ${Project_WC_REVISION}&#8221;)<br />
            Subversion_WC_LOG(${PROJECT_SOURCE_DIR} Project)<br />
                message(&#8220;Last changed log is ${Project_LAST_CHANGED_LOG}&#8221;)<br />
                    endif()</p>
<dt><code>FindTCL</code></p>
<dd> TK_INTERNAL_PATH was removed. </p>
<p> This module finds if Tcl is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TCL_FOUND              = Tcl was found
  TK_FOUND               = Tk was found
  TCLTK_FOUND            = Tcl and Tk were found
  TCL_LIBRARY            = path to Tcl library (tcl tcl80)
  TCL_INCLUDE_PATH       = path to where tcl.h can be found
  TCL_TCLSH              = path to tclsh binary (tcl tcl80)
  TK_LIBRARY             = path to Tk library (tk tk80 etc)
  TK_INCLUDE_PATH        = path to where tk.h can be found
  TK_WISH                = full path to the wish executable
</pre>
<p> In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>
   =&gt; they were only useful for people writing Tcl/Tk extensions.
   =&gt; these libs are not packaged by default with Tcl/Tk distributions.
      Even when Tcl/Tk is built from source, several flavors of debug libs
      are created and there is no real reason to pick a single one
      specifically (say, amongst tcl84g, tcl84gs, or tcl84sgx).
      Let's leave that choice to the user by allowing him to assign
      TCL_LIBRARY to any Tcl library, debug or not.
   =&gt; this ended up being only a Win32 variable, and there is a lot of
      confusion regarding the location of this file in an installed Tcl/Tk
      tree anyway (see 8.5 for example). If you need the internal path at
      this point it is safer you ask directly where the *source* tree is
      and dig from there.
</pre>
<dt><code>FindTIFF</code></p>
<dd> Find TIFF library </p>
<p> Find the native TIFF includes and library This module defines </p>
<pre>
  TIFF_INCLUDE_DIR, where to find tiff.h, etc.
  TIFF_LIBRARIES, libraries to link against to use TIFF.
  TIFF_FOUND, If false, do not try to use TIFF.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  TIFF_LIBRARY, where to find the TIFF library.
</pre>
<dt><code>FindTclStub</code></p>
<dd> TCL_STUB_LIBRARY_DEBUG and TK_STUB_LIBRARY_DEBUG were removed. </p>
<p> This module finds Tcl stub libraries. It first finds Tcl include files and libraries by calling FindTCL.cmake. How to Use the Tcl Stubs Library: </p>
<pre>
   <a rel="nofollow" href="http://tcl.activestate.com/doc/howto/stubs.html">http://tcl.activestate.com/doc/howto/stubs.html</a>
</pre>
<p> Using Stub Libraries: </p>
<pre>
   <a rel="nofollow" href="http://safari.oreilly.com/0130385603/ch48lev1sec3">http://safari.oreilly.com/0130385603/ch48lev1sec3</a>
</pre>
<p> This code sets the following variables: </p>
<pre>
  TCL_STUB_LIBRARY       = path to Tcl stub library
  TK_STUB_LIBRARY        = path to Tk stub library
  TTK_STUB_LIBRARY       = path to ttk stub library
</pre>
<p> In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>
   =&gt; these libs are not packaged by default with Tcl/Tk distributions.
      Even when Tcl/Tk is built from source, several flavors of debug libs
      are created and there is no real reason to pick a single one
      specifically (say, amongst tclstub84g, tclstub84gs, or tclstub84sgx).
      Let's leave that choice to the user by allowing him to assign
      TCL_STUB_LIBRARY to any Tcl library, debug or not.
</pre>
<dt><code>FindTclsh</code></p>
<dd> Find tclsh </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TCLSH_FOUND = TRUE if tclsh has been found
  TCL_TCLSH = the path to the tclsh executable
</pre>
<p> In cygwin, look for the cygwin version first. Don&#8217;t look for it later to avoid finding the cygwin version on a Win32 build. </p>
<dt><code>FindThreads</code></p>
<dd> This module determines the thread library of the system. </p>
<p> The following variables are set </p>
<pre>
  CMAKE_THREAD_LIBS_INIT     - the thread library
  CMAKE_USE_SPROC_INIT       - are we using sproc?
  CMAKE_USE_WIN32_THREADS_INIT - using WIN32 threads?
  CMAKE_USE_PTHREADS_INIT    - are we using pthreads
  CMAKE_HP_PTHREADS_INIT     - are we using hp pthreads
</pre>
<p> For systems with multiple thread libraries, caller can set </p>
<pre>
  CMAKE_THREAD_PREFER_PTHREAD
</pre>
<dt><code>FindUnixCommands</code></p>
<dd> Find unix commands from cygwin </p>
<p> This module looks for some usual Unix commands. </p>
<dt><code>FindVTK</code></p>
<dd> Find a VTK installation or build tree. </p>
<p> The following variables are set if VTK is found. If VTK is not found, VTK_FOUND is set to false. </p>
<pre>
  VTK_FOUND         - Set to true when VTK is found.
  VTK_USE_FILE      - CMake file to use VTK.
  VTK_MAJOR_VERSION - The VTK major version number.
  VTK_MINOR_VERSION - The VTK minor version number
                       (odd non-release).
  VTK_BUILD_VERSION - The VTK patch level
                       (meaningless for odd minor).
  VTK_INCLUDE_DIRS  - Include directories for VTK
  VTK_LIBRARY_DIRS  - Link directories for VTK libraries
  VTK_KITS          - List of VTK kits, in CAPS
                      (COMMON,IO,) etc.
  VTK_LANGUAGES     - List of wrapped languages, in CAPS
                      (TCL, PYHTON,) etc.
</pre>
<p> The following cache entries must be set by the user to locate VTK: </p>
<pre>
  VTK_DIR  - The directory containing VTKConfig.cmake.
             This is either the root of the build tree,
             or the lib/vtk directory.  This is the
             only cache entry.
</pre>
<p> The following variables are set for backward compatibility and should not be used in new code: </p>
<pre>
  USE_VTK_FILE - The full path to the UseVTK.cmake file.
                 This is provided for backward
                 compatibility.  Use VTK_USE_FILE
                 instead.
</pre>
<dt><code>FindWget</code></p>
<dd> Find wget </p>
<p> This module looks for wget. This module defines the following values: </p>
<pre>
  WGET_EXECUTABLE: the full path to the wget tool.
  WGET_FOUND: True if wget has been found.
</pre>
<dt><code>FindWish</code></p>
<dd> Find wish installation </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TK_WISH = the path to the wish executable
</pre>
<p> if UNIX is defined, then it will look for the cygwin version first </p>
<dt><code>FindX11</code></p>
<dd> Find X11 installation </p>
<p> Try to find X11 on UNIX systems. The following values are defined </p>
<pre>
  X11_FOUND        - True if X11 is available
  X11_INCLUDE_DIR  - include directories to use X11
  X11_LIBRARIES    - link against these to use X11
</pre>
<p> and also the following more fine grained variables: Include paths: X11_ICE_INCLUDE_PATH, X11_ICE_LIB, X11_ICE_FOUND </p>
<pre>
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
                X11_xf86vmode_INCLUDE_PATH,    X11_Xxf86vm_LIB     X11_xf86vmode_FOUND
                X11_Xfixes_INCLUDE_PATH,       X11_Xfixes_LIB,     X11_Xfixes_FOUND
                X11_Xft_INCLUDE_PATH,          X11_Xft_LIB,        X11_Xft_FOUND
                X11_Xi_INCLUDE_PATH,           X11_Xi_LIB,         X11_Xi_FOUND
                X11_Xinerama_INCLUDE_PATH,     X11_Xinerama_LIB,   X11_Xinerama_FOUND
                X11_Xinput_INCLUDE_PATH,       X11_Xinput_LIB,     X11_Xinput_FOUND
                X11_Xkb_INCLUDE_PATH,                              X11_Xkb_FOUND
                X11_Xkblib_INCLUDE_PATH,                           X11_Xkb_FOUND
                X11_Xkbfile_INCLUDE_PATH,      X11_Xkbfile_LIB,    X11_Xkbfile_FOUND
                X11_Xmu_INCLUDE_PATH,          X11_Xmu_LIB,        X11_Xmu_FOUND
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
<dt><code>FindXMLRPC</code></p>
<dd> Find xmlrpc </p>
<p> Find the native XMLRPC headers and libraries. </p>
<pre>
  XMLRPC_INCLUDE_DIRS      - where to find xmlrpc.h, etc.
  XMLRPC_LIBRARIES         - List of libraries when using xmlrpc.
  XMLRPC_FOUND             - True if xmlrpc found.
</pre>
<p> XMLRPC modules may be specified as components for this find module. Modules may be listed by running &quot;xmlrpc-c-config&quot;. Modules include: </p>
<pre>
  c++            C++ wrapper code
  libwww-client  libwww-based client
  cgi-server     CGI-based server
  abyss-server   ABYSS-based server
</pre>
<p> Typical usage: </p>
<pre>
  find_package(XMLRPC REQUIRED libwww-client)
</pre>
<dt><code>FindZLIB</code></p>
<dd> Find zlib </p>
<p> Find the native ZLIB includes and library. Once done this will define </p>
<pre>
  ZLIB_INCLUDE_DIRS   - where to find zlib.h, etc.
  ZLIB_LIBRARIES      - List of libraries when using zlib.
  ZLIB_FOUND          - True if zlib found.
</pre>
<pre>
  ZLIB_VERSION_STRING - The version of zlib found (x.y.z)
  ZLIB_VERSION_MAJOR  - The major version of zlib
  ZLIB_VERSION_MINOR  - The minor version of zlib
  ZLIB_VERSION_PATCH  - The patch version of zlib
  ZLIB_VERSION_TWEAK  - The tweak version of zlib
</pre>
<p> The following variable are provided for backward compatibility </p>
<pre>
  ZLIB_MAJOR_VERSION  - The major version of zlib
  ZLIB_MINOR_VERSION  - The minor version of zlib
  ZLIB_PATCH_VERSION  - The patch version of zlib
</pre>
<p> An includer may set ZLIB_ROOT to a zlib installation root to tell this module where to look. </p>
<dt><code>Findosg</code></p>
<dd>
<p> NOTE: It is highly recommended that you use the new FindOpenSceneGraph.cmake introduced in CMake 2.6.3 and not use this Find module directly. </p>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osg This module defines </p>
<p> OSG_FOUND &#8211; Was the Osg found? OSG_INCLUDE_DIR &#8211; Where to find the headers OSG_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSG_LIBRARY &#8211; The OSG library OSG_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgAnimation</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgAnimation This module defines </p>
<p> OSGANIMATION_FOUND &#8211; Was osgAnimation found? OSGANIMATION_INCLUDE_DIR &#8211; Where to find the headers OSGANIMATION_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSGANIMATION_LIBRARY &#8211; The OSG library OSGANIMATION_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgDB</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgDB This module defines </p>
<p> OSGDB_FOUND &#8211; Was osgDB found? OSGDB_INCLUDE_DIR &#8211; Where to find the headers OSGDB_LIBRARIES &#8211; The libraries to link against for the osgDB (use this) </p>
<p> OSGDB_LIBRARY &#8211; The osgDB library OSGDB_LIBRARY_DEBUG &#8211; The osgDB debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgFX</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgFX This module defines </p>
<p> OSGFX_FOUND &#8211; Was osgFX found? OSGFX_INCLUDE_DIR &#8211; Where to find the headers OSGFX_LIBRARIES &#8211; The libraries to link against for the osgFX (use this) </p>
<p> OSGFX_LIBRARY &#8211; The osgFX library OSGFX_LIBRARY_DEBUG &#8211; The osgFX debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgGA</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgGA This module defines </p>
<p> OSGGA_FOUND &#8211; Was osgGA found? OSGGA_INCLUDE_DIR &#8211; Where to find the headers OSGGA_LIBRARIES &#8211; The libraries to link against for the osgGA (use this) </p>
<p> OSGGA_LIBRARY &#8211; The osgGA library OSGGA_LIBRARY_DEBUG &#8211; The osgGA debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgIntrospection</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgINTROSPECTION This module defines </p>
<p> OSGINTROSPECTION_FOUND &#8211; Was osgIntrospection found? OSGINTROSPECTION_INCLUDE_DIR &#8211; Where to find the headers OSGINTROSPECTION_LIBRARIES &#8211; The libraries to link for osgIntrospection (use this) </p>
<p> OSGINTROSPECTION_LIBRARY &#8211; The osgIntrospection library OSGINTROSPECTION_LIBRARY_DEBUG &#8211; The osgIntrospection debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgManipulator</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgManipulator This module defines </p>
<p> OSGMANIPULATOR_FOUND &#8211; Was osgManipulator found? OSGMANIPULATOR_INCLUDE_DIR &#8211; Where to find the headers OSGMANIPULATOR_LIBRARIES &#8211; The libraries to link for osgManipulator (use this) </p>
<p> OSGMANIPULATOR_LIBRARY &#8211; The osgManipulator library OSGMANIPULATOR_LIBRARY_DEBUG &#8211; The osgManipulator debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgParticle</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgParticle This module defines </p>
<p> OSGPARTICLE_FOUND &#8211; Was osgParticle found? OSGPARTICLE_INCLUDE_DIR &#8211; Where to find the headers OSGPARTICLE_LIBRARIES &#8211; The libraries to link for osgParticle (use this) </p>
<p> OSGPARTICLE_LIBRARY &#8211; The osgParticle library OSGPARTICLE_LIBRARY_DEBUG &#8211; The osgParticle debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgPresentation</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgPresentation This module defines </p>
<p> OSGPRESENTATION_FOUND &#8211; Was osgPresentation found? OSGPRESENTATION_INCLUDE_DIR &#8211; Where to find the headers OSGPRESENTATION_LIBRARIES &#8211; The libraries to link for osgPresentation (use this) </p>
<p> OSGPRESENTATION_LIBRARY &#8211; The osgPresentation library OSGPRESENTATION_LIBRARY_DEBUG &#8211; The osgPresentation debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. Modified to work with osgPresentation by Robert Osfield, January 2012. </p>
<dt><code>FindosgProducer</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgProducer This module defines </p>
<p> OSGPRODUCER_FOUND &#8211; Was osgProducer found? OSGPRODUCER_INCLUDE_DIR &#8211; Where to find the headers OSGPRODUCER_LIBRARIES &#8211; The libraries to link for osgProducer (use this) </p>
<p> OSGPRODUCER_LIBRARY &#8211; The osgProducer library OSGPRODUCER_LIBRARY_DEBUG &#8211; The osgProducer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgQt</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgQt This module defines </p>
<p> OSGQT_FOUND &#8211; Was osgQt found? OSGQT_INCLUDE_DIR &#8211; Where to find the headers OSGQT_LIBRARIES &#8211; The libraries to link for osgQt (use this) </p>
<p> OSGQT_LIBRARY &#8211; The osgQt library OSGQT_LIBRARY_DEBUG &#8211; The osgQt debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. Modified to work with osgQt by Robert Osfield, January 2012. </p>
<dt><code>FindosgShadow</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgShadow This module defines </p>
<p> OSGSHADOW_FOUND &#8211; Was osgShadow found? OSGSHADOW_INCLUDE_DIR &#8211; Where to find the headers OSGSHADOW_LIBRARIES &#8211; The libraries to link for osgShadow (use this) </p>
<p> OSGSHADOW_LIBRARY &#8211; The osgShadow library OSGSHADOW_LIBRARY_DEBUG &#8211; The osgShadow debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgSim</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgSim This module defines </p>
<p> OSGSIM_FOUND &#8211; Was osgSim found? OSGSIM_INCLUDE_DIR &#8211; Where to find the headers OSGSIM_LIBRARIES &#8211; The libraries to link for osgSim (use this) </p>
<p> OSGSIM_LIBRARY &#8211; The osgSim library OSGSIM_LIBRARY_DEBUG &#8211; The osgSim debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgTerrain</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgTerrain This module defines </p>
<p> OSGTERRAIN_FOUND &#8211; Was osgTerrain found? OSGTERRAIN_INCLUDE_DIR &#8211; Where to find the headers OSGTERRAIN_LIBRARIES &#8211; The libraries to link for osgTerrain (use this) </p>
<p> OSGTERRAIN_LIBRARY &#8211; The osgTerrain library OSGTERRAIN_LIBRARY_DEBUG &#8211; The osgTerrain debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgText</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgText This module defines </p>
<p> OSGTEXT_FOUND &#8211; Was osgText found? OSGTEXT_INCLUDE_DIR &#8211; Where to find the headers OSGTEXT_LIBRARIES &#8211; The libraries to link for osgText (use this) </p>
<p> OSGTEXT_LIBRARY &#8211; The osgText library OSGTEXT_LIBRARY_DEBUG &#8211; The osgText debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgUtil</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgUtil This module defines </p>
<p> OSGUTIL_FOUND &#8211; Was osgUtil found? OSGUTIL_INCLUDE_DIR &#8211; Where to find the headers OSGUTIL_LIBRARIES &#8211; The libraries to link for osgUtil (use this) </p>
<p> OSGUTIL_LIBRARY &#8211; The osgUtil library OSGUTIL_LIBRARY_DEBUG &#8211; The osgUtil debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgViewer</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgViewer This module defines </p>
<p> OSGVIEWER_FOUND &#8211; Was osgViewer found? OSGVIEWER_INCLUDE_DIR &#8211; Where to find the headers OSGVIEWER_LIBRARIES &#8211; The libraries to link for osgViewer (use this) </p>
<p> OSGVIEWER_LIBRARY &#8211; The osgViewer library OSGVIEWER_LIBRARY_DEBUG &#8211; The osgViewer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgVolume</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgVolume This module defines </p>
<p> OSGVOLUME_FOUND &#8211; Was osgVolume found? OSGVOLUME_INCLUDE_DIR &#8211; Where to find the headers OSGVOLUME_LIBRARIES &#8211; The libraries to link for osgVolume (use this) </p>
<p> OSGVOLUME_LIBRARY &#8211; The osgVolume library OSGVOLUME_LIBRARY_DEBUG &#8211; The osgVolume debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgWidget</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgWidget This module defines </p>
<p> OSGWIDGET_FOUND &#8211; Was osgWidget found? OSGWIDGET_INCLUDE_DIR &#8211; Where to find the headers OSGWIDGET_LIBRARIES &#8211; The libraries to link for osgWidget (use this) </p>
<p> OSGWIDGET_LIBRARY &#8211; The osgWidget library OSGWIDGET_LIBRARY_DEBUG &#8211; The osgWidget debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> FindosgWidget.cmake tweaked from Findosg* suite as created by Eric Wing. </p>
<dt><code>Findosg_functions</code></p>
<dd>
<p> This CMake file contains two macros to assist with searching for OSG libraries and nodekits. Please see FindOpenSceneGraph.cmake for full documentation. </p>
<dt><code>FindwxWidgets</code></p>
<dd> Find a wxWidgets (a.k.a., wxWindows) installation. </p>
<p> This module finds if wxWidgets is installed and selects a default configuration to use. wxWidgets is a modular library. To specify the modules that you will use, you need to name them as components to the package: </p>
<p> find_package(wxWidgets COMPONENTS core base &#8230;) </p>
<p> There are two search branches: a windows style and a unix style. For windows, the following variables are searched for and set to defaults in case of multiple choices. Change them if the defaults are not desired (i.e., these are the only variables you should change to select a configuration): </p>
<pre>
  wxWidgets_ROOT_DIR      - Base wxWidgets directory
                            (e.g., C:/wxWidgets-2.6.3).
  wxWidgets_LIB_DIR       - Path to wxWidgets libraries
                            (e.g., C:/wxWidgets-2.6.3/lib/vc_lib).
  wxWidgets_CONFIGURATION - Configuration to use
                            (e.g., msw, mswd, mswu, mswunivud, etc.)
  wxWidgets_EXCLUDE_COMMON_LIBRARIES
                          - Set to TRUE to exclude linking of
                            commonly required libs (e.g., png tiff
                            jpeg zlib regex expat).
</pre>
<p> For unix style it uses the wx-config utility. You can select between debug/release, unicode/ansi, universal/non-universal, and static/shared in the QtDialog or ccmake interfaces by turning ON/OFF the following variables: </p>
<pre>
  wxWidgets_USE_DEBUG
  wxWidgets_USE_UNICODE
  wxWidgets_USE_UNIVERSAL
  wxWidgets_USE_STATIC
</pre>
<p> There is also a wxWidgets_CONFIG_OPTIONS variable for all other options that need to be passed to the wx-config utility. For example, to use the base toolkit found in the /usr/local path, set the variable (before calling the FIND_PACKAGE command) as such: </p>
<pre>
  set(wxWidgets_CONFIG_OPTIONS --toolkit=base --prefix=/usr)
</pre>
<p> The following are set after the configuration is done for both windows and unix style: </p>
<p>  wxWidgets_FOUND            &#8211; Set to TRUE if wxWidgets was found.<br />
  wxWidgets_INCLUDE_DIRS     &#8211; Include directories for WIN32<br />
                               i.e., where to find &#8220;wx/wx.h&#8221; and<br />
                               &#8220;wx/setup.h&#8221;; possibly empty for unices.<br />
  wxWidgets_LIBRARIES        &#8211; Path to the wxWidgets libraries.<br />
  wxWidgets_LIBRARY_DIRS     &#8211; compile time link dirs, useful for<br />
                               rpath on UNIX. Typically an empty string<br />
                               in WIN32 environment.<br />
  wxWidgets_DEFINITIONS      &#8211; Contains defines required to compile/link<br />
                               against WX, e.g. WXUSINGDLL<br />
  wxWidgets_DEFINITIONS_DEBUG- Contains defines required to compile/link<br />
                               against WX debug builds, e.g. __WXDEBUG__<br />
  wxWidgets_CXX_FLAGS        &#8211; Include dirs and compiler flags for<br />
                               unices, empty on WIN32. Essentially<br />
                               &#8220;`wx-config &#8211;cxxflags`&#8221;.<br />
  wxWidgets_USE_FILE         &#8211; Convenience include file.</p>
<p> Sample usage: </p>
<p>#Note that for MinGW users the order of libs is important !<br />
find_package(wxWidgets COMPONENTS net gl core base) if (wxWidgets_FOUND)<br />
    include(${wxWidgets_USE_FILE})<br />
#and for each of your dependent executable / library targets:<br />
        target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})<br />
            endif()</p>
<p> If wxWidgets is required (i.e., not an optional part): </p>
<p>find_package(wxWidgets REQUIRED net gl core base)<br />
    include(${wxWidgets_USE_FILE})<br />
#and for each of your dependent executable / library targets:<br />
        target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})</p>
<dt><code>FindwxWindows</code></p>
<dd> Find wxWindows (wxWidgets) installation </p>
<p> This module finds if wxWindows/wxWidgets is installed and determines where the include files and libraries are. It also determines what the name of the library is. Please note this file is DEPRECATED and replaced by FindwxWidgets.cmake. This code sets the following variables: </p>
<p>  WXWINDOWS_FOUND     = system has WxWindows<br />
  WXWINDOWS_LIBRARIES = path to the wxWindows libraries<br />
                        on Unix/Linux with additional<br />
                        linker flags from<br />
                        &#8220;wx-config &#8211;libs&#8221;<br />
  CMAKE_WXWINDOWS_CXX_FLAGS  = Compiler flags for wxWindows,<br />
                               essentially &#8220;`wx-config &#8211;cxxflags`&#8221;<br />
                               on Linux<br />
  WXWINDOWS_INCLUDE_DIR      = where to find &#8220;wx/wx.h&#8221; and &#8220;wx/setup.h&#8221;<br />
  WXWINDOWS_LINK_DIRECTORIES = link directories, useful for rpath on<br />
                                Unix<br />
  WXWINDOWS_DEFINITIONS      = extra defines</p>
<p> OPTIONS If you need OpenGL support please </p>
<pre>
  set(WXWINDOWS_USE_GL 1)
</pre>
<p> in your CMakeLists.txt *before* you include this file. </p>
<pre>
  HAVE_ISYSTEM      - true required to replace -I by -isystem on g++
</pre>
<p> For convenience include Use_wxWindows.cmake in your project&#8217;s CMakeLists.txt using include(${CMAKE_CURRENT_LIST_DIR}/Use_wxWindows.cmake). </p>
<p> USAGE </p>
<pre>
  set(WXWINDOWS_USE_GL 1)
  find_package(wxWindows)
</pre>
<p> NOTES wxWidgets 2.6.x is supported for monolithic builds e.g. compiled in wx/build/msw dir as: </p>
<pre>
  nmake -f makefile.vc BUILD=debug SHARED=0 USE_OPENGL=1 MONOLITHIC=1
</pre>
<p> DEPRECATED </p>
<pre>
  CMAKE_WX_CAN_COMPILE
  WXWINDOWS_LIBRARY
  CMAKE_WX_CXX_FLAGS
  WXWINDOWS_INCLUDE_PATH
</pre>
<p> AUTHOR Jan Woetzel &lt;<a rel="nofollow" href="http://www.mip.informatik.uni-kiel.de/~jw">http://www.mip.informatik.uni-kiel.de/~jw</a>&gt; (07/2003-01/2006) </p>
<dt><code>FortranCInterface</code></p>
<dd> Fortran/C Interface Detection </p>
<p> This module automatically detects the API by which C and Fortran languages interact. Variables indicate if the mangling is found: </p>
<pre>
   FortranCInterface_GLOBAL_FOUND = Global subroutines and functions
   FortranCInterface_MODULE_FOUND = Module subroutines and functions
                                    (declared by &quot;MODULE PROCEDURE&quot;)
</pre>
<p> A function is provided to generate a C header file containing macros to mangle symbol names: </p>
<p>FortranCInterface_HEADER(&lt;file&gt;[MACRO_NAMESPACE&lt;macro &#8211; ns&gt;]<br />
                               [SYMBOL_NAMESPACE&lt;ns&gt;]<br />
                               [SYMBOLS [&lt;module&gt;:]&lt;function&gt;&#8230;])</p>
<p> It generates in &lt;file&gt; definitions of the following macros: </p>
<p>#define FortranCInterface_GLOBAL (name, NAME)&#8230;<br />
#define FortranCInterface_GLOBAL_(name, NAME) &#8230;<br />
#define FortranCInterface_MODULE (mod, name, MOD, NAME)&#8230;<br />
#define FortranCInterface_MODULE_(mod, name, MOD, NAME) &#8230;</p>
<p> These macros mangle four categories of Fortran symbols, respectively: </p>
<pre>
   - Global symbols without '_': call mysub()
   - Global symbols with '_'   : call my_sub()
   - Module symbols without '_': use mymod; call mysub()
   - Module symbols with '_'   : use mymod; call my_sub()
</pre>
<p> If mangling for a category is not known, its macro is left undefined. All macros require raw names in both lower case and upper case. The MACRO_NAMESPACE option replaces the default &quot;FortranCInterface_&quot; prefix with a given namespace &quot;&lt;macro-ns&gt;&quot;. </p>
<p> The SYMBOLS option lists symbols to mangle automatically with C preprocessor definitions: </p>
<p>   &lt;function&gt;          ==&gt; #define &lt;ns&gt;&lt;function&gt; &#8230;<br />
   &lt;module&gt;:&lt;function&gt; ==&gt; #define &lt;ns&gt;&lt;module&gt;_&lt;function&gt; &#8230;</p>
<p> If the mangling for some symbol is not known then no preprocessor definition is created, and a warning is displayed. The SYMBOL_NAMESPACE option prefixes all preprocessor definitions generated by the SYMBOLS option with a given namespace &quot;&lt;ns&gt;&quot;. </p>
<p> Example usage: </p>
<pre>
   include(FortranCInterface)
   FortranCInterface_HEADER(FC.h MACRO_NAMESPACE &quot;FC_&quot;)
</pre>
<p> This creates a &quot;FC.h&quot; header that defines mangling macros FC_GLOBAL(), FC_GLOBAL_(), FC_MODULE(), and FC_MODULE_(). </p>
<p> Example usage: </p>
<pre>
   include(FortranCInterface)
   FortranCInterface_HEADER(FCMangle.h
                            MACRO_NAMESPACE &quot;FC_&quot;
                            SYMBOL_NAMESPACE &quot;FC_&quot;
                            SYMBOLS mysub mymod:my_sub)
</pre>
<p> This creates a &quot;FCMangle.h&quot; header that defines the same FC_*() mangling macros as the previous example plus preprocessor symbols FC_mysub and FC_mymod_my_sub. </p>
<p> Another function is provided to verify that the Fortran and C/C++ compilers work together: </p>
<p>FortranCInterface_VERIFY([CXX][QUIET])</p>
<p> It tests whether a simple test executable using Fortran and C (and C++ when the CXX option is given) compiles and links successfully. The result is stored in the cache entry FortranCInterface_VERIFIED_C (or FortranCInterface_VERIFIED_CXX if CXX is given) as a boolean. If the check fails and QUIET is not given the function terminates with a FATAL_ERROR message describing the problem. The purpose of this check is to stop a build early for incompatible compiler combinations. The test is built in the Release configuration. </p>
<p> FortranCInterface is aware of possible GLOBAL and MODULE manglings for many Fortran compilers, but it also provides an interface to specify new possible manglings. Set the variables </p>
<pre>
   FortranCInterface_GLOBAL_SYMBOLS
   FortranCInterface_MODULE_SYMBOLS
</pre>
<p> before including FortranCInterface to specify manglings of the symbols &quot;MySub&quot;, &quot;My_Sub&quot;, &quot;MyModule:MySub&quot;, and &quot;My_Module:My_Sub&quot;. For example, the code: </p>
<pre>
   set(FortranCInterface_GLOBAL_SYMBOLS mysub_ my_sub__ MYSUB_)
     #                                  ^^^^^  ^^^^^^   ^^^^^
   set(FortranCInterface_MODULE_SYMBOLS
       __mymodule_MOD_mysub __my_module_MOD_my_sub)
     #   ^^^^^^^^     ^^^^^   ^^^^^^^^^     ^^^^^^
   include(FortranCInterface)
</pre>
<p> tells FortranCInterface to try given GLOBAL and MODULE manglings. (The carets point at raw symbol names for clarity in this example but are not needed.) </p>
<dt><code>GNUInstallDirs</code></p>
<dd> Define GNU standard installation directories </p>
<p> Provides install directory variables as defined for GNU software: </p>
<pre>
  <a rel="nofollow" href="http://www.gnu.org/prep/standards/html_node/Directory-Variables.html">http://www.gnu.org/prep/standards/html_node/Directory-Variables.html</a>
</pre>
<p> Inclusion of this module defines the following variables: </p>
<pre>
  CMAKE_INSTALL_&lt;dir&gt;      - destination for files of a given type
  CMAKE_INSTALL_FULL_&lt;dir&gt; - corresponding absolute path
</pre>
<p> where &lt;dir&gt; is one of: </p>
<pre>
  BINDIR           - user executables (bin)
  SBINDIR          - system admin executables (sbin)
  LIBEXECDIR       - program executables (libexec)
  SYSCONFDIR       - read-only single-machine data (etc)
  SHAREDSTATEDIR   - modifiable architecture-independent data (com)
  LOCALSTATEDIR    - modifiable single-machine data (var)
  LIBDIR           - object code libraries (lib or lib64 or lib/&lt;multiarch-tuple&gt; on Debian)
  INCLUDEDIR       - C header files (include)
  OLDINCLUDEDIR    - C header files for non-gcc (/usr/include)
  DATAROOTDIR      - read-only architecture-independent data root (share)
  DATADIR          - read-only architecture-independent data (DATAROOTDIR)
  INFODIR          - info documentation (DATAROOTDIR/info)
  LOCALEDIR        - locale-dependent data (DATAROOTDIR/locale)
  MANDIR           - man documentation (DATAROOTDIR/man)
  DOCDIR           - documentation root (DATAROOTDIR/doc/PROJECT_NAME)
</pre>
<p> Each CMAKE_INSTALL_&lt;dir&gt; value may be passed to the DESTINATION options of install() commands for the corresponding file type. If the includer does not define a value the above-shown default will be used and the value will appear in the cache for editing by the user. Each CMAKE_INSTALL_FULL_&lt;dir&gt; value contains an absolute path constructed from the corresponding destination by prepending (if necessary) the value of CMAKE_INSTALL_PREFIX. </p>
<dt><code>GenerateExportHeader</code></p>
<dd> Function for generation of export macros for libraries </p>
<p> This module provides the function GENERATE_EXPORT_HEADER() and the accompanying ADD_COMPILER_EXPORT_FLAGS() function. </p>
<p> The GENERATE_EXPORT_HEADER function can be used to generate a file suitable for preprocessor inclusion which contains EXPORT macros to be used in library classes. </p>
<p> GENERATE_EXPORT_HEADER( LIBRARY_TARGET </p>
<p>[BASE_NAME&lt;base_name&gt;]<br />
    [EXPORT_MACRO_NAME&lt;export_macro_name&gt;]<br />
    [EXPORT_FILE_NAME&lt;export_file_name&gt;]<br />
    [DEPRECATED_MACRO_NAME&lt;deprecated_macro_name&gt;]<br />
    [NO_EXPORT_MACRO_NAME&lt;no_export_macro_name&gt;]<br />
    [STATIC_DEFINE&lt;static_define&gt;]<br />
    [NO_DEPRECATED_MACRO_NAME&lt;no_deprecated_macro_name&gt;]<br />
    [DEFINE_NO_DEPRECATED]<br />
    [PREFIX_NAME&lt;prefix_name&gt;]</p>
<p> ) </p>
<p> ADD_COMPILER_EXPORT_FLAGS( [&lt;output_variable&gt;] ) </p>
<p> By default GENERATE_EXPORT_HEADER() generates macro names in a file name determined by the name of the library. The ADD_COMPILER_EXPORT_FLAGS function adds -fvisibility=hidden to CMAKE_CXX_FLAGS if supported, and is a no-op on Windows which does not need extra compiler flags for exporting support. You may optionally pass a single argument to ADD_COMPILER_EXPORT_FLAGS that will be populated with the required CXX_FLAGS required to enable visibility support for the compiler/architecture in use. </p>
<p> This means that in the simplest case, users of these functions will be equivalent to: </p>
<p>add_compiler_export_flags()<br />
    add_library(somelib someclass.cpp)<br />
        generate_export_header(somelib)<br />
            install(TARGETS somelib DESTINATION ${LIBRARY_INSTALL_DIR})<br />
                install(FILES<br />
                            someclass.h<br />
                                ${PROJECT_BINARY_DIR} /<br />
                        somelib_export.h DESTINATION ${INCLUDE_INSTALL_DIR})</p>
<p> And in the ABI header files: </p>
<p>#include &#8220;somelib_export.h&#8221;<br />
class SOMELIB_EXPORT SomeClass<br />
{<br />
    &#8230;<br />
};</p>
<p> The CMake fragment will generate a file in the ${CMAKE_CURRENT_BINARY_DIR} called somelib_export.h containing the macros SOMELIB_EXPORT, SOMELIB_NO_EXPORT, SOMELIB_DEPRECATED, SOMELIB_DEPRECATED_EXPORT and SOMELIB_DEPRECATED_NO_EXPORT. The resulting file should be installed with other headers in the library. </p>
<p> The BASE_NAME argument can be used to override the file name and the names used for the macros </p>
<pre>
   add_library(somelib someclass.cpp)
   generate_export_header(somelib
     BASE_NAME other_name
   )
</pre>
<p> Generates a file called other_name_export.h containing the macros OTHER_NAME_EXPORT, OTHER_NAME_NO_EXPORT and OTHER_NAME_DEPRECATED etc. </p>
<p> The BASE_NAME may be overridden by specifiying other options in the function. For example: </p>
<pre>
   add_library(somelib someclass.cpp)
   generate_export_header(somelib
     EXPORT_MACRO_NAME OTHER_NAME_EXPORT
   )
</pre>
<p> creates the macro OTHER_NAME_EXPORT instead of SOMELIB_EXPORT, but other macros and the generated file name is as default. </p>
<pre>
   add_library(somelib someclass.cpp)
   generate_export_header(somelib
     DEPRECATED_MACRO_NAME KDE_DEPRECATED
   )
</pre>
<p> creates the macro KDE_DEPRECATED instead of SOMELIB_DEPRECATED. </p>
<p> If LIBRARY_TARGET is a static library, macros are defined without values. </p>
<p> If the same sources are used to create both a shared and a static library, the uppercased symbol ${BASE_NAME}_STATIC_DEFINE should be used when building the static library </p>
<p>add_library(shared_variant SHARED ${lib_SRCS})<br />
    add_library(static_variant ${lib_SRCS})<br />
        generate_export_header(shared_variant BASE_NAME libshared_and_static)<br />
            set_target_properties(static_variant PROPERTIES<br />
                                      COMPILE_FLAGS &#8211;<br />
                                  DLIBSHARED_AND_STATIC_STATIC_DEFINE)</p>
<p> This will cause the export macros to expand to nothing when building the static library. </p>
<p> If DEFINE_NO_DEPRECATED is specified, then a macro ${BASE_NAME}_NO_DEPRECATED will be defined This macro can be used to remove deprecated code from preprocessor output. </p>
<p>option(EXCLUDE_DEPRECATED &#8220;Exclude deprecated parts of the library&#8221; FALSE) if (EXCLUDE_DEPRECATED)<br />
    set(NO_BUILD_DEPRECATED DEFINE_NO_DEPRECATED)<br />
        endif()<br />
            generate_export_header(somelib ${NO_BUILD_DEPRECATED})</p>
<p> And then in somelib: </p>
<p>class SOMELIB_EXPORT SomeClass<br />
{<br />
  public:<br />
#ifndef SOMELIB_NO_DEPRECATED<br />
    SOMELIB_DEPRECATED void oldMethod();<br />
#endif<br />
};</p>
<p>#ifndef SOMELIB_NO_DEPRECATED<br />
void SomeClass::oldMethod()<br />
{<br />
}<br />
#endif</p>
<p> If PREFIX_NAME is specified, the argument will be used as a prefix to all generated macros. </p>
<p> For example: </p>
<pre>
   generate_export_header(somelib PREFIX_NAME VTK_)
</pre>
<p> Generates the macros VTK_SOMELIB_EXPORT etc. </p>
<dt><code>GetPrerequisites</code></p>
<dd> Functions to analyze and list executable file prerequisites. </p>
<p> This module provides functions to list the .dll, .dylib or .so files that an executable or shared library file depends on. (Its prerequisites.) </p>
<p> It uses various tools to obtain the list of required shared library files: </p>
<pre>
   dumpbin (Windows)
   objdump (MinGW on Windows)
   ldd (Linux/Unix)
   otool (Mac OSX)
</pre>
<p> The following functions are provided by this module: </p>
<pre>
   get_prerequisites
   list_prerequisites
   list_prerequisites_by_glob
   gp_append_unique
   is_file_executable
   gp_item_default_embedded_path
     (projects can override with gp_item_default_embedded_path_override)
   gp_resolve_item
     (projects can override with gp_resolve_item_override)
   gp_resolved_file_type
     (projects can override with gp_resolved_file_type_override)
   gp_file_type
</pre>
<p> Requires CMake 2.6 or greater because it uses function, break, return and PARENT_SCOPE. </p>
<pre>
  GET_PREREQUISITES(&lt;target&gt; &lt;prerequisites_var&gt; &lt;exclude_system&gt; &lt;recurse&gt;
                    &lt;exepath&gt; &lt;dirs&gt;)
</pre>
<p> Get the list of shared library files required by &lt;target&gt;. The list in the variable named &lt;prerequisites_var&gt; should be empty on first entry to this function. On exit, &lt;prerequisites_var&gt; will contain the list of required shared library files. </p>
<p> &lt;target&gt; is the full path to an executable file. &lt;prerequisites_var&gt; is the name of a CMake variable to contain the results. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exepath&gt; is the path to the top level executable used for @executable_path replacment on the Mac. &lt;dirs&gt; is a list of paths where libraries might be found: these paths are searched first when a target without any path info is given. Then standard system locations are also searched: PATH, Framework locations, /usr/lib&#8230; </p>
<p>LIST_PREREQUISITES(&lt;target&gt;[&lt;recurse&gt;[&lt;exclude_system&gt;[&lt;verbose&gt;]]])</p>
<p> Print a message listing the prerequisites of &lt;target&gt;. </p>
<p> &lt;target&gt; is the name of a shared library or executable target or the full path to a shared library or executable file. If &lt;recurse&gt; is set to 1 all prerequisites will be found recursively, if set to 0 only direct prerequisites are listed. &lt;exclude_system&gt; must be 0 or 1 indicating whether to include or exclude &quot;system&quot; prerequisites. With &lt;verbose&gt; set to 0 only the full path names of the prerequisites are printed, set to 1 extra informatin will be displayed. </p>
<pre>
  LIST_PREREQUISITES_BY_GLOB(&lt;glob_arg&gt; &lt;glob_exp&gt;)
</pre>
<p> Print the prerequisites of shared library and executable files matching a globbing pattern. &lt;glob_arg&gt; is GLOB or GLOB_RECURSE and &lt;glob_exp&gt; is a globbing expression used with &quot;file(GLOB&quot; or &quot;file(GLOB_RECURSE&quot; to retrieve a list of matching files. If a matching file is executable, its prerequisites are listed. </p>
<p> Any additional (optional) arguments provided are passed along as the optional arguments to the list_prerequisites calls. </p>
<pre>
  GP_APPEND_UNIQUE(&lt;list_var&gt; &lt;value&gt;)
</pre>
<p> Append &lt;value&gt; to the list variable &lt;list_var&gt; only if the value is not already in the list. </p>
<pre>
  IS_FILE_EXECUTABLE(&lt;file&gt; &lt;result_var&gt;)
</pre>
<p> Return 1 in &lt;result_var&gt; if &lt;file&gt; is a binary executable, 0 otherwise. </p>
<pre>
  GP_ITEM_DEFAULT_EMBEDDED_PATH(&lt;item&gt; &lt;default_embedded_path_var&gt;)
</pre>
<p> Return the path that others should refer to the item by when the item is embedded inside a bundle. </p>
<p> Override on a per-project basis by providing a project-specific gp_item_default_embedded_path_override function. </p>
<pre>
  GP_RESOLVE_ITEM(&lt;context&gt; &lt;item&gt; &lt;exepath&gt; &lt;dirs&gt; &lt;resolved_item_var&gt;)
</pre>
<p> Resolve an item into an existing full path file. </p>
<p> Override on a per-project basis by providing a project-specific gp_resolve_item_override function. </p>
<pre>
  GP_RESOLVED_FILE_TYPE(&lt;original_file&gt; &lt;file&gt; &lt;exepath&gt; &lt;dirs&gt; &lt;type_var&gt;)
</pre>
<p> Return the type of &lt;file&gt; with respect to &lt;original_file&gt;. String describing type of prerequisite is returned in variable named &lt;type_var&gt;. </p>
<p> Use &lt;exepath&gt; and &lt;dirs&gt; if necessary to resolve non-absolute &lt;file&gt; values &#8212; but only for non-embedded items. </p>
<p> Possible types are: </p>
<pre>
   system
   local
   embedded
   other
</pre>
<p> Override on a per-project basis by providing a project-specific gp_resolved_file_type_override function. </p>
<pre>
  GP_FILE_TYPE(&lt;original_file&gt; &lt;file&gt; &lt;type_var&gt;)
</pre>
<p> Return the type of &lt;file&gt; with respect to &lt;original_file&gt;. String describing type of prerequisite is returned in variable named &lt;type_var&gt;. </p>
<p> Possible types are: </p>
<pre>
   system
   local
   embedded
   other
</pre>
<dt><code>InstallRequiredSystemLibraries</code></p>
<dd>
<p> By including this file, all library files listed in the variable CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS will be installed with install(PROGRAMS &#8230;) into bin for WIN32 and lib for non-WIN32. If CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_SKIP is set to TRUE before including this file, then the INSTALL command is not called. The user can use the variable CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS to use a custom install command and install them however they want. If it is the MSVC compiler, then the microsoft run time libraries will be found and automatically added to the CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS, and installed. If CMAKE_INSTALL_DEBUG_LIBRARIES is set and it is the MSVC compiler, then the debug libraries are installed when available. If CMAKE_INSTALL_DEBUG_LIBRARIES_ONLY is set then only the debug libraries are installed when both debug and release are available. If CMAKE_INSTALL_MFC_LIBRARIES is set then the MFC run time libraries are installed as well as the CRT run time libraries. If CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION is set then the libraries are installed to that directory rather than the default. If CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_NO_WARNINGS is NOT set, then this file warns about required files that do not exist. You can set this variable to ON before including this file to avoid the warning. For example, the Visual Studio Express editions do not include the redistributable files, so if you include this file on a machine with only VS Express installed, you&#8217;ll get the warning. </p>
<dt><code>MacroAddFileDependencies</code></p>
<dd> MACRO_ADD_FILE_DEPENDENCIES(&lt;_file&gt; depend_files&#8230;) </p>
<p> Using the macro MACRO_ADD_FILE_DEPENDENCIES() is discouraged. There are usually better ways to specify the correct dependencies. </p>
<p> MACRO_ADD_FILE_DEPENDENCIES(&lt;_file&gt; depend_files&#8230;) is just a convenience wrapper around the OBJECT_DEPENDS source file property. You can just use set_property(SOURCE &lt;file&gt; APPEND PROPERTY OBJECT_DEPENDS depend_files) instead. </p>
<dt><code>ProcessorCount</code></p>
<dd> ProcessorCount(var) </p>
<p> Determine the number of processors/cores and save value in ${var} </p>
<p> Sets the variable named ${var} to the number of physical cores available on the machine if the information can be determined. Otherwise it is set to 0. Currently this functionality is implemented for AIX, cygwin, FreeBSD, HPUX, IRIX, Linux, Mac OS X, QNX, Sun and Windows. </p>
<p> This function is guaranteed to return a positive integer (&gt;=1) if it succeeds. It returns 0 if there&#8217;s a problem determining the processor count. </p>
<p> Example use, in a ctest -S dashboard script: </p>
<p>include(ProcessorCount)<br />
    ProcessorCount(N) if (NOT N EQUAL 0)<br />
        set(CTEST_BUILD_FLAGS &#8211; j${N})<br />
            set(ctest_test_args ${ctest_test_args} PARALLEL_LEVEL ${N})<br />
                endif()</p>
<p> This function is intended to offer an approximation of the value of the number of compute cores available on the current machine, such that you may use that value for parallel building and parallel testing. It is meant to help utilize as much of the machine as seems reasonable. Of course, knowledge of what else might be running on the machine simultaneously should be used when deciding whether to request a machine&#8217;s full capacity all for yourself. </p>
<dt><code>Qt4ConfigDependentSettings</code></p>
<dd>
<p> This file is included by FindQt4.cmake, don&#8217;t include it directly. </p>
<dt><code>Qt4Macros</code></p>
<dd>
<p> This file is included by FindQt4.cmake, don&#8217;t include it directly. </p>
<dt><code>SelectLibraryConfigurations</code></p>
<dd>
<p> select_library_configurations( basename ) </p>
<p> This macro takes a library base name as an argument, and will choose good values for basename_LIBRARY, basename_LIBRARIES, basename_LIBRARY_DEBUG, and basename_LIBRARY_RELEASE depending on what has been found and set. If only basename_LIBRARY_RELEASE is defined, basename_LIBRARY will be set to the release value, and basename_LIBRARY_DEBUG will be set to basename_LIBRARY_DEBUG-NOTFOUND. If only basename_LIBRARY_DEBUG is defined, then basename_LIBRARY will take the debug value, and basename_LIBRARY_RELEASE will be set to basename_LIBRARY_RELEASE-NOTFOUND. </p>
<p> If the generator supports configuration types, then basename_LIBRARY and basename_LIBRARIES will be set with debug and optimized flags specifying the library to be used for the given configuration. If no build type has been set or the generator in use does not support configuration types, then basename_LIBRARY and basename_LIBRARIES will take only the release value, or the debug value if the release one is not set. </p>
<dt><code>SquishTestScript</code></p>
<dd>
<p> This script launches a GUI test using Squish. You should not call the script directly; instead, you should access it via the SQUISH_ADD_TEST macro that is defined in FindSquish.cmake. </p>
<p> This script starts the Squish server, launches the test on the client, and finally stops the squish server. If any of these steps fail (including if the tests do not pass) then a fatal error is raised. </p>
<dt><code>TestBigEndian</code></p>
<dd> Define macro to determine endian type </p>
<p> Check if the system is big endian or little endian </p>
<pre>
  TEST_BIG_ENDIAN(VARIABLE)
  VARIABLE - variable to store the result to
</pre>
<dt><code>TestCXXAcceptsFlag</code></p>
<dd> Test CXX compiler for a flag </p>
<p> Check if the CXX compiler accepts a flag </p>
<pre>
  Macro CHECK_CXX_ACCEPTS_FLAG(FLAGS VARIABLE) -
     checks if the function exists
  FLAGS - the flags to try
  VARIABLE - variable to store the result
</pre>
<dt><code>TestForANSIForScope</code></p>
<dd> Check for ANSI for scope support </p>
<p> Check if the compiler restricts the scope of variables declared in a for-init-statement to the loop body. </p>
<pre>
  CMAKE_NO_ANSI_FOR_SCOPE - holds result
</pre>
<dt><code>TestForANSIStreamHeaders</code></p>
<dd> Test for compiler support of ANSI stream headers iostream, etc. </p>
<p> check if the compiler supports the standard ANSI iostream header (without the .h) </p>
<pre>
  CMAKE_NO_ANSI_STREAM_HEADERS - defined by the results
</pre>
<dt><code>TestForSSTREAM</code></p>
<dd> Test for compiler support of ANSI sstream header </p>
<p> check if the compiler supports the standard ANSI sstream header </p>
<pre>
  CMAKE_NO_ANSI_STRING_STREAM - defined by the results
</pre>
<dt><code>TestForSTDNamespace</code></p>
<dd> Test for std:: namespace support </p>
<p> check if the compiler supports std:: on stl classes </p>
<pre>
  CMAKE_NO_STD_NAMESPACE - defined by the results
</pre>
<dt><code>UseEcos</code></p>
<dd> This module defines variables and macros required to build eCos application. </p>
<p> This file contains the following macros: ECOS_ADD_INCLUDE_DIRECTORIES() &#8211; add the eCos include dirs ECOS_ADD_EXECUTABLE(name source1 &#8230; sourceN ) &#8211; create an eCos executable ECOS_ADJUST_DIRECTORY(VAR source1 &#8230; sourceN ) &#8211; adjusts the path of the source files and puts the result into VAR </p>
<p> Macros for selecting the toolchain: ECOS_USE_ARM_ELF_TOOLS() &#8211; enable the ARM ELF toolchain for the directory where it is called ECOS_USE_I386_ELF_TOOLS() &#8211; enable the i386 ELF toolchain for the directory where it is called ECOS_USE_PPC_EABI_TOOLS() &#8211; enable the PowerPC toolchain for the directory where it is called </p>
<p> It contains the following variables: ECOS_DEFINITIONS ECOSCONFIG_EXECUTABLE ECOS_CONFIG_FILE &#8211; defaults to ecos.ecc, if your eCos configuration file has a different name, adjust this variable for internal use only: </p>
<pre>
  ECOS_ADD_TARGET_LIB
</pre>
<dt><code>UseJava</code></p>
<dd> Use Module for Java </p>
<p> This file provides functions for Java. It is assumed that FindJava.cmake has already been loaded. See FindJava.cmake for information on how to load Java into your CMake project. </p>
<p> add_jar(target_name </p>
<p>         [SOURCES] source1 [source2 &#8230;] [resource1 &#8230;]<br />
         [INCLUDE_JARS jar1 [jar2 &#8230;]]<br />
         [ENTRY_POINT entry]<br />
         [VERSION version]<br />
         [OUTPUT_NAME name]<br />
         [OUTPUT_DIR dir]<br />
        )</p>
<p> This command creates a &lt;target_name&gt;.jar. It compiles the given source files (source) and adds the given resource files (resource) to the jar file. If only resource files are given then just a jar file is created. The list of include jars are added to the classpath when compiling the java sources and also to the dependencies of the target. INCLUDE_JARS also accepts other target names created by add_jar. For backwards compatibility, jar files listed as sources are ignored (as they have been since the first version of this module). </p>
<p> The default OUTPUT_DIR can also be changed by setting the variable CMAKE_JAVA_TARGET_OUTPUT_DIR. </p>
<p> Additional instructions: </p>
<pre>
   To add compile flags to the target you can set these flags with
   the following variable:
</pre>
<pre>
       set(CMAKE_JAVA_COMPILE_FLAGS -nowarn)
</pre>
<pre>
   To add a path or a jar file to the class path you can do this
   with the CMAKE_JAVA_INCLUDE_PATH variable.
</pre>
<pre>
       set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/shibboleet.jar)
</pre>
<pre>
   To use a different output name for the target you can set it with:
</pre>
<pre>
       add_jar(foobar foobar.java OUTPUT_NAME shibboleet.jar)
</pre>
<pre>
   To use a different output directory than CMAKE_CURRENT_BINARY_DIR
   you can set it with:
</pre>
<pre>
       add_jar(foobar foobar.java OUTPUT_DIR ${PROJECT_BINARY_DIR}/bin)
</pre>
<pre>
   To define an entry point in your jar you can set it with the ENTRY_POINT
   named argument:
</pre>
<pre>
       add_jar(example ENTRY_POINT com/examples/MyProject/Main)
</pre>
<pre>
   To add a VERSION to the target output name you can set it using
   the VERSION named argument to add_jar. This will create a jar file with the
   name shibboleet-1.0.0.jar and will create a symlink shibboleet.jar
   pointing to the jar with the version information.
</pre>
<pre>
       add_jar(shibboleet shibbotleet.java VERSION 1.2.0)
</pre>
<pre>
    If the target is a JNI library, utilize the following commands to
    create a JNI symbolic link:
</pre>
<p>set(CMAKE_JNI_TARGET TRUE)<br />
    add_jar(shibboleet shibbotleet.java VERSION 1.2.0)<br />
        install_jar(shibboleet ${LIB_INSTALL_DIR} / shibboleet)<br />
            install_jni_symlink(shibboleet ${JAVA_LIB_INSTALL_DIR})</p>
<pre>
    If a single target needs to produce more than one jar from its
    java source code, to prevent the accumulation of duplicate class
    files in subsequent jars, set/reset CMAKE_JAR_CLASSES_PREFIX prior
    to calling the add_jar() function:
</pre>
<pre>
       set(CMAKE_JAR_CLASSES_PREFIX com/redhat/foo)
       add_jar(foo foo.java)
</pre>
<pre>
       set(CMAKE_JAR_CLASSES_PREFIX com/redhat/bar)
       add_jar(bar bar.java)
</pre>
<p> Target Properties: </p>
<pre>
   The add_jar() functions sets some target properties. You can get these
   properties with the
      get_property(TARGET &lt;target_name&gt; PROPERTY &lt;propery_name&gt;)
   command.
</pre>
<pre>
   INSTALL_FILES      The files which should be installed. This is used by
                      install_jar().
   JNI_SYMLINK        The JNI symlink which should be installed.
                      This is used by install_jni_symlink().
   JAR_FILE           The location of the jar file so that you can include
                      it.
   CLASS_DIR          The directory where the class files can be found. For
                      example to use them with javah.
</pre>
<p> find_jar(&lt;VAR&gt; </p>
<p>          name | NAMES name1 [name2 &#8230;]<br />
          [PATHS path1 [path2 &#8230; ENV var]]<br />
          [VERSIONS version1 [version2]]<br />
          [DOC &#8220;cache documentation string&#8221;]<br />
         )</p>
<p> This command is used to find a full path to the named jar. A cache entry named by &lt;VAR&gt; is created to stor the result of this command. If the full path to a jar is found the result is stored in the variable and the search will not repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again next time find_jar is invoked with the same variable. The name of the full path to a file that is searched for is specified by the names listed after NAMES argument. Additional search locations can be specified after the PATHS argument. If you require special a version of a jar file you can specify it with the VERSIONS argument. The argument after DOC will be used for the documentation string in the cache. </p>
<p> install_jar(TARGET_NAME DESTINATION) </p>
<p> This command installs the TARGET_NAME files to the given DESTINATION. It should be called in the same scope as add_jar() or it will fail. </p>
<p> install_jni_symlink(TARGET_NAME DESTINATION) </p>
<p> This command installs the TARGET_NAME JNI symlinks to the given DESTINATION. It should be called in the same scope as add_jar() or it will fail. </p>
<p> create_javadoc(&lt;VAR&gt; </p>
<p>                PACKAGES pkg1 [pkg2 &#8230;]<br />
                [SOURCEPATH &lt;sourcepath&gt;]<br />
                [CLASSPATH &lt;classpath&gt;]<br />
                [INSTALLPATH &lt;install path&gt;]<br />
                [DOCTITLE &#8220;the documentation title&#8221;]<br />
                [WINDOWTITLE &#8220;the title of the document&#8221;]<br />
                [AUTHOR TRUE|FALSE]<br />
                [USE TRUE|FALSE]<br />
                [VERSION TRUE|FALSE]<br />
               )</p>
<p> Create java documentation based on files or packages. For more details please read the javadoc manpage. </p>
<p> There are two main signatures for create_javadoc. The first signature works with package names on a path with source files: </p>
<p>Example : create_javadoc(my_example_doc<br />
                             PACKAGES com.exmaple.foo com.example.bar<br />
                                 SOURCEPATH &#8220;${CMAKE_CURRENT_SOURCE_DIR}&#8221; CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH} WINDOWTITLE &#8220;My example&#8221; DOCTITLE &#8220;&lt;h1&gt;My example&lt;/h1&gt;&#8221; AUTHOR TRUE<br />
                                     USE TRUE<br />
                                         VERSION TRUE)</p>
<p> The second signature for create_javadoc works on a given list of files. </p>
<p>create_javadoc(&lt;VAR&gt;<br />
                   FILES file1[file2&#8230;]<br />
                              [CLASSPATH&lt;classpath&gt;]<br />
                              [INSTALLPATH&lt;install path&gt;]<br />
                              [DOCTITLE &#8220;the documentation title&#8221;]<br />
                              [WINDOWTITLE &#8220;the title of the document&#8221;]<br />
                              [AUTHOR TRUE | FALSE]<br />
                              [USE TRUE | FALSE]<br />
                              [VERSION TRUE | FALSE])</p>
<p> Example: </p>
<p>create_javadoc(my_example_doc<br />
                   FILES ${example_SRCS} CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH} WINDOWTITLE &#8220;My example&#8221; DOCTITLE &#8220;&lt;h1&gt;My example&lt;/h1&gt;&#8221; AUTHOR TRUE<br />
                       USE TRUE<br />
                           VERSION TRUE)</p>
<p> Both signatures share most of the options. These options are the same as what you can find in the javadoc manpage. Please look at the manpage for CLASSPATH, DOCTITLE, WINDOWTITLE, AUTHOR, USE and VERSION. </p>
<p> The documentation will be by default installed to </p>
<pre>
   ${CMAKE_INSTALL_PREFIX}/share/javadoc/&lt;VAR&gt;
</pre>
<p> if you don&#8217;t set the INSTALLPATH. </p>
<dt><code>UseJavaClassFilelist</code></p>
<dd>
<p> This script create a list of compiled Java class files to be added to a jar file. This avoids including cmake files which get created in the binary directory. </p>
<dt><code>UseJavaSymlinks</code></p>
<dd>
<p> Helper script for UseJava.cmake </p>
<dt><code>UsePkgConfig</code></p>
<dd> Obsolete pkg-config module for CMake, use FindPkgConfig instead. </p>
<p> This module defines the following macro: </p>
<p> PKGCONFIG(package includedir libdir linkflags cflags) </p>
<p> Calling PKGCONFIG will fill the desired information into the 4 given arguments, e.g. PKGCONFIG(libart-2.0 LIBART_INCLUDE_DIR LIBART_LINK_DIR LIBART_LINK_FLAGS LIBART_CFLAGS) if pkg-config was NOT found or the specified software package doesn&#8217;t exist, the variable will be empty when the function returns, otherwise they will contain the respective information </p>
<dt><code>UseQt4</code></p>
<dd> Use Module for QT4 </p>
<p> Sets up C and C++ to use Qt 4. It is assumed that FindQt.cmake has already been loaded. See FindQt.cmake for information on how to load Qt 4 into your CMake project. </p>
<dt><code>UseSWIG</code></p>
<dd> SWIG module for CMake </p>
<p> Defines the following macros: </p>
<p>SWIG_ADD_MODULE(name language[files])<br />
&#8211; Define swig module with given name and specified language<br />
    SWIG_LINK_LIBRARIES(name[libraries]) &#8211;<br />
    Link libraries to swig module</p>
<p> All other macros are for internal use only. To get the actual name of the swig module, use: ${SWIG_MODULE_${name}_REAL_NAME}. Set Source files properties such as CPLUSPLUS and SWIG_FLAGS to specify special behavior of SWIG. Also global CMAKE_SWIG_FLAGS can be used to add special flags to all swig calls. Another special variable is CMAKE_SWIG_OUTDIR, it allows one to specify where to write all the swig generated module (swig -outdir option) The name-specific variable SWIG_MODULE_&lt;name&gt;_EXTRA_DEPS may be used to specify extra dependencies for the generated modules. If the source file generated by swig need some special flag you can use set_source_files_properties( ${swig_generated_file_fullname} </p>
<pre>
        PROPERTIES COMPILE_FLAGS &quot;-bla&quot;)
</pre>
<dt><code>Use_wxWindows</code></p>
<dd> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; </p>
<p> This convenience include finds if wxWindows is installed and set the appropriate libs, incdirs, flags etc. author Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt; (07/2003) USAGE: </p>
<pre>
   just include Use_wxWindows.cmake
   in your projects CMakeLists.txt
</pre>
<p> include( ${CMAKE_MODULE_PATH}/Use_wxWindows.cmake) </p>
<pre>
   if you are sure you need GL then
</pre>
<p> set(WXWINDOWS_USE_GL 1) </p>
<pre>
   *before* you include this file.
</pre>
<dt><code>UsewxWidgets</code></p>
<dd> Convenience include for using wxWidgets library. </p>
<p> Determines if wxWidgets was FOUND and sets the appropriate libs, incdirs, flags, etc. INCLUDE_DIRECTORIES and LINK_DIRECTORIES are called. </p>
<p> USAGE </p>
<pre><code>
#Note that for MinGW users the order of libs is important !
find_package(wxWidgets REQUIRED net gl core base)
    include(${wxWidgets_USE_FILE})
#and for each of your dependent executable / library targets:
        target_link_libraries(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})
</code></pre>
<p> DEPRECATED </p>
<pre>
  LINK_LIBRARIES is not called in favor of adding dependencies per target.
</pre>
<p> AUTHOR </p>
<pre>
  Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt;
</pre>
<dt><code>WriteBasicConfigVersionFile</code></p>
<dd>
<pre>
  WRITE_BASIC_CONFIG_VERSION_FILE( filename VERSION major.minor.patch COMPATIBILITY (AnyNewerVersion|SameMajorVersion) )
</pre>
<p> Deprecated, see WRITE_BASIC_PACKAGE_VERSION_FILE(), it is identical. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2000-2012 Kitware, Inc., Insight Software Consortium. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<p> Neither the names of Kitware, Inc., the Insight Software Consortium, nor the names of their contributors may be used to endorse or promote products derived from this software without specific prior written permission. </p>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
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
<h2>Index</h2>
