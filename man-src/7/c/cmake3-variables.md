---
title: "cmake3-variables(7)"
name: "cmake3-variables"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-variables/"
description: "cmake-variables – CMake Variables Reference"
---

<p>cmake-variables &#8211; CMake Variables Reference</p>
<h2>Variables That Provide Information</h2>
<h3>Cmake_Argc</h3>
<p>Number of command line arguments passed to CMake in script mode. </p>
<p> When run in <i>-P</i> script mode, CMake sets this variable to the number of command line arguments. See also <code>CMAKE_ARGV0</code>, <code>1</code>, <code>2</code> &#8230;</p>
<h3>Cmake_Argv0</h3>
<p>Command line argument passed to CMake in script mode. </p>
<p> When run in <i>-P</i> script mode, CMake sets this variable to the first command line argument. It then also sets <code>CMAKE_ARGV1</code>, <code>CMAKE_ARGV2</code>, &#8230; and so on, up to the number of command line arguments given. See also <code>CMAKE_ARGC</code>.</p>
<h3>Cmake_Ar</h3>
<p>Name of archiving tool for static libraries. </p>
<p> This specifies the name of the program that creates archive or static libraries.</p>
<h3>Cmake_Binary_Dir</h3>
<p>The path to the top level of the build tree. </p>
<p> This is the full path to the top level of the current CMake build tree. For an in-source build, this would be the same as <code>CMAKE_SOURCE_DIR</code>. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Build_Tool</h3>
<p>This variable exists only for backwards compatibility. It contains the same value as <code>CMAKE_MAKE_PROGRAM</code>. Use that variable instead.</p>
<h3>Cmake_Cachefile_Dir</h3>
<p>The directory with the <code>CMakeCache.txt</code> file. </p>
<p> This is the full path to the directory that has the <code>CMakeCache.txt</code> file in it. This is the same as <code>CMAKE_BINARY_DIR</code>.</p>
<h3>Cmake_Cache_Major_Version</h3>
<p>Major version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the major version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cache_Minor_Version</h3>
<p>Minor version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the minor version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cache_Patch_Version</h3>
<p>Patch version of CMake used to create the <code>CMakeCache.txt</code> file </p>
<p> This stores the patch version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file.</p>
<h3>Cmake_Cfg_Intdir</h3>
<p>Build-time reference to per-configuration output subdirectory. </p>
<p> For native build systems supporting multiple configurations in the build tree (such as <i>Visual Studio Generators</i> and <code>Xcode</code>), the value is a reference to a build-time variable specifying the name of the per-configuration output subdirectory. On <i>Makefile Generators</i> this evaluates to <i>.</i> because there is only one configuration in a build tree. Example values: </p>
<pre>$(ConfigurationName) = Visual Studio 7, 8, 9
$(Configuration) = Visual Studio 10
$(CONFIGURATION) = Xcode
. = Make-based tools</pre>
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
<p>The full path to the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> executable. </p>
<p> This is the full path to the CMake executable <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> which is useful from custom commands that want to use the <code>cmake -E</code> option for portable system commands. (e.g. <code>/usr/local/bin/cmake</code>)</p>
<h3>Cmake_Crosscompiling</h3>
<p>Is CMake currently cross compiling. </p>
<p> This variable will be set to true by CMake if CMake is cross compiling. Specifically if the build platform is different from the target platform.</p>
<h3>Cmake_Crosscompiling_Emulator</h3>
<p>This variable is only used when <code>CMAKE_CROSSCOMPILING</code> is on. It should point to a command on the host system that can run executable built for the target system. </p>
<p> The command will be used to run <code>try_run()</code> generated executables, which avoids manual population of the TryRunResults.cmake file. </p>
<p> It is also used as the default value for the <code>CROSSCOMPILING_EMULATOR</code> target property of executables.</p>
<h3>Cmake_Ctest_Command</h3>
<p>Full path to <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> command installed with CMake. </p>
<p> This is the full path to the CTest executable <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> which is useful from custom commands that want to use the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-E</code> option for portable system commands.</p>
<h3>Cmake_Current_Binary_Dir</h3>
<p>The path to the binary directory currently being processed. </p>
<p> This the full path to the build directory that is currently being processed by cmake. Each directory added by <code>add_subdirectory()</code> will create a binary directory in the build tree, and as it is being processed this variable will be set. For in-source builds this is the current source directory being processed. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
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
<p> This is the line number of the file currently being processed by cmake.</p>
<h3>Cmake_Current_Source_Dir</h3>
<p>The path to the source directory currently being processed. </p>
<p> This the full path to the source directory that is currently being processed by cmake. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Dl_Libs</h3>
<p>Name of library containing <code>dlopen</code> and <code>dlcose</code>. </p>
<p> The name of the library that has <code>dlopen</code> and <code>dlclose</code> in it, usually <code>-ldl</code> on most UNIX machines.</p>
<h3>Cmake_Edit_Command</h3>
<p>Full path to <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake3/">ccmake3</a>(1)</code>. Defined only for <i>Makefile Generators</i> when not using an &quot;extra&quot; generator for an IDE. </p>
<p> This is the full path to the CMake executable that can graphically edit the cache. For example, <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> or <code><a href="/docs/linux/man/1-ccmake3/">ccmake3</a>(1)</code>.</p>
<h3>Cmake_Executable_Suffix</h3>
<p>The suffix for executables on this platform. </p>
<p> The suffix to use for the end of an executable filename if any, <code>.exe</code> on Windows. </p>
<p> <code>CMAKE_EXECUTABLE_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Extra_Generator</h3>
<p>The extra generator used to build the project. See <code><a href="/docs/linux/man/7-cmake3-generators/">cmake3-generators</a>(7)</code>. </p>
<p> When using the Eclipse, CodeBlocks or KDevelop generators, CMake generates Makefiles (<code>CMAKE_GENERATOR</code>) and additionally project files for the respective IDE. This IDE project file generator is stored in <code>CMAKE_EXTRA_GENERATOR</code> (e.g. <code>Eclipse CDT4</code>).</p>
<h3>Cmake_Extra_Shared_Library_Suffixes</h3>
<p>Additional suffixes for shared libraries. </p>
<p> Extensions for shared libraries other than that specified by <code>CMAKE_SHARED_LIBRARY_SUFFIX</code>, if any. CMake uses this to recognize external shared library files during analysis of libraries linked by a target.</p>
<h3>Cmake_Find_Package_Name</h3>
<p>Defined by the <code>find_package()</code> command while loading a find module to record the caller-specified package name. See command documentation for details.</p>
<h3>Cmake_Generator</h3>
<p>The generator used to build the project. See <code><a href="/docs/linux/man/7-cmake3-generators/">cmake3-generators</a>(7)</code>. </p>
<p> The name of the generator that is being used to generate the build files. (e.g. <code>Unix Makefiles</code>, <code>Ninja</code>, etc.)</p>
<h3>Cmake_Generator_Platform</h3>
<p>Generator-specific target platform name specified by user. </p>
<p> Some CMake generators support a target platform name to be given to the native build system to choose a compiler toolchain. If the user specifies a platform name (e.g. via the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-A</code> option) the value will be available in this variable. </p>
<p> The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_PLATFORM</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior.</p>
<h3>Cmake_Generator_Toolset</h3>
<p>Native build system toolset name specified by user. </p>
<p> Some CMake generators support a toolset name to be given to the native build system to choose a compiler. If the user specifies a toolset name (e.g. via the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-T</code> option) the value will be available in this variable. </p>
<p> The value of this variable should never be modified by project code. A toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable may initialize <code>CMAKE_GENERATOR_TOOLSET</code>. Once a given build tree has been initialized with a particular value for this variable, changing the value has undefined behavior.</p>
<h3>Cmake_Home_Directory</h3>
<p>Path to top of source tree. </p>
<p> This is the path to the top level of the source tree.</p>
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
<h3>Cmake_Link_Library_Suffix</h3>
<p>The suffix for libraries that you link to. </p>
<p> The suffix to use for the end of a library filename, <code>.lib</code> on Windows.</p>
<h3>Cmake_Link_Search_End_Static</h3>
<p>End a link line such that static system libraries are used. </p>
<p> Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default CMake adds an option at the end of the library list (if necessary) to set the linker search type back to its starting type. This property switches the final linker search type to <code>-Bstatic</code> regardless of how it started. </p>
<p> This variable is used to initialize the target property <code>LINK_SEARCH_END_STATIC</code> for all targets. If set, it&#8217;s value is also used by the <code>try_compile()</code> command. </p>
<p> See also <code>CMAKE_LINK_SEARCH_START_STATIC</code>.</p>
<h3>Cmake_Link_Search_Start_Static</h3>
<p>Assume the linker looks for static libraries by default. </p>
<p> Some linkers support switches such as <code>-Bstatic</code> and <code>-Bdynamic</code> to determine whether to use static or shared libraries for <code>-lXXX</code> options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default the linker search type is assumed to be <code>-Bdynamic</code> at the beginning of the library list. This property switches the assumption to <code>-Bstatic</code>. It is intended for use when linking an executable statically (e.g. with the GNU <code>-static</code> option). </p>
<p> This variable is used to initialize the target property <code>LINK_SEARCH_START_STATIC</code> for all targets. If set, it&#8217;s value is also used by the <code>try_compile()</code> command. </p>
<p> See also <code>CMAKE_LINK_SEARCH_END_STATIC</code>.</p>
<h3>Cmake_Major_Version</h3>
<p>First version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Make_Program</h3>
<p>Tool that can launch the native build system. The value may be the full path to an executable or just the tool name if it is expected to be in the <code>PATH</code>. </p>
<p> The tool selected depends on the <code>CMAKE_GENERATOR</code> used to configure the project:</p>
<dl>
<dt>&bull;</p>
<dd>The <i>Makefile Generators</i> set this to <code>make</code>, <code>gmake</code>, or a generator-specific tool (e.g. <code>nmake</code> for <code>NMake Makefiles</code>). </p>
<p> These generators store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user.</p>
<dt>&bull;</p>
<dd>The <code>Ninja</code> generator sets this to <code>ninja</code>. </p>
<p> This generator stores <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache so that it may be edited by the user.</p>
<dt>&bull;</p>
<dd>The <code>Xcode</code> generator sets this to <code>xcodebuild</code> (or possibly an otherwise undocumented <code>cmakexbuild</code> wrapper implementing some workarounds). </p>
<p> This generator prefers to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because <code>xcodebuild</code> is easy to find, the <code>cmakexbuild</code> wrapper is needed only for older Xcode versions, and the path to <code>cmakexbuild</code> may be outdated if CMake itself moves. </p>
<p> For compatibility with versions of CMake prior to 3.2, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value.</p>
<dt>&bull;</p>
<dd>The <i>Visual Studio Generators</i> set this to the full path to <code>MSBuild.exe</code> (VS &gt;= 10), <code>devenv.com</code> (VS 7,8,9), or <code>VCExpress.exe</code> (VS Express 8,9). (See also variables <code>CMAKE_VS_MSBUILD_COMMAND</code> and <code>CMAKE_VS_DEVENV_COMMAND</code>. </p>
<p> These generators prefer to lookup the build tool at build time rather than to store <code>CMAKE_MAKE_PROGRAM</code> in the CMake cache ahead of time. This is because the tools are version-specific and can be located using the Windows Registry. It is also necessary because the proper build tool may depend on the project content (e.g. the Intel Fortran plugin to VS 10 and 11 requires <code>devenv.com</code> to build its <code>.vfproj</code> project files even though <code>MSBuild.exe</code> is normally preferred to support the <code>CMAKE_GENERATOR_TOOLSET</code>). </p>
<p> For compatibility with versions of CMake prior to 3.0, if a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value if possible.</p>
<dt>&bull;</p>
<dd>The <code>Green Hills MULTI</code> generator sets this to <code>gbuild</code>. If a user or project explicitly adds <code>CMAKE_MAKE_PROGRAM</code> to the CMake cache then CMake will use the specified value. </p>
<p> The <code>CMAKE_MAKE_PROGRAM</code> variable is set for use by project code. The value is also used by the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>&#8211;build</code> and <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> <code>&#8211;build-and-test</code> tools to launch the native build process.</dl>
<h3>Cmake_Match_Count</h3>
<p>The number of matches with the last regular expression. </p>
<p> When a regular expression match is used, CMake fills in <code>CMAKE_MATCH_&lt;n&gt;</code> variables with the match contents. The <code>CMAKE_MATCH_COUNT</code> variable holds the number of match expressions when these are filled.</p>
<h3>Cmake_Minimum_Required_Version</h3>
<p>Version specified to <code>cmake_minimum_required()</code> command </p>
<p> Variable containing the <code>VERSION</code> component specified in the <code>cmake_minimum_required()</code> command.</p>
<h3>Cmake_Minor_Version</h3>
<p>Second version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Parent_List_File</h3>
<p>Full path to the CMake file that included the current one. </p>
<p> While processing a CMake file loaded by <code>include()</code> or <code>find_package()</code> this variable contains the full path to the file including it. The top of the include stack is always the <code>CMakeLists.txt</code> for the current directory. See also <code>CMAKE_CURRENT_LIST_FILE</code>.</p>
<h3>Cmake_Patch_Version</h3>
<p>Third version number component of the <code>CMAKE_VERSION</code> variable.</p>
<h3>Cmake_Project_Name</h3>
<p>The name of the current project. </p>
<p> This specifies name of the current project from the closest inherited <code>project()</code> command.</p>
<h3>Cmake_Ranlib</h3>
<p>Name of randomizing tool for static libraries. </p>
<p> This specifies name of the program that randomizes libraries on UNIX, not used on Windows, but may be present.</p>
<h3>Cmake_Root</h3>
<p>Install directory for running cmake. </p>
<p> This is the install root for the running CMake and the <code>Modules</code> directory can be found here. This is commonly used in this format: <code>${CMAKE_ROOT}/Modules</code></p>
<h3>Cmake_Script_Mode_File</h3>
<p>Full path to the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-P</code> script file currently being processed. </p>
<p> When run in <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-P</code> script mode, CMake sets this variable to the full path of the script file. When run to configure a <code>CMakeLists.txt</code> file, this variable is not set.</p>
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
<p> If <code>TRUE</code>, cmake will neither generate installaton rules nor will it generate <code>cmake_install.cmake</code> files. This variable is <code>FALSE</code> by default.</p>
<h3>Cmake_Skip_Rpath</h3>
<p>If true, do not add run time path information. </p>
<p> If this is set to <code>TRUE</code>, then the rpath information is not added to compiled executables. The default is to add rpath information if the platform supports it. This allows for easy running from the build tree. To omit RPATH in the install step, but not the build step, use <code>CMAKE_SKIP_INSTALL_RPATH</code> instead.</p>
<h3>Cmake_Source_Dir</h3>
<p>The path to the top level of the source tree. </p>
<p> This is the full path to the top level of the current CMake source tree. For an in-source build, this would be the same as <code>CMAKE_BINARY_DIR</code>. </p>
<p> When run in -P script mode, CMake sets the variables <code>CMAKE_BINARY_DIR</code>, <code>CMAKE_SOURCE_DIR</code>, <code>CMAKE_CURRENT_BINARY_DIR</code> and <code>CMAKE_CURRENT_SOURCE_DIR</code> to the current working directory.</p>
<h3>Cmake_Static_Library_Prefix</h3>
<p>The prefix for static libraries that you link to. </p>
<p> The prefix to use for the name of a static library, <code>lib</code> on UNIX. </p>
<p> <code>CMAKE_STATIC_LIBRARY_PREFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Static_Library_Suffix</h3>
<p>The suffix for static libraries that you link to. </p>
<p> The suffix to use for the end of a static library filename, <code>.lib</code> on Windows. </p>
<p> <code>CMAKE_STATIC_LIBRARY_SUFFIX_&lt;LANG&gt;</code> overrides this for language <code>&lt;LANG&gt;</code>.</p>
<h3>Cmake_Toolchain_File</h3>
<p>Path to toolchain file supplied to <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code>. </p>
<p> This variable is specified on the command line when cross-compiling with CMake. It is the path to a file which is read early in the CMake run and which specifies locations for compilers and toolchain utilities, and other target platform and compiler related information.</p>
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
<p> Use the <code>if()</code> command <code>VERSION_LESS</code>, <code>VERSION_EQUAL</code>, or <code>VERSION_GREATER</code> operators to compare version string values against <code>CMAKE_VERSION</code> using a component-wise test. Version component values may be 10 or larger so do not attempt to compare version strings as floating-point numbers. </p>
<p> <code>NOTE:</code> CMake versions 2.8.2 through 2.8.12 used three components for the feature level. Release versions represented the bug-fix level in a fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;[.&lt;tweak&gt;][-rc&lt;n&gt;]</code>. Development versions represented the development date in the fourth component, i.e. <code>&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;.&lt;date&gt;[-&lt;id&gt;]</code>. </p>
<p> CMake versions prior to 2.8.2 used three components for the feature level and had no bug-fix component. Release versions used an even-valued second component, i.e. <code>&lt;major&gt;.&lt;even-minor&gt;.&lt;patch&gt;[-rc&lt;n&gt;]</code>. Development versions used an odd-valued second component with the development date as the third component, i.e. <code>&lt;major&gt;.&lt;odd-minor&gt;.&lt;date&gt;</code>. </p>
<p> The <code>CMAKE_VERSION</code> variable is defined by CMake 2.6.3 and higher. Earlier versions defined only the individual component variables.</dl>
<h3>Cmake_Vs_Devenv_Command</h3>
<p>The generators for <code>Visual Studio 7</code> and above set this variable to the <code>devenv.com</code> command installed with the corresponding Visual Studio version. Note that this variable may be empty on Visual Studio Express editions because they do not provide this tool. </p>
<p> This variable is not defined by other generators even if <code>devenv.com</code> is installed on the computer. </p>
<p> The <code>CMAKE_VS_MSBUILD_COMMAND</code> is also provided for <code>Visual Studio 10 2010</code> and above. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.</p>
<h3>CMAKE_VS_INTEL_Fortran_PROJECT_VERSION</h3>
<p>When generating for <code>Visual Studio 7</code> or greater with the Intel Fortran plugin installed, this specifies the <code>.vfproj</code> project file format version. This is intended for internal use by CMake and should not be used by project code.</p>
<h3>Cmake_Vs_Msbuild_Command</h3>
<p>The generators for <code>Visual Studio 10 2010</code> and above set this variable to the <code>MSBuild.exe</code> command installed with the corresponding Visual Studio version. </p>
<p> This variable is not defined by other generators even if <code>MSBuild.exe</code> is installed on the computer. </p>
<p> The <code>CMAKE_VS_DEVENV_COMMAND</code> is also provided for the non-Express editions of Visual Studio. See also the <code>CMAKE_MAKE_PROGRAM</code> variable.</p>
<h3>CMAKE_VS_NsightTegra_VERSION</h3>
<p>When using a Visual Studio generator with the <code>CMAKE_SYSTEM_NAME</code> variable set to <code>Android</code>, this variable contains the version number of the installed NVIDIA Nsight Tegra Visual Studio Edition.</p>
<h3>Cmake_Vs_Platform_Name</h3>
<p>Visual Studio target platform name. </p>
<p> VS 8 and above allow project files to specify a target platform. CMake provides the name of the chosen platform in this variable.</p>
<h3>Cmake_Vs_Platform_Toolset</h3>
<p>Visual Studio Platform Toolset name. </p>
<p> VS 10 and above use MSBuild under the hood and support multiple compiler toolchains. CMake may specify a toolset explicitly, such as <code>v110</code> for VS 11 or <code>Windows7.1SDK</code> for 64-bit support in VS 10 Express. CMake provides the name of the chosen toolset in this variable.</p>
<h3>Cmake_Vs_Windows_Target_Platform_Version</h3>
<p>Visual Studio Windows Target Platform Version. </p>
<p> When targeting Windows 10 and above Visual Studio 2015 and above support specification of a target Windows version to select a corresponding SDK. The <code>CMAKE_SYSTEM_VERSION</code> variable may be set to specify a version. Otherwise CMake computes a default version based on the Windows SDK versions available. The chosen Windows target version number is provided in <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION</code>. If no Windows 10 SDK is available this value will be empty.</p>
<h3>Cmake_Xcode_Platform_Toolset</h3>
<p>Xcode compiler selection. </p>
<p> <code>Xcode</code> supports selection of a compiler from one of the installed toolsets. CMake provides the name of the chosen toolset in this variable, if any is explicitly selected (e.g. via the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-T</code> option).</p>
<h3>Project_Binary_Dir</h3>
<p>Full path to build directory for project. </p>
<p> This is the binary directory of the most recent <code>project()</code> command.</p>
<h3>&lt;PROJECT-NAME&gt;_BINARY_DIR</h3>
<p>Top level binary directory for the named project. </p>
<p> A variable is created with the name used in the <code>project()</code> command, and is the binary directory for the project. This can be useful when <code>add_subdirectory()</code> is used to connect several projects.</p>
<h3>Project_Name</h3>
<p>Name of the project given to the project command. </p>
<p> This is the name given to the most recent <code>project()</code> command.</p>
<h3>&lt;PROJECT-NAME&gt;_SOURCE_DIR</h3>
<p>Top level source directory for the named project. </p>
<p> A variable is created with the name used in the <code>project()</code> command, and is the source directory for the project. This can be useful when <code>add_subdirectory()</code> is used to connect several projects.</p>
<h3>&lt;PROJECT-NAME&gt;_VERSION</h3>
<p>Value given to the <code>VERSION</code> option of the most recent call to the <code>project()</code> command with project name <code>&lt;PROJECT-NAME&gt;</code>, if any. </p>
<p> See also the component-wise version variables <code>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MINOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_PATCH</code>, and <code>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</code>.</p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</h3>
<p>First version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_MINOR</h3>
<p>Second version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_PATCH</h3>
<p>Third version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</h3>
<p>Fourth version number component of the <code>&lt;PROJECT-NAME&gt;_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>Project_Source_Dir</h3>
<p>Top level source directory for the current project. </p>
<p> This is the source directory of the most recent <code>project()</code> command.</p>
<h3>Project_Version</h3>
<p>Value given to the <code>VERSION</code> option of the most recent call to the <code>project()</code> command, if any. </p>
<p> See also the component-wise version variables <code>PROJECT_VERSION_MAJOR</code>, <code>PROJECT_VERSION_MINOR</code>, <code>PROJECT_VERSION_PATCH</code>, and <code>PROJECT_VERSION_TWEAK</code>.</p>
<h3>Project_Version_Major</h3>
<p>First version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>Project_Version_Minor</h3>
<p>Second version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>Project_Version_Patch</h3>
<p>Third version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h3>Project_Version_Tweak</h3>
<p>Fourth version number component of the <code>PROJECT_VERSION</code> variable as set by the <code>project()</code> command.</p>
<h2>Variables That Change Behavior</h2>
<h3>Build_Shared_Libs</h3>
<p>Global flag to cause <code>add_library()</code> to create shared libraries if on. </p>
<p> If present and true, this will cause all libraries to be built shared unless the library was explicitly added as a static library. This variable is often added to projects as an <code>option()</code> so that each user of a project can decide if they want to build the project using shared or static libraries.</p>
<h3>Cmake_Absolute_Destination_Files</h3>
<p>List of files which have been installed using an <code>ABSOLUTE DESTINATION</code> path. </p>
<p> This variable is defined by CMake-generated <code>cmake_install.cmake</code> scripts. It can be used (read-only) by programs or scripts that source those install scripts. This is used by some CPack generators (e.g. RPM).</p>
<h3>Cmake_Appbundle_Path</h3>
<p><i>;-list</i> of directories specifying a search path for OS X application bundles used by the <code>find_program()</code>, and <code>find_package()</code> commands.</p>
<h3>Cmake_Automoc_Relaxed_Mode</h3>
<p>Switch between strict and relaxed automoc mode. </p>
<p> By default, <code>AUTOMOC</code> behaves exactly as described in the documentation of the <code>AUTOMOC</code> target property. When set to <code>TRUE</code>, it accepts more input and tries to find the correct input file for <code>moc</code> even if it differs from the documented behaviour. In this mode it e.g. also checks whether a header file is intended to be processed by moc when a <code>&quot;foo.moc&quot;</code> file has been included. </p>
<p> Relaxed mode has to be enabled for KDE4 compatibility.</p>
<h3>Cmake_Backwards_Compatibility</h3>
<p>Deprecated. See CMake Policy <code>CMP0001</code> documentation.</p>
<h3>Cmake_Build_Type</h3>
<p>Specifies the build type on single-configuration generators. </p>
<p> This statically specifies what build type (configuration) will be built in this build tree. Possible values are empty, <code>Debug</code>, <code>Release</code>, <code>RelWithDebInfo</code> and <code>MinSizeRel</code>. This variable is only meaningful to single-configuration generators (such as <i>Makefile Generators</i> and <code>Ninja</code>) i.e. those which choose a single configuration when CMake runs to generate a build tree as opposed to multi-configuration generators which offer selection of the build configuration within the generated build environment. There are many per-config properties and variables (usually following clean <code>SOME_VAR_&lt;CONFIG&gt;</code> order conventions), such as <code>CMAKE_C_FLAGS_&lt;CONFIG&gt;</code>, specified as uppercase: <code>CMAKE_C_FLAGS_[DEBUG|RELEASE|RELWITHDEBINFO|MINSIZEREL]</code>. For example, in a build tree configured to build type <code>Debug</code>, CMake will see to having <code>CMAKE_C_FLAGS_DEBUG</code> settings get added to the <code>CMAKE_C_FLAGS</code> settings. See also <code>CMAKE_CONFIGURATION_TYPES</code>.</p>
<h3>Cmake_Color_Makefile</h3>
<p>Enables color output when using the <i>Makefile Generators</i>. </p>
<p> When enabled, the generated Makefiles will produce colored output. Default is <code>ON</code>.</p>
<h3>Cmake_Configuration_Types</h3>
<p>Specifies the available build types on multi-config generators. </p>
<p> This specifies what build types (configurations) will be available such as <code>Debug</code>, <code>Release</code>, <code>RelWithDebInfo</code> etc. This has reasonable defaults on most platforms, but can be extended to provide other build types. See also <code>CMAKE_BUILD_TYPE</code> for details of managing configuration data, and <code>CMAKE_CFG_INTDIR</code>.</p>
<h3>Cmake_Debug_Target_Properties</h3>
<p>Enables tracing output for target properties. </p>
<p> This variable can be populated with a list of properties to generate debug output for when evaluating target properties. Currently it can only be used when evaluating the <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code>, <code>COMPILE_OPTIONS</code>, <code>AUTOUIC_OPTIONS</code>, <code>SOURCES</code>, <code>COMPILE_FEATURES</code>, <code>POSITION_INDEPENDENT_CODE</code> target properties and any other property listed in <code>COMPATIBLE_INTERFACE_STRING</code> and other <code>COMPATIBLE_INTERFACE_</code> properties. It outputs an origin for each entry in the target property. Default is unset.</p>
<h3>Cmake_Depends_In_Project_Only</h3>
<p>When set to <code>TRUE</code> in a directory, the build system produced by the <i>Makefile Generators</i> is set up to only consider dependencies on source files that appear either in the source or in the binary directories. Changes to source files outside of these directories will not cause rebuilds. </p>
<p> This should be used carefully in cases where some source files are picked up through external headers during the build.</p>
<h3>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</h3>
<p>Variable for disabling <code>find_package()</code> calls. </p>
<p> Every non-<code>REQUIRED</code> <code>find_package()</code> call in a project can be disabled by setting the variable <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> to <code>TRUE</code>. This can be used to build a project without an optional package, although that package is installed. </p>
<p> This switch should be used during the initial CMake run. Otherwise if the package has already been found in a previous CMake run, the variables which have been stored in the cache will still be there. In that case it is recommended to remove the cache variables for this package from the cache using the cache editor or <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> <code>-U</code></p>
<h3>Cmake_Eclipse_Generate_Linked_Resources</h3>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> The Eclipse project generator generates so-called linked resources e.g. to the subproject root dirs in the source tree or to the source files of targets. This can be disabled by setting this variable to FALSE.</p>
<h3>Cmake_Eclipse_Generate_Source_Project</h3>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> If this variable is set to TRUE, the Eclipse project generator will generate an Eclipse project in <code>CMAKE_SOURCE_DIR</code> . This project can then be used in Eclipse e.g. for the version control functionality. <code>CMAKE_ECLIPSE_GENERATE_SOURCE_PROJECT</code> defaults to FALSE; so nothing is written into the source directory.</p>
<h3>Cmake_Eclipse_Make_Arguments</h3>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> This variable holds arguments which are used when Eclipse invokes the make tool. By default it is initialized to hold flags to enable parallel builds (using -j typically).</p>
<h3>Cmake_Eclipse_Version</h3>
<p>This cache variable is used by the Eclipse project generator. See <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code>. </p>
<p> When using the Eclipse project generator, CMake tries to find the Eclipse executable and detect the version of it. Depending on the version it finds, some features are enabled or disabled. If CMake doesn&#8217;t find Eclipse, it assumes the oldest supported version, Eclipse Callisto (3.2).</p>
<h3>Cmake_Error_Deprecated</h3>
<p>Whether to issue errors for deprecated functionality. </p>
<p> If <code>TRUE</code>, use of deprecated functionality will issue fatal errors. If this variable is not set, CMake behaves as if it were set to <code>FALSE</code>.</p>
<h3>Cmake_Error_On_Absolute_Install_Destination</h3>
<p>Ask <code>cmake_install.cmake</code> script to error out as soon as a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p> The fatal error is emitted before the installation of the offending file takes place. This variable is used by CMake-generated <code>cmake_install.cmake</code> scripts. If one sets this variable to <code>ON</code> while running the script, it may get fatal error messages from the script.</p>
<h3>Cmake_Export_Compile_Commands</h3>
<p>Enable/Disable output of compile commands during generation. </p>
<p> If enabled, generates a <code>compile_commands.json</code> file containing the exact compiler calls for all translation units of the project in machine-readable form. The format of the JSON file looks like: </p>
<pre>[
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
]</pre>
<p><code>NOTE:</code> This option is implemented only by <i>Makefile Generators</i> and the <code>Ninja</code>. It is ignored on other generators.</p>
<h3>Cmake_Export_No_Package_Registry</h3>
<p>Disable the <code>export(PACKAGE)</code> command. </p>
<p> In some cases, for example for packaging and for system wide installations, it is not desirable to write the user package registry. If the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> variable is enabled, the <code>export(PACKAGE)</code> command will do nothing. </p>
<p> See also <i>Disabling the Package Registry</i>.</p>
<h3>Cmake_Sysroot</h3>
<p>Path to pass to the compiler in the <code>&#8211;sysroot</code> flag. </p>
<p> The <code>CMAKE_SYSROOT</code> content is passed to the compiler in the <code>&#8211;sysroot</code> flag, if supported. The path is also stripped from the RPATH/RUNPATH if necessary on installation. The <code>CMAKE_SYSROOT</code> is also used to prefix paths searched by the <code>find_*</code> commands. </p>
<p> This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.</p>
<h3>Cmake_Find_Appbundle</h3>
<p>This variable affects how <code>find_*</code> commands choose between OS X Application Bundles and unix-style package components. </p>
<p> On Darwin or systems supporting OS X Application Bundles, the <code>CMAKE_FIND_APPBUNDLE</code> variable can be set to empty or one of the following:</p>
<dl>
<dt><code>FIRST</code></p>
<dd>Try to find application bundles before standard programs. This is the default on Darwin.</p>
<dt><code>LAST</code></p>
<dd>Try to find application bundles after standard programs.</p>
<dt><code>ONLY</code></p>
<dd>Only try to find application bundles.</p>
<dt><code>NEVER</code></p>
<dd>Never try to find application bundles.</dl>
<h3>Cmake_Find_Framework</h3>
<p>This variable affects how <code>find_*</code> commands choose between OS X Frameworks and unix-style package components. </p>
<p> On Darwin or systems supporting OS X Frameworks, the <code>CMAKE_FIND_FRAMEWORK</code> variable can be set to empty or one of the following:</p>
<dl>
<dt><code>FIRST</code></p>
<dd>Try to find frameworks before standard libraries or headers. This is the default on Darwin.</p>
<dt><code>LAST</code></p>
<dd>Try to find frameworks after standard libraries or headers.</p>
<dt><code>ONLY</code></p>
<dd>Only try to find frameworks.</p>
<dt><code>NEVER</code></p>
<dd>Never try to find frameworks.</dl>
<h3>Cmake_Find_Library_Prefixes</h3>
<p>Prefixes to prepend when looking for libraries. </p>
<p> This specifies what prefixes to add to library names when the <code>find_library()</code> command looks for libraries. On UNIX systems this is typically <code>lib</code>, meaning that when trying to find the <code>foo</code> library it will look for <code>libfoo</code>.</p>
<h3>Cmake_Find_Library_Suffixes</h3>
<p>Suffixes to append when looking for libraries. </p>
<p> This specifies what suffixes to add to library names when the <code>find_library()</code> command looks for libraries. On Windows systems this is typically <code>.lib</code> and <code>.dll</code>, meaning that when trying to find the <code>foo</code> library it will look for <code>foo.dll</code> etc.</p>
<h3>Cmake_Find_No_Install_Prefix</h3>
<p>Ignore the <code>CMAKE_INSTALL_PREFIX</code> when searching for assets. </p>
<p> CMake adds the <code>CMAKE_INSTALL_PREFIX</code> and the <code>CMAKE_STAGING_PREFIX</code> variable to the <code>CMAKE_SYSTEM_PREFIX_PATH</code> by default. This variable may be set on the command line to control that behavior. </p>
<p> Set <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> to <code>TRUE</code> to tell <code>find_package()</code> not to search in the <code>CMAKE_INSTALL_PREFIX</code> or <code>CMAKE_STAGING_PREFIX</code> by default. Note that the prefix may still be searched for other reasons, such as being the same prefix as the CMake installation, or for being a built-in system prefix.</p>
<h3>Cmake_Find_Package_No_Package_Registry</h3>
<p>Skip <i>User Package Registry</i> in <code>find_package()</code> calls. </p>
<p> In some cases, for example to locate only system wide installations, it is not desirable to use the <i>User Package Registry</i> when searching for packages. If the <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> variable is enabled, all the <code>find_package()</code> commands will skip the <i>User Package Registry</i> as if they were called with the <code>NO_CMAKE_PACKAGE_REGISTRY</code> argument. </p>
<p> See also <i>Disabling the Package Registry</i>.</p>
<h3>Cmake_Find_Package_No_System_Package_Registry</h3>
<p>Skip <i>System Package Registry</i> in <code>find_package()</code> calls. </p>
<p> In some cases, it is not desirable to use the <i>System Package Registry</i> when searching for packages. If the <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> variable is enabled, all the <code>find_package()</code> commands will skip the <i>System Package Registry</i> as if they were called with the <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> argument. </p>
<p> See also <i>Disabling the Package Registry</i>.</p>
<h3>Cmake_Find_Package_Warn_No_Module</h3>
<p>Tell <code>find_package()</code> to warn if called without an explicit mode. </p>
<p> If <code>find_package()</code> is called without an explicit mode option (<code>MODULE</code>, <code>CONFIG</code>, or <code>NO_MODULE</code>) and no <code>Find&lt;pkg&gt;.cmake</code> module is in <code>CMAKE_MODULE_PATH</code> then CMake implicitly assumes that the caller intends to search for a package configuration file. If no package configuration file is found then the wording of the failure message must account for both the case that the package is really missing and the case that the project has a bug and failed to provide the intended Find module. If instead the caller specifies an explicit mode option then the failure message can be more specific. </p>
<p> Set <code>CMAKE_FIND_PACKAGE_WARN_NO_MODULE</code> to <code>TRUE</code> to tell <code>find_package()</code> to warn when it implicitly assumes Config mode. This helps developers enforce use of an explicit mode in all calls to <code>find_package()</code> within a project.</p>
<h3>Cmake_Find_Root_Path</h3>
<p><i>;-list</i> of root paths to search on the filesystem. </p>
<p> This variable is most useful when cross-compiling. CMake uses the paths in this list as alternative roots to find filesystem items with <code>find_package()</code>, <code>find_library()</code> etc.</p>
<h3>Cmake_Find_Root_Path_Mode_Include</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_file()</code> and <code>find_path()</code>. </p>
<p> If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.</p>
<h3>Cmake_Find_Root_Path_Mode_Library</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_library()</code>. </p>
<p> If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.</p>
<h3>Cmake_Find_Root_Path_Mode_Package</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_package()</code>. </p>
<p> If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.</p>
<h3>Cmake_Find_Root_Path_Mode_Program</h3>
<p>This variable controls whether the <code>CMAKE_FIND_ROOT_PATH</code> and <code>CMAKE_SYSROOT</code> are used by <code>find_program()</code>. </p>
<p> If set to <code>ONLY</code>, then only the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be searched. If set to <code>NEVER</code>, then the roots in <code>CMAKE_FIND_ROOT_PATH</code> will be ignored and only the host system root will be used. If set to <code>BOTH</code>, then the host system paths and the paths in <code>CMAKE_FIND_ROOT_PATH</code> will be searched.</p>
<h3>Cmake_Framework_Path</h3>
<p><i>;-list</i> of directories specifying a search path for OS X frameworks used by the <code>find_library()</code>, <code>find_package()</code>, <code>find_path()</code>, and <code>find_file()</code> commands.</p>
<h3>Cmake_Ignore_Path</h3>
<p><i>;-list</i> of directories to be <i>ignored</i> by the <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. This is useful in cross-compiling environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine. </p>
<p> By default this is empty; it is intended to be set by the project. Note that <code>CMAKE_IGNORE_PATH</code> takes a list of directory names, <i>not</i> a list of prefixes. To ignore paths under prefixes (<code>bin</code>, <code>include</code>, <code>lib</code>, etc.), specify them explicitly. </p>
<p> See also the <code>CMAKE_PREFIX_PATH</code>, <code>CMAKE_LIBRARY_PATH</code>, <code>CMAKE_INCLUDE_PATH</code>, and <code>CMAKE_PROGRAM_PATH</code> variables.</p>
<h3>Cmake_Include_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_file()</code> and <code>find_path()</code> commands. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_INCLUDE_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.</p>
<h3>Cmake_Include_Directories_Before</h3>
<p>Whether to append or prepend directories by default in <code>include_directories()</code>. </p>
<p> This variable affects the default behavior of the <code>include_directories()</code> command. Setting this variable to <code>ON</code> is equivalent to using the <code>BEFORE</code> option in all uses of that command.</p>
<h3>Cmake_Include_Directories_Project_Before</h3>
<p>Whether to force prepending of project include directories. </p>
<p> This variable affects the order of include directories generated in compiler command lines. If set to <code>ON</code>, it causes the <code>CMAKE_SOURCE_DIR</code> and the <code>CMAKE_BINARY_DIR</code> to appear first.</p>
<h3>Cmake_Install_Default_Component_Name</h3>
<p>Default component used in <code>install()</code> commands. </p>
<p> If an <code>install()</code> command is used without the <code>COMPONENT</code> argument, these files will be grouped into a default component. The name of this default install component will be taken from this variable. It defaults to <code>Unspecified</code>.</p>
<h3>Cmake_Install_Message</h3>
<p>Specify verbosity of installation script code generated by the <code>install()</code> command (using the <code>file(INSTALL)</code> command). For paths that are newly installed or updated, installation may print lines like: </p>
<pre>-- Installing: /some/destination/path</pre>
<p>For paths that are already up to date, installation may print lines like: </p>
<pre>-- Up-to-date: /some/destination/path</pre>
<p>The <code>CMAKE_INSTALL_MESSAGE</code> variable may be set to control which messages are printed:</p>
<dl>
<dt><code>ALWAYS</code></p>
<dd>Print both <code>Installing</code> and <code>Up-to-date</code> messages.</p>
<dt><code>LAZY</code></p>
<dd>Print <code>Installing</code> but not <code>Up-to-date</code> messages.</p>
<dt><code>NEVER</code></p>
<dd>Print neither <code>Installing</code> nor <code>Up-to-date</code> messages. </p>
<p> Other values have undefined behavior and may not be diagnosed. </p>
<p> If this variable is not set, the default behavior is <code>ALWAYS</code>.</dl>
<h3>Cmake_Install_Prefix</h3>
<p>Install directory used by <code>install()</code>. </p>
<p> If <code>make install</code> is invoked or <code>INSTALL</code> is built, this directory is prepended onto all install directories. This variable defaults to <code>/usr/local</code> on UNIX and <code>c:/Program Files</code> on Windows. </p>
<p> On UNIX one can use the <code>DESTDIR</code> mechanism in order to relocate the whole installation. <code>DESTDIR</code> means DESTination DIRectory. It is commonly used by makefile users in order to install software at non-default location. It is usually invoked like this: </p>
<pre>make DESTDIR=/home/john install</pre>
<p>which will install the concerned software using the installation prefix, e.g. <code>/usr/local</code> prepended with the <code>DESTDIR</code> value which finally gives <code>/home/john/usr/local</code>. </p>
<p> WARNING: <code>DESTDIR</code> may not be used on Windows because installation prefix usually contains a drive letter like in <code>C:/Program Files</code> which cannot be prepended with some other prefix. </p>
<p> The installation prefix is also added to <code>CMAKE_SYSTEM_PREFIX_PATH</code> so that <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_path()</code>, and <code>find_file()</code> will search the prefix for other software. </p>
<p> <code>NOTE:</code> Use the <code>GNUInstallDirs</code> module to provide GNU-style options for the layout of directories within the installation.</p>
<h3>Cmake_Library_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_library()</code> command. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_LIBRARY_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.</p>
<h3>Cmake_Mfc_Flag</h3>
<p>Tell cmake to use MFC for an executable or dll. </p>
<p> This can be set in a <code>CMakeLists.txt</code> file and will enable MFC in the application. It should be set to <code>1</code> for the static MFC library, and <code>2</code> for the shared MFC library. This is used in Visual Studio 7 project files. The CMakeSetup dialog used MFC and the <code>CMakeLists.txt</code> looks like this: </p>
<pre>add_definitions(-D_AFXDLL)
set(CMAKE_MFC_FLAG 2)
add_executable(CMakeSetup WIN32 ${SRCS})</pre>
<h3>Cmake_Module_Path</h3>
<p><i>;-list</i> of directories specifying a search path for CMake modules to be loaded by the the <code>include()</code> or <code>find_package()</code> commands before checking the default modules that come with CMake. By default it is empty, it is intended to be set by the project.</p>
<h3>Cmake_Not_Using_Config_Flags</h3>
<p>Skip <code>_BUILD_TYPE</code> flags if true. </p>
<p> This is an internal flag used by the generators in CMake to tell CMake to skip the <code>_BUILD_TYPE</code> flags.</p>
<h3>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</h3>
<p>Default for CMake Policy <code>CMP&lt;NNNN&gt;</code> when it is otherwise left unset. </p>
<p> Commands <code>cmake_minimum_required(VERSION)</code> and <code>cmake_policy(VERSION)</code> by default leave policies introduced after the given version unset. Set <code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code> to <code>OLD</code> or <code>NEW</code> to specify the default for policy <code>CMP&lt;NNNN&gt;</code>, where <code>&lt;NNNN&gt;</code> is the policy number. </p>
<p> This variable should not be set by a project in CMake code; use <code>cmake_policy(SET)</code> instead. Users running CMake may set this variable in the cache (e.g. <code>-DCMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;=&lt;OLD|NEW&gt;</code>) to set a policy not otherwise set by the project. Set to <code>OLD</code> to quiet a policy warning while using old behavior or to <code>NEW</code> to try building the project with new behavior.</p>
<h3>CMAKE_POLICY_WARNING_CMP&lt;NNNN&gt;</h3>
<p>Explicitly enable or disable the warning when CMake Policy <code>CMP&lt;NNNN&gt;</code> is not set. This is meaningful only for the few policies that do not warn by default:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_POLICY_WARNING_CMP0025</code> controls the warning for policy <code>CMP0025</code>.</p>
<dt>&bull;</p>
<dd><code>CMAKE_POLICY_WARNING_CMP0047</code> controls the warning for policy <code>CMP0047</code>.</p>
<dt>&bull;</p>
<dd><code>CMAKE_POLICY_WARNING_CMP0056</code> controls the warning for policy <code>CMP0056</code>.</p>
<dt>&bull;</p>
<dd><code>CMAKE_POLICY_WARNING_CMP0060</code> controls the warning for policy <code>CMP0060</code>.</p>
<dt>&bull;</p>
<dd><code>CMAKE_POLICY_WARNING_CMP0065</code> controls the warning for policy <code>CMP0065</code>. </p>
<p> This variable should not be set by a project in CMake code. Project developers running CMake may set this variable in their cache to enable the warning (e.g. <code>-DCMAKE_POLICY_WARNING_CMP&lt;NNNN&gt;=ON</code>). Alternatively, running <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> with the <code>&#8211;debug-output</code>, <code>&#8211;trace</code>, or <code>&#8211;trace-expand</code> option will also enable the warning.</dl>
<h3>Cmake_Prefix_Path</h3>
<p><i>;-list</i> of directories specifying installation <i>prefixes</i> to be searched by the <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. Each command will add appropriate subdirectories (like <code>bin</code>, <code>lib</code>, or <code>include</code>) as specified in its own documentation. </p>
<p> By default this is empty. It is intended to be set by the project. </p>
<p> See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>, <code>CMAKE_INCLUDE_PATH</code>, <code>CMAKE_LIBRARY_PATH</code>, <code>CMAKE_PROGRAM_PATH</code>, and <code>CMAKE_IGNORE_PATH</code>.</p>
<h3>Cmake_Program_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_program()</code> command. By default it is empty, it is intended to be set by the project. See also <code>CMAKE_SYSTEM_PROGRAM_PATH</code> and <code>CMAKE_PREFIX_PATH</code>.</p>
<h3>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</h3>
<p>A CMake language file or module to be included by the <code>project()</code> command. This is is intended for injecting custom code into project builds without modifying their source.</p>
<h3>Cmake_Skip_Install_All_Dependency</h3>
<p>Don&#8217;t make the <code>install</code> target depend on the <code>all</code> target. </p>
<p> By default, the <code>install</code> target depends on the <code>all</code> target. This has the effect, that when <code>make install</code> is invoked or <code>INSTALL</code> is built, first the <code>all</code> target is built, then the installation starts. If <code>CMAKE_SKIP_INSTALL_ALL_DEPENDENCY</code> is set to <code>TRUE</code>, this dependency is not created, so the installation process will start immediately, independent from whether the project has been completely built or not.</p>
<h3>Cmake_Staging_Prefix</h3>
<p>This variable may be set to a path to install to when cross-compiling. This can be useful if the path in <code>CMAKE_SYSROOT</code> is read-only, or otherwise should remain pristine. </p>
<p> The <code>CMAKE_STAGING_PREFIX</code> location is also used as a search prefix by the <code>find_*</code> commands. This can be controlled by setting the <code>CMAKE_FIND_NO_INSTALL_PREFIX</code> variable. </p>
<p> If any RPATH/RUNPATH entries passed to the linker contain the <code>CMAKE_STAGING_PREFIX</code>, the matching path fragments are replaced with the <code>CMAKE_INSTALL_PREFIX</code>.</p>
<h3>Cmake_System_Appbundle_Path</h3>
<p>Search path for OS X application bundles used by the <code>find_program()</code>, and <code>find_package()</code> commands. By default it contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project, use <code>CMAKE_APPBUNDLE_PATH</code> for this.</p>
<h3>Cmake_System_Framework_Path</h3>
<p>Search path for OS X frameworks used by the <code>find_library()</code>, <code>find_package()</code>, <code>find_path()</code>, and <code>find_file()</code> commands. By default it contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project, use <code>CMAKE_FRAMEWORK_PATH</code> for this.</p>
<h3>Cmake_System_Ignore_Path</h3>
<p><i>;-list</i> of directories to be <i>ignored</i> by the <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. This is useful in cross-compiling environments where some system directories contain incompatible but possibly linkable libraries. For example, on cross-compiled cluster environments, this allows a user to ignore directories containing libraries meant for the front-end machine. </p>
<p> By default this contains a list of directories containing incompatible binaries for the host system. See the <code>CMAKE_IGNORE_PATH</code> variable that is intended to be set by the project. </p>
<p> See also the <code>CMAKE_SYSTEM_PREFIX_PATH</code>, <code>CMAKE_SYSTEM_LIBRARY_PATH</code>, <code>CMAKE_SYSTEM_INCLUDE_PATH</code>, and <code>CMAKE_SYSTEM_PROGRAM_PATH</code> variables.</p>
<h3>Cmake_System_Include_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_file()</code> and <code>find_path()</code> commands. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_INCLUDE_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.</p>
<h3>Cmake_System_Library_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_library()</code> command. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_LIBRARY_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.</p>
<h3>Cmake_System_Prefix_Path</h3>
<p><i>;-list</i> of directories specifying installation <i>prefixes</i> to be searched by the <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. Each command will add appropriate subdirectories (like <code>bin</code>, <code>lib</code>, or <code>include</code>) as specified in its own documentation. </p>
<p> By default this contains the standard directories for the current system, the <code>CMAKE_INSTALL_PREFIX</code>, and the <code>CMAKE_STAGING_PREFIX</code>. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_PREFIX_PATH</code> for this. </p>
<p> See also <code>CMAKE_SYSTEM_INCLUDE_PATH</code>, <code>CMAKE_SYSTEM_LIBRARY_PATH</code>, <code>CMAKE_SYSTEM_PROGRAM_PATH</code>, and <code>CMAKE_SYSTEM_IGNORE_PATH</code>.</p>
<h3>Cmake_System_Program_Path</h3>
<p><i>;-list</i> of directories specifying a search path for the <code>find_program()</code> command. By default this contains the standard directories for the current system. It is <i>not</i> intended to be modified by the project; use <code>CMAKE_PROGRAM_PATH</code> for this. See also <code>CMAKE_SYSTEM_PREFIX_PATH</code>.</p>
<h3>Cmake_User_Make_Rules_Override</h3>
<p>Specify a CMake file that overrides platform information. </p>
<p> CMake loads the specified file while enabling support for each language from either the <code>project()</code> or <code>enable_language()</code> commands. It is loaded after CMake&#8217;s builtin compiler and platform information modules have been loaded but before the information is used. The file may set platform information variables to override CMake&#8217;s defaults. </p>
<p> This feature is intended for use only in overriding information variables that must be set before CMake builds its first test project to check that the compiler for a language works. It should not be used to load a file in cases that a normal <code>include()</code> will work. Use it only as a last resort for behavior that cannot be achieved any other way. For example, one may set <code>CMAKE_C_FLAGS_INIT</code> to change the default value used to initialize <code>CMAKE_C_FLAGS</code> before it is cached. The override file should NOT be used to set anything that could be set after languages are enabled, such as variables like <code>CMAKE_RUNTIME_OUTPUT_DIRECTORY</code> that affect the placement of binaries. Information set in the file will be used for <code>try_compile()</code> and <code>try_run()</code> builds too.</p>
<h3>Cmake_Warn_Deprecated</h3>
<p>Whether to issue warnings for deprecated functionality. </p>
<p> If not <code>FALSE</code>, use of deprecated functionality will issue warnings. If this variable is not set, CMake behaves as if it were set to <code>TRUE</code>. </p>
<p> When running <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code>, this option can be enabled with the <code>-Wdeprecated</code> option, or disabled with the <code>-Wno-deprecated</code> option.</p>
<h3>Cmake_Warn_On_Absolute_Install_Destination</h3>
<p>Ask <code>cmake_install.cmake</code> script to warn each time a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p> This variable is used by CMake-generated <code>cmake_install.cmake</code> scripts. If one sets this variable to <code>ON</code> while running the script, it may get warning messages from the script.</p>
<h2>Variables That Describe The System</h2>
<h3>Apple</h3>
<p><code>True</code> if running on OS X. </p>
<p> Set to <code>true</code> on OS X.</p>
<h3>Borland</h3>
<p><code>True</code> if the Borland compiler is being used. </p>
<p> This is set to <code>true</code> if the Borland compiler is being used.</p>
<h3>Cmake_Cl_64</h3>
<p>Using the 64-bit compiler from Microsoft </p>
<p> Set to <code>true</code> when using the 64-bit <code>cl</code> compiler from Microsoft.</p>
<h3>Cmake_Compiler_2005</h3>
<p>Using the Visual Studio 2005 compiler from Microsoft </p>
<p> Set to true when using the Visual Studio 2005 compiler from Microsoft.</p>
<h3>Cmake_Host_Apple</h3>
<p><code>True</code> for Apple OS X operating systems. </p>
<p> Set to <code>true</code> when the host system is Apple OS X.</p>
<h3>Cmake_Host_Solaris</h3>
<p><code>True</code> for Oracle Solaris operating systems. </p>
<p> Set to <code>true</code> when the host system is Oracle Solaris.</p>
<h3>Cmake_Host_System_Name</h3>
<p>Name of the OS CMake is running on. </p>
<p> On systems that have the uname command, this variable is set to the output of <code>uname -s</code>. <code>Linux</code>, <code>Windows</code>, and <code>Darwin</code> for OS X are the values found on the big three operating systems.</p>
<h3>Cmake_Host_System_Processor</h3>
<p>The name of the CPU CMake is running on. </p>
<p> On systems that support <code>uname</code>, this variable is set to the output of <code>uname -p</code>. On Windows it is set to the value of the environment variable <code>PROCESSOR_ARCHITECTURE</code>.</p>
<h3>Cmake_Host_System</h3>
<p>Composit Name of OS CMake is being run on. </p>
<p> This variable is the composite of <code>CMAKE_HOST_SYSTEM_NAME</code> and <code>CMAKE_HOST_SYSTEM_VERSION</code>, e.g. <code>${CMAKE_HOST_SYSTEM_NAME}-${CMAKE_HOST_SYSTEM_VERSION}</code>. If <code>CMAKE_HOST_SYSTEM_VERSION</code> is not set, then this variable is the same as <code>CMAKE_HOST_SYSTEM_NAME</code>.</p>
<h3>Cmake_Host_System_Version</h3>
<p>The OS version CMake is running on. </p>
<p> A numeric version string for the system. On systems that support <code>uname</code>, this variable is set to the output of <code>uname -r</code>. On other systems this is set to major-minor version numbers.</p>
<h3>Cmake_Host_Unix</h3>
<p><code>True</code> for UNIX and UNIX like operating systems. </p>
<p> Set to <code>true</code> when the host system is UNIX or UNIX like (i.e. APPLE and CYGWIN).</p>
<h3>Cmake_Host_Win32</h3>
<p><code>True</code> on Windows systems, including Win64. </p>
<p> Set to <code>true</code> when the host system is Windows and on Cygwin.</p>
<h3>Cmake_Library_Architecture_Regex</h3>
<p>Regex matching possible target architecture library directory names. </p>
<p> This is used to detect <code>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</code> from the implicit linker search path by matching the <code>&lt;arch&gt;</code> name.</p>
<h3>Cmake_Library_Architecture</h3>
<p>Target architecture library directory name, if detected. </p>
<p> This is the value of <code>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</code> as detected for one of the enabled languages.</p>
<h3>Cmake_Object_Path_Max</h3>
<p>Maximum object file full-path length allowed by native build tools. </p>
<p> CMake computes for every source file an object file name that is unique to the source file and deterministic with respect to the full path to the source file. This allows multiple source files in a target to share the same name if they lie in different directories without rebuilding when one is added or removed. However, it can produce long full paths in a few cases, so CMake shortens the path using a hashing scheme when the full path to an object file exceeds a limit. CMake has a built-in limit for each platform that is sufficient for common tools, but some native tools may have a lower limit. This variable may be set to specify the limit explicitly. The value must be an integer no less than 128.</p>
<h3>Cmake_System_Name</h3>
<p>The name of the operating system for which CMake is to build. See the <code>CMAKE_SYSTEM_VERSION</code> variable for the OS version.</p>
<h3>System Name for Host Builds</h3>
<p><code>CMAKE_SYSTEM_NAME</code> is by default set to the same value as the <code>CMAKE_HOST_SYSTEM_NAME</code> variable so that the build targets the host system.</p>
<h3>System Name for Cross Compiling</h3>
<p><code>CMAKE_SYSTEM_NAME</code> may be set explicitly when first configuring a new build tree in order to enable <i>cross compiling</i>. In this case the <code>CMAKE_SYSTEM_VERSION</code> variable must also be set explicitly.</p>
<h3>Cmake_System_Processor</h3>
<p>The name of the CPU CMake is building for. </p>
<p> This variable is the same as <code>CMAKE_HOST_SYSTEM_PROCESSOR</code> if you build for the host system instead of the target system when cross compiling.</p>
<dl>
<dt>&bull;</p>
<dd>The <code>Green Hills MULTI</code> generator sets this to <code>ARM</code> by default.</dl>
<h3>Cmake_System</h3>
<p>Composite name of operating system CMake is compiling for. </p>
<p> This variable is the composite of <code>CMAKE_SYSTEM_NAME</code> and <code>CMAKE_SYSTEM_VERSION</code>, e.g. <code>${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_VERSION}</code>. If <code>CMAKE_SYSTEM_VERSION</code> is not set, then this variable is the same as <code>CMAKE_SYSTEM_NAME</code>.</p>
<h3>Cmake_System_Version</h3>
<p>The version of the operating system for which CMake is to build. See the <code>CMAKE_SYSTEM_NAME</code> variable for the OS name.</p>
<h3>System Version for Host Builds</h3>
<p>When the <code>CMAKE_SYSTEM_NAME</code> variable takes its default value then <code>CMAKE_SYSTEM_VERSION</code> is by default set to the same value as the <code>CMAKE_HOST_SYSTEM_VERSION</code> variable so that the build targets the host system version. </p>
<p> In the case of a host build then <code>CMAKE_SYSTEM_VERSION</code> may be set explicitly when first configuring a new build tree in order to enable targeting the build for a different version of the host operating system than is actually running on the host. This is allowed and not considered cross compiling so long as the binaries built for the specified OS version can still run on the host.</p>
<h3>System Version for Cross Compiling</h3>
<p>When the <code>CMAKE_SYSTEM_NAME</code> variable is set explicitly to enable <i>cross compiling</i> then the value of <code>CMAKE_SYSTEM_VERSION</code> must also be set explicitly to specify the target system version.</p>
<h3>Cygwin</h3>
<p><code>True</code> for Cygwin. </p>
<p> Set to <code>true</code> when using Cygwin.</p>
<h3>Env</h3>
<p>Access environment variables. </p>
<p> Use the syntax <code>$ENV{VAR}</code> to read environment variable <code>VAR</code>. See also the <code>set()</code> command to set <code>ENV{VAR}</code>.</p>
<h3>Ghs-Multi</h3>
<p>True when using Green Hills MULTI</p>
<h3>Mingw</h3>
<p><code>True</code> when using MinGW </p>
<p> Set to <code>true</code> when the compiler is some version of MinGW.</p>
<h3>Msvc10</h3>
<p><code>True</code> when using Microsoft Visual C++ 10.0 </p>
<p> Set to <code>true</code> when the compiler is version 10.0 of Microsoft Visual C++.</p>
<h3>Msvc11</h3>
<p><code>True</code> when using Microsoft Visual C++ 11.0 </p>
<p> Set to <code>true</code> when the compiler is version 11.0 of Microsoft Visual C++.</p>
<h3>Msvc12</h3>
<p><code>True</code> when using Microsoft Visual C++ 12.0. </p>
<p> Set to <code>true</code> when the compiler is version 12.0 of Microsoft Visual C++.</p>
<h3>Msvc14</h3>
<p><code>True</code> when using Microsoft Visual C++ 14.0. </p>
<p> Set to <code>true</code> when the compiler is version 14.0 of Microsoft Visual C++.</p>
<h3>Msvc60</h3>
<p><code>True</code> when using Microsoft Visual C++ 6.0. </p>
<p> Set to <code>true</code> when the compiler is version 6.0 of Microsoft Visual C++.</p>
<h3>Msvc70</h3>
<p><code>True</code> when using Microsoft Visual C++ 7.0. </p>
<p> Set to <code>true</code> when the compiler is version 7.0 of Microsoft Visual C++.</p>
<h3>Msvc71</h3>
<p><code>True</code> when using Microsoft Visual C++ 7.1. </p>
<p> Set to <code>true</code> when the compiler is version 7.1 of Microsoft Visual C++.</p>
<h3>Msvc80</h3>
<p><code>True</code> when using Microsoft Visual C++ 8.0. </p>
<p> Set to <code>true</code> when the compiler is version 8.0 of Microsoft Visual C++.</p>
<h3>Msvc90</h3>
<p><code>True</code> when using Microsoft Visual C++ 9.0. </p>
<p> Set to <code>true</code> when the compiler is version 9.0 of Microsoft Visual C++.</p>
<h3>Msvc_Ide</h3>
<p><code>True</code> when using the Microsoft Visual C++ IDE. </p>
<p> Set to <code>true</code> when the target platform is the Microsoft Visual C++ IDE, as opposed to the command line compiler.</p>
<h3>Msvc</h3>
<p><code>True</code> when using Microsoft Visual C++. </p>
<p> Set to <code>true</code> when the compiler is some version of Microsoft Visual C++.</p>
<h3>Msvc_Version</h3>
<p>The version of Microsoft Visual C/C++ being used if any. </p>
<p> Known version numbers are: </p>
<pre>1200 = VS 6.0
1300 = VS 7.0
1310 = VS 7.1
1400 = VS 8.0
1500 = VS 9.0
1600 = VS 10.0
1700 = VS 11.0
1800 = VS 12.0
1900 = VS 14.0</pre>
<h3>Unix</h3>
<p><code>True</code> for UNIX and UNIX like operating systems. </p>
<p> Set to <code>true</code> when the target system is UNIX or UNIX like (i.e. <code>APPLE</code> and <code>CYGWIN</code>).</p>
<h3>Win32</h3>
<p><code>True</code> on Windows systems, including Win64. </p>
<p> Set to <code>true</code> when the target system is Windows.</p>
<h3>Wince</h3>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsCE</code>.</p>
<h3>Windows_Phone</h3>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsPhone</code>.</p>
<h3>Windows_Store</h3>
<p>True when the <code>CMAKE_SYSTEM_NAME</code> variable is set to <code>WindowsStore</code>.</p>
<h3>Xcode_Version</h3>
<p>Version of Xcode (<code>Xcode</code> generator only). </p>
<p> Under the Xcode generator, this is the version of Xcode as specified in <code>Xcode.app/Contents/version.plist</code> (such as <code>3.1.2</code>).</p>
<h2>Variables That Control The Build</h2>
<h3>Cmake_Android_Ant_Additional_Options</h3>
<p>Default value for the <code>ANDROID_ANT_ADDITIONAL_OPTIONS</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Api</h3>
<p>Default value for the <code>ANDROID_API</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Api_Min</h3>
<p>Default value for the <code>ANDROID_API_MIN</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Arch</h3>
<p>Default value for the <code>ANDROID_ARCH</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Assets_Directories</h3>
<p>Default value for the <code>ANDROID_ASSETS_DIRECTORIES</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Gui</h3>
<p>Default value for the <code>ANDROID_GUI</code> target property of executables. See that target property for additional information.</p>
<h3>Cmake_Android_Jar_Dependencies</h3>
<p>Default value for the <code>ANDROID_JAR_DEPENDENCIES</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Jar_Directories</h3>
<p>Default value for the <code>ANDROID_JAR_DIRECTORIES</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Java_Source_Dir</h3>
<p>Default value for the <code>ANDROID_JAVA_SOURCE_DIR</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Native_Lib_Dependencies</h3>
<p>Default value for the <code>ANDROID_NATIVE_LIB_DEPENDENCIES</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Native_Lib_Directories</h3>
<p>Default value for the <code>ANDROID_NATIVE_LIB_DIRECTORIES</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Process_Max</h3>
<p>Default value for the <code>ANDROID_PROCESS_MAX</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Proguard</h3>
<p>Default value for the <code>ANDROID_PROGUARD</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Proguard_Config_Path</h3>
<p>Default value for the <code>ANDROID_PROGUARD_CONFIG_PATH</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Secure_Props_Path</h3>
<p>Default value for the <code>ANDROID_SECURE_PROPS_PATH</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Skip_Ant_Step</h3>
<p>Default value for the <code>ANDROID_SKIP_ANT_STEP</code> target property. See that target property for additional information.</p>
<h3>Cmake_Android_Stl_Type</h3>
<p>Default value for the <code>ANDROID_STL_TYPE</code> target property. See that target property for additional information.</p>
<h3>Cmake_Archive_Output_Directory</h3>
<p>Where to put all the <i>ARCHIVE</i> target files when built. </p>
<p> This variable is used to initialize the <code>ARCHIVE_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Where to put all the <i>ARCHIVE</i> target files when built for a specific configuration. </p>
<p> This variable is used to initialize the <code>ARCHIVE_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Automoc_Moc_Options</h3>
<p>Additional options for <code>moc</code> when using <code>CMAKE_AUTOMOC</code>. </p>
<p> This variable is used to initialize the <code>AUTOMOC_MOC_OPTIONS</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Automoc</h3>
<p>Whether to handle <code>moc</code> automatically for Qt targets. </p>
<p> This variable is used to initialize the <code>AUTOMOC</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Autorcc</h3>
<p>Whether to handle <code>rcc</code> automatically for Qt targets. </p>
<p> This variable is used to initialize the <code>AUTORCC</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Autorcc_Options</h3>
<p>Whether to handle <code>rcc</code> automatically for Qt targets. </p>
<p> This variable is used to initialize the <code>AUTORCC_OPTIONS</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Autouic</h3>
<p>Whether to handle <code>uic</code> automatically for Qt targets. </p>
<p> This variable is used to initialize the <code>AUTOUIC</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Autouic_Options</h3>
<p>Whether to handle <code>uic</code> automatically for Qt targets. </p>
<p> This variable is used to initialize the <code>AUTOUIC_OPTIONS</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Build_With_Install_Rpath</h3>
<p>Use the install path for the <code>RPATH</code>. </p>
<p> Normally CMake uses the build tree for the <code>RPATH</code> when building executables etc on systems that use <code>RPATH</code>. When the software is installed the executables etc are relinked by CMake to have the install <code>RPATH</code>. If this variable is set to true then the software is always built with the install path for the <code>RPATH</code> and does not need to be relinked when installed.</p>
<h3>Cmake_Compile_Pdb_Output_Directory</h3>
<p>Output directory for MS debug symbol <code>.pdb</code> files generated by the compiler while building source files. </p>
<p> This variable is used to initialize the <code>COMPILE_PDB_OUTPUT_DIRECTORY</code> property on all the targets.</p>
<h3>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for MS debug symbol <code>.pdb</code> files generated by the compiler while building source files. </p>
<p> This is a per-configuration version of <code>CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY</code>. This variable is used to initialize the <code>COMPILE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets.</p>
<h3>CMAKE_&lt;CONFIG&gt;_POSTFIX</h3>
<p>Default filename postfix for libraries under configuration <code>&lt;CONFIG&gt;</code>. </p>
<p> When a non-executable target is created its <code>&lt;CONFIG&gt;_POSTFIX</code> target property is initialized with the value of this variable if it is set.</p>
<h3>Cmake_Debug_Postfix</h3>
<p>See variable <code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code>. </p>
<p> This variable is a special case of the more-general <code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code> variable for the <i>DEBUG</i> configuration.</p>
<h3>Cmake_Enable_Exports</h3>
<p>Specify whether an executable exports symbols for loadable modules. </p>
<p> Normally an executable does not export any symbols because it is the final program. It is possible for an executable to export symbols to be used by loadable modules. When this property is set to true CMake will allow other targets to <code>link</code> to the executable with the <code>TARGET_LINK_LIBRARIES()</code> command. On all platforms a target-level dependency on the executable is created for targets that link to it. For DLL platforms an import library will be created for the exported symbols and then used for linking. All Windows-based systems including Cygwin are DLL platforms. For non-DLL platforms that require all symbols to be resolved at link time, such as OS X, the module will <code>link</code> to the executable using a flag like <code>-bundle_loader</code>. For other non-DLL platforms the link rule is simply ignored since the dynamic loader will automatically bind symbols when the module is loaded. </p>
<p> This variable is used to initialize the target property <code>ENABLE_EXPORTS</code> for executable targets.</p>
<h3>CMAKE_EXE_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking an executable. </p>
<p> Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating executables.</p>
<h3>Cmake_Exe_Linker_Flags</h3>
<p>Linker flags to be used to create executables. </p>
<p> These flags will be used by the linker when creating an executable.</p>
<h3>CMAKE_Fortran_FORMAT</h3>
<p>Set to <code>FIXED</code> or <code>FREE</code> to indicate the Fortran source layout. </p>
<p> This variable is used to initialize the <code>Fortran_FORMAT</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_Fortran_MODULE_DIRECTORY</h3>
<p>Fortran module output directory. </p>
<p> This variable is used to initialize the <code>Fortran_MODULE_DIRECTORY</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_GNUtoMS</h3>
<p>Convert GNU import libraries (<code>.dll.a</code>) to MS format (<code>.lib</code>). </p>
<p> This variable is used to initialize the <code>GNUtoMS</code> property on targets when they are created. See that target property for additional information.</p>
<h3>Cmake_Include_Current_Dir_In_Interface</h3>
<p>Automatically add the current source- and build directories to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property. </p>
<p> If this variable is enabled, CMake automatically adds for each shared library target, static library target, module target and executable target, <code>CMAKE_CURRENT_SOURCE_DIR</code> and <code>CMAKE_CURRENT_BINARY_DIR</code> to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property. By default <code>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</code> is <code>OFF</code>.</p>
<h3>Cmake_Include_Current_Dir</h3>
<p>Automatically add the current source- and build directories to the include path. </p>
<p> If this variable is enabled, CMake automatically adds <code>CMAKE_CURRENT_SOURCE_DIR</code> and <code>CMAKE_CURRENT_BINARY_DIR</code> to the include path for each directory. These additional include directories do not propagate down to subdirectories. This is useful mainly for out-of-source builds, where files generated into the build tree are included by files located in the source tree. </p>
<p> By default <code>CMAKE_INCLUDE_CURRENT_DIR</code> is <code>OFF</code>.</p>
<h3>Cmake_Install_Name_Dir</h3>
<p>OS X directory name for installed targets. </p>
<p> <code>CMAKE_INSTALL_NAME_DIR</code> is used to initialize the <code>INSTALL_NAME_DIR</code> property on all targets. See that target property for more information.</p>
<h3>Cmake_Install_Rpath</h3>
<p>The rpath to use for installed targets. </p>
<p> A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This is used to initialize the target property <code>INSTALL_RPATH</code> for all targets.</p>
<h3>Cmake_Install_Rpath_Use_Link_Path</h3>
<p>Add paths to linker search and installed rpath. </p>
<p> <code>CMAKE_INSTALL_RPATH_USE_LINK_PATH</code> is a boolean that if set to <code>true</code> will append directories in the linker search path and outside the project to the <code>INSTALL_RPATH</code>. This is used to initialize the target property <code>INSTALL_RPATH_USE_LINK_PATH</code> for all targets.</p>
<h3>Cmake_Ios_Install_Combined</h3>
<p>Default value for <code>IOS_INSTALL_COMBINED</code> of targets. </p>
<p> This variable is used to initialize the <code>IOS_INSTALL_COMBINED</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_&lt;LANG&gt;_CLANG_TIDY</h3>
<p>Default value for <code>&lt;LANG&gt;_CLANG_TIDY</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</h3>
<p>Default value for <code>&lt;LANG&gt;_COMPILER_LAUNCHER</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</h3>
<p>Default value for <code>&lt;LANG&gt;_INCLUDE_WHAT_YOU_USE</code> target property. This variable is used to initialize the property on each target as it is created. This is done only when <code>&lt;LANG&gt;</code> is <code>C</code> or <code>CXX</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_VISIBILITY_PRESET</h3>
<p>Default value for the <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> target property when a target is created.</p>
<h3>Cmake_Library_Output_Directory</h3>
<p>Where to put all the <i>LIBRARY</i> target files when built. </p>
<p> This variable is used to initialize the <code>LIBRARY_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Where to put all the <i>LIBRARY</i> target files when built for a specific configuration. </p>
<p> This variable is used to initialize the <code>LIBRARY_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Library_Path_Flag</h3>
<p>The flag to be used to add a library search path to a compiler. </p>
<p> The flag will be used to specify a library directory to the compiler. On most compilers this is <code>-L</code>.</p>
<h3>Cmake_Link_Def_File_Flag</h3>
<p>Linker flag to be used to specify a <code>.def</code> file for dll creation. </p>
<p> The flag will be used to add a <code>.def</code> file when creating a dll on Windows; this is only defined on Windows.</p>
<h3>Cmake_Link_Depends_No_Shared</h3>
<p>Whether to skip link dependencies on shared library files. </p>
<p> This variable initializes the <code>LINK_DEPENDS_NO_SHARED</code> property on targets when they are created. See that target property for additional information.</p>
<h3>Cmake_Link_Interface_Libraries</h3>
<p>Default value for <code>LINK_INTERFACE_LIBRARIES</code> of targets. </p>
<p> This variable is used to initialize the <code>LINK_INTERFACE_LIBRARIES</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Link_Library_File_Flag</h3>
<p>Flag to be used to link a library specified by a path to its file. </p>
<p> The flag will be used before a library file path is given to the linker. This is needed only on very few platforms.</p>
<h3>Cmake_Link_Library_Flag</h3>
<p>Flag to be used to link a library into an executable. </p>
<p> The flag will be used to specify a library to link to an executable. On most compilers this is <code>-l</code>.</p>
<h3>Cmake_Macosx_Bundle</h3>
<p>Default value for <code>MACOSX_BUNDLE</code> of targets. </p>
<p> This variable is used to initialize the <code>MACOSX_BUNDLE</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Macosx_Rpath</h3>
<p>Whether to use rpaths on OS X and iOS. </p>
<p> This variable is used to initialize the <code>MACOSX_RPATH</code> property on all targets.</p>
<h3>CMAKE_MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</h3>
<p>Default value for <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> of targets. </p>
<p> This variable is used to initialize the <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_MODULE_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking a module. </p>
<p> Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating modules.</p>
<h3>Cmake_Module_Linker_Flags</h3>
<p>Linker flags to be used to create modules. </p>
<p> These flags will be used by the linker when creating a module.</p>
<h3>Cmake_Ninja_Output_Path_Prefix</h3>
<p>Set output files path prefix for the <code>Ninja</code> generator. </p>
<p> Every output files listed in the generated <code>build.ninja</code> will be prefixed by the contents of this variable (a trailing slash is appended if missing). This is useful when the generated ninja file is meant to be embedded as a <code>subninja</code> file into a <i>super</i> ninja project. For example, a ninja build file generated with a command like: </p>
<pre>cd top-build-dir/sub &amp;&amp;
cmake -G Ninja -DCMAKE_NINJA_OUTPUT_PATH_PREFIX=sub/ path/to/source</pre>
<p>can be embedded in <code>top-build-dir/build.ninja</code> with a directive like this: </p>
<pre>subninja sub/build.ninja</pre>
<p>The <code>auto-regeneration</code> rule in <code>top-build-dir/build.ninja</code> must have an order-only dependency on <code>sub/build.ninja</code>. </p>
<p> <code>NOTE:</code> When <code>CMAKE_NINJA_OUTPUT_PATH_PREFIX</code> is set, the project generated by CMake cannot be used as a standalone project. No default targets are specified.</p>
<h3>Cmake_No_Builtin_Chrpath</h3>
<p>Do not use the builtin ELF editor to fix RPATHs on installation. </p>
<p> When an ELF binary needs to have a different RPATH after installation than it does in the build tree, CMake uses a builtin editor to change the RPATH in the installed copy. If this variable is set to true then CMake will relink the binary before installation instead of using its builtin editor.</p>
<h3>Cmake_No_System_From_Imported</h3>
<p>Default value for <code>NO_SYSTEM_FROM_IMPORTED</code> of targets. </p>
<p> This variable is used to initialize the <code>NO_SYSTEM_FROM_IMPORTED</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Osx_Architectures</h3>
<p>Target specific architectures for OS X and iOS. </p>
<p> This variable is used to initialize the <code>OSX_ARCHITECTURES</code> property on each target as it is creaed. See that target property for additional information. </p>
<p> The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. </p>
<p> This variable is ignored on platforms other than OS X.</p>
<h3>Cmake_Osx_Deployment_Target</h3>
<p>Specify the minimum version of OS X on which the target binaries are to be deployed. CMake uses this value for the <code>-mmacosx-version-min</code> flag and to help choose the default SDK (see <code>CMAKE_OSX_SYSROOT</code>). </p>
<p> If not set explicitly the value is initialized by the <code>MACOSX_DEPLOYMENT_TARGET</code> environment variable, if set, and otherwise computed based on the host platform. </p>
<p> The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. </p>
<p> This variable is ignored on platforms other than OS X.</p>
<h3>Cmake_Osx_Sysroot</h3>
<p>Specify the location or name of the OS X platform SDK to be used. CMake uses this value to compute the value of the <code>-isysroot</code> flag or equivalent and to help the <code>find_*</code> commands locate files in the SDK. </p>
<p> If not set explicitly the value is initialized by the <code>SDKROOT</code> environment variable, if set, and otherwise computed based on the <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> or the host platform. </p>
<p> The value of this variable should be set prior to the first <code>project()</code> or <code>enable_language()</code> command invocation because it may influence configuration of the toolchain and flags. It is intended to be set locally by the user creating a build tree. </p>
<p> This variable is ignored on platforms other than OS X.</p>
<h3>Cmake_Pdb_Output_Directory</h3>
<p>Output directory for MS debug symbol <code>.pdb</code> files generated by the linker for executable and shared library targets. </p>
<p> This variable is used to initialize the <code>PDB_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Per-configuration output directory for MS debug symbol <code>.pdb</code> files generated by the linker for executable and shared library targets. </p>
<p> This is a per-configuration version of <code>CMAKE_PDB_OUTPUT_DIRECTORY</code>. This variable is used to initialize the <code>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.</p>
<h3>Cmake_Position_Independent_Code</h3>
<p>Default value for <code>POSITION_INDEPENDENT_CODE</code> of targets. </p>
<p> This variable is used to initialize the <code>POSITION_INDEPENDENT_CODE</code> property on all the targets. See that target property for additional information. If set, it&#8217;s value is also used by the <code>try_compile()</code> command.</p>
<h3>Cmake_Runtime_Output_Directory</h3>
<p>Where to put all the <i>RUNTIME</i> target files when built. </p>
<p> This variable is used to initialize the <code>RUNTIME_OUTPUT_DIRECTORY</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</h3>
<p>Where to put all the <i>RUNTIME</i> target files when built for a specific configuration. </p>
<p> This variable is used to initialize the <code>RUNTIME_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_SHARED_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking a shared library. </p>
<p> Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating shared libraries.</p>
<h3>Cmake_Shared_Linker_Flags</h3>
<p>Linker flags to be used to create shared libraries. </p>
<p> These flags will be used by the linker when creating a shared library.</p>
<h3>Cmake_Skip_Build_Rpath</h3>
<p>Do not include RPATHs in the build tree. </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with no RPATH.</p>
<h3>Cmake_Skip_Install_Rpath</h3>
<p>Do not include RPATHs in the install tree. </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always installed without RPATH, even if RPATH is enabled when building. This can be useful for example to allow running tests from the build directory with RPATH enabled before the installation step. To omit RPATH in both the build and install steps, use <code>CMAKE_SKIP_RPATH</code> instead.</p>
<h3>CMAKE_STATIC_LINKER_FLAGS_&lt;CONFIG&gt;</h3>
<p>Flags to be used when linking a static library. </p>
<p> Same as <code>CMAKE_C_FLAGS_*</code> but used by the linker when creating static libraries.</p>
<h3>Cmake_Static_Linker_Flags</h3>
<p>Linker flags to be used to create static libraries. </p>
<p> These flags will be used by the linker when creating a static library.</p>
<h3>Cmake_Try_Compile_Configuration</h3>
<p>Build configuration used for <code>try_compile()</code> and <code>try_run()</code> projects. </p>
<p> Projects built by <code>try_compile()</code> and <code>try_run()</code> are built synchronously during the CMake configuration step. Therefore a specific build configuration must be chosen even if the generated build system supports multiple configurations.</p>
<h3>Cmake_Try_Compile_Platform_Variables</h3>
<p>List of variables that the <code>try_compile()</code> command source file signature must propagate into the test project in order to target the same platform as the host project. </p>
<p> This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p> Variables meaningful to CMake, such as <code>CMAKE_&lt;LANG&gt;_FLAGS</code>, are propagated automatically. The <code>CMAKE_TRY_COMPILE_PLATFORM_VARIABLES</code> variable may be set to pass custom variables meaningful to a toolchain file. For example, a toolchain file may contain: </p>
<pre>set(CMAKE_SYSTEM_NAME ...)
set(CMAKE_TRY_COMPILE_PLATFORM_VARIABLES MY_CUSTOM_VARIABLE)
# ... use MY_CUSTOM_VARIABLE ...</pre>
<p>If a user passes <code>-DMY_CUSTOM_VARIABLE=SomeValue</code> to CMake then this setting will be made visible to the toolchain file both for the main project and for test projects generated by the <code>try_compile()</code> command source file signature.</p>
<h3>Cmake_Try_Compile_Target_Type</h3>
<p>Type of target generated for <code>try_compile()</code> calls using the source file signature. Valid values are:</p>
<dl>
<dt><code>EXECUTABLE</code></p>
<dd>Use <code>add_executable()</code> to name the source file in the generated project. This is the default if no value is given.</p>
<dt><code>STATIC_LIBRARY</code></p>
<dd>Use <code>add_library()</code> with the <code>STATIC</code> option to name the source file in the generated project. This avoids running the linker and is intended for use with cross-compiling toolchains that cannot link without custom flags or linker scripts.</dl>
<h3>Cmake_Use_Relative_Paths</h3>
<p>This variable has no effect. The partially implemented effect it had in previous releases was removed in CMake 3.4.</p>
<h3>Cmake_Visibility_Inlines_Hidden</h3>
<p>Default value for the <code>VISIBILITY_INLINES_HIDDEN</code> target property when a target is created.</p>
<h3>Cmake_Vs_Include_Install_To_Default_Build</h3>
<p>Include <code>INSTALL</code> target to default build. </p>
<p> In Visual Studio solution, by default the <code>INSTALL</code> target will not be part of the default build. Setting this variable will enable the <code>INSTALL</code> target to be part of the default build.</p>
<h3>Cmake_Windows_Export_All_Symbols</h3>
<p>Default value for <code>WINDOWS_EXPORT_ALL_SYMBOLS</code> target property. This variable is used to initialize the property on each target as it is created.</p>
<h3>Cmake_Win32_Executable</h3>
<p>Default value for <code>WIN32_EXECUTABLE</code> of targets. </p>
<p> This variable is used to initialize the <code>WIN32_EXECUTABLE</code> property on all the targets. See that target property for additional information.</p>
<h3>CMAKE_XCODE_ATTRIBUTE_&lt;an-attribute&gt;</h3>
<p>Set Xcode target attributes directly. </p>
<p> Tell the <code>Xcode</code> generator to set &#8216;&lt;an-attribute&gt;&#8217; to a given value in the generated Xcode project. Ignored on other generators. </p>
<p> See the <code>XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> target property to set attributes on a specific target. </p>
<p> Contents of <code>CMAKE_XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Executable_Output_Path</h3>
<p>Old executable location variable. </p>
<p> The target property <code>RUNTIME_OUTPUT_DIRECTORY</code> supercedes this variable for a target if it is set. Executable targets are otherwise placed in this directory.</p>
<h3>Library_Output_Path</h3>
<p>Old library location variable. </p>
<p> The target properties <code>ARCHIVE_OUTPUT_DIRECTORY</code>, <code>LIBRARY_OUTPUT_DIRECTORY</code>, and <code>RUNTIME_OUTPUT_DIRECTORY</code> supercede this variable for a target if they are set. Library targets are otherwise placed in this directory.</p>
<h2>Variables For Languages</h2>
<h3>CMAKE_COMPILER_IS_GNU&lt;LANG&gt;</h3>
<p>True if the compiler is GNU. </p>
<p> If the selected <code>&lt;LANG&gt;</code> compiler is the GNU compiler then this is <code>TRUE</code>, if not it is <code>FALSE</code>. Unlike the other per-language variables, this uses the GNU syntax for identifying languages instead of the CMake syntax. Recognized values of the <code>&lt;LANG&gt;</code> suffix are: </p>
<pre>CC = C compiler
CXX = C++ compiler
G77 = Fortran compiler</pre>
<h3>Cmake_C_Compile_Features</h3>
<p>List of features known to the C compiler </p>
<p> These features are known to be available for use with the C compiler. This list is a subset of the features listed in the <code>CMAKE_C_KNOWN_FEATURES</code> global property. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_C_Extensions</h3>
<p>Default value for <code>C_EXTENSIONS</code> property of targets. </p>
<p> This variable is used to initialize the <code>C_EXTENSIONS</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_C_Standard</h3>
<p>Default value for <code>C_STANDARD</code> property of targets. </p>
<p> This variable is used to initialize the <code>C_STANDARD</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_C_Standard_Required</h3>
<p>Default value for <code>C_STANDARD_REQUIRED</code> property of targets. </p>
<p> This variable is used to initialize the <code>C_STANDARD_REQUIRED</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_Cxx_Compile_Features</h3>
<p>List of features known to the C++ compiler </p>
<p> These features are known to be available for use with the C++ compiler. This list is a subset of the features listed in the <code>CMAKE_CXX_KNOWN_FEATURES</code> global property. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_Cxx_Extensions</h3>
<p>Default value for <code>CXX_EXTENSIONS</code> property of targets. </p>
<p> This variable is used to initialize the <code>CXX_EXTENSIONS</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_Cxx_Standard</h3>
<p>Default value for <code>CXX_STANDARD</code> property of targets. </p>
<p> This variable is used to initialize the <code>CXX_STANDARD</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>Cmake_Cxx_Standard_Required</h3>
<p>Default value for <code>CXX_STANDARD_REQUIRED</code> property of targets. </p>
<p> This variable is used to initialize the <code>CXX_STANDARD_REQUIRED</code> property on all targets. See that target property for additional information. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>CMAKE_Fortran_MODDIR_DEFAULT</h3>
<p>Fortran default module output directory. </p>
<p> Most Fortran compilers write <code>.mod</code> files to the current working directory. For those that do not, this is set to <code>.</code> and used when the <code>Fortran_MODULE_DIRECTORY</code> target property is not set.</p>
<h3>CMAKE_Fortran_MODDIR_FLAG</h3>
<p>Fortran flag for module output directory. </p>
<p> This stores the flag needed to pass the value of the <code>Fortran_MODULE_DIRECTORY</code> target property to the compiler.</p>
<h3>CMAKE_Fortran_MODOUT_FLAG</h3>
<p>Fortran flag to enable module output. </p>
<p> Most Fortran compilers write <code>.mod</code> files out by default. For others, this stores the flag needed to enable module output.</p>
<h3>Cmake_Internal_Platform_Abi</h3>
<p>An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change.</p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</h3>
<p>Rule variable to append to a static archive. </p>
<p> This is a rule variable that tells CMake how to append to a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</h3>
<p>Rule variable to create a new static archive. </p>
<p> This is a rule variable that tells CMake how to create a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</h3>
<p>Rule variable to finish an existing static archive. </p>
<p> This is a rule variable that tells CMake how to finish a static archive. It is used in place of <code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code> on some platforms in order to support large object counts. See also <code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code> and <code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILE_OBJECT</h3>
<p>Rule variable to compile a single object file. </p>
<p> This is a rule variable that tells CMake how to compile a single object file for the language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_ABI</h3>
<p>An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_ID</h3>
<p>Compiler identification string. </p>
<p> A short string unique to the compiler vendor. Possible values include: </p>
<pre>Absoft = Absoft Fortran (absoft.com)
ADSP = Analog VisualDSP++ (analog.com)
AppleClang = Apple Clang (apple.com)
ARMCC = ARM Compiler (arm.com)
Bruce = Bruce C Compiler
CCur = Concurrent Fortran (ccur.com)
Clang = LLVM Clang (clang.llvm.org)
Cray = Cray Compiler (cray.com)
Embarcadero, Borland = Embarcadero (embarcadero.com)
G95 = G95 Fortran (g95.org)
GNU = GNU Compiler Collection (gcc.gnu.org)
HP = Hewlett-Packard Compiler (hp.com)
Intel = Intel Compiler (intel.com)
MIPSpro = SGI MIPSpro (sgi.com)
MSVC = Microsoft Visual Studio (microsoft.com)
OpenWatcom = Open Watcom (openwatcom.org)
PGI = The Portland Group (pgroup.com)
PathScale = PathScale (pathscale.com)
SDCC = Small Device C Compiler (sdcc.sourceforge.net)
SunPro = Oracle Solaris Studio (oracle.com)
TI = Texas Instruments (ti.com)
TinyCC = Tiny C Compiler (tinycc.org)
XL, VisualAge, zOS = IBM XL (ibm.com)</pre>
<p>This variable is not guaranteed to be defined for all compilers or languages.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_LOADED</h3>
<p>Defined to true if the language is enabled. </p>
<p> When language <code>&lt;LANG&gt;</code> is enabled by <code>project()</code> or <code>enable_language()</code> this variable is defined to <code>1</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER</h3>
<p>The full path to the compiler for <code>LANG</code>. </p>
<p> This is the command that will be used as the <code>&lt;LANG&gt;</code> compiler. Once set, you can not change this variable.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_EXTERNAL_TOOLCHAIN</h3>
<p>The external toolchain for cross-compiling, if supported. </p>
<p> Some compiler toolchains do not ship their own auxiliary utilities such as archivers and linkers. The compiler driver may support a command-line argument to specify the location of such tools. <code>CMAKE_&lt;LANG&gt;_COMPILER_EXTERNAL_TOOLCHAIN</code> may be set to a path to a path to the external toolchain and will be passed to the compiler driver if supported. </p>
<p> This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</h3>
<p>The target for cross-compiling, if supported. </p>
<p> Some compiler drivers are inherently cross-compilers, such as clang and QNX qcc. These compiler drivers support a command-line argument to specify the target to cross-compile for. </p>
<p> This variable may only be set in a toolchain file specified by the <code>CMAKE_TOOLCHAIN_FILE</code> variable.</p>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</h3>
<p>Compiler version string. </p>
<p> Compiler version in major[.minor[.patch[.tweak]]] format. This variable is not guaranteed to be defined for all compilers or languages.</p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_SHARED_LIBRARY</h3>
<p>Rule variable to create a shared library. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_SHARED_MODULE</h3>
<p>Rule variable to create a shared module. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</h3>
<p>Rule variable to create a static library. </p>
<p> This is a rule variable that tells CMake how to create a static library for the language <code>&lt;LANG&gt;</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</h3>
<p>Flags for <code>Debug</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>Debug</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_MINSIZEREL</h3>
<p>Flags for <code>MinSizeRel</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>MinSizeRel</code> (short for minimum size release).</p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELEASE</h3>
<p>Flags for <code>Release</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>Release</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS_RELWITHDEBINFO</h3>
<p>Flags for <code>RelWithDebInfo</code> type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>RelWithDebInfo</code> (short for Release With Debug Information).</p>
<h3>CMAKE_&lt;LANG&gt;_FLAGS</h3>
<p>Flags for all build types. </p>
<p> <code>&lt;LANG&gt;</code> flags used regardless of the value of <code>CMAKE_BUILD_TYPE</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_GHS_KERNEL_FLAGS_DEBUG</h3>
<p>GHS kernel flags for <code>Debug</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>Debug</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_GHS_KERNEL_FLAGS_MINSIZEREL</h3>
<p>GHS kernel flags for <code>MinSizeRel</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>MinSizeRel</code> (short for minimum size release).</p>
<h3>CMAKE_&lt;LANG&gt;_GHS_KERNEL_FLAGS_RELEASE</h3>
<p>GHS kernel flags for <code>Release</code> build type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>Release</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_GHS_KERNEL_FLAGS_RELWITHDEBINFO</h3>
<p>GHS kernel flags for <code>RelWithDebInfo</code> type or configuration. </p>
<p> <code>&lt;LANG&gt;</code> flags used when <code>CMAKE_BUILD_TYPE</code> is <code>RelWithDebInfo</code> (short for Release With Debug Information).</p>
<h3>CMAKE_&lt;LANG&gt;_IGNORE_EXTENSIONS</h3>
<p>File extensions that should be ignored by the build. </p>
<p> This is a list of file extensions that may be part of a project for a given language but are not compiled.</p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_INCLUDE_DIRECTORIES</h3>
<p>Directories implicitly searched by the compiler for header files. </p>
<p> CMake does not explicitly specify these directories on compiler command lines for language <code>&lt;LANG&gt;</code>. This prevents system include directories from being treated as user include directories on some compilers.</p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_DIRECTORIES</h3>
<p>Implicit linker search path detected for language <code>&lt;LANG&gt;</code>. </p>
<p> Compilers typically pass directories containing language runtime libraries and default library search paths when they invoke a linker. These paths are implicit linker search directories for the compiler&#8217;s language. CMake automatically detects these directories for each language and reports the results in this variable. </p>
<p> When a library in one of these directories is given by full path to <code>target_link_libraries()</code> CMake will generate the <code>-l&lt;name&gt;</code> form on link lines to ensure the linker searches its implicit directories for the library. Note that some toolchains read implicit directories from an environment variable such as <code>LIBRARY_PATH</code> so keep its value consistent when operating in a given build tree.</p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES</h3>
<p>Implicit linker framework search path detected for language <code>&lt;LANG&gt;</code>. </p>
<p> These paths are implicit linker framework search directories for the compiler&#8217;s language. CMake automatically detects these directories for each language and reports the results in this variable.</p>
<h3>CMAKE_&lt;LANG&gt;_IMPLICIT_LINK_LIBRARIES</h3>
<p>Implicit link libraries and flags detected for language <code>&lt;LANG&gt;</code>. </p>
<p> Compilers typically pass language runtime library names and other flags when they invoke a linker. These flags are implicit link options for the compiler&#8217;s language. CMake automatically detects these libraries and flags for each language and reports the results in this variable.</p>
<h3>CMAKE_&lt;LANG&gt;_LIBRARY_ARCHITECTURE</h3>
<p>Target architecture library directory name detected for <code>&lt;LANG&gt;</code>. </p>
<p> If the <code>&lt;LANG&gt;</code> compiler passes to the linker an architecture-specific system library search directory such as <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> this variable contains the <code>&lt;arch&gt;</code> name if/as detected by CMake.</p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES</h3>
<p>True if <code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</code> propagates across targets. </p>
<p> This is used when CMake selects a linker language for a target. Languages compiled directly into the target are always considered. A language compiled into static libraries linked by the target is considered if this variable is true.</p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</h3>
<p>Preference value for linker language selection. </p>
<p> The &quot;linker language&quot; for executable, shared library, and module targets is the language whose compiler will invoke the linker. The <code>LINKER_LANGUAGE</code> target property sets the language explicitly. Otherwise, the linker language is that whose linker preference value is highest among languages compiled and linked into the target. See also the <code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE_PROPAGATES</code> variable.</p>
<h3>CMAKE_&lt;LANG&gt;_LINK_EXECUTABLE</h3>
<p>Rule variable to link an executable. </p>
<p> Rule variable to link an executable for the given language.</p>
<h3>CMAKE_&lt;LANG&gt;_OUTPUT_EXTENSION</h3>
<p>Extension for the output of a compile for a single file. </p>
<p> This is the extension for an object file for the given <code>&lt;LANG&gt;</code>. For example <code>.obj</code> for C on Windows.</p>
<h3>CMAKE_&lt;LANG&gt;_PLATFORM_ID</h3>
<p>An internal variable subject to change. </p>
<p> This is used in determining the platform and is subject to change.</p>
<h3>CMAKE_&lt;LANG&gt;_SIMULATE_ID</h3>
<p>Identification string of &quot;simulated&quot; compiler. </p>
<p> Some compilers simulate other compilers to serve as drop-in replacements. When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> for the simulated compiler.</p>
<h3>CMAKE_&lt;LANG&gt;_SIMULATE_VERSION</h3>
<p>Version string of &quot;simulated&quot; compiler. </p>
<p> Some compilers simulate other compilers to serve as drop-in replacements. When CMake detects such a compiler it sets this variable to what would have been the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> for the simulated compiler.</p>
<h3>CMAKE_&lt;LANG&gt;_SIZEOF_DATA_PTR</h3>
<p>Size of pointer-to-data types for language <code>&lt;LANG&gt;</code>. </p>
<p> This holds the size (in bytes) of pointer-to-data types in the target platform ABI. It is defined for languages <code>C</code> and <code>CXX</code> (C++).</p>
<h3>CMAKE_&lt;LANG&gt;_SOURCE_FILE_EXTENSIONS</h3>
<p>Extensions of source files for the given language. </p>
<p> This is the list of extensions for a given language&#8217;s source files.</p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_INCLUDE_DIRECTORIES</h3>
<p>Include directories to be used for every source file compiled with the <code>&lt;LANG&gt;</code> compiler. This is meant for specification of system include directories needed by the language for the current platform. The directories always appear at the end of the include path passed to the compiler. </p>
<p> This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p> See also <code>CMAKE_&lt;LANG&gt;_STANDARD_LIBRARIES</code>.</p>
<h3>CMAKE_&lt;LANG&gt;_STANDARD_LIBRARIES</h3>
<p>Libraries linked into every executable and shared library linked for language <code>&lt;LANG&gt;</code>. This is meant for specification of system libraries needed by the language for the current platform. </p>
<p> This variable should not be set by project code. It is meant to be set by CMake&#8217;s platform information modules for the current toolchain, or by a toolchain file when used with <code>CMAKE_TOOLCHAIN_FILE</code>. </p>
<p> See also <code>CMAKE_&lt;LANG&gt;_STANDARD_INCLUDE_DIRECTORIES</code>.</p>
<h3>CMAKE_USER_MAKE_RULES_OVERRIDE_&lt;LANG&gt;</h3>
<p>Specify a CMake file that overrides platform information for <code>&lt;LANG&gt;</code>. </p>
<p> This is a language-specific version of <code>CMAKE_USER_MAKE_RULES_OVERRIDE</code> loaded only when enabling language <code>&lt;LANG&gt;</code>.</p>
<h2>Variables For Ctest</h2>
<h3>Ctest_Binary_Directory</h3>
<p>Specify the CTest <code>BuildDirectory</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Build_Command</h3>
<p>Specify the CTest <code>MakeCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Build_Name</h3>
<p>Specify the CTest <code>BuildName</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Bzr_Command</h3>
<p>Specify the CTest <code>BZRCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Bzr_Update_Options</h3>
<p>Specify the CTest <code>BZRUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Change_Id</h3>
<p>Specify the CTest <code>ChangeId</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script. </p>
<p> This setting allows CTest to pass arbitrary information about this build up to CDash. One use of this feature is to allow CDash to post comments on your pull request if anything goes wrong with your build.</p>
<h3>Ctest_Checkout_Command</h3>
<p>Tell the <code>ctest_start()</code> command how to checkout or initialize the source directory in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Configuration_Type</h3>
<p>Specify the CTest <code>DefaultCTestConfigurationType</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Configure_Command</h3>
<p>Specify the CTest <code>ConfigureCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Coverage_Command</h3>
<p>Specify the CTest <code>CoverageCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Cobertura</h3>
<p>Using <i>Cobertura</i> as the coverage generation within your multi-module Java project can generate a series of XML files. </p>
<p> The Cobertura Coverage parser expects to read the coverage data from a single XML file which contains the coverage data for all modules. Cobertura has a program with the ability to merge given <code>cobertura.ser</code> files and then another program to generate a combined XML file from the previous merged file. For command line testing, this can be done by hand prior to CTest looking for the coverage files. For script builds, set the <code>CTEST_COVERAGE_COMMAND</code> variable to point to a file which will perform these same steps, such as a <code>.sh</code> or <code>.bat</code> file. </p>
<pre>set(CTEST_COVERAGE_COMMAND .../run-coverage-and-consolidate.sh)</pre>
<p>where the <code>run-coverage-and-consolidate.sh</code> script is perhaps created by the <code>configure_file()</code> command and might contain the following code: </p>
<pre>#!/usr/bin/env bash
CoberturaFiles=&quot;$(find &quot;/path/to/source&quot; -name &quot;cobertura.ser&quot;)&quot;
SourceDirs=&quot;$(find &quot;/path/to/source&quot; -name &quot;java&quot; -type d)&quot;
cobertura-merge --datafile coberturamerge.ser $CoberturaFiles
cobertura-report --datafile coberturamerge.ser --destination . \
 --format xml $SourceDirs</pre>
<p>The script uses <code>find</code> to capture the paths to all of the <code>cobertura.ser</code> files found below the project&#8217;s source directory. It keeps the list of files and supplies it as an argument to the <code>cobertura-merge</code> program. The <code>&#8211;datafile</code> argument signifies where the result of the merge will be kept. </p>
<p> The combined <code>coberturamerge.ser</code> file is then used to generate the XML report using the <code>cobertura-report</code> program. The call to the cobertura-report program requires some named arguments.</p>
<dl>
<dt><code>&#8211;datafila</code></p>
<dd>path to the merged <code>.ser</code> file</p>
<dt><code>&#8211;destination</code></p>
<dd>path to put the output files(s)</p>
<dt><code>&#8211;format</code></p>
<dd>file format to write output in: xml or html </p>
<p> The rest of the supplied arguments consist of the full paths to the <code>/src/main/java</code> directories of each module within the source tree. These directories are needed and should not be forgotten.</dl>
<h3>Ctest_Coverage_Extra_Flags</h3>
<p>Specify the CTest <code>CoverageExtraFlags</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Curl_Options</h3>
<p>Specify the CTest <code>CurlOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Custom_Coverage_Exclude</h3>
<p>A list of regular expressions which will be used to exclude files by their path from coverage output by the <code>ctest_coverage()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Error_Exception</h3>
<p>A list of regular expressions which will be used to exclude when detecting error messages in build outputs by the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Error_Match</h3>
<p>A list of regular expressions which will be used to detect error messages in build outputs by the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Error_Post_Context</h3>
<p>The number of lines to include as context which follow an error message by the <code>ctest_test()</code> command. The default is 10. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Error_Pre_Context</h3>
<p>The number of lines to include as context which precede an error message by the <code>ctest_test()</code> command. The default is 10. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Maximum_Failed_Test_Output_Size</h3>
<p>When saving a failing test&#8217;s output, this is the maximum size, in bytes, that will be collected by the <code>ctest_test()</code> command. Defaults to 307200 (300 KiB). </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Maximum_Number_Of_Errors</h3>
<p>The maximum number of errors in a single build step which will be detected. After this, the <code>ctest_test()</code> command will truncate the output. Defaults to 50. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Maximum_Number_Of_Warnings</h3>
<p>The maximum number of warnings in a single build step which will be detected. After this, the <code>ctest_test()</code> command will truncate the output. Defaults to 50. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Maximum_Passed_Test_Output_Size</h3>
<p>When saving a passing test&#8217;s output, this is the maximum size, in bytes, that will be collected by the <code>ctest_test()</code> command. Defaults to 1024 (1 KiB). </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Memcheck_Ignore</h3>
<p>A list of regular expressions to use to exclude tests during the <code>ctest_memcheck()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Post_Memcheck</h3>
<p>A list of commands to run at the end of the <code>ctest_memcheck()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Post_Test</h3>
<p>A list of commands to run at the end of the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Pre_Memcheck</h3>
<p>A list of commands to run at the start of the <code>ctest_memcheck()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Pre_Test</h3>
<p>A list of commands to run at the start of the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Test_Ignore</h3>
<p>A list of regular expressions to use to exclude tests during the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Warning_Exception</h3>
<p>A list of regular expressions which will be used to exclude when detecting warning messages in build outputs by the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Custom_Warning_Match</h3>
<p>A list of regular expressions which will be used to detect warning messages in build outputs by the <code>ctest_test()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Cvs_Checkout</h3>
<p>Deprecated. Use <code>CTEST_CHECKOUT_COMMAND</code> instead.</p>
<h3>Ctest_Cvs_Command</h3>
<p>Specify the CTest <code>CVSCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Cvs_Update_Options</h3>
<p>Specify the CTest <code>CVSUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Location</h3>
<p>Specify the CTest <code>DropLocation</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Method</h3>
<p>Specify the CTest <code>DropMethod</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Site</h3>
<p>Specify the CTest <code>DropSite</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Site_Cdash</h3>
<p>Specify the CTest <code>IsCDash</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Site_Password</h3>
<p>Specify the CTest <code>DropSitePassword</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Drop_Site_User</h3>
<p>Specify the CTest <code>DropSiteUser</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Extra_Coverage_Glob</h3>
<p>A list of regular expressions which will be used to find files which should be covered by the <code>ctest_coverage()</code> command. </p>
<p> It is initialized by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code>, but may be edited in a <code>CTestCustom</code> file. See <code>ctest_read_custom_files()</code> documentation.</p>
<h3>Ctest_Git_Command</h3>
<p>Specify the CTest <code>GITCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Git_Init_Submodules</h3>
<p>Specify the CTest <code>GITInitSubmodules</code> setting in a <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Git_Update_Custom</h3>
<p>Specify the CTest <code>GITUpdateCustom</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Git_Update_Options</h3>
<p>Specify the CTest <code>GITUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Hg_Command</h3>
<p>Specify the CTest <code>HGCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Hg_Update_Options</h3>
<p>Specify the CTest <code>HGUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Memorycheck_Command</h3>
<p>Specify the CTest <code>MemoryCheckCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Memorycheck_Command_Options</h3>
<p>Specify the CTest <code>MemoryCheckCommandOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Memorycheck_Sanitizer_Options</h3>
<p>Specify the CTest <code>MemoryCheckSanitizerOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Memorycheck_Suppressions_File</h3>
<p>Specify the CTest <code>MemoryCheckSuppressionFile</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Memorycheck_Type</h3>
<p>Specify the CTest <code>MemoryCheckType</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script. Valid values are <code>Valgrind</code>, <code>Purify</code>, <code>BoundsChecker</code>, and <code>ThreadSanitizer</code>, <code>AddressSanitizer</code>, <code>MemorySanitizer</code>, and <code>UndefinedBehaviorSanitizer</code>.</p>
<h3>Ctest_Nightly_Start_Time</h3>
<p>Specify the CTest <code>NightlyStartTime</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_P4_Client</h3>
<p>Specify the CTest <code>P4Client</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_P4_Command</h3>
<p>Specify the CTest <code>P4Command</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_P4_Options</h3>
<p>Specify the CTest <code>P4Options</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_P4_Update_Options</h3>
<p>Specify the CTest <code>P4UpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Scp_Command</h3>
<p>Specify the CTest <code>SCPCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Site</h3>
<p>Specify the CTest <code>Site</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Source_Directory</h3>
<p>Specify the CTest <code>SourceDirectory</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Svn_Command</h3>
<p>Specify the CTest <code>SVNCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Svn_Options</h3>
<p>Specify the CTest <code>SVNOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Svn_Update_Options</h3>
<p>Specify the CTest <code>SVNUpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Test_Load</h3>
<p>Specify the <code>TestLoad</code> setting in the <i>CTest Test Step</i> of a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script. This sets the default value for the <code>TEST_LOAD</code> option of the <code>ctest_test()</code> command.</p>
<h3>Ctest_Test_Timeout</h3>
<p>Specify the CTest <code>TimeOut</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Trigger_Site</h3>
<p>Specify the CTest <code>TriggerSite</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Update_Command</h3>
<p>Specify the CTest <code>UpdateCommand</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Update_Options</h3>
<p>Specify the CTest <code>UpdateOptions</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Update_Version_Only</h3>
<p>Specify the CTest <code>UpdateVersionOnly</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h3>Ctest_Use_Launchers</h3>
<p>Specify the CTest <code>UseLaunchers</code> setting in a <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> dashboard client script.</p>
<h2>Variables For Cpack</h2>
<h3>Cpack_Absolute_Destination_Files</h3>
<p>List of files which have been installed using an <code>ABSOLUTE DESTINATION</code> path. </p>
<p> This variable is a Read-Only variable which is set internally by CPack during installation and before packaging using <code>CMAKE_ABSOLUTE_DESTINATION_FILES</code> defined in <code>cmake_install.cmake</code> scripts. The value can be used within CPack project configuration file and/or <code>CPack&lt;GEN&gt;.cmake</code> file of <code>&lt;GEN&gt;</code> generator.</p>
<h3>Cpack_Component_Include_Toplevel_Directory</h3>
<p>Boolean toggle to include/exclude top level directory (component case). </p>
<p> Similar usage as <code>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</code> but for the component case. See <code>CPACK_INCLUDE_TOPLEVEL_DIRECTORY</code> documentation for the detail.</p>
<h3>Cpack_Error_On_Absolute_Install_Destination</h3>
<p>Ask CPack to error out as soon as a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p> The fatal error is emitted before the installation of the offending file takes place. Some CPack generators, like NSIS, enforce this internally. This variable triggers the definition of <code>CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION</code> when CPack runs.</p>
<h3>Cpack_Include_Toplevel_Directory</h3>
<p>Boolean toggle to include/exclude top level directory. </p>
<p> When preparing a package CPack installs the item under the so-called top level directory. The purpose of is to include (set to <code>1</code> or <code>ON</code> or <code>TRUE</code>) the top level directory in the package or not (set to <code>0</code> or <code>OFF</code> or <code>FALSE</code>). </p>
<p> Each CPack generator has a built-in default value for this variable. E.g. Archive generators (ZIP, TGZ, &#8230;) includes the top level whereas RPM or DEB don&#8217;t. The user may override the default value by setting this variable. </p>
<p> There is a similar variable <code>CPACK_COMPONENT_INCLUDE_TOPLEVEL_DIRECTORY</code> which may be used to override the behavior for the component packaging case which may have different default value for historical (now backward compatibility) reason.</p>
<h3>Cpack_Install_Script</h3>
<p>Extra CMake script provided by the user. </p>
<p> If set this CMake script will be executed by CPack during its local [CPack-private] installation which is done right before packaging the files. The script is not called by e.g.: <code>make install</code>.</p>
<h3>Cpack_Packaging_Install_Prefix</h3>
<p>The prefix used in the built package. </p>
<p> Each CPack generator has a default value (like <code>/usr</code>). This default value may be overwritten from the <code>CMakeLists.txt</code> or the <code><a href="/docs/linux/man/1-cpack/">cpack</a>(1)</code> command line by setting an alternative value. Example: </p>
<pre>set(CPACK_PACKAGING_INSTALL_PREFIX &quot;/opt&quot;)</pre>
<p>This is not the same purpose as <code>CMAKE_INSTALL_PREFIX</code> which is used when installing from the build tree without building a package.</p>
<h3>Cpack_Set_Destdir</h3>
<p>Boolean toggle to make CPack use <code>DESTDIR</code> mechanism when packaging. </p>
<p> <code>DESTDIR</code> means DESTination DIRectory. It is commonly used by makefile users in order to install software at non-default location. It is a basic relocation mechanism that should not be used on Windows (see <code>CMAKE_INSTALL_PREFIX</code> documentation). It is usually invoked like this: </p>
<pre>make DESTDIR=/home/john install</pre>
<p>which will install the concerned software using the installation prefix, e.g. <code>/usr/local</code> prepended with the <code>DESTDIR</code> value which finally gives <code>/home/john/usr/local</code>. When preparing a package, CPack first installs the items to be packaged in a local (to the build tree) directory by using the same <code>DESTDIR</code> mechanism. Nevertheless, if <code>CPACK_SET_DESTDIR</code> is set then CPack will set <code>DESTDIR</code> before doing the local install. The most noticeable difference is that without <code>CPACK_SET_DESTDIR</code>, CPack uses <code>CPACK_PACKAGING_INSTALL_PREFIX</code> as a prefix whereas with <code>CPACK_SET_DESTDIR</code> set, CPack will use <code>CMAKE_INSTALL_PREFIX</code> as a prefix. </p>
<p> Manually setting <code>CPACK_SET_DESTDIR</code> may help (or simply be necessary) if some install rules uses absolute <code>DESTINATION</code> (see CMake <code>install()</code> command). However, starting with CPack/CMake 2.8.3 RPM and DEB installers tries to handle <code>DESTDIR</code> automatically so that it is seldom necessary for the user to set it.</p>
<h3>Cpack_Warn_On_Absolute_Install_Destination</h3>
<p>Ask CPack to warn each time a file with absolute <code>INSTALL DESTINATION</code> is encountered. </p>
<p> This variable triggers the definition of <code>CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION</code> when CPack runs <code>cmake_install.cmake</code> scripts.</p>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
