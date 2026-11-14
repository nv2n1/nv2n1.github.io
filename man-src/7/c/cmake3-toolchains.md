---
title: "cmake3-toolchains(7)"
name: "cmake3-toolchains"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-toolchains/"
description: "cmake-toolchains – CMake Toolchains Reference"
---

<p>cmake-toolchains &#8211; CMake Toolchains Reference</p>
<h2>Introduction</h2>
<p>CMake uses a toolchain of utilities to compile, link libraries and create archives, and other tasks to drive the build. The toolchain utilities available are determined by the languages enabled. In normal builds, CMake automatically determines the toolchain for host builds based on system introspection and defaults. In cross-compiling scenarios, a toolchain file may be specified with information about compiler and utility paths.</p>
<h2>Languages</h2>
<p>Languages are enabled by the <code>project()</code> command. Language-specific built-in variables, such as <code>CMAKE_CXX_COMPILER</code>, <code>CMAKE_CXX_COMPILER_ID</code> etc are set by invoking the <code>project()</code> command. If no project command is in the top-level CMakeLists file, one will be implicitly generated. By default the enabled languages are C and CXX: </p>
<pre>project(C_Only C)</pre>
<p>A special value of NONE can also be used with the <code>project()</code> command to enable no languages: </p>
<pre>project(MyProject NONE)</pre>
<p>The <code>enable_language()</code> command can be used to enable languages after the <code>project()</code> command: </p>
<pre>enable_language(CXX)</pre>
<p>When a language is enabled, CMake finds a compiler for that language, and determines some information, such as the vendor and version of the compiler, the target architecture and bitwidth, the location of corresponding utilities etc. </p>
<p> The <code>ENABLED_LANGUAGES</code> global property contains the languages which are currently enabled.</p>
<h2>Variables And Properties</h2>
<p>Several variables relate to the language components of a toolchain which are enabled. <code>CMAKE_&lt;LANG&gt;_COMPILER</code> is the full path to the compiler used for <code>&lt;LANG&gt;</code>. <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> is the identifier used by CMake for the compiler and <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> is the version of the compiler. </p>
<p> The <code>CMAKE_&lt;LANG&gt;_FLAGS</code> variables and the configuration-specific equivalents contain flags that will be added to the compile command when compiling a file of a particular language. </p>
<p> As the linker is invoked by the compiler driver, CMake needs a way to determine which compiler to use to invoke the linker. This is calculated by the <code>LANGUAGE</code> of source files in the target, and in the case of static libraries, the language of the dependent libraries. The choice CMake makes may be overridden with the <code>LINKER_LANGUAGE</code> target property.</p>
<h2>Toolchain Features</h2>
<p>CMake provides the <code>try_compile()</code> command and wrapper macros such as <code>CheckCXXSourceCompiles</code>, <code>CheckCXXSymbolExists</code> and <code>CheckIncludeFile</code> to test capability and availability of various toolchain features. These APIs test the toolchain in some way and cache the result so that the test does not have to be performed again the next time CMake runs. </p>
<p> Some toolchain features have built-in handling in CMake, and do not require compile-tests. For example, <code>POSITION_INDEPENDENT_CODE</code> allows specifying that a target should be built as position-independent code, if the compiler supports that feature. The <code>&lt;LANG&gt;_VISIBILITY_PRESET</code> and <code>VISIBILITY_INLINES_HIDDEN</code> target properties add flags for hidden visibility, if supported by the compiler.</p>
<h2>Cross Compiling</h2>
<p>If <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> is invoked with the command line parameter <code>-DCMAKE_TOOLCHAIN_FILE=path/to/file</code>, the file will be loaded early to set values for the compilers. The <code>CMAKE_CROSSCOMPILING</code> variable is set to true when CMake is cross-compiling.</p>
<h3>Cross Compiling for Linux</h3>
<p>A typical cross-compiling toolchain for Linux has content such as: </p>
<pre>set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_SYSROOT /home/devel/rasp-pi-rootfs)
set(CMAKE_STAGING_PREFIX /home/devel/stage)
set(tools /home/devel/gcc-4.7-linaro-rpi-gnueabihf)
set(CMAKE_C_COMPILER ${tools}/bin/arm-linux-gnueabihf-gcc)
set(CMAKE_CXX_COMPILER ${tools}/bin/arm-linux-gnueabihf-g++)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)</pre>
<p>The <code>CMAKE_SYSTEM_NAME</code> is the CMake-identifier of the target platform to build for. </p>
<p> The <code>CMAKE_SYSTEM_PROCESSOR</code> is the CMake-identifier of the target architecture to build for. </p>
<p> The <code>CMAKE_SYSROOT</code> is optional, and may be specified if a sysroot is available. </p>
<p> The <code>CMAKE_STAGING_PREFIX</code> is also optional. It may be used to specify a path on the host to install to. The <code>CMAKE_INSTALL_PREFIX</code> is always the runtime installation location, even when cross-compiling. </p>
<p> The <code>CMAKE_&lt;LANG&gt;_COMPILER</code> variables may be set to full paths, or to names of compilers to search for in standard locations. For toolchains that do not support linking binaries without custom flags or scripts one may set the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable to <code>STATIC_LIBRARY</code> to tell CMake not to try to link executables during its checks. </p>
<p> CMake <code>find_*</code> commands will look in the sysroot, and the <code>CMAKE_FIND_ROOT_PATH</code> entries by default in all cases, as well as looking in the host system root prefix. Although this can be controlled on a case-by-case basis, when cross-compiling, it can be useful to exclude looking in either the host or the target for particular artifacts. Generally, includes, libraries and packages should be found in the target system prefixes, whereas executables which must be run as part of the build should be found only on the host and not on the target. This is the purpose of the <code>CMAKE_FIND_ROOT_PATH_MODE_*</code> variables.</p>
<h3>Cross Compiling for the Cray Linux Environment</h3>
<p>Cross compiling for compute nodes in the Cray Linux Environment can be done without needing a separate toolchain file. Specifying <code>-DCMAKE_SYSTEM_NAME=CrayLinuxEnvironment</code> on the CMake command line will ensure that the appropriate build settings and search paths are configured. The platform will pull its configuration from the current environment variables and will configure a project to use the compiler wrappers from the Cray Programming Environment&#8217;s <code>PrgEnv-*</code> modules if present and loaded. </p>
<p> The default configuration of the Cray Programming Environment is to only support static libraries. This can be overridden and shared libraries enabled by setting the <code>CRAYPE_LINK_TYPE</code> environment variable to <code>dynamic</code>. </p>
<p> Running CMake without specifying <code>CMAKE_SYSTEM_NAME</code> will run the configure step in host mode assuming a standard Linux environment. If not overridden, the <code>PrgEnv-*</code> compiler wrappers will end up getting used, which if targeting the either the login node or compute node, is likely not the desired behavior. The exception to this would be if you are building directly on a NID instead of cross-compiling from a login node. If trying to build software for a login node, you will need to either first unload the currently loaded <code>PrgEnv-*</code> module or explicitly tell CMake to use the system compilers in <code>/usr/bin</code> instead of the Cray wrappers. If instead targeting a compute node is desired, just specify the <code>CMAKE_SYSTEM_NAME</code> as mentioned above.</p>
<h3>Cross Compiling using Clang</h3>
<p>Some compilers such as Clang are inherently cross compilers. The <code>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</code> can be set to pass a value to those supported compilers when compiling: </p>
<pre>set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(triple arm-linux-gnueabihf)
set(CMAKE_C_COMPILER clang)
set(CMAKE_C_COMPILER_TARGET ${triple})
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_COMPILER_TARGET ${triple})</pre>
<p>Similarly, some compilers do not ship their own supplementary utilities such as linkers, but provide a way to specify the location of the external toolchain which will be used by the compiler driver. The <code>CMAKE_&lt;LANG&gt;_COMPILER_EXTERNAL_TOOLCHAIN</code> variable can be set in a toolchain file to pass the path to the compiler driver.</p>
<h3>Cross Compiling for QNX</h3>
<p>As the Clang compiler the QNX QCC compile is inherently a cross compiler. And the <code>CMAKE_&lt;LANG&gt;_COMPILER_TARGET</code> can be set to pass a value to those supported compilers when compiling: </p>
<pre>set(CMAKE_SYSTEM_NAME QNX)
set(arch gcc_ntoarmv7le)
set(CMAKE_C_COMPILER qcc)
set(CMAKE_C_COMPILER_TARGET ${arch})
set(CMAKE_CXX_COMPILER QCC)
set(CMAKE_CXX_COMPILER_TARGET ${arch})</pre>
<h3>Cross Compiling for Windows CE</h3>
<p>Cross compiling for Windows CE requires the corresponding SDK being installed on your system. These SDKs are usually installed under <code>C:/Program Files (x86)/Windows CE Tools/SDKs</code>. </p>
<p> A toolchain file to configure a Visual Studio generator for Windows CE may look like this: </p>
<pre>set(CMAKE_SYSTEM_NAME WindowsCE)
set(CMAKE_SYSTEM_VERSION 8.0)
set(CMAKE_SYSTEM_PROCESSOR arm)
set(CMAKE_GENERATOR_TOOLSET CE800) # Can be omitted for 8.0
set(CMAKE_GENERATOR_PLATFORM SDK_AM335X_SK_WEC2013_V310)</pre>
<p>The <code>CMAKE_GENERATOR_PLATFORM</code> tells the generator which SDK to use. Further <code>CMAKE_SYSTEM_VERSION</code> tells the generator what version of Windows CE to use. Currently version 8.0 (Windows Embedded Compact 2013) is supported out of the box. Other versions may require one to set <code>CMAKE_GENERATOR_TOOLSET</code> to the correct value.</p>
<h3>Cross Compiling for Windows 10 Universal Applications</h3>
<p>A toolchain file to configure a Visual Studio generator for a Windows 10 Universal Application may look like this: </p>
<pre>set(CMAKE_SYSTEM_NAME WindowsStore)
set(CMAKE_SYSTEM_VERSION 10.0)</pre>
<p>A Windows 10 Universal Application targets both Windows Store and Windows Phone. Specify the <code>CMAKE_SYSTEM_VERSION</code> variable to be <code>10.0</code> to build with the latest available Windows 10 SDK. Specify a more specific version (e.g. <code>10.0.10240.0</code> for RTM) to build with the corresponding SDK.</p>
<h3>Cross Compiling for Windows Phone</h3>
<p>A toolchain file to configure a Visual Studio generator for Windows Phone may look like this: </p>
<pre>set(CMAKE_SYSTEM_NAME WindowsPhone)
set(CMAKE_SYSTEM_VERSION 8.1)</pre>
<h3>Cross Compiling for Windows Store</h3>
<p>A toolchain file to configure a Visual Studio generator for Windows Store may look like this: </p>
<pre>set(CMAKE_SYSTEM_NAME WindowsStore)
set(CMAKE_SYSTEM_VERSION 8.1)</pre>
<h3>Cross Compiling using NVIDIA Nsight Tegra</h3>
<p>A toolchain file to configure a Visual Studio generator to build using NVIDIA Nsight Tegra targeting Android may look like this: </p>
<pre>set(CMAKE_SYSTEM_NAME Android)</pre>
<p>The <code>CMAKE_GENERATOR_TOOLSET</code> may be set to select the Nsight Tegra &quot;Toolchain Version&quot; value. </p>
<p> See also target properties:</p>
<dl>
<dt>&bull;</p>
<dd><code>ANDROID_ANT_ADDITIONAL_OPTIONS</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_API_MIN</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_API</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_ARCH</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_ASSETS_DIRECTORIES</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_GUI</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_JAR_DEPENDENCIES</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_JAR_DIRECTORIES</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_JAVA_SOURCE_DIR</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_NATIVE_LIB_DEPENDENCIES</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_NATIVE_LIB_DIRECTORIES</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_PROCESS_MAX</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_PROGUARD_CONFIG_PATH</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_PROGUARD</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_SECURE_PROPS_PATH</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_SKIP_ANT_STEP</code></p>
<dt>&bull;</p>
<dd><code>ANDROID_STL_TYPE</code></dl>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
