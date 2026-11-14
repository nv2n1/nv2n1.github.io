---
title: "cmake3-generators(7)"
name: "cmake3-generators"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-generators/"
description: "cmake-generators – CMake Generators Reference"
---

<p>cmake-generators &#8211; CMake Generators Reference</p>
<h2>Introduction</h2>
<p>A <i>CMake Generator</i> is responsible for writing the input files for a native build system. Exactly one of the <i>CMake Generators</i> must be selected for a build tree to determine what native build system is to be used. Optionally one of the <i>Extra Generators</i> may be selected as a variant of some of the <i>Command-Line Build Tool Generators</i> to produce project files for an auxiliary IDE. </p>
<p> CMake Generators are platform-specific so each may be available only on certain platforms. The <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> command-line tool <code>&#8211;help</code> output lists available generators on the current platform. Use its <code>-G</code> option to specify the generator for a new build tree. The <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> offers interactive selection of a generator when creating a new build tree.</p>
<h2>Cmake Generators</h2>
<h3>Command-Line Build Tool Generators</h3>
<p>These generators support command-line build tools. In order to use them, one must launch CMake from a command-line prompt whose environment is already configured for the chosen compiler and build tool.</p>
<h3>Makefile Generators</h3>
<h3>Borland Makefiles</h3>
<p>Generates Borland makefiles.</p>
<h3>MSYS Makefiles</h3>
<p>Generates makefiles for use with MSYS <code>make</code> under the MSYS shell. </p>
<p> Use this generator in a MSYS shell prompt and using <code>make</code> as the build tool. The generated makefiles use <code>/bin/sh</code> as the shell to launch build rules. They are not compatible with a Windows command prompt. </p>
<p> To build under a Windows command prompt, use the <code>MinGW Makefiles</code> generator.</p>
<h3>MinGW Makefiles</h3>
<p>Generates makefiles for use with <code>mingw32-make</code> under a Windows command prompt. </p>
<p> Use this generator under a Windows command prompt with MinGW in the <code>PATH</code> and using <code>mingw32-make</code> as the build tool. The generated makefiles use <code>cmd.exe</code> as the shell to launch build rules. They are not compatible with MSYS or a unix shell. </p>
<p> To build under the MSYS shell, use the <code>MSYS Makefiles</code> generator.</p>
<h3>NMake Makefiles</h3>
<p>Generates NMake makefiles.</p>
<h3>NMake Makefiles JOM</h3>
<p>Generates JOM makefiles.</p>
<h3>Unix Makefiles</h3>
<p>Generates standard UNIX makefiles. </p>
<p> A hierarchy of UNIX makefiles is generated into the build tree. Any standard UNIX-style make program can build the project through the default make target. A &quot;make install&quot; target is also provided.</p>
<h3>Watcom WMake</h3>
<p>Generates Watcom WMake makefiles.</p>
<h3>Ninja Generator</h3>
<h3>Ninja</h3>
<p>Generates build.ninja files. </p>
<p> A build.ninja file is generated into the build tree. Recent versions of the ninja program can build the project through the &quot;all&quot; target. An &quot;install&quot; target is also provided. </p>
<p> For each subdirectory <code>sub/dir</code> of the project an additional target named <code>sub/dir/all</code> is generated that depends on all targets required by that subdirectory.</p>
<h3>IDE Build Tool Generators</h3>
<p>These generators support Integrated Development Environment (IDE) project files. Since the IDEs configure their own environment one may launch CMake from any environment.</p>
<h3>Visual Studio Generators</h3>
<h3>Visual Studio 6</h3>
<p>Removed. This once generated Visual Studio 6 project files, but the generator has been removed since CMake 3.6. It is still possible to build with VS 6 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 7</h3>
<p>Removed. This once generated Visual Studio .NET 2002 project files, but the generator has been removed since CMake 3.6. It is still possible to build with VS 7.0 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 7 .NET 2003</h3>
<p>Deprecated. Generates Visual Studio .NET 2003 project files. </p>
<p> <code>NOTE:</code> This generator is deprecated and will be removed in a future version of CMake. It will still be possible to build with VS 7.1 tools using the <code>NMake Makefiles</code> generator.</p>
<h3>Visual Studio 8 2005</h3>
<p>Generates Visual Studio 8 2005 project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 8 2005 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 8 2005 &lt;WinCE-SDK&gt;</code></p>
<dd>Specify target platform matching a Windows CE SDK name.</dl>
<h3>Visual Studio 9 2008</h3>
<p>Generates Visual Studio 9 2008 project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 9 2008 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 9 2008 IA64</code></p>
<dd>Specify target platform <code>Itanium</code>.</p>
<dt><code>Visual Studio 9 2008 &lt;WinCE-SDK&gt;</code></p>
<dd>Specify target platform matching a Windows CE SDK name.</dl>
<h3>Visual Studio 10 2010</h3>
<p>Generates Visual Studio 10 (VS 2010) project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 10 2010 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 10 2010 IA64</code></p>
<dd>Specify target platform <code>Itanium</code>. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name <code>Visual Studio 10</code> without the year component.</dl>
<h3>Visual Studio 11 2012</h3>
<p>Generates Visual Studio 11 (VS 2012) project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 11 2012 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 11 2012 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</p>
<dt><code>Visual Studio 11 2012 &lt;WinCE-SDK&gt;</code></p>
<dd>Specify target platform matching a Windows CE SDK name. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name &quot;Visual Studio 11&quot; without the year component.</dl>
<h3>Visual Studio 12 2013</h3>
<p>Generates Visual Studio 12 (VS 2013) project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 12 2013 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 12 2013 ARM</code></p>
<dd>Specify target platform <code>ARM</code>. </p>
<p> For compatibility with CMake versions prior to 3.0, one may specify this generator using the name &quot;Visual Studio 12&quot; without the year component.</dl>
<h3>Visual Studio 14 2015</h3>
<p>Generates Visual Studio 14 (VS 2015) project files. </p>
<p> The <code>CMAKE_GENERATOR_PLATFORM</code> variable may be set to specify a target platform name. </p>
<p> For compatibility with CMake versions prior to 3.1, one may specify a target platform name optionally at the end of this generator name:</p>
<dl>
<dt><code>Visual Studio 14 2015 Win64</code></p>
<dd>Specify target platform <code>x64</code>.</p>
<dt><code>Visual Studio 14 2015 ARM</code></p>
<dd>Specify target platform <code>ARM</code>.</dl>
<h3>Other Generators</h3>
<h3>Green Hills MULTI</h3>
<p>Generates Green Hills MULTI project files (experimental, work-in-progress). </p>
<p> Customizations are available through the following cache variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>GHS_BSP_NAME</code></p>
<dt>&bull;</p>
<dd><code>GHS_CUSTOMIZATION</code></p>
<dt>&bull;</p>
<dd><code>GHS_GPJ_MACROS</code></p>
<dt>&bull;</p>
<dd><code>GHS_OS_DIR</code> </p>
<p> <code>NOTE:</code> This generator is deemed experimental as of CMake 3.6.3 and is still a work in progress. Future versions of CMake may make breaking changes as the generator matures.</dl>
<h3>Xcode</h3>
<p>Generate Xcode project files.</p>
<h2>Extra Generators</h2>
<p>Some of the <i>CMake Generators</i> listed in the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> command-line tool <code>&#8211;help</code> output may have variants that specify an extra generator for an auxiliary IDE tool. Such generator names have the form <code>&lt;extra-generator&gt; &#8211; &lt;main-generator&gt;</code>. The following extra generators are known to CMake.</p>
<h3>CodeBlocks</h3>
<p>Generates CodeBlocks project files. </p>
<p> Project files for CodeBlocks will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>CodeBlocks &#8211; MinGW Makefiles</code></p>
<dd>Generate with <code>MinGW Makefiles</code>.</p>
<dt><code>CodeBlocks &#8211; NMake Makefiles</code></p>
<dd>Generate with <code>NMake Makefiles</code>.</p>
<dt><code>CodeBlocks &#8211; Ninja</code></p>
<dd>Generate with <code>Ninja</code>.</p>
<dt><code>CodeBlocks &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</dl>
<h3>CodeLite</h3>
<p>Generates CodeLite project files. </p>
<p> Project files for CodeLite will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
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
<p> Project files for Eclipse will be created in the top directory. In out of source builds, a linked resource to the top level source directory will be created. Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
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
<h3>KDevelop3</h3>
<p>Generates KDevelop 3 project files. </p>
<p> Project files for KDevelop 3 will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. If you change the settings using KDevelop cmake will try its best to keep your changes when regenerating the project files. Additionally a hierarchy of UNIX makefiles is generated into the build tree. Any standard UNIX-style make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<p> This &quot;extra&quot; generator may be specified as:</p>
<dl>
<dt><code>KDevelop3 &#8211; Unix Makefiles</code></p>
<dd>Generate with <code>Unix Makefiles</code>.</p>
<dt><code>KDevelop3</code></p>
<dd>Generate with <code>Unix Makefiles</code>. </p>
<p> For historical reasons this extra generator may be specified directly as the main generator and it will be used as the extra generator with <code>Unix Makefiles</code> automatically.</dl>
<h3>Kate</h3>
<p>Generates Kate project files. </p>
<p> A project file for Kate will be created in the top directory in the top level build directory. To use it in kate, the Project plugin must be enabled. The project file is loaded in kate simply by opening the ProjectName.kateproject file in the editor. If the kate Build-plugin is enabled, all targets generated by CMake are available for building. </p>
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
<p> Project files for Sublime Text 2 will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. Additionally Makefiles (or build.ninja files) are generated into the build tree. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
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
<p>2000-2016 Kitware, Inc.</p>
