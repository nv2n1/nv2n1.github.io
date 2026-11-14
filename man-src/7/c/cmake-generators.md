---
title: "cmake-generators(7)"
name: "cmake-generators"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-generators/"
description: "cmake-generators – CMake Generators Reference"
---

<p>cmake-generators &#8211; CMake Generators Reference</p>
<h2>Introduction</h2>
<p>A <i>CMake Generator</i> is responsible for writing the input files for a native build system. Exactly one of the <i>CMake Generators</i> must be selected for a build tree to determine what native build system is to be used. Optionally one of the <i>Extra Generators</i> may be selected as a variant of some of the <i>Command-Line Build Tool Generators</i> to produce project files for an auxiliary IDE. </p>
<p> CMake Generators are platform-specific so each may be available only on certain platforms. The <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command-line tool <code>&#8211;help</code> output lists available generators on the current platform. Use its <code>-G</code> option to specify the generator for a new build tree. The <code><a href="/docs/linux/man/1-cmake-gui/">cmake-gui</a>(1)</code> offers interactive selection of a generator when creating a new build tree.</p>
<h2>Cmake Generators</h2>
<h3>Command-Line Build Tool Generators</h3>
<p>These generators support command-line build tools. In order to use them, one must launch CMake from a command-line prompt whose environment is already configured for the chosen compiler and build tool.</p>
<h3>Makefile Generators</h3>
<h3>Borland Makefiles</h3>
<p>Generates Borland makefiles.</p>
<h3>MSYS Makefiles</h3>
<p>Generates makefiles for use with MSYS (Minimal SYStem) <code>make</code> under the MSYS shell. </p>
<p> Use this generator in a MSYS shell prompt and using <code>make</code> as the build tool. The generated makefiles use <code>/bin/sh</code> as the shell to launch build rules. They are not compatible with a Windows command prompt. </p>
<p> To build under a Windows command prompt, use the <code>MinGW Makefiles</code> generator.</p>
<h3>MinGW Makefiles</h3>
<p>Generates makefiles for use with <code>mingw32-make</code> under a Windows command prompt. </p>
<p> Use this generator under a Windows command prompt with MinGW (Minimalist GNU for Windows) in the <code>PATH</code> and using <code>mingw32-make</code> as the build tool. The generated makefiles use <code>cmd.exe</code> as the shell to launch build rules. They are not compatible with MSYS or a unix shell. </p>
<p> To build under the MSYS shell, use the <code>MSYS Makefiles</code> generator.</p>
<h3>NMake Makefiles</h3>
<p>Generates NMake makefiles.</p>
<h3>NMake Makefiles JOM</h3>
<p>Generates JOM makefiles. </p>
<p> New in version 3.8: <code>CodeBlocks</code> generator can be used as an extra generator.</p>
<h3>Unix Makefiles</h3>
<p>Generates standard UNIX makefiles. </p>
<p> A hierarchy of UNIX makefiles is generated into the build tree. Use any standard UNIX-style make program to build the project through the <code>all</code> target and install the project through the <code>install</code> (or <code>install/strip</code>) target. </p>
<p> For each subdirectory <code>sub/dir</code> of the project a UNIX makefile will be created, containing the following targets:</p>
<dl>
<dt><code>all</code></p>
<dd>Depends on all targets required by the subdirectory.</p>
<dt><code>install</code></p>
<dd>Runs the install step in the subdirectory, if any.</p>
<dt><code>install/strip</code></p>
<dd>Runs the install step in the subdirectory followed by a <code>CMAKE_STRIP</code> command, if any. </p>
<p> The <code>CMAKE_STRIP</code> variable will contain the platform&#8217;s <code>strip</code> utility, which removes symbols information from generated binaries.</p>
<dt><code>test</code></p>
<dd>Runs the test step in the subdirectory, if any.</p>
<dt><code>package</code></p>
<dd>Runs the package step in the subdirectory, if any.</dl>
<h3>Watcom WMake</h3>
<p>Generates Watcom WMake makefiles.</p>
<h3>Ninja Generators</h3>
<h3>Ninja</h3>
<p>Generates <code>build.ninja</code> files. </p>
<p> A <code>build.ninja</code> file is generated into the build tree. Use the ninja program to build the project through the <code>all</code> target and install the project through the <code>install</code> (or <code>install/strip</code>) target. </p>
<p> For each subdirectory <code>sub/dir</code> of the project, additional targets are generated: </p>
<p> <code>sub/dir/all</code> New in version 3.6: Depends on all targets required by the subdirectory. </p>
<p> <code>sub/dir/install</code> New in version 3.7: Runs the install step in the subdirectory, if any. </p>
<p> <code>sub/dir/install/strip</code> New in version 3.7: Runs the install step in the subdirectory followed by a <code>CMAKE_STRIP</code> command, if any. </p>
<p> The <code>CMAKE_STRIP</code> variable will contain the platform&#8217;s <code>strip</code> utility, which removes symbols information from generated binaries. </p>
<p> <code>sub/dir/test</code> New in version 3.7: Runs the test step in the subdirectory, if any. </p>
<p> <code>sub/dir/package</code> New in version 3.7: Runs the package step in the subdirectory, if any.</p>
<h3>Fortran Support</h3>
<p>New in version 3.7. </p>
<p> The <code>Ninja</code> generator conditionally supports Fortran when the <code>ninja</code> tool is at least version 1.10 (which has the required features).</p>
<h3>Swift Support</h3>
<p>New in version 3.15. </p>
<p> The Swift support is experimental, not considered stable, and may change in future releases of CMake.</p>
<h3>See Also</h3>
<p>New in version 3.17: The <code>Ninja Multi-Config</code> generator is similar to the <code>Ninja</code> generator, but generates multiple configurations at once.</p>
<h3>Ninja Multi-Config</h3>
<p>New in version 3.17. </p>
<p> Generates multiple <code>build-&lt;Config&gt;.ninja</code> files. </p>
<p> This generator is very much like the <code>Ninja</code> generator, but with some key differences. Only these differences will be discussed in this document. </p>
<p> Unlike the <code>Ninja</code> generator, <code>Ninja Multi-Config</code> generates multiple configurations at once with <code>CMAKE_CONFIGURATION_TYPES</code> instead of only one configuration with <code>CMAKE_BUILD_TYPE</code>. One <code>build-&lt;Config&gt;.ninja</code> file will be generated for each of these configurations (with <code>&lt;Config&gt;</code> being the configuration name.) These files are intended to be run with <code>ninja -f build-&lt;Config&gt;.ninja</code>. A <code>build.ninja</code> file is also generated, using the configuration from either <code>CMAKE_DEFAULT_BUILD_TYPE</code> or the first item from <code>CMAKE_CONFIGURATION_TYPES</code>. </p>
<p> <code>cmake &#8211;build . &#8211;config &lt;Config&gt;</code> will always use <code>build-&lt;Config&gt;.ninja</code> to build. If no <code>&#8211;config</code> argument is specified, <code>cmake &#8211;build .</code> will use <code>build.ninja</code>. </p>
<p> Each <code>build-&lt;Config&gt;.ninja</code> file contains <code>&lt;target&gt;</code> targets as well as <code>&lt;target&gt;:&lt;Config&gt;</code> targets, where <code>&lt;Config&gt;</code> is the same as the configuration specified in <code>build-&lt;Config&gt;.ninja</code> Additionally, if cross-config mode is enabled, <code>build-&lt;Config&gt;.ninja</code> may contain <code>&lt;target&gt;:&lt;OtherConfig&gt;</code> targets, where <code>&lt;OtherConfig&gt;</code> is a cross-config, as well as <code>&lt;target&gt;:all</code>, which builds the target in all cross-configs. See below for how to enable cross-config mode. </p>
<p> The <code>Ninja Multi-Config</code> generator recognizes the following variables:</p>
<dl>
<dt><code>CMAKE_CONFIGURATION_TYPES</code></p>
<dd>Specifies the total set of configurations to build. Unlike with other multi-config generators, this variable has a value of <code>Debug;Release;RelWithDebInfo</code> by default.</p>
<dt><code>CMAKE_CROSS_CONFIGS</code></p>
<dd>Specifies a semicolon-separated list of configurations available from all <code>build-&lt;Config&gt;.ninja</code> files.</p>
<dt><code>CMAKE_DEFAULT_BUILD_TYPE</code></p>
<dd>Specifies the configuration to use by default in a <code>build.ninja</code> file.</p>
<dt><code>CMAKE_DEFAULT_CONFIGS</code></p>
<dd>Specifies a semicolon-separated list of configurations to build for a target in <code>build.ninja</code> if no <code>:&lt;Config&gt;</code> suffix is specified. </p>
<p> Consider the following example: </p>
<pre>cmake_minimum_required(VERSION 3.16)
project(MultiConfigNinja C)
add_executable(generator generator.c)
add_custom_command(OUTPUT generated.c COMMAND generator generated.c)
add_library(generated ${CMAKE_BINARY_DIR}/generated.c)</pre>
<p>Now assume you configure the project with <code>Ninja Multi-Config</code> and run one of the following commands: </p>
<pre>ninja -f build-Debug.ninja generated
# OR
cmake --build . --config Debug --target generated</pre>
<p>This would build the <code>Debug</code> configuration of <code>generator</code>, which would be used to generate <code>generated.c</code>, which would be used to build the <code>Debug</code> configuration of <code>generated</code>. </p>
<p> But if <code>CMAKE_CROSS_CONFIGS</code> is set to <code>all</code>, and you run the following instead: </p>
<pre>ninja -f build-Release.ninja generated:Debug
# OR
cmake --build . --config Release --target generated:Debug</pre>
<p>This would build the <code>Release</code> configuration of <code>generator</code>, which would be used to generate <code>generated.c</code>, which would be used to build the <code>Debug</code> configuration of <code>generated</code>. This is useful for running a release-optimized version of a generator utility while still building the debug version of the targets built with the generated code.</dl>
<h3>Custom Commands</h3>
<p>New in version 3.20. </p>
<p> The <code>Ninja Multi-Config</code> generator adds extra capabilities to <code>add_custom_command()</code> and <code>add_custom_target()</code> through its cross-config mode. The <code>COMMAND</code>, <code>DEPENDS</code>, and <code>WORKING_DIRECTORY</code> arguments can be evaluated in the context of either the &quot;command config&quot; (the &quot;native&quot; configuration of the <code>build-&lt;Config&gt;.ninja</code> file in use) or the &quot;output config&quot; (the configuration used to evaluate the <code>OUTPUT</code> and <code>BYPRODUCTS</code>). </p>
<p> If either <code>OUTPUT</code> or <code>BYPRODUCTS</code> names a path that is common to more than one configuration (e.g. it does not use any generator expressions), all arguments are evaluated in the command config by default. If all <code>OUTPUT</code> and <code>BYPRODUCTS</code> paths are unique to each configuration (e.g. by using the <code>$&lt;CONFIG&gt;</code> generator expression), the first argument of <code>COMMAND</code> is still evaluated in the command config by default, while all subsequent arguments, as well as the arguments to <code>DEPENDS</code> and <code>WORKING_DIRECTORY</code>, are evaluated in the output config. These defaults can be overridden with the <code>$&lt;OUTPUT_CONFIG:&#8230;&gt;</code> and <code>$&lt;COMMAND_CONFIG:&#8230;&gt;</code> generator-expressions. Note that if a target is specified by its name in <code>DEPENDS</code>, or as the first argument of <code>COMMAND</code>, it is always evaluated in the command config, even if it is wrapped in <code>$&lt;OUTPUT_CONFIG:&#8230;&gt;</code> (because its plain name is not a generator expression). </p>
<p> As an example, consider the following: </p>
<pre>add_custom_command(
 OUTPUT &quot;$&lt;CONFIG&gt;.txt&quot;
 COMMAND generator &quot;$&lt;CONFIG&gt;.txt&quot; &quot;$&lt;OUTPUT_CONFIG:$&lt;CONFIG&gt;&gt;&quot; &quot;$&lt;COMMAND_CONFIG:$&lt;CONFIG&gt;&gt;&quot;
 DEPENDS tgt1 &quot;$&lt;TARGET_FILE:tgt2&gt;&quot; &quot;$&lt;OUTPUT_CONFIG:$&lt;TARGET_FILE:tgt3&gt;&gt;&quot; &quot;$&lt;COMMAND_CONFIG:$&lt;TARGET_FILE:tgt4&gt;&gt;&quot;
 )</pre>
<p>Assume that <code>generator</code>, <code>tgt1</code>, <code>tgt2</code>, <code>tgt3</code>, and <code>tgt4</code> are all executable targets, and assume that <code>$&lt;CONFIG&gt;.txt</code> is built in the <code>Debug</code> output config using the <code>Release</code> command config. The <code>Release</code> build of the <code>generator</code> target is called with <code>Debug.txt Debug Release</code> as arguments. The command depends on the <code>Release</code> builds of <code>tgt1</code> and <code>tgt4</code>, and the <code>Debug</code> builds of <code>tgt2</code> and <code>tgt3</code>. </p>
<p> <code>PRE_BUILD</code>, <code>PRE_LINK</code>, and <code>POST_BUILD</code> custom commands for targets only get run in their &quot;native&quot; configuration (the <code>Release</code> configuration in the <code>build-Release.ninja</code> file) unless they have no <code>BYPRODUCTS</code> or their <code>BYPRODUCTS</code> are unique per config. Consider the following example: </p>
<pre>add_executable(exe main.c)
add_custom_command(
 TARGET exe
 POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E echo &quot;Running no-byproduct command&quot;
 )
add_custom_command(
 TARGET exe
 POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E echo &quot;Running separate-byproduct command for $&lt;CONFIG&gt;&quot;
 BYPRODUCTS $&lt;CONFIG&gt;.txt
 )
add_custom_command(
 TARGET exe
 POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E echo &quot;Running common-byproduct command for $&lt;CONFIG&gt;&quot;
 BYPRODUCTS exe.txt
 )</pre>
<p>In this example, if you build <code>exe:Debug</code> in <code>build-Release.ninja</code>, the first and second custom commands get run, since their byproducts are unique per-config, but the last custom command does not. However, if you build <code>exe:Release</code> in <code>build-Release.ninja</code>, all three custom commands get run.</p>
<h3>IDE Build Tool Generators</h3>
<p>These generators support Integrated Development Environment (IDE) project files. Since the IDEs configure their own environment one may launch CMake from any environment.</p>
<h3>Visual Studio Generators</h3>
<h3>Visual Studio 6</h3>
<p>Removed. This once generated Visual Studio 6 project files, but the generator has been removed since CMake 3.6. It is still possible to build with VS 6 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 7</h3>
<p>Removed. This once generated Visual Studio .NET 2002 project files, but the generator has been removed since CMake 3.6. It is still possible to build with VS 7.0 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 7 .NET 2003</h3>
<p>Removed. This once generated Visual Studio .NET 2003 project files, but the generator has been removed since CMake 3.9. It is still possible to build with VS 7.1 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 8 2005</h3>
<p>Removed. This once generated Visual Studio 8 2005 project files, but the generator has been removed since CMake 3.12. It is still possible to build with VS 2005 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 9 2008</h3>
<p>Generates Visual Studio 9 2008 project files.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> New in version 3.1: The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 9 2008&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 9 2008&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 9 2008&quot; -A Itanium</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 9 2008&quot; -A &lt;WinCE-SDK&gt;</code> (Specify a target platform matching a Windows CE SDK name.) </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 9 2008 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 9 2008 IA64</code></p>
<dd>Specify target platform <code>Itanium</code>.</p>
<dt><code>Visual Studio 9 2008 &lt;WinCE-SDK&gt;</code></p>
<dd>Specify target platform matching a Windows CE SDK name.</dl>
<h3>Visual Studio 10 2010</h3>
<p>Deprecated. Generates Visual Studio 10 (VS 2010) project files. </p>
<p> <code>NOTE:</code> This generator is deprecated and will be removed in a future version of CMake. It will still be possible to build with VS 10 2010 tools using the <code>Visual Studio 11 2012</code> (or above) generator with <code>CMAKE_GENERATOR_TOOLSET</code> set to <code>v100</code>, or by using the <code>NMake Makefiles</code> generator. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name <code>Visual Studio 10</code> without the year component.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (Database, Website, etc.) are not supported.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> New in version 3.1: The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 10 2010&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 10 2010&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 10 2010&quot; -A Itanium</code> </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 10 2010 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 10 2010 IA64</code></p>
<dd>Specify target platform <code>Itanium</code>.</dl>
<h3>Toolset Selection</h3>
<p>The <code>v100</code> toolset that comes with Visual Studio 10 2010 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset.</p>
<h3>Visual Studio 11 2012</h3>
<p>Generates Visual Studio 11 (VS 2012) project files. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name &quot;Visual Studio 11&quot; without the year component.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Database, Website, etc.) are not supported.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> New in version 3.1: The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 11 2012&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 11 2012&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 11 2012&quot; -A ARM</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 11 2012&quot; -A &lt;WinCE-SDK&gt;</code> (Specify a target platform matching a Windows CE SDK name.) </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 11 2012 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 11 2012 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</p>
<dt><code>Visual Studio 11 2012 &lt;WinCE-SDK&gt;</code></p>
<dd>Specify target platform matching a Windows CE SDK name.</dl>
<h3>Toolset Selection</h3>
<p>The <code>v110</code> toolset that comes with Visual Studio 11 2012 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset.</p>
<h3>Visual Studio 12 2013</h3>
<p>Generates Visual Studio 12 (VS 2013) project files. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name &quot;Visual Studio 12&quot; without the year component.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Powershell, Python, etc.) are not supported.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> New in version 3.1: The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 12 2013&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 12 2013&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 12 2013&quot; -A ARM</code> </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 12 2013 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 12 2013 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</dl>
<h3>Toolset Selection</h3>
<p>The <code>v120</code> toolset that comes with Visual Studio 12 2013 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> New in version 3.8: For each toolset that comes with this version of Visual Studio, there are variants that are themselves compiled for 32-bit (<code>x86</code>) and 64-bit (<code>x64</code>) hosts (independent of the architecture they target). By default this generator uses the 32-bit variant even on a 64-bit host. One may explicitly request use of either the 32-bit or 64-bit host tools by adding either <code>host=x86</code> or <code>host=x64</code> to the toolset specification. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details. </p>
<p> New in version 3.14: Added support for <code>host=x86</code> option.</p>
<h3>Visual Studio 14 2015</h3>
<p>New in version 3.1. </p>
<p> Generates Visual Studio 14 (VS 2015) project files.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Powershell, Python, etc.) are not supported.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 14 2015&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 14 2015&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 14 2015&quot; -A ARM</code> </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 14 2015 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 14 2015 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</dl>
<h3>Toolset Selection</h3>
<p>The <code>v140</code> toolset that comes with Visual Studio 14 2015 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> New in version 3.8: For each toolset that comes with this version of Visual Studio, there are variants that are themselves compiled for 32-bit (<code>x86</code>) and 64-bit (<code>x64</code>) hosts (independent of the architecture they target). By default this generator uses the 32-bit variant even on a 64-bit host. One may explicitly request use of either the 32-bit or 64-bit host tools by adding either <code>host=x86</code> or <code>host=x64</code> to the toolset specification. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details. </p>
<p> New in version 3.14: Added support for <code>host=x86</code> option.</p>
<h3>Windows 10 SDK Maximum Version for VS 2015</h3>
<p>New in version 3.19. </p>
<p> Microsoft stated in a &quot;Windows 10 October 2018 Update&quot; blog post that Windows 10 SDK versions (15063, 16299, 17134, 17763) are not supported by VS 2015 and are only supported by VS 2017 and later. Therefore by default CMake automatically ignores Windows 10 SDKs beyond <code>10.0.14393.0</code>. </p>
<p> However, there are other recommendations for certain driver/Win32 builds that indicate otherwise. A user can override this behavior by either setting the <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION_MAXIMUM</code> to a false value or setting the <code>CMAKE_VS_WINDOWS_TARGET_PLATFORM_VERSION_MAXIMUM</code> to the string value of the required maximum (e.g. <code>10.0.15063.0</code>).</p>
<h3>Visual Studio 15 2017</h3>
<p>New in version 3.7.1. </p>
<p> Generates Visual Studio 15 (VS 2017) project files.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Powershell, Python, etc.) are not supported.</p>
<h3>Instance Selection</h3>
<p>New in version 3.11. </p>
<p> VS 2017 supports multiple installations on the same machine. The <code>CMAKE_GENERATOR_INSTANCE</code> variable may be set as a cache entry containing the absolute path to a Visual Studio instance. If the value is not specified explicitly by the user or a toolchain file, CMake queries the Visual Studio Installer to locate VS instances, chooses one, and sets the variable as a cache entry to hold the value persistently. </p>
<p> When CMake first chooses an instance, if the <code>VS150COMNTOOLS</code> environment variable is set and points to the <code>Common7/Tools</code> directory within one of the instances, that instance will be used. Otherwise, if more than one instance is installed we do not define which one is chosen by default.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is <code>Win32</code>. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 15 2017&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 15 2017&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 15 2017&quot; -A ARM</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 15 2017&quot; -A ARM64</code> </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of the generator name. This is supported only for:</p>
<dt><code>Visual Studio 15 2017 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 15 2017 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</dl>
<h3>Toolset Selection</h3>
<p>The <code>v141</code> toolset that comes with Visual Studio 15 2017 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> New in version 3.8: For each toolset that comes with this version of Visual Studio, there are variants that are themselves compiled for 32-bit (<code>x86</code>) and 64-bit (<code>x64</code>) hosts (independent of the architecture they target). By default this generator uses the 32-bit variant even on a 64-bit host. One may explicitly request use of either the 32-bit or 64-bit host tools by adding either <code>host=x86</code> or <code>host=x64</code> to the toolset specification. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details. </p>
<p> New in version 3.14: Added support for <code>host=x86</code> option.</p>
<h3>Visual Studio 16 2019</h3>
<p>New in version 3.14. </p>
<p> Generates Visual Studio 16 (VS 2019) project files.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Powershell, Python, etc.) are not supported.</p>
<h3>Instance Selection</h3>
<p>VS 2019 supports multiple installations on the same machine. The <code>CMAKE_GENERATOR_INSTANCE</code> variable may be set as a cache entry containing the absolute path to a Visual Studio instance. If the value is not specified explicitly by the user or a toolchain file, CMake queries the Visual Studio Installer to locate VS instances, chooses one, and sets the variable as a cache entry to hold the value persistently. </p>
<p> When CMake first chooses an instance, if the <code>VS160COMNTOOLS</code> environment variable is set and points to the <code>Common7/Tools</code> directory within one of the instances, that instance will be used. Otherwise, if more than one instance is installed we do not define which one is chosen by default.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is that of the host and is provided in the <code>CMAKE_VS_PLATFORM_NAME_DEFAULT</code> variable. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 16 2019&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 16 2019&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 16 2019&quot; -A ARM</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 16 2019&quot; -A ARM64</code></dl>
<h3>Toolset Selection</h3>
<p>The <code>v142</code> toolset that comes with Visual Studio 16 2019 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> For each toolset that comes with this version of Visual Studio, there are variants that are themselves compiled for 32-bit (<code>x86</code>) and 64-bit (<code>x64</code>) hosts (independent of the architecture they target). By default this generator uses the 64-bit variant on x64 hosts and the 32-bit variant otherwise. One may explicitly request use of either the 32-bit or 64-bit host tools by adding either <code>host=x86</code> or <code>host=x64</code> to the toolset specification. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details.</p>
<h3>Visual Studio 17 2022</h3>
<p>New in version 3.21. </p>
<p> Generates Visual Studio 17 (VS 2022) project files.</p>
<h3>Project Types</h3>
<p>Only Visual C++ and C# projects may be generated (and Fortran with Intel compiler integration). Other types of projects (JavaScript, Powershell, Python, etc.) are not supported.</p>
<h3>Instance Selection</h3>
<p>VS 2022 supports multiple installations on the same machine. The <code>CMAKE_GENERATOR_INSTANCE</code> variable may be set as a cache entry containing the absolute path to a Visual Studio instance. If the value is not specified explicitly by the user or a toolchain file, CMake queries the Visual Studio Installer to locate VS instances, chooses one, and sets the variable as a cache entry to hold the value persistently. </p>
<p> When CMake first chooses an instance, if the <code>VS170COMNTOOLS</code> environment variable is set and points to the <code>Common7/Tools</code> directory within one of the instances, that instance will be used. Otherwise, if more than one instance is installed we do not define which one is chosen by default.</p>
<h3>Platform Selection</h3>
<p>The default target platform name (architecture) is that of the host and is provided in the <code>CMAKE_VS_PLATFORM_NAME_DEFAULT</code> variable. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-A</code> option, to specify a target platform name (architecture). For example:</p>
<dl>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 17 2022&quot; -A Win32</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 17 2022&quot; -A x64</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 17 2022&quot; -A ARM</code></p>
<dt>&bull;</p>
<dd><code>cmake -G &quot;Visual Studio 17 2022&quot; -A ARM64</code></dl>
<h3>Toolset Selection</h3>
<p>The <code>v143</code> toolset that comes with VS 17 2022 is selected by default. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> For each toolset that comes with this version of Visual Studio, there are variants that are themselves compiled for 32-bit (<code>x86</code>) and 64-bit (<code>x64</code>) hosts (independent of the architecture they target). By default this generator uses the 64-bit variant on x64 hosts and the 32-bit variant otherwise. One may explicitly request use of either the 32-bit or 64-bit host tools by adding either <code>host=x86</code> or <code>host=x64</code> to the toolset specification. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details.</p>
<h3>Other Generators</h3>
<h3>Green Hills MULTI</h3>
<p>New in version 3.3. </p>
<p> New in version 3.15: Linux support. </p>
<p> Generates Green Hills MULTI project files (experimental, work-in-progress). </p>
<p> Customizations are available through the following cache variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>GHS_CUSTOMIZATION</code></p>
<dt>&bull;</p>
<dd><code>GHS_GPJ_MACROS</code> </p>
<p> New in version 3.14: The buildsystem has predetermined build-configuration settings that can be controlled via the <code>CMAKE_BUILD_TYPE</code> variable. </p>
</dl>
<h3>Toolset and Platform Selection</h3>
<p>New in version 3.13. </p>
<p> Customizations that are used to pick toolset and target system:</p>
<dl>
<dt>&bull;</p>
<dd>The <code>-A &lt;arch&gt;</code> can be supplied for setting the target architecture. <code>&lt;arch&gt;</code> usually is one of <code>arm</code>, <code>ppc</code>, <code>86</code>, etcetera. If the target architecture is not specified then the default architecture of <code>arm</code> will be used.</p>
<dt>&bull;</p>
<dd>The <code>-T &lt;toolset&gt;</code> option can be used to set the directory location of the toolset. Both absolute and relative paths are valid. Relative paths use <code>GHS_TOOLSET_ROOT</code> as the root. If the toolset is not specified then the latest toolset found in <code>GHS_TOOLSET_ROOT</code> will be used. </p>
<p> Cache variables that are used for toolset and target system customization:</p>
<dt>&bull;</p>
<dd><code>GHS_TARGET_PLATFORM</code> </p>
<pre>Defaults to <code>integrity</code>.
Usual values are <code>integrity</code>, <code>threadx</code>, <code>uvelosity</code>, <code>velosity</code>,
<code>vxworks</code>, <code>standalone</code>.</pre>
<dt>&bull;</p>
<dd><code>GHS_PRIMARY_TARGET</code> </p>
<pre>Sets <code>primaryTarget</code> entry in project file.
Defaults to <code>&lt;arch&gt;_&lt;GHS_TARGET_PLATFORM&gt;.tgt</code>.</pre>
<dt>&bull;</p>
<dd><code>GHS_TOOLSET_ROOT</code> </p>
<pre>Root path for <code>toolset</code> searches.
Defaults to <code>C:/ghs</code> in Windows or <code>/usr/ghs</code> in Linux.</pre>
<dt>&bull;</p>
<dd><code>GHS_OS_ROOT</code> </p>
<pre>Root path for RTOS searches.
Defaults to <code>C:/ghs</code> in Windows or <code>/usr/ghs</code> in Linux.</pre>
<dt>&bull;</p>
<dd><code>GHS_OS_DIR</code> and <code>GHS_OS_DIR_OPTION</code> </p>
<pre>Sets <code>-os_dir</code> entry in project file.
Defaults to latest platform OS installation at <code>GHS_OS_ROOT</code>. Set this value if
a specific RTOS is to be used.
<code>GHS_OS_DIR_OPTION</code> default value is <code>-os_dir</code>.</pre>
<p>New in version 3.15: The <code>GHS_OS_DIR_OPTION</code> variable. </p>
<dt>&bull;</p>
<dd><code>GHS_BSP_NAME</code> </p>
<pre>Sets <code>-bsp</code> entry in project file.
Defaults to <code>sim&lt;arch&gt;</code> for <code>integrity</code> platforms.</pre>
</dl>
<h3>Target Properties</h3>
<p>New in version 3.14. </p>
<p> The following properties are available:</p>
<dl>
<dt>&bull;</p>
<dd><code>GHS_INTEGRITY_APP</code></p>
<dt>&bull;</p>
<dd><code>GHS_NO_SOURCE_GROUP_FILE</code> </p>
<p> <code>NOTE:</code> This generator is deemed experimental as of CMake 3.22.1 and is still a work in progress. Future versions of CMake may make breaking changes as the generator matures.</dl>
<h3>Xcode</h3>
<p>Generate Xcode project files. </p>
<p> Changed in version 3.15: This generator supports Xcode 5.0 and above.</p>
<h3>Toolset and Build System Selection</h3>
<p>By default Xcode is allowed to select its own default toolchain. The <code>CMAKE_GENERATOR_TOOLSET</code> option may be set, perhaps via the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> <code>-T</code> option, to specify another toolset. </p>
<p> New in version 3.19: This generator supports toolset specification using one of these forms: </p>
<dl>
<dt>&bull;</p>
<dd><code>toolset</code></p>
<dt>&bull;</p>
<dd><code>toolset[,key=value]*</code></p>
<dt>&bull;</p>
<dd><code>key=value[,key=value]*</code> </p>
<p> The <code>toolset</code> specifies the toolset name. The selected toolset name is provided in the <code>CMAKE_XCODE_PLATFORM_TOOLSET</code> variable. </p>
<p> The <code>key=value</code> pairs form a comma-separated list of options to specify generator-specific details of the toolset selection. Supported pairs are:</p>
<dt><code>buildsystem=&lt;variant&gt;</code></p>
<dd>Specify the buildsystem variant to use. See the <code>CMAKE_XCODE_BUILD_SYSTEM</code> variable for allowed values. </p>
<p> For example, to select the original build system under Xcode 12, run <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> with the option <code>-T buildsystem=1</code>.</dl>
<h3>Swift Support</h3>
<p>New in version 3.4. </p>
<p> When using the <i>Xcode</i> generator with Xcode 6.1 or higher, one may enable the <code>Swift</code> language with the <code>enable_language()</code> command or the <code>project()</code>.</p>
<h2>Extra Generators</h2>
<p>Some of the <i>CMake Generators</i> listed in the <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> command-line tool <code>&#8211;help</code> output may have variants that specify an extra generator for an auxiliary IDE tool. Such generator names have the form <code>&lt;extra-generator&gt; &#8211; &lt;main-generator&gt;</code>. The following extra generators are known to CMake.</p>
<h3>CodeBlocks</h3>
<p>Generates CodeBlocks project files. </p>
<p> Project files for CodeBlocks will be created in the top directory and in every subdirectory which features a <code>CMakeLists.txt</code> file containing a <code>project()</code> call. Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default <code>all</code> target. An <code>install</code> target is also provided. </p>
<p> New in version 3.10: The <code>CMAKE_CODEBLOCKS_EXCLUDE_EXTERNAL_FILES</code> variable may be set to <code>ON</code> to exclude any files which are located outside of the project root directory. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>CodeBlocks &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>CodeBlocks &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>CodeBlocks &#8211; NMake Makefiles JOM</code></p>
<dd>New in version 3.8: Generate with <code>NMake Makefiles JOM</code>. </p>
<dt><code>CodeBlocks &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>CodeBlocks &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h3>CodeLite</h3>
<p>Generates CodeLite project files. </p>
<p> Project files for CodeLite will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a <code>project()</code> call. The appropriate make program can build the project through the default <code>all</code> target. An <code>install</code> target is also provided. </p>
<p> New in version 3.7: The <code>CMAKE_CODELITE_USE_TARGETS</code> variable may be set to <code>ON</code> to change the default behavior from projects to targets as the basis for project files. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>CodeLite &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>CodeLite &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>CodeLite &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>CodeLite &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h3>Eclipse CDT4</h3>
<p>Generates Eclipse CDT 4.0 project files. </p>
<p> Project files for Eclipse will be created in the top directory. In out of source builds, a linked resource to the top level source directory will be created. Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default <code>all</code> target. An <code>install</code> target is also provided. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>Eclipse CDT4 &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>Eclipse CDT4 &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>Eclipse CDT4 &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>Eclipse CDT4 &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h3>Kate</h3>
<p>Generates Kate project files. </p>
<p> A project file for Kate will be created in the top directory in the top level build directory. To use it in Kate, the Project plugin must be enabled. The project file is loaded in Kate by opening the <code>ProjectName.kateproject</code> file in the editor. If the Kate Build-plugin is enabled, all targets generated by CMake are available for building. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>Kate &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>Kate &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>Kate &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>Kate &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h3>Sublime Text 2</h3>
<p>Generates Sublime Text 2 project files. </p>
<p> Project files for Sublime Text 2 will be created in the top directory and in every subdirectory which features a <code>CMakeLists.txt</code> file containing a <code>project()</code> call. Additionally <code>Makefiles</code> (or <code>build.ninja</code> files) are generated into the build tree. The appropriate make program can build the project through the default <code>all</code> target. An <code>install</code> target is also provided. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>Sublime Text 2 &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>Sublime Text 2 &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>Sublime Text 2 &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>Sublime Text 2 &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
