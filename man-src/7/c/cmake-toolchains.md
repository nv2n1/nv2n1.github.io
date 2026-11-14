---
title: "cmake-toolchains(7)"
name: "cmake-toolchains"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-toolchains/"
description: "cmake-toolchains – CMake Toolchains Reference"
---

<p>cmake-toolchains &#8211; CMake Toolchains Reference</p>
<h2>Introduction</h2>
<p>CMake uses a toolchain of utilities to compile, link libraries and create archives, and other tasks to drive the build. The toolchain utilities available are determined by the languages enabled. In normal builds, CMake automatically determines the toolchain for host builds based on system introspection and defaults. In cross-compiling scenarios, a toolchain file may be specified with information about compiler and utility paths.</p>
<h2>Languages</h2>
<p>Languages are enabled by the <code>project()</code> command. Language-specific built-in variables, such as <code>CMAKE_CXX_COMPILER</code>, <code>CMAKE_CXX_COMPILER_ID</code> etc are set by invoking the <code>project()</code> command. If no project command is in the top-level CMakeLists file, one will be implicitly generated. By default the enabled languages are <code>C</code> and <code>CXX</code>: </p>
<pre>project(C_Only C)</pre>
<p>A special value of <code>NONE</code> can also be used with the <code>project()</code> command to enable no languages: </p>
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
<p>If <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> is invoked with the command line parameter <code>&#8211;toolchain path/to/file</code> or <code>-DCMAKE_TOOLCHAIN_FILE=path/to/file</code>, the file will be loaded early to set values for the compilers. The <code>CMAKE_CROSSCOMPILING</code> variable is set to true when CMake is cross-compiling. </p>
<p> Note that using the <code>CMAKE_SOURCE_DIR</code> or <code>CMAKE_BINARY_DIR</code> variables inside a toolchain file is typically undesirable. The toolchain file is used in contexts where these variables have different values when used in different places (e.g. as part of a call to <code>try_compile()</code>). In most cases, where there is a need to evaluate paths inside a toolchain file, the more appropriate variable to use would be <code>CMAKE_CURRENT_LIST_DIR</code>, since it always has an unambiguous, predictable value.</p>
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
set(CMAKE_CXX_COMPILER_TARGET ${arch})
set(CMAKE_SYSROOT $ENV{QNX_TARGET})</pre>
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
<h3>Cross Compiling for Android</h3>
<p>A toolchain file may configure cross-compiling for Android by setting the <code>CMAKE_SYSTEM_NAME</code> variable to <code>Android</code>. Further configuration is specific to the Android development environment to be used. </p>
<p> For Visual Studio Generators, CMake expects <i>NVIDIA Nsight Tegra Visual Studio Edition</i> or the <i>Visual Studio tools for Android</i> to be installed. See those sections for further configuration details. </p>
<p> For Makefile Generators and the <code>Ninja</code> generator, CMake expects one of these environments:</p>
<dl>
<dt>&bull;</p>
<dd><i>NDK</i></p>
<dt>&bull;</p>
<dd><i>Standalone Toolchain</i> </p>
<p> CMake uses the following steps to select one of the environments:</p>
<dt>&bull;</p>
<dd>If the <code>CMAKE_ANDROID_NDK</code> variable is set, the NDK at the specified location will be used.</p>
<dt>&bull;</p>
<dd>Else, if the <code>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</code> variable is set, the Standalone Toolchain at the specified location will be used.</p>
<dt>&bull;</p>
<dd>Else, if the <code>CMAKE_SYSROOT</code> variable is set to a directory of the form <code>&lt;ndk&gt;/platforms/android-&lt;api&gt;/arch-&lt;arch&gt;</code>, the <code>&lt;ndk&gt;</code> part will be used as the value of <code>CMAKE_ANDROID_NDK</code> and the NDK will be used.</p>
<dt>&bull;</p>
<dd>Else, if the <code>CMAKE_SYSROOT</code> variable is set to a directory of the form <code>&lt;standalone-toolchain&gt;/sysroot</code>, the <code>&lt;standalone-toolchain&gt;</code> part will be used as the value of <code>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</code> and the Standalone Toolchain will be used.</p>
<dt>&bull;</p>
<dd>Else, if a cmake variable <code>ANDROID_NDK</code> is set it will be used as the value of <code>CMAKE_ANDROID_NDK</code>, and the NDK will be used.</p>
<dt>&bull;</p>
<dd>Else, if a cmake variable <code>ANDROID_STANDALONE_TOOLCHAIN</code> is set, it will be used as the value of <code>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</code>, and the Standalone Toolchain will be used.</p>
<dt>&bull;</p>
<dd>Else, if an environment variable <code>ANDROID_NDK_ROOT</code> or <code>ANDROID_NDK</code> is set, it will be used as the value of <code>CMAKE_ANDROID_NDK</code>, and the NDK will be used.</p>
<dt>&bull;</p>
<dd>Else, if an environment variable <code>ANDROID_STANDALONE_TOOLCHAIN</code> is set then it will be used as the value of <code>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</code>, and the Standalone Toolchain will be used.</p>
<dt>&bull;</p>
<dd>Else, an error diagnostic will be issued that neither the NDK or Standalone Toolchain can be found. </p>
<p> New in version 3.20: If an Android NDK is selected, its version number is reported in the <code>CMAKE_ANDROID_NDK_VERSION</code> variable. </p>
</dl>
<h3>Cross Compiling for Android with the NDK</h3>
<p>A toolchain file may configure Makefile Generators, Ninja Generators, or Visual Studio Generators to target Android for cross-compiling. </p>
<p> Configure use of an Android NDK with the following variables:</p>
<dl>
<dt><code>CMAKE_SYSTEM_NAME</code></p>
<dd>Set to <code>Android</code>. Must be specified to enable cross compiling for Android.</p>
<dt><code>CMAKE_SYSTEM_VERSION</code></p>
<dd>Set to the Android API level. If not specified, the value is determined as follows:</p>
<dt>&bull;</p>
<dd>If the <code>CMAKE_ANDROID_API</code> variable is set, its value is used as the API level.</p>
<dt>&bull;</p>
<dd>If the <code>CMAKE_SYSROOT</code> variable is set, the API level is detected from the NDK directory structure containing the sysroot.</p>
<dt>&bull;</p>
<dd>Otherwise, the latest API level available in the NDK is used.</p>
<dt><code>CMAKE_ANDROID_ARCH_ABI</code></p>
<dd>Set to the Android ABI (architecture). If not specified, this variable will default to the first supported ABI in the list of <code>armeabi</code>, <code>armeabi-v7a</code> and <code>arm64-v8a</code>. The <code>CMAKE_ANDROID_ARCH</code> variable will be computed from <code>CMAKE_ANDROID_ARCH_ABI</code> automatically. Also see the <code>CMAKE_ANDROID_ARM_MODE</code> and <code>CMAKE_ANDROID_ARM_NEON</code> variables.</p>
<dt><code>CMAKE_ANDROID_NDK</code></p>
<dd>Set to the absolute path to the Android NDK root directory. If not specified, a default for this variable will be chosen as specified <i>above</i>.</p>
<dt><code>CMAKE_ANDROID_NDK_DEPRECATED_HEADERS</code></p>
<dd>Set to a true value to use the deprecated per-api-level headers instead of the unified headers. If not specified, the default will be false unless using a NDK that does not provide unified headers.</p>
<dt><code>CMAKE_ANDROID_NDK_TOOLCHAIN_VERSION</code></p>
<dd>On NDK r19 or above, this variable must be unset or set to <code>clang</code>. On NDK r18 or below, set this to the version of the NDK toolchain to be selected as the compiler. If not specified, the default will be the latest available GCC toolchain.</p>
<dt><code>CMAKE_ANDROID_STL_TYPE</code></p>
<dd>Set to specify which C++ standard library to use. If not specified, a default will be selected as described in the variable documentation. </p>
<p> The following variables will be computed and provided automatically:</p>
<dt><code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_PREFIX</code></p>
<dd>The absolute path prefix to the binutils in the NDK toolchain.</p>
<dt><code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_SUFFIX</code></p>
<dd>The host platform suffix of the binutils in the NDK toolchain. </p>
<p> For example, a toolchain file might contain: </p>
<pre>set(CMAKE_SYSTEM_NAME Android)
set(CMAKE_SYSTEM_VERSION 21) # API level
set(CMAKE_ANDROID_ARCH_ABI arm64-v8a)
set(CMAKE_ANDROID_NDK /path/to/android-ndk)
set(CMAKE_ANDROID_STL_TYPE gnustl_static)</pre>
<p>Alternatively one may specify the values without a toolchain file: </p>
<pre>$ cmake ../src \
 -DCMAKE_SYSTEM_NAME=Android \
 -DCMAKE_SYSTEM_VERSION=21 \
 -DCMAKE_ANDROID_ARCH_ABI=arm64-v8a \
 -DCMAKE_ANDROID_NDK=/path/to/android-ndk \
 -DCMAKE_ANDROID_STL_TYPE=gnustl_static</pre>
</dl>
<h3>Cross Compiling for Android with a Standalone Toolchain</h3>
<p>A toolchain file may configure Makefile Generators or the <code>Ninja</code> generator to target Android for cross-compiling using a standalone toolchain. </p>
<p> Configure use of an Android standalone toolchain with the following variables:</p>
<dl>
<dt><code>CMAKE_SYSTEM_NAME</code></p>
<dd>Set to <code>Android</code>. Must be specified to enable cross compiling for Android.</p>
<dt><code>CMAKE_ANDROID_STANDALONE_TOOLCHAIN</code></p>
<dd>Set to the absolute path to the standalone toolchain root directory. A <code>${CMAKE_ANDROID_STANDALONE_TOOLCHAIN}/sysroot</code> directory must exist. If not specified, a default for this variable will be chosen as specified <i>above</i>.</p>
<dt><code>CMAKE_ANDROID_ARM_MODE</code></p>
<dd>When the standalone toolchain targets ARM, optionally set this to <code>ON</code> to target 32-bit ARM instead of 16-bit Thumb. See variable documentation for details.</p>
<dt><code>CMAKE_ANDROID_ARM_NEON</code></p>
<dd>When the standalone toolchain targets ARM v7, optionally set thisto <code>ON</code> to target ARM NEON devices. See variable documentation for details. </p>
<p> The following variables will be computed and provided automatically:</p>
<dt><code>CMAKE_SYSTEM_VERSION</code></p>
<dd>The Android API level detected from the standalone toolchain.</p>
<dt><code>CMAKE_ANDROID_ARCH_ABI</code></p>
<dd>The Android ABI detected from the standalone toolchain.</p>
<dt><code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_PREFIX</code></p>
<dd>The absolute path prefix to the <code>binutils</code> in the standalone toolchain.</p>
<dt><code>CMAKE_&lt;LANG&gt;_ANDROID_TOOLCHAIN_SUFFIX</code></p>
<dd>The host platform suffix of the <code>binutils</code> in the standalone toolchain. </p>
<p> For example, a toolchain file might contain: </p>
<pre>set(CMAKE_SYSTEM_NAME Android)
set(CMAKE_ANDROID_STANDALONE_TOOLCHAIN /path/to/android-toolchain)</pre>
<p>Alternatively one may specify the values without a toolchain file: </p>
<pre>$ cmake ../src \
 -DCMAKE_SYSTEM_NAME=Android \
 -DCMAKE_ANDROID_STANDALONE_TOOLCHAIN=/path/to/android-toolchain</pre>
</dl>
<h3>Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition</h3>
<p>A toolchain file to configure one of the Visual Studio Generators to build using NVIDIA Nsight Tegra targeting Android may look like this: </p>
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
<h3>Cross Compiling for iOS, tvOS, or watchOS</h3>
<p>For cross-compiling to iOS, tvOS, or watchOS, the <code>Xcode</code> generator is recommended. The <code>Unix Makefiles</code> or <code>Ninja</code> generators can also be used, but they require the project to handle more areas like target CPU selection and code signing. </p>
<p> Any of the three systems can be targeted by setting the <code>CMAKE_SYSTEM_NAME</code> variable to a value from the table below. By default, the latest Device SDK is chosen. As for all Apple platforms, a different SDK (e.g. a simulator) can be selected by setting the <code>CMAKE_OSX_SYSROOT</code> variable, although this should rarely be necessary (see <i>Switching Between Device and Simulator</i> below). A list of available SDKs can be obtained by running <code>xcodebuild -showsdks</code>. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> OS </td>
<td> CMAKE_SYSTEM_NAME </td>
<td> Device SDK (default) </td>
<td> Simulator SDK
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> iOS </td>
<td> iOS </td>
<td> iphoneos </td>
<td> iphonesimulator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> tvOS </td>
<td> tvOS </td>
<td> appletvos </td>
<td> appletvsimulator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> watchOS </td>
<td> watchOS </td>
<td> watchos </td>
<td> watchsimulator
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> For example, to create a CMake configuration for iOS, the following command is sufficient: </p>
<pre>cmake .. -GXcode -DCMAKE_SYSTEM_NAME=iOS</pre>
<p>Variable <code>CMAKE_OSX_ARCHITECTURES</code> can be used to set architectures for both device and simulator. Variable <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> can be used to set an iOS/tvOS/watchOS deployment target. </p>
<p> Next configuration will install fat 5 architectures iOS library and add the <code>-miphoneos-version-min=9.3</code>/<code>-mios-simulator-version-min=9.3</code> flags to the compiler: </p>
<pre>$ cmake -S. -B_builds -GXcode \
 -DCMAKE_SYSTEM_NAME=iOS \
 &quot;-DCMAKE_OSX_ARCHITECTURES=armv7;armv7s;arm64;i386;x86_64&quot; \
 -DCMAKE_OSX_DEPLOYMENT_TARGET=9.3 \
 -DCMAKE_INSTALL_PREFIX=`pwd`/_install \
 -DCMAKE_XCODE_ATTRIBUTE_ONLY_ACTIVE_ARCH=NO \
 -DCMAKE_IOS_INSTALL_COMBINED=YES</pre>
<p>Example: </p>
<pre># CMakeLists.txt
cmake_minimum_required(VERSION 3.14)
project(foo)
add_library(foo foo.cpp)
install(TARGETS foo DESTINATION lib)</pre>
<p>Install: </p>
<pre>$ cmake --build _builds --config Release --target install</pre>
<p>Check library: </p>
<pre>$ lipo -info _install/lib/libfoo.a
Architectures in the fat file: _install/lib/libfoo.a are: i386 armv7 armv7s x86_64 arm64</pre>
<pre>$ otool -l _install/lib/libfoo.a | grep -A2 LC_VERSION_MIN_IPHONEOS
 cmd LC_VERSION_MIN_IPHONEOS
 cmdsize 16
 version 9.3</pre>
<h3>Code Signing</h3>
<p>Some build artifacts for the embedded Apple platforms require mandatory code signing. If the <code>Xcode</code> generator is being used and code signing is required or desired, the development team ID can be specified via the <code>CMAKE_XCODE_ATTRIBUTE_DEVELOPMENT_TEAM</code> CMake variable. This team ID will then be included in the generated Xcode project. By default, CMake avoids the need for code signing during the internal configuration phase (i.e compiler ID and feature detection).</p>
<h3>Switching Between Device and Simulator</h3>
<p>When configuring for any of the embedded platforms, one can target either real devices or the simulator. Both have their own separate SDK, but CMake only supports specifying a single SDK for the configuration phase. This means the developer must select one or the other at configuration time. When using the <code>Xcode</code> generator, this is less of a limitation because Xcode still allows you to build for either a device or a simulator, even though configuration was only performed for one of the two. From within the Xcode IDE, builds are performed for the selected &quot;destination&quot; platform. When building from the command line, the desired sdk can be specified directly by passing a <code>-sdk</code> option to the underlying build tool (<code>xcodebuild</code>). For example: </p>
<pre>$ cmake --build ... -- -sdk iphonesimulator</pre>
<p>Please note that checks made during configuration were performed against the configure-time SDK and might not hold true for other SDKs. Commands like <code>find_package()</code>, <code>find_library()</code>, etc. store and use details only for the configured SDK/platform, so they can be problematic if wanting to switch between device and simulator builds. You can follow the next rules to make device + simulator configuration work:</p>
<dl>
<dt>&bull;</p>
<dd>Use explicit <code>-l</code> linker flag, e.g. <code>target_link_libraries(foo PUBLIC &quot;-lz&quot;)</code></p>
<dt>&bull;</p>
<dd>Use explicit <code>-framework</code> linker flag, e.g. <code>target_link_libraries(foo PUBLIC &quot;-framework CoreFoundation&quot;)</code></p>
<dt>&bull;</p>
<dd>Use <code>find_package()</code> only for libraries installed with <code>CMAKE_IOS_INSTALL_COMBINED</code> feature</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
