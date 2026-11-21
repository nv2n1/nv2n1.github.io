---
title: "cmake-variables(7)"
name: "cmake-variables"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-variables/"
description: "cmake-variables – CMake Variables Reference"
---
<p>cmake-variables &#8211; CMake Variables Reference </p>
<p>This page documents variables that are provided by CMake or have meaning to CMake when set by project code. </p>
<p>For general information on variables, see the Variables section in the cmake-language manual. </p>
<p> <code>NOTE:</code> CMake reserves identifiers that: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> begin with <code>CMAKE_</code> (upper-, lower-, or mixed-case), or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> begin with <code>_CMAKE_</code> (upper-, lower-, or mixed-case), or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> begin with <code>_</code> followed by the name of any <code>CMake Command</code>. </p>
 </dd></dl>
<h2>VARIABLES THAT PROVIDE INFORMATION</h2>
<h3>CMAKE_AR</h3>
<p>Name of archiving tool for static libraries. </p>
<p>This specifies the name of the program that creates archive or static libraries.  </p>
<h3>CMAKE_ARGC</h3>
<p>Number of command line arguments passed to CMake in script mode. </p>
<p>When run in -P script mode, CMake sets this variable to the number of command line arguments. See also <code>CMAKE_ARGV0</code>, <code>1</code>, <code>2</code> ...  </p>
<h3>CMAKE_ARGV0</h3>
<p>Command line argument passed to CMake in script mode. </p>
<p>When run in -P script mode, CMake sets this variable to the first command line argument. It then also sets <code>CMAKE_ARGV1</code>, <code>CMAKE_ARGV2</code>, ... and so on, up to the number of command line arguments given. See also <code>CMAKE_ARGC</code>.  </p>
<h3>CMAKE_BINARY_DIR</h3>
<p>The path to the top level of the build tree. </p>
<p>This is the full path to the top level of the current CMake build tree. For an in-source build, this would be the same as <code>CMAKE_SOURCE_DIR</code>. </p>
<p>When run in -P script mode, CMake sets the variables <i>CMAKE_BINARY_DIR</i>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.  </p>
<h3>CMAKE_BUILD_TOOL</h3>
<p>This variable exists only for backwards compatibility. It contains the same value as <code>CMAKE_MAKE_PROGRAM</code>. Use that variable instead.  </p>
<h3>CMAKE_CACHE_MAJOR_VERSION</h3>
<p>Major version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p>This stores the major version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.  </p>
<h3>CMAKE_CACHE_MINOR_VERSION</h3>
<p>Minor version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p>This stores the minor version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.  </p>
<h3>CMAKE_CACHE_PATCH_VERSION</h3>
<p>Patch version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p>This stores the patch version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.  </p>
<h3>CMAKE_CACHEFILE_DIR</h3>
<p>The directory with the <code>CMakeCache.txt</code> file. </p>
<p>This is the full path to the directory that has the <code>CMakeCache.txt</code> file in it. This is the same as <code>CMAKE_BINARY_DIR</code>.  </p>
<h3>CMAKE_CFG_INTDIR</h3>
<p>Deprecated since version 3.21: This variable has poor support on <code>Ninja Multi-Config</code>, and predates the existence of the <code>$&lt;CONFIG&gt;</code> generator expression. Use <code>$&lt;CONFIG&gt;</code> instead. </p>
<p>Build-time reference to per-configuration output subdirectory. </p>
<p>For native build systems supporting multiple configurations in the build tree (such as Visual Studio Generators and <code>Xcode</code>), the value is a reference to a build-time variable specifying the name of the per-configuration output subdirectory. On Makefile Generators this evaluates to <i>.</i> because there is only one configuration in a build tree. Example values: </p>
<pre><code>$(ConfigurationName) = Visual Studio 9
$(Configuration) = Visual Studio 10
$(CONFIGURATION) = Xcode
. = Make-based tools
. = Ninja
${CONFIGURATION} = Ninja Multi-Config
</code></pre>
<p>Since these values are evaluated by the native build system, this variable is suitable only for use in command lines that will be evaluated at build time. Example of intended usage: </p>
<pre><code>add_executable(mytool mytool.c)
add_custom_command(
  OUTPUT out.txt
  COMMAND ${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool
          ${CMAKE_CURRENT_SOURCE_DIR}/in.txt out.txt
  DEPENDS mytool in.txt
  )
add_custom_target(drive ALL DEPENDS out.txt)
</code></pre>
<p>Note that <code>CMAKE_CFG_INTDIR</code> is no longer necessary for this purpose but has been left for compatibility with existing projects. Instead <code>add_custom_command()</code> recognizes executable target names in its <code>COMMAND</code> option, so <code>${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_CFG_INTDIR}/mytool</code> can be replaced by just <code>mytool</code>. </p>
<p>This variable is read-only. Setting it is undefined behavior. In multi-configuration build systems the value of this variable is passed as the value of preprocessor symbol <code>CMAKE_INTDIR</code> to the compilation of all source files.  </p>
<h3>CMAKE_COMMAND</h3>
<p>The full path to the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> executable. </p>
<p>This is the full path to the CMake executable <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> which is useful from custom commands that want to use the <code>cmake -E</code> option for portable system commands. (e.g. <code>/usr/local/bin/cmake</code>)  </p>
<h3>CMAKE_CPACK_COMMAND</h3>
<p>New in version 3.13. </p>
<p>Full path to <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> command installed with CMake. </p>
<p>This is the full path to the CPack executable <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> which is useful from custom commands that want to use the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-E</code> option for portable system commands.  </p>
<h3>CMAKE_CROSSCOMPILING</h3>
<p>Intended to indicate whether CMake is cross compiling, but note limitations discussed below. </p>
<p>This variable will be set to true by CMake if the <code>CMAKE_SYSTEM_NAME</code> variable has been set manually (i.e. in a toolchain file or as a cache entry from the <code>cmake</code> command line). In most cases, manually setting <code>CMAKE_SYSTEM_NAME</code> will only be done when cross compiling, since it will otherwise be given the same value as <code>CMAKE_HOST_SYSTEM_NAME</code> if not manually set, which is correct for the non-cross-compiling case. In the event that <code>CMAKE_SYSTEM_NAME</code> is manually set to the same value as <code>CMAKE_HOST_SYSTEM_NAME</code>, then <code>CMAKE_CROSSCOMPILING</code> will still be set to true. </p>
<p>Another case to be aware of is that builds targeting Apple platforms other than macOS are handled differently to other cross compiling scenarios. Rather than relying on <code>CMAKE_SYSTEM_NAME</code> to select the target platform, Apple device builds use <code>CMAKE_OSX_SYSROOT</code> to select the appropriate SDK, which indirectly determines the target platform. Furthermore, when using the <code>Xcode</code> generator, developers can switch between device and simulator builds at build time rather than having a single choice at configure time, so the concept of whether the build is cross compiling or not is more complex. Therefore, the use of <code>CMAKE_CROSSCOMPILING</code> is not recommended for projects targeting Apple devices.  </p>
<h3>CMAKE_CROSSCOMPILING_EMULATOR</h3>
<p>New in version 3.3. </p>
<p>This variable is only used when <code>CMAKE_CROSSCOMPILING</code> is on. It should point to a command on the host system that can run executable built for the target system. </p>
<p>If this variable contains a semicolon-separated list, then the first value is the command and remaining values are its arguments. </p>
<p>The command will be used to run <code>try_run()</code> generated executables, which avoids manual population of the <code>TryRunResults.cmake</code> file. </p>
<p>It is also used as the default value for the <code>CROSSCOMPILING_EMULATOR</code> target property of executables.  </p>
<h3>CMAKE_CTEST_COMMAND</h3>
<p>Full path to <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> command installed with CMake. </p>
<p>This is the full path to the CTest executable <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> which is useful from custom commands that want to use the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-E</code> option for portable system commands.  </p>
<h3>CMAKE_CURRENT_BINARY_DIR</h3>
<p>The path to the binary directory currently being processed. </p>
<p>This the full path to the build directory that is currently being processed by cmake. Each directory added by <code>add_subdirectory()</code> will create a binary directory in the build tree, and as it is being processed this variable will be set. For in-source builds this is the current source directory being processed. </p>
<p>When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <i>CMAKE_CURRENT_BINARY_DIR</i> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.  </p>
<h3>CMAKE_CURRENT_FUNCTION</h3>
<p>New in version 3.17. </p>
<p>When executing code inside a <code>function()</code>, this variable contains the name of the current function. It can be useful for diagnostic or debug messages. </p>
<p>See also <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.  </p>
<h3>CMAKE_CURRENT_FUNCTION_LIST_DIR</h3>
<p>New in version 3.17. </p>
<p>When executing code inside a <code>function()</code>, this variable contains the full directory of the listfile that defined the current function. </p>
<p>It is quite common practice in CMake for modules to use some additional files, such as templates to be copied in after substituting CMake variables. In such cases, a function needs to know where to locate those files in a way that doesn&#8217;t depend on where the function is called. Without <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code>, the code to do that would typically use the following pattern: </p>
<pre><code>set(_THIS_MODULE_BASE_DIR &quot;${CMAKE_CURRENT_LIST_DIR}&quot;)
function(foo)
  configure_file(
    &quot;${_THIS_MODULE_BASE_DIR}/some.template.in&quot;
    some.output
  )
endfunction()
</code></pre>
<p>Using <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> inside the function instead eliminates the need for the extra variable which would otherwise be visible outside the function&#8217;s scope. The above example can be written in the more concise and more robust form: </p>
<pre><code>function(foo)
  configure_file(
    &quot;${CMAKE_CURRENT_FUNCTION_LIST_DIR}/some.template.in&quot;
    some.output
  )
endfunction()
</code></pre>
<p>See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.  </p>
<h3>CMAKE_CURRENT_FUNCTION_LIST_FILE</h3>
<p>New in version 3.17. </p>
<p>When executing code inside a <code>function()</code>, this variable contains the full path to the listfile that defined the current function. </p>
<p>See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_LINE</code>.  </p>
<h3>CMAKE_CURRENT_FUNCTION_LIST_LINE</h3>
<p>New in version 3.17. </p>
<p>When executing code inside a <code>function()</code>, this variable contains the line number in the listfile where the current function was defined. </p>
<p>See also <code>CMAKE_CURRENT_FUNCTION</code>, <code>CMAKE_CURRENT_FUNCTION_LIST_DIR</code> and <code>CMAKE_CURRENT_FUNCTION_LIST_FILE</code>.  </p>
<h3>CMAKE_CURRENT_LIST_DIR</h3>
<p>Full directory of the listfile currently being processed. </p>
<p>As CMake processes the listfiles in your project this variable will always be set to the directory where the listfile which is currently being processed (<code>CMAKE_CURRENT_LIST_FILE</code>) is located. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the directory where this file is located. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the directory of the file invoking the bottom-most entry on the call stack, not the directory of the file containing the macro or function definition. </p>
<p>See also <code>CMAKE_CURRENT_LIST_FILE</code>.  </p>
<h3>CMAKE_CURRENT_LIST_FILE</h3>
<p>Full path to the listfile currently being processed. </p>
<p>As CMake processes the listfiles in your project this variable will always be set to the one currently being processed. The value has dynamic scope. When CMake starts processing commands in a source file it sets this variable to the location of the file. When CMake finishes processing commands from the file it restores the previous value. Therefore the value of the variable inside a macro or function is the file invoking the bottom-most entry on the call stack, not the file containing the macro or function definition. </p>
<p>See also <code>CMAKE_PARENT_LIST_FILE</code>.  </p>
<h3>CMAKE_CURRENT_LIST_LINE</h3>
<p>The line number of the current file being processed. </p>
<p>This is the line number of the file currently being processed by cmake. </p>
<p>If CMake is currently processing deferred calls scheduled by the <code>cmake_language(DEFER)</code> command, this variable evaluates to <code>DEFERRED</code> instead of a specific line number.  </p>
<h3>CMAKE_CURRENT_SOURCE_DIR</h3>
<p>The path to the source directory currently being processed. </p>
<p>This the full path to the source directory that is currently being processed by cmake. </p>
<p>When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <i>CMAKE_CURRENT_SOURCE_DIR</i> to the current working directory.  </p>
<h3>CMAKE_DEBUG_TARGET_PROPERTIES</h3>
<p>Enables tracing output for target properties. </p>
<p>This variable can be populated with a list of properties to generate debug output for when evaluating target properties. Currently it can only be used when evaluating: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>AUTOUIC_OPTIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>COMPILE_DEFINITIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>COMPILE_FEATURES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>COMPILE_OPTIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>INCLUDE_DIRECTORIES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>LINK_DIRECTORIES</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>LINK_OPTIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POSITION_INDEPENDENT_CODE</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>SOURCES</code> </p>
<p>target properties and any other property listed in <code>COMPATIBLE_INTERFACE_STRING</code> and other <code>COMPATIBLE_INTERFACE_</code> properties. It outputs an origin for each entry in the target property. Default is unset. </p>
 </dd></dl>
<h3>CMAKE_DIRECTORY_LABELS</h3>
<p>New in version 3.10. </p>
<p>Specify labels for the current directory. </p>
<p>This is used to initialize the <code>LABELS</code> directory property.  </p>
<h3>CMAKE_DL_LIBS</h3>
<p>Name of library containing <code>dlopen</code> and <code>dlclose</code>. </p>
<p>The name of the library that has <code>dlopen</code> and <code>dlclose</code> in it, usually <code>-ldl</code> on most UNIX machines.  </p>
<h3>CMAKE_DOTNET_TARGET_FRAMEWORK</h3>
<p>New in version 3.17. </p>
<p>Default value for <code>DOTNET_TARGET_FRAMEWORK</code> property of targets. </p>
<p>This variable is used to initialize the <code>DOTNET_TARGET_FRAMEWORK</code> property on all targets. See that target property for additional information. </p>
<p>Setting <code>CMAKE_DOTNET_TARGET_FRAMEWORK</code> may be necessary when working with <code>C#</code> and newer .NET framework versions to avoid referencing errors with the <code>ALL_BUILD</code> CMake target. </p>
<p>This variable is only evaluated for Visual Studio Generators VS 2010 and above.  </p>
<h3>CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION</h3>
<p>New in version 3.12. </p>
<p>Default value for <code>DOTNET_TARGET_FRAMEWORK_VERSION</code> property of targets. </p>
<p>This variable is used to initialize the <code>DOTNET_TARGET_FRAMEWORK_VERSION</code> property on all targets. See that target property for additional information. When set, <code>CMAKE_DOTNET_TARGET_FRAMEWORK</code> takes precednece over this variable. See that variable or the associated target property <code>DOTNET_TARGET_FRAMEWORK</code> for additional information. </p>
<p>Setting <code>CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION</code> may be necessary when working with <code>C#</code> and newer .NET framework versions to avoid referencing errors with the <code>ALL_BUILD</code> CMake target. </p>
<p>This variable is only evaluated for Visual Studio Generators VS 2010 and above.  </p>
<h3>CMAKE_EDIT_COMMAND</h3>
<p>Full path to <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake/">ccmake</a>(1)</code>. Defined only for Makefile Generators when not using an &quot;extra&quot; generator for an IDE. </p>
<p>This is the full path to the CMake executable that can graphically edit the cache. For example, <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake/">ccmake</a>(1)</code>.  </p>
<h3>CMAKE_EXECUTABLE_SUFFIX</h3>
<p>The suffix for executables on this platform. </p>
<p>The suffix to use for the end of an executable filename if any, <code>.exe</code> on Windows. </p>
<p> <code>CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt;</h3>
<p>The suffix to use for the end of an executable filename of <code>&lt;LANG&gt;</code> compiler target architecture, if any. </p>
<p>It overrides <code>CMAKE_EXECUTABLE_SUFFIX</code> for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_EXTRA_GENERATOR</h3>
<p>The extra generator used to build the project. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>When using the Eclipse, CodeBlocks, CodeLite, Kate or Sublime generators, CMake generates Makefiles (<code>CMAKE_GENERATOR</code>) and additionally project files for the respective IDE. This IDE project file generator is stored in <code>CMAKE_EXTRA_GENERATOR</code> (e.g. <code>Eclipse CDT4</code>).  </p>
<h3>CMAKE_EXTRA_SHARED_LIBRARY_SUFFIXES</h3>
<p>Additional suffixes for shared libraries. </p>
<p>Extensions for shared libraries other than that specified by <code>CMAKE_SHARED_LIBRARY_SUFFIX</code>, if any. CMake uses this to recognize external shared library files during analysis of libraries linked by a target.  </p>
<h3>CMAKE_FIND_DEBUG_MODE</h3>
<p>New in version 3.17. </p>
<p>Print extra find call information for the following commands to standard error: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>Output is designed for human consumption and not for parsing. Enabling this variable is equivalent to using <code>cmake</code> <code>--debug-find</code> with the added ability to enable debugging for a subset of find calls. </p>
<pre><code>set(CMAKE_FIND_DEBUG_MODE TRUE)
find_program(...)
set(CMAKE_FIND_DEBUG_MODE FALSE)
</code></pre>
<p>Default is unset. </p>
 </dd></dl>
<h3>CMAKE_FIND_PACKAGE_NAME</h3>
<p>New in version 3.1.1. </p>
<p>Defined by the <code>find_package()</code> command while loading a find module to record the caller-specified package name. See command documentation for details.  </p>
<h3>CMAKE_FIND_PACKAGE_SORT_DIRECTION</h3>
<p>New in version 3.7. </p>
<p>The sorting direction used by <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code>. It can assume one of the following values: </p>
<dl>
<dt><code>DEC</code></dt>
<dd> <p> Default. Ordering is done in descending mode. The highest folder found will be tested first. </p>
 </dd>
<dt><code>ASC</code></dt>
<dd> <p> Ordering is done in ascending mode. The lowest folder found will be tested first. </p>
<p>If <code>CMAKE_FIND_PACKAGE_SORT_ORDER</code> is not set or is set to <code>NONE</code> this variable has no effect. </p>
 </dd></dl>
<h3>CMAKE_FIND_PACKAGE_SORT_ORDER</h3>
<p>New in version 3.7. </p>
<p>The default order for sorting packages found using <code>find_package()</code>. It can assume one of the following values: </p>
<dl>
<dt><code>NONE</code></dt>
<dd> <p> Default. No attempt is done to sort packages. The first valid package found will be selected. </p>
 </dd>
<dt><code>NAME</code></dt>
<dd> <p> Sort packages lexicographically before selecting one. </p>
 </dd>
<dt><code>NATURAL</code></dt>
<dd> <p> Sort packages using natural order (see <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a>(3)</code> manual), i.e. such that contiguous digits are compared as whole numbers. </p>
<p>Natural sorting can be employed to return the highest version when multiple versions of the same library are found by <code>find_package()</code>. For example suppose that the following libraries have been found: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> libX-1.1.0 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> libX-1.2.9 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> libX-1.2.10 </p>
<p>By setting <code>NATURAL</code> order we can select the one with the highest version number <code>libX-1.2.10</code>. </p>
<pre><code>set(CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
find_package(libX CONFIG)
</code></pre>
<p>The sort direction can be controlled using the <code>CMAKE_FIND_PACKAGE_SORT_DIRECTION</code> variable (by default decrescent, e.g. lib-B will be tested before lib-A). </p>
 </dd></dl>
<h3>CMAKE_GENERATOR</h3>
<p>The generator used to build the project. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>The name of the generator that is being used to generate the build files. (e.g. <code>Unix Makefiles</code>, <code>Ninja</code>, etc.) </p>
<p>The value of this variable should never be modified by project code. A generator may be selected via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-G</code> option, interactively in <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code>, or via the <code>CMAKE_GENERATOR</code> environment variable.  </p>
<h3>CMAKE_GENERATOR_INSTANCE</h3>
<p>New in version 3.11. </p>
<p>Generator-specific instance specification provided by user. </p>
<p>Some CMake generators support selection of an instance of the native build system when multiple instances are available. If the user specifies an instance (e.g. by setting this cache entry or via the <code>CMAKE_GENERATOR_INSTANCE</code> environment variable), or after a default instance is chosen when a build tree is first configured, the value will be available in this variable. </p>
<p>The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_INSTANCE</code> as a cache entry. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p>Instance specification is supported only on specific generators: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For the <code>Visual Studio 15 2017</code> generator (and above) this specifies the absolute path to the VS installation directory of the selected VS instance. </p>
<p>See native build system documentation for allowed instance values. </p>
 </dd></dl>
<h3>CMAKE_GENERATOR_PLATFORM</h3>
<p>New in version 3.1. </p>
<p>Generator-specific target platform specification provided by user. </p>
<p>Some CMake generators support a target platform name to be given to the native build system to choose a compiler toolchain. If the user specifies a platform name (e.g. via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option or via the <code>CMAKE_GENERATOR_PLATFORM</code> environment variable) the value will be available in this variable. </p>
<p>The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_PLATFORM</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p>Platform specification is supported only on specific generators: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For Visual Studio Generators with VS 2005 and above this specifies the target architecture. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For <code>Green Hills MULTI</code> this specifies the target architecture. </p>
<p>See native build system documentation for allowed platform names. </p>
 </dd></dl>
<h3>Visual Studio Platform Selection</h3>
<p>On Visual Studio Generators the selected platform name is provided in the <code>CMAKE_VS_PLATFORM_NAME</code> variable.  </p>
<h3>CMAKE_GENERATOR_TOOLSET</h3>
<p>Native build system toolset specification provided by user. </p>
<p>Some CMake generators support a toolset specification to tell the native build system how to choose a compiler. If the user specifies a toolset (e.g. via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option or via the <code>CMAKE_GENERATOR_TOOLSET</code> environment variable) the value will be available in this variable. </p>
<p>The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_TOOLSET</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior. </p>
<p>Toolset specification is supported only on specific generators: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Visual Studio Generators for VS 2010 and above </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Xcode</code> generator for Xcode 3.0 and above </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Green Hills MULTI</code> generator </p>
<p>See native build system documentation for allowed toolset names. </p>
 </dd></dl>
<h3>Visual Studio Toolset Selection</h3>
<p>The Visual Studio Generators support toolset specification using one of these forms: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>toolset</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>toolset[,key=value]*</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>key=value[,key=value]*</code> </p>
<p>The <code>toolset</code> specifies the toolset name. The selected toolset name is provided in the <code>CMAKE_VS_PLATFORM_TOOLSET</code> variable. </p>
<p>The <code>key=value</code> pairs form a comma-separated list of options to specify generator-specific details of the toolset selection. Supported pairs are: </p>
 </dd>
<dt><code>cuda=&lt;version&gt;|&lt;path&gt;</code></dt>
<dd> <p> Specify the CUDA toolkit version to use or the path to a standalone CUDA toolkit directory. Supported by VS 2010 and above. The version can only be used with the CUDA toolkit VS integration globally installed. See the <code>CMAKE_VS_PLATFORM_TOOLSET_CUDA</code> and <code>CMAKE_VS_PLATFORM_TOOLSET_CUDA_CUSTOM_DIR</code> variables. </p>
 </dd>
<dt><code>host=&lt;arch&gt;</code></dt>
<dd> <p> Specify the host tools architecture as <code>x64</code> or <code>x86</code>. Supported by VS 2013 and above. See the <code>CMAKE_VS_PLATFORM_TOOLSET_HOST_ARCHITECTURE</code> variable. </p>
 </dd>
<dt><code>version=&lt;version&gt;</code></dt>
<dd> <p> Specify the toolset version to use. Supported by VS 2017 and above with the specified toolset installed. See the <code>CMAKE_VS_PLATFORM_TOOLSET_VERSION</code> variable. </p>
 </dd>
<dt><code>VCTargetsPath=&lt;path&gt;</code></dt>
<dd> <p> Specify an alternative <code>VCTargetsPath</code> value for Visual Studio project files. This allows use of VS platform extension configuration files (<code>.props</code> and <code>.targets</code>) that are not installed with VS. </p>
 </dd></dl>
<h3>Visual Studio Toolset Customization</h3>
<p> <code>These are unstable interfaces with no compatibility guarantees</code> because they hook into undocumented internal CMake implementation details. Institutions may use these to internally maintain support for non-public Visual Studio platforms and toolsets, but must accept responsibility to make updates as changes are made to CMake. </p>
<p>Additional <code>key=value</code> pairs are available: </p>
<dl>
<dt><code>customFlagTableDir=&lt;path&gt;</code></dt>
<dd> <p> New in version 3.21. </p>
<p>Specify the absolute path to a directory from which to load custom flag tables stored as JSON documents with file names of the form <code>&lt;platform&gt;_&lt;toolset&gt;_&lt;tool&gt;.json</code> or <code>&lt;platform&gt;_&lt;tool&gt;.json</code>, where <code>&lt;platform&gt;</code> is the <code>CMAKE_VS_PLATFORM_NAME</code>, <code>&lt;toolset&gt;</code> is the <code>CMAKE_VS_PLATFORM_TOOLSET</code>, and <code>&lt;tool&gt;</code> is the tool for which the flag table is meant. <code>This naming pattern is an internal CMake implementation detail.</code> The <code>&lt;tool&gt;</code> names are undocumented. The format of the <code>.json</code> flag table files is undocumented. </p>
 </dd></dl>
<h3>CMAKE_IMPORT_LIBRARY_PREFIX</h3>
<p>The prefix for import libraries that you link to. </p>
<p>The prefix to use for the name of an import library if used on this platform. </p>
<p> <code>CMAKE_IMPORT_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_IMPORT_LIBRARY_SUFFIX</h3>
<p>The suffix for import libraries that you link to. </p>
<p>The suffix to use for the end of an import library filename if used on this platform. </p>
<p> <code>CMAKE_IMPORT_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_JOB_POOL_COMPILE</h3>
<p>This variable is used to initialize the <code>JOB_POOL_COMPILE</code> property on all the targets. See <code>JOB_POOL_COMPILE</code> for additional information.  </p>
<h3>CMAKE_JOB_POOL_LINK</h3>
<p>This variable is used to initialize the <code>JOB_POOL_LINK</code> property on all the targets. See <code>JOB_POOL_LINK</code> for additional information.  </p>
<h3>CMAKE_JOB_POOL_PRECOMPILE_HEADER</h3>
<p>New in version 3.17. </p>
<p>This variable is used to initialize the <code>JOB_POOL_PRECOMPILE_HEADER</code> property on all the targets. See <code>JOB_POOL_PRECOMPILE_HEADER</code> for additional information.  </p>
<h3>CMAKE_JOB_POOLS</h3>
<p>New in version 3.11. </p>
<p>If the <code>JOB_POOLS</code> global property is not set, the value of this variable is used in its place. See <code>JOB_POOLS</code> for additional information.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_AR</h3>
<p>New in version 3.9. </p>
<p>A wrapper around <code>ar</code> adding the appropriate <code>--plugin</code> option for the compiler. </p>
<p>See also <code>CMAKE_AR</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_FRONTEND_VARIANT</h3>
<p>New in version 3.14. </p>
<p>Identification string of the compiler frontend variant. </p>
<p>Some compilers have multiple, different frontends for accepting command line options. (For example <code>Clang</code> originally only had a frontend compatible with the <code>GNU</code> compiler but since its port to Windows (<code>Clang-Cl</code>) it now also supports a frontend compatible with <code>MSVC</code>.) When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> for the compiler whose frontend it resembles. </p>
<p> <code>NOTE:</code> In other words, this variable describes what command line options and language extensions the compiler frontend expects.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_RANLIB</h3>
<p>New in version 3.9. </p>
<p>A wrapper around <code>ranlib</code> adding the appropriate <code>--plugin</code> option for the compiler. </p>
<p>See also <code>CMAKE_RANLIB</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINK_LIBRARY_SUFFIX</h3>
<p>New in version 3.16. </p>
<p>Language-specific suffix for libraries that you link to. </p>
<p>The suffix to use for the end of a library filename, <code>.lib</code> on Windows.  </p>
<h3>CMAKE_LINK_LIBRARY_SUFFIX</h3>
<p>The suffix for libraries that you link to. </p>
<p>The suffix to use for the end of a library filename, <code>.lib</code> on Windows.  </p>
<h3>CMAKE_LINK_SEARCH_END_STATIC</h3>
<p>New in version 3.4. </p>
<p>End a link line such that static system libraries are used. </p>
<p>Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default CMake adds an option at the end of the library list (if necessary) to set the linker search type back to its starting type. This property switches the final linker search type to <code>-Bstatic</code> regardless of how it started. </p>
<p>This variable is used to initialize the target property <code>LINK_SEARCH_END_STATIC</code> for all targets. If set, its value is also used by the <code>try_compile()</code> command. </p>
<p>See also <code>CMAKE_LINK_SEARCH_START_STATIC</code>.  </p>
<h3>CMAKE_LINK_SEARCH_START_STATIC</h3>
<p>New in version 3.4. </p>
<p>Assume the linker looks for static libraries by default. </p>
<p>Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default the linker search type is assumed to be <code>-Bdynamic</code> at the beginning of the library list. This property switches the assumption to <code>-Bstatic</code>. It is intended for use when linking an executable statically (e.g. with the GNU <code>-static</code> option). </p>
<p>This variable is used to initialize the target property <code>LINK_SEARCH_START_STATIC</code> for all targets. If set, its value is also used by the <code>try_compile()</code> command. </p>
<p>See also <code>CMAKE_LINK_SEARCH_END_STATIC</code>.  </p>
<h3>CMAKE_MAJOR_VERSION</h3>
<p>First version number component of the <code>CMAKE_VERSION</code> variable.  </p>
<h3>CMAKE_MAKE_PROGRAM</h3>
<p>Tool that can launch the native build system. The value may be the full path to an executable or just the tool name if it is expected to be in the <code>PATH</code>. </p>
<p>The tool selected depends on the <code>CMAKE_GENERATOR</code> used to configure the project: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The Makefile Generators set this to <code>make</code>, <code>gmake</code>, or a generator-specific tool (e.g. <code>nmake</code> for <code>NMake Makefiles</code>). </p>
<p>These generators store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Ninja</code> generator sets this to <code>ninja</code>. </p>
<p>This generator stores <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Xcode</code> generator sets this to <code>xcodebuild</code>. </p>
<p>This generator prefers to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because <code>xcodebuild</code> is easy to find. </p>
<p>For compatibility with versions of CMake prior to 3.2, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Visual Studio Generators set this to the full path to <code>MSBuild.exe</code> (VS &gt;= 10), <code>devenv.com</code> (VS 7,8,9), or <code>VCExpress.exe</code> (VS Express 8,9). (See also variables <code>CMAKE_VS_MSBUILD_COMMAND</code> and <code>CMAKE_VS_DEVENV_COMMAND</code>. </p>
<p>These generators prefer to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because the tools are version-specific and can be located using the Windows Registry. It is also necessary because the proper build tool may depend on the project content (e.g. the Intel Fortran plugin to VS 10 and 11 requires <code>devenv.com</code> to build its <code>.vfproj</code> project files even though <code>MSBuild.exe</code> is normally preferred to support the <code>CMAKE_GENERATOR_TOOLSET</code>). </p>
<p>For compatibility with versions of CMake prior to 3.0, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value if possible. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Green Hills MULTI</code> generator sets this to the full path to <code>gbuild.exe(Windows)</code> or <code>gbuild(Linux)</code> based upon the toolset being used. </p>
<p>Once the generator has initialized a particular value for this variable, changing the value has undefined behavior. </p>
<p>The <code>CMAKE_MAKE_PROGRAM</code> variable is set for use by project code. The value is also used by the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>--build</code> and <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> <code>--build-and-test</code> tools to launch the native build process. </p>
 </dd></dl>
<h3>CMAKE_MATCH_COUNT</h3>
<p>New in version 3.2. </p>
<p>The number of matches with the last regular expression. </p>
<p>When a regular expression match is used, CMake fills in <code>CMAKE_MATCH_&lt;n&gt;</code> variables with the match contents. The <code>CMAKE_MATCH_COUNT</code> variable holds the number of match expressions when these are filled.  </p>
<h3>CMAKE_MATCH_&lt;n&gt;</h3>
<p>New in version 3.9. </p>
<p>Capture group <code>&lt;n&gt;</code> matched by the last regular expression, for groups 0 through 9. Group 0 is the entire match. Groups 1 through 9 are the subexpressions captured by <code>()</code> syntax. </p>
<p>When a regular expression match is used, CMake fills in <code>CMAKE_MATCH_&lt;n&gt;</code> variables with the match contents. The <code>CMAKE_MATCH_COUNT</code> variable holds the number of match expressions when these are filled.  </p>
<h3>CMAKE_MINIMUM_REQUIRED_VERSION</h3>
<p>The <code>&lt;min&gt;</code> version of CMake given to the most recent call to the <code>cmake_minimum_required(VERSION)</code> command in the current variable scope or any parent variable scope.  </p>
<h3>CMAKE_MINOR_VERSION</h3>
<p>Second version number component of the <code>CMAKE_VERSION</code> variable.  </p>
<h3>CMAKE_NETRC</h3>
<p>New in version 3.11. </p>
<p>This variable is used to initialize the <code>NETRC</code> option for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands. See those commands for additional information. </p>
<p>This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>. </p>
<p>The local option takes precedence over this variable.  </p>
<h3>CMAKE_NETRC_FILE</h3>
<p>New in version 3.11. </p>
<p>This variable is used to initialize the <code>NETRC_FILE</code> option for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands. See those commands for additional information. </p>
<p>This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>. </p>
<p>The local option takes precedence over this variable.  </p>
<h3>CMAKE_PARENT_LIST_FILE</h3>
<p>Full path to the CMake file that included the current one. </p>
<p>While processing a CMake file loaded by <code>include()</code> or <code>find_package()</code> this variable contains the full path to the file including it. The top of the include stack is always the <code>CMakeLists.txt</code> for the current directory. See also <code>CMAKE_CURRENT_LIST_FILE</code>.  </p>
<h3>CMAKE_PATCH_VERSION</h3>
<p>Third version number component of the <code>CMAKE_VERSION</code> variable.  </p>
<h3>CMAKE_PROJECT_DESCRIPTION</h3>
<p>New in version 3.9. </p>
<p>The description of the top level project. </p>
<p>This variable holds the description of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_DESCRIPTION</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre><code>cmake_minimum_required(VERSION 3.0)
project(First DESCRIPTION &quot;I am First&quot;)
project(Second DESCRIPTION &quot;I am Second&quot;)
add_subdirectory(sub)
project(Third DESCRIPTION &quot;I am Third&quot;)
</code></pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre><code>project(SubProj DESCRIPTION &quot;I am SubProj&quot;)
message(&quot;CMAKE_PROJECT_DESCRIPTION = ${CMAKE_PROJECT_DESCRIPTION}&quot;)
</code></pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second ...)</code>, so this will print: </p>
<pre><code>CMAKE_PROJECT_DESCRIPTION = I am Second
</code></pre>
<p>To obtain the description from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_DESCRIPTION</code> variable.  </p>
<h3>CMAKE_PROJECT_HOMEPAGE_URL</h3>
<p>New in version 3.12. </p>
<p>The homepage URL of the top level project. </p>
<p>This variable holds the homepage URL of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_HOMEPAGE_URL</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre><code>cmake_minimum_required(VERSION 3.0)
project(First HOMEPAGE_URL &quot;http://first.example.com&quot;)
project(Second HOMEPAGE_URL &quot;http://second.example.com&quot;)
add_subdirectory(sub)
project(Third HOMEPAGE_URL &quot;http://third.example.com&quot;)
</code></pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre><code>project(SubProj HOMEPAGE_URL &quot;http://subproj.example.com&quot;)
message(&quot;CMAKE_PROJECT_HOMEPAGE_URL = ${CMAKE_PROJECT_HOMEPAGE_URL}&quot;)
</code></pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second ...)</code>, so this will print: </p>
<pre><code>CMAKE_PROJECT_HOMEPAGE_URL =http://second.example.com
</code></pre>
<p>To obtain the homepage URL from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_HOMEPAGE_URL</code> variable.  </p>
<h3>CMAKE_PROJECT_NAME</h3>
<p>The name of the top level project. </p>
<p>This variable holds the name of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the name that <code>CMAKE_PROJECT_NAME</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre><code>cmake_minimum_required(VERSION 3.0)
project(First)
project(Second)
add_subdirectory(sub)
project(Third)
</code></pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre><code>project(SubProj)
message(&quot;CMAKE_PROJECT_NAME = ${CMAKE_PROJECT_NAME}&quot;)
</code></pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second)</code>, so this will print: </p>
<pre><code>CMAKE_PROJECT_NAME = Second
</code></pre>
<p>To obtain the name from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_NAME</code> variable.  </p>
<h3>CMAKE_PROJECT_VERSION</h3>
<p>New in version 3.12. </p>
<p>The version of the top level project. </p>
<p>This variable holds the version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. In the event that the top level CMakeLists.txt contains multiple <code>project()</code> calls, the most recently called one from that top level CMakeLists.txt will determine the value that <code>CMAKE_PROJECT_VERSION</code> contains. For example, consider the following top level CMakeLists.txt: </p>
<pre><code>cmake_minimum_required(VERSION 3.0)
project(First VERSION 1.2.3)
project(Second VERSION 3.4.5)
add_subdirectory(sub)
project(Third VERSION 6.7.8)
</code></pre>
<p>And <code>sub/CMakeLists.txt</code> with the following contents: </p>
<pre><code>project(SubProj VERSION 1)
message(&quot;CMAKE_PROJECT_VERSION = ${CMAKE_PROJECT_VERSION}&quot;)
</code></pre>
<p>The most recently seen <code>project()</code> command from the top level CMakeLists.txt would be <code>project(Second ...)</code>, so this will print: </p>
<pre><code>CMAKE_PROJECT_VERSION = 3.4.5
</code></pre>
<p>To obtain the version from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_VERSION</code> variable.  </p>
<h3>CMAKE_PROJECT_VERSION_MAJOR</h3>
<p>New in version 3.12. </p>
<p>The major version of the top level project. </p>
<p>This variable holds the major version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.  </p>
<h3>CMAKE_PROJECT_VERSION_MINOR</h3>
<p>New in version 3.12. </p>
<p>The minor version of the top level project. </p>
<p>This variable holds the minor version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.  </p>
<h3>CMAKE_PROJECT_VERSION_PATCH</h3>
<p>New in version 3.12. </p>
<p>The patch version of the top level project. </p>
<p>This variable holds the patch version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.  </p>
<h3>CMAKE_PROJECT_VERSION_TWEAK</h3>
<p>New in version 3.12. </p>
<p>The tweak version of the top level project. </p>
<p>This variable holds the tweak version of the project as specified in the top level CMakeLists.txt file by a <code>project()</code> command. Please see <code>CMAKE_PROJECT_VERSION</code> documentation for the behavior when multiple <code>project()</code> commands are used in the sources.  </p>
<h3>CMAKE_RANLIB</h3>
<p>Name of randomizing tool for static libraries. </p>
<p>This specifies name of the program that randomizes libraries on UNIX, not used on Windows, but may be present.  </p>
<h3>CMAKE_ROOT</h3>
<p>Install directory for running cmake. </p>
<p>This is the install root for the running CMake and the <code>Modules</code> directory can be found here. This is commonly used in this format: <code>${CMAKE_ROOT}/Modules</code>  </p>
<h3>CMAKE_RULE_MESSAGES</h3>
<p>New in version 3.13. </p>
<p>Specify whether to report a message for each make rule. </p>
<p>If set in the cache it is used to initialize the value of the <code>RULE_MESSAGES</code> property. Users may disable the option in their local build tree to disable granular messages and report only as each target completes in Makefile builds.  </p>
<h3>CMAKE_SCRIPT_MODE_FILE</h3>
<p>Full path to the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-P</code> script file currently being processed. </p>
<p>When run in <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-P</code> script mode, CMake sets this variable to the full path of the script file. When run to configure a <code>CMakeLists.txt</code> file, this variable is not set.  </p>
<h3>CMAKE_SHARED_LIBRARY_PREFIX</h3>
<p>The prefix for shared libraries that you link to. </p>
<p>The prefix to use for the name of a shared library, <code>lib</code> on UNIX. </p>
<p> <code>CMAKE_SHARED_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_SHARED_LIBRARY_SUFFIX</h3>
<p>The suffix for shared libraries that you link to. </p>
<p>The suffix to use for the end of a shared library filename, <code>.dll</code> on Windows. </p>
<p> <code>CMAKE_SHARED_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_SHARED_MODULE_PREFIX</h3>
<p>The prefix for loadable modules that you link to. </p>
<p>The prefix to use for the name of a loadable module on this platform. </p>
<p> <code>CMAKE_SHARED_MODULE_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_SHARED_MODULE_SUFFIX</h3>
<p>The suffix for shared libraries that you link to. </p>
<p>The suffix to use for the end of a loadable module filename on this platform </p>
<p> <code>CMAKE_SHARED_MODULE_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_SIZEOF_VOID_P</h3>
<p>Size of a <code>void</code> pointer. </p>
<p>This is set to the size of a pointer on the target machine, and is determined by a try compile. If a 64-bit size is found, then the library search path is modified to look for 64-bit libraries first.  </p>
<h3>CMAKE_SKIP_INSTALL_RULES</h3>
<p>Whether to disable generation of installation rules. </p>
<p>If <code>TRUE</code>, CMake will neither generate installation rules nor will it generate <code>cmake_install.cmake</code> files. This variable is <code>FALSE</code> by default.  </p>
<h3>CMAKE_SKIP_RPATH</h3>
<p>If true, do not add run time path information. </p>
<p>If this is set to <code>TRUE</code>, then the rpath information is not added to compiled executables. The default is to add rpath information if the platform supports it. This allows for easy running from the build tree. To omit RPATH in the install step, but not the build step, use <code>CMAKE_SKIP_INSTALL_RPATH</code> instead.  </p>
<h3>CMAKE_SOURCE_DIR</h3>
<p>The path to the top level of the source tree. </p>
<p>This is the full path to the top level of the current CMake source tree. For an in-source build, this would be the same as <code>CMAKE_BINARY_DIR</code>. </p>
<p>When run in <code>-P</code> script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <i>CMAKE_SOURCE_DIR</i>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.  </p>
<h3>CMAKE_STATIC_LIBRARY_PREFIX</h3>
<p>The prefix for static libraries that you link to. </p>
<p>The prefix to use for the name of a static library, <code>lib</code> on UNIX. </p>
<p> <code>CMAKE_STATIC_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_STATIC_LIBRARY_SUFFIX</h3>
<p>The suffix for static libraries that you link to. </p>
<p>The suffix to use for the end of a static library filename, <code>.lib</code> on Windows. </p>
<p> <code>CMAKE_STATIC_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_Swift_MODULE_DIRECTORY</h3>
<p>New in version 3.15. </p>
<p>Swift module output directory. </p>
<p>This variable is used to initialize the <code>Swift_MODULE_DIRECTORY</code> property on all the targets. See the target property for additional information.  </p>
<h3>CMAKE_Swift_NUM_THREADS</h3>
<p>New in version 3.15.1. </p>
<p>Number of threads for parallel compilation for Swift targets. </p>
<p>This variable controls the number of parallel jobs that the swift driver creates for building targets. If not specified, it will default to the number of logical CPUs on the host.  </p>
<h3>CMAKE_TOOLCHAIN_FILE</h3>
<p>Path to toolchain file supplied to <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code>. </p>
<p>This variable is specified on the command line when cross-compiling with CMake. It is the path to a file which is read early in the CMake run and which specifies locations for compilers and toolchain utilities, and other target platform and compiler related information. </p>
<p>Relative paths are allowed and are interpreted first as relative to the build directory, and if not found, relative to the source directory. </p>
<p>This is initialized by the <code>CMAKE_TOOLCHAIN_FILE</code> environment variable if it is set when a new build tree is first created.  </p>
<h3>CMAKE_TWEAK_VERSION</h3>
<p>Defined to <code>0</code> for compatibility with code written for older CMake versions that may have defined higher values. </p>
<p> <code>NOTE:</code> In CMake versions 2.8.2 through 2.8.12, this variable holds the fourth version number component of the <code>CMAKE_VERSION</code> variable.  </p>
<h3>CMAKE_VERBOSE_MAKEFILE</h3>
<p>Enable verbose output from Makefile builds. </p>
<p>This variable is a cache entry initialized (to <code>FALSE</code>) by the <code>project()</code> command. Users may enable the option in their local build tree to get more verbose output from Makefile builds and show each command line as it is launched.  </p>
<h3>CMAKE_VERSION</h3>
<p>The CMake version string as three non-negative integer components separated by <code>.</code> and possibly followed by <code>-</code> and other information. The first two components represent the feature level and the third component represents either a bug-fix level or development date. </p>
<p>Release versions and release candidate versions of CMake use the format: </p>
<pre><code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[-rc&lt;n&gt;]
</code></pre>
<p>where the <code>&lt;patch&gt;</code> component is less than <code>20000000</code>. Development versions of CMake use the format: </p>
<pre><code>&lt;major&gt;.&lt;minor&gt;.&lt;date&gt;[-&lt;id&gt;]
</code></pre>
<p>where the <code>&lt;date&gt;</code> component is of format <code>CCYYMMDD</code> and <code>&lt;id&gt;</code> may contain arbitrary text. This represents development as of a particular date following the <code>&lt;major&gt;.&lt;minor&gt;</code> feature release. </p>
<p>Individual component values are also available in variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_MAJOR_VERSION</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_MINOR_VERSION</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_PATCH_VERSION</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_TWEAK_VERSION</code> </p>
<p>Use the <code>if()</code> command <code>VERSION_LESS</code>, <code>VERSION_GREATER</code>, <code>VERSION_EQUAL</code>, <code>VERSION_LESS_EQUAL</code>, or <code>VERSION_GREATER_EQUAL</code> operators to compare version string values against <code>CMAKE_VERSION</code> using a component-wise test. Version component values may be 10 or larger so do not attempt to compare version strings as floating-point numbers. </p>
<p> <code>NOTE:</code> CMake versions 2.8.2 through 2.8.12 used three components for the feature level. Release versions represented the bug-fix level in a fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[.&lt;tweak&gt;][-rc&lt;n&gt;]</code>. Development versions represented the development date in the fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;.&lt;date&gt;[-&lt;id&gt;]</code>. </p>
<p>CMake versions prior to 2.8.2 used three components for the feature level and had no bug-fix component. Release versions used an even-valued second component, i.e. <code>&lt;major&gt;.&lt;even-minor&gt;.&lt;patch&gt;[-rc&lt;n&gt;]</code>. Development versions used an odd-valued second component with the development date as the third component, i.e. <code>&lt;major&gt;.&lt;odd-minor&gt;.&lt;date&gt;</code>. </p>
<p>The <code>CMAKE_VERSION</code> variable is defined by CMake 2.6.3 and higher. Earlier versions defined only the individual component variables. </p>
 </dd></dl>
<h3>CMAKE_VS_DEVENV_COMMAND</h3>
<p>The generators for <code>Visual Studio 9 2008</code> and above set this variable to the <code>devenv.com</code> command installed with the corresponding Visual Studio version. Note that this variable may be empty on Visual Studio Express editions because they do not provide this tool. </p>
<p>This variable is not defined by other generators even if <code>devenv.com</code> is installed on the computer. </p>
<p>The <code>CMAKE_VS_MSBUILD_COMMAND</code> is also provided for <code>Visual Studio 10 2010</code> and above. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.  </p>
<h3>CMAKE_VS_MSBUILD_COMMAND</h3>
<p>The generators for <code>Visual Studio 10 2010</code> and above set this variable to the <code>MSBuild.exe</code> command installed with the corresponding Visual Studio version. </p>
<p>This variable is not defined by other generators even if <code>MSBuild.exe</code> is installed on the computer. </p>
<p>The <code>CMAKE_VS_DEVENV_COMMAND</code> is also provided for the non-Express editions of Visual Studio. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.  </p>
<h3>CMAKE_VS_NsightTegra_VERSION</h3>
<p>New in version 3.1. </p>
<p>When using a Visual Studio generator with the <code>CMAKE_SYSTEM_NAME</code> variable set to <code>Android</code>, this variable contains the version number of the installed NVIDIA Nsight Tegra Visual Studio Edition.  </p>
<h3>CMAKE_VS_PLATFORM_NAME</h3>
<p>New in version 3.1. </p>
<p>Visual Studio target platform name used by the current generator. </p>
<p>VS 8 and above allow project files to specify a target platform. CMake provides the name of the chosen platform in this variable. See the <code>CMAKE_GENERATOR_PLATFORM</code> variable for details. </p>
<p>See also the <code>CMAKE_VS_PLATFORM_NAME_DEFAULT</code> variable.  </p>
<h3>CMAKE_VS_PLATFORM_NAME_DEFAULT</h3>
<p>New in version 3.14.3. </p>
<p>Default for the Visual Studio target platform name for the current generator without considering the value of the <code>CMAKE_GENERATOR_PLATFORM</code> variable. For Visual Studio Generators for VS 2017 and below this is always <code>Win32</code>. For VS 2019 and above this is based on the host platform. </p>
<p>See also the <code>CMAKE_VS_PLATFORM_NAME</code> variable.  </p>
<h3>CMAKE_VS_PLATFORM_TOOLSET</h3>
<p>Visual Studio Platform Toolset name. </p>
<p>VS 10 and above use MSBuild under the hood and support multiple compiler toolchains. CMake may specify a toolset explicitly, such as <code>v110</code> for VS 11 or <code>Windows7.1SDK</code> for 64-bit support in VS 10 Express. CMake provides the name of the chosen toolset in this variable. </p>
<p>See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details.  </p>
<h3>CMAKE_VS_PLATFORM_TOOLSET_CUDA</h3>
<p>New in version 3.9. </p>
<p>NVIDIA CUDA Toolkit version whose Visual Studio toolset to use. </p>
<p>The Visual Studio Generators for VS 2010 and above support using a CUDA toolset provided by a CUDA Toolkit. The toolset version number may be specified by a field in <code>CMAKE_GENERATOR_TOOLSET</code> of the form <code>cuda=8.0</code>. Or it is automatically detected if a path to a standalone CUDA directory is specified in the form <code>cuda=C:\path\to\cuda</code>. If none is specified CMake will choose a default version. CMake provides the selected CUDA toolset version in this variable. The value may be empty if no CUDA Toolkit with Visual Studio integration is installed.  </p>
<h3>CMAKE_VS_PLATFORM_TOOLSET_CUDA_CUSTOM_DIR</h3>
<p>New in version 3.16. </p>
<p>Path to standalone NVIDIA CUDA Toolkit (eg. extracted from installer). </p>
<p>The Visual Studio Generators for VS 2010 and above support using a standalone (non-installed) NVIDIA CUDA toolkit. The path may be specified by a field in <code>CMAKE_GENERATOR_TOOLSET</code> of the form <code>cuda=C:\path\to\cuda</code>. The given directory must at least contain the nvcc compiler in path <code>.\bin</code> and must provide Visual Studio integration files in path <code>.\extras\visual_studio_integration\ MSBuildExtensions\</code>. One can create a standalone CUDA toolkit directory by either opening a installer with 7zip or copying the files that are extracted by the running installer. The value may be empty if no path to a standalone CUDA Toolkit was specified.  </p>
<h3>CMAKE_VS_PLATFORM_TOOLSET_HOST_ARCHITECTURE</h3>
<p>New in version 3.8. </p>
<p>Visual Studio preferred tool architecture. </p>
<p>The Visual Studio Generators for VS 2013 and above support using either the 32-bit or 64-bit host toolchains by specifying a <code>host=x86</code> or <code>host=x64</code> value in the <code>CMAKE_GENERATOR_TOOLSET</code> option. CMake provides the selected toolchain architecture preference in this variable (<code>x86</code>, <code>x64</code>, or empty).  </p>
<h3>CMAKE_VS_PLATFORM_TOOLSET_VERSION</h3>
<p>New in version 3.12. </p>
<p>Visual Studio Platform Toolset version. </p>
<p>The Visual Studio Generators for VS 2017 and above allow to select minor versions of the same toolset. The toolset version number may be specified by a field in <code>CMAKE_GENERATOR_TOOLSET</code> of the form <code>version=14.11</code>. If none is specified CMake will choose a default toolset. The value may be empty if no minor version was selected and the default is used. </p>
<p>If the value is not empty, it is the version number that MSBuild uses in its <code>Microsoft.VCToolsVersion.*.props</code> file names. </p>
<p>New in version 3.19.7: VS 16.9&#8217;s toolset may also be specified as <code>14.28.16.9</code> because VS 16.10 uses the file name <code>Microsoft.VCToolsVersion.14.28.16.9.props</code>. </p>
<h3>Three-Component MSVC Toolset Versions</h3>
<p>New in version 3.19.7. </p>
<p>The <code>version=</code> field may be given a three-component toolset version such as <code>14.28.29910</code>, and CMake will convert it to the name used by MSBuild <code>Microsoft.VCToolsVersion.*.props</code> files. This is useful to distinguish between VS 16.8&#8217;s <code>14.28.29333</code> toolset and VS 16.9&#8217;s <code>14.28.29910</code> toolset. It also matches <code>vcvarsall</code>&#8216;s <code>-vcvars_ver=</code> behavior.  </p>
<h3>CMAKE_VS_TARGET_FRAMEWORK_VERSION</h3>
<p>New in version 3.22. </p>
<p>Visual Studio target framework version. </p>
<p>In some cases, the Visual Studio Generators may use an explicit value for the MSBuild <code>TargetFrameworkVersion</code> setting in <code>.csproj</code> files. CMake provides the chosen value in this variable. </p>
<p>See the <code>CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION</code> variable and <code>DOTNET_TARGET_FRAMEWORK_VERSION</code> target property to specify custom <code>TargetFrameworkVersion</code> values for project targets. </p>
<p>See also <code>CMAKE_VS_TARGET_FRAMEWORK_IDENTIFIER</code> and <code>CMAKE_VS_TARGET_FRAMEWORK_TARGETS_VERSION</code>.  </p>
<h3>CMAKE_VS_TARGET_FRAMEWORK_IDENTIFIER</h3>
<p>New in version 3.22. </p>
<p>Visual Studio target framework identifier. </p>
<p>In some cases, the Visual Studio Generators may use an explicit value for the MSBuild <code>TargetFrameworkIdentifier</code> setting in <code>.csproj</code> files. CMake provides the chosen value in this variable. </p>
<p>See also <code>CMAKE_VS_TARGET_FRAMEWORK_VERSION</code> and <code>CMAKE_VS_TARGET_FRAMEWORK_TARGETS_VERSION</code>.  </p>
<h3>CMAKE_VS_TARGET_FRAMEWORK_TARGETS_VERSION</h3>
<p>New in version 3.22. </p>
<p>Visual Studio target framework targets version. </p>
<p>In some cases, the Visual Studio Generators may use an explicit value for the MSBuild <code>TargetFrameworkTargetsVersion</code> setting in <code>.csproj</code> files. CMake provides the chosen value in this variable. </p>
<p>See also <code>CMAKE_VS_TARGET_FRAMEWORK_VERSION</code> and <code>CMAKE_VS_TARGET_FRAMEWORK_IDENTIFIER</code>.  </p>
<h3>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</h3>
<p>New in version 3.4. </p>
<p>Visual Studio Windows Target Platform Version. </p>
<p>When targeting Windows 10 and above Visual Studio 2015 and above support specification of a target Windows version to select a corresponding SDK. The <code>CMAKE_SYSTEM_VERSION</code> variable may be set to specify a version. Otherwise CMake computes a default version based on the Windows SDK versions available. The chosen Windows target version number is provided in <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code>. If no Windows 10 SDK is available this value will be empty. </p>
<p>One may set a <code>CMAKE_WINDOWS_KITS_10_DIR</code> <i>environment variable</i> to an absolute path to tell CMake to look for Windows 10 SDKs in a custom location. The specified directory is expected to contain <code>Include/10.0.*</code> directories. </p>
<p>See also <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION_MAXIMUM</code>.  </p>
<h3>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION_MAXIMUM</h3>
<p>New in version 3.19. </p>
<p>Override the Windows 10 SDK Maximum Version for VS 2015 and beyond. </p>
<p>The <i>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION_MAXIMUM</i> variable may be set to a false value (e.g. <code>OFF</code>, <code>FALSE</code>, or <code>0</code>) or the SDK version to use as the maximum (e.g. <code>10.0.14393.0</code>). If unset, the default depends on which version of Visual Studio is targeted by the current generator. </p>
<p>This can be used in conjunction with <code>CMAKE_SYSTEM_VERSION</code>, which CMake uses to select <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code>.  </p>
<h3>CMAKE_XCODE_BUILD_SYSTEM</h3>
<p>New in version 3.19. </p>
<p>Xcode build system selection. </p>
<p>The <code>Xcode</code> generator defines this variable to indicate which variant of the Xcode build system will be used. The value is the version of Xcode in which the corresponding build system first became mature enough for use by CMake. The possible values are: </p>
<dl>
<dt><code>1</code></dt>
<dd> <p> The original Xcode build system. This is the default when using Xcode 11.x or below. </p>
 </dd>
<dt><code>12</code></dt>
<dd> <p> The Xcode &quot;new build system&quot; introduced by Xcode 10. It became mature enough for use by CMake in Xcode 12. This is the default when using Xcode 12.x or above. </p>
<p>The <code>CMAKE_XCODE_BUILD_SYSTEM</code> variable is informational and should not be modified by project code. See the Xcode Build System Selection documentation section to select the Xcode build system. </p>
 </dd></dl>
<h3>CMAKE_XCODE_PLATFORM_TOOLSET</h3>
<p>Xcode compiler selection. </p>
<p> <code>Xcode</code> supports selection of a compiler from one of the installed toolsets. CMake provides the name of the chosen toolset in this variable, if any is explicitly selected (e.g. via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option).  </p>
<h3>&lt;PROJECT-NAME&gt;_BINARY_DIR</h3>
<p>Top level binary directory for the named project. </p>
<p>A variable is created with the name used in the <code>project()</code> command, and is the binary directory for the project. This can be useful when <code>add_subdirectory()</code> is used to connect several projects.  </p>
<h3>&lt;PROJECT-NAME&gt;_DESCRIPTION</h3>
<p>New in version 3.12. </p>
<p>Value given to the <code>DESCRIPTION</code> option of the most recent call to the <code>project()</code> command with project name <code>&lt;PROJECT-NAME&gt;</code>, if any.  </p>
<h3>&lt;PROJECT-NAME&gt;_HOMEPAGE_URL</h3>
<p>New in version 3.12. </p>
<p>Value given to the <code>HOMEPAGE_URL</code> option of the most recent call to the <code>project()</code> command with project name <code>&lt;PROJECT-NAME&gt;</code>, if any.  </p>
<h3>&lt;PROJECT-NAME&gt;_IS_TOP_LEVEL</h3>
<p>New in version 3.21. </p>
<p>A boolean variable indicating whether the named project was called in a top level <code>CMakeLists.txt</code> file. </p>
<p>To obtain the value from the most recent call to <code>project()</code> in the current directory scope or above, see the <code>PROJECT_IS_TOP_LEVEL</code> variable. </p>
<p>The variable value will be true in: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> the top-level directory of the project </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the top-level directory of an external project added by <code>ExternalProject</code> </p>
<p>The variable value will be false in: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a directory added by <code>add_subdirectory()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a directory added by <code>FetchContent</code> </p>
 </dd></dl>
<h3>&lt;PROJECT-NAME&gt;_SOURCE_DIR</h3>
<p>Top level source directory for the named project. </p>
<p>A variable is created with the name used in the <code>project()</code> command, and is the source directory for the project. This can be useful when <code>add_subdirectory()</code> is used to connect several projects.  </p>
<h3>&lt;PROJECT-NAME&gt;_VERSION</h3>
<p>Value given to the <code>VERSION</code> option of the most recent call to the <code>project()</code> command with project name <code>&lt;PROJECT-NAME&gt;</code>, if any. </p>
<p>See also the component-wise version variables <code>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MINOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_PATCH</code>, and <code>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</code>.  </p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</h3>
<p>First version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_MINOR</h3>
<p>Second version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_PATCH</h3>
<p>Third version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</h3>
<p>Fourth version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>PROJECT_BINARY_DIR</h3>
<p>Full path to build directory for project. </p>
<p>This is the binary directory of the most recent <code>project()</code> command.  </p>
<h3>PROJECT_DESCRIPTION</h3>
<p>New in version 3.9. </p>
<p>Short project description given to the project command. </p>
<p>This is the description given to the most recently called <code>project()</code> command in the current directory scope or above. To obtain the description of the top level project, see the <code>CMAKE_PROJECT_DESCRIPTION</code> variable.  </p>
<h3>PROJECT_HOMEPAGE_URL</h3>
<p>New in version 3.12. </p>
<p>The homepage URL of the project. </p>
<p>This is the homepage URL given to the most recently called <code>project()</code> command in the current directory scope or above. To obtain the homepage URL of the top level project, see the <code>CMAKE_PROJECT_HOMEPAGE_URL</code> variable.  </p>
<h3>PROJECT_IS_TOP_LEVEL</h3>
<p>New in version 3.21. </p>
<p>A boolean variable indicating whether the most recently called <code>project()</code> command in the current scope or above was in the top level <code>CMakeLists.txt</code> file. </p>
<p>Some modules should only be included as part of the top level <code>CMakeLists.txt</code> file to not cause unintended side effects in the build tree, and this variable can be used to conditionally execute such code. For example, consider the <code>CTest</code> module, which creates targets and options: </p>
<pre><code>project(MyProject)
...
if(PROJECT_IS_TOP_LEVEL)
  include(CTest)
endif()
</code></pre>
<p>The variable value will be true in: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> the top-level directory of the project </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> the top-level directory of an external project added by <code>ExternalProject</code> </p>
<p>The variable value will be false in: </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a directory added by <code>add_subdirectory()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> a directory added by <code>FetchContent</code> </p>
 </dd></dl>
<h3>PROJECT_NAME</h3>
<p>Name of the project given to the project command. </p>
<p>This is the name given to the most recently called <code>project()</code> command in the current directory scope or above. To obtain the name of the top level project, see the <code>CMAKE_PROJECT_NAME</code> variable.  </p>
<h3>PROJECT_SOURCE_DIR</h3>
<p>This is the source directory of the last call to the <code>project()</code> command made in the current directory scope or one of its parents. Note, it is not affected by calls to <code>project()</code> made within a child directory scope (i.e. from within a call to <code>add_subdirectory()</code> from the current scope).  </p>
<h3>PROJECT_VERSION</h3>
<p>Value given to the <code>VERSION</code> option of the most recent call to the <code>project()</code> command, if any. </p>
<p>See also the component-wise version variables <code>PROJECT_VERSION_MAJOR</code>, <code>PROJECT_VERSION_MINOR</code>, <code>PROJECT_VERSION_PATCH</code>, and <code>PROJECT_VERSION_TWEAK</code>.  </p>
<h3>PROJECT_VERSION_MAJOR</h3>
<p>First version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>PROJECT_VERSION_MINOR</h3>
<p>Second version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>PROJECT_VERSION_PATCH</h3>
<p>Third version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h3>PROJECT_VERSION_TWEAK</h3>
<p>Fourth version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.  </p>
<h2>VARIABLES THAT CHANGE BEHAVIOR</h2>
<h3>BUILD_SHARED_LIBS</h3>
<p>Global flag to cause <code>add_library()</code> to create shared libraries if on. </p>
<p>If present and true, this will cause all libraries to be built shared unless the library was explicitly added as a static library. This variable is often added to projects as an <code>option()</code> so that each user of a project can decide if they want to build the project using shared or static libraries.  </p>
<h3>CMAKE_ABSOLUTE_DESTINATION_FILES</h3>
<p>List of files which have been installed using an <code>ABSOLUTE DESTINATION</code> path. </p>
<p>This variable is defined by CMake-generated <code>cmake_install.cmake</code> scripts. It can be used (read-only) by programs or scripts that source those install scripts. This is used by some CPack generators (e.g. RPM).  </p>
<h3>CMAKE_APPBUNDLE_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for macOS application bundles used by the <code>find_program()</code>, and <code>find_package()</code> commands.  </p>
<h3>CMAKE_AUTOMOC_RELAXED_MODE</h3>
<p>Deprecated since version 3.15. </p>
<p>Switch between strict and relaxed automoc mode. </p>
<p>By default, <code>AUTOMOC</code> behaves exactly as described in the documentation of the <code>AUTOMOC</code> target property. When set to <code>TRUE</code>, it accepts more input and tries to find the correct input file for <code>moc</code> even if it differs from the documented behavior. In this mode it e.g. also checks whether a header file is intended to be processed by moc when a <code>&quot;foo.moc&quot;</code> file has been included. </p>
<p>Relaxed mode has to be enabled for KDE4 compatibility.  </p>
<h3>CMAKE_BACKWARDS_COMPATIBILITY</h3>
<p>Deprecated. See CMake Policy <code>CMP0001</code> documentation.  </p>
<h3>CMAKE_BUILD_TYPE</h3>
<p>Specifies the build type on single-configuration generators (e.g. Makefile Generators or <code>Ninja</code>). Typical values include <code>Debug</code>, <code>Release</code>, <code>RelWithDebInfo</code> and <code>MinSizeRel</code>, but custom build types can also be defined. </p>
<p>This variable is initialized by the first <code>project()</code> or <code>enable_language()</code> command called in a project when a new build tree is first created. If the <code>CMAKE_BUILD_TYPE</code> environment variable is set, its value is used. Otherwise, a toolchain-specific default is chosen when a language is enabled. The default value is often an empty string, but this is usually not desirable and one of the other standard build types is usually more appropriate. </p>
<p>Depending on the situation, the value of this variable may be treated case-sensitively or case-insensitively. See Build Configurations for discussion of this and other related topics. </p>
<p>For multi-config generators, see <code>CMAKE_CONFIGURATION_TYPES</code>.  </p>
<h3>CMAKE_CLANG_VFS_OVERLAY</h3>
<p>New in version 3.19. </p>
<p>When cross compiling for windows with clang-cl, this variable can be an absolute path pointing to a clang virtual file system yaml file, which will enable clang-cl to resolve windows header names on a case sensitive file system.  </p>
<h3>CMAKE_CODEBLOCKS_COMPILER_ID</h3>
<p>New in version 3.11. </p>
<p>Change the compiler id in the generated CodeBlocks project files. </p>
<p>CodeBlocks uses its own compiler id string which differs from <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code>. If this variable is left empty, CMake tries to recognize the CodeBlocks compiler id automatically. Otherwise the specified string is used in the CodeBlocks project file. See the CodeBlocks documentation for valid compiler id strings. </p>
<p>Other IDEs like QtCreator that also use the CodeBlocks generator may ignore this setting.  </p>
<h3>CMAKE_CODEBLOCKS_EXCLUDE_EXTERNAL_FILES</h3>
<p>New in version 3.10. </p>
<p>Change the way the CodeBlocks generator creates project files. </p>
<p>If this variable evaluates to <code>ON</code> the generator excludes from the project file any files that are located outside the project root.  </p>
<h3>CMAKE_CODELITE_USE_TARGETS</h3>
<p>New in version 3.7. </p>
<p>Change the way the CodeLite generator creates projectfiles. </p>
<p>If this variable evaluates to <code>ON</code> at the end of the top-level <code>CMakeLists.txt</code> file, the generator creates projectfiles based on targets rather than projects.  </p>
<h3>CMAKE_COLOR_MAKEFILE</h3>
<p>Enables color output when using the Makefile Generators. </p>
<p>When enabled, the generated Makefiles will produce colored output. Default is <code>ON</code>.  </p>
<h3>CMAKE_CONFIGURATION_TYPES</h3>
<p>Specifies the available build types (configurations) on multi-config generators (e.g. Visual Studio, <code>Xcode</code>, or <code>Ninja Multi-Config</code>). Typical values include <code>Debug</code>, <code>Release</code>, <code>RelWithDebInfo</code> and <code>MinSizeRel</code>, but custom build types can also be defined. </p>
<p>This variable is initialized by the first <code>project()</code> or <code>enable_language()</code> command called in a project when a new build tree is first created. If the <code>CMAKE_CONFIGURATION_TYPES</code> environment variable is set, its value is used. Otherwise, the default value is generator-specific. </p>
<p>Depending on the situation, the values in this variable may be treated case-sensitively or case-insensitively. See Build Configurations for discussion of this and other related topics. </p>
<p>For single-config generators, see <code>CMAKE_BUILD_TYPE</code>.  </p>
<h3>CMAKE_DEPENDS_IN_PROJECT_ONLY</h3>
<p>New in version 3.6. </p>
<p>When set to <code>TRUE</code> in a directory, the build system produced by the Makefile Generators is set up to only consider dependencies on source files that appear either in the source or in the binary directories. Changes to source files outside of these directories will not cause rebuilds. </p>
<p>This should be used carefully in cases where some source files are picked up through external headers during the build.  </p>
<h3>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</h3>
<p>Variable for disabling <code>find_package()</code> calls. </p>
<p>Every non-<code>REQUIRED</code> <code>find_package()</code> call in a project can be disabled by setting the variable <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> to <code>TRUE</code>. This can be used to build a project without an optional package, although that package is installed. </p>
<p>This switch should be used during the initial CMake run. Otherwise if the package has already been found in a previous CMake run, the variables which have been stored in the cache will still be there. In that case it is recommended to remove the cache variables for this package from the cache using the cache editor or <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-U</code> </p>
<p>See also the <code>CMAKE_REQUIRE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable.  </p>
<h3>CMAKE_ECLIPSE_GENERATE_LINKED_RESOURCES</h3>
<p>New in version 3.6. </p>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>The Eclipse project generator generates so-called linked resources e.g. to the subproject root dirs in the source tree or to the source files of targets. This can be disabled by setting this variable to FALSE.  </p>
<h3>CMAKE_ECLIPSE_GENERATE_SOURCE_PROJECT</h3>
<p>New in version 3.6. </p>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>If this variable is set to TRUE, the Eclipse project generator will generate an Eclipse project in <code>CMAKE_SOURCE_DIR</code> . This project can then be used in Eclipse e.g. for the version control functionality. <i>CMAKE_ECLIPSE_GENERATE_SOURCE_PROJECT</i> defaults to FALSE; so nothing is written into the source directory.  </p>
<h3>CMAKE_ECLIPSE_MAKE_ARGUMENTS</h3>
<p>New in version 3.6. </p>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>This variable holds arguments which are used when Eclipse invokes the make tool. By default it is initialized to hold flags to enable parallel builds (using -j typically).  </p>
<h3>CMAKE_ECLIPSE_RESOURCE_ENCODING</h3>
<p>New in version 3.16. </p>
<p>This cache variable tells the <code>Eclipse CDT4</code> project generator to set the resource encoding to the given value in generated project files. If no value is given, no encoding will be set.  </p>
<h3>CMAKE_ECLIPSE_VERSION</h3>
<p>New in version 3.6. </p>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p>When using the Eclipse project generator, CMake tries to find the Eclipse executable and detect the version of it. Depending on the version it finds, some features are enabled or disabled. If CMake doesn&#8217;t find Eclipse, it assumes the oldest supported version, Eclipse Callisto (3.2).  </p>
<h3>CMAKE_ERROR_DEPRECATED</h3>
<p>Whether to issue errors for deprecated functionality. </p>
<p>If <code>TRUE</code>, use of deprecated functionality will issue fatal errors. If this variable is not set, CMake behaves as if it were set to <code>FALSE</code>.  </p>
<h3>CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</h3>
<p>Ask <code>cmake_install.cmake</code> script to error out as soon as a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p>The fatal error is emitted before the installation of the offending file takes place. This variable is used by CMake-generated <code>cmake_install.cmake</code> scripts. If one sets this variable to <code>ON</code> while running the script, it may get fatal error messages from the script.  </p>
<h3>CMAKE_EXECUTE_PROCESS_COMMAND_ECHO</h3>
<p>New in version 3.15. </p>
<p>If this variable is set to <code>STDERR</code>, <code>STDOUT</code> or <code>NONE</code> then commands in <code>execute_process()</code> calls will be printed to either stderr or stdout or not at all.  </p>
<h3>CMAKE_EXPORT_COMPILE_COMMANDS</h3>
<p>New in version 3.5. </p>
<p>Enable/Disable output of compile commands during generation. </p>
<p>If enabled, generates a <code>compile_commands.json</code> file containing the exact compiler calls for all translation units of the project in machine-readable form. The format of the JSON file looks like: </p>
<pre><code>[
  {
    &quot;directory&quot;: &quot;/home/user/development/project&quot;,
    &quot;command&quot;: &quot;/usr/bin/c++ ... -c ../foo/foo.cc&quot;,
    &quot;file&quot;: &quot;../foo/foo.cc&quot;
  },
  ...
  {
    &quot;directory&quot;: &quot;/home/user/development/project&quot;,
    &quot;command&quot;: &quot;/usr/bin/c++ ... -c ../foo/bar.cc&quot;,
    &quot;file&quot;: &quot;../foo/bar.cc&quot;
  }
]
</code></pre>
<p>This is initialized by the <code>CMAKE_EXPORT_COMPILE_COMMANDS</code> environment variable, and initializes the <code>EXPORT_COMPILE_COMMANDS</code> target property for all targets. </p>
<p> <code>NOTE:</code> This option is implemented only by Makefile Generators and the <code>Ninja</code>. It is ignored on other generators. </p>
<p>This option currently does not work well in combination with the <code>UNITY_BUILD</code> target property or the <code>CMAKE_UNITY_BUILD</code> variable.  </p>
<h3>CMAKE_EXPORT_PACKAGE_REGISTRY</h3>
<p>New in version 3.15. </p>
<p>Enables the <code>export(PACKAGE)</code> command when <code>CMP0090</code> is set to <code>NEW</code>. </p>
<p>The <code>export(PACKAGE)</code> command does nothing by default. In some cases it is desirable to write to the user package registry, so the <code>CMAKE_EXPORT_PACKAGE_REGISTRY</code> variable may be set to enable it. </p>
<p>If <code>CMP0090</code> is <i>not</i> set to <code>NEW</code> this variable does nothing, and the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> variable controls the behavior instead. </p>
<p>See also Disabling the Package Registry.  </p>
<h3>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</h3>
<p>New in version 3.1. </p>
<p>Disable the <code>export(PACKAGE)</code> command when <code>CMP0090</code> is not set to <code>NEW</code>. </p>
<p>In some cases, for example for packaging and for system wide installations, it is not desirable to write the user package registry. If the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> variable is enabled, the <code>export(PACKAGE)</code> command will do nothing. </p>
<p>If <code>CMP0090</code> is set to <code>NEW</code> this variable does nothing, and the <code>CMAKE_EXPORT_PACKAGE_REGISTRY</code> variable controls the behavior instead. </p>
<p>See also Disabling the Package Registry.  </p>
<h3>CMAKE_FIND_APPBUNDLE</h3>
<p>New in version 3.4. </p>
<p>This variable affects how <code>find_*</code> commands choose between macOS Application Bundles and unix-style package components. </p>
<p>On Darwin or systems supporting macOS Application Bundles, the <code>CMAKE_FIND_APPBUNDLE</code> variable can be set to empty or one of the following: </p>
<dl>
<dt><code>FIRST</code></dt>
<dd> <p> Try to find application bundles before standard programs. This is the default on Darwin. </p>
 </dd>
<dt><code>LAST</code></dt>
<dd> <p> Try to find application bundles after standard programs. </p>
 </dd>
<dt><code>ONLY</code></dt>
<dd> <p> Only try to find application bundles. </p>
 </dd>
<dt><code>NEVER</code></dt>
<dd> <p> Never try to find application bundles. </p>
 </dd></dl>
<h3>CMAKE_FIND_FRAMEWORK</h3>
<p>New in version 3.4. </p>
<p>This variable affects how <code>find_*</code> commands choose between macOS Frameworks and unix-style package components. </p>
<p>On Darwin or systems supporting macOS Frameworks, the <code>CMAKE_FIND_FRAMEWORK</code> variable can be set to empty or one of the following: </p>
<dl>
<dt><code>FIRST</code></dt>
<dd> <p> Try to find frameworks before standard libraries or headers. This is the default on Darwin. </p>
 </dd>
<dt><code>LAST</code></dt>
<dd> <p> Try to find frameworks after standard libraries or headers. </p>
 </dd>
<dt><code>ONLY</code></dt>
<dd> <p> Only try to find frameworks. </p>
 </dd>
<dt><code>NEVER</code></dt>
<dd> <p> Never try to find frameworks. </p>
 </dd></dl>
<h3>CMAKE_FIND_LIBRARY_CUSTOM_LIB_SUFFIX</h3>
<p>New in version 3.9. </p>
<p>Specify a <code>&lt;suffix&gt;</code> to tell the <code>find_library()</code> command to search in a <code>lib&lt;suffix&gt;</code> directory before each <code>lib</code> directory that would normally be searched. </p>
<p>This overrides the behavior of related global properties: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>FIND_LIBRARY_USE_LIB32_PATHS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>FIND_LIBRARY_USE_LIB64_PATHS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>FIND_LIBRARY_USE_LIBX32_PATHS</code> </p>
 </dd></dl>
<h3>CMAKE_FIND_LIBRARY_PREFIXES</h3>
<p>Prefixes to prepend when looking for libraries. </p>
<p>This specifies what prefixes to add to library names when the <code>find_library()</code> command looks for libraries. On UNIX systems this is typically <code>lib</code>, meaning that when trying to find the <code>foo</code> library it will look for <code>libfoo</code>.  </p>
<h3>CMAKE_FIND_LIBRARY_SUFFIXES</h3>
<p>Suffixes to append when looking for libraries. </p>
<p>This specifies what suffixes to add to library names when the <code>find_library()</code> command looks for libraries. On Windows systems this is typically <code>.lib</code> and, depending on the compiler, <code>.dll.a</code>, <code>.a</code> (e.g. GCC and Clang), so when it tries to find the <code>foo</code> library, it will look for <code>[&lt;prefix&gt;]foo.lib</code> and/or <code>[&lt;prefix&gt;]foo[.dll].a</code>, depending on the compiler used and the <code>&lt;prefix&gt;</code> specified in the <code>CMAKE_FIND_LIBRARY_PREFIXES</code>.  </p>
<h3>CMAKE_FIND_NO_INSTALL_PREFIX</h3>
<p>Exclude the values of the <code>CMAKE_INSTALL_PREFIX</code> and <code>CMAKE_STAGING_PREFIX</code> variables from <code>CMAKE_SYSTEM_PREFIX_PATH</code>. CMake adds these project-destination prefixes to <code>CMAKE_SYSTEM_PREFIX_PATH</code> by default in order to support building a series of dependent packages and installing them into a common prefix. Set <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> to <code>TRUE</code> to suppress this behavior. </p>
<p>The <code>CMAKE_SYSTEM_PREFIX_PATH</code> is initialized on the first call to a <code>project()</code> or <code>enable_language()</code> command. Therefore one must set <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> before this in order to take effect. A user may set the variable as a cache entry on the command line to achieve this. </p>
<p>Note that the prefix(es) may still be searched for other reasons, such as being the same prefix as the CMake installation, or for being a built-in system prefix.  </p>
<h3>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</h3>
<p>New in version 3.1. </p>
<p>Deprecated since version 3.16: Use the <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code> variable instead. </p>
<p>By default this variable is not set. If neither <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code> nor <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> is set, then <code>find_package()</code> will use the User Package Registry unless the <code>NO_CMAKE_PACKAGE_REGISTRY</code> option is provided. </p>
<p> <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> is ignored if <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code> is set. </p>
<p>In some cases, for example to locate only system wide installations, it is not desirable to use the User Package Registry when searching for packages. If the <i>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</i> variable is <code>TRUE</code>, all the <code>find_package()</code> commands will skip the User Package Registry as if they were called with the <code>NO_CMAKE_PACKAGE_REGISTRY</code> argument. </p>
<p>See also Disabling the Package Registry.  </p>
<h3>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</h3>
<p>New in version 3.1. </p>
<p>Deprecated since version 3.16: Use the <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> variable instead. </p>
<p>By default this variable is not set. If neither <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> nor <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> is set, then <code>find_package()</code> will use the System Package Registry unless the <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> option is provided. </p>
<p> <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> is ignored if <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> is set. </p>
<p>In some cases, it is not desirable to use the System Package Registry when searching for packages. If the <i>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</i> variable is <code>TRUE</code>, all the <code>find_package()</code> commands will skip the System Package Registry as if they were called with the <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> argument. </p>
<p>See also Disabling the Package Registry.  </p>
<h3>CMAKE_FIND_PACKAGE_PREFER_CONFIG</h3>
<p>New in version 3.15. </p>
<p>Tell <code>find_package()</code> to try &quot;Config&quot; mode before &quot;Module&quot; mode if no mode was specified. </p>
<p>The command <code>find_package()</code> operates without an explicit mode when the reduced signature is used without the <code>MODULE</code> option. In this case, by default, CMake first tries Module mode by searching for a <code>Find&lt;pkg&gt;.cmake</code> module. If it fails, CMake then searches for the package using Config mode. </p>
<p>Set <code>CMAKE_FIND_PACKAGE_PREFER_CONFIG</code> to <code>TRUE</code> to tell <code>find_package()</code> to first search using Config mode before falling back to Module mode. </p>
<p>This variable may be useful when a developer has compiled a custom version of a common library and wishes to link it to a dependent project. If this variable is set to <code>TRUE</code>, it would prevent a dependent project&#8217;s call to <code>find_package()</code> from selecting the default library located by the system&#8217;s <code>Find&lt;pkg&gt;.cmake</code> module before finding the developer&#8217;s custom built library. </p>
<p>Once this variable is set, it is the responsibility of the exported <code>&lt;pkg&gt;Config.cmake</code> files to provide the same result variables as the <code>Find&lt;pkg&gt;.cmake</code> modules so that dependent projects can use them interchangeably.  </p>
<h3>CMAKE_FIND_PACKAGE_RESOLVE_SYMLINKS</h3>
<p>New in version 3.14. </p>
<p>Set to <code>TRUE</code> to tell <code>find_package()</code> calls to resolve symbolic links in the value of <code>&lt;PackageName&gt;_DIR</code>. </p>
<p>This is helpful in use cases where the package search path points at a proxy directory in which symlinks to the real package locations appear. This is not enabled by default because there are also common use cases in which the symlinks should be preserved.  </p>
<h3>CMAKE_FIND_PACKAGE_WARN_NO_MODULE</h3>
<p>Tell <code>find_package()</code> to warn if called without an explicit mode. </p>
<p>If <code>find_package()</code> is called without an explicit mode option (<code>MODULE</code>, <code>CONFIG</code>, or <code>NO_MODULE</code>) and no <code>Find&lt;pkg&gt;.cmake</code> module is in <code>CMAKE_MODULE_PATH</code> then CMake implicitly assumes that the caller intends to search for a package configuration file. If no package configuration file is found then the wording of the failure message must account for both the case that the package is really missing and the case that the project has a bug and failed to provide the intended Find module. If instead the caller specifies an explicit mode option then the failure message can be more specific. </p>
<p>Set <code>CMAKE_FIND_PACKAGE_WARN_NO_MODULE</code> to <code>TRUE</code> to tell <code>find_package()</code> to warn when it implicitly assumes Config mode. This helps developers enforce use of an explicit mode in all calls to <code>find_package()</code> within a project. </p>
<p>This variable has no effect if <code>CMAKE_FIND_PACKAGE_PREFER_CONFIG</code> is set to <code>TRUE</code>.  </p>
<h3>CMAKE_FIND_ROOT_PATH</h3>
<p>Semicolon-separated list of root paths to search on the filesystem. </p>
<p>This variable is most useful when cross-compiling. CMake uses the paths in this list as alternative roots to find filesystem items with <code>find_package()</code>, <code>find_library()</code> etc.  </p>
<h3>CMAKE_FIND_ROOT_PATH_MODE_INCLUDE</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_file()</code> and <code>find_path()</code>. </p>
<p>If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.  </p>
<h3>CMAKE_FIND_ROOT_PATH_MODE_LIBRARY</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_library()</code>. </p>
<p>If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.  </p>
<h3>CMAKE_FIND_ROOT_PATH_MODE_PACKAGE</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_package()</code>. </p>
<p>If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.  </p>
<h3>CMAKE_FIND_ROOT_PATH_MODE_PROGRAM</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_program()</code>. </p>
<p>If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.  </p>
<h3>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the following commands for whether or not to search paths provided by cmake-specific environment variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>This is useful in cross-compiling environments. </p>
<p>By default this variable is not set, which is equivalent to it having a value of <code>TRUE</code>. Explicit options given to the above commands take precedence over this variable. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code>, <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> variables. </p>
 </dd></dl>
<h3>CMAKE_FIND_USE_CMAKE_PATH</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the following commands for whether or not to search paths provided by cmake-specific cache variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>This is useful in cross-compiling environments. </p>
<p>By default this variable is not set, which is equivalent to it having a value of <code>TRUE</code>. Explicit options given to the above commands take precedence over this variable. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code>, <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> variables. </p>
 </dd></dl>
<h3>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the following commands for whether or not to search paths provided by platform-specific cmake variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>This is useful in cross-compiling environments. </p>
<p>By default this variable is not set, which is equivalent to it having a value of <code>TRUE</code>. Explicit options given to the above commands take precedence over this variable. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code>, <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> variables. </p>
 </dd></dl>
<h3>CMAKE_FIND_USE_PACKAGE_REGISTRY</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the <code>find_package()</code> command for whether or not to search paths provided by the User Package Registry. </p>
<p>By default this variable is not set and the behavior will fall back to that determined by the deprecated <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> variable. If that is also not set, then <code>find_package()</code> will use the User Package Registry unless the <code>NO_CMAKE_PACKAGE_REGISTRY</code> option is provided. </p>
<p>This variable takes precedence over <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> when both are set. </p>
<p>In some cases, for example to locate only system wide installations, it is not desirable to use the User Package Registry when searching for packages. If the <i>CMAKE_FIND_USE_PACKAGE_REGISTRY</i> variable is <code>FALSE</code>, all the <code>find_package()</code> commands will skip the User Package Registry as if they were called with the <code>NO_CMAKE_PACKAGE_REGISTRY</code> argument. </p>
<p>See also Disabling the Package Registry and the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> variables.  </p>
<h3>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the following commands for whether or not to search paths provided by <code>&lt;PackageName&gt;_ROOT</code> variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>By default this variable is not set, which is equivalent to it having a value of <code>TRUE</code>. Explicit options given to the above commands take precedence over this variable. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code> variables. </p>
 </dd></dl>
<h3>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</h3>
<p>New in version 3.16. </p>
<p>Controls the default behavior of the following commands for whether or not to search paths provided by standard system environment variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>find_program()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_library()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_file()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_path()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
<p>This is useful in cross-compiling environments. </p>
<p>By default this variable is not set, which is equivalent to it having a value of <code>TRUE</code>. Explicit options given to the above commands take precedence over this variable. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code>, <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code>, and <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> variables. </p>
 </dd></dl>
<h3>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</h3>
<p>New in version 3.16. </p>
<p>Controls searching the System Package Registry by the <code>find_package()</code> command. </p>
<p>By default this variable is not set and the behavior will fall back to that determined by the deprecated <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> variable. If that is also not set, then <code>find_package()</code> will use the System Package Registry unless the <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> option is provided. </p>
<p>This variable takes precedence over <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> when both are set. </p>
<p>In some cases, for example to locate only user specific installations, it is not desirable to use the System Package Registry when searching for packages. If the <code>CMAKE_FIND_USE_SYSTEM_PACKAGE_REGISTRY</code> variable is <code>FALSE</code>, all the <code>find_package()</code> commands will skip the System Package Registry as if they were called with the <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> argument. </p>
<p>See also Disabling the Package Registry. </p>
<p>See also the <code>CMAKE_FIND_USE_CMAKE_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_CMAKE_SYSTEM_PATH</code>, <code>CMAKE_FIND_USE_SYSTEM_ENVIRONMENT_PATH</code>, <code>CMAKE_FIND_USE_PACKAGE_REGISTRY</code>, and <code>CMAKE_FIND_USE_PACKAGE_ROOT_PATH</code> variables.  </p>
<h3>CMAKE_FRAMEWORK_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for macOS frameworks used by the <code>find_library()</code>, <code>find_package()</code>, <code>find_path()</code>, and <code>find_file()</code> commands.  </p>
<h3>CMAKE_IGNORE_PATH</h3>
<p>Semicolon-separated list of directories to be <i>ignored</i> by the <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. This is useful in cross-compiling environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine. </p>
<p>By default this is empty; it is intended to be set by the project. Note that <code>CMAKE_IGNORE_PATH</code> takes a list of directory names, <i>not</i> a list of prefixes. To ignore paths under prefixes (<code>bin</code>, <code>include</code>, <code>lib</code>, etc.), specify them explicitly. </p>
<p>See also the <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_LIBRARY_PATH</code>, <code>CMAKE_INCLUDE_PATH</code>, and <code>CMAKE_PROGRAM_PATH</code> variables.  </p>
<h3>CMAKE_INCLUDE_DIRECTORIES_BEFORE</h3>
<p>Whether to append or prepend directories by default in <code>include_directories()</code>. </p>
<p>This variable affects the default behavior of the <code>include_directories()</code> command. Setting this variable to <code>ON</code> is equivalent to using the <code>BEFORE</code> option in all uses of that command.  </p>
<h3>CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE</h3>
<p>Whether to force prepending of project include directories. </p>
<p>This variable affects the order of include directories generated in compiler command lines. If set to <code>ON</code>, it causes the <code>CMAKE_SOURCE_DIR</code> and the <code>CMAKE_BINARY_DIR</code> to appear first.  </p>
<h3>CMAKE_INCLUDE_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_file()</code> and <code>find_path()</code> commands. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_INCLUDE_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.  </p>
<h3>CMAKE_INSTALL_DEFAULT_COMPONENT_NAME</h3>
<p>Default component used in <code>install()</code> commands. </p>
<p>If an <code>install()</code> command is used without the <code>COMPONENT</code> argument, these files will be grouped into a default component. The name of this default install component will be taken from this variable. It defaults to <code>Unspecified</code>.  </p>
<h3>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</h3>
<p>New in version 3.11. </p>
<p>Default permissions for directories created implicitly during installation of files by <code>install()</code> and <code>file(INSTALL)</code>. </p>
<p>If <code>make install</code> is invoked and directories are implicitly created they get permissions set by <i>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</i> variable or platform specific default permissions if the variable is not set. </p>
<p>Implicitly created directories are created if they are not explicitly installed by <code>install()</code> command but are needed to install a file on a certain path. Example of such locations are directories created due to the setting of <code>CMAKE_INSTALL_PREFIX</code>. </p>
<p>Expected content of the <i>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</i> variable is a list of permissions that can be used by <code>install()</code> command <i>PERMISSIONS</i> section. </p>
<p>Example usage: </p>
<pre><code>set(CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS
     OWNER_READ
     OWNER_WRITE
     OWNER_EXECUTE
     GROUP_READ
   )
</code></pre>
<h3>CMAKE_INSTALL_MESSAGE</h3>
<p>New in version 3.1. </p>
<p>Specify verbosity of installation script code generated by the <code>install()</code> command (using the <code>file(INSTALL)</code> command). For paths that are newly installed or updated, installation may print lines like: </p>
<pre><code>-- Installing: /some/destination/path
</code></pre>
<p>For paths that are already up to date, installation may print lines like: </p>
<pre><code>-- Up-to-date: /some/destination/path
</code></pre>
<p>The <code>CMAKE_INSTALL_MESSAGE</code> variable may be set to control which messages are printed: </p>
<dl>
<dt><code>ALWAYS</code></dt>
<dd> <p> Print both <code>Installing</code> and <code>Up-to-date</code> messages. </p>
 </dd>
<dt><code>LAZY</code></dt>
<dd> <p> Print <code>Installing</code> but not <code>Up-to-date</code> messages. </p>
 </dd>
<dt><code>NEVER</code></dt>
<dd> <p> Print neither <code>Installing</code> nor <code>Up-to-date</code> messages. </p>
<p>Other values have undefined behavior and may not be diagnosed. </p>
<p>If this variable is not set, the default behavior is <code>ALWAYS</code>. </p>
 </dd></dl>
<h3>CMAKE_INSTALL_PREFIX</h3>
<p>Install directory used by <code>install()</code>. </p>
<p>If <code>make install</code> is invoked or <code>INSTALL</code> is built, this directory is prepended onto all install directories. This variable defaults to <code>/usr/local</code> on UNIX and <code>c:/Program Files/${PROJECT_NAME}</code> on Windows. See <code>CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT</code> for how a project might choose its own default. </p>
<p>On UNIX one can use the <code>DESTDIR</code> mechanism in order to relocate the whole installation. See <code>DESTDIR</code> for more information. </p>
<p>The installation prefix is also added to <code>CMAKE_SYSTEM_PREFIX_PATH</code> so that <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_path()</code>, and <code>find_file()</code> will search the prefix for other software. </p>
<p> <code>NOTE:</code> Use the <code>GNUInstallDirs</code> module to provide GNU-style options for the layout of directories within the installation.  </p>
<h3>CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT</h3>
<p>New in version 3.7.1. </p>
<p>CMake sets this variable to a <code>TRUE</code> value when the <code>CMAKE_INSTALL_PREFIX</code> has just been initialized to its default value, typically on the first run of CMake within a new build tree. This can be used by project code to change the default without overriding a user-provided value: </p>
<pre><code>if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX &quot;/my/default&quot; CACHE PATH &quot;...&quot; FORCE)
endif()
</code></pre>
<h3>CMAKE_LIBRARY_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_library()</code> command. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_LIBRARY_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.  </p>
<h3>CMAKE_LINK_DIRECTORIES_BEFORE</h3>
<p>New in version 3.13. </p>
<p>Whether to append or prepend directories by default in <code>link_directories()</code>. </p>
<p>This variable affects the default behavior of the <code>link_directories()</code> command. Setting this variable to <code>ON</code> is equivalent to using the <code>BEFORE</code> option in all uses of that command.  </p>
<h3>CMAKE_MFC_FLAG</h3>
<p>Use the MFC library for an executable or dll. </p>
<p>Enables the use of the Microsoft Foundation Classes (MFC). It should be set to <code>1</code> for the static MFC library, and <code>2</code> for the shared MFC library. This is used in Visual Studio project files. </p>
<p>Usage example: </p>
<pre><code>add_definitions(-D_AFXDLL)
set(CMAKE_MFC_FLAG 2)
add_executable(CMakeSetup WIN32 ${SRCS})
</code></pre>
<p>Contents of <code>CMAKE_MFC_FLAG</code> may use <code>generator expressions</code>.  </p>
<h3>CMAKE_MAXIMUM_RECURSION_DEPTH</h3>
<p>New in version 3.14. </p>
<p>Maximum recursion depth for CMake scripts. It is intended to be set on the command line with <code>-DCMAKE_MAXIMUM_RECURSION_DEPTH=&lt;x&gt;</code>, or within <code>CMakeLists.txt</code> by projects that require a large recursion depth. Projects that set this variable should provide the user with a way to override it. For example: </p>
<pre><code># About to perform deeply recursive actions
if(NOT CMAKE_MAXIMUM_RECURSION_DEPTH)
  set(CMAKE_MAXIMUM_RECURSION_DEPTH 2000)
endif()
</code></pre>
<p>If it is not set, or is set to a non-integer value, a sensible default limit is used. If the recursion limit is reached, the script terminates immediately with a fatal error. </p>
<p>Calling any of the following commands increases the recursion depth: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>include()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>find_package()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>add_subdirectory()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>try_compile()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ctest_read_custom_files()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ctest_run_script()</code> (unless <code>NEW_PROCESS</code> is specified) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> User-defined <code>function()</code>&#8216;s and <code>macro()</code>&#8216;s (note that <code>function()</code> and <code>macro()</code> themselves don&#8217;t increase recursion depth) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reading or writing variables that are being watched by a <code>variable_watch()</code> </p>
 </dd></dl>
<h3>CMAKE_MESSAGE_CONTEXT</h3>
<p>New in version 3.17. </p>
<p>When enabled by the <code>cmake</code> <code>--log-context</code> command line option or the <code>CMAKE_MESSAGE_CONTEXT_SHOW</code> variable, the <code>message()</code> command converts the <code>CMAKE_MESSAGE_CONTEXT</code> list into a dot-separated string surrounded by square brackets and prepends it to each line for messages of log levels <code>NOTICE</code> and below. </p>
<p>For logging contexts to work effectively, projects should generally <code>APPEND</code> and <code>POP_BACK</code> an item to the current value of <code>CMAKE_MESSAGE_CONTEXT</code> rather than replace it. Projects should not assume the message context at the top of the source tree is empty, as there are scenarios where the context might have already been set (e.g. hierarchical projects). </p>
<p> <code>WARNING:</code> Valid context names are restricted to anything that could be used as a CMake variable name. All names that begin with an underscore or the string <code>cmake_</code> are also reserved for use by CMake and should not be used by projects. </p>
<p>Example: </p>
<pre><code>function(bar)
  list(APPEND CMAKE_MESSAGE_CONTEXT &quot;bar&quot;)
  message(VERBOSE &quot;bar VERBOSE message&quot;)
endfunction()
function(baz)
  list(APPEND CMAKE_MESSAGE_CONTEXT &quot;baz&quot;)
  message(DEBUG &quot;baz DEBUG message&quot;)
endfunction()
function(foo)
  list(APPEND CMAKE_MESSAGE_CONTEXT &quot;foo&quot;)
  bar()
  message(TRACE &quot;foo TRACE message&quot;)
  baz()
endfunction()
list(APPEND CMAKE_MESSAGE_CONTEXT &quot;top&quot;)
message(VERBOSE &quot;Before `foo`&quot;)
foo()
message(VERBOSE &quot;After `foo`&quot;)
list(POP_BACK CMAKE_MESSAGE_CONTEXT)
</code></pre>
<p>Which results in the following output: </p>
<pre><code>-- [top] Before `foo`
-- [top.foo.bar] bar VERBOSE message
-- [top.foo] foo TRACE message
-- [top.foo.baz] baz DEBUG message
-- [top] After `foo`
</code></pre>
<h3>CMAKE_MESSAGE_CONTEXT_SHOW</h3>
<p>New in version 3.17. </p>
<p>Setting this variable to true enables showing a context with each line logged by the <code>message()</code> command (see <code>CMAKE_MESSAGE_CONTEXT</code> for how the context itself is specified). </p>
<p>This variable is an alternative to providing the <code>--log-context</code> option on the <code>cmake</code> command line. Whereas the command line option will apply only to that one CMake run, setting <code>CMAKE_MESSAGE_CONTEXT_SHOW</code> to true as a cache variable will ensure that subsequent CMake runs will continue to show the message context. </p>
<p>Projects should not set <code>CMAKE_MESSAGE_CONTEXT_SHOW</code>. It is intended for users so that they may control whether or not to include context with messages.  </p>
<h3>CMAKE_MESSAGE_INDENT</h3>
<p>New in version 3.16. </p>
<p>The <code>message()</code> command joins the strings from this list and for log levels of <code>NOTICE</code> and below, it prepends the resultant string to each line of the message. </p>
<p>Example: </p>
<pre><code>list(APPEND listVar one two three)
message(VERBOSE [[Collected items in the &quot;listVar&quot;:]])
list(APPEND CMAKE_MESSAGE_INDENT &quot; &quot;)
foreach(item IN LISTS listVar)
  message(VERBOSE ${item})
endforeach()
list(POP_BACK CMAKE_MESSAGE_INDENT)
message(VERBOSE &quot;No more indent&quot;)
</code></pre>
<p>Which results in the following output: </p>
<pre><code>-- Collected items in the &quot;listVar&quot;:
-- one
-- two
-- three
-- No more indent
</code></pre>
<h3>CMAKE_MESSAGE_LOG_LEVEL</h3>
<p>New in version 3.17. </p>
<p>When set, this variable specifies the logging level used by the <code>message()</code> command. Valid values are the same as those for the <code>--log-level</code> command line option of the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> program. If this variable is set and the <code>--log-level</code> command line option is given, the command line option takes precedence. </p>
<p>The main advantage to using this variable is to make a log level persist between CMake runs. Setting it as a cache variable will ensure that subsequent CMake runs will continue to use the chosen log level. </p>
<p>Projects should not set this variable, it is intended for users so that they may control the log level according to their own needs.  </p>
<h3>CMAKE_MODULE_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for CMake modules to be loaded by the <code>include()</code> or <code>find_package()</code> commands before checking the default modules that come with CMake. By default it is empty, it is intended to be set by the project.  </p>
<h3>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</h3>
<p>Default for CMake Policy <code>CMP&lt;NNNN&gt;</code> when it is otherwise left unset. </p>
<p>Commands <code>cmake_minimum_required(VERSION)</code> and <code>cmake_policy(VERSION)</code> by default leave policies introduced after the given version unset. Set <code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code> to <code>OLD</code> or <code>NEW</code> to specify the default for policy <code>CMP&lt;NNNN&gt;</code>, where <code>&lt;NNNN&gt;</code> is the policy number. </p>
<p>This variable should not be set by a project in CMake code as a way to set its own policies; use <code>cmake_policy(SET)</code> instead. This variable is meant to externally set policies for which a project has not itself been updated: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Users running CMake may set this variable in the cache (e.g. <code>-DCMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;=&lt;OLD|NEW&gt;</code>). Set it to <code>OLD</code> to quiet a policy warning while using old behavior or to <code>NEW</code> to try building the project with new behavior. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Projects may set this variable before a call to <code>add_subdirectory()</code> that adds a third-party project in order to set its policies without modifying third-party code. </p>
 </dd></dl>
<h3>CMAKE_POLICY_WARNING_CMP&lt;NNNN&gt;</h3>
<p>Explicitly enable or disable the warning when CMake Policy <code>CMP&lt;NNNN&gt;</code> has not been set explicitly by <code>cmake_policy()</code> or implicitly by <code>cmake_minimum_required()</code>. This is meaningful only for the policies that do not warn by default: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0025</code> controls the warning for policy <code>CMP0025</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0047</code> controls the warning for policy <code>CMP0047</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0056</code> controls the warning for policy <code>CMP0056</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0060</code> controls the warning for policy <code>CMP0060</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0065</code> controls the warning for policy <code>CMP0065</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0066</code> controls the warning for policy <code>CMP0066</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0067</code> controls the warning for policy <code>CMP0067</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0082</code> controls the warning for policy <code>CMP0082</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0089</code> controls the warning for policy <code>CMP0089</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0102</code> controls the warning for policy <code>CMP0102</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0112</code> controls the warning for policy <code>CMP0112</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0116</code> controls the warning for policy <code>CMP0116</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0126</code> controls the warning for policy <code>CMP0126</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_POLICY_WARNING_CMP0128</code> controls the warning for policy <code>CMP0128</code>. </p>
<p>This variable should not be set by a project in CMake code. Project developers running CMake may set this variable in their cache to enable the warning (e.g. <code>-DCMAKE_POLICY_WARNING_CMP&lt;NNNN&gt;=ON</code>). Alternatively, running <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> with the <code>--debug-output</code>, <code>--trace</code>, or <code>--trace-expand</code> option will also enable the warning. </p>
 </dd></dl>
<h3>CMAKE_PREFIX_PATH</h3>
<p>Semicolon-separated list of directories specifying installation <i>prefixes</i> to be searched by the <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. Each command will add appropriate subdirectories (like <code>bin</code>, <code>lib</code>, or <code>include</code>) as specified in its own documentation. </p>
<p>By default this is empty. It is intended to be set by the project. </p>
<p>See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>, <code>CMAKE_INCLUDE_PATH</code>, <code>CMAKE_LIBRARY_PATH</code>, <code>CMAKE_PROGRAM_PATH</code>, and <code>CMAKE_IGNORE_PATH</code>.  </p>
<h3>CMAKE_PROGRAM_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_program()</code> command. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_PROGRAM_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.  </p>
<h3>CMAKE_PROJECT_INCLUDE</h3>
<p>New in version 3.15. </p>
<p>A CMake language file or module to be included as the last step of all <code>project()</code> command calls. This is intended for injecting custom code into project builds without modifying their source. </p>
<p>See also the <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code>, <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code> and <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> variables.  </p>
<h3>CMAKE_PROJECT_INCLUDE_BEFORE</h3>
<p>New in version 3.15. </p>
<p>A CMake language file or module to be included as the first step of all <code>project()</code> command calls. This is intended for injecting custom code into project builds without modifying their source. </p>
<p>See also the <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code>, <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code> and <code>CMAKE_PROJECT_INCLUDE</code> variables.  </p>
<h3>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</h3>
<p>A CMake language file or module to be included as the last step of any <code>project()</code> command calls that specify <code>&lt;PROJECT-NAME&gt;</code> as the project name. This is intended for injecting custom code into project builds without modifying their source. </p>
<p>See also the <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</code>, <code>CMAKE_PROJECT_INCLUDE</code> and <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> variables.  </p>
<h3>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE_BEFORE</h3>
<p>New in version 3.17. </p>
<p>A CMake language file or module to be included as the first step of any <code>project()</code> command calls that specify <code>&lt;PROJECT-NAME&gt;</code> as the project name. This is intended for injecting custom code into project builds without modifying their source. </p>
<p>See also the <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code>, <code>CMAKE_PROJECT_INCLUDE</code> and <code>CMAKE_PROJECT_INCLUDE_BEFORE</code> variables.  </p>
<h3>CMAKE_REQUIRE_FIND_PACKAGE_&lt;PackageName&gt;</h3>
<p>New in version 3.22. </p>
<p>Variable for making <code>find_package()</code> call <code>REQUIRED</code>. </p>
<p>Every non-<code>REQUIRED</code> <code>find_package()</code> call in a project can be turned into <code>REQUIRED</code> by setting the variable <code>CMAKE_REQUIRE_FIND_PACKAGE_&lt;PackageName&gt;</code> to <code>TRUE</code>. This can be used to assert assumptions about build environment and to ensure the build will fail early if they do not hold. </p>
<p>See also the <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable.  </p>
<h3>CMAKE_SKIP_INSTALL_ALL_DEPENDENCY</h3>
<p>Don&#8217;t make the <code>install</code> target depend on the <code>all</code> target. </p>
<p>By default, the <code>install</code> target depends on the <code>all</code> target. This has the effect, that when <code>make install</code> is invoked or <code>INSTALL</code> is built, first the <code>all</code> target is built, then the installation starts. If <i>CMAKE_SKIP_INSTALL_ALL_DEPENDENCY</i> is set to <code>TRUE</code>, this dependency is not created, so the installation process will start immediately, independent from whether the project has been completely built or not.  </p>
<h3>CMAKE_STAGING_PREFIX</h3>
<p>This variable may be set to a path to install to when cross-compiling. This can be useful if the path in <code>CMAKE_SYSROOT</code> is read-only, or otherwise should remain pristine. </p>
<p>The <i>CMAKE_STAGING_PREFIX</i> location is also used as a search prefix by the <code>find_*</code> commands. This can be controlled by setting the <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> variable. </p>
<p>If any <code>RPATH</code>/<code>RUNPATH</code> entries passed to the linker contain the <i>CMAKE_STAGING_PREFIX</i>, the matching path fragments are replaced with the <code>CMAKE_INSTALL_PREFIX</code>.  </p>
<h3>CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS</h3>
<p>New in version 3.8. </p>
<p>This variable contains a list of env vars as a list of tokens with the syntax <code>var=value</code>. </p>
<p>Example: </p>
<pre><code>set(CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS
   &quot;FOO=FOO1\;FOO2\;FOON&quot;
   &quot;BAR=BAR1\;BAR2\;BARN&quot;
   &quot;BAZ=BAZ1\;BAZ2\;BAZN&quot;
   &quot;FOOBAR=FOOBAR1\;FOOBAR2\;FOOBARN&quot;
   &quot;VALID=&quot;
   )
</code></pre>
<p>In case of malformed variables CMake will fail: </p>
<pre><code>set(CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS
    &quot;THIS_IS_NOT_VALID&quot;
    )
</code></pre>
<h3>CMAKE_SUBLIME_TEXT_2_EXCLUDE_BUILD_TREE</h3>
<p>New in version 3.8. </p>
<p>If this variable evaluates to <code>ON</code> at the end of the top-level <code>CMakeLists.txt</code> file, the <code>Sublime Text 2</code> extra generator excludes the build tree from the <code>.sublime-project</code> if it is inside the source tree.  </p>
<h3>CMAKE_SUPPRESS_REGENERATION</h3>
<p>New in version 3.12. </p>
<p>If <code>CMAKE_SUPPRESS_REGENERATION</code> is <code>OFF</code>, which is default, then CMake adds a special target on which all other targets depend that checks the build system and optionally re-runs CMake to regenerate the build system when the target specification source changes. </p>
<p>If this variable evaluates to <code>ON</code> at the end of the top-level <code>CMakeLists.txt</code> file, CMake will not add the regeneration target to the build system or perform any build system checks.  </p>
<h3>CMAKE_SYSROOT</h3>
<p>Path to pass to the compiler in the <code>--sysroot</code> flag. </p>
<p>The <code>CMAKE_SYSROOT</code> content is passed to the compiler in the <code>--sysroot</code> flag, if supported. The path is also stripped from the <code>RPATH</code>/<code>RUNPATH</code> if necessary on installation. The <code>CMAKE_SYSROOT</code> is also used to prefix paths searched by the <code>find_*</code> commands. </p>
<p>This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable. </p>
<p>See also the <code>CMAKE_SYSROOT_COMPILE</code> and <code>CMAKE_SYSROOT_LINK</code> variables.  </p>
<h3>CMAKE_SYSROOT_COMPILE</h3>
<p>New in version 3.9. </p>
<p>Path to pass to the compiler in the <code>--sysroot</code> flag when compiling source files. This is the same as <code>CMAKE_SYSROOT</code> but is used only for compiling sources and not linking. </p>
<p>This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.  </p>
<h3>CMAKE_SYSROOT_LINK</h3>
<p>New in version 3.9. </p>
<p>Path to pass to the compiler in the <code>--sysroot</code> flag when linking. This is the same as <code>CMAKE_SYSROOT</code> but is used only for linking and not compiling sources. </p>
<p>This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.  </p>
<h3>CMAKE_SYSTEM_APPBUNDLE_PATH</h3>
<p>New in version 3.4. </p>
<p>Search path for macOS application bundles used by the <code>find_program()</code>, and <code>find_package()</code> commands. By default it contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project, use <code>CMAKE_APPBUNDLE_PATH</code> for this.  </p>
<h3>CMAKE_SYSTEM_FRAMEWORK_PATH</h3>
<p>New in version 3.4. </p>
<p>Search path for macOS frameworks used by the <code>find_library()</code>, <code>find_package()</code>, <code>find_path()</code>, and <code>find_file()</code> commands. By default it contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project, use <code>CMAKE_FRAMEWORK_PATH</code> for this.  </p>
<h3>CMAKE_SYSTEM_IGNORE_PATH</h3>
<p>Semicolon-separated list of directories to be <i>ignored</i> by the <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. This is useful in cross-compiling environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine. </p>
<p>By default this contains a list of directories containing incompatible binaries for the host system. See the <code>CMAKE_IGNORE_PATH</code> variable that is intended to be set by the project. </p>
<p>See also the <code>CMAKE_SYSTEM_PREFIX_PATH</code>, <code>CMAKE_SYSTEM_LIBRARY_PATH</code>, <code>CMAKE_SYSTEM_INCLUDE_PATH</code>, and <code>CMAKE_SYSTEM_PROGRAM_PATH</code> variables.  </p>
<h3>CMAKE_SYSTEM_INCLUDE_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_file()</code> and <code>find_path()</code> commands. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_INCLUDE_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.  </p>
<h3>CMAKE_SYSTEM_LIBRARY_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_library()</code> command. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_LIBRARY_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.  </p>
<h3>CMAKE_SYSTEM_PREFIX_PATH</h3>
<p>Semicolon-separated list of directories specifying installation <i>prefixes</i> to be searched by the <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. Each command will add appropriate subdirectories (like <code>bin</code>, <code>lib</code>, or <code>include</code>) as specified in its own documentation. </p>
<p>By default this contains the system directories for the current system, the <code>CMAKE_INSTALL_PREFIX</code>, and the <code>CMAKE_STAGING_PREFIX</code>. The installation and staging prefixes may be excluded by setting the <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> variable. </p>
<p>The system directories that are contained in <code>CMAKE_SYSTEM_PREFIX_PATH</code> are locations that typically include installed software. An example being <code>/usr/local</code> for UNIX based platforms. In addition to standard platform locations, CMake will also add values to <code>CMAKE_SYSTEM_PREFIX_PATH</code> based on environment variables. The environment variables and search locations that CMake uses may evolve over time, as platforms and their conventions also evolve. The following provides an indicative list of environment variables and locations that CMake searches, but they are subject to change: </p>
<dl>
<dt><code>CrayLinuxEnvironment:</code></dt>
<dd>  </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SYSROOT_DIR}/</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SYSROOT_DIR}/usr</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SYSROOT_DIR}/usr/local</code> </p>
 </dd>
<dt><code>Darwin:</code></dt>
<dd>  </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SDKROOT}/usr</code> When <code>CMAKE_OSX_SYSROOT</code> is not explicitly specified. </p>
 </dd>
<dt><code>OpenBSD:</code></dt>
<dd>  </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{LOCALBASE}</code> </p>
 </dd>
<dt><code>Unix:</code></dt>
<dd>  </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{CONDA_PREFIX}</code> when using a conda compiler </p>
 </dd>
<dt><code>Windows:</code></dt>
<dd>  </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{ProgramW6432}</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{ProgramFiles}</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{ProgramFiles(x86)}</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SystemDrive}/Program Files</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>ENV{SystemDrive}/Program Files (x86)</code> </p>
<p> <code>CMAKE_SYSTEM_PREFIX_PATH</code> is <i>not</i> intended to be modified by the project; use <code>CMAKE_PREFIX_PATH</code> for this. </p>
<p>See also <code>CMAKE_SYSTEM_INCLUDE_PATH</code>, <code>CMAKE_SYSTEM_LIBRARY_PATH</code>, <code>CMAKE_SYSTEM_PROGRAM_PATH</code>, and <code>CMAKE_SYSTEM_IGNORE_PATH</code>. </p>
 </dd></dl>
<h3>CMAKE_SYSTEM_PROGRAM_PATH</h3>
<p>Semicolon-separated list of directories specifying a search path for the <code>find_program()</code> command. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_PROGRAM_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.  </p>
<h3>CMAKE_TLS_CAINFO</h3>
<p>Specify the default value for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands&#8217; <code>TLS_CAINFO</code> options. It is unset by default. </p>
<p>This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>.  </p>
<h3>CMAKE_TLS_VERIFY</h3>
<p>Specify the default value for the <code>file(DOWNLOAD)</code> and <code>file(UPLOAD)</code> commands&#8217; <code>TLS_VERIFY</code> options. If not set, the default is <i>off</i>. </p>
<p>This variable is also used by the <code>ExternalProject</code> and <code>FetchContent</code> modules for internal calls to <code>file(DOWNLOAD)</code>. </p>
<p>TLS verification can help provide confidence that one is connecting to the desired server. When downloading known content, one should also use file hashes to verify it. </p>
<pre><code>set(CMAKE_TLS_VERIFY TRUE)
</code></pre>
<h3>CMAKE_USER_MAKE_RULES_OVERRIDE</h3>
<p>Specify a CMake file that overrides platform information. </p>
<p>CMake loads the specified file while enabling support for each language from either the <code>project()</code> or <code>enable_language()</code> commands. It is loaded after CMake&#8217;s builtin compiler and platform information modules have been loaded but before the information is used. The file may set platform information variables to override CMake&#8217;s defaults. </p>
<p>This feature is intended for use only in overriding information variables that must be set before CMake builds its first test project to check that the compiler for a language works. It should not be used to load a file in cases that a normal <code>include()</code> will work. Use it only as a last resort for behavior that cannot be achieved any other way. For example, one may set the <code>CMAKE_C_FLAGS_INIT</code> variable to change the default value used to initialize the <code>CMAKE_C_FLAGS</code> variable before it is cached. The override file should NOT be used to set anything that could be set after languages are enabled, such as variables like <code>CMAKE_RUNTIME_OUTPUT_DIRECTORY</code> that affect the placement of binaries. Information set in the file will be used for <code>try_compile()</code> and <code>try_run()</code> builds too.  </p>
<h3>CMAKE_WARN_DEPRECATED</h3>
<p>Whether to issue warnings for deprecated functionality. </p>
<p>If not <code>FALSE</code>, use of deprecated functionality will issue warnings. If this variable is not set, CMake behaves as if it were set to <code>TRUE</code>. </p>
<p>When running <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code>, this option can be enabled with the <code>-Wdeprecated</code> option, or disabled with the <code>-Wno-deprecated</code> option.  </p>
<h3>CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</h3>
<p>Ask <code>cmake_install.cmake</code> script to warn each time a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p>This variable is used by CMake-generated <code>cmake_install.cmake</code> scripts. If one sets this variable to <code>ON</code> while running the script, it may get warning messages from the script.  </p>
<h3>CMAKE_XCODE_GENERATE_SCHEME</h3>
<p>New in version 3.9. </p>
<p>If enabled, the <code>Xcode</code> generator will generate schema files. These are useful to invoke analyze, archive, build-for-testing and test actions from the command line. </p>
<p>This variable initializes the <code>XCODE_GENERATE_SCHEME</code> target property on all targets.  </p>
<h3>CMAKE_XCODE_GENERATE_TOP_LEVEL_PROJECT_ONLY</h3>
<p>New in version 3.11. </p>
<p>If enabled, the <code>Xcode</code> generator will generate only a single Xcode project file for the topmost <code>project()</code> command instead of generating one for every <code>project()</code> command. </p>
<p>This could be useful to speed up the CMake generation step for large projects and to work-around a bug in the <code>ZERO_CHECK</code> logic.  </p>
<h3>CMAKE_XCODE_LINK_BUILD_PHASE_MODE</h3>
<p>New in version 3.19. </p>
<p>This variable is used to initialize the <code>XCODE_LINK_BUILD_PHASE_MODE</code> property on targets. It affects the methods that the <code>Xcode</code> generator uses to link different kinds of libraries. Its default value is <code>NONE</code>.  </p>
<h3>CMAKE_XCODE_SCHEME_ADDRESS_SANITIZER</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Address Sanitizer</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_ADDRESS_SANITIZER</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_ADDRESS_SANITIZER_USE_AFTER_RETURN</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Detect use of stack after return</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_ADDRESS_SANITIZER_USE_AFTER_RETURN</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_DEBUG_DOCUMENT_VERSIONING</h3>
<p>New in version 3.16. </p>
<p>Whether to enable <code>Allow debugging when using document Versions Browser</code> in the Options section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_DEBUG_DOCUMENT_VERSIONING</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_DISABLE_MAIN_THREAD_CHECKER</h3>
<p>New in version 3.13. </p>
<p>Whether to disable the <code>Main Thread Checker</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_DISABLE_MAIN_THREAD_CHECKER</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_DYNAMIC_LIBRARY_LOADS</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Dynamic Library Loads</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_DYNAMIC_LIBRARY_LOADS</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_DYNAMIC_LINKER_API_USAGE</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Dynamic Linker API usage</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_DYNAMIC_LINKER_API_USAGE</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_ENVIRONMENT</h3>
<p>New in version 3.17. </p>
<p>Specify environment variables that should be added to the Arguments section of the generated Xcode scheme. </p>
<p>If set to a list of environment variables and values of the form <code>MYVAR=value</code> those environment variables will be added to the scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_ENVIRONMENT</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_GUARD_MALLOC</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Guard Malloc</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_GUARD_MALLOC</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_MAIN_THREAD_CHECKER_STOP</h3>
<p>New in version 3.13. </p>
<p>Whether to enable the <code>Main Thread Checker</code> option <code>Pause on issues</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_MAIN_THREAD_CHECKER_STOP</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_MALLOC_GUARD_EDGES</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Malloc Guard Edges</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_MALLOC_GUARD_EDGES</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_MALLOC_SCRIBBLE</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Malloc Scribble</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_MALLOC_SCRIBBLE</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_MALLOC_STACK</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Malloc Stack</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_MALLOC_STACK</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_THREAD_SANITIZER</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Thread Sanitizer</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_THREAD_SANITIZER</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_THREAD_SANITIZER_STOP</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Thread Sanitizer - Pause on issues</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_THREAD_SANITIZER_STOP</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Undefined Behavior Sanitizer</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER_STOP</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Undefined Behavior Sanitizer</code> option <code>Pause on issues</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER_STOP</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_WORKING_DIRECTORY</h3>
<p>New in version 3.17. </p>
<p>Specify the <code>Working Directory</code> of the <i>Run</i> and <i>Profile</i> actions in the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_WORKING_DIRECTORY</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>CMAKE_XCODE_SCHEME_ZOMBIE_OBJECTS</h3>
<p>New in version 3.13. </p>
<p>Whether to enable <code>Zombie Objects</code> in the Diagnostics section of the generated Xcode scheme. </p>
<p>This variable initializes the <code>XCODE_SCHEME_ZOMBIE_OBJECTS</code> property on all targets. </p>
<p>Please refer to the <code>XCODE_GENERATE_SCHEME</code> target property documentation to see all Xcode schema related properties.  </p>
<h3>&lt;PackageName&gt;_ROOT</h3>
<p>New in version 3.12. </p>
<p>Calls to <code>find_package(&lt;PackageName&gt;)</code> will search in prefixes specified by the <code>&lt;PackageName&gt;_ROOT</code> CMake variable, where <code>&lt;PackageName&gt;</code> is the name given to the <code>find_package()</code> call and <code>_ROOT</code> is literal. For example, <code>find_package(Foo)</code> will search prefixes specified in the <code>Foo_ROOT</code> CMake variable (if set). See policy <code>CMP0074</code>. </p>
<p>This variable may hold a single prefix or a semicolon-separated list of multiple prefixes. </p>
<p>See also the <code>&lt;PackageName&gt;_ROOT</code> environment variable.  </p>
<h2>VARIABLES THAT DESCRIBE THE SYSTEM</h2>
<h3>ANDROID</h3>
<p>New in version 3.7. </p>
<p>Set to <code>1</code> when the target system (<code>CMAKE_SYSTEM_NAME</code>) is <code>Android</code>.  </p>
<h3>APPLE</h3>
<p>Set to <code>True</code> when the target system is an Apple platform (macOS, iOS, tvOS or watchOS).  </p>
<h3>BORLAND</h3>
<p> <code>True</code> if the Borland compiler is being used. </p>
<p>This is set to <code>true</code> if the Borland compiler is being used.  </p>
<h3>CMAKE_ANDROID_NDK_VERSION</h3>
<p>New in version 3.20. </p>
<p>When Cross Compiling for Android with the NDK and using an Android NDK version 11 or higher, this variable is provided by CMake to report the NDK version number.  </p>
<h3>CMAKE_CL_64</h3>
<p>Discouraged. Use <code>CMAKE_SIZEOF_VOID_P</code> instead. </p>
<p>Set to a true value when using a Microsoft Visual Studio <code>cl</code> compiler that <i>targets</i> a 64-bit architecture.  </p>
<h3>CMAKE_COMPILER_2005</h3>
<p>Using the Visual Studio 2005 compiler from Microsoft </p>
<p>Set to true when using the Visual Studio 2005 compiler from Microsoft.  </p>
<h3>CMAKE_HOST_APPLE</h3>
<p> <code>True</code> for Apple macOS operating systems. </p>
<p>Set to <code>true</code> when the host system is Apple macOS.  </p>
<h3>CMAKE_HOST_SOLARIS</h3>
<p>New in version 3.6. </p>
<p> <code>True</code> for Oracle Solaris operating systems. </p>
<p>Set to <code>true</code> when the host system is Oracle Solaris.  </p>
<h3>CMAKE_HOST_SYSTEM</h3>
<p>Composite Name of OS CMake is being run on. </p>
<p>This variable is the composite of <code>CMAKE_HOST_SYSTEM_NAME</code> and <code>CMAKE_HOST_SYSTEM_VERSION</code>, e.g. <code>${CMAKE_HOST_SYSTEM_NAME}-${CMAKE_HOST_SYSTEM_VERSION}</code>. If <code>CMAKE_HOST_SYSTEM_VERSION</code> is not set, then this variable is the same as <code>CMAKE_HOST_SYSTEM_NAME</code>.  </p>
<h3>CMAKE_HOST_SYSTEM_NAME</h3>
<p>Name of the OS CMake is running on. </p>
<p>On systems that have the uname command, this variable is set to the output of <code>uname -s</code>. <code>Linux</code>, <code>Windows</code>, and <code>Darwin</code> for macOS are the values found on the big three operating systems.  </p>
<h3>CMAKE_HOST_SYSTEM_PROCESSOR</h3>
<p>The name of the CPU CMake is running on.  </p>
<h3>Windows Platforms</h3>
<p>On Windows, this variable is set to the value of the environment variable <code>PROCESSOR_ARCHITECTURE</code>.  </p>
<h3>Unix Platforms</h3>
<p>On systems that support <code>uname</code>, this variable is set to the output of: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>uname -m</code> on GNU, Linux, Cygwin, Android, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>arch</code> on OpenBSD, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> on other systems, </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>uname -p</code> if its exit code is nonzero, or </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>uname -m</code> otherwise. </p>
 </dd></dl>
<h3>macOS Platforms</h3>
<p>The value of <code>uname -m</code> is used by default. </p>
<p>On Apple Silicon hosts, the architecture printed by <code>uname -m</code> may vary based on CMake&#8217;s own architecture and that of the invoking process tree. </p>
<p>New in version 3.19.2: On Apple Silicon hosts: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>CMAKE_APPLE_SILICON_PROCESSOR</code> variable or the <code>CMAKE_APPLE_SILICON_PROCESSOR</code> environment variable may be set to specify the host architecture explicitly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If <code>CMAKE_OSX_ARCHITECTURES</code> is not set, CMake adds explicit flags to tell the compiler to build for the host architecture so the toolchain does not have to guess based on the process tree&#8217;s architecture. </p>
 </dd></dl>
<h3>CMAKE_HOST_SYSTEM_VERSION</h3>
<p>The OS version CMake is running on. </p>
<p>A numeric version string for the system. On systems that support <code>uname</code>, this variable is set to the output of <code>uname -r</code>. On other systems this is set to major-minor version numbers.  </p>
<h3>CMAKE_HOST_UNIX</h3>
<p> <code>True</code> for UNIX and UNIX like operating systems. </p>
<p>Set to <code>true</code> when the host system is UNIX or UNIX like (i.e. APPLE and CYGWIN).  </p>
<h3>CMAKE_HOST_WIN32</h3>
<p> <code>True</code> if the host system is running Windows, including Windows 64-bit and MSYS. </p>
<p>Set to <code>false</code> on Cygwin.  </p>
<h3>CMAKE_LIBRARY_ARCHITECTURE</h3>
<p>Target architecture library directory name, if detected. </p>
<p>This is the value of <code>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</code> as detected for one of the enabled languages.  </p>
<h3>CMAKE_LIBRARY_ARCHITECTURE_REGEX</h3>
<p>Regex matching possible target architecture library directory names. </p>
<p>This is used to detect <code>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</code> from the implicit linker search path by matching the <code>&lt;arch&gt;</code> name.  </p>
<h3>CMAKE_OBJECT_PATH_MAX</h3>
<p>Maximum object file full-path length allowed by native build tools. </p>
<p>CMake computes for every source file an object file name that is unique to the source file and deterministic with respect to the full path to the source file. This allows multiple source files in a target to share the same name if they lie in different directories without rebuilding when one is added or removed. However, it can produce long full paths in a few cases, so CMake shortens the path using a hashing scheme when the full path to an object file exceeds a limit. CMake has a built-in limit for each platform that is sufficient for common tools, but some native tools may have a lower limit. This variable may be set to specify the limit explicitly. The value must be an integer no less than 128.  </p>
<h3>CMAKE_SYSTEM</h3>
<p>Composite name of operating system CMake is compiling for. </p>
<p>This variable is the composite of <code>CMAKE_SYSTEM_NAME</code> and <code>CMAKE_SYSTEM_VERSION</code>, e.g. <code>${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_VERSION}</code>. If <code>CMAKE_SYSTEM_VERSION</code> is not set, then this variable is the same as <code>CMAKE_SYSTEM_NAME</code>.  </p>
<h3>CMAKE_SYSTEM_NAME</h3>
<p>The name of the operating system for which CMake is to build. See the <code>CMAKE_SYSTEM_VERSION</code> variable for the OS version. </p>
<p>Note that <code>CMAKE_SYSTEM_NAME</code> is not set to anything by default when running in script mode, since it&#8217;s not building anything.  </p>
<h3>System Name for Host Builds</h3>
<p> <code>CMAKE_SYSTEM_NAME</code> is by default set to the same value as the <code>CMAKE_HOST_SYSTEM_NAME</code> variable so that the build targets the host system.  </p>
<h3>System Name for Cross Compiling</h3>
<p> <code>CMAKE_SYSTEM_NAME</code> may be set explicitly when first configuring a new build tree in order to enable cross compiling. In this case the <code>CMAKE_SYSTEM_VERSION</code> variable must also be set explicitly.  </p>
<h3>CMAKE_SYSTEM_PROCESSOR</h3>
<p>When not cross-compiling, this variable has the same value as the <code>CMAKE_HOST_SYSTEM_PROCESSOR</code> variable. In many cases, this will correspond to the target architecture for the build, but this is not guaranteed. (E.g. on Windows, the host may be <code>AMD64</code> even when using a MSVC <code>cl</code> compiler with a 32-bit target.) </p>
<p>When cross-compiling, a <code>CMAKE_TOOLCHAIN_FILE</code> should set the <code>CMAKE_SYSTEM_PROCESSOR</code> variable to match target architecture that it specifies (via <code>CMAKE_&lt;LANG&gt;_COMPILER</code> and perhaps <code>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</code>).  </p>
<h3>CMAKE_SYSTEM_VERSION</h3>
<p>The version of the operating system for which CMake is to build. See the <code>CMAKE_SYSTEM_NAME</code> variable for the OS name.  </p>
<h3>System Version for Host Builds</h3>
<p>When the <code>CMAKE_SYSTEM_NAME</code> variable takes its default value then <code>CMAKE_SYSTEM_VERSION</code> is by default set to the same value as the <code>CMAKE_HOST_SYSTEM_VERSION</code> variable so that the build targets the host system version. </p>
<p>In the case of a host build then <code>CMAKE_SYSTEM_VERSION</code> may be set explicitly when first configuring a new build tree in order to enable targeting the build for a different version of the host operating system than is actually running on the host. This is allowed and not considered cross compiling so long as the binaries built for the specified OS version can still run on the host.  </p>
<h3>System Version for Cross Compiling</h3>
<p>When the <code>CMAKE_SYSTEM_NAME</code> variable is set explicitly to enable cross compiling then the value of <code>CMAKE_SYSTEM_VERSION</code> must also be set explicitly to specify the target system version.  </p>
<h3>CYGWIN</h3>
<p> <code>True</code> for Cygwin. </p>
<p>Set to <code>true</code> when using Cygwin.  </p>
<h3>GHS-MULTI</h3>
<p>New in version 3.3. </p>
<p> <code>True</code> when using <code>Green Hills MULTI</code> generator.  </p>
<h3>IOS</h3>
<p>New in version 3.14. </p>
<p>Set to <code>1</code> when the target system (<code>CMAKE_SYSTEM_NAME</code>) is <code>iOS</code>.  </p>
<h3>MINGW</h3>
<p>New in version 3.2. </p>
<p> <code>True</code> when using MinGW </p>
<p>Set to <code>true</code> when the compiler is some version of MinGW.  </p>
<h3>MSVC</h3>
<p>Set to <code>true</code> when the compiler is some version of Microsoft Visual C++ or another compiler simulating the Visual C++ <code>cl</code> command-line syntax. </p>
<p>See also the <code>MSVC_VERSION</code> variable.  </p>
<h3>MSVC10</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v100</code> toolset (<code>cl</code> version 16) or another compiler that simulates it.  </p>
<h3>MSVC11</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v110</code> toolset (<code>cl</code> version 17) or another compiler that simulates it.  </p>
<h3>MSVC12</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v120</code> toolset (<code>cl</code> version 18) or another compiler that simulates it.  </p>
<h3>MSVC14</h3>
<p>New in version 3.1. </p>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v140</code> or <code>v141</code> toolset (<code>cl</code> version 19) or another compiler that simulates it.  </p>
<h3>MSVC60</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using Microsoft Visual C++ 6.0. </p>
<p>Set to <code>true</code> when the compiler is version 6.0 of Microsoft Visual C++.  </p>
<h3>MSVC70</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using Microsoft Visual C++ 7.0. </p>
<p>Set to <code>true</code> when the compiler is version 7.0 of Microsoft Visual C++.  </p>
<h3>MSVC71</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using Microsoft Visual C++ 7.1. </p>
<p>Set to <code>true</code> when the compiler is version 7.1 of Microsoft Visual C++.  </p>
<h3>MSVC80</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v80</code> toolset (<code>cl</code> version 14) or another compiler that simulates it.  </p>
<h3>MSVC90</h3>
<p>Discouraged. Use the <code>MSVC_VERSION</code> variable instead. </p>
<p> <code>True</code> when using the Microsoft Visual Studio <code>v90</code> toolset (<code>cl</code> version 15) or another compiler that simulates it.  </p>
<h3>MSVC_IDE</h3>
<p> <code>True</code> when using the Microsoft Visual C++ IDE. </p>
<p>Set to <code>true</code> when the target platform is the Microsoft Visual C++ IDE, as opposed to the command line compiler. </p>
<p> <code>NOTE:</code> This variable is only available after compiler detection has been performed, so it is not available to toolchain files or before the first <code>project()</code> or <code>enable_language()</code> call which uses an MSVC-like compiler.  </p>
<h3>MSVC_TOOLSET_VERSION</h3>
<p>New in version 3.12. </p>
<p>The toolset version of Microsoft Visual C/C++ being used if any. If MSVC-like is being used, this variable is set based on the version of the compiler as given by the <code>MSVC_VERSION</code> variable. </p>
<p>Known toolset version numbers are: </p>
<pre><code>80 = VS 2005 (8.0)
90 = VS 2008 (9.0)
100 = VS 2010 (10.0)
110 = VS 2012 (11.0)
120 = VS 2013 (12.0)
140 = VS 2015 (14.0)
141 = VS 2017 (15.0)
142 = VS 2019 (16.0)
</code></pre>
<p>Compiler versions newer than those known to CMake will be reported as the latest known toolset version. </p>
<p>See also the <code>MSVC_VERSION</code> variable.  </p>
<h3>MSVC_VERSION</h3>
<p>The version of Microsoft Visual C/C++ being used if any. If a compiler simulating Visual C++ is being used, this variable is set to the toolset version simulated as given by the <code>_MSC_VER</code> preprocessor definition. </p>
<p>Known version numbers are: </p>
<pre><code>1200 = VS 6.0
1300 = VS 7.0
1310 = VS 7.1
1400 = VS 8.0 (v80 toolset)
1500 = VS 9.0 (v90 toolset)
1600 = VS 10.0 (v100 toolset)
1700 = VS 11.0 (v110 toolset)
1800 = VS 12.0 (v120 toolset)
1900 = VS 14.0 (v140 toolset)
1910-1919 = VS 15.0 (v141 toolset)
1920-1929 = VS 16.0 (v142 toolset)
1930-1939 = VS 17.0 (v143 toolset)
</code></pre>
<p>See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> and <code>MSVC_TOOLSET_VERSION</code> variable.  </p>
<h3>MSYS</h3>
<p>New in version 3.14. </p>
<p> <code>True</code> when using the <code>MSYS Makefiles</code> generator.  </p>
<h3>UNIX</h3>
<p>Set to <code>True</code> when the target system is UNIX or UNIX-like (e.g. <code>APPLE</code> and <code>CYGWIN</code>). The <code>CMAKE_SYSTEM_NAME</code> variable should be queried if a more specific understanding of the target system is required.  </p>
<h3>WIN32</h3>
<p>Set to <code>True</code> when the target system is Windows, including Win64.  </p>
<h3>WINCE</h3>
<p>New in version 3.1. </p>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsCE</code>.  </p>
<h3>WINDOWS_PHONE</h3>
<p>New in version 3.1. </p>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsPhone</code>.  </p>
<h3>WINDOWS_STORE</h3>
<p>New in version 3.1. </p>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsStore</code>.  </p>
<h3>XCODE</h3>
<p>New in version 3.7. </p>
<p> <code>True</code> when using <code>Xcode</code> generator.  </p>
<h3>XCODE_VERSION</h3>
<p>Version of Xcode (<code>Xcode</code> generator only). </p>
<p>Under the <code>Xcode</code> generator, this is the version of Xcode as specified in <code>Xcode.app/Contents/version.plist</code> (such as <code>3.1.2</code>).  </p>
<h2>VARIABLES THAT CONTROL THE BUILD</h2>
<h3>CMAKE_AIX_EXPORT_ALL_SYMBOLS</h3>
<p>New in version 3.17. </p>
<p>Default value for <code>AIX_EXPORT_ALL_SYMBOLS</code> target property. This variable is used to initialize the property on each target as it is created.  </p>
<h3>CMAKE_ANDROID_ANT_ADDITIONAL_OPTIONS</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_ANT_ADDITIONAL_OPTIONS</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_API</h3>
<p>New in version 3.1. </p>
<p>When Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition, this variable may be set to specify the default value for the <code>ANDROID_API</code> target property. See that target property for additional information. </p>
<p>Otherwise, when Cross Compiling for Android, this variable provides the Android API version number targeted. This will be the same value as the <code>CMAKE_SYSTEM_VERSION</code> variable for <code>Android</code> platforms.  </p>
<h3>CMAKE_ANDROID_API_MIN</h3>
<p>New in version 3.2. </p>
<p>Default value for the <code>ANDROID_API_MIN</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_ARCH</h3>
<p>New in version 3.4. </p>
<p>When Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition, this variable may be set to specify the default value for the <code>ANDROID_ARCH</code> target property. See that target property for additional information. </p>
<p>Otherwise, when Cross Compiling for Android, this variable provides the name of the Android architecture corresponding to the value of the <code>CMAKE_ANDROID_ARCH_ABI</code> variable. The architecture name may be one of: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>arm</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>arm64</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>mips</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>mips64</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>x86</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>x86_64</code> </p>
 </dd></dl>
<h3>CMAKE_ANDROID_ARCH_ABI</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android, this variable specifies the target architecture and ABI to be used. Valid values are: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>arm64-v8a</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>armeabi-v7a</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>armeabi-v6</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>armeabi</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>mips</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>mips64</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>x86</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>x86_64</code> </p>
<p>See also the <code>CMAKE_ANDROID_ARM_MODE</code> and <code>CMAKE_ANDROID_ARM_NEON</code> variables. </p>
 </dd></dl>
<h3>CMAKE_ANDROID_ARM_MODE</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android and <code>CMAKE_ANDROID_ARCH_ABI</code> is set to one of the <code>armeabi</code> architectures, set <code>CMAKE_ANDROID_ARM_MODE</code> to <code>ON</code> to target 32-bit ARM processors (<code>-marm</code>). Otherwise, the default is to target the 16-bit Thumb processors (<code>-mthumb</code>).  </p>
<h3>CMAKE_ANDROID_ARM_NEON</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android and <code>CMAKE_ANDROID_ARCH_ABI</code> is set to <code>armeabi-v7a</code> set <code>CMAKE_ANDROID_ARM_NEON</code> to <code>ON</code> to target ARM NEON devices.  </p>
<h3>CMAKE_ANDROID_ASSETS_DIRECTORIES</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_ASSETS_DIRECTORIES</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_EXCEPTIONS</h3>
<p>New in version 3.20. </p>
<p>When Cross Compiling for Android with the NDK, this variable may be set to specify whether exceptions are enabled.  </p>
<h3>CMAKE_ANDROID_GUI</h3>
<p>New in version 3.1. </p>
<p>Default value for the <code>ANDROID_GUI</code> target property of executables. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_JAR_DEPENDENCIES</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_JAR_DEPENDENCIES</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_JAR_DIRECTORIES</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_JAR_DIRECTORIES</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_JAVA_SOURCE_DIR</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_JAVA_SOURCE_DIR</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_NATIVE_LIB_DEPENDENCIES</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_NATIVE_LIB_DEPENDENCIES</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_NATIVE_LIB_DIRECTORIES</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_NATIVE_LIB_DIRECTORIES</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_NDK</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android with the NDK, this variable holds the absolute path to the root directory of the NDK. The directory must contain a <code>platforms</code> subdirectory holding the <code>android-&lt;api&gt;</code> directories.  </p>
<h3>CMAKE_ANDROID_NDK_DEPRECATED_HEADERS</h3>
<p>New in version 3.9. </p>
<p>When Cross Compiling for Android with the NDK, this variable may be set to specify whether to use the deprecated per-api-level headers instead of the unified headers. </p>
<p>If not specified, the default will be <i>false</i> if using a NDK version that provides the unified headers and <i>true</i> otherwise.  </p>
<h3>CMAKE_ANDROID_NDK_TOOLCHAIN_HOST_TAG</h3>
<p>New in version 3.7.1. </p>
<p>When Cross Compiling for Android with the NDK, this variable provides the NDK&#8217;s &quot;host tag&quot; used to construct the path to prebuilt toolchains that run on the host.  </p>
<h3>CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android with the NDK, this variable may be set to specify the version of the toolchain to be used as the compiler. </p>
<p>On NDK r19 or above, this variable must be unset or set to <code>clang</code>. </p>
<p>On NDK r18 or below, this variable must be set to one of these forms: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&lt;major&gt;.&lt;minor&gt;</code>: GCC of specified version </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>clang&lt;major&gt;.&lt;minor&gt;</code>: Clang of specified version </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>clang</code>: Clang of most recent available version </p>
<p>A toolchain of the requested version will be selected automatically to match the ABI named in the <code>CMAKE_ANDROID_ARCH_ABI</code> variable. </p>
<p>If not specified, the default will be a value that selects the latest available GCC toolchain. </p>
 </dd></dl>
<h3>CMAKE_ANDROID_PROCESS_MAX</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_PROCESS_MAX</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_PROGUARD</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_PROGUARD</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_PROGUARD_CONFIG_PATH</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_PROGUARD_CONFIG_PATH</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_RTTI</h3>
<p>New in version 3.20. </p>
<p>When Cross Compiling for Android with the NDK, this variable may be set to specify whether RTTI is enabled.  </p>
<h3>CMAKE_ANDROID_SECURE_PROPS_PATH</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_SECURE_PROPS_PATH</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_SKIP_ANT_STEP</h3>
<p>New in version 3.4. </p>
<p>Default value for the <code>ANDROID_SKIP_ANT_STEP</code> target property. See that target property for additional information.  </p>
<h3>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android with a Standalone Toolchain, this variable holds the absolute path to the root directory of the toolchain. The specified directory must contain a <code>sysroot</code> subdirectory.  </p>
<h3>CMAKE_ANDROID_STL_TYPE</h3>
<p>New in version 3.4. </p>
<p>When Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition, this variable may be set to specify the default value for the <code>ANDROID_STL_TYPE</code> target property. See that target property for additional information. </p>
<p>When Cross Compiling for Android with the NDK, this variable may be set to specify the STL variant to be used. The value may be one of: </p>
<dl>
<dt><code>none</code></dt>
<dd> <p> No C++ Support </p>
 </dd>
<dt><code>system</code></dt>
<dd> <p> Minimal C++ without STL </p>
 </dd>
<dt><code>gabi++_static</code></dt>
<dd> <p> GAbi++ Static </p>
 </dd>
<dt><code>gabi++_shared</code></dt>
<dd> <p> GAbi++ Shared </p>
 </dd>
<dt><code>gnustl_static</code></dt>
<dd> <p> GNU libstdc++ Static </p>
 </dd>
<dt><code>gnustl_shared</code></dt>
<dd> <p> GNU libstdc++ Shared </p>
 </dd>
<dt><code>c++_static</code></dt>
<dd> <p> LLVM libc++ Static </p>
 </dd>
<dt><code>c++_shared</code></dt>
<dd> <p> LLVM libc++ Shared </p>
 </dd>
<dt><code>stlport_static</code></dt>
<dd> <p> STLport Static </p>
 </dd>
<dt><code>stlport_shared</code></dt>
<dd> <p> STLport Shared </p>
<p>The default value is <code>gnustl_static</code> on NDK versions that provide it and otherwise <code>c++_static</code>. Note that this default differs from the native NDK build system because CMake may be used to build projects for Android that are not natively implemented for it and use the C++ standard library. </p>
 </dd></dl>
<h3>CMAKE_APPLE_SILICON_PROCESSOR</h3>
<p>New in version 3.19.2. </p>
<p>On Apple Silicon hosts running macOS, set this variable to tell CMake what architecture to use for <code>CMAKE_HOST_SYSTEM_PROCESSOR</code>. The value must be either <code>arm64</code> or <code>x86_64</code>. </p>
<p>The value of this variable should never be modified by project code. It is meant to be set as a cache entry provided by the user, e.g. via <code>-DCMAKE_APPLE_SILICON_PROCESSOR=...</code>. </p>
<p>See also the <code>CMAKE_APPLE_SILICON_PROCESSOR</code> environment variable.  </p>
<h3>CMAKE_ARCHIVE_OUTPUT_DIRECTORY</h3>
<p>Where to put all the ARCHIVE target files when built. </p>
<p>This variable is used to initialize the <code>ARCHIVE_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>New in version 3.3. </p>
<p>Where to put all the ARCHIVE target files when built for a specific configuration. </p>
<p>This variable is used to initialize the <code>ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_AUTOGEN_ORIGIN_DEPENDS</h3>
<p>New in version 3.14. </p>
<p>Switch for forwarding origin target dependencies to the corresponding <code>_autogen</code> targets. </p>
<p>This variable is used to initialize the <code>AUTOGEN_ORIGIN_DEPENDS</code> property on all the targets. See that target property for additional information. </p>
<p>By default <i>CMAKE_AUTOGEN_ORIGIN_DEPENDS</i> is <code>ON</code>.  </p>
<h3>CMAKE_AUTOGEN_PARALLEL</h3>
<p>New in version 3.11. </p>
<p>Number of parallel <code>moc</code> or <code>uic</code> processes to start when using <code>AUTOMOC</code> and <code>AUTOUIC</code>. </p>
<p>This variable is used to initialize the <code>AUTOGEN_PARALLEL</code> property on all the targets. See that target property for additional information. </p>
<p>By default <i>CMAKE_AUTOGEN_PARALLEL</i> is unset.  </p>
<h3>CMAKE_AUTOGEN_VERBOSE</h3>
<p>New in version 3.13. </p>
<p>Sets the verbosity of <code>AUTOMOC</code>, <code>AUTOUIC</code> and <code>AUTORCC</code>. A positive integer value or a true boolean value lets the <code>AUTO*</code> generators output additional processing information. </p>
<p>Setting <i>CMAKE_AUTOGEN_VERBOSE</i> has the same effect as setting the <code>VERBOSE</code> environment variable during generation (e.g. by calling <code>make VERBOSE=1</code>). The extra verbosity is limited to the <code>AUTO*</code> generators though. </p>
<p>By default <i>CMAKE_AUTOGEN_VERBOSE</i> is unset.  </p>
<h3>CMAKE_AUTOMOC</h3>
<p>Whether to handle <code>moc</code> automatically for Qt targets. </p>
<p>This variable is used to initialize the <code>AUTOMOC</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_AUTOMOC_COMPILER_PREDEFINES</h3>
<p>New in version 3.10. </p>
<p>This variable is used to initialize the <code>AUTOMOC_COMPILER_PREDEFINES</code> property on all the targets. See that target property for additional information. </p>
<p>By default it is ON.  </p>
<h3>CMAKE_AUTOMOC_DEPEND_FILTERS</h3>
<p>New in version 3.9. </p>
<p>Filter definitions used by <code>CMAKE_AUTOMOC</code> to extract file names from source code as additional dependencies for the <code>moc</code> file. </p>
<p>This variable is used to initialize the <code>AUTOMOC_DEPEND_FILTERS</code> property on all the targets. See that target property for additional information. </p>
<p>By default it is empty.  </p>
<h3>CMAKE_AUTOMOC_MACRO_NAMES</h3>
<p>New in version 3.10. </p>
<p>Semicolon-separated list list of macro names used by <code>CMAKE_AUTOMOC</code> to determine if a C++ file needs to be processed by <code>moc</code>. </p>
<p>This variable is used to initialize the <code>AUTOMOC_MACRO_NAMES</code> property on all the targets. See that target property for additional information. </p>
<p>The default value is <code>Q_OBJECT;Q_GADGET;Q_NAMESPACE;Q_NAMESPACE_EXPORT</code>.  </p>
<h3>Example</h3>
<p>Let CMake know that source files that contain <code>CUSTOM_MACRO</code> must be <code>moc</code> processed as well: </p>
<pre><code>set(CMAKE_AUTOMOC ON)
list(APPEND CMAKE_AUTOMOC_MACRO_NAMES &quot;CUSTOM_MACRO&quot;)
</code></pre>
<h3>CMAKE_AUTOMOC_MOC_OPTIONS</h3>
<p>Additional options for <code>moc</code> when using <code>CMAKE_AUTOMOC</code>. </p>
<p>This variable is used to initialize the <code>AUTOMOC_MOC_OPTIONS</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_AUTOMOC_PATH_PREFIX</h3>
<p>New in version 3.16. </p>
<p>Whether to generate the <code>-p</code> path prefix option for <code>moc</code> on <code>AUTOMOC</code> enabled Qt targets. </p>
<p>This variable is used to initialize the <code>AUTOMOC_PATH_PREFIX</code> property on all the targets. See that target property for additional information. </p>
<p>The default value is <code>OFF</code>.  </p>
<h3>CMAKE_AUTORCC</h3>
<p>Whether to handle <code>rcc</code> automatically for Qt targets. </p>
<p>This variable is used to initialize the <code>AUTORCC</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_AUTORCC_OPTIONS</h3>
<p>Additional options for <code>rcc</code> when using <code>CMAKE_AUTORCC</code>. </p>
<p>This variable is used to initialize the <code>AUTORCC_OPTIONS</code> property on all the targets. See that target property for additional information.  </p>
<h3>EXAMPLE</h3>
<pre><code># ...
set(CMAKE_AUTORCC_OPTIONS &quot;--compress;9&quot;)
# ...
</code></pre>
<h3>CMAKE_AUTOUIC</h3>
<p>Whether to handle <code>uic</code> automatically for Qt targets. </p>
<p>This variable is used to initialize the <code>AUTOUIC</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_AUTOUIC_OPTIONS</h3>
<p>Additional options for <code>uic</code> when using <code>CMAKE_AUTOUIC</code>. </p>
<p>This variable is used to initialize the <code>AUTOUIC_OPTIONS</code> property on all the targets. See that target property for additional information.  </p>
<h3>EXAMPLE</h3>
<pre><code># ...
set_property(CMAKE_AUTOUIC_OPTIONS &quot;--no-protection&quot;)
# ...
</code></pre>
<h3>CMAKE_AUTOUIC_SEARCH_PATHS</h3>
<p>New in version 3.9. </p>
<p>Search path list used by <code>CMAKE_AUTOUIC</code> to find included <code>.ui</code> files. </p>
<p>This variable is used to initialize the <code>AUTOUIC_SEARCH_PATHS</code> property on all the targets. See that target property for additional information. </p>
<p>By default it is empty.  </p>
<h3>CMAKE_BUILD_RPATH</h3>
<p>New in version 3.8. </p>
<p>Semicolon-separated list specifying runtime path (<code>RPATH</code>) entries to add to binaries linked in the build tree (for platforms that support it). The entries will <i>not</i> be used for binaries in the install tree. See also the <code>CMAKE_INSTALL_RPATH</code> variable. </p>
<p>This is used to initialize the <code>BUILD_RPATH</code> target property for all targets.  </p>
<h3>CMAKE_BUILD_RPATH_USE_ORIGIN</h3>
<p>New in version 3.14. </p>
<p>Whether to use relative paths for the build <code>RPATH</code>. </p>
<p>This is used to initialize the <code>BUILD_RPATH_USE_ORIGIN</code> target property for all targets, see that property for more details.  </p>
<h3>CMAKE_BUILD_WITH_INSTALL_NAME_DIR</h3>
<p>New in version 3.9. </p>
<p>Whether to use <code>INSTALL_NAME_DIR</code> on targets in the build tree. </p>
<p>This variable is used to initialize the <code>BUILD_WITH_INSTALL_NAME_DIR</code> property on all targets.  </p>
<h3>CMAKE_BUILD_WITH_INSTALL_RPATH</h3>
<p>Use the install path for the <code>RPATH</code>. </p>
<p>Normally CMake uses the build tree for the <code>RPATH</code> when building executables etc on systems that use <code>RPATH</code>. When the software is installed the executables etc are relinked by CMake to have the install <code>RPATH</code>. If this variable is set to true then the software is always built with the install path for the <code>RPATH</code> and does not need to be relinked when installed.  </p>
<h3>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY</h3>
<p>New in version 3.1. </p>
<p>Output directory for MS debug symbol <code>.pdb</code> files generated by the compiler while building source files. </p>
<p>This variable is used to initialize the <code>COMPILE_PDB_OUTPUT_DIRECTORY</code> property on all the targets.  </p>
<h3>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>New in version 3.1. </p>
<p>Per-configuration output directory for MS debug symbol <code>.pdb</code> files generated by the compiler while building source files. </p>
<p>This is a per-configuration version of <code>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY</code>. This variable is used to initialize the <code>COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets.  </p>
<h3>CMAKE_&lt;CONFIG&gt;_POSTFIX</h3>
<p>Default filename postfix for libraries under configuration <code>&lt;CONFIG&gt;</code>. </p>
<p>When a non-executable target is created its <code>&lt;CONFIG&gt;_POSTFIX</code> target property is initialized with the value of this variable if it is set.  </p>
<h3>CMAKE_CROSS_CONFIGS</h3>
<p>New in version 3.17. </p>
<p>Specifies a semicolon-separated list of configurations available from all <code>build-&lt;Config&gt;.ninja</code> files in the <code>Ninja Multi-Config</code> generator. This variable activates cross-config mode. Targets from each config specified in this variable can be built from any <code>build-&lt;Config&gt;.ninja</code> file. Custom commands will use the configuration native to <code>build-&lt;Config&gt;.ninja</code>. If it is set to <code>all</code>, all configurations from <code>CMAKE_CONFIGURATION_TYPES</code> are cross-configs. If it is not specified, or empty, each <code>build-&lt;Config&gt;.ninja</code> file will only contain build rules for its own configuration. </p>
<p>The value of this variable must be a subset of <code>CMAKE_CONFIGURATION_TYPES</code>.  </p>
<h3>CMAKE_CTEST_ARGUMENTS</h3>
<p>New in version 3.17. </p>
<p>Set this to a semicolon-separated list of command-line arguments to pass to <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> when running tests through the <code>test</code> (or <code>RUN_TESTS</code>) target of the generated build system.  </p>
<h3>CMAKE_CUDA_RESOLVE_DEVICE_SYMBOLS</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>CUDA_RESOLVE_DEVICE_SYMBOLS</code> target property. This variable is used to initialize the property on each target as it is created.  </p>
<h3>CMAKE_CUDA_RUNTIME_LIBRARY</h3>
<p>New in version 3.17. </p>
<p>Select the CUDA runtime library for use when compiling and linking CUDA. This variable is used to initialize the <code>CUDA_RUNTIME_LIBRARY</code> property on all targets as they are created. </p>
<p>The allowed case insensitive values are: </p>
<dl>
<dt><code>None</code></dt>
<dd> <p> Link with <code>-cudart=none</code> or equivalent flag(s) to use no CUDA runtime library. </p>
 </dd>
<dt><code>Shared</code></dt>
<dd> <p> Link with <code>-cudart=shared</code> or equivalent flag(s) to use a dynamically-linked CUDA runtime library. </p>
 </dd>
<dt><code>Static</code></dt>
<dd> <p> Link with <code>-cudart=static</code> or equivalent flag(s) to use a statically-linked CUDA runtime library. </p>
<p>Contents of <code>CMAKE_CUDA_RUNTIME_LIBRARY</code> may use <code>generator expressions</code>. </p>
<p>If this variable is not set then the <code>CUDA_RUNTIME_LIBRARY</code> target property will not be set automatically. If that property is not set then CMake uses an appropriate default value based on the compiler to select the CUDA runtime library. </p>
<p> <code>NOTE:</code> This property has effect only when the <code>CUDA</code> language is enabled. To control the CUDA runtime linking when only using the CUDA SDK with the <code>C</code> or <code>C++</code> language we recommend using the <code>FindCUDAToolkit</code> module. </p>
 </dd></dl>
<h3>CMAKE_CUDA_SEPARABLE_COMPILATION</h3>
<p>New in version 3.11. </p>
<p>Default value for <code>CUDA_SEPARABLE_COMPILATION</code> target property. This variable is used to initialize the property on each target as it is created.  </p>
<h3>CMAKE_DEBUG_POSTFIX</h3>
<p>See variable <code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code>. </p>
<p>This variable is a special case of the more-general <code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code> variable for the <i>DEBUG</i> configuration.  </p>
<h3>CMAKE_DEFAULT_BUILD_TYPE</h3>
<p>New in version 3.17. </p>
<p>Specifies the configuration to use by default in a <code>build.ninja</code> file in the <code>Ninja Multi-Config</code> generator. If this variable is specified, <code>build.ninja</code> uses build rules from <code>build-&lt;Config&gt;.ninja</code> by default. All custom commands are executed with this configuration. If the variable is not specified, the first item from <code>CMAKE_CONFIGURATION_TYPES</code> is used instead. </p>
<p>The value of this variable must be one of the items from <code>CMAKE_CONFIGURATION_TYPES</code>.  </p>
<h3>CMAKE_DEFAULT_CONFIGS</h3>
<p>New in version 3.17. </p>
<p>Specifies a semicolon-separated list of configurations to build for a target in <code>build.ninja</code> if no <code>:&lt;Config&gt;</code> suffix is specified in the <code>Ninja Multi-Config</code> generator. If it is set to <code>all</code>, all configurations from <code>CMAKE_CROSS_CONFIGS</code> are used. If it is not specified, it defaults to <code>CMAKE_DEFAULT_BUILD_TYPE</code>. </p>
<p>For example, if you set <code>CMAKE_DEFAULT_BUILD_TYPE</code> to <code>Release</code>, but set <i>CMAKE_DEFAULT_CONFIGS</i> to <code>Debug</code> or <code>all</code>, all <code>&lt;target&gt;</code> aliases in <code>build.ninja</code> will resolve to <code>&lt;target&gt;:Debug</code> or <code>&lt;target&gt;:all</code>, but custom commands will still use the <code>Release</code> configuration. </p>
<p>The value of this variable must be a subset of <code>CMAKE_CROSS_CONFIGS</code> or be the same as <code>CMAKE_DEFAULT_BUILD_TYPE</code>. It must not be specified if <code>CMAKE_DEFAULT_BUILD_TYPE</code> or <code>CMAKE_CROSS_CONFIGS</code> is not used.  </p>
<h3>CMAKE_DISABLE_PRECOMPILE_HEADERS</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>DISABLE_PRECOMPILE_HEADERS</code> of targets. </p>
<p>By default <code>CMAKE_DISABLE_PRECOMPILE_HEADERS</code> is <code>OFF</code>.  </p>
<h3>CMAKE_DEPENDS_USE_COMPILER</h3>
<p>New in version 3.20. </p>
<p>For the Makefile Generators, source dependencies are now, for a selection of compilers, generated by the compiler itself. By defining this variable with value <code>FALSE</code>, you can restore the legacy behavior (i.e. using <code>CMake</code> for dependencies discovery).  </p>
<h3>CMAKE_ENABLE_EXPORTS</h3>
<p>New in version 3.4. </p>
<p>Specify whether executables export symbols for loadable modules. </p>
<p>This variable is used to initialize the <code>ENABLE_EXPORTS</code> target property for executable targets when they are created by calls to the <code>add_executable()</code> command. See the property documentation for details.  </p>
<h3>CMAKE_EXE_LINKER_FLAGS</h3>
<p>Linker flags to be used to create executables. </p>
<p>These flags will be used by the linker when creating an executable.  </p>
<h3>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking an executable. </p>
<p>Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating executables.  </p>
<h3>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also <code>CMAKE_EXE_LINKER_FLAGS_INIT</code>.  </p>
<h3>CMAKE_EXE_LINKER_FLAGS_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_EXE_LINKER_FLAGS</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also the configuration-specific variable <code>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</code>.  </p>
<h3>CMAKE_FOLDER</h3>
<p>New in version 3.12. </p>
<p>Set the folder name. Use to organize targets in an IDE. </p>
<p>This variable is used to initialize the <code>FOLDER</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_FRAMEWORK</h3>
<p>New in version 3.15. </p>
<p>Default value for <code>FRAMEWORK</code> of targets. </p>
<p>This variable is used to initialize the <code>FRAMEWORK</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_FRAMEWORK_MULTI_CONFIG_POSTFIX_&lt;CONFIG&gt;</h3>
<p>New in version 3.18. </p>
<p>Default framework filename postfix under configuration <code>&lt;CONFIG&gt;</code> when using a multi-config generator. </p>
<p>When a framework target is created its <code>FRAMEWORK_MULTI_CONFIG_POSTFIX_&lt;CONFIG&gt;</code> target property is initialized with the value of this variable if it is set.  </p>
<h3>CMAKE_Fortran_FORMAT</h3>
<p>Set to <code>FIXED</code> or <code>FREE</code> to indicate the Fortran source layout. </p>
<p>This variable is used to initialize the <code>Fortran_FORMAT</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_Fortran_MODULE_DIRECTORY</h3>
<p>Fortran module output directory. </p>
<p>This variable is used to initialize the <code>Fortran_MODULE_DIRECTORY</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_Fortran_PREPROCESS</h3>
<p>New in version 3.18. </p>
<p>Default value for <code>Fortran_PREPROCESS</code> of targets. </p>
<p>This variable is used to initialize the <code>Fortran_PREPROCESS</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_GHS_NO_SOURCE_GROUP_FILE</h3>
<p>New in version 3.14. </p>
<p> <code>ON</code> / <code>OFF</code> boolean to control if the project file for a target should be one single file or multiple files. Refer to <code>GHS_NO_SOURCE_GROUP_FILE</code> for further details.  </p>
<h3>CMAKE_GLOBAL_AUTOGEN_TARGET</h3>
<p>New in version 3.14. </p>
<p>Switch to enable generation of a global <code>autogen</code> target. </p>
<p>When <i>CMAKE_GLOBAL_AUTOGEN_TARGET</i> is enabled, a custom target <code>autogen</code> is generated. This target depends on all <code>AUTOMOC</code> and <code>AUTOUIC</code> generated <code>&lt;ORIGIN&gt;_autogen</code> targets in the project. By building the global <code>autogen</code> target, all <code>AUTOMOC</code> and <code>AUTOUIC</code> files in the project will be generated. </p>
<p>The name of the global <code>autogen</code> target can be changed by setting <code>CMAKE_GLOBAL_AUTOGEN_TARGET_NAME</code>. </p>
<p>By default <i>CMAKE_GLOBAL_AUTOGEN_TARGET</i> is unset. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code> manual for more information on using CMake with Qt.  </p>
<h3>Note</h3>
<p> <code>&lt;ORIGIN&gt;_autogen</code> targets by default inherit their origin target&#8217;s dependencies. This might result in unintended dependency target builds when only <code>&lt;ORIGIN&gt;_autogen</code> targets are built. A solution is to disable <code>AUTOGEN_ORIGIN_DEPENDS</code> on the respective origin targets.  </p>
<h3>CMAKE_GLOBAL_AUTOGEN_TARGET_NAME</h3>
<p>New in version 3.14. </p>
<p>Change the name of the global <code>autogen</code> target. </p>
<p>When <code>CMAKE_GLOBAL_AUTOGEN_TARGET</code> is enabled, a global custom target named <code>autogen</code> is created. <i>CMAKE_GLOBAL_AUTOGEN_TARGET_NAME</i> allows to set a different name for that target. </p>
<p>By default <i>CMAKE_GLOBAL_AUTOGEN_TARGET_NAME</i> is unset. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code> manual for more information on using CMake with Qt.  </p>
<h3>CMAKE_GLOBAL_AUTORCC_TARGET</h3>
<p>New in version 3.14. </p>
<p>Switch to enable generation of a global <code>autorcc</code> target. </p>
<p>When <i>CMAKE_GLOBAL_AUTORCC_TARGET</i> is enabled, a custom target <code>autorcc</code> is generated. This target depends on all <code>AUTORCC</code> generated <code>&lt;ORIGIN&gt;_arcc_&lt;QRC&gt;</code> targets in the project. By building the global <code>autorcc</code> target, all <code>AUTORCC</code> files in the project will be generated. </p>
<p>The name of the global <code>autorcc</code> target can be changed by setting <code>CMAKE_GLOBAL_AUTORCC_TARGET_NAME</code>. </p>
<p>By default <i>CMAKE_GLOBAL_AUTORCC_TARGET</i> is unset. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code> manual for more information on using CMake with Qt.  </p>
<h3>CMAKE_GLOBAL_AUTORCC_TARGET_NAME</h3>
<p>New in version 3.14. </p>
<p>Change the name of the global <code>autorcc</code> target. </p>
<p>When <code>CMAKE_GLOBAL_AUTORCC_TARGET</code> is enabled, a global custom target named <code>autorcc</code> is created. <i>CMAKE_GLOBAL_AUTORCC_TARGET_NAME</i> allows to set a different name for that target. </p>
<p>By default <code>CMAKE_GLOBAL_AUTOGEN_TARGET_NAME</code> is unset. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-qt/">cmake-qt</a>(7)</code> manual for more information on using CMake with Qt.  </p>
<h3>CMAKE_GNUtoMS</h3>
<p>Convert GNU import libraries (<code>.dll.a</code>) to MS format (<code>.lib</code>). </p>
<p>This variable is used to initialize the <code>GNUtoMS</code> property on targets when they are created. See that target property for additional information.  </p>
<h3>CMAKE_INCLUDE_CURRENT_DIR</h3>
<p>Automatically add the current source and build directories to the include path. </p>
<p>If this variable is enabled, CMake automatically adds <code>CMAKE_CURRENT_SOURCE_DIR</code> and <code>CMAKE_CURRENT_BINARY_DIR</code> to the include path for each directory. These additional include directories do not propagate down to subdirectories. This is useful mainly for out-of-source builds, where files generated into the build tree are included by files located in the source tree. </p>
<p>By default <code>CMAKE_INCLUDE_CURRENT_DIR</code> is <code>OFF</code>.  </p>
<h3>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</h3>
<p>Automatically add the current source and build directories to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property. </p>
<p>If this variable is enabled, CMake automatically adds for each shared library target, static library target, module target and executable target, <code>CMAKE_CURRENT_SOURCE_DIR</code> and <code>CMAKE_CURRENT_BINARY_DIR</code> to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property. By default <code>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</code> is <code>OFF</code>.  </p>
<h3>CMAKE_INSTALL_NAME_DIR</h3>
<p>Directory name for installed targets on Apple platforms. </p>
<p> <code>CMAKE_INSTALL_NAME_DIR</code> is used to initialize the <code>INSTALL_NAME_DIR</code> property on all targets. See that target property for more information.  </p>
<h3>CMAKE_INSTALL_REMOVE_ENVIRONMENT_RPATH</h3>
<p>New in version 3.16. </p>
<p>Sets the default for whether toolchain-defined rpaths should be removed during installation. </p>
<p> <code>CMAKE_INSTALL_REMOVE_ENVIRONMENT_RPATH</code> is a boolean that provides the default value for the <code>INSTALL_REMOVE_ENVIRONMENT_RPATH</code> property of all subsequently created targets.  </p>
<h3>CMAKE_INSTALL_RPATH</h3>
<p>The rpath to use for installed targets. </p>
<p>A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This is used to initialize the target property <code>INSTALL_RPATH</code> for all targets.  </p>
<h3>CMAKE_INSTALL_RPATH_USE_LINK_PATH</h3>
<p>Add paths to linker search and installed rpath. </p>
<p> <code>CMAKE_INSTALL_RPATH_USE_LINK_PATH</code> is a boolean that if set to <code>True</code> will append to the runtime search path (rpath) of installed binaries any directories outside the project that are in the linker search path or contain linked library files. The directories are appended after the value of the <code>INSTALL_RPATH</code> target property. </p>
<p>This variable is used to initialize the target property <code>INSTALL_RPATH_USE_LINK_PATH</code> for all targets.  </p>
<h3>CMAKE_INTERPROCEDURAL_OPTIMIZATION</h3>
<p>New in version 3.9. </p>
<p>Default value for <code>INTERPROCEDURAL_OPTIMIZATION</code> of targets. </p>
<p>This variable is used to initialize the <code>INTERPROCEDURAL_OPTIMIZATION</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_INTERPROCEDURAL_OPTIMIZATION_&lt;CONFIG&gt;</h3>
<p>New in version 3.9. </p>
<p>Default value for <code>INTERPROCEDURAL_OPTIMIZATION_&lt;CONFIG&gt;</code> of targets. </p>
<p>This variable is used to initialize the <code>INTERPROCEDURAL_OPTIMIZATION_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_IOS_INSTALL_COMBINED</h3>
<p>New in version 3.5. </p>
<p>Default value for <code>IOS_INSTALL_COMBINED</code> of targets. </p>
<p>This variable is used to initialize the <code>IOS_INSTALL_COMBINED</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_&lt;LANG&gt;_CLANG_TIDY</h3>
<p>New in version 3.6. </p>
<p>Default value for <code>&lt;LANG&gt;_CLANG_TIDY</code> target property when <code>&lt;LANG&gt;</code> is <code>C</code>, <code>CXX</code>, <code>OBJC</code> or <code>OBJCXX</code>. </p>
<p>This variable is used to initialize the property on each target as it is created. For example: </p>
<pre><code>set(CMAKE_CXX_CLANG_TIDY clang-tidy -checks=-*,readability-*)
add_executable(foo foo.cxx)
</code></pre>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</h3>
<p>New in version 3.4. </p>
<p>Default value for <code>&lt;LANG&gt;_COMPILER_LAUNCHER</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code>, <code>CXX</code>, <code>Fortran</code>, <code>HIP</code>, <code>ISPC</code>, <code>OBJC</code>, <code>OBJCXX</code>, or <code>CUDA</code>. </p>
<p>This variable is initialized to the <code>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</code> environment variable if it is set.  </p>
<h3>CMAKE_&lt;LANG&gt;_CPPCHECK</h3>
<p>New in version 3.10. </p>
<p>Default value for <code>&lt;LANG&gt;_CPPCHECK</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_CPPLINT</h3>
<p>New in version 3.8. </p>
<p>Default value for <code>&lt;LANG&gt;_CPPLINT</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</h3>
<p>New in version 3.3. </p>
<p>Default value for <code>&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_LAUNCHER</h3>
<p>New in version 3.21. </p>
<p>Default value for <code>&lt;LANG&gt;_LINKER_LAUNCHER</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code>, <code>CXX</code>, <code>OBJC</code>, or <code>OBJCXX</code>. </p>
<p>This variable is initialized to the <code>CMAKE_&lt;LANG&gt;_LINKER_LAUNCHER</code> environment variable if it is set.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINK_LIBRARY_FILE_FLAG</h3>
<p>New in version 3.16. </p>
<p>Language-specific flag to be used to link a library specified by a path to its file. </p>
<p>The flag will be used before a library file path is given to the linker. This is needed only on very few platforms.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINK_LIBRARY_FLAG</h3>
<p>New in version 3.16. </p>
<p>Flag to be used to link a library into a shared library or executable. </p>
<p>This flag will be used to specify a library to link to a shared library or an executable for the specific language. On most compilers this is <code>-l</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINK_WHAT_YOU_USE_FLAG</h3>
<p>New in version 3.22. </p>
<p>Linker flag to be used to configure linker so that all specified libraries on the command line will be linked into the target. </p>
<p>See also variable <code>CMAKE_LINK_WHAT_YOU_USE_CHECK</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_VISIBILITY_PRESET</h3>
<p>Default value for the <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> target property when a target is created.  </p>
<h3>CMAKE_LIBRARY_OUTPUT_DIRECTORY</h3>
<p>Where to put all the LIBRARY target files when built. </p>
<p>This variable is used to initialize the <code>LIBRARY_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>New in version 3.3. </p>
<p>Where to put all the LIBRARY target files when built for a specific configuration. </p>
<p>This variable is used to initialize the <code>LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_LIBRARY_PATH_FLAG</h3>
<p>The flag to be used to add a library search path to a compiler. </p>
<p>The flag will be used to specify a library directory to the compiler. On most compilers this is <code>-L</code>.  </p>
<h3>CMAKE_LINK_DEF_FILE_FLAG</h3>
<p>Linker flag to be used to specify a <code>.def</code> file for dll creation. </p>
<p>The flag will be used to add a <code>.def</code> file when creating a dll on Windows; this is only defined on Windows.  </p>
<h3>CMAKE_LINK_DEPENDS_NO_SHARED</h3>
<p>Whether to skip link dependencies on shared library files. </p>
<p>This variable initializes the <code>LINK_DEPENDS_NO_SHARED</code> property on targets when they are created. See that target property for additional information.  </p>
<h3>CMAKE_LINK_INTERFACE_LIBRARIES</h3>
<p>Default value for <code>LINK_INTERFACE_LIBRARIES</code> of targets. </p>
<p>This variable is used to initialize the <code>LINK_INTERFACE_LIBRARIES</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_LINK_LIBRARY_FILE_FLAG</h3>
<p>Flag to be used to link a library specified by a path to its file. </p>
<p>The flag will be used before a library file path is given to the linker. This is needed only on very few platforms.  </p>
<h3>CMAKE_LINK_LIBRARY_FLAG</h3>
<p>Flag to be used to link a library into an executable. </p>
<p>The flag will be used to specify a library to link to an executable. On most compilers this is <code>-l</code>.  </p>
<h3>CMAKE_LINK_WHAT_YOU_USE</h3>
<p>New in version 3.7. </p>
<p>Default value for <code>LINK_WHAT_YOU_USE</code> target property. This variable is used to initialize the property on each target as it is created.  </p>
<h3>CMAKE_LINK_WHAT_YOU_USE_CHECK</h3>
<p>New in version 3.22. </p>
<p>Defines the command executed after the link step to check libraries usage. This check is currently only defined on <code>ELF</code> platforms with value <code>ldd -u -r</code>. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_LINK_WHAT_YOU_USE_FLAG</code> variables.  </p>
<h3>CMAKE_MACOSX_BUNDLE</h3>
<p>Default value for <code>MACOSX_BUNDLE</code> of targets. </p>
<p>This variable is used to initialize the <code>MACOSX_BUNDLE</code> property on all the targets. See that target property for additional information. </p>
<p>This variable is set to <code>ON</code> by default if <code>CMAKE_SYSTEM_NAME</code> equals to iOS, tvOS or watchOS.  </p>
<h3>CMAKE_MACOSX_RPATH</h3>
<p>Whether to use rpaths on macOS and iOS. </p>
<p>This variable is used to initialize the <code>MACOSX_RPATH</code> property on all targets.  </p>
<h3>CMAKE_MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</h3>
<p>Default value for <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> of targets. </p>
<p>This variable is used to initialize the <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_MODULE_LINKER_FLAGS</h3>
<p>Linker flags to be used to create modules. </p>
<p>These flags will be used by the linker when creating a module.  </p>
<h3>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking a module. </p>
<p>Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating modules.  </p>
<h3>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also <code>CMAKE_MODULE_LINKER_FLAGS_INIT</code>.  </p>
<h3>CMAKE_MODULE_LINKER_FLAGS_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_MODULE_LINKER_FLAGS</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also the configuration-specific variable <code>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</code>.  </p>
<h3>CMAKE_MSVCIDE_RUN_PATH</h3>
<p>New in version 3.10. </p>
<p>Extra PATH locations that should be used when executing <code>add_custom_command()</code> or <code>add_custom_target()</code> when using the <code>Visual Studio 9 2008</code> (or above) generator. This allows for running commands and using dll&#8217;s that the IDE environment is not aware of. </p>
<p>If not set explicitly the value is initialized by the <code>CMAKE_MSVCIDE_RUN_PATH</code> environment variable, if set, and otherwise left empty.  </p>
<h3>CMAKE_MSVC_RUNTIME_LIBRARY</h3>
<p>New in version 3.15. </p>
<p>Select the MSVC runtime library for use by compilers targeting the MSVC ABI. This variable is used to initialize the <code>MSVC_RUNTIME_LIBRARY</code> property on all targets as they are created. It is also propagated by calls to the <code>try_compile()</code> command into the test project. </p>
<p>The allowed values are: </p>
<dl>
<dt><code>MultiThreaded</code></dt>
<dd> <p> Compile with <code>-MT</code> or equivalent flag(s) to use a multi-threaded statically-linked runtime library. </p>
 </dd>
<dt><code>MultiThreadedDLL</code></dt>
<dd> <p> Compile with <code>-MD</code> or equivalent flag(s) to use a multi-threaded dynamically-linked runtime library. </p>
 </dd>
<dt><code>MultiThreadedDebug</code></dt>
<dd> <p> Compile with <code>-MTd</code> or equivalent flag(s) to use a multi-threaded statically-linked runtime library. </p>
 </dd>
<dt><code>MultiThreadedDebugDLL</code></dt>
<dd> <p> Compile with <code>-MDd</code> or equivalent flag(s) to use a multi-threaded dynamically-linked runtime library. </p>
<p>The value is ignored on non-MSVC compilers but an unsupported value will be rejected as an error when using a compiler targeting the MSVC ABI. </p>
<p>The value may also be the empty string (<code>&quot;&quot;</code>) in which case no runtime library selection flag will be added explicitly by CMake. Note that with Visual Studio Generators the native build system may choose to add its own default runtime library selection flag. </p>
<p>Use <code>generator expressions</code> to support per-configuration specification. For example, the code: </p>
<pre><code>set(CMAKE_MSVC_RUNTIME_LIBRARY &quot;MultiThreaded$&lt;$&lt;CONFIG:Debug&gt;:Debug&gt;&quot;)
</code></pre>
<p>selects for all following targets a multi-threaded statically-linked runtime library with or without debug information depending on the configuration. </p>
<p>If this variable is not set then the <code>MSVC_RUNTIME_LIBRARY</code> target property will not be set automatically. If that property is not set then CMake uses the default value <code>MultiThreaded$&lt;$&lt;CONFIG:Debug&gt;:Debug&gt;DLL</code> to select a MSVC runtime library. </p>
<p> <code>NOTE:</code> This variable has effect only when policy <code>CMP0091</code> is set to <code>NEW</code> prior to the first <code>project()</code> or <code>enable_language()</code> command that enables a language using a compiler targeting the MSVC ABI. </p>
 </dd></dl>
<h3>CMAKE_NINJA_OUTPUT_PATH_PREFIX</h3>
<p>New in version 3.6. </p>
<p>Set output files path prefix for the <code>Ninja</code> generator. </p>
<p>Every output files listed in the generated <code>build.ninja</code> will be prefixed by the contents of this variable (a trailing slash is appended if missing). This is useful when the generated ninja file is meant to be embedded as a <code>subninja</code> file into a <i>super</i> ninja project. For example, a ninja build file generated with a command like: </p>
<pre><code>cd top-build-dir/sub &amp;&amp;
cmake -G Ninja -DCMAKE_NINJA_OUTPUT_PATH_PREFIX=sub/ path/to/source
</code></pre>
<p>can be embedded in <code>top-build-dir/build.ninja</code> with a directive like this: </p>
<pre><code>subninja sub/build.ninja
</code></pre>
<p>The <code>auto-regeneration</code> rule in <code>top-build-dir/build.ninja</code> must have an order-only dependency on <code>sub/build.ninja</code>. </p>
<p> <code>NOTE:</code> When <code>CMAKE_NINJA_OUTPUT_PATH_PREFIX</code> is set, the project generated by CMake cannot be used as a standalone project. No default targets are specified.  </p>
<h3>CMAKE_NO_BUILTIN_CHRPATH</h3>
<p>Do not use the builtin binary editor to fix runtime library search paths on installation. </p>
<p>When an ELF or XCOFF binary needs to have a different runtime library search path after installation than it does in the build tree, CMake uses a builtin editor to change the runtime search path in the installed copy. If this variable is set to true then CMake will relink the binary before installation instead of using its builtin editor. </p>
<p>New in version 3.20: This variable also applies to XCOFF binaries&#8217; LIBPATH. Prior to the addition of the XCOFF editor in CMake 3.20, this variable applied only to ELF binaries&#8217; RPATH/RUNPATH. </p>
<h3>CMAKE_NO_SYSTEM_FROM_IMPORTED</h3>
<p>Default value for <code>NO_SYSTEM_FROM_IMPORTED</code> of targets. </p>
<p>This variable is used to initialize the <code>NO_SYSTEM_FROM_IMPORTED</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_OPTIMIZE_DEPENDENCIES</h3>
<p>New in version 3.19. </p>
<p>Initializes the <code>OPTIMIZE_DEPENDENCIES</code> target property.  </p>
<h3>CMAKE_OSX_ARCHITECTURES</h3>
<p>Target specific architectures for macOS and iOS. </p>
<p>This variable is used to initialize the <code>OSX_ARCHITECTURES</code> property on each target as it is created. See that target property for additional information. </p>
<p>The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. This variable should be set as a <code>CACHE</code> entry (or else CMake may remove it while initializing a cache entry of the same name). </p>
<p>Despite the <code>OSX</code> part in the variable name(s) they apply also to other SDKs than macOS like iOS, tvOS, or watchOS. </p>
<p>This variable is ignored on platforms other than Apple.  </p>
<h3>CMAKE_OSX_DEPLOYMENT_TARGET</h3>
<p>Specify the minimum version of the target platform (e.g. macOS or iOS) on which the target binaries are to be deployed. CMake uses this variable value for the <code>-mmacosx-version-min</code> flag or their respective target platform equivalents. For older Xcode versions that shipped multiple macOS SDKs this variable also helps to choose the SDK in case <code>CMAKE_OSX_SYSROOT</code> is unset. </p>
<p>If not set explicitly the value is initialized by the <code>MACOSX_DEPLOYMENT_TARGET</code> environment variable, if set, and otherwise computed based on the host platform. </p>
<p>The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. This variable should be set as a <code>CACHE</code> entry (or else CMake may remove it while initializing a cache entry of the same name). </p>
<p>Despite the <code>OSX</code> part in the variable name(s) they apply also to other SDKs than macOS like iOS, tvOS, or watchOS. </p>
<p>This variable is ignored on platforms other than Apple.  </p>
<h3>CMAKE_OSX_SYSROOT</h3>
<p>Specify the location or name of the macOS platform SDK to be used. CMake uses this value to compute the value of the <code>-isysroot</code> flag or equivalent and to help the <code>find_*</code> commands locate files in the SDK. </p>
<p>If not set explicitly the value is initialized by the <code>SDKROOT</code> environment variable, if set, and otherwise computed based on the <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> or the host platform. </p>
<p>The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. This variable should be set as a <code>CACHE</code> entry (or else CMake may remove it while initializing a cache entry of the same name). </p>
<p>Despite the <code>OSX</code> part in the variable name(s) they apply also to other SDKs than macOS like iOS, tvOS, or watchOS. </p>
<p>This variable is ignored on platforms other than Apple.  </p>
<h3>CMAKE_PCH_WARN_INVALID</h3>
<p>New in version 3.18. </p>
<p>This variable is used to initialize the <code>PCH_WARN_INVALID</code> property of targets when they are created.  </p>
<h3>CMAKE_PCH_INSTANTIATE_TEMPLATES</h3>
<p>New in version 3.19. </p>
<p>This variable is used to initialize the <code>PCH_INSTANTIATE_TEMPLATES</code> property of targets when they are created.  </p>
<h3>CMAKE_PDB_OUTPUT_DIRECTORY</h3>
<p>Output directory for MS debug symbol <code>.pdb</code> files generated by the linker for executable and shared library targets. </p>
<p>This variable is used to initialize the <code>PDB_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for MS debug symbol <code>.pdb</code> files generated by the linker for executable and shared library targets. </p>
<p>This is a per-configuration version of <code>CMAKE_PDB_OUTPUT_DIRECTORY</code>. This variable is used to initialize the <code>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_POSITION_INDEPENDENT_CODE</h3>
<p>Default value for <code>POSITION_INDEPENDENT_CODE</code> of targets. </p>
<p>This variable is used to initialize the <code>POSITION_INDEPENDENT_CODE</code> property on all the targets. See that target property for additional information. If set, its value is also used by the <code>try_compile()</code> command.  </p>
<h3>CMAKE_RUNTIME_OUTPUT_DIRECTORY</h3>
<p>Where to put all the RUNTIME target files when built. </p>
<p>This variable is used to initialize the <code>RUNTIME_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>New in version 3.3. </p>
<p>Where to put all the RUNTIME target files when built for a specific configuration. </p>
<p>This variable is used to initialize the <code>RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_SHARED_LINKER_FLAGS</h3>
<p>Linker flags to be used to create shared libraries. </p>
<p>These flags will be used by the linker when creating a shared library.  </p>
<h3>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking a shared library. </p>
<p>Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating shared libraries.  </p>
<h3>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also <code>CMAKE_SHARED_LINKER_FLAGS_INIT</code>.  </p>
<h3>CMAKE_SHARED_LINKER_FLAGS_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_SHARED_LINKER_FLAGS</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also the configuration-specific variable <code>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</code>.  </p>
<h3>CMAKE_SKIP_BUILD_RPATH</h3>
<p>Do not include RPATHs in the build tree. </p>
<p>Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with no RPATH.  </p>
<h3>CMAKE_SKIP_INSTALL_RPATH</h3>
<p>Do not include RPATHs in the install tree. </p>
<p>Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always installed without RPATH, even if RPATH is enabled when building. This can be useful for example to allow running tests from the build directory with RPATH enabled before the installation step. To omit RPATH in both the build and install steps, use <code>CMAKE_SKIP_RPATH</code> instead.  </p>
<h3>CMAKE_STATIC_LINKER_FLAGS</h3>
<p>Flags to be used to create static libraries. These flags will be passed to the archiver when creating a static library. </p>
<p>See also <code>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;</code>. </p>
<p> <code>NOTE:</code> Static libraries do not actually link. They are essentially archives of object files. The use of the name &quot;linker&quot; in the name of this variable is kept for compatibility.  </p>
<h3>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used to create static libraries. These flags will be passed to the archiver when creating a static library in the <code>&lt;CONFIG&gt;</code> configuration. </p>
<p>See also <code>CMAKE_STATIC_LINKER_FLAGS</code>. </p>
<p> <code>NOTE:</code> Static libraries do not actually link. They are essentially archives of object files. The use of the name &quot;linker&quot; in the name of this variable is kept for compatibility.  </p>
<h3>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also <code>CMAKE_STATIC_LINKER_FLAGS_INIT</code>.  </p>
<h3>CMAKE_STATIC_LINKER_FLAGS_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_STATIC_LINKER_FLAGS</code> cache entry the first time a build tree is configured. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also the configuration-specific variable <code>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;_INIT</code>.  </p>
<h3>CMAKE_TRY_COMPILE_CONFIGURATION</h3>
<p>Build configuration used for <code>try_compile()</code> and <code>try_run()</code> projects. </p>
<p>Projects built by <code>try_compile()</code> and <code>try_run()</code> are built synchronously during the CMake configuration step. Therefore a specific build configuration must be chosen even if the generated build system supports multiple configurations.  </p>
<h3>CMAKE_TRY_COMPILE_PLATFORM_VARIABLES</h3>
<p>New in version 3.6. </p>
<p>List of variables that the <code>try_compile()</code> command source file signature must propagate into the test project in order to target the same platform as the host project. </p>
<p>This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p>Variables meaningful to CMake, such as <code>CMAKE_&lt;LANG&gt;_FLAGS</code>, are propagated automatically. The <code>CMAKE_TRY_COMPILE_PLATFORM_VARIABLES</code> variable may be set to pass custom variables meaningful to a toolchain file. For example, a toolchain file may contain: </p>
<pre><code>set(CMAKE_SYSTEM_NAME ...)
set(CMAKE_TRY_COMPILE_PLATFORM_VARIABLES MY_CUSTOM_VARIABLE)
# ... use MY_CUSTOM_VARIABLE ...
</code></pre>
<p>If a user passes <code>-DMY_CUSTOM_VARIABLE=SomeValue</code> to CMake then this setting will be made visible to the toolchain file both for the main project and for test projects generated by the <code>try_compile()</code> command source file signature.  </p>
<h3>CMAKE_TRY_COMPILE_TARGET_TYPE</h3>
<p>New in version 3.6. </p>
<p>Type of target generated for <code>try_compile()</code> calls using the source file signature. Valid values are: </p>
<dl>
<dt><code>EXECUTABLE</code></dt>
<dd> <p> Use <code>add_executable()</code> to name the source file in the generated project. This is the default if no value is given. </p>
 </dd>
<dt><code>STATIC_LIBRARY</code></dt>
<dd> <p> Use <code>add_library()</code> with the <code>STATIC</code> option to name the source file in the generated project. This avoids running the linker and is intended for use with cross-compiling toolchains that cannot link without custom flags or linker scripts. </p>
 </dd></dl>
<h3>CMAKE_UNITY_BUILD</h3>
<p>New in version 3.16. </p>
<p>This variable is used to initialize the <code>UNITY_BUILD</code> property of targets when they are created. Setting it to true enables batch compilation of multiple sources within each target. This feature is known as a <i>Unity</i> or <i>Jumbo</i> build. </p>
<p>Projects should not set this variable, it is intended as a developer control to be set on the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command line or other equivalent methods. The developer must have the ability to enable or disable unity builds according to the capabilities of their own machine and compiler. </p>
<p>By default, this variable is not set, which will result in unity builds being disabled. </p>
<p> <code>NOTE:</code> This option currently does not work well in combination with the <code>CMAKE_EXPORT_COMPILE_COMMANDS</code> variable.  </p>
<h3>CMAKE_UNITY_BUILD_BATCH_SIZE</h3>
<p>New in version 3.16. </p>
<p>This variable is used to initialize the <code>UNITY_BUILD_BATCH_SIZE</code> property of targets when they are created. It specifies the default upper limit on the number of source files that may be combined in any one unity source file when unity builds are enabled for a target.  </p>
<h3>CMAKE_UNITY_BUILD_UNIQUE_ID</h3>
<p>New in version 3.20. </p>
<p>This variable is used to initialize the <code>UNITY_BUILD_UNIQUE_ID</code> property of targets when they are created. It specifies the name of the unique identifier generated per file in a unity build.  </p>
<h3>CMAKE_USE_RELATIVE_PATHS</h3>
<p>This variable has no effect. The partially implemented effect it had in previous releases was removed in CMake 3.4.  </p>
<h3>CMAKE_VISIBILITY_INLINES_HIDDEN</h3>
<p>Default value for the <code>VISIBILITY_INLINES_HIDDEN</code> target property when a target is created.  </p>
<h3>CMAKE_VS_GLOBALS</h3>
<p>New in version 3.13. </p>
<p>List of <code>Key=Value</code> records to be set per target as target properties <code>VS_GLOBAL_&lt;variable&gt;</code> with <code>variable=Key</code> and value <code>Value</code>. </p>
<p>For example: </p>
<pre><code>set(CMAKE_VS_GLOBALS
  &quot;DefaultLanguage=en-US&quot;
  &quot;MinimumVisualStudioVersion=14.0&quot;
  )
</code></pre>
<p>will set properties <code>VS_GLOBAL_DefaultLanguage</code> to <code>en-US</code> and <code>VS_GLOBAL_MinimumVisualStudioVersion</code> to <code>14.0</code> for all targets (except for <code>INTERFACE</code> libraries). </p>
<p>This variable is meant to be set by a <code>toolchain file</code>.  </p>
<h3>CMAKE_VS_INCLUDE_INSTALL_TO_DEFAULT_BUILD</h3>
<p>New in version 3.3. </p>
<p>Include <code>INSTALL</code> target to default build. </p>
<p>In Visual Studio solution, by default the <code>INSTALL</code> target will not be part of the default build. Setting this variable will enable the <code>INSTALL</code> target to be part of the default build.  </p>
<h3>CMAKE_VS_INCLUDE_PACKAGE_TO_DEFAULT_BUILD</h3>
<p>New in version 3.8. </p>
<p>Include <code>PACKAGE</code> target to default build. </p>
<p>In Visual Studio solution, by default the <code>PACKAGE</code> target will not be part of the default build. Setting this variable will enable the <code>PACKAGE</code> target to be part of the default build.  </p>
<h3>CMAKE_VS_JUST_MY_CODE_DEBUGGING</h3>
<p>New in version 3.15. </p>
<p>Enable Just My Code with Visual Studio debugger. </p>
<p>This variable is used to initialize the <code>VS_JUST_MY_CODE_DEBUGGING</code> property on all targets when they are created. See that target property for additional information.  </p>
<h3>CMAKE_VS_SDK_EXCLUDE_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Exclude Directories.  </p>
<h3>CMAKE_VS_SDK_EXECUTABLE_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Executable Directories.  </p>
<h3>CMAKE_VS_SDK_INCLUDE_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Include Directories.  </p>
<h3>CMAKE_VS_SDK_LIBRARY_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Library Directories.  </p>
<h3>CMAKE_VS_SDK_LIBRARY_WINRT_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Library WinRT Directories.  </p>
<h3>CMAKE_VS_SDK_REFERENCE_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Reference Directories.  </p>
<h3>CMAKE_VS_SDK_SOURCE_DIRECTORIES</h3>
<p>New in version 3.12. </p>
<p>This variable allows to override Visual Studio default Source Directories.  </p>
<h3>CMAKE_VS_WINRT_BY_DEFAULT</h3>
<p>New in version 3.13. </p>
<p>Inform Visual Studio Generators for VS 2010 and above that the target platform enables WinRT compilation by default and it needs to be explicitly disabled if <code>/ZW</code> or <code>VS_WINRT_COMPONENT</code> is omitted (as opposed to enabling it when either of those options is present) </p>
<p>This makes cmake configuration consistent in terms of WinRT among platforms &#8211; if you did not enable the WinRT compilation explicitly, it will be disabled (by either not enabling it or explicitly disabling it) </p>
<p>Note: WinRT compilation is always explicitly disabled for C language source files, even if it is expliclty enabled for a project </p>
<p>This variable is meant to be set by a <code>toolchain file</code> for such platforms.  </p>
<h3>CMAKE_WIN32_EXECUTABLE</h3>
<p>Default value for <code>WIN32_EXECUTABLE</code> of targets. </p>
<p>This variable is used to initialize the <code>WIN32_EXECUTABLE</code> property on all the targets. See that target property for additional information.  </p>
<h3>CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS</h3>
<p>New in version 3.4. </p>
<p>Default value for <code>WINDOWS_EXPORT_ALL_SYMBOLS</code> target property. This variable is used to initialize the property on each target as it is created.  </p>
<h3>CMAKE_XCODE_ATTRIBUTE_&lt;an-attribute&gt;</h3>
<p>New in version 3.1. </p>
<p>Set Xcode target attributes directly. </p>
<p>Tell the <code>Xcode</code> generator to set <code>&lt;an-attribute&gt;</code> to a given value in the generated Xcode project. Ignored on other generators. </p>
<p>This offers low-level control over the generated Xcode project file. It is meant as a last resort for specifying settings that CMake does not otherwise have a way to control. Although this can override a setting CMake normally produces on its own, doing so bypasses CMake&#8217;s model of the project and can break things. </p>
<p>See the <code>XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> target property to set attributes on a specific target. </p>
<p>Contents of <code>CMAKE_XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;...&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake-generator-expressions/">cmake-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.  </p>
<h3>EXECUTABLE_OUTPUT_PATH</h3>
<p>Old executable location variable. </p>
<p>The target property <code>RUNTIME_OUTPUT_DIRECTORY</code> supersedes this variable for a target if it is set. Executable targets are otherwise placed in this directory.  </p>
<h3>LIBRARY_OUTPUT_PATH</h3>
<p>Old library location variable. </p>
<p>The target properties <code>ARCHIVE_OUTPUT_DIRECTORY</code>, <code>LIBRARY_OUTPUT_DIRECTORY</code>, and <code>RUNTIME_OUTPUT_DIRECTORY</code> supersede this variable for a target if they are set. Library targets are otherwise placed in this directory.  </p>
<h2>VARIABLES FOR LANGUAGES</h2>
<h3>CMAKE_COMPILER_IS_GNUCC</h3>
<p>New in version 3.7. </p>
<p>True if the <code>C</code> compiler is GNU. Use <code>CMAKE_C_COMPILER_ID</code> instead.  </p>
<h3>CMAKE_COMPILER_IS_GNUCXX</h3>
<p>New in version 3.7. </p>
<p>True if the C++ (<code>CXX</code>) compiler is GNU. Use <code>CMAKE_CXX_COMPILER_ID</code> instead.  </p>
<h3>CMAKE_COMPILER_IS_GNUG77</h3>
<p>New in version 3.7. </p>
<p>True if the <code>Fortran</code> compiler is GNU. Use <code>CMAKE_Fortran_COMPILER_ID</code> instead.  </p>
<h3>CMAKE_CUDA_ARCHITECTURES</h3>
<p>New in version 3.18. </p>
<p>Default value for <code>CUDA_ARCHITECTURES</code> property of targets. </p>
<p>Initialized by the <code>CUDAARCHS</code> environment variable if set. Otherwise as follows depending on <code>CMAKE_CUDA_COMPILER_ID</code>: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> For <code>Clang</code>: the oldest architecture that works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For <code>NVIDIA</code>: the default architecture chosen by the compiler. See policy <code>CMP0104</code>. </p>
<p>Users are encouraged to override this, as the default varies across compilers and compiler versions. </p>
<p>This variable is used to initialize the <code>CUDA_ARCHITECTURES</code> property on all targets. See the target property for additional information. </p>
 </dd></dl>
<h3>Examples</h3>
<pre><code>cmake_minimum_required(VERSION)
if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
  set(CMAKE_CUDA_ARCHITECTURES 75)
endif()
project(example LANGUAGES CUDA)
</code></pre>
<p> <code>CMAKE_CUDA_ARCHITECTURES</code> will default to <code>75</code> unless overridden by the user.  </p>
<h3>CMAKE_CUDA_COMPILE_FEATURES</h3>
<p>New in version 3.17. </p>
<p>List of features known to the CUDA compiler </p>
<p>These features are known to be available for use with the CUDA compiler. This list is a subset of the features listed in the <code>CMAKE_CUDA_KNOWN_FEATURES</code> global property. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CUDA_EXTENSIONS</h3>
<p>New in version 3.8. </p>
<p>Default value for <code>CUDA_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CUDA_HOST_COMPILER</h3>
<p>New in version 3.10. </p>
<p>When <code>CMAKE_CUDA_COMPILER_ID</code> is <code>NVIDIA</code>, <code>CMAKE_CUDA_HOST_COMPILER</code> selects the compiler executable to use when compiling host code for <code>CUDA</code> language files. This maps to the <code>nvcc -ccbin</code> option. </p>
<p>The <code>CMAKE_CUDA_HOST_COMPILER</code> variable may be set explicitly before CUDA is first enabled by a <code>project()</code> or <code>enable_language()</code> command. This can be done via <code>-DCMAKE_CUDA_HOST_COMPILER=...</code> on the command line or in a toolchain file. Or, one may set the <code>CUDAHOSTCXX</code> environment variable to provide a default value. </p>
<p>Once the CUDA language is enabled, the <code>CMAKE_CUDA_HOST_COMPILER</code> variable is read-only and changes to it are undefined behavior. </p>
<p> <code>NOTE:</code> Since <code>CMAKE_CUDA_HOST_COMPILER</code> is meaningful only when the <code>CMAKE_CUDA_COMPILER_ID</code> is <code>NVIDIA</code>, it does not make sense to set <code>CMAKE_CUDA_HOST_COMPILER</code> without also setting <code>CMAKE_CUDA_COMPILER</code> to NVCC. </p>
<p> <code>NOTE:</code> Ignored when using Visual Studio Generators.  </p>
<h3>CMAKE_CUDA_STANDARD</h3>
<p>New in version 3.8. </p>
<p>Default value for <code>CUDA_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CUDA_STANDARD_REQUIRED</h3>
<p>New in version 3.8. </p>
<p>Default value for <code>CUDA_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CUDA_TOOLKIT_INCLUDE_DIRECTORIES</h3>
<p>New in version 3.8. </p>
<p>When the <code>CUDA</code> language has been enabled, this provides a semicolon-separated list of include directories provided by the CUDA Toolkit. The value may be useful for C++ source files to include CUDA headers.  </p>
<h3>CMAKE_CXX_COMPILE_FEATURES</h3>
<p>New in version 3.1. </p>
<p>List of features known to the C++ compiler </p>
<p>These features are known to be available for use with the C++ compiler. This list is a subset of the features listed in the <code>CMAKE_CXX_KNOWN_FEATURES</code> global property. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CXX_EXTENSIONS</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>CXX_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CXX_STANDARD</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>CXX_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_CXX_STANDARD_REQUIRED</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>CXX_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_C_COMPILE_FEATURES</h3>
<p>New in version 3.1. </p>
<p>List of features known to the C compiler </p>
<p>These features are known to be available for use with the C compiler. This list is a subset of the features listed in the <code>CMAKE_C_KNOWN_FEATURES</code> global property. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_C_EXTENSIONS</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>C_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_C_STANDARD</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>C_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_C_STANDARD_REQUIRED</h3>
<p>New in version 3.1. </p>
<p>Default value for <code>C_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_Fortran_MODDIR_DEFAULT</h3>
<p>Fortran default module output directory. </p>
<p>Most Fortran compilers write <code>.mod</code> files to the current working directory. For those that do not, this is set to <code>.</code> and used when the <code>Fortran_MODULE_DIRECTORY</code> target property is not set.  </p>
<h3>CMAKE_Fortran_MODDIR_FLAG</h3>
<p>Fortran flag for module output directory. </p>
<p>This stores the flag needed to pass the value of the <code>Fortran_MODULE_DIRECTORY</code> target property to the compiler.  </p>
<h3>CMAKE_Fortran_MODOUT_FLAG</h3>
<p>Fortran flag to enable module output. </p>
<p>Most Fortran compilers write <code>.mod</code> files out by default. For others, this stores the flag needed to enable module output.  </p>
<h3>CMAKE_HIP_ARCHITECTURES</h3>
<p>New in version 3.21. </p>
<p>Default value for <code>HIP_ARCHITECTURES</code> property of targets. </p>
<p>This is initialized to the architectures reported by <code>rocm_agent_enumerator</code>, if available, and otherwise to the default chosen by the compiler. </p>
<p>This variable is used to initialize the <code>HIP_ARCHITECTURES</code> property on all targets. See the target property for additional information.  </p>
<h3>CMAKE_HIP_EXTENSIONS</h3>
<p>New in version 3.21. </p>
<p>Default value for <code>HIP_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_HIP_STANDARD</h3>
<p>New in version 3.21. </p>
<p>Default value for <code>HIP_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_HIP_STANDARD_REQUIRED</h3>
<p>New in version 3.21. </p>
<p>Default value for <code>HIP_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_ISPC_HEADER_DIRECTORY</h3>
<p>New in version 3.19. </p>
<p>ISPC generated header output directory. </p>
<p>This variable is used to initialize the <code>ISPC_HEADER_DIRECTORY</code> property on all the targets. See the target property for additional information.  </p>
<h3>CMAKE_ISPC_HEADER_SUFFIX</h3>
<p>New in version 3.19.2. </p>
<p>Output suffix to be used for ISPC generated headers. </p>
<p>This variable is used to initialize the <code>ISPC_HEADER_SUFFIX</code> property on all the targets. See the target property for additional information.  </p>
<h3>CMAKE_ISPC_INSTRUCTION_SETS</h3>
<p>New in version 3.19. </p>
<p>Default value for <code>ISPC_INSTRUCTION_SETS</code> property of targets. </p>
<p>This variable is used to initialize the <code>ISPC_INSTRUCTION_SETS</code> property on all targets. See the target property for additional information.  </p>
<h3>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_MACHINE</h3>
<p>New in version 3.7.1. </p>
<p>When Cross Compiling for Android this variable contains the toolchain binutils machine name (e.g. <code>gcc -dumpmachine</code>). The binutils typically have a <code>&lt;machine&gt;-</code> prefix on their name. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_PREFIX</code> and <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_SUFFIX</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_PREFIX</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android this variable contains the absolute path prefixing the toolchain GNU compiler and its binutils. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_SUFFIX</code> and <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_MACHINE</code>. </p>
<p>For example, the path to the linker is: </p>
<pre><code>${CMAKE_CXX_ANDROID_TOOLCHAIN_PREFIX}ld${CMAKE_CXX_ANDROID_TOOLCHAIN_SUFFIX}
</code></pre>
<h3>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_SUFFIX</h3>
<p>New in version 3.7. </p>
<p>When Cross Compiling for Android this variable contains the host platform suffix of the toolchain GNU compiler and its binutils. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_PREFIX</code> and <code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_MACHINE</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</h3>
<p>Rule variable to append to a static archive. </p>
<p>This is a rule variable that tells CMake how to append to a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</h3>
<p>Rule variable to create a new static archive. </p>
<p>This is a rule variable that tells CMake how to create a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</h3>
<p>Rule variable to finish an existing static archive. </p>
<p>This is a rule variable that tells CMake how to finish a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_BYTE_ORDER</h3>
<p>New in version 3.20. </p>
<p>Byte order of <code>&lt;LANG&gt;</code> compiler target architecture, if known. If defined and not empty, the value is one of: </p>
<dl>
<dt><code>BIG_ENDIAN</code></dt>
<dd> <p> The target architecture is Big Endian. </p>
 </dd>
<dt><code>LITTLE_ENDIAN</code></dt>
<dd> <p> The target architecture is Little Endian. </p>
<p>This is defined for languages <code>C</code>, <code>CXX</code>, <code>OBJC</code>, <code>OBJCXX</code>, and <code>CUDA</code>. </p>
<p>If <code>CMAKE_OSX_ARCHITECTURES</code> specifies multiple architectures, the value of <code>CMAKE_&lt;LANG&gt;_BYTE_ORDER</code> is non-empty only if all architectures share the same byte order. </p>
 </dd></dl>
<h3>CMAKE_&lt;LANG&gt;_COMPILER</h3>
<p>The full path to the compiler for <code>LANG</code>. </p>
<p>This is the command that will be used as the <code>&lt;LANG&gt;</code> compiler. Once set, you can not change this variable.  </p>
<h3>Usage</h3>
<p>This variable can be set by the user during the first time a build tree is configured. </p>
<p>If a non-full path value is supplied then CMake will resolve the full path of the compiler. </p>
<p>The variable could be set in a user supplied toolchain file or via <i>-D</i> on the command line. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included as items in a list; they can not be changed. </p>
<pre><code>#set within user supplied toolchain file
set(CMAKE_C_COMPILER /full/path/to/qcc --arg1 --arg2)
</code></pre>
<p>or </p>
<pre><code>$ cmake ... -DCMAKE_C_COMPILER='qcc;--arg1;--arg2'
</code></pre>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_EXTERNAL_TOOLCHAIN</h3>
<p>The external toolchain for cross-compiling, if supported. </p>
<p>Some compiler toolchains do not ship their own auxiliary utilities such as archivers and linkers. The compiler driver may support a command-line argument to specify the location of such tools. <code>CMAKE_&lt;LANG&gt;_COMPILER_EXTERNAL_TOOLCHAIN</code> may be set to a path to the external toolchain and will be passed to the compiler driver if supported. </p>
<p>This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_ID</h3>
<p>Compiler identification string. </p>
<p>A short string unique to the compiler vendor. Possible values include: </p>
<pre><code>Absoft = Absoft Fortran (absoft.com)
ADSP = Analog VisualDSP++ (analog.com)
AppleClang = Apple Clang (apple.com)
ARMCC = ARM Compiler (arm.com)
ARMClang = ARM Compiler based on Clang (arm.com)
Bruce = Bruce C Compiler
CCur = Concurrent Fortran (ccur.com)
Clang = LLVM Clang (clang.llvm.org)
Cray = Cray Compiler (cray.com)
Embarcadero, Borland = Embarcadero (embarcadero.com)
Flang = Flang LLVM Fortran Compiler
Fujitsu = Fujitsu HPC compiler (Trad mode)
FujitsuClang = Fujitsu HPC compiler (Clang mode)
G95 = G95 Fortran (g95.org)
GNU = GNU Compiler Collection (gcc.gnu.org)
GHS = Green Hills Software (www.ghs.com)
HP = Hewlett-Packard Compiler (hp.com)
IAR = IAR Systems (iar.com)
Intel = Intel Compiler (intel.com)
IntelLLVM = Intel LLVM-Based Compiler (intel.com)
MSVC = Microsoft Visual Studio (microsoft.com)
NVHPC = NVIDIA HPC SDK Compiler (nvidia.com)
NVIDIA = NVIDIA CUDA Compiler (nvidia.com)
OpenWatcom = Open Watcom (openwatcom.org)
PGI = The Portland Group (pgroup.com)
PathScale = PathScale (pathscale.com)
SDCC = Small Device C Compiler (sdcc.sourceforge.net)
SunPro = Oracle Solaris Studio (oracle.com)
TI = Texas Instruments (ti.com)
TinyCC = Tiny C Compiler (tinycc.org)
XL, VisualAge, zOS = IBM XL (ibm.com)
XLClang = IBM Clang-based XL (ibm.com)
</code></pre>
<p>This variable is not guaranteed to be defined for all compilers or languages.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_LOADED</h3>
<p>Defined to true if the language is enabled. </p>
<p>When language <code>&lt;LANG&gt;</code> is enabled by <code>project()</code> or <code>enable_language()</code> this variable is defined to <code>1</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_PREDEFINES_COMMAND</h3>
<p>New in version 3.10. </p>
<p>Command that outputs the compiler pre definitions. </p>
<p>See <code>AUTOMOC</code> which uses <i>CMAKE_CXX_COMPILER_PREDEFINES_COMMAND</i> to generate the <code>AUTOMOC_COMPILER_PREDEFINES</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</h3>
<p>The target for cross-compiling, if supported. </p>
<p>Some compiler drivers are inherently cross-compilers, such as clang and QNX qcc. These compiler drivers support a command-line argument to specify the target to cross-compile for. </p>
<p>This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</h3>
<p>Compiler version string. </p>
<p>Compiler version in major[.minor[.patch[.tweak]]] format. This variable is not guaranteed to be defined for all compilers or languages. </p>
<p>For example <code>CMAKE_C_COMPILER_VERSION</code> and <code>CMAKE_CXX_COMPILER_VERSION</code> might indicate the respective C and C++ compiler version.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILE_OBJECT</h3>
<p>Rule variable to compile a single object file. </p>
<p>This is a rule variable that tells CMake how to compile a single object file for the language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_SHARED_LIBRARY</h3>
<p>Rule variable to create a shared library. </p>
<p>This is a rule variable that tells CMake how to create a shared library for the language <code>&lt;LANG&gt;</code>. This rule variable is a <code>;</code> delimited list of commands to run to perform the linking step.  </p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_SHARED_MODULE</h3>
<p>Rule variable to create a shared module. </p>
<p>This is a rule variable that tells CMake how to create a shared library for the language <code>&lt;LANG&gt;</code>. This rule variable is a <code>;</code> delimited list of commands to run.  </p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</h3>
<p>Rule variable to create a static library. </p>
<p>This is a rule variable that tells CMake how to create a static library for the language <code>&lt;LANG&gt;</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_EXTENSIONS</h3>
<p>The variations are: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_HIP_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_EXTENSIONS</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_EXTENSIONS</code> </p>
<p>Default values for <code>&lt;LANG&gt;_EXTENSIONS</code> target properties if set when a target is created. For the compiler&#8217;s default setting see <code>CMAKE_&lt;LANG&gt;_EXTENSIONS_DEFAULT</code>. </p>
<p>For supported CMake versions see the respective pages. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
 </dd></dl>
<h3>CMAKE_&lt;LANG&gt;_EXTENSIONS_DEFAULT</h3>
<p>New in version 3.22. </p>
<p>Compiler&#8217;s default extensions mode. Used as the default for the <code>&lt;LANG&gt;_EXTENSIONS</code> target property when <code>CMAKE_&lt;LANG&gt;_EXTENSIONS</code> is not set (see <code>CMP0128</code>). </p>
<p>This variable is read-only. Modifying it is undefined behavior.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS</h3>
<p>Flags for all build types. </p>
<p> <code>&lt;LANG&gt;</code> flags used regardless of the value of <code>CMAKE_BUILD_TYPE</code>. </p>
<p>This is initialized for each language from environment variables: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_FLAGS</code>: Initialized by the <code>CFLAGS</code> environment variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_FLAGS</code>: Initialized by the <code>CXXFLAGS</code> environment variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_FLAGS</code>: Initialized by the <code>CUDAFLAGS</code> environment variable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_Fortran_FLAGS</code>: Initialized by the <code>FFLAGS</code> environment variable. </p>
<p>This value is a command-line string fragment. Therefore, multiple options should be separated by spaces, and options with spaces should be quoted. </p>
<p>The flags in this variable will be passed to the compiler before those in the per-configuration <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variant, and before flags added by the <code>add_compile_options()</code> or <code>target_compile_options()</code> commands. </p>
 </dd></dl>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags for language <code>&lt;LANG&gt;</code> when building for the <code>&lt;CONFIG&gt;</code> configuration. </p>
<p>The flags in this variable will be passed to the compiler after those in the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variable, but before flags added by the <code>add_compile_options()</code> or <code>target_compile_options()</code> commands.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</h3>
<p>New in version 3.11. </p>
<p>Value used to initialize the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> cache entry the first time a build tree is configured for language <code>&lt;LANG&gt;</code>. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_FLAGS_INIT</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</h3>
<p>This variable is the <code>Debug</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG_INIT</h3>
<p>New in version 3.7. </p>
<p>This variable is the <code>Debug</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_INIT</h3>
<p>New in version 3.7. </p>
<p>Value used to initialize the <code>CMAKE_&lt;LANG&gt;_FLAGS</code> cache entry the first time a build tree is configured for language <code>&lt;LANG&gt;</code>. This variable is meant to be set by a <code>toolchain file</code>. CMake may prepend or append content to the value based on the environment and target platform. For example, the contents of a <code>xxxFLAGS</code> environment variable will be prepended, where <code>xxx</code> will be language-specific but not necessarily the same as <code>&lt;LANG&gt;</code> (e.g. <code>CXXFLAGS</code> for <code>CXX</code>, <code>FFLAGS</code> for <code>Fortran</code>, and so on). This value is a command-line string fragment. Therefore, multiple options should be separated by spaces, and options with spaces should be quoted. </p>
<p>See also the configuration-specific <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_MINSIZEREL</h3>
<p>This variable is the <code>MinSizeRel</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_MINSIZEREL_INIT</h3>
<p>New in version 3.7. </p>
<p>This variable is the <code>MinSizeRel</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELEASE</h3>
<p>This variable is the <code>Release</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELEASE_INIT</h3>
<p>New in version 3.7. </p>
<p>This variable is the <code>Release</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELWITHDEBINFO</h3>
<p>This variable is the <code>RelWithDebInfo</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELWITHDEBINFO_INIT</h3>
<p>New in version 3.7. </p>
<p>This variable is the <code>RelWithDebInfo</code> variant of the <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;_INIT</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_IGNORE_EXTENSIONS</h3>
<p>File extensions that should be ignored by the build. </p>
<p>This is a list of file extensions that may be part of a project for a given language but are not compiled.  </p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_INCLUDE_DIRECTORIES</h3>
<p>Directories implicitly searched by the compiler for header files. </p>
<p>CMake does not explicitly specify these directories on compiler command lines for language <code>&lt;LANG&gt;</code>. This prevents system include directories from being treated as user include directories on some compilers, which is important for <code>C</code>, <code>CXX</code>, and <code>CUDA</code> to avoid overriding standard library headers. </p>
<p>This value is not used for <code>Fortran</code> because it has no standard library headers and some compilers do not search their implicit include directories for module <code>.mod</code> files.  </p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</h3>
<p>Implicit linker search path detected for language <code>&lt;LANG&gt;</code>. </p>
<p>Compilers typically pass directories containing language runtime libraries and default library search paths when they invoke a linker. These paths are implicit linker search directories for the compiler&#8217;s language. For each language enabled by the <code>project()</code> or <code>enable_language()</code> command, CMake automatically detects these directories and reports the results in this variable. </p>
<p>When linking to a static library, CMake adds the implicit link directories from this variable for each language used in the static library (except the language whose compiler is used to drive linking). In the case of an imported static library, the <code>IMPORTED_LINK_INTERFACE_LANGUAGES</code> target property lists the languages whose implicit link information is needed. If any of the languages is not enabled, its value for the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</code> variable may instead be provided by the project. Or, a <code>toolchain file</code> may set the variable to a value known for the specified toolchain. It will either be overridden when the language is enabled, or used as a fallback. </p>
<p>Some toolchains read implicit directories from an environment variable such as <code>LIBRARY_PATH</code>. If using such an environment variable, keep its value consistent when operating in a given build tree because CMake saves the value detected when first creating a build tree. </p>
<p>If policy <code>CMP0060</code> is not set to <code>NEW</code>, then when a library in one of these directories is given by full path to <code>target_link_libraries()</code> CMake will generate the <code>-l&lt;name&gt;</code> form on link lines for historical purposes. </p>
<p>See also the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES</h3>
<p>Implicit linker framework search path detected for language <code>&lt;LANG&gt;</code>. </p>
<p>These paths are implicit linker framework search directories for the compiler&#8217;s language. CMake automatically detects these directories for each language and reports the results in this variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</h3>
<p>Implicit link libraries and flags detected for language <code>&lt;LANG&gt;</code>. </p>
<p>Compilers typically pass language runtime library names and other flags when they invoke a linker. These flags are implicit link options for the compiler&#8217;s language. For each language enabled by the <code>project()</code> or <code>enable_language()</code> command, CMake automatically detects these libraries and flags and reports the results in this variable. </p>
<p>When linking to a static library, CMake adds the implicit link libraries and flags from this variable for each language used in the static library (except the language whose compiler is used to drive linking). In the case of an imported static library, the <code>IMPORTED_LINK_INTERFACE_LANGUAGES</code> target property lists the languages whose implicit link information is needed. If any of the languages is not enabled, its value for the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</code> variable may instead be provided by the project. Or, a <code>toolchain file</code> may set the variable to a value known for the specified toolchain. It will either be overridden when the language is enabled, or used as a fallback. </p>
<p>See also the <code>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</h3>
<p>Target architecture library directory name detected for <code>&lt;LANG&gt;</code>. </p>
<p>If the <code>&lt;LANG&gt;</code> compiler passes to the linker an architecture-specific system library search directory such as <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> this variable contains the <code>&lt;arch&gt;</code> name if/as detected by CMake.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINK_EXECUTABLE</h3>
<p>Rule variable to link an executable. </p>
<p>Rule variable to link an executable for the given language.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</h3>
<p>Preference value for linker language selection. </p>
<p>The &quot;linker language&quot; for executable, shared library, and module targets is the language whose compiler will invoke the linker. The <code>LINKER_LANGUAGE</code> target property sets the language explicitly. Otherwise, the linker language is that whose linker preference value is highest among languages compiled and linked into the target. See also the <code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES</code> variable.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES</h3>
<p>True if <code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</code> propagates across targets. </p>
<p>This is used when CMake selects a linker language for a target. Languages compiled directly into the target are always considered. A language compiled into static libraries linked by the target is considered if this variable is true.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG</h3>
<p>New in version 3.13. </p>
<p>Defines the syntax of compiler driver option to pass options to the linker tool. It will be used to translate the <code>LINKER:</code> prefix in the link options (see <code>add_link_options()</code> and <code>target_link_options()</code>). </p>
<p>This variable holds a semicolon-separated list of tokens. If a space (i.e. &quot; &quot;) is specified as last token, flag and <code>LINKER:</code> arguments will be specified as separate arguments to the compiler driver. The <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG_SEP</code> variable can be specified to manage concatenation of arguments. </p>
<p>For example, for <code>Clang</code> we have: </p>
<pre><code>set (CMAKE_C_LINKER_WRAPPER_FLAG &quot;-Xlinker&quot; &quot; &quot;)
</code></pre>
<p>Specifying <code>&quot;LINKER:-z,defs&quot;</code> will be transformed in <code>-Xlinker -z -Xlinker defs</code>. </p>
<p>For <code>GNU GCC</code>: </p>
<pre><code>set (CMAKE_C_LINKER_WRAPPER_FLAG &quot;-Wl,&quot;)
set (CMAKE_C_LINKER_WRAPPER_FLAG_SEP &quot;,&quot;)
</code></pre>
<p>Specifying <code>&quot;LINKER:-z,defs&quot;</code> will be transformed in <code>-Wl,-z,defs</code>. </p>
<p>And for <code>SunPro</code>: </p>
<pre><code>set (CMAKE_C_LINKER_WRAPPER_FLAG &quot;-Qoption&quot; &quot;ld&quot; &quot; &quot;)
set (CMAKE_C_LINKER_WRAPPER_FLAG_SEP &quot;,&quot;)
</code></pre>
<p>Specifying <code>&quot;LINKER:-z,defs&quot;</code> will be transformed in <code>-Qoption ld -z,defs</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG_SEP</h3>
<p>New in version 3.13. </p>
<p>This variable is used with <code>CMAKE_&lt;LANG&gt;_LINKER_WRAPPER_FLAG</code> variable to format <code>LINKER:</code> prefix in the link options (see <code>add_link_options()</code> and <code>target_link_options()</code>). </p>
<p>When specified, arguments of the <code>LINKER:</code> prefix will be concatenated using this value as separator.  </p>
<h3>CMAKE_&lt;LANG&gt;_OUTPUT_EXTENSION</h3>
<p>Extension for the output of a compile for a single file. </p>
<p>This is the extension for an object file for the given <code>&lt;LANG&gt;</code>. For example <code>.obj</code> for C on Windows.  </p>
<h3>CMAKE_&lt;LANG&gt;_SIMULATE_ID</h3>
<p>Identification string of the &quot;simulated&quot; compiler. </p>
<p>Some compilers simulate other compilers to serve as drop-in replacements. When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> for the simulated compiler. </p>
<p> <code>NOTE:</code> In other words, this variable describes the ABI compatibility of the generated code.  </p>
<h3>CMAKE_&lt;LANG&gt;_SIMULATE_VERSION</h3>
<p>Version string of &quot;simulated&quot; compiler. </p>
<p>Some compilers simulate other compilers to serve as drop-in replacements. When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> for the simulated compiler.  </p>
<h3>CMAKE_&lt;LANG&gt;_SIZEOF_DATA_PTR</h3>
<p>Size of pointer-to-data types for language <code>&lt;LANG&gt;</code>. </p>
<p>This holds the size (in bytes) of pointer-to-data types in the target platform ABI. It is defined for languages <code>C</code> and <code>CXX</code> (C++).  </p>
<h3>CMAKE_&lt;LANG&gt;_SOURCE_FILE_EXTENSIONS</h3>
<p>Extensions of source files for the given language. </p>
<p>This is the list of extensions for a given language&#8217;s source files.  </p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD</h3>
<p>The variations are: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_HIP_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_STANDARD</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_STANDARD</code> </p>
<p>Default values for <code>&lt;LANG&gt;_STANDARD</code> target properties if set when a target is created. </p>
<p>For supported CMake versions see the respective pages. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
 </dd></dl>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_DEFAULT</h3>
<p>New in version 3.9. </p>
<p>The compiler&#8217;s default standard for the language <code>&lt;LANG&gt;</code>. Empty if the compiler has no conception of standard levels.  </p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_INCLUDE_DIRECTORIES</h3>
<p>New in version 3.6. </p>
<p>Include directories to be used for every source file compiled with the <code>&lt;LANG&gt;</code> compiler. This is meant for specification of system include directories needed by the language for the current platform. The directories always appear at the end of the include path passed to the compiler. </p>
<p>This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_STANDARD_LIBRARIES</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_LIBRARIES</h3>
<p>New in version 3.6. </p>
<p>Libraries linked into every executable and shared library linked for language <code>&lt;LANG&gt;</code>. This is meant for specification of system libraries needed by the language for the current platform. </p>
<p>This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p>See also <code>CMAKE_&lt;LANG&gt;_STANDARD_INCLUDE_DIRECTORIES</code>.  </p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_REQUIRED</h3>
<p>The variations are: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_C_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CXX_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_CUDA_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_HIP_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJC_STANDARD_REQUIRED</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>CMAKE_OBJCXX_STANDARD_REQUIRED</code> </p>
<p>Default values for <code>&lt;LANG&gt;_STANDARD_REQUIRED</code> target properties if set when a target is created. </p>
<p>For supported CMake versions see the respective pages. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers. </p>
 </dd></dl>
<h3>CMAKE_OBJC_EXTENSIONS</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJC_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_OBJC_STANDARD</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJC_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_OBJC_STANDARD_REQUIRED</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJC_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_OBJCXX_EXTENSIONS</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJCXX_EXTENSIONS</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_OBJCXX_STANDARD</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJCXX_STANDARD</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_OBJCXX_STANDARD_REQUIRED</h3>
<p>New in version 3.16. </p>
<p>Default value for <code>OBJCXX_STANDARD_REQUIRED</code> target property if set when a target is created. </p>
<p>See the <code><a href="/docs/linux/man/7-cmake-compile-features/">cmake-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.  </p>
<h3>CMAKE_Swift_LANGUAGE_VERSION</h3>
<p>New in version 3.7. </p>
<p>Set to the Swift language version number. If not set, the oldest legacy version known to be available in the host Xcode version is assumed: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Swift <code>4.0</code> for Xcode 10.2 and above. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Swift <code>3.0</code> for Xcode 8.3 and above. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Swift <code>2.3</code> for Xcode 8.2 and below. </p>
 </dd></dl>
<h3>CMAKE_USER_MAKE_RULES_OVERRIDE_&lt;LANG&gt;</h3>
<p>Specify a CMake file that overrides platform information for <code>&lt;LANG&gt;</code>. </p>
<p>This is a language-specific version of <code>CMAKE_USER_MAKE_RULES_OVERRIDE</code> loaded only when enabling language <code>&lt;LANG&gt;</code>.  </p>
<h2>VARIABLES FOR CTEST</h2>
<h3>CTEST_BINARY_DIRECTORY</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>BuildDirectory</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_BUILD_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MakeCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_BUILD_NAME</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>BuildName</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_BZR_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>BZRCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_BZR_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>BZRUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_CHANGE_ID</h3>
<p>New in version 3.4. </p>
<p>Specify the CTest <code>ChangeId</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. </p>
<p>This setting allows CTest to pass arbitrary information about this build up to CDash. One use of this feature is to allow CDash to post comments on your pull request if anything goes wrong with your build.  </p>
<h3>CTEST_CHECKOUT_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Tell the <code>ctest_start()</code> command how to checkout or initialize the source directory in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_CONFIGURATION_TYPE</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DefaultCTestConfigurationType</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. </p>
<p>If the configuration type is set via <code>-C &lt;cfg&gt;</code> from the command line then this variable is populated accordingly.  </p>
<h3>CTEST_CONFIGURE_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>ConfigureCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_COVERAGE_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>CoverageCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>Cobertura</h3>
<p>Using <i>Cobertura</i> as the coverage generation within your multi-module Java project can generate a series of XML files. </p>
<p>The Cobertura Coverage parser expects to read the coverage data from a single XML file which contains the coverage data for all modules. Cobertura has a program with the ability to merge given <code>cobertura.ser</code> files and then another program to generate a combined XML file from the previous merged file. For command line testing, this can be done by hand prior to CTest looking for the coverage files. For script builds, set the <code>CTEST_COVERAGE_COMMAND</code> variable to point to a file which will perform these same steps, such as a <code>.sh</code> or <code>.bat</code> file. </p>
<pre><code>set(CTEST_COVERAGE_COMMAND .../run-coverage-and-consolidate.sh)
</code></pre>
<p>where the <code>run-coverage-and-consolidate.sh</code> script is perhaps created by the <code>configure_file()</code> command and might contain the following code: </p>
<pre><code>#!/usr/bin/env bash
CoberturaFiles=&quot;$(find &quot;/path/to/source&quot; -name &quot;cobertura.ser&quot;)&quot;
SourceDirs=&quot;$(find &quot;/path/to/source&quot; -name &quot;java&quot; -type d)&quot;
cobertura-merge --datafile coberturamerge.ser $CoberturaFiles
cobertura-report --datafile coberturamerge.ser --destination . \
                 --format xml $SourceDirs
</code></pre>
<p>The script uses <code>find</code> to capture the paths to all of the <code>cobertura.ser</code> files found below the project&#8217;s source directory. It keeps the list of files and supplies it as an argument to the <code>cobertura-merge</code> program. The <code>--datafile</code> argument signifies where the result of the merge will be kept. </p>
<p>The combined <code>coberturamerge.ser</code> file is then used to generate the XML report using the <code>cobertura-report</code> program. The call to the cobertura-report program requires some named arguments. </p>
<dl>
<dt><code>--datafila</code></dt>
<dd> <p> path to the merged <code>.ser</code> file </p>
 </dd>
<dt><code>--destination</code></dt>
<dd> <p> path to put the output files(s) </p>
 </dd>
<dt><code>--format</code></dt>
<dd> <p> file format to write output in: xml or html </p>
<p>The rest of the supplied arguments consist of the full paths to the <code>/src/main/java</code> directories of each module within the source tree. These directories are needed and should not be forgotten. </p>
 </dd></dl>
<h3>CTEST_COVERAGE_EXTRA_FLAGS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>CoverageExtraFlags</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_CURL_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>CurlOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_CUSTOM_COVERAGE_EXCLUDE</h3>
<p>A list of regular expressions which will be used to exclude files by their path from coverage output by the <code>ctest_coverage()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_ERROR_EXCEPTION</h3>
<p>A list of regular expressions which will be used to exclude when detecting error messages in build outputs by the <code>ctest_test()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_ERROR_MATCH</h3>
<p>A list of regular expressions which will be used to detect error messages in build outputs by the <code>ctest_test()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_ERROR_POST_CONTEXT</h3>
<p>The number of lines to include as context which follow an error message by the <code>ctest_test()</code> command. The default is 10. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_ERROR_PRE_CONTEXT</h3>
<p>The number of lines to include as context which precede an error message by the <code>ctest_test()</code> command. The default is 10. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_MAXIMUM_FAILED_TEST_OUTPUT_SIZE</h3>
<p>When saving a failing test&#8217;s output, this is the maximum size, in bytes, that will be collected by the <code>ctest_test()</code> command. Defaults to 307200 (300 KiB). </p>
<p>If a test&#8217;s output contains the literal string &quot;CTEST_FULL_OUTPUT&quot;, the output will not be truncated and may exceed the maximum size. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation. </p>
<p>For controlling the output collection of passing tests, see <code>CTEST_CUSTOM_MAXIMUM_PASSED_TEST_OUTPUT_SIZE</code>.  </p>
<h3>CTEST_CUSTOM_MAXIMUM_NUMBER_OF_ERRORS</h3>
<p>The maximum number of errors in a single build step which will be detected. After this, the <code>ctest_test()</code> command will truncate the output. Defaults to 50. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_MAXIMUM_NUMBER_OF_WARNINGS</h3>
<p>The maximum number of warnings in a single build step which will be detected. After this, the <code>ctest_test()</code> command will truncate the output. Defaults to 50. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_MAXIMUM_PASSED_TEST_OUTPUT_SIZE</h3>
<p>When saving a passing test&#8217;s output, this is the maximum size, in bytes, that will be collected by the <code>ctest_test()</code> command. Defaults to 1024 (1 KiB). </p>
<p>If a test&#8217;s output contains the literal string &quot;CTEST_FULL_OUTPUT&quot;, the output will not be truncated and may exceed the maximum size. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation. </p>
<p>For controlling the output collection of failing tests, see <code>CTEST_CUSTOM_MAXIMUM_FAILED_TEST_OUTPUT_SIZE</code>.  </p>
<h3>CTEST_CUSTOM_MEMCHECK_IGNORE</h3>
<p>A list of regular expressions to use to exclude tests during the <code>ctest_memcheck()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_POST_MEMCHECK</h3>
<p>A list of commands to run at the end of the <code>ctest_memcheck()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_POST_TEST</h3>
<p>A list of commands to run at the end of the <code>ctest_test()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_PRE_MEMCHECK</h3>
<p>A list of commands to run at the start of the <code>ctest_memcheck()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_PRE_TEST</h3>
<p>A list of commands to run at the start of the <code>ctest_test()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_TESTS_IGNORE</h3>
<p>A list of regular expressions to use to exclude tests during the <code>ctest_test()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_WARNING_EXCEPTION</h3>
<p>A list of regular expressions which will be used to exclude when detecting warning messages in build outputs by the <code>ctest_build()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CUSTOM_WARNING_MATCH</h3>
<p>A list of regular expressions which will be used to detect warning messages in build outputs by the <code>ctest_build()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_CVS_CHECKOUT</h3>
<p>New in version 3.1. </p>
<p>Deprecated. Use <code>CTEST_CHECKOUT_COMMAND</code> instead.  </p>
<h3>CTEST_CVS_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>CVSCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_CVS_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>CVSUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_LOCATION</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DropLocation</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_METHOD</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DropMethod</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_SITE</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DropSite</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_SITE_CDASH</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>IsCDash</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_SITE_PASSWORD</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DropSitePassword</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_DROP_SITE_USER</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>DropSiteUser</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_EXTRA_COVERAGE_GLOB</h3>
<p>New in version 3.4. </p>
<p>A list of regular expressions which will be used to find files which should be covered by the <code>ctest_coverage()</code> command. </p>
<p>It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.  </p>
<h3>CTEST_GIT_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>GITCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_GIT_INIT_SUBMODULES</h3>
<p>New in version 3.6. </p>
<p>Specify the CTest <code>GITInitSubmodules</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_GIT_UPDATE_CUSTOM</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>GITUpdateCustom</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_GIT_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>GITUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_HG_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>HGCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_HG_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>HGUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_LABELS_FOR_SUBPROJECTS</h3>
<p>New in version 3.10. </p>
<p>Specify the CTest <code>LabelsForSubprojects</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_MEMORYCHECK_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MemoryCheckCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_MEMORYCHECK_COMMAND_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MemoryCheckCommandOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_MEMORYCHECK_SANITIZER_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MemoryCheckSanitizerOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. </p>
<p>CTest prepends correct sanitizer options <code>*_OPTIONS</code> environment variable to executed command. CTests adds its own <code>log_path</code> to sanitizer options, don&#8217;t provide your own <code>log_path</code>.  </p>
<h3>CTEST_MEMORYCHECK_SUPPRESSIONS_FILE</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MemoryCheckSuppressionFile</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_MEMORYCHECK_TYPE</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>MemoryCheckType</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. Valid values are <code>Valgrind</code>, <code>Purify</code>, <code>BoundsChecker</code>, <code>DrMemory</code>, <code>CudaSanitizer</code>, <code>ThreadSanitizer</code>, <code>AddressSanitizer</code>, <code>LeakSanitizer</code>, <code>MemorySanitizer</code> and <code>UndefinedBehaviorSanitizer</code>.  </p>
<h3>CTEST_NIGHTLY_START_TIME</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>NightlyStartTime</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. </p>
<p>Note that this variable must always be set for a nightly build in a dashboard script. It is needed so that nightly builds can be properly grouped together in CDash.  </p>
<h3>CTEST_P4_CLIENT</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>P4Client</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_P4_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>P4Command</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_P4_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>P4Options</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_P4_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>P4UpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_RESOURCE_SPEC_FILE</h3>
<p>New in version 3.18. </p>
<p>Specify the CTest <code>ResourceSpecFile</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. </p>
<p>This can also be used to specify the resource spec file from a CMake build. If no <code>RESOURCE_SPEC_FILE</code> is passed to <code>ctest_test()</code>, and <code>CTEST_RESOURCE_SPEC_FILE</code> is not specified in the dashboard script, the value of this variable from the build is used.  </p>
<h3>CTEST_RUN_CURRENT_SCRIPT</h3>
<p>New in version 3.11. </p>
<p>Setting this to 0 prevents <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> from being run again when it reaches the end of a script run by calling <code>ctest -S</code>.  </p>
<h3>CTEST_SCP_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Legacy option. Not used.  </p>
<h3>CTEST_SCRIPT_DIRECTORY</h3>
<p>The directory containing the top-level CTest script. The concept is similar to <code>CMAKE_SOURCE_DIR</code>.  </p>
<h3>CTEST_SITE</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>Site</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_SUBMIT_URL</h3>
<p>New in version 3.14. </p>
<p>Specify the CTest <code>SubmitURL</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_SOURCE_DIRECTORY</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>SourceDirectory</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_SVN_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>SVNCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_SVN_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>SVNOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_SVN_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>SVNUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_TEST_LOAD</h3>
<p>New in version 3.4. </p>
<p>Specify the <code>TestLoad</code> setting in the CTest Test Step of a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script. This sets the default value for the <code>TEST_LOAD</code> option of the <code>ctest_test()</code> command.  </p>
<h3>CTEST_TEST_TIMEOUT</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>TimeOut</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_TRIGGER_SITE</h3>
<p>New in version 3.1. </p>
<p>Legacy option. Not used.  </p>
<h3>CTEST_UPDATE_COMMAND</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>UpdateCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_UPDATE_OPTIONS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>UpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_UPDATE_VERSION_ONLY</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest UpdateVersionOnly setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_UPDATE_VERSION_OVERRIDE</h3>
<p>New in version 3.15. </p>
<p>Specify the CTest UpdateVersionOverride setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h3>CTEST_USE_LAUNCHERS</h3>
<p>New in version 3.1. </p>
<p>Specify the CTest <code>UseLaunchers</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.  </p>
<h2>VARIABLES FOR CPACK</h2>
<h3>CPACK_ABSOLUTE_DESTINATION_FILES</h3>
<p>List of files which have been installed using an <code>ABSOLUTE DESTINATION</code> path. </p>
<p>This variable is a Read-Only variable which is set internally by CPack during installation and before packaging using <code>CMAKE_ABSOLUTE_DESTINATION_FILES</code> defined in <code>cmake_install.cmake</code> scripts. The value can be used within CPack project configuration file and/or <code>CPack&lt;GEN&gt;.cmake</code> file of <code>&lt;GEN&gt;</code> generator.  </p>
<h3>CPACK_COMPONENT_INCLUDE_TOPLEVEL_DIRECTORY</h3>
<p>Boolean toggle to include/exclude top level directory (component case). </p>
<p>Similar usage as <code>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</code> but for the component case. See <code>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</code> documentation for the detail.  </p>
<h3>CPACK_CUSTOM_INSTALL_VARIABLES</h3>
<p>New in version 3.21. </p>
<p>CPack variables (set via e.g. <code>cpack -D</code>, <code>CPackConfig.cmake</code> or <code>CPACK_PROJECT_CONFIG_FILE</code> scripts) are not directly visible in installation scripts. Instead, one can pass a list of <code>varName=value</code> pairs in the <code>CPACK_CUSTOM_INSTALL_VARIABLES</code> variable. At install time, each list item will result in a variable of the specified name (<code>varName</code>) being set to the given <code>value</code>. The <code>=</code> can be omitted for an empty <code>value</code>. </p>
<p> <code>CPACK_CUSTOM_INSTALL_VARIABLES</code> allows the packaging installation to be influenced by the user or driving script at CPack runtime without having to regenerate the install scripts.  </p>
<h3>Example</h3>
<pre><code>install(FILES large.txt DESTINATION data)
install(CODE [[
  if(ENABLE_COMPRESSION)
    # &quot;run-compressor&quot; is a fictional tool that produces
    # large.txt.xz from large.txt and then removes the input file
    execute_process(COMMAND run-compressor $ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/large.txt)
  endif()
]])
</code></pre>
<p>With the above example snippet, <code>cpack</code> will by default run the installation script with <code>ENABLE_COMPRESSION</code> unset, resulting in a package containing the uncompressed <code>large.txt</code>. This can be overridden when invoking <code>cpack</code> like so: </p>
<pre><code>cpack -D &quot;CPACK_CUSTOM_INSTALL_VARIABLES=ENABLE_COMPRESSION=TRUE&quot;
</code></pre>
<p>The installation script will then run with <code>ENABLE_COMPRESSION</code> set to <code>TRUE</code>, resulting in a package containing the compressed <code>large.txt.xz</code> instead.  </p>
<h3>CPACK_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</h3>
<p>Ask CPack to error out as soon as a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p>The fatal error is emitted before the installation of the offending file takes place. Some CPack generators, like <code>NSIS</code>, enforce this internally. This variable triggers the definition of <code>CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</code> when CPack runs.  </p>
<h3>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</h3>
<p>Boolean toggle to include/exclude top level directory. </p>
<p>When preparing a package CPack installs the item under the so-called top level directory. The purpose of is to include (set to <code>1</code> or <code>ON</code> or <code>TRUE</code>) the top level directory in the package or not (set to <code>0</code> or <code>OFF</code> or <code>FALSE</code>). </p>
<p>Each CPack generator has a built-in default value for this variable. E.g. Archive generators (ZIP, TGZ, ...) includes the top level whereas RPM or DEB don&#8217;t. The user may override the default value by setting this variable. </p>
<p>There is a similar variable <code>CPACK_COMPONENT_INCLUDE_TOPLEVEL_DIRECTORY</code> which may be used to override the behavior for the component packaging case which may have different default value for historical (now backward compatibility) reason.  </p>
<h3>CPACK_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</h3>
<p>New in version 3.11. </p>
<p>Default permissions for implicitly created directories during packaging. </p>
<p>This variable serves the same purpose during packaging as the <code>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</code> variable serves during installation (e.g. <code>make install</code>). </p>
<p>If <i>include(CPack)</i> is used then by default this variable is set to the content of <code>CMAKE_INSTALL_DEFAULT_DIRECTORY_PERMISSIONS</code>.  </p>
<h3>CPACK_PACKAGING_INSTALL_PREFIX</h3>
<p>The prefix used in the built package. </p>
<p>Each CPack generator has a default value (like <code>/usr</code>). This default value may be overwritten from the <code>CMakeLists.txt</code> or the <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> command line by setting an alternative value. Example: </p>
<pre><code>set(CPACK_PACKAGING_INSTALL_PREFIX &quot;/opt&quot;)
</code></pre>
<p>This is not the same purpose as <code>CMAKE_INSTALL_PREFIX</code> which is used when installing from the build tree without building a package.  </p>
<h3>CPACK_SET_DESTDIR</h3>
<p>Boolean toggle to make CPack use <code>DESTDIR</code> mechanism when packaging. </p>
<p> <code>DESTDIR</code> means DESTination DIRectory. It is commonly used by makefile users in order to install software at non-default location. It is a basic relocation mechanism that should not be used on Windows (see <code>CMAKE_INSTALL_PREFIX</code> documentation). It is usually invoked like this: </p>
<pre><code>make DESTDIR=/home/john install
</code></pre>
<p>which will install the concerned software using the installation prefix, e.g. <code>/usr/local</code> prepended with the <code>DESTDIR</code> value which finally gives <code>/home/john/usr/local</code>. When preparing a package, CPack first installs the items to be packaged in a local (to the build tree) directory by using the same <code>DESTDIR</code> mechanism. Nevertheless, if <code>CPACK_SET_DESTDIR</code> is set then CPack will set <code>DESTDIR</code> before doing the local install. The most noticeable difference is that without <code>CPACK_SET_DESTDIR</code>, CPack uses <code>CPACK_PACKAGING_INSTALL_PREFIX</code> as a prefix whereas with <code>CPACK_SET_DESTDIR</code> set, CPack will use <code>CMAKE_INSTALL_PREFIX</code> as a prefix. </p>
<p>Manually setting <code>CPACK_SET_DESTDIR</code> may help (or simply be necessary) if some install rules uses absolute <code>DESTINATION</code> (see CMake <code>install()</code> command). However, starting with CPack/CMake 2.8.3 RPM and DEB installers tries to handle <code>DESTDIR</code> automatically so that it is seldom necessary for the user to set it.  </p>
<h3>CPACK_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</h3>
<p>Ask CPack to warn each time a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p>This variable triggers the definition of <code>CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</code> when CPack runs <code>cmake_install.cmake</code> scripts.  </p>
<h2>VARIABLE EXPANSION OPERATORS</h2>
<h3>CACHE</h3>
<p>New in version 3.13. </p>
<p>Operator to read cache variables. </p>
<p>Use the syntax <code>$CACHE{VAR}</code> to read cache entry <code>VAR</code>. See the <a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7) variables documentation for more complete documentation of the interaction of normal variables and cache entries. </p>
<p>When evaluating Variable References of the form <code>${VAR}</code>, CMake first searches for a normal variable with that name, and if not found CMake will search for a cache entry with that name. The <code>$CACHE{VAR}</code> syntax can be used to do direct cache lookup and ignore any existing normal variable. </p>
<p>See the <code>set()</code> and <code>unset()</code> commands to see how to write or remove cache variables.  </p>
<h3>ENV</h3>
<p>Operator to read environment variables. </p>
<p>Use the syntax <code>$ENV{VAR}</code> to read environment variable <code>VAR</code>. </p>
<p>To test whether an environment variable is defined, use the signature <code>if(DEFINED ENV{&lt;name&gt;})</code> of the <code>if()</code> command. </p>
<p>See the <code>set()</code> and <code>unset()</code> commands to see how to write or remove environment variables.  </p>
<h2>INTERNAL VARIABLES</h2>
<p>CMake has many internal variables. Most of them are undocumented. Some of them, however, were at some point described as normal variables, and therefore may be encountered in legacy code. They are subject to change, and not recommended for use in project code.  </p>
<h3>CMAKE_HOME_DIRECTORY</h3>
<p>Path to top of source tree. Same as <code>CMAKE_SOURCE_DIR</code>. </p>
<p>This is an internal cache entry used to locate the source directory when loading a <code>CMakeCache.txt</code> from a build tree. It should not be used in project code. The variable <code>CMAKE_SOURCE_DIR</code> has the same value and should be preferred.  </p>
<h3>CMAKE_INTERNAL_PLATFORM_ABI</h3>
<p>An internal variable subject to change. </p>
<p>This is used in determining the compiler ABI and is subject to change.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_ABI</h3>
<p>An internal variable subject to change. </p>
<p>This is used in determining the compiler ABI and is subject to change.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_ARCHITECTURE_ID</h3>
<p>New in version 3.10. </p>
<p>An internal variable subject to change. </p>
<p>This is used to identify the variant of a compiler based on its target architecture. For some compilers this is needed to determine the correct usage.  </p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_VERSION_INTERNAL</h3>
<p>New in version 3.10. </p>
<p>An internal variable subject to change. </p>
<p>This is used to identify the variant of a compiler based on an internal version number. For some compilers this is needed to determine the correct usage.  </p>
<h3>CMAKE_&lt;LANG&gt;_PLATFORM_ID</h3>
<p>An internal variable subject to change. </p>
<p>This is used in determining the platform and is subject to change.  </p>
<h3>CMAKE_NOT_USING_CONFIG_FLAGS</h3>
<p>Skip <code>_BUILD_TYPE</code> flags if true. </p>
<p>This is an internal flag used by the generators in CMake to tell CMake to skip the <code>_BUILD_TYPE</code> flags.  </p>
<h3>CMAKE_VS_INTEL_Fortran_PROJECT_VERSION</h3>
<p>When generating for <code>Visual Studio 9 2008</code> or greater with the Intel Fortran plugin installed, this specifies the <code>.vfproj</code> project file format version. This is intended for internal use by CMake and should not be used by project code.  </p>
<h2>COPYRIGHT</h2>
<p> 2000-2022 Kitware, Inc. and Contributors </p>
