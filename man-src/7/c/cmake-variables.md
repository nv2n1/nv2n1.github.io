---
title: "cmake-variables(7)"
name: "cmake-variables"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-variables/"
description: "cmake-variables – CMake Variables Reference"
---

<p>cmake-variables &#8211; CMake Variables Reference </p>
<p> This page documents variables that are provided by CMake or have meaning to CMake when set by project code. </p>
<p> For general information on variables, see the Variables section in the cmake-language manual. </p>
<p> <code>NOTE:</code> CMake reserves identifiers that:</p>
<dl>
<dt>&bull;</p>
<dd>begin with <code>CMAKE_</code> (upper-, lower-, or mixed-case), or</p>
<dt>&bull;</p>
<dd>begin with <code>_CMAKE_</code> (upper-, lower-, or mixed-case), or</p>
<dt>&bull;</p>
<dd>begin with <code>_</code> followed by the name of any <code>CMake Command</code>.</dl>
<h2>Variables That Provide Information</h2>
<h3>Cmake_Ar</h3>
<p>Name of archiving tool for static libraries. </p>
<p> This specifies the name of the program that creates archive or static libraries.</p>
<h3>Cmake_Argc</h3>
<p>Number of command line arguments passed to CMake in script mode. </p>
<p> When run in -P script mode, CMake sets this variable to the number of command line arguments. See also <code>CMAKE_ARGV0</code>, <code>1</code>, <code>2</code> &#8230;</p>
<h3>Cmake_Argv0</h3>
<p>Command line argument passed to CMake in script mode. </p>
<p> When run in -P script mode, CMake sets this variable to the first command line argument. It then also sets <code>CMAKE_ARGV1</code>, <code>CMAKE_ARGV2</code>, &#8230; and so on, up to the number of command line arguments given. See also <code>CMAKE_ARGC</code>.</p>
<h3>Cmake_Binary_Dir</h3>
<p>The path to the top level of the build tree. </p>
<p> This is the full path to the top level of the current CMake build tree. For an in-source build, this would be the same as <code>CMAKE_SOURCE_DIR</code>. </p>
<p> When run in -P script mode, CMake sets the variables <i>CMAKE_BINARY_DIR</i>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Build_Tool</h3>
<p>This variable exists only for backwards compatibility. It contains the same value as <code>CMAKE_MAKE_PROGRAM</code>. Use that variable instead.</p>
<h3>Cmake_Cache_Major_Version</h3>
<p>Major version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the major version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cache_Minor_Version</h3>
<p>Minor version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the minor version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cache_Patch_Version</h3>
<p>Patch version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the patch version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cachefile_Dir</h3>
<p>The directory with the <code>CMakeCache.txt</code> file. </p>
<p> This is the full path to the directory that has the <code>CMakeCache.txt</code> file in it. This is the same as <code>CMAKE_BINARY_DIR</code>.</p>
<h3>Cmake_Cfg_Intdir</h3>
<p>Deprecated since version 3.21: This variable has poor support on <code>Ninja Multi-Config</code>, and predates the existence of the <code>$&lt;CONFIG&gt;</code> generator expression. Use <code>$&lt;CONFIG&gt;</code> instead. </p>
<p> Build-time reference to per-configuration output subdirectory. </p>
<p> For native build systems supporting multiple configurations in the build tree (such as Visual Studio Generators and <code>Xcode</code>), the value is a reference to a build-time variable specifying the name of the per-configuration output subdirectory. On Makefile Generators this evaluates to <i>.</i> because there is only one configuration in a build tree. Example values: </p>
<pre>$(ConfigurationName) = Visual Studio 9
$(Configuration) = Visual Studio 10
$(CONFIGURATION) = Xcode
. = Make-based tools
. = Ninja
${CONFIGURATION} = Ninja Multi-Config</pre>
<p>Since these values are evaluated by the native build system, this variable is suitable only for use in command lines that will be evaluated at build time. Example of intended usage: </p>
<pre>add_executable(mytool mytool.c)
add_custom_command(
 OUTPUT out.txt
 COMMAND ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool
 ${CMAKE_CURRENT_SOURCE_DIR}/in.txt out.txt
 DEPENDS mytool in.txt
 )
add_custom_target(drive ALL DEPENDS out.txt)</pre>
<p>Note that <code>CMAKE_CFG_INTDIR</code> is no longer necessary for this purpose but has been left for compatibility with existing projects. Instead <code>add_custom_command()</code> recognizes executable target names in its <code>COMMAND</code> option, so <code>${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool</code> can be replaced by just <code>mytool</code>. </p>
<p> This variable is read-only. Setting it is undefined behavior. In multi-configuration build systems the value of this variable is passed as the value of preprocessor symbol <code>CMAKE_INTDIR</code> to the compilation of all source files.</p>
<h3>Cmake_Command</h3>
<p>The full path to the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> executable. </p>
<p> This is the full path to the CMake executable <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> which is useful from custom commands that want to use the <code>cmake -E</code> option for portable system commands. (e.g. <code>/usr/local/bin/cmake</code>)</p>
<h3>Cmake_Cpack_Command</h3>
<p>New in version 3.13. </p>
<p> Full path to <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> command installed with CMake. </p>
<p> This is the full path to the CPack executable <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> which is useful from custom commands that want to use the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-E</code> option for portable system commands.</p>
<h3>Cmake_Crosscompiling</h3>
<p>Intended to indicate whether CMake is cross compiling, but note limitations discussed below. </p>
<p> This variable will be set to true by CMake if the <code>CMAKE_SYSTEM_NAME</code> variable has been set manually (i.e. in a toolchain file or as a cache entry from the <code>cmake</code> command line). In most cases, manually setting <code>CMAKE_SYSTEM_NAME</code> will only be done when cross compiling, since it will otherwise be given the same value as <code>CMAKE_HOST_SYSTEM_NAME</code> if not manually set, which is correct for the non-cross-compiling case. In the event that <code>CMAKE_SYSTEM_NAME</code> is manually set to the same value as <code>CMAKE_HOST_SYSTEM_NAME</code>, then <code>CMAKE_CROSSCOMPILING</code> will still be set to true. </p>
<p> Another case to be aware of is that builds targeting Apple platforms other than macOS are handled differently to other cross compiling scenarios. Rather than relying on <code>CMAKE_SYSTEM_NAME</code> to select the target platform, Apple device builds use <code>CMAKE_OSX_SYSROOT</code> to select the appropriate SDK, which indirectly determines the target platform. Furthermore, when using the <code>Xcode</code> generator, developers can switch between device and simulator builds at build time rather than having a single choice at configure time, so the concept of whether the build is cross compiling or not is more complex. Therefore, the use of <code>CMAKE_CROSSCOMPILING</code> is not recommended for projects targeting Apple devices.</p>
<h3>Cmake_Crosscompiling_Emulator</h3>
<p>New in version 3.3. </p>
<p> This variable is only used when <code>CMAKE_CROSSCOMPILING</code> is on. It should point to a command on the host system that can run executable built for the target system. </p>
<p> If this variable contains a semicolon-separated list, then the first value is the command and remaining values are its arguments. </p>
<p> The command will be used to run <code>try_run()</code> generated executables, which avoids manual population of the <code>TryRunResults.cmake</code> file. </p>
<p> It is also used as the default value for the <code>CROSSCOMPILING_EMULATOR</code> target property of executables.</p>
<h3>Cmake_Ctest_Command</h3>
<p>Full path to <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> command installed with CMake. </p>
<p> This is the full path to the CTest executable <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> which is useful from custom commands that want to use the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-E</code> option for portable system commands.</p>
<h3>Cmake_Current_Binary_Dir</h3>
<p>The path to the binary directory currently being processed. </p>
<p> This the full path to the build directory that is currently being processed by cmake. Each directory added by <code>add_subdirectory()</code> will create a binary directory in the build tree, and as it is being processed this variable will be set. For in-source builds this is the current source directory being processed. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <i>CMAKE_CURRENT_BINARY_DIR</i> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Current_Function</h3>
<p>New in version 3.17. </p>
<p> When executing code inside a <code>function()</code>, this variable contains the name of the current function. It can be useful for diagnostic or debug messages. </p>
<p> See also <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.</p>
<h3>Cmake_Current_Function_List_Dir</h3>
<p>New in version 3.17. </p>
<p> When executing code inside a <code>function()</code>, this variable contains the full directory of the listfile that defined the current function. </p>
<p> It is quite common practice in CMake for modules to use some additional files, such as templates to be copied in after substituting CMake variables. In such cases, a function needs to know where to locate those files in a way that doesn&#8217;t depend on where the function is called. Without <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code>, the code to do that would typically use the following pattern: </p>
<pre>set(_THIS_MODULE_BASE_DIR &quot;${CMAKE_CURRENT_LIST_DIR}&quot;)
function(foo)
 configure_file(
 &quot;${_THIS_MODULE_BASE_DIR}/some.template.in&quot;
 some.output
 )
endfunction()</pre>
<p>Using <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> inside the function instead eliminates the need for the extra variable which would otherwise be visible outside the function&#8217;s scope. The above example can be written in the more concise and more robust form: </p>
<pre>function(foo)
 configure_file(
 &quot;${CMAKE_CURRENT_FUNCTION_LIST_DIR}/some.template.in&quot;
 some.output
 )
endfunction()</pre>
<p>See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.</p>
<h3>Cmake_Current_Function_List_File</h3>
<p>New in version 3.17. </p>
<p> When executing code inside a <code>function()</code>, this variable contains the full path to the listfile that defined the current function. </p>
<p> See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.</p>
<h3>Cmake_Current_Function_List_Line</h3>
<p>New in version 3.17. </p>
<p> When executing code inside a <code>function()</code>, this variable contains the line number in the listfile where the current function was defined. </p>
<p> See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code>.</p>
<h3>Cmake_Current_List_Dir</h3>
<p>Full directory of the listfile currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the directory where the listfile which is currently being processed (<code>CMAKE_CURRENT_LIST_FILE</code>) is located. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the directory where this file is located. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the directory of the file invoking the bottom-most entry on the call stack, not the directory of the file containing the macro or function definition. </p>
<p> See also <code>CMAKE_CURRENT_LIST_FILE</code>.</p>
<h3>Cmake_Current_List_File</h3>
<p>Full path to the listfile currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the one currently being processed. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the location of the file. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the file invoking the bottom-most entry on the call stack, not the file containing the macro or function definition. </p>
<p> See also <code>CMAKE_PARENT_LIST_FILE</code>.</p>
<h3>Cmake_Current_List_Line</h3>
<p>The line number of the current file being processed. </p>
<p> This is the line number of the file currently being processed by cmake. </p>
<p> If CMake is currently processing deferred calls scheduled by the <code>cmake_language(DEFER)</code> command, this variable evaluates to <code>DEFERRED</code> instead of a specific line number.</p>
<h3>Cmake_Current_Source_Dir</h3>
<p>The path to the source directory currently being processed. </p>
<p> This the full path to the source directory that is currently being processed by cmake. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <i>CMAKE_CURRENT_SOURCE_DIR</i> to the current working directory.</p>
<h3>Cmake_Debug_Target_Properties</h3>
<p>Enables tracing output for target properties. </p>
<p> This variable can be populated with a list of properties to generate debug output for when evaluating target properties. Currently it can only be used when evaluating:</p>
<dl>
<dt>&bull;</p>
<dd><code>AUTOUIC_OPTIONS</code></p>
<dt>&bull;</p>
<dd><code>COMPILE_DEFINITIONS</code></p>
<dt>&bull;</p>
<dd><code>COMPILE_FEATURES</code></p>
<dt>&bull;</p>
<dd><code>COMPILE_OPTIONS</code></p>
<dt>&bull;</p>
<dd><code>INCLUDE_DIRECTORIES</code></p>
<dt>&bull;</p>
<dd><code>LINK_DIRECTORIES</code></p>
<dt>&bull;</p>
<dd><code>LINK_OPTIONS</code></p>
<dt>&bull;</p>
<dd><code>POSITION_INDEPENDENT_CODE</code></p>
<dt>&bull;</p>
<dd><code>SOURCES</code> </p>
<p> target properties and any other property listed in <code>COMPATIBLE_INTERFACE_STRING</code> and other <code>COMPATIBLE_INTERFACE_</code> properties. It outputs an origin for each entry in the target property. Default is unset.</dl>
<h3>Cmake_Directory_Labels</h3>
<p>New in version 3.10. </p>
<p> Specify labels for the current directory. </p>
<p> This is used to initialize the <code>LABELS</code> directory property.</p>
<h3>Cmake_Dl_Libs</h3>
<p>Name of library containing <code>dlopen</code> and <code>dlclose</code>. </p>
<p> The name of the library that has <code>dlopen</code> and <code>dlclose</code> in it, usually <code>-ldl</code> on most UNIX machines.</p>
<h3>Cmake_Dotnet_Target_Framework</h3>
<p>New in version 3.17. </p>
<p> Default value for <code>DOTNET_TARGET_FRAMEWORK</code> property of targets. </p>
<p> This variable is used to initialize the <code>DOTNET_TARGET_FRAMEWORK</code> property on all targets. See that target property for additional information. </p>
<p> Setting <code>CMAKE_DOTNET_TARGET_FRAMEWORK</code> may be necessary when working with <code>C#</code> and newer .NET framework versions to avoid referencing errors with the <code>ALL_BUILD</code> CMake target. </p>
<p> This variable is only evaluated for Visual Studio Generators VS 2010 and above.</p>
<h3>Cmake_Dotnet_Target_Framework_Version</h3>
<p>New in version 3.12. </p>
<p> Default value for <code>DOTNET_TARGET_FRAMEWORK_VERSION</code> property of targets. </p>
<p> This variable is used to initialize the <code>DOTNET_TARGET_FRAMEWORK_VERSION</code> property on all targets. See that target property for additional information. When set, <code>CMAKE_DOTNET_TARGET_FRAMEWORK</code> takes precednece over this variable. See that variable or the associated target property <code>DOTNET_TARGET_FRAMEWORK</code> for additional information. </p>
<p> Setting <code>CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION</code> may be necessary when working with <code>C#</code> and newer .NET framework versions to avoid referencing errors with the <code>ALL_BUILD</code> CMake target. </p>
<p> This variable is only evaluated for Visual Studio Generators VS 2010 and above.</p>
<h3>Cmake_Edit_Command</h3>
<p>Full path to <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake/">ccmake</a>(1)</code>. Defined only for Makefile Generators when not using an &quot;extra&quot; generator for an IDE. </p>
<p> This is the full path to the CMake executable that can graphically edit the cache. For example, <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake/">ccmake</a>(1)</code>.</p>
<h3>Cmake_Executable_Suffix</h3>
<p>The suffix for executables on this platform. </p>
<p> The suffix to use for the end of an executable filename if any, <code>.exe</code> on Windows. </p>
<p> <code>CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt;</h3>
<p>The suffix to use for the end of an executable filename of <code>&lt;LANG&gt;</code> compiler target architecture, if any. </p>
<p> It overrides <code>CMAKE_EXECUTABLE_SUFFIX</code> for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Extra_Generator</h3>
<p>The extra generator used to build the project. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> When using the Eclipse, CodeBlocks, CodeLite, Kate or Sublime generators, CMake generates Makefiles (<code>CMAKE_GENERATOR</code>) and additionally project files for the respective IDE. This IDE project file generator is stored in <code>CMAKE_EXTRA_GENERATOR</code> (e.g. <code>Eclipse CDT4</code>).</p>
<h3>Cmake_Extra_Shared_Library_Suffixes</h3>
<p>Additional suffixes for shared libraries. </p>
<p> Extensions for shared libraries other than that specified by <code>CMAKE_SHARED_LIBRARY_SUFFIX</code>, if any. CMake uses this to recognize external shared library files during analysis of libraries linked by a target.</p>
<h3>Cmake_Find_Debug_Mode</h3>
<p>New in version 3.17. </p>
<p> Print extra find call information for the following commands to standard error:</p>
<dl>
<dt>&bull;</p>
<dd><code>find_program()</code></p>
<dt>&bull;</p>
<dd><code>find_library()</code></p>
<dt>&bull;</p>
<dd><code>find_file()</code></p>
<dt>&bull;</p>
<dd><code>find_path()</code></p>
<dt>&bull;</p>
<dd><code>find_package()</code> </p>
<p> Output is designed for human consumption and not for parsing. Enabling this variable is equivalent to using <code>cmake</code> <code>&#8211;debug-find</code> with the added ability to enable debugging for a subset of find calls. </p>
<pre>set(CMAKE_FIND_DEBUG_MODE TRUE)
find_program(...)
set(CMAKE_FIND_DEBUG_MODE FALSE)</pre>
<p>Default is unset.</dl>
<h3>Cmake_Find_Package_Name</h3>
<p>New in version 3.1.1. </p>
<p> Defined by the <code>find_package()</code> command while loading a find module to record the caller-specified package name. See command documentation for details.</p>
<h3>Cmake_Find_Package_Sort_Direction</h3>
<p>New in version 3.7. </p>
<p> The sorting direction used by <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code>. It can assume one of the following values:</p>
<dl>
<dt><code>DEC</code></p>
<dd>Default. Ordering is done in descending mode. The highest folder found will be tested first.</p>
<dt><code>ASC</code></p>
<dd>Ordering is done in ascending mode. The lowest folder found will be tested first. </p>
<p> If <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code> is not set or is set to <code>NONE</code> this variable has no effect.</dl>
<h3>Cmake_Find_Package_Sort_Order</h3>
<p>New in version 3.7. </p>
<p> The default order for sorting packages found using <code>find_package()</code>. It can assume one of the following values:</p>
<dl>
<dt><code>NONE</code></p>
<dd>Default. No attempt is done to sort packages. The first valid package found will be selected.</p>
<dt><code>NAME</code></p>
<dd>Sort packages lexicographically before selecting one.</p>
<dt><code>NATURAL</code></p>
<dd>Sort packages using natural order (see <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a>(3)</code> manual), i.e. such that contiguous digits are compared as whole numbers. </p>
<p> Natural sorting can be employed to return the highest version when multiple versions of the same library are found by <code>find_package()</code>. For example suppose that the following libraries have been found:</p>
<dt>&bull;</p>
<dd>libX-1.1.0</p>
<dt>&bull;</p>
<dd>libX-1.2.9</p>
<dt>&bull;</p>
<dd>libX-1.2.10 </p>
<p> By setting <code>NATURAL</code> order we can select the one with the highest version number <code>libX-1.2.10</code>. </p>
<pre>set(CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
find_package(libX CONFIG)</pre>
<p>The sort direction can be controlled using the <code>CMAKE_FIND_PACKAGE_SORT_DIRECTION</code> variable (by default decrescent, e.g. lib-B will be tested before lib-A).</dl>
<h3>Cmake_Generator</h3>
<p>The generator used to build the project. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> The name of the generator that is being used to generate the build files. (e.g. <code>Unix Makefiles</code>, <code>Ninja</code>, etc.) </p>
<p> The value of this variable should never be modified by project code. A generator may be selected via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-G</code> option, interactively in <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code>, or via the <code>CMAKE_GENERATOR</code> environment variable.</p>
<h3>Cmake_Generator_Instance</h3>
<p>New in version 3.11. </p>
<p> Generator-specific instance specification provided by user. </p>
<p> Some CMake generators support selection of an instance of the native build system when multiple instances are available. If the user specifies an instance (e.g. by setting this cache entry or via the <code>CMAKE_GENERATOR_INSTANCE</code> environment variable), or after a default instance is chosen when a build tree is first configured, the value will be available in this variable. </p>
<p> The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_INSTANCE</code> as a cache entry. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p> Instance specification is supported only on specific generators:</p>
<dl>
<dt>&bull;</p>
<dd>For the <code>Visual Studio 15 2017</code> generator (and above) this specifies the absolute path to the VS installation directory of the selected VS instance. </p>
<p> See native build system documentation for allowed instance values.</dl>
<h3>Cmake_Generator_Platform</h3>
<p>New in version 3.1. </p>
<p> Generator-specific target platform specification provided by user. </p>
<p> Some CMake generators support a target platform name to be given to the native build system to choose a compiler toolchain. If the user specifies a platform name (e.g. via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option or via the <code>CMAKE_GENERATOR_PLATFORM</code> environment variable) the value will be available in this variable. </p>
<p> The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_PLATFORM</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p> Platform specification is supported only on specific generators:</p>
<dl>
<dt>&bull;</p>
<dd>For Visual Studio Generators with VS 2005 and above this specifies the target architecture.</p>
<dt>&bull;</p>
<dd>For <code>Green Hills MULTI</code> this specifies the target architecture. </p>
<p> See native build system documentation for allowed platform names.</dl>
<h3>Visual Studio Platform Selection</h3>
<p>On Visual Studio Generators the selected platform name is provided in the <code>CMAKE_VS_PLATFORM_NAME</code> variable.</p>
<h3>Cmake_Generator_Toolset</h3>
<p>Native build system toolset specification provided by user. </p>
<p> Some CMake generators support a toolset specification to tell the native build system how to choose a compiler. If the user specifies a toolset (e.g. via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option or via the <code>CMAKE_GENERATOR_TOOLSET</code> environment variable) the value will be available in this variable. </p>
<p> The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_TOOLSET</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p> Toolset specification is supported only on specific generators:</p>
<dl>
<dt>&bull;</p>
<dd>Visual Studio Generators for VS 2010 and above</p>
<dt>&bull;</p>
<dd>The <code>Xcode</code> generator for Xcode 3.0 and above</p>
<dt>&bull;</p>
<dd>The <code>Green Hills MULTI</code> generator </p>
<p> See native build system documentation for allowed toolset names.</dl>
<h3>Visual Studio Toolset Selection</h3>
<p>The Visual Studio Generators support toolset specification using one of these forms:</p>
<dl>
<dt>&bull;</p>
<dd><code>toolset</code></p>
<dt>&bull;</p>
<dd><code>toolset[,key=value]*</code></p>
<dt>&bull;</p>
<dd><code>key=value[,key=value]*</code> </p>
<p> The <code>toolset</code> specifies the toolset name. The selected toolset name is provided in the <code>CMAKE_VS_PLATFORM_TOOLSET</code> variable. </p>
<p> The <code>key=value</code> pairs form a comma-separated list of options to specify generator-specific details of the toolset selection. Supported pairs are:</p>
<dt><code>cuda=&lt;version&gt;|&lt;path&gt;</code></p>
<dd>Specify the CUDA toolkit version to use or the path to a standalone CUDA toolkit directory. Supported by VS 2010 and above. The version can only be used with the CUDA toolkit VS integration globally installed. See the <code>CMAKE_VS_PLATFORM_TOOLSET_CUDA</code> and <code>CMAKE_VS_PLATFORM_TOOLSET_CUDA_CUSTOM_DIR</code> variables.</p>
<dt><code>host=&lt;arch&gt;</code></p>
<dd>Specify the host tools architecture as <code>x64</code> or <code>x86</code>. Supported by VS 2013 and above. See the <code>CMAKE_VS_PLATFORM_TOOLSET_HOST_ARCHITECTURE</code> variable.</p>
<dt><code>version=&lt;version&gt;</code></p>
<dd>Specify the toolset version to use. Supported by VS 2017 and above with the specified toolset installed. See the <code>CMAKE_VS_PLATFORM_TOOLSET_VERSION</code> variable.</p>
<dt><code>VCTargetsPath=&lt;path&gt;</code></p>
<dd>Specify an alternative <code>VCTargetsPath</code> value for Visual Studio project files. This allows use of VS platform extension configuration files (<code>.props</code> and <code>.targets</code>) that are not installed with VS.</dl>
<h3>Visual Studio Toolset Customization</h3>
<p><code>These are unstable interfaces with no compatibility guarantees</code> because they hook into undocumented internal CMake implementation details. Institutions may use these to internally maintain support for non-public Visual Studio platforms and toolsets, but must accept responsibility to make updates as changes are made to CMake. </p>
<p> Additional <code>key=value</code> pairs are available:</p>
<dl>
<dt><code>customFlagTableDir=&lt;path&gt;</code></p>
<dd>New in version 3.21. </p>
<p> Specify the absolute path to a directory from which to load custom flag tables stored as JSON documents with file names of the form <code>&lt;platform&gt;_&lt;toolset&gt;_&lt;tool&gt;.json</code> or <code>&lt;platform&gt;_&lt;tool&gt;.json</code>, where <code>&lt;platform&gt;</code> is the <code>CMAKE_VS_PLATFORM_NAME</code>, <code>&lt;toolset&gt;</code> is the <code>CMAKE_VS_PLATFORM_TOOLSET</code>, and <code>&lt;tool&gt;</code> is the tool for which the flag table is meant. <code>This naming pattern is an internal CMake implementation detail.</code> The <code>&lt;tool&gt;</code> names are undocumented. The format of the <code>.json</code> flag table files is undocumented.</dl>
<h3>Cmake_Import_Library_Prefix</h3>
<p>The prefix for import libraries that you link to. </p>
<p> The prefix to use for the name of an import library if used on this platform. </p>
<p> <code>CMAKE_IMPORT_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Import_Library_Suffix</h3>
<p>The suffix for import libraries that you link to. </p>
<p> The suffix to use for the end of an import library filename if used on this platform. </p>
<p> <code>CMAKE_IMPORT_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Job_Pool_Compile</h3>
<p>This variable is used to initialize the <code>JOB_POOL_COMPILE</code> property on all the targets. See <code>JOB_POOL_COMPILE</code> for additional information.</p>
<h3>Cmake_Job_Pool_Link</h3>
<p>This variable is used to initialize the <code>JOB_POOL_LINK</code> property on all the targets. See <code>JOB_POOL_LINK</code> for additional information.</p>
<h3>Cmake_Job_Pool_Precompile_Header</h3>
<p>New in version 3.17. </p>
<p> This variable is used to initialize the <code>JOB_POOL_PRECOMPILE_HEADER</code> property on all the targets. See <code>JOB_POOL_PRECOMPILE_HEADER</code> for additional information.</p>
<h3>Cmake_Job_Pools</h3>
<p>New in version 3.11. </p>
<p> If the <code>JOB_POOLS</code> global property is not set, the value of this variable is used in its place. See <code>JOB_POOLS</code> for additional information.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_AR</h3>
<p>New in version 3.9. </p>
<p> A wrapper around <code>ar</code> adding the appropriate <code>&#8211;plugin</code> option for the compiler. </p>
<p> See also <code>CMAKE_AR</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_FRONTEND_VARIANT</h3>
<p>New in version 3.14. </p>
<p> Identification string of the compiler frontend variant. </p>
<p> Some compilers have multiple, different frontends for accepting command line options. (For example <code>Clang</code> originally only had a frontend compatible with the <code>GNU</code> compiler but since its port to Windows (<code>Clang-Cl</code>) it now also supports a frontend compatible with <code>MSVC</code>.) When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> for the compiler whose frontend it resembles. </p>
<p> <code>NOTE:</code> In other words, this variable describes what command line options and language extensions the compiler frontend expects.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_RANLIB</h3>
<p>New in version 3.9. </p>
<p> A wrapper around <code>ranlib</code> adding the appropriate <code>&#8211;plugin</code> option for the compiler. </p>
<p> See also <code>CMAKE_RANLIB</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_LINK_LIBRARY_SUFFIX</h3>
<p>New in version 3.16. </p>
<p> Language-specific suffix for libraries that you link to. </p>
<p> The suffix to use for the end of a library filename, <code>.lib</code> on Windows.</p>
<h3>Cmake_Link_Library_Suffix</h3>
<p>The suffix for libraries that you link to. </p>
<p> The suffix to use for the end of a library filename, <code>.lib</code> on Windows.</p>
<h3>Cmake_Link_Search_End_Static</h3>
<p>New in version 3.4. </p>
<p> End a link line such that static system libraries are used. </p>
<p> Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default CMake adds an option at the end of the library list (if necessary) to set the linker search type back to its starting type. This property switches the final linker search type to <code>-Bstatic</code> regardless of how it started. </p>
<p> This variable is used to initialize the target property <code>LINK_SEARCH_END_STATIC</code> for all targets. If set, its value is also used by the <code>try_compile()</code> command. </p>
<p> See also <code>CMAKE_LINK_SEARCH_START_STATIC</code>.</p>
<h3>Cmake_Link_Search_Start_Static</h3>
<p>New in version 3.4. </p>
<p> Assume the linker looks for static libraries by default. </p>
<p> Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default the linker search type is assumed to be <code>-Bdynamic</code> at the beginning of the library list. This property switches the assumption to <code>-Bstatic</code>. It is intended for use when linking an executable statically (e.g. with the GNU <code>-static</code> option). </p>
<p> This variable is used to initialize the target property <code>LINK_SEARCH_START_STATIC</code> for all targets. If set, its value is also used by the <code>try_compile()</code> command. </p>
<p> See also <code>CMAKE_LINK_SEARCH_END_STATIC</code>.</p>
<h3>Cmake_Major_Version</h3>
<p>First version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Make_Program</h3>
<p>Tool that can launch the native build system. The value may be the full path to an executable or just the tool name if it is expected to be in the <code>PATH</code>. </p>
<p> The tool selected depends on the <code>CMAKE_GENERATOR</code> used to configure the project:</p>
<dl>
<dt>&bull;</p>
<dd>The Makefile Generators set this to <code>make</code>, <code>gmake</code>, or a generator-specific tool (e.g. <code>nmake</code> for <code>NMake Makefiles</code>). </p>
<p> These generators store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user.</p>
<dt>&bull;</p>
<dd>The <code>Ninja</code> generator sets this to <code>ninja</code>. </p>
<p> This generator stores <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user.</p>
<dt>&bull;</p>
<dd>The <code>Xcode</code> generator sets this to <code>xcodebuild</code>. </p>
<p> This generator prefers to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because <code>xcodebuild</code> is easy to find. </p>
<p> For compatibility with versions of CMake prior to 3.2, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value.</p>
<dt>&bull;</p>
<dd>The Visual Studio Generators set this to the full path to <code>MSBuild.exe</code> (VS &gt;= 10), <code>devenv.com</code> (VS 7,8,9), or <code>VCExpress.exe</code> (VS Express 8,9). (See also variables <code>CMAKE_VS_MSBUILD_COMMAND</code> and <code>CMAKE_VS_DEVENV_COMMAND</code>. </p>
<p> These generators prefer to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because the tools are version-specific and can be located using the Windows Registry. It is also necessary because the proper build tool may depend on the project content (e.g. the Intel Fortran plugin to VS 10 and 11 requires <code>devenv.com</code> to build its <code>.vfproj</code> project files even though <code>MSBuild.exe</code> is normally preferred to support the <code>CMAKE_GENERATOR_TOOLSET</code>). </p>
<p> For compatibility with versions of CMake prior to 3.0, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value if possible.</p>
<dt>&bull;</p>
<dd>The <code>Green Hills MULTI</code> generator sets this to the full path to <code>gbuild.exe(Windows)</code> or <code>gbuild(Linux)</code> based upon the toolset being used. </p>
<p> Once the generator has initialized a particular value for this variable, changing the value has undefined behavior. </p>
<p> The <code>CMAKE_MAKE_PROGRAM</code> variable is set for use by project code. The value is also used by the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>&#8211;build</code> and <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> <code>&#8211;build-and-test</code> tools to launch the native build process.</dl>
<h3>Cmake_Match_Count</h3>
<p>New in version 3.2. </p>
<p> The number of matches with the last regular expression. </p>
<p> When a regular expression match is used, CMake fills in <code>CMAKE_MATCH_&lt;n&gt;</code> variables with the match contents. The <code>CMAKE_MATCH_COUNT</code> variable holds the number of match expressions when these are filled.</p>
<h3>CMAKE_MATCH_&lt;n&gt;</h3>
<p>New in version 3.9. </p>
<p> Capture group <code>&lt;n&gt;</code> matched by the last regular expression, for groups 0 through 9. Group 0 is the entire match. Groups 1 through 9 are the subexpressions captured by <code>()</code> syntax. </p>
<p> When a regular expression match is used, CMake fills in <code>CMAKE_MATCH_&lt;n&gt;</code> variables with the match contents. The <code>CMAKE_MATCH_COUNT</code> variable holds the number of match expressions when these are filled.</p>
<h3>Cmake_Minimum_Required_Version</h3>
<p>The <code>&lt;min&gt;</code> version of CMake given to the most recent call to the <code>cmake_minimum_required(VERSION)</code> command in the current variable scope or any parent variable scope.</p>
<h3>Cmake_Minor_Version</h3>
<p>Second version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Netrc</h3>
<p>New in version 3.11. </p>
<p> This variable is used to initialize the <code>NETRC</code> option for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands. See those commands for additional information. </p>
<p> This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>. </p>
<p> The local option takes precedence over this variable.</p>
<h3>Cmake_Netrc_File</h3>
<p>New in version 3.11. </p>
<p> This variable is used to initialize the <code>NETRC_FILE</code> option for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands. See those commands for additional information. </p>
<p> This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>. </p>
<p> The local option takes precedence over this variable.</p>
<h3>Cmake_Parent_List_File</h3>
<p>Full path to the CMake file that included the current one. </p>
<p> While processing a CMake file loaded by <code>include()</code> or <code>find_package()</code> this variable contains the full path to the file including it. The top of the include stack is always the <code>CMakeLists.txt</code> for the current directory. See also <code>CMAKE_CURRENT_LIST_FILE</code>.</p>
<h3>Cmake_Patch_Version</h3>
<p>Third version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Project_Description</h3>
<p>New in version 3.9. </p>
<p> The description of the top level project. </p>
<p> This variable holds the description of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_DESCRIPTION</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre>cmake_minimum_required(VERSION 3.0)
project(First DESCRIPTION &quot;I am First&quot;)
project(Second DESCRIPTION &quot;I am Second&quot;)
add_subdirectory(sub)
project(Third DESCRIPTION &quot;I am Third&quot;)</pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre>project(SubProj DESCRIPTION &quot;I am SubProj&quot;)
message(&quot;CMAKE_PROJECT_DESCRIPTION = ${CMAKE_PROJECT_DESCRIPTION}&quot;)</pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second &#8230;)</code>, so this will print: </p>
<pre>CMAKE_PROJECT_DESCRIPTION = I am Second</pre>
<p>To obtain the description from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_DESCRIPTION</code> variable.</p>
<h3>Cmake_Project_Homepage_Url</h3>
<p>New in version 3.12. </p>
<p> The homepage URL of the top level project. </p>
<p> This variable holds the homepage URL of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_HOMEPAGE_URL</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre>cmake_minimum_required(VERSION 3.0)
project(First HOMEPAGE_URL &quot;<a rel="nofollow" href="http://first.example.com">http://first.example.com</a>&quot;)
project(Second HOMEPAGE_URL &quot;<a rel="nofollow" href="http://second.example.com">http://second.example.com</a>&quot;)
add_subdirectory(sub)
project(Third HOMEPAGE_URL &quot;<a rel="nofollow" href="http://third.example.com">http://third.example.com</a>&quot;)</pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre>project(SubProj HOMEPAGE_URL &quot;<a rel="nofollow" href="http://subproj.example.com">http://subproj.example.com</a>&quot;)
message(&quot;CMAKE_PROJECT_HOMEPAGE_URL = ${CMAKE_PROJECT_HOMEPAGE_URL}&quot;)</pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second &#8230;)</code>, so this will print: </p>
<pre>CMAKE_PROJECT_HOMEPAGE_URL = <a rel="nofollow" href="http://second.example.com">http://second.example.com</a></pre>
<p>To obtain the homepage URL from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_HOMEPAGE_URL</code> variable.</p>
<h3>Cmake_Project_Name</h3>
<p>The name of the top level project. </p>
<p> This variable holds the name of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the name that <code>CMAKE_PROJECT_NAME</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre>cmake_minimum_required(VERSION 3.0)
project(First)
project(Second)
add_subdirectory(sub)
project(Third)</pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre>project(SubProj)
message(&quot;CMAKE_PROJECT_NAME = ${CMAKE_PROJECT_NAME}&quot;)</pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second)</code>, so this will print: </p>
<pre>CMAKE_PROJECT_NAME = Second</pre>
<p>To obtain the name from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_NAME</code> variable.</p>
<h3>Cmake_Project_Version</h3>
<p>New in version 3.12. </p>
<p> The version of the top level project. </p>
<p> This variable holds the version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_VERSION</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre>cmake_minimum_required(VERSION 3.0)
project(First VERSION 1.2.3)
project(Second VERSION 3.4.5)
add_subdirectory(sub)
project(Third VERSION 6.7.8)</pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre>project(SubProj VERSION 1)
message(&quot;CMAKE_PROJECT_VERSION = ${CMAKE_PROJECT_VERSION}&quot;)</pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second &#8230;)</code>, so this will print: </p>
<pre>CMAKE_PROJECT_VERSION = 3.4.5</pre>
<p>To obtain the version from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_VERSION</code> variable.</p>
<h3>Cmake_Project_Version_Major</h3>
<p>New in version 3.12. </p>
<p> The major version of the top level project. </p>
<p> This variable holds the major version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.</p>
<h3>Cmake_Project_Version_Minor</h3>
<p>New in version 3.12. </p>
<p> The minor version of the top level project. </p>
<p> This variable holds the minor version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.</p>
<h3>Cmake_Project_Version_Patch</h3>
<p>New in version 3.12. </p>
<p> The patch version of the top level project. </p>
<p> This variable holds the patch version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.</p>
<h3>Cmake_Project_Version_Tweak</h3>
<p>New in version 3.12. </p>
<p> The tweak version of the top level project. </p>
<p> This variable holds the tweak version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.</p>
<h3>Cmake_Ranlib</h3>
<p>Name of randomizing tool for static libraries. </p>
<p> This specifies name of the program that randomizes libraries on UNIX, not used on Windows, but may be present.</p>
<h3>Cmake_Root</h3>
<p>Install directory for running cmake. </p>
<p> This is the install root for the running CMake and the <code>Modules</code> directory can be found here. This is commonly used in this format: <code>${CMAKE_ROOT}/Modules</code></p>
<h3>Cmake_Rule_Messages</h3>
<p>New in version 3.13. </p>
<p> Specify whether to report a message for each make rule. </p>
<p> If set in the cache it is used to initialize the value of the <code>RULE_MESSAGES</code> property. Users may disable the option in their local build tree to disable granular messages and report only as each target completes in Makefile builds.</p>
<h3>Cmake_Script_Mode_File</h3>
<p>Full path to the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-P</code> script file currently being processed. </p>
<p> When run in <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-P</code> script mode, CMake sets this variable to the full path of the script file. When run to configure a <code>CMakeLists.txt</code> file, this variable is not set.</p>
<h3>Cmake_Shared_Library_Prefix</h3>
<p>The prefix for shared libraries that you link to. </p>
<p> The prefix to use for the name of a shared library, <code>lib</code> on UNIX. </p>
<p> <code>CMAKE_SHARED_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Shared_Library_Suffix</h3>
<p>The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a shared library filename, <code>.dll</code> on Windows. </p>
<p> <code>CMAKE_SHARED_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Shared_Module_Prefix</h3>
<p>The prefix for loadable modules that you link to. </p>
<p> The prefix to use for the name of a loadable module on this platform. </p>
<p> <code>CMAKE_SHARED_MODULE_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Shared_Module_Suffix</h3>
<p>The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a loadable module filename on this platform </p>
<p> <code>CMAKE_SHARED_MODULE_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Sizeof_Void_P</h3>
<p>Size of a <code>void</code> pointer. </p>
<p> This is set to the size of a pointer on the target machine, and is determined by a try compile. If a 64-bit size is found, then the library search path is modified to look for 64-bit libraries first.</p>
<h3>Cmake_Skip_Install_Rules</h3>
<p>Whether to disable generation of installation rules. </p>
<p> If <code>TRUE</code>, CMake will neither generate installation rules nor will it generate <code>cmake_install.cmake</code> files. This variable is <code>FALSE</code> by default.</p>
<h3>Cmake_Skip_Rpath</h3>
<p>If true, do not add run time path information. </p>
<p> If this is set to <code>TRUE</code>, then the rpath information is not added to compiled executables. The default is to add rpath information if the platform supports it. This allows for easy running from the build tree. To omit RPATH in the install step, but not the build step, use <code>CMAKE_SKIP_INSTALL_RPATH</code> instead.</p>
<h3>Cmake_Source_Dir</h3>
<p>The path to the top level of the source tree. </p>
<p> This is the full path to the top level of the current CMake source tree. For an in-source build, this would be the same as <code>CMAKE_BINARY_DIR</code>. </p>
<p> When run in <code>-P</code> script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <i>CMAKE_SOURCE_DIR</i>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Static_Library_Prefix</h3>
<p>The prefix for static libraries that you link to. </p>
<p> The prefix to use for the name of a static library, <code>lib</code> on UNIX. </p>
<p> <code>CMAKE_STATIC_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Static_Library_Suffix</h3>
<p>The suffix for static libraries that you link to. </p>
<p> The suffix to use for the end of a static library filename, <code>.lib</code> on Windows. </p>
<p> <code>CMAKE_STATIC_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_Swift_MODULE_DIRECTORY</h3>
<p>New in version 3.15. </p>
<p> Swift module output directory. </p>
<p> This variable is used to initialize the <code>Swift_MODULE_DIRECTORY</code> property on all the targets. See the target property for additional information.</p>
<h3>CMAKE_Swift_NUM_THREADS</h3>
<p>New in version 3.15.1. </p>
<p> Number of threads for parallel compilation for Swift targets. </p>
<p> This variable controls the number of parallel jobs that the swift driver creates for building targets. If not specified, it will default to the number of logical CPUs on the host.</p>
<h3>Cmake_Toolchain_File</h3>
<p>Path to toolchain file supplied to <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code>. </p>
<p> This variable is specified on the command line when cross-compiling with CMake. It is the path to a file which is read early in the CMake run and which specifies locations for compilers and toolchain utilities, and other target platform and compiler related information. </p>
<p> Relative paths are allowed and are interpreted first as relative to the build directory, and if not found, relative to the source directory. </p>
<p> This is initialized by the <code>CMAKE_TOOLCHAIN_FILE</code> environment variable if it is set when a new build tree is first created.</p>
<h3>Cmake_Tweak_Version</h3>
<p>Defined to <code>0</code> for compatibility with code written for older CMake versions that may have defined higher values. </p>
<p> <code>NOTE:</code> In CMake versions 2.8.2 through 2.8.12, this variable holds the fourth version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Verbose_Makefile</h3>
<p>Enable verbose output from Makefile builds. </p>
<p> This variable is a cache entry initialized (to <code>FALSE</code>) by the <code>project()</code> command. Users may enable the option in their local build tree to get more verbose output from Makefile builds and show each command line as it is launched.</p>
<h3>Cmake_Version</h3>
<p>The CMake version string as three non-negative integer components separated by <code>.</code> and possibly followed by <code>&#8211;</code> and other information. The first two components represent the feature level and the third component represents either a bug-fix level or development date. </p>
<p> Release versions and release candidate versions of CMake use the format: </p>
<pre>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[-rc&lt;n&gt;]</pre>
<p>where the <code>&lt;patch&gt;</code> component is less than <code>20000000</code>. Development versions of CMake use the format: </p>
<pre>&lt;major&gt;.&lt;minor&gt;.&lt;date&gt;[-&lt;id&gt;]</pre>
<p>where the <code>&lt;date&gt;</code> component is of format <code>CCYYMMDD</code> and <code>&lt;id&gt;</code> may contain arbitrary text. This represents development as of a particular date following the <code>&lt;major&gt;.&lt;minor&gt;</code> feature release. </p>
<p> Individual component values are also available in variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_MAJOR_VERSION</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_MINOR_VERSION</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_PATCH_VERSION</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_TWEAK_VERSION</code> </p>
<p> Use the <code>if()</code> command <code>VERSION_LESS</code>, <code>VERSION_GREATER</code>, <code>VERSION_EQUAL</code>, <code>VERSION_LESS_EQUAL</code>, or <code>VERSION_GREATER_EQUAL</code> operators to compare version string values against <code>CMAKE_VERSION</code> using a component-wise test. Version component values may be 10 or larger so do not attempt to compare version strings as floating-point numbers. </p>
<p> <code>NOTE:</code> CMake versions 2.8.2 through 2.8.12 used three components for the feature level. Release versions represented the bug-fix level in a fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[.&lt;tweak&gt;][-rc&lt;n&gt;]</code>. Development versions represented the development date in the fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;.&lt;date&gt;[-&lt;id&gt;]</code>. </p>
<p> CMake versions prior to 2.8.2 used three components for the feature level and had no bug-fix component. Release versions used an even-valued second component, i.e. <code>&lt;major&gt;.&lt;even-minor&gt;.&lt;patch&gt;[-rc&lt;n&gt;]</code>. Development versions used an odd-valued second component with the development date as the third component, i.e. <code>&lt;major&gt;.&lt;odd-minor&gt;.&lt;date&gt;</code>. </p>
<p> The <code>CMAKE_VERSION</code> variable is defined by CMake 2.6.3 and higher. Earlier versions defined only the individual component variables.</dl>
<h3>Cmake_Vs_Devenv_Command</h3>
<p>The generators for <code>Visual Studio 9 2008</code> and above set this variable to the <code>devenv.com</code> command installed with the corresponding Visual Studio version. Note that this variable may be empty on Visual Studio Express editions because they do not provide this tool. </p>
<p> This variable is not defined by other generators even if <code>devenv.com</code> is installed on the computer. </p>
<p> The <code>CMAKE_VS_MSBUILD_COMMAND</code> is also provided for <code>Visual Studio 10 2010</code> and above. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.</p>
<h3>Cmake_Vs_Msbuild_Command</h3>
<p>The generators for <code>Visual Studio 10 2010</code> and above set this variable to the <code>MSBuild.exe</code> command installed with the corresponding Visual Studio version. </p>
<p> This variable is not defined by other generators even if <code>MSBuild.exe</code> is installed on the computer. </p>
<p> The <code>CMAKE_VS_DEVENV_COMMAND</code> is also provided for the non-Express editions of Visual Studio. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.</p>
<h3>CMAKE_VS_NsightTegra_VERSION</h3>
<p>New in version 3.1. </p>
<p> When using a Visual Studio generator with the <code>CMAKE_SYSTEM_NAME</code> variable set to <code>Android</code>, this variable contains the version number of the installed NVIDIA Nsight Tegra Visual Studio Edition.</p>
<h3>Cmake_Vs_Platform_Name</h3>
<p>New in version 3.1. </p>
<p> Visual Studio target platform name used by the current generator. </p>
<p> VS 8 and above allow project files to specify a target platform. CMake provides the name of the chosen platform in this variable. See the <code>CMAKE_GENERATOR_PLATFORM</code> variable for details. </p>
<p> See also the <code>CMAKE_VS_PLATFORM_NAME_DEFAULT</code> variable.</p>
<h3>Cmake_Vs_Platform_Name_Default</h3>
<p>New in version 3.14.3. </p>
<p> Default for the Visual Studio target platform name for the current generator without considering the value of the <code>CMAKE_GENERATOR_PLATFORM</code> variable. For Visual Studio Generators for VS 2017 and below this is always <code>Win32</code>. For VS 2019 and above this is based on the host platform. </p>
<p> See also the <code>CMAKE_VS_PLATFORM_NAME</code> variable.</p>
<h3>Cmake_Vs_Platform_Toolset</h3>
<p>Visual Studio Platform Toolset name. </p>
<p> VS 10 and above use MSBuild under the hood and support multiple compiler toolchains. CMake may specify a toolset explicitly, such as <code>v110</code> for VS 11 or <code>Windows7.1SDK</code> for 64-bit support in VS 10 Express. CMake provides the name of the chosen toolset in this variable. </p>
<p> See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details.</p>
<h3>Cmake_Vs_Platform_Toolset_Cuda</h3>
<p>New in version 3.9. </p>
<p> NVIDIA CUDA Toolkit version whose Visual Studio toolset to use. </p>
<p> The Visual Studio Generators for VS 2010 and above support using a CUDA toolset provided by a CUDA Toolkit. The toolset version number may be specified by a field in <code>CMAKE_GENERATOR_TOOLSET</code> of the form <code>cuda=8.0</code>. Or it is automatically detected if a path to a standalone CUDA directory is specified in the form <code>cuda=C:\path	o
