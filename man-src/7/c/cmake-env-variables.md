---
title: "cmake-env-variables(7)"
name: "cmake-env-variables"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-env-variables/"
description: "cmake-env-variables – CMake Environment Variables Reference"
---

<p>cmake-env-variables &#8211; CMake Environment Variables Reference </p>
<p> This page lists environment variables that have special meaning to CMake. </p>
<p> For general information on environment variables, see the Environment Variables section in the cmake-language manual.</p>
<h2>Environment Variables That Change Behavior</h2>
<h3>Cmake_Prefix_Path</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The <code>CMAKE_PREFIX_PATH</code> environment variable may be set to a list of directories specifying installation <i>prefixes</i> to be searched by the <code>find_package()</code>, <code>find_program()</code>, <code>find_library()</code>, <code>find_file()</code>, and <code>find_path()</code> commands. Each command will add appropriate subdirectories (like <code>bin</code>, <code>lib</code>, or <code>include</code>) as specified in its own documentation. </p>
<p> This variable may hold a single prefix or a list of prefixes separated by <code>:</code> on UNIX or <code>;</code> on Windows (the same as the <code>PATH</code> environment variable convention on those platforms). </p>
<p> See also the <code>CMAKE_PREFIX_PATH</code> CMake variable.</p>
<h2>Environment Variables That Control The Build</h2>
<h3>Cmake_Apple_Silicon_Processor</h3>
<p>New in version 3.19.2. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> On Apple Silicon hosts running macOS, set this environment variable to tell CMake what architecture to use for <code>CMAKE_HOST_SYSTEM_PROCESSOR</code>. The value must be either <code>arm64</code> or <code>x86_64</code>. </p>
<p> The <code>CMAKE_APPLE_SILICON_PROCESSOR</code> normal variable, if set, overrides this environment variable.</p>
<h3>Cmake_Build_Parallel_Level</h3>
<p>New in version 3.12. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Specifies the maximum number of concurrent processes to use when building using the <code>cmake &#8211;build</code> command line Build Tool Mode. </p>
<p> If this variable is defined empty the native build tool&#8217;s default number is used.</p>
<h3>Cmake_Build_Type</h3>
<p>New in version 3.22. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The <code>CMAKE_BUILD_TYPE</code> environment variable specifies a default value for the <code>CMAKE_BUILD_TYPE</code> variable when there is no explicit configuration given on the first run while creating a new build tree.</p>
<h3>Cmake_Configuration_Types</h3>
<p>New in version 3.22. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The <code>CMAKE_CONFIGURATION_TYPES</code> environment variable specifies a default value for the <code>CMAKE_CONFIGURATION_TYPES</code> variable when there is no explicit configuration given on the first run while creating a new build tree.</p>
<h3>Cmake_Config_Type</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The default build configuration for Build Tool Mode and <code>ctest</code> build handler when there is no explicit configuration given.</p>
<h3>Cmake_Export_Compile_Commands</h3>
<p>New in version 3.17. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The default value for <code>CMAKE_EXPORT_COMPILE_COMMANDS</code> when there is no explicit configuration given on the first run while creating a new build tree. On later runs in an existing build tree the value persists in the cache as <code>CMAKE_EXPORT_COMPILE_COMMANDS</code>.</p>
<h3>Cmake_Generator</h3>
<p>New in version 3.15. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Specifies the CMake default generator to use when no generator is supplied with <code>-G</code>. If the provided value doesn&#8217;t name a generator known by CMake, the internal default is used. Either way the resulting generator selection is stored in the <code>CMAKE_GENERATOR</code> variable. </p>
<p> Some generators may be additionally configured using the environment variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_GENERATOR_PLATFORM</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_GENERATOR_TOOLSET</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_GENERATOR_INSTANCE</code></dl>
<h3>Cmake_Generator_Instance</h3>
<p>New in version 3.15. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default value for <code>CMAKE_GENERATOR_INSTANCE</code> if no Cache entry is present. This value is only applied if <code>CMAKE_GENERATOR</code> is set.</p>
<h3>Cmake_Generator_Platform</h3>
<p>New in version 3.15. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default value for <code>CMAKE_GENERATOR_PLATFORM</code> if no Cache entry is present and no value is specified by <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option. This value is only applied if <code>CMAKE_GENERATOR</code> is set.</p>
<h3>Cmake_Generator_Toolset</h3>
<p>New in version 3.15. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default value for <code>CMAKE_GENERATOR_TOOLSET</code> if no Cache entry is present and no value is specified by <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option. This value is only applied if <code>CMAKE_GENERATOR</code> is set.</p>
<h3>Cmake_Install_Mode</h3>
<p>New in version 3.22. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The <code>CMAKE_INSTALL_MODE</code> environment variable allows users to operate CMake in an alternate mode of <code>file(INSTALL)</code> and <code>install()</code>. </p>
<p> The default behavior for an installation is to copy a source file from a source directory into a destination directory. This environment variable however allows the user to override this behavior, causing CMake to create symbolic links instead.</p>
<h3>Usage Scenarios</h3>
<p>Installing symbolic links rather than copying files can help in the following ways:</p>
<dl>
<dt>&bull;</p>
<dd>Conserving storage space because files do not have to be duplicated on disk.</p>
<dt>&bull;</p>
<dd>Changes to the source of the symbolic link are seen at the install destination without having to re-run the install step.</p>
<dt>&bull;</p>
<dd>Editing through the link at the install destination will modify the source of the link. This may be useful when dealing with CMake project hierarchies, i.e. using <code>ExternalProject</code> and consistent source navigation and refactoring is desired across projects.</dl>
<h3>Allowed Values</h3>
<p>The following values are allowed for <code>CMAKE_INSTALL_MODE</code>:</p>
<dl>
<dt><code>COPY</code>, empty or unset</p>
<dd>Duplicate the file at its destination. This is the default behavior.</p>
<dt><code>ABS_SYMLINK</code></p>
<dd>Create an <i>absolute</i> symbolic link to the source file at the destination. Halt with an error if the link cannot be created.</p>
<dt><code>ABS_SYMLINK_OR_COPY</code></p>
<dd>Like <code>ABS_SYMLINK</code> but fall back to silently copying if the symlink couldn&#8217;t be created.</p>
<dt><code>REL_SYMLINK</code></p>
<dd>Create a <i>relative</i> symbolic link to the source file at the destination. Halt with an error if the link cannot be created.</p>
<dt><code>REL_SYMLINK_OR_COPY</code></p>
<dd>Like <code>REL_SYMLINK</code> but fall back to silently copying if the symlink couldn&#8217;t be created.</p>
<dt><code>SYMLINK</code></p>
<dd>Try as if through <code>REL_SYMLINK</code> and fall back to <code>ABS_SYMLINK</code> if the referenced file cannot be expressed using a relative path. Halt with an error if the link cannot be created.</p>
<dt><code>SYMLINK_OR_COPY</code></p>
<dd>Like <code>SYMLINK</code> but fall back to silently copying if the symlink couldn&#8217;t be created. </p>
<p> <code>NOTE:</code> A symbolic link consists of a reference file path rather than contents of its own, hence there are two ways to express the relation, either by a <i>relative</i> or an <i>absolute</i> path.</dl>
<h3>When To Set The Environment Variable</h3>
<p>For the environment variable to take effect, it must be set during the correct build phase(s).</p>
<dl>
<dt>&bull;</p>
<dd>If the project calls <code>file(INSTALL)</code> directly, the environment variable must be set during the configuration phase.</p>
<dt>&bull;</p>
<dd>In order to apply to <code>install()</code>, the environment variable must be set during installation. This could be during a build if using the <code>install</code> or <code>package</code> build targets, or separate from the build when invoking an install or running <code>cpack</code> from the command line.</p>
<dt>&bull;</p>
<dd>When using <code>ExternalProject</code>, it might be required during the build phase, since the external project&#8217;s own configure, build and install steps will execute during the main project&#8217;s build phase. </p>
<p> Given the above, it is recommended to set the environment variable consistently across all phases (configure, build and install).</dl>
<h3>Caveats</h3>
<p>Use this environment variable with caution. The following highlights some points to be considered:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_INSTALL_MODE</code> only affects files, not directories.</p>
<dt>&bull;</p>
<dd>Symbolic links are not available on all platforms.</p>
<dt>&bull;</p>
<dd>The way this environment variable interacts with the install step of <code>ExternalProject</code> is more complex. For further details, see that module&#8217;s documentation.</p>
<dt>&bull;</p>
<dd>A symbolic link ties the destination to the source in a persistent way. Writing to either of the two affects both file system objects. This is in contrast to normal install behavior which only copies files as they were at the time the install was performed, with no enduring relationship between the source and destination of the install.</p>
<dt>&bull;</p>
<dd>Combining <code>CMAKE_INSTALL_MODE</code> with <code>IOS_INSTALL_COMBINED</code> is not supported.</p>
<dt>&bull;</p>
<dd>Changing <code>CMAKE_INSTALL_MODE</code> from what it was on a previous run can lead to unexpected results. Moving from a non-symlinking mode to a symlinking mode will discard any previous file at the destination, but the reverse is not true. Once a symlink exists at the destination, even if you switch to a non-symlink mode, the symlink will continue to exist at the destination and will not be replaced by an actual file.</dl>
<h3>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</h3>
<p>New in version 3.17. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compiler launcher to use for the specified language. Will only be used by CMake to initialize the variable on the first configuration. Afterwards, it is available through the cache setting of the variable of the same name. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_&lt;LANG&gt;_COMPILER_LAUNCHER</code> variable is defined.</p>
<h3>CMAKE_&lt;LANG&gt;_LINKER_LAUNCHER</h3>
<p>New in version 3.21. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default launcher to use when linking a target of the specified language. Will only be used by CMake to initialize the variable on the first configuration. Afterwards, it is available through the cache setting of the variable of the same name. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_&lt;LANG&gt;_LINKER_LAUNCHER</code> variable is defined.</p>
<h3>Cmake_Msvcide_Run_Path</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Extra PATH locations for custom commands when using <code>Visual Studio 9 2008</code> (or above) generators. </p>
<p> The <code>CMAKE_MSVCIDE_RUN_PATH</code> environment variable sets the default value for the <code>CMAKE_MSVCIDE_RUN_PATH</code> variable if not already explicitly set.</p>
<h3>Cmake_No_Verbose</h3>
<p>New in version 3.14. </p>
<p> Disables verbose output from CMake when <code>VERBOSE</code> environment variable is set. </p>
<p> Only your build tool of choice will still print verbose output when you start to actually build your project.</p>
<h3>Cmake_Osx_Architectures</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Target specific architectures for macOS. </p>
<p> The <code>CMAKE_OSX_ARCHITECTURES</code> environment variable sets the default value for the <code>CMAKE_OSX_ARCHITECTURES</code> variable. See <code>OSX_ARCHITECTURES</code> for more information.</p>
<h3>Cmake_Toolchain_File</h3>
<p>New in version 3.21. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> The <code>CMAKE_TOOLCHAIN_FILE</code> environment variable specifies a default value for the <code>CMAKE_TOOLCHAIN_FILE</code> variable when there is no explicit configuration given on the first run while creating a new build tree. On later runs in an existing build tree the value persists in the cache as <code>CMAKE_TOOLCHAIN_FILE</code>.</p>
<h3>Destdir</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> On UNIX one can use the <code>DESTDIR</code> mechanism in order to relocate the whole installation. <code>DESTDIR</code> means DESTination DIRectory. It is commonly used by makefile users in order to install software at non-default location. It is usually invoked like this: </p>
<pre>make DESTDIR=/home/john install</pre>
<p>which will install the concerned software using the installation prefix, e.g. <code>/usr/local</code> prepended with the <code>DESTDIR</code> value which finally gives <code>/home/john/usr/local</code>. </p>
<p> WARNING: <code>DESTDIR</code> may not be used on Windows because installation prefix usually contains a drive letter like in <code>C:/Program Files</code> which cannot be prepended with some other prefix.</p>
<h3>Ldflags</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Will only be used by CMake on the first configuration to determine the default linker flags, after which the value for <code>LDFLAGS</code> is stored in the cache as <code>CMAKE_EXE_LINKER_FLAGS_INIT</code>, <code>CMAKE_SHARED_LINKER_FLAGS_INIT</code>, and <code>CMAKE_MODULE_LINKER_FLAGS_INIT</code>. For any configuration run (including the first), the environment variable will be ignored if the equivalent <code>CMAKE_&lt;TYPE&gt;_LINKER_FLAGS_INIT</code> variable is defined.</p>
<h3>Macosx_Deployment_Target</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Specify the minimum version of macOS on which the target binaries are to be deployed. </p>
<p> The <code>MACOSX_DEPLOYMENT_TARGET</code> environment variable sets the default value for the <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> variable.</p>
<h3>&lt;PackageName&gt;_ROOT</h3>
<p>New in version 3.12. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Calls to <code>find_package(&lt;PackageName&gt;)</code> will search in prefixes specified by the <code>&lt;PackageName&gt;_ROOT</code> environment variable, where <code>&lt;PackageName&gt;</code> is the name given to the <code>find_package()</code> call and <code>_ROOT</code> is literal. For example, <code>find_package(Foo)</code> will search prefixes specified in the <code>Foo_ROOT</code> environment variable (if set). See policy <code>CMP0074</code>. </p>
<p> This variable may hold a single prefix or a list of prefixes separated by <code>:</code> on UNIX or <code>;</code> on Windows (the same as the <code>PATH</code> environment variable convention on those platforms). </p>
<p> See also the <code>&lt;PackageName&gt;_ROOT</code> CMake variable.</p>
<h3>Verbose</h3>
<p>New in version 3.14. </p>
<p> Activates verbose output from CMake and your build tools of choice when you start to actually build your project. </p>
<p> Note that any given value is ignored. It&#8217;s just checked for existence. </p>
<p> See also Build Tool Mode and <code>CMAKE_NO_VERBOSE</code> environment variable</p>
<h2>Environment Variables For Languages</h2>
<h3>ASM&lt;DIALECT&gt;</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling a specific dialect of assembly language files. <code>ASM&lt;DIALECT&gt;</code> can be <code>ASM</code>, <code>ASM_NASM</code> (Netwide Assembler), <code>ASM_MASM</code> (Microsoft Assembler) or <code>ASM-ATT</code> (Assembler AT&amp;T). Will only be used by CMake on the first configuration to determine <code>ASM&lt;DIALECT&gt;</code> compiler, after which the value for <code>ASM&lt;DIALECT&gt;</code> is stored in the cache as <code>CMAKE_ASM&lt;DIALECT&gt;_COMPILER</code>. For subsequent configuration runs, the environment variable will be ignored in favor of <code>CMAKE_ASM&lt;DIALECT&gt;_COMPILER</code>. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export ASM=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>ASM&lt;DIALECT&gt;FLAGS</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling a specific dialect of an assembly language. <code>ASM&lt;DIALECT&gt;FLAGS</code> can be <code>ASMFLAGS</code>, <code>ASM_NASMFLAGS</code>, <code>ASM_MASMFLAGS</code> or <code>ASM-ATTFLAGS</code>. Will only be used by CMake on the first configuration to determine <code>ASM_&lt;DIALECT&gt;</code> default compilation flags, after which the value for <code>ASM&lt;DIALECT&gt;FLAGS</code> is stored in the cache as <code>CMAKE_ASM&lt;DIALECT&gt;_FLAGS &lt;CMAKE_&lt;LANG&gt;_FLAGS&gt;</code>. For any configuration run (including the first), the environment variable will be ignored, if the <code>CMAKE_ASM&lt;DIALECT&gt;_FLAGS &lt;CMAKE_&lt;LANG&gt;_FLAGS&gt;</code> variable is defined. </p>
<p> See also <code>CMAKE_ASM&lt;DIALECT&gt;_FLAGS_INIT</code>.</p>
<h3>Cc</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>C</code> language files. Will only be used by CMake on the first configuration to determine <code>C</code> compiler, after which the value for <code>CC</code> is stored in the cache as <code>CMAKE_C_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_C_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export CC=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>Cflags</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>C</code> files. Will only be used by CMake on the first configuration to determine <code>CC</code> default compilation flags, after which the value for <code>CFLAGS</code> is stored in the cache as <code>CMAKE_C_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_C_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_C_FLAGS_INIT</code>.</p>
<h3>Csflags</h3>
<p>New in version 3.9.2. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>CSharp</code> files. Will only be used by CMake on the first configuration to determine <code>CSharp</code> default compilation flags, after which the value for <code>CSFLAGS</code> is stored in the cache as <code>CMAKE_CSharp_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_CSharp_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_CSharp_FLAGS_INIT</code>.</p>
<h3>Cudaarchs</h3>
<p>New in version 3.20. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Value used to initialize <code>CMAKE_CUDA_ARCHITECTURES</code> on the first configuration if it&#8217;s not already defined. Subsequent runs will use the value stored in the cache. </p>
<p> This is a semicolon-separated list of architectures as described in <code>CUDA_ARCHITECTURES</code>.</p>
<h3>Cudacxx</h3>
<p>New in version 3.8. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>CUDA</code> language files. Will only be used by CMake on the first configuration to determine <code>CUDA</code> compiler, after which the value for <code>CUDA</code> is stored in the cache as <code>CMAKE_CUDA_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_CUDA_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export CUDACXX=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>Cudaflags</h3>
<p>New in version 3.8. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>CUDA</code> files. Will only be used by CMake on the first configuration to determine <code>CUDA</code> default compilation flags, after which the value for <code>CUDAFLAGS</code> is stored in the cache as <code>CMAKE_CUDA_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_CUDA_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_CUDA_FLAGS_INIT</code>.</p>
<h3>Cudahostcxx</h3>
<p>New in version 3.8. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling host code when compiling <code>CUDA</code> language files. Will only be used by CMake on the first configuration to determine <code>CUDA</code> host compiler, after which the value for <code>CUDAHOSTCXX</code> is stored in the cache as <code>CMAKE_CUDA_HOST_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_CUDA_HOST_COMPILER</code> variable is defined. </p>
<p> This environment variable is primarily meant for use with projects that enable <code>CUDA</code> as a first-class language. </p>
<p> <code>NOTE:</code> Ignored when using Visual Studio Generators. </p>
<p> New in version 3.13: The <code>FindCUDA</code> module will use this variable to initialize its <code>CUDA_HOST_COMPILER</code> setting.</p>
<h3>Cxx</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>CXX</code> language files. Will only be used by CMake on the first configuration to determine <code>CXX</code> compiler, after which the value for <code>CXX</code> is stored in the cache as <code>CMAKE_CXX_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_CXX_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export CXX=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>Cxxflags</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>CXX</code> (C++) files. Will only be used by CMake on the first configuration to determine <code>CXX</code> default compilation flags, after which the value for <code>CXXFLAGS</code> is stored in the cache as <code>CMAKE_CXX_FLAGS</code>. For any configuration run ( including the first), the environment variable will be ignored if the <code>CMAKE_CXX_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_CXX_FLAGS_INIT</code>.</p>
<h3>Fc</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>Fortran</code> language files. Will only be used by CMake on the first configuration to determine <code>Fortran</code> compiler, after which the value for <code>Fortran</code> is stored in the cache as <code>CMAKE_Fortran_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_Fortran_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export FC=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>Fflags</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>Fortran</code> files. Will only be used by CMake on the first configuration to determine <code>Fortran</code> default compilation flags, after which the value for <code>FFLAGS</code> is stored in the cache as <code>CMAKE_Fortran_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_Fortran_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_Fortran_FLAGS_INIT</code>.</p>
<h3>Hipcxx</h3>
<p>New in version 3.21. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>HIP</code> language files. Will only be used by CMake on the first configuration to determine <code>HIP</code> compiler, after which the value for <code>HIP</code> is stored in the cache as <code>CMAKE_HIP_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_HIP_COMPILER</code> variable is defined.</p>
<h3>Hipflags</h3>
<p>New in version 3.21. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>HIP</code> files. Will only be used by CMake on the first configuration to determine <code>HIP</code> default compilation flags, after which the value for <code>HIPFLAGS</code> is stored in the cache as <code>CMAKE_HIP_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_HIP_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_HIP_FLAGS_INIT</code>.</p>
<h3>Ispc</h3>
<p>New in version 3.19. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>ISPC</code> language files. Will only be used by CMake on the first configuration to determine <code>ISPC</code> compiler, after which the value for <code>ISPC</code> is stored in the cache as <code>CMAKE_ISPC_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_ISPC_COMPILER</code> variable is defined.</p>
<h3>Ispcflags</h3>
<p>New in version 3.19. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>ISPC</code> files. Will only be used by CMake on the first configuration to determine <code>ISPC</code> default compilation flags, after which the value for <code>ISPCFLAGS</code> is stored in the cache as <code>CMAKE_ISPC_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_ISPC_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_ISPC_FLAGS_INIT</code>.</p>
<h3>Objc</h3>
<p>New in version 3.16.7. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>OBJC</code> language files. Will only be used by CMake on the first configuration to determine <code>OBJC</code> compiler, after which the value for <code>OBJC</code> is stored in the cache as <code>CMAKE_OBJC_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_OBJC_COMPILER</code> variable is defined. </p>
<p> If <code>OBJC</code> is not defined, the <code>CC</code> environment variable will be checked instead.</p>
<h3>Objcxx</h3>
<p>New in version 3.16.7. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>OBJCXX</code> language files. Will only be used by CMake on the first configuration to determine <code>OBJCXX</code> compiler, after which the value for <code>OBJCXX</code> is stored in the cache as <code>CMAKE_OBJCXX_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_OBJCXX_COMPILER</code> variable is defined. </p>
<p> If <code>OBJCXX</code> is not defined, the <code>CXX</code> environment variable will be checked instead.</p>
<h3>Rc</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>resource</code> files. Will only be used by CMake on the first configuration to determine <code>resource</code> compiler, after which the value for <code>RC</code> is stored in the cache as <code>CMAKE_RC_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_RC_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export RC=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h3>Rcflags</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Default compilation flags to be used when compiling <code>resource</code> files. Will only be used by CMake on the first configuration to determine <code>resource</code> default compilation flags, after which the value for <code>RCFLAGS</code> is stored in the cache as <code>CMAKE_RC_FLAGS</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_RC_FLAGS</code> variable is defined. </p>
<p> See also <code>CMAKE_RC_FLAGS_INIT</code>.</p>
<h3>Swiftc</h3>
<p>New in version 3.15. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Preferred executable for compiling <code>Swift</code> language files. Will only be used by CMake on the first configuration to determine <code>Swift</code> compiler, after which the value for <code>SWIFTC</code> is stored in the cache as <code>CMAKE_Swift_COMPILER</code>. For any configuration run (including the first), the environment variable will be ignored if the <code>CMAKE_Swift_COMPILER</code> variable is defined. </p>
<p> <code>NOTE:</code> Options that are required to make the compiler work correctly can be included; they can not be changed. </p>
<pre>$ export SWIFTC=&quot;custom-compiler --arg1 --arg2&quot;</pre>
<h2>Environment Variables For Ctest</h2>
<h3>Ctest_Interactive_Debug_Mode</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Environment variable that will exist and be set to <code>1</code> when a test executed by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> is run in interactive mode.</p>
<h3>Ctest_Output_On_Failure</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Boolean environment variable that controls if the output should be logged for failed tests. Set the value to <code>1</code>, <code>True</code>, or <code>ON</code> to enable output on failure. See <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> for more information on controlling output of failed tests.</p>
<h3>Ctest_Parallel_Level</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Specify the number of tests for CTest to run in parallel. See <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> for more information on parallel test execution.</p>
<h3>Ctest_Progress_Output</h3>
<p>New in version 3.13. </p>
<p> This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Boolean environment variable that affects how <code>ctest</code> command output reports overall progress. When set to <code>1</code>, <code>TRUE</code>, <code>ON</code> or anything else that evaluates to boolean true, progress is reported by repeatedly updating the same line. This greatly reduces the overall verbosity, but is only supported when output is sent directly to a terminal. If the environment variable is not set or has a value that evaluates to false, output is reported normally with each test having its own start and end lines logged to the output. </p>
<p> The <code>&#8211;progress</code> option to <code>ctest</code> overrides this environment variable if both are given.</p>
<h3>Ctest_Use_Launchers_Default</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Initializes the <code>CTEST_USE_LAUNCHERS</code> variable if not already defined.</p>
<h3>Dashboard_Test_From_Ctest</h3>
<p>This is a CMake Environment Variable. Its initial value is taken from the calling process environment. </p>
<p> Environment variable that will exist when a test executed by <code><a href="/docs/linux/man/1-ctest/">ctest</a>(1)</code> is run in non-interactive mode. The value will be equal to <code>CMAKE_VERSION</code>.</p>
<h2>Environment Variables For The Cmake Curses Interface</h2>
<h3>Ccmake_Colors</h3>
<p>New in version 3.18. </p>
<p> Determines what colors are used by the CMake curses interface, when run on a terminal that supports colors. The syntax follows the same conventions as <code>LS_COLORS</code>; that is, a list of key/value pairs separated by <code>:</code>. </p>
<p> Keys are a single letter corresponding to a CMake cache variable type:</p>
<dl>
<dt>&bull;</p>
<dd><code>s</code>: A <code>STRING</code>.</p>
<dt>&bull;</p>
<dd><code>p</code>: A <code>FILEPATH</code>.</p>
<dt>&bull;</p>
<dd><code>c</code>: A value which has an associated list of choices.</p>
<dt>&bull;</p>
<dd><code>y</code>: A <code>BOOL</code> which has a true-like value (e.g. <code>ON</code>, <code>YES</code>).</p>
<dt>&bull;</p>
<dd><code>n</code>: A <code>BOOL</code> which has a false-like value (e.g. <code>OFF</code>, <code>NO</code>). </p>
<p> Values are an integer number that specifies what color to use. <code>0</code> is black (you probably don&#8217;t want to use that). Others are determined by your terminal&#8217;s color support. Most (color) terminals will support at least 8 or 16 colors. Some will support up to 256 colors. The colors will likely match <i>this chart</i>, although the first 16 colors may match the original <i>CGA color palette</i>. (Many modern terminal emulators also allow their color palette, at least for the first 16 colors, to be configured by the user.) </p>
<p> Note that fairly minimal checking is done for bad colors (although a value higher than what curses believes your terminal supports will be silently ignored) or bad syntax. </p>
<p> For example: </p>
<pre>CCMAKE_COLORS='s=39:p=220:c=207:n=196:y=46'</pre>
</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
