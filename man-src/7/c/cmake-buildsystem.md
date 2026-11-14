---
title: "cmake-buildsystem(7)"
name: "cmake-buildsystem"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-buildsystem/"
description: "cmake-buildsystem – CMake Buildsystem Reference"
---

<p>cmake-buildsystem &#8211; CMake Buildsystem Reference</p>
<h2>Introduction</h2>
<p>A CMake-based buildsystem is organized as a set of high-level logical targets. Each target corresponds to an executable or library, or is a custom target containing custom commands. Dependencies between the targets are expressed in the buildsystem to determine the build order and the rules for regeneration in response to change.</p>
<h2>Binary Targets</h2>
<p>Executables and libraries are defined using the <code>add_executable()</code> and <code>add_library()</code> commands. The resulting binary files have appropriate <code>PREFIX</code>, <code>SUFFIX</code> and extensions for the platform targeted. Dependencies between binary targets are expressed using the <code>target_link_libraries()</code> command: </p>
<pre>add_library(archive archive.cpp zip.cpp lzma.cpp)
add_executable(zipapp zipapp.cpp)
target_link_libraries(zipapp archive)</pre>
<p><code>archive</code> is defined as a <code>STATIC</code> library &#8212; an archive containing objects compiled from <code>archive.cpp</code>, <code>zip.cpp</code>, and <code>lzma.cpp</code>. <code>zipapp</code> is defined as an executable formed by compiling and linking <code>zipapp.cpp</code>. When linking the <code>zipapp</code> executable, the <code>archive</code> static library is linked in.</p>
<h3>Binary Executables</h3>
<p>The <code>add_executable()</code> command defines an executable target: </p>
<pre>add_executable(mytool mytool.cpp)</pre>
<p>Commands such as <code>add_custom_command()</code>, which generates rules to be run at build time can transparently use an <code>EXECUTABLE</code> target as a <code>COMMAND</code> executable. The buildsystem rules will ensure that the executable is built before attempting to run the command.</p>
<h3>Binary Library Types</h3>
<h3>Normal Libraries</h3>
<p>By default, the <code>add_library()</code> command defines a <code>STATIC</code> library, unless a type is specified. A type may be specified when using the command: </p>
<pre>add_library(archive SHARED archive.cpp zip.cpp lzma.cpp)</pre>
<pre>add_library(archive STATIC archive.cpp zip.cpp lzma.cpp)</pre>
<p>The <code>BUILD_SHARED_LIBS</code> variable may be enabled to change the behavior of <code>add_library()</code> to build shared libraries by default. </p>
<p> In the context of the buildsystem definition as a whole, it is largely irrelevant whether particular libraries are <code>SHARED</code> or <code>STATIC</code> &#8212; the commands, dependency specifications and other APIs work similarly regardless of the library type. The <code>MODULE</code> library type is dissimilar in that it is generally not linked to &#8212; it is not used in the right-hand-side of the <code>target_link_libraries()</code> command. It is a type which is loaded as a plugin using runtime techniques. If the library does not export any unmanaged symbols (e.g. Windows resource DLL, C++/CLI DLL), it is required that the library not be a <code>SHARED</code> library because CMake expects <code>SHARED</code> libraries to export at least one symbol. </p>
<pre>add_library(archive MODULE 7z.cpp)</pre>
<h3>Apple Frameworks</h3>
<p>A <code>SHARED</code> library may be marked with the <code>FRAMEWORK</code> target property to create an macOS or iOS Framework Bundle. A library with the <code>FRAMEWORK</code> target property should also set the <code>FRAMEWORK_VERSION</code> target property. This property is typically set to the value of &quot;A&quot; by macOS conventions. The <code>MACOSX_FRAMEWORK_IDENTIFIER</code> sets <code>CFBundleIdentifier</code> key and it uniquely identifies the bundle. </p>
<pre>add_library(MyFramework SHARED MyFramework.cpp)
set_target_properties(MyFramework PROPERTIES
 FRAMEWORK TRUE
 FRAMEWORK_VERSION A # Version &quot;A&quot; is macOS convention
 MACOSX_FRAMEWORK_IDENTIFIER org.cmake.MyFramework
)</pre>
<h3>Object Libraries</h3>
<p>The <code>OBJECT</code> library type defines a non-archival collection of object files resulting from compiling the given source files. The object files collection may be used as source inputs to other targets by using the syntax <code>$&lt;TARGET_OBJECTS:name&gt;</code>. This is a <code>generator expression</code> that can be used to supply the <code>OBJECT</code> library content to other targets: </p>
<pre>add_library(archive OBJECT archive.cpp zip.cpp lzma.cpp)
add_library(archiveExtras STATIC $&lt;TARGET_OBJECTS:archive&gt; extras.cpp)
add_executable(test_exe $&lt;TARGET_OBJECTS:archive&gt; test.cpp)</pre>
<p>The link (or archiving) step of those other targets will use the object files collection in addition to those from their own sources. </p>
<p> Alternatively, object libraries may be linked into other targets: </p>
<pre>add_library(archive OBJECT archive.cpp zip.cpp lzma.cpp)
add_library(archiveExtras STATIC extras.cpp)
target_link_libraries(archiveExtras PUBLIC archive)
add_executable(test_exe test.cpp)
target_link_libraries(test_exe archive)</pre>
<p>The link (or archiving) step of those other targets will use the object files from <code>OBJECT</code> libraries that are <i>directly</i> linked. Additionally, usage requirements of the <code>OBJECT</code> libraries will be honored when compiling sources in those other targets. Furthermore, those usage requirements will propagate transitively to dependents of those other targets. </p>
<p> Object libraries may not be used as the <code>TARGET</code> in a use of the <code>add_custom_command(TARGET)</code> command signature. However, the list of objects can be used by <code>add_custom_command(OUTPUT)</code> or <code>file(GENERATE)</code> by using <code>$&lt;TARGET_OBJECTS:objlib&gt;</code>.</p>
<h2>Build Specification And Usage Requirements</h2>
<p>The <code>target_include_directories()</code>, <code>target_compile_definitions()</code> and <code>target_compile_options()</code> commands specify the build specifications and the usage requirements of binary targets. The commands populate the <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code> target properties respectively, and/or the <code>INTERFACE_INCLUDE_DIRECTORIES</code>, <code>INTERFACE_COMPILE_DEFINITIONS</code> and <code>INTERFACE_COMPILE_OPTIONS</code> target properties. </p>
<p> Each of the commands has a <code>PRIVATE</code>, <code>PUBLIC</code> and <code>INTERFACE</code> mode. The <code>PRIVATE</code> mode populates only the non-<code>INTERFACE_</code> variant of the target property and the <code>INTERFACE</code> mode populates only the <code>INTERFACE_</code> variants. The <code>PUBLIC</code> mode populates both variants of the respective target property. Each command may be invoked with multiple uses of each keyword: </p>
<pre>target_compile_definitions(archive
 PRIVATE BUILDING_WITH_LZMA
 INTERFACE USING_ARCHIVE_LIB
)</pre>
<p>Note that usage requirements are not designed as a way to make downstreams use particular <code>COMPILE_OPTIONS</code> or <code>COMPILE_DEFINITIONS</code> etc for convenience only. The contents of the properties must be <code>requirements</code>, not merely recommendations or convenience. </p>
<p> See the Creating Relocatable Packages section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>Target Properties</h3>
<p>The contents of the <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and <code>COMPILE_OPTIONS</code> target properties are used appropriately when compiling the source files of a binary target. </p>
<p> Entries in the <code>INCLUDE_DIRECTORIES</code> are added to the compile line with <code>-I</code> or <code>-isystem</code> prefixes and in the order of appearance in the property value. </p>
<p> Entries in the <code>COMPILE_DEFINITIONS</code> are prefixed with <code>-D</code> or <code>/D</code> and added to the compile line in an unspecified order. The <code>DEFINE_SYMBOL</code> target property is also added as a compile definition as a special convenience case for <code>SHARED</code> and <code>MODULE</code> library targets. </p>
<p> Entries in the <code>COMPILE_OPTIONS</code> are escaped for the shell and added in the order of appearance in the property value. Several compile options have special separate handling, such as <code>POSITION_INDEPENDENT_CODE</code>. </p>
<p> The contents of the <code>INTERFACE_INCLUDE_DIRECTORIES</code>, <code>INTERFACE_COMPILE_DEFINITIONS</code> and <code>INTERFACE_COMPILE_OPTIONS</code> target properties are <i>Usage Requirements</i> &#8212; they specify content which consumers must use to correctly compile and link with the target they appear on. For any binary target, the contents of each <code>INTERFACE_</code> property on each target specified in a <code>target_link_libraries()</code> command is consumed: </p>
<pre>set(srcs archive.cpp zip.cpp)
if (LZMA_FOUND)
 list(APPEND srcs lzma.cpp)
endif()
add_library(archive SHARED ${srcs})
if (LZMA_FOUND)
 # The archive library sources are compiled with -DBUILDING_WITH_LZMA
 target_compile_definitions(archive PRIVATE BUILDING_WITH_LZMA)
endif()
target_compile_definitions(archive INTERFACE USING_ARCHIVE_LIB)
add_executable(consumer)
# Link consumer to archive and consume its usage requirements. The consumer
# executable sources are compiled with -DUSING_ARCHIVE_LIB.
target_link_libraries(consumer archive)</pre>
<p>Because it is common to require that the source directory and corresponding build directory are added to the <code>INCLUDE_DIRECTORIES</code>, the <code>CMAKE_INCLUDE_CURRENT_DIR</code> variable can be enabled to conveniently add the corresponding directories to the <code>INCLUDE_DIRECTORIES</code> of all targets. The variable <code>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</code> can be enabled to add the corresponding directories to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of all targets. This makes use of targets in multiple different directories convenient through use of the <code>target_link_libraries()</code> command.</p>
<h3>Transitive Usage Requirements</h3>
<p>The usage requirements of a target can transitively propagate to dependents. The <code>target_link_libraries()</code> command has <code>PRIVATE</code>, <code>INTERFACE</code> and <code>PUBLIC</code> keywords to control the propagation. </p>
<pre>add_library(archive archive.cpp)
target_compile_definitions(archive INTERFACE USING_ARCHIVE_LIB)
add_library(serialization serialization.cpp)
target_compile_definitions(serialization INTERFACE USING_SERIALIZATION_LIB)
add_library(archiveExtras extras.cpp)
target_link_libraries(archiveExtras PUBLIC archive)
target_link_libraries(archiveExtras PRIVATE serialization)
# archiveExtras is compiled with -DUSING_ARCHIVE_LIB
# and -DUSING_SERIALIZATION_LIB
add_executable(consumer consumer.cpp)
# consumer is compiled with -DUSING_ARCHIVE_LIB
target_link_libraries(consumer archiveExtras)</pre>
<p>Because <code>archive</code> is a <code>PUBLIC</code> dependency of <code>archiveExtras</code>, the usage requirements of it are propagated to <code>consumer</code> too. Because <code>serialization</code> is a <code>PRIVATE</code> dependency of <code>archiveExtras</code>, the usage requirements of it are not propagated to <code>consumer</code>. </p>
<p> Generally, a dependency should be specified in a use of <code>target_link_libraries()</code> with the <code>PRIVATE</code> keyword if it is used by only the implementation of a library, and not in the header files. If a dependency is additionally used in the header files of a library (e.g. for class inheritance), then it should be specified as a <code>PUBLIC</code> dependency. A dependency which is not used by the implementation of a library, but only by its headers should be specified as an <code>INTERFACE</code> dependency. The <code>target_link_libraries()</code> command may be invoked with multiple uses of each keyword: </p>
<pre>target_link_libraries(archiveExtras
 PUBLIC archive
 PRIVATE serialization
)</pre>
<p>Usage requirements are propagated by reading the <code>INTERFACE_</code> variants of target properties from dependencies and appending the values to the non-<code>INTERFACE_</code> variants of the operand. For example, the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of dependencies is read and appended to the <code>INCLUDE_DIRECTORIES</code> of the operand. In cases where order is relevant and maintained, and the order resulting from the <code>target_link_libraries()</code> calls does not allow correct compilation, use of an appropriate command to set the property directly may update the order. </p>
<p> For example, if the linked libraries for a target must be specified in the order <code>lib1</code> <code>lib2</code> <code>lib3</code> , but the include directories must be specified in the order <code>lib3</code> <code>lib1</code> <code>lib2</code>: </p>
<pre>target_link_libraries(myExe lib1 lib2 lib3)
target_include_directories(myExe
 PRIVATE $&lt;TARGET_PROPERTY:lib3,INTERFACE_INCLUDE_DIRECTORIES&gt;)</pre>
<p>Note that care must be taken when specifying usage requirements for targets which will be exported for installation using the <code>install(EXPORT)</code> command. See Creating Packages for more.</p>
<h3>Compatible Interface Properties</h3>
<p>Some target properties are required to be compatible between a target and the interface of each dependency. For example, the <code>POSITION_INDEPENDENT_CODE</code> target property may specify a boolean value of whether a target should be compiled as position-independent-code, which has platform-specific consequences. A target may also specify the usage requirement <code>INTERFACE_POSITION_INDEPENDENT_CODE</code> to communicate that consumers must be compiled as position-independent-code. </p>
<pre>add_executable(exe1 exe1.cpp)
set_property(TARGET exe1 PROPERTY POSITION_INDEPENDENT_CODE ON)
add_library(lib1 SHARED lib1.cpp)
set_property(TARGET lib1 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)
add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1)</pre>
<p>Here, both <code>exe1</code> and <code>exe2</code> will be compiled as position-independent-code. <code>lib1</code> will also be compiled as position-independent-code because that is the default setting for <code>SHARED</code> libraries. If dependencies have conflicting, non-compatible requirements <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> issues a diagnostic: </p>
<pre>add_library(lib1 SHARED lib1.cpp)
set_property(TARGET lib1 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)
add_library(lib2 SHARED lib2.cpp)
set_property(TARGET lib2 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE OFF)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1)
set_property(TARGET exe1 PROPERTY POSITION_INDEPENDENT_CODE OFF)
add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1 lib2)</pre>
<p>The <code>lib1</code> requirement <code>INTERFACE_POSITION_INDEPENDENT_CODE</code> is not &quot;compatible&quot; with the <code>POSITION_INDEPENDENT_CODE</code> property of the <code>exe1</code> target. The library requires that consumers are built as position-independent-code, while the executable specifies to not built as position-independent-code, so a diagnostic is issued. </p>
<p> The <code>lib1</code> and <code>lib2</code> requirements are not &quot;compatible&quot;. One of them requires that consumers are built as position-independent-code, while the other requires that consumers are not built as position-independent-code. Because <code>exe2</code> links to both and they are in conflict, a CMake error message is issued: </p>
<pre>CMake Error: The INTERFACE_POSITION_INDEPENDENT_CODE property of &quot;lib2&quot; does
not agree with the value of POSITION_INDEPENDENT_CODE already determined
for &quot;exe2&quot;.</pre>
<p>To be &quot;compatible&quot;, the <code>POSITION_INDEPENDENT_CODE</code> property, if set must be either the same, in a boolean sense, as the <code>INTERFACE_POSITION_INDEPENDENT_CODE</code> property of all transitively specified dependencies on which that property is set. </p>
<p> This property of &quot;compatible interface requirement&quot; may be extended to other properties by specifying the property in the content of the <code>COMPATIBLE_INTERFACE_BOOL</code> target property. Each specified property must be compatible between the consuming target and the corresponding property with an <code>INTERFACE_</code> prefix from each dependency: </p>
<pre>add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_CUSTOM_PROP ON)
set_property(TARGET lib1Version2 APPEND PROPERTY
 COMPATIBLE_INTERFACE_BOOL CUSTOM_PROP
)
add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_CUSTOM_PROP OFF)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2) # CUSTOM_PROP will be ON
add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1Version2 lib1Version3) # Diagnostic</pre>
<p>Non-boolean properties may also participate in &quot;compatible interface&quot; computations. Properties specified in the <code>COMPATIBLE_INTERFACE_STRING</code> property must be either unspecified or compare to the same string among all transitively specified dependencies. This can be useful to ensure that multiple incompatible versions of a library are not linked together through transitive requirements of a target: </p>
<pre>add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_LIB_VERSION 2)
set_property(TARGET lib1Version2 APPEND PROPERTY
 COMPATIBLE_INTERFACE_STRING LIB_VERSION
)
add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_LIB_VERSION 3)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2) # LIB_VERSION will be &quot;2&quot;
add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1Version2 lib1Version3) # Diagnostic</pre>
<p>The <code>COMPATIBLE_INTERFACE_NUMBER_MAX</code> target property specifies that content will be evaluated numerically and the maximum number among all specified will be calculated: </p>
<pre>add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_CONTAINER_SIZE_REQUIRED 200)
set_property(TARGET lib1Version2 APPEND PROPERTY
 COMPATIBLE_INTERFACE_NUMBER_MAX CONTAINER_SIZE_REQUIRED
)
add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_CONTAINER_SIZE_REQUIRED 1000)
add_executable(exe1 exe1.cpp)
# CONTAINER_SIZE_REQUIRED will be &quot;200&quot;
target_link_libraries(exe1 lib1Version2)
add_executable(exe2 exe2.cpp)
# CONTAINER_SIZE_REQUIRED will be &quot;1000&quot;
target_link_libraries(exe2 lib1Version2 lib1Version3)</pre>
<p>Similarly, the <code>COMPATIBLE_INTERFACE_NUMBER_MIN</code> may be used to calculate the numeric minimum value for a property from dependencies. </p>
<p> Each calculated &quot;compatible&quot; property value may be read in the consumer at generate-time using generator expressions. </p>
<p> Note that for each dependee, the set of properties specified in each compatible interface property must not intersect with the set specified in any of the other properties.</p>
<h3>Property Origin Debugging</h3>
<p>Because build specifications can be determined by dependencies, the lack of locality of code which creates a target and code which is responsible for setting build specifications may make the code more difficult to reason about. <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> provides a debugging facility to print the origin of the contents of properties which may be determined by dependencies. The properties which can be debugged are listed in the <code>CMAKE_DEBUG_TARGET_PROPERTIES</code> variable documentation: </p>
<pre>set(CMAKE_DEBUG_TARGET_PROPERTIES
 INCLUDE_DIRECTORIES
 COMPILE_DEFINITIONS
 POSITION_INDEPENDENT_CODE
 CONTAINER_SIZE_REQUIRED
 LIB_VERSION
)
add_executable(exe1 exe1.cpp)</pre>
<p>In the case of properties listed in <code>COMPATIBLE_INTERFACE_BOOL</code> or <code>COMPATIBLE_INTERFACE_STRING</code>, the debug output shows which target was responsible for setting the property, and which other dependencies also defined the property. In the case of <code>COMPATIBLE_INTERFACE_NUMBER_MAX</code> and <code>COMPATIBLE_INTERFACE_NUMBER_MIN</code>, the debug output shows the value of the property from each dependency, and whether the value determines the new extreme.</p>
<h3>Build Specification with Generator Expressions</h3>
<p>Build specifications may use <code>generator expressions</code> containing content which may be conditional or known only at generate-time. For example, the calculated &quot;compatible&quot; value of a property may be read with the <code>TARGET_PROPERTY</code> expression: </p>
<pre>add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY
 INTERFACE_CONTAINER_SIZE_REQUIRED 200)
set_property(TARGET lib1Version2 APPEND PROPERTY
 COMPATIBLE_INTERFACE_NUMBER_MAX CONTAINER_SIZE_REQUIRED
)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2)
target_compile_definitions(exe1 PRIVATE
 CONTAINER_SIZE=$&lt;TARGET_PROPERTY:CONTAINER_SIZE_REQUIRED&gt;
)</pre>
<p>In this case, the <code>exe1</code> source files will be compiled with <code>-DCONTAINER_SIZE=200</code>. </p>
<p> The unary <code>TARGET_PROPERTY</code> generator expression and the <code>TARGET_POLICY</code> generator expression are evaluated with the consuming target context. This means that a usage requirement specification may be evaluated differently based on the consumer: </p>
<pre>add_library(lib1 lib1.cpp)
target_compile_definitions(lib1 INTERFACE
 $&lt;$&lt;STREQUAL:$&lt;TARGET_PROPERTY:TYPE&gt;,EXECUTABLE&gt;:LIB1_WITH_EXE&gt;
 $&lt;$&lt;STREQUAL:$&lt;TARGET_PROPERTY:TYPE&gt;,SHARED_LIBRARY&gt;:LIB1_WITH_SHARED_LIB&gt;
 $&lt;$&lt;TARGET_POLICY:CMP0041&gt;:CONSUMER_CMP0041_NEW&gt;
)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1)
cmake_policy(SET CMP0041 NEW)
add_library(shared_lib shared_lib.cpp)
target_link_libraries(shared_lib lib1)</pre>
<p>The <code>exe1</code> executable will be compiled with <code>-DLIB1_WITH_EXE</code>, while the <code>shared_lib</code> shared library will be compiled with <code>-DLIB1_WITH_SHARED_LIB</code> and <code>-DCONSUMER_CMP0041_NEW</code>, because policy <code>CMP0041</code> is <code>NEW</code> at the point where the <code>shared_lib</code> target is created. </p>
<p> The <code>BUILD_INTERFACE</code> expression wraps requirements which are only used when consumed from a target in the same buildsystem, or when consumed from a target exported to the build directory using the <code>export()</code> command. The <code>INSTALL_INTERFACE</code> expression wraps requirements which are only used when consumed from a target which has been installed and exported with the <code>install(EXPORT)</code> command: </p>
<pre>add_library(ClimbingStats climbingstats.cpp)
target_compile_definitions(ClimbingStats INTERFACE
 $&lt;BUILD_INTERFACE:ClimbingStats_FROM_BUILD_LOCATION&gt;
 $&lt;INSTALL_INTERFACE:ClimbingStats_FROM_INSTALLED_LOCATION&gt;
)
install(TARGETS ClimbingStats EXPORT libExport ${InstallArgs})
install(EXPORT libExport NAMESPACE Upstream::
 DESTINATION lib/cmake/ClimbingStats)
export(EXPORT libExport NAMESPACE Upstream::)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 ClimbingStats)</pre>
<p>In this case, the <code>exe1</code> executable will be compiled with <code>-DClimbingStats_FROM_BUILD_LOCATION</code>. The exporting commands generate <code>IMPORTED</code> targets with either the <code>INSTALL_INTERFACE</code> or the <code>BUILD_INTERFACE</code> omitted, and the <code>*_INTERFACE</code> marker stripped away. A separate project consuming the <code>ClimbingStats</code> package would contain: </p>
<pre>find_package(ClimbingStats REQUIRED)
add_executable(Downstream main.cpp)
target_link_libraries(Downstream Upstream::ClimbingStats)</pre>
<p>Depending on whether the <code>ClimbingStats</code> package was used from the build location or the install location, the <code>Downstream</code> target would be compiled with either <code>-DClimbingStats_FROM_BUILD_LOCATION</code> or <code>-DClimbingStats_FROM_INSTALL_LOCATION</code>. For more about packages and exporting see the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual.</p>
<h3>Include Directories and Usage Requirements</h3>
<p>Include directories require some special consideration when specified as usage requirements and when used with generator expressions. The <code>target_include_directories()</code> command accepts both relative and absolute include directories: </p>
<pre>add_library(lib1 lib1.cpp)
target_include_directories(lib1 PRIVATE
 /absolute/path
 relative/path
)</pre>
<p>Relative paths are interpreted relative to the source directory where the command appears. Relative paths are not allowed in the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of <code>IMPORTED</code> targets. </p>
<p> In cases where a non-trivial generator expression is used, the <code>INSTALL_PREFIX</code> expression may be used within the argument of an <code>INSTALL_INTERFACE</code> expression. It is a replacement marker which expands to the installation prefix when imported by a consuming project. </p>
<p> Include directories usage requirements commonly differ between the build-tree and the install-tree. The <code>BUILD_INTERFACE</code> and <code>INSTALL_INTERFACE</code> generator expressions can be used to describe separate usage requirements based on the usage location. Relative paths are allowed within the <code>INSTALL_INTERFACE</code> expression and are interpreted relative to the installation prefix. For example: </p>
<pre>add_library(ClimbingStats climbingstats.cpp)
target_include_directories(ClimbingStats INTERFACE
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/generated&gt;
 $&lt;INSTALL_INTERFACE:/absolute/path&gt;
 $&lt;INSTALL_INTERFACE:relative/path&gt;
 $&lt;INSTALL_INTERFACE:$&lt;INSTALL_PREFIX&gt;/$&lt;CONFIG&gt;/generated&gt;
)</pre>
<p>Two convenience APIs are provided relating to include directories usage requirements. The <code>CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE</code> variable may be enabled, with an equivalent effect to: </p>
<pre>set_property(TARGET tgt APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR};${CMAKE_CURRENT_BINARY_DIR}&gt;
)</pre>
<p>for each target affected. The convenience for installed targets is an <code>INCLUDES DESTINATION</code> component with the <code>install(TARGETS)</code> command: </p>
<pre>install(TARGETS foo bar bat EXPORT tgts ${dest_args}
 INCLUDES DESTINATION include
)
install(EXPORT tgts ${other_args})
install(FILES ${headers} DESTINATION include)</pre>
<p>This is equivalent to appending <code>${CMAKE_INSTALL_PREFIX}/include</code> to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of each of the installed <code>IMPORTED</code> targets when generated by <code>install(EXPORT)</code>. </p>
<p> When the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of an <i>imported target</i> is consumed, the entries in the property are treated as <code>SYSTEM</code> include directories, as if they were listed in the <code>INTERFACE_SYSTEM_INCLUDE_DIRECTORIES</code> of the dependency. This can result in omission of compiler warnings for headers found in those directories. This behavior for <i>Imported Targets</i> may be controlled by setting the <code>NO_SYSTEM_FROM_IMPORTED</code> target property on the <i>consumers</i> of imported targets. </p>
<p> If a binary target is linked transitively to a macOS <code>FRAMEWORK</code>, the <code>Headers</code> directory of the framework is also treated as a usage requirement. This has the same effect as passing the framework directory as an include directory.</p>
<h3>Link Libraries and Generator Expressions</h3>
<p>Like build specifications, <code>link libraries</code> may be specified with generator expression conditions. However, as consumption of usage requirements is based on collection from linked dependencies, there is an additional limitation that the link dependencies must form a &quot;directed acyclic graph&quot;. That is, if linking to a target is dependent on the value of a target property, that target property may not be dependent on the linked dependencies: </p>
<pre>add_library(lib1 lib1.cpp)
add_library(lib2 lib2.cpp)
target_link_libraries(lib1 PUBLIC
 $&lt;$&lt;TARGET_PROPERTY:POSITION_INDEPENDENT_CODE&gt;:lib2&gt;
)
add_library(lib3 lib3.cpp)
set_property(TARGET lib3 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1 lib3)</pre>
<p>As the value of the <code>POSITION_INDEPENDENT_CODE</code> property of the <code>exe1</code> target is dependent on the linked libraries (<code>lib3</code>), and the edge of linking <code>exe1</code> is determined by the same <code>POSITION_INDEPENDENT_CODE</code> property, the dependency graph above contains a cycle. <code><a href="/docs/linux/man/1-cmake/">cmake</a>(1)</code> issues an error message.</p>
<h3>Output Artifacts</h3>
<p>The buildsystem targets created by the <code>add_library()</code> and <code>add_executable()</code> commands create rules to create binary outputs. The exact output location of the binaries can only be determined at generate-time because it can depend on the build-configuration and the link-language of linked dependencies etc. <code>TARGET_FILE</code>, <code>TARGET_LINKER_FILE</code> and related expressions can be used to access the name and location of generated binaries. These expressions do not work for <code>OBJECT</code> libraries however, as there is no single file generated by such libraries which is relevant to the expressions. </p>
<p> There are three kinds of output artifacts that may be build by targets as detailed in the following sections. Their classification differs between DLL platforms and non-DLL platforms. All Windows-based systems including Cygwin are DLL platforms.</p>
<h3>Runtime Output Artifacts</h3>
<p>A <i>runtime</i> output artifact of a buildsystem target may be:</p>
<dl>
<dt>&bull;</p>
<dd>The executable file (e.g. <code>.exe</code>) of an executable target created by the <code>add_executable()</code> command.</p>
<dt>&bull;</p>
<dd>On DLL platforms: the executable file (e.g. <code>.dll</code>) of a shared library target created by the <code>add_library()</code> command with the <code>SHARED</code> option. </p>
<p> The <code>RUNTIME_OUTPUT_DIRECTORY</code> and <code>RUNTIME_OUTPUT_NAME</code> target properties may be used to control runtime output artifact locations and names in the build tree.</dl>
<h3>Library Output Artifacts</h3>
<p>A <i>library</i> output artifact of a buildsystem target may be:</p>
<dl>
<dt>&bull;</p>
<dd>The loadable module file (e.g. <code>.dll</code> or <code>.so</code>) of a module library target created by the <code>add_library()</code> command with the <code>MODULE</code> option.</p>
<dt>&bull;</p>
<dd>On non-DLL platforms: the shared library file (e.g. <code>.so</code> or <code>.dylib</code>) of a shared library target created by the <code>add_library()</code> command with the <code>SHARED</code> option. </p>
<p> The <code>LIBRARY_OUTPUT_DIRECTORY</code> and <code>LIBRARY_OUTPUT_NAME</code> target properties may be used to control library output artifact locations and names in the build tree.</dl>
<h3>Archive Output Artifacts</h3>
<p>An <i>archive</i> output artifact of a buildsystem target may be:</p>
<dl>
<dt>&bull;</p>
<dd>The static library file (e.g. <code>.lib</code> or <code>.a</code>) of a static library target created by the <code>add_library()</code> command with the <code>STATIC</code> option.</p>
<dt>&bull;</p>
<dd>On DLL platforms: the import library file (e.g. <code>.lib</code>) of a shared library target created by the <code>add_library()</code> command with the <code>SHARED</code> option. This file is only guaranteed to exist if the library exports at least one unmanaged symbol.</p>
<dt>&bull;</p>
<dd>On DLL platforms: the import library file (e.g. <code>.lib</code>) of an executable target created by the <code>add_executable()</code> command when its <code>ENABLE_EXPORTS</code> target property is set.</p>
<dt>&bull;</p>
<dd>On AIX: the linker import file (e.g. <code>.imp</code>) of an executable target created by the <code>add_executable()</code> command when its <code>ENABLE_EXPORTS</code> target property is set. </p>
<p> The <code>ARCHIVE_OUTPUT_DIRECTORY</code> and <code>ARCHIVE_OUTPUT_NAME</code> target properties may be used to control archive output artifact locations and names in the build tree.</dl>
<h3>Directory-Scoped Commands</h3>
<p>The <code>target_include_directories()</code>, <code>target_compile_definitions()</code> and <code>target_compile_options()</code> commands have an effect on only one target at a time. The commands <code>add_compile_definitions()</code>, <code>add_compile_options()</code> and <code>include_directories()</code> have a similar function, but operate at directory scope instead of target scope for convenience.</p>
<h2>Build Configurations</h2>
<p>Configurations determine specifications for a certain type of build, such as <code>Release</code> or <code>Debug</code>. The way this is specified depends on the type of <code>generator</code> being used. For single configuration generators like Makefile Generators and <code>Ninja</code>, the configuration is specified at configure time by the <code>CMAKE_BUILD_TYPE</code> variable. For multi-configuration generators like Visual Studio, <code>Xcode</code>, and <code>Ninja Multi-Config</code>, the configuration is chosen by the user at build time and <code>CMAKE_BUILD_TYPE</code> is ignored. In the multi-configuration case, the set of <i>available</i> configurations is specified at configure time by the <code>CMAKE_CONFIGURATION_TYPES</code> variable, but the actual configuration used cannot be known until the build stage. This difference is often misunderstood, leading to problematic code like the following: </p>
<pre># WARNING: This is wrong for multi-config generators because they don't use
# and typically don't even set CMAKE_BUILD_TYPE
string(TOLOWER ${CMAKE_BUILD_TYPE} build_type)
if (build_type STREQUAL debug)
 target_compile_definitions(exe1 PRIVATE DEBUG_BUILD)
endif()</pre>
<p><code>Generator expressions</code> should be used instead to handle configuration-specific logic correctly, regardless of the generator used. For example: </p>
<pre># Works correctly for both single and multi-config generators
target_compile_definitions(exe1 PRIVATE
 $&lt;$&lt;CONFIG:Debug&gt;:DEBUG_BUILD&gt;
)</pre>
<p>In the presence of <code>IMPORTED</code> targets, the content of <code>MAP_IMPORTED_CONFIG_DEBUG</code> is also accounted for by the above <code>$&lt;CONFIG:Debug&gt;</code> expression.</p>
<h3>Case Sensitivity</h3>
<p><code>CMAKE_BUILD_TYPE</code> and <code>CMAKE_CONFIGURATION_TYPES</code> are just like other variables in that any string comparisons made with their values will be case-sensitive. The <code>$&lt;CONFIG&gt;</code> generator expression also preserves the casing of the configuration as set by the user or CMake defaults. For example: </p>
<pre># NOTE: Don't use these patterns, they are for illustration purposes only.
set(CMAKE_BUILD_TYPE Debug)
if(CMAKE_BUILD_TYPE STREQUAL DEBUG)
 # ... will never get here, &quot;Debug&quot; != &quot;DEBUG&quot;
endif()
add_custom_target(print_config ALL
 # Prints &quot;Config is Debug&quot; in this single-config case
 COMMAND ${CMAKE_COMMAND} -E echo &quot;Config is $&lt;CONFIG&gt;&quot;
 VERBATIM
)
set(CMAKE_CONFIGURATION_TYPES Debug Release)
if(DEBUG IN_LIST CMAKE_CONFIGURATION_TYPES)
 # ... will never get here, &quot;Debug&quot; != &quot;DEBUG&quot;
endif()</pre>
<p>In contrast, CMake treats the configuration type case-insensitively when using it internally in places that modify behavior based on the configuration. For example, the <code>$&lt;CONFIG:Debug&gt;</code> generator expression will evaluate to 1 for a configuration of not only <code>Debug</code>, but also <code>DEBUG</code>, <code>debug</code> or even <code>DeBuG</code>. Therefore, you can specify configuration types in <code>CMAKE_BUILD_TYPE</code> and <code>CMAKE_CONFIGURATION_TYPES</code> with any mixture of upper and lowercase, although there are strong conventions (see the next section). If you must test the value in string comparisons, always convert the value to upper or lowercase first and adjust the test accordingly.</p>
<h3>Default And Custom Configurations</h3>
<p>By default, CMake defines a number of standard configurations:</p>
<dl>
<dt>&bull;</p>
<dd><code>Debug</code></p>
<dt>&bull;</p>
<dd><code>Release</code></p>
<dt>&bull;</p>
<dd><code>RelWithDebInfo</code></p>
<dt>&bull;</p>
<dd><code>MinSizeRel</code> </p>
<p> In multi-config generators, the <code>CMAKE_CONFIGURATION_TYPES</code> variable will be populated with (potentially a subset of) the above list by default, unless overridden by the project or user. The actual configuration used is selected by the user at build time. </p>
<p> For single-config generators, the configuration is specified with the <code>CMAKE_BUILD_TYPE</code> variable at configure time and cannot be changed at build time. The default value will often be none of the above standard configurations and will instead be an empty string. A common misunderstanding is that this is the same as <code>Debug</code>, but that is not the case. Users should always explicitly specify the build type instead to avoid this common problem. </p>
<p> The above standard configuration types provide reasonable behavior on most platforms, but they can be extended to provide other types. Each configuration defines a set of compiler and linker flag variables for the language in use. These variables follow the convention <code>CMAKE_&lt;LANG&gt;_FLAGS_&lt;CONFIG&gt;</code>, where <code>&lt;CONFIG&gt;</code> is always the uppercase configuration name. When defining a custom configuration type, make sure these variables are set appropriately, typically as cache variables.</dl>
<h2>Pseudo Targets</h2>
<p>Some target types do not represent outputs of the buildsystem, but only inputs such as external dependencies, aliases or other non-build artifacts. Pseudo targets are not represented in the generated buildsystem.</p>
<h3>Imported Targets</h3>
<p>An <code>IMPORTED</code> target represents a pre-existing dependency. Usually such targets are defined by an upstream package and should be treated as immutable. After declaring an <code>IMPORTED</code> target one can adjust its target properties by using the customary commands such as <code>target_compile_definitions()</code>, <code>target_include_directories()</code>, <code>target_compile_options()</code> or <code>target_link_libraries()</code> just like with any other regular target. </p>
<p> <code>IMPORTED</code> targets may have the same usage requirement properties populated as binary targets, such as <code>INTERFACE_INCLUDE_DIRECTORIES</code>, <code>INTERFACE_COMPILE_DEFINITIONS</code>, <code>INTERFACE_COMPILE_OPTIONS</code>, <code>INTERFACE_LINK_LIBRARIES</code>, and <code>INTERFACE_POSITION_INDEPENDENT_CODE</code>. </p>
<p> The <code>LOCATION</code> may also be read from an IMPORTED target, though there is rarely reason to do so. Commands such as <code>add_custom_command()</code> can transparently use an <code>IMPORTED</code> <code>EXECUTABLE</code> target as a <code>COMMAND</code> executable. </p>
<p> The scope of the definition of an <code>IMPORTED</code> target is the directory where it was defined. It may be accessed and used from subdirectories, but not from parent directories or sibling directories. The scope is similar to the scope of a cmake variable. </p>
<p> It is also possible to define a <code>GLOBAL</code> <code>IMPORTED</code> target which is accessible globally in the buildsystem. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for more on creating packages with <code>IMPORTED</code> targets.</p>
<h3>Alias Targets</h3>
<p>An <code>ALIAS</code> target is a name which may be used interchangeably with a binary target name in read-only contexts. A primary use-case for <code>ALIAS</code> targets is for example or unit test executables accompanying a library, which may be part of the same buildsystem or built separately based on user configuration. </p>
<pre>add_library(lib1 lib1.cpp)
install(TARGETS lib1 EXPORT lib1Export ${dest_args})
install(EXPORT lib1Export NAMESPACE Upstream:: ${other_args})
add_library(Upstream::lib1 ALIAS lib1)</pre>
<p>In another directory, we can link unconditionally to the <code>Upstream::lib1</code> target, which may be an <code>IMPORTED</code> target from a package, or an <code>ALIAS</code> target if built as part of the same buildsystem. </p>
<pre>if (NOT TARGET Upstream::lib1)
 find_package(lib1 REQUIRED)
endif()
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 Upstream::lib1)</pre>
<p><code>ALIAS</code> targets are not mutable, installable or exportable. They are entirely local to the buildsystem description. A name can be tested for whether it is an <code>ALIAS</code> name by reading the <code>ALIASED_TARGET</code> property from it: </p>
<pre>get_target_property(_aliased Upstream::lib1 ALIASED_TARGET)
if(_aliased)
 message(STATUS &quot;The name Upstream::lib1 is an ALIAS for ${_aliased}.&quot;)
endif()</pre>
<h3>Interface Libraries</h3>
<p>An <code>INTERFACE</code> library target does not compile sources and does not produce a library artifact on disk, so it has no <code>LOCATION</code>. </p>
<p> It may specify usage requirements such as <code>INTERFACE_INCLUDE_DIRECTORIES</code>, <code>INTERFACE_COMPILE_DEFINITIONS</code>, <code>INTERFACE_COMPILE_OPTIONS</code>, <code>INTERFACE_LINK_LIBRARIES</code>, <code>INTERFACE_SOURCES</code>, and <code>INTERFACE_POSITION_INDEPENDENT_CODE</code>. Only the <code>INTERFACE</code> modes of the <code>target_include_directories()</code>, <code>target_compile_definitions()</code>, <code>target_compile_options()</code>, <code>target_sources()</code>, and <code>target_link_libraries()</code> commands may be used with <code>INTERFACE</code> libraries. </p>
<p> Since CMake 3.19, an <code>INTERFACE</code> library target may optionally contain source files. An interface library that contains source files will be included as a build target in the generated buildsystem. It does not compile sources, but may contain custom commands to generate other sources. Additionally, IDEs will show the source files as part of the target for interactive reading and editing. </p>
<p> A primary use-case for <code>INTERFACE</code> libraries is header-only libraries. </p>
<pre>add_library(Eigen INTERFACE
 src/eigen.h
 src/vector.h
 src/matrix.h
 )
target_include_directories(Eigen INTERFACE
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src&gt;
 $&lt;INSTALL_INTERFACE:include/Eigen&gt;
)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 Eigen)</pre>
<p>Here, the usage requirements from the <code>Eigen</code> target are consumed and used when compiling, but it has no effect on linking. </p>
<p> Another use-case is to employ an entirely target-focussed design for usage requirements: </p>
<pre>add_library(pic_on INTERFACE)
set_property(TARGET pic_on PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)
add_library(pic_off INTERFACE)
set_property(TARGET pic_off PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE OFF)
add_library(enable_rtti INTERFACE)
target_compile_options(enable_rtti INTERFACE
 $&lt;$&lt;OR:$&lt;COMPILER_ID:GNU&gt;,$&lt;COMPILER_ID:Clang&gt;&gt;:-rtti&gt;
)
add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 pic_on enable_rtti)</pre>
<p>This way, the build specification of <code>exe1</code> is expressed entirely as linked targets, and the complexity of compiler-specific flags is encapsulated in an <code>INTERFACE</code> library target. </p>
<p> <code>INTERFACE</code> libraries may be installed and exported. Any content they refer to must be installed separately: </p>
<pre>set(Eigen_headers
 src/eigen.h
 src/vector.h
 src/matrix.h
 )
add_library(Eigen INTERFACE ${Eigen_headers})
target_include_directories(Eigen INTERFACE
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src&gt;
 $&lt;INSTALL_INTERFACE:include/Eigen&gt;
)
install(TARGETS Eigen EXPORT eigenExport)
install(EXPORT eigenExport NAMESPACE Upstream::
 DESTINATION lib/cmake/Eigen
)
install(FILES ${Eigen_headers}
 DESTINATION include/Eigen
)</pre>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
