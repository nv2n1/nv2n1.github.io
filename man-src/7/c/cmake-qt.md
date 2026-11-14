---
title: "cmake-qt(7)"
name: "cmake-qt"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-qt/"
description: "cmake-qt – CMake Qt Features Reference"
---

<p>cmake-qt &#8211; CMake Qt Features Reference</p>
<h2>Introduction</h2>
<p>CMake can find and use Qt 4 and Qt 5 libraries. The Qt 4 libraries are found by the <code>FindQt4</code> find-module shipped with CMake, whereas the Qt 5 libraries are found using &quot;Config-file Packages&quot; shipped with Qt 5. See <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> for more information about CMake packages, and see <i>the Qt cmake manual</i> for your Qt version. </p>
<p> Qt 4 and Qt 5 may be used together in the same <code>CMake buildsystem</code>: </p>
<pre>cmake_minimum_required(VERSION 3.8.0 FATAL_ERROR)
project(Qt4And5)
set(CMAKE_AUTOMOC ON)
find_package(Qt5 COMPONENTS Widgets DBus REQUIRED)
add_executable(publisher publisher.cpp)
target_link_libraries(publisher Qt5::Widgets Qt5::DBus)
find_package(Qt4 REQUIRED)
add_executable(subscriber subscriber.cpp)
target_link_libraries(subscriber Qt4::QtGui Qt4::QtDBus)</pre>
<p>A CMake target may not link to both Qt 4 and Qt 5. A diagnostic is issued if this is attempted or results from transitive target dependency evaluation.</p>
<h2>Qt Build Tools</h2>
<p>Qt relies on some bundled tools for code generation, such as <code>moc</code> for meta-object code generation, <code>uic</code> for widget layout and population, and <code>rcc</code> for virtual file system content generation. These tools may be automatically invoked by <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> if the appropriate conditions are met. The automatic tool invocation may be used with both Qt 4 and Qt 5.</p>
<h3>Automoc</h3>
<p>The <code>AUTOMOC</code> target property controls whether <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> inspects the C++ files in the target to determine if they require <code>moc</code> to be run, and to create rules to execute <code>moc</code> at the appropriate time. </p>
<p> If a macro from <code>AUTOMOC_MACRO_NAMES</code> is found in a header file, <code>moc</code> will be run on the file. The result will be put into a file named according to <code>moc_&lt;basename&gt;.cpp</code>. If the macro is found in a C++ implementation file, the moc output will be put into a file named according to <code>&lt;basename&gt;.moc</code>, following the Qt conventions. The <code>&lt;basename&gt;.moc</code> must be included by the user in the C++ implementation file with a preprocessor <code>#include</code>. </p>
<p> Included <code>moc_*.cpp</code> and <code>*.moc</code> files will be generated in the <code>&lt;AUTOGEN_BUILD_DIR&gt;/include</code> directory which is automatically added to the target&#8217;s <code>INCLUDE_DIRECTORIES</code>.</p>
<dl>
<dt>&bull;</p>
<dd>This differs from CMake 3.7 and below; see their documentation for details.</p>
<dt>&bull;</p>
<dd>For <code>multi configuration generators</code>, the include directory is <code>&lt;AUTOGEN_BUILD_DIR&gt;/include_&lt;CONFIG&gt;</code>.</p>
<dt>&bull;</p>
<dd>See <code>AUTOGEN_BUILD_DIR</code>. </p>
<p> Not included <code>moc_&lt;basename&gt;.cpp</code> files will be generated in custom folders to avoid name collisions and included in a separate file which is compiled into the target, named either <code>&lt;AUTOGEN_BUILD_DIR&gt;/mocs_compilation.cpp</code> or <code>&lt;AUTOGEN_BUILD_DIR&gt;/mocs_compilation_$&lt;CONFIG&gt;.cpp</code>.</p>
<dt>&bull;</p>
<dd>See <code>AUTOGEN_BUILD_DIR</code>. </p>
<p> The <code>moc</code> command line will consume the <code>COMPILE_DEFINITIONS</code> and <code>INCLUDE_DIRECTORIES</code> target properties from the target it is being invoked for, and for the appropriate build configuration. </p>
<p> The <code>AUTOMOC</code> target property may be pre-set for all following targets by setting the <code>CMAKE_AUTOMOC</code> variable. The <code>AUTOMOC_MOC_OPTIONS</code> target property may be populated to set options to pass to <code>moc</code>. The <code>CMAKE_AUTOMOC_MOC_OPTIONS</code> variable may be populated to pre-set the options for all following targets. </p>
<p> Additional macro names to search for can be added to <code>AUTOMOC_MACRO_NAMES</code>. </p>
<p> Additional <code>moc</code> dependency file names can be extracted from source code by using <code>AUTOMOC_DEPEND_FILTERS</code>. </p>
<p> Source C++ files can be excluded from <code>AUTOMOC</code> processing by enabling <code>SKIP_AUTOMOC</code> or the broader <code>SKIP_AUTOGEN</code>.</dl>
<h3>Autouic</h3>
<p>The <code>AUTOUIC</code> target property controls whether <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> inspects the C++ files in the target to determine if they require <code>uic</code> to be run, and to create rules to execute <code>uic</code> at the appropriate time. </p>
<p> If a preprocessor <code>#include</code> directive is found which matches <code>&lt;path&gt;ui_&lt;basename&gt;.h</code>, and a <code>&lt;basename&gt;.ui</code> file exists, then <code>uic</code> will be executed to generate the appropriate file. The <code>&lt;basename&gt;.ui</code> file is searched for in the following places</p>
<dl>
<dt>1.</p>
<dd><code>&lt;source_dir&gt;/&lt;basename&gt;.ui</code></p>
<dt>2.</p>
<dd><code>&lt;source_dir&gt;/&lt;path&gt;&lt;basename&gt;.ui</code></p>
<dt>3.</p>
<dd><code>&lt;AUTOUIC_SEARCH_PATHS&gt;/&lt;basename&gt;.ui</code></p>
<dt>4.</p>
<dd><code>&lt;AUTOUIC_SEARCH_PATHS&gt;/&lt;path&gt;&lt;basename&gt;.ui</code> </p>
<p> where <code>&lt;source_dir&gt;</code> is the directory of the C++ file and <code>AUTOUIC_SEARCH_PATHS</code> is a list of additional search paths. </p>
<p> The generated generated <code>ui_*.h</code> files are placed in the <code>&lt;AUTOGEN_BUILD_DIR&gt;/include</code> directory which is automatically added to the target&#8217;s <code>INCLUDE_DIRECTORIES</code>.</p>
<dt>&bull;</p>
<dd>This differs from CMake 3.7 and below; see their documentation for details.</p>
<dt>&bull;</p>
<dd>For <code>multi configuration generators</code>, the include directory is <code>&lt;AUTOGEN_BUILD_DIR&gt;/include_&lt;CONFIG&gt;</code>.</p>
<dt>&bull;</p>
<dd>See <code>AUTOGEN_BUILD_DIR</code>. </p>
<p> The <code>AUTOUIC</code> target property may be pre-set for all following targets by setting the <code>CMAKE_AUTOUIC</code> variable. The <code>AUTOUIC_OPTIONS</code> target property may be populated to set options to pass to <code>uic</code>. The <code>CMAKE_AUTOUIC_OPTIONS</code> variable may be populated to pre-set the options for all following targets. The <code>AUTOUIC_OPTIONS</code> source file property may be set on the <code>&lt;basename&gt;.ui</code> file to set particular options for the file. This overrides options from the <code>AUTOUIC_OPTIONS</code> target property. </p>
<p> A target may populate the <code>INTERFACE_AUTOUIC_OPTIONS</code> target property with options that should be used when invoking <code>uic</code>. This must be consistent with the <code>AUTOUIC_OPTIONS</code> target property content of the depender target. The <code>CMAKE_DEBUG_TARGET_PROPERTIES</code> variable may be used to track the origin target of such <code>INTERFACE_AUTOUIC_OPTIONS</code>. This means that a library which provides an alternative translation system for Qt may specify options which should be used when running <code>uic</code>: </p>
<pre>add_library(KI18n klocalizedstring.cpp)
target_link_libraries(KI18n Qt5::Core)
# KI18n uses the tr2i18n() function instead of tr(). That function is
# declared in the klocalizedstring.h header.
set(autouic_options
 -tr tr2i18n
 -include klocalizedstring.h
)
set_property(TARGET KI18n APPEND PROPERTY
 INTERFACE_AUTOUIC_OPTIONS ${autouic_options}
)</pre>
<p>A consuming project linking to the target exported from upstream automatically uses appropriate options when <code>uic</code> is run by <code>AUTOUIC</code>, as a result of linking with the <code>IMPORTED</code> target: </p>
<pre>set(CMAKE_AUTOUIC ON)
# Uses a libwidget.ui file:
add_library(LibWidget libwidget.cpp)
target_link_libraries(LibWidget
 KF5::KI18n
 Qt5::Widgets
)</pre>
<p>Source files can be excluded from <code>AUTOUIC</code> processing by enabling <code>SKIP_AUTOUIC</code> or the broader <code>SKIP_AUTOGEN</code>.</dl>
<h3>Autorcc</h3>
<p>The <code>AUTORCC</code> target property controls whether <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> creates rules to execute <code>rcc</code> at the appropriate time on source files which have the suffix <code>.qrc</code>. </p>
<pre>add_executable(myexe main.cpp resource_file.qrc)</pre>
<p>The <code>AUTORCC</code> target property may be pre-set for all following targets by setting the <code>CMAKE_AUTORCC</code> variable. The <code>AUTORCC_OPTIONS</code> target property may be populated to set options to pass to <code>rcc</code>. The <code>CMAKE_AUTORCC_OPTIONS</code> variable may be populated to pre-set the options for all following targets. The <code>AUTORCC_OPTIONS</code> source file property may be set on the <code>&lt;name&gt;.qrc</code> file to set particular options for the file. This overrides options from the <code>AUTORCC_OPTIONS</code> target property. </p>
<p> Source files can be excluded from <code>AUTORCC</code> processing by enabling <code>SKIP_AUTORCC</code> or the broader <code>SKIP_AUTOGEN</code>.</p>
<h2>THE &lt;ORIGIN&gt;_AUTOGEN TARGET</h2>
<p>The <code>moc</code> and <code>uic</code> tools are executed as part of a synthesized <code>&lt;ORIGIN&gt;_autogen</code> <code>custom target</code> generated by CMake. By default that <code>&lt;ORIGIN&gt;_autogen</code> target inherits the dependencies of the <code>&lt;ORIGIN&gt;</code> target (see <code>AUTOGEN_ORIGIN_DEPENDS</code>). Target dependencies may be added to the <code>&lt;ORIGIN&gt;_autogen</code> target by adding them to the <code>AUTOGEN_TARGET_DEPENDS</code> target property.</p>
<h2>Visual Studio Generators</h2>
<p>When using the <code>Visual Studio generators</code>, CMake generates a <code>PRE_BUILD</code> <code>custom command</code> instead of the <code>&lt;ORIGIN&gt;_autogen</code> <code>custom target</code> (for <code>AUTOMOC</code> and <code>AUTOUIC</code>). This isn&#8217;t always possible though and an <code>&lt;ORIGIN&gt;_autogen</code> <code>custom target</code> is used, when either</p>
<dl>
<dt>&bull;</p>
<dd>the <code>&lt;ORIGIN&gt;</code> target depends on <code>GENERATED</code> files which aren&#8217;t excluded from <code>AUTOMOC</code> and <code>AUTOUIC</code> by <code>SKIP_AUTOMOC</code>, <code>SKIP_AUTOUIC</code>, <code>SKIP_AUTOGEN</code> or <code>CMP0071</code></p>
<dt>&bull;</p>
<dd><code>AUTOGEN_TARGET_DEPENDS</code> lists a source file</p>
<dt>&bull;</p>
<dd><code>CMAKE_GLOBAL_AUTOGEN_TARGET</code> is enabled</dl>
<h2>Qtmain.Lib On Windows</h2>
<p>The Qt 4 and 5 <code>IMPORTED</code> targets for the QtGui libraries specify that the qtmain.lib static library shipped with Qt will be linked by all dependent executables which have the <code>WIN32_EXECUTABLE</code> enabled. </p>
<p> To disable this behavior, enable the <code>Qt5_NO_LINK_QTMAIN</code> target property for Qt 5 based targets or <code>QT4_NO_LINK_QTMAIN</code> target property for Qt 4 based targets. </p>
<pre>add_executable(myexe WIN32 main.cpp)
target_link_libraries(myexe Qt4::QtGui)
add_executable(myexe_no_qtmain WIN32 main_no_qtmain.cpp)
set_property(TARGET main_no_qtmain PROPERTY QT4_NO_LINK_QTMAIN ON)
target_link_libraries(main_no_qtmain Qt4::QtGui)</pre>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
