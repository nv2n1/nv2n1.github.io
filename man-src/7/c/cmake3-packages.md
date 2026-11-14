---
title: "cmake3-packages(7)"
name: "cmake3-packages"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-packages/"
description: "cmake-packages – CMake Packages Reference"
---

<p>cmake-packages &#8211; CMake Packages Reference</p>
<h2>Introduction</h2>
<p>Packages provide dependency information to CMake based buildsystems. Packages are found with the <code>find_package()</code> command. The result of using <code>find_package</code> is either a set of <code>IMPORTED</code> targets, or a set of variables corresponding to build-relevant information.</p>
<h2>Using Packages</h2>
<p>CMake provides direct support for two forms of packages, <i>Config-file Packages</i> and <i>Find-module Packages</i>. Indirect support for <code>pkg-config</code> packages is also provided via the <code>FindPkgConfig</code> module. In all cases, the basic form of <code>find_package()</code> calls is the same: </p>
<pre>find_package(Qt4 4.7.0 REQUIRED) # CMake provides a Qt4 find-module
find_package(Qt5Core 5.1.0 REQUIRED) # Qt provides a Qt5 package config file.
find_package(LibXml2 REQUIRED) # Use pkg-config via the LibXml2 find-module</pre>
<p>In cases where it is known that a package configuration file is provided by upstream, and only that should be used, the <code>CONFIG</code> keyword may be passed to <code>find_package()</code>: </p>
<pre>find_package(Qt5Core 5.1.0 CONFIG REQUIRED)
find_package(Qt5Gui 5.1.0 CONFIG)</pre>
<p>Similarly, the <code>MODULE</code> keyword says to use only a find-module: </p>
<pre>find_package(Qt4 4.7.0 MODULE REQUIRED)</pre>
<p>Specifying the type of package explicitly improves the error message shown to the user if it is not found. </p>
<p> Both types of packages also support specifying components of a package, either after the <code>REQUIRED</code> keyword: </p>
<pre>find_package(Qt5 5.1.0 CONFIG REQUIRED Widgets Xml Sql)</pre>
<p>or as a separate <code>COMPONENTS</code> list: </p>
<pre>find_package(Qt5 5.1.0 COMPONENTS Widgets Xml Sql)</pre>
<p>or as a separate <code>OPTIONAL_COMPONENTS</code> list: </p>
<pre>find_package(Qt5 5.1.0 COMPONENTS Widgets
 OPTIONAL_COMPONENTS Xml Sql
)</pre>
<p>Handling of <code>COMPONENTS</code> and <code>OPTIONAL_COMPONENTS</code> is defined by the package. </p>
<p> By setting the <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable to <code>TRUE</code>, the <code>PackageName</code> package will not be searched, and will always be <code>NOTFOUND</code>.</p>
<h3>Config-file Packages</h3>
<p>A config-file package is a set of files provided by upstreams for downstreams to use. CMake searches in a number of locations for package configuration files, as described in the <code>find_package()</code> documentation. The most simple way for a CMake user to tell <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> to search in a non-standard prefix for a package is to set the <code>CMAKE_PREFIX_PATH</code> cache variable. </p>
<p> Config-file packages are provided by upstream vendors as part of development packages, that is, they belong with the header files and any other files provided to assist downstreams in using the package. </p>
<p> A set of variables which provide package status information are also set automatically when using a config-file package. The <code>&lt;Package&gt;_FOUND</code> variable is set to true or false, depending on whether the package was found. The <code>&lt;Package&gt;_DIR</code> cache variable is set to the location of the package configuration file.</p>
<h3>Find-module Packages</h3>
<p>A find module is a file with a set of rules for finding the required pieces of a dependency, primarily header files and libraries. Typically, a find module is needed when the upstream is not built with CMake, or is not CMake-aware enough to otherwise provide a package configuration file. Unlike a package configuration file, it is not shipped with upstream, but is used by downstream to find the files by guessing locations of files with platform-specific hints. </p>
<p> Unlike the case of an upstream-provided package configuration file, no single point of reference identifies the package as being found, so the <code>&lt;Package&gt;_FOUND</code> variable is not automatically set by the <code>find_package()</code> command. It can still be expected to be set by convention however and should be set by the author of the Find-module. Similarly there is no <code>&lt;Package&gt;_DIR</code> variable, but each of the artifacts such as library locations and header file locations provide a separate cache variable. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-developer/">cmake3-developer</a>(7)</code> manual for more information about creating Find-module files.</p>
<h2>Package Layout</h2>
<p>A config-file package consists of a <i>Package Configuration File</i> and optionally a <i>Package Version File</i> provided with the project distribution.</p>
<h3>Package Configuration File</h3>
<p>Consider a project <code>Foo</code> that installs the following files: </p>
<pre>&lt;prefix&gt;/include/foo-1.2/foo.h
&lt;prefix&gt;/lib/foo-1.2/libfoo.a</pre>
<p>It may also provide a CMake package configuration file: </p>
<pre>&lt;prefix&gt;/lib/cmake/foo-1.2/FooConfig.cmake</pre>
<p>with content defining <code>IMPORTED</code> targets, or defining variables, such as: </p>
<pre># ...
# (compute PREFIX relative to file location)
# ...
set(Foo_INCLUDE_DIRS ${PREFIX}/include/foo-1.2)
set(Foo_LIBRARIES ${PREFIX}/lib/foo-1.2/libfoo.a)</pre>
<p>If another project wishes to use <code>Foo</code> it need only to locate the <code>FooConfig.cmake</code> file and load it to get all the information it needs about package content locations. Since the package configuration file is provided by the package installation it already knows all the file locations. </p>
<p> The <code>find_package()</code> command may be used to search for the package configuration file. This command constructs a set of installation prefixes and searches under each prefix in several locations. Given the name <code>Foo</code>, it looks for a file called <code>FooConfig.cmake</code> or <code>foo-config.cmake</code>. The full set of locations is specified in the <code>find_package()</code> command documentation. One place it looks is: </p>
<pre>&lt;prefix&gt;/lib/cmake/Foo*/</pre>
<p>where <code>Foo*</code> is a case-insensitive globbing expression. In our example the globbing expression will match <code>&lt;prefix&gt;/lib/cmake/foo-1.2</code> and the package configuration file will be found. </p>
<p> Once found, a package configuration file is immediately loaded. It, together with a package version file, contains all the information the project needs to use the package.</p>
<h3>Package Version File</h3>
<p>When the <code>find_package()</code> command finds a candidate package configuration file it looks next to it for a version file. The version file is loaded to test whether the package version is an acceptable match for the version requested. If the version file claims compatibility the configuration file is accepted. Otherwise it is ignored. </p>
<p> The name of the package version file must match that of the package configuration file but has either <code>-version</code> or <code>Version</code> appended to the name before the <code>.cmake</code> extension. For example, the files: </p>
<pre>&lt;prefix&gt;/lib/cmake/foo-1.3/foo-config.cmake
&lt;prefix&gt;/lib/cmake/foo-1.3/foo-config-version.cmake</pre>
<p>and: </p>
<pre>&lt;prefix&gt;/lib/cmake/bar-4.2/BarConfig.cmake
&lt;prefix&gt;/lib/cmake/bar-4.2/BarConfigVersion.cmake</pre>
<p>are each pairs of package configuration files and corresponding package version files. </p>
<p> When the <code>find_package()</code> command loads a version file it first sets the following variables:</p>
<dl>
<dt><code>PACKAGE_FIND_NAME</code></p>
<dd>The &lt;package&gt; name</p>
<dt><code>PACKAGE_FIND_VERSION</code></p>
<dd>Full requested version string</p>
<dt><code>PACKAGE_FIND_VERSION_MAJOR</code></p>
<dd>Major version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_MINOR</code></p>
<dd>Minor version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_PATCH</code></p>
<dd>Patch version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_TWEAK</code></p>
<dd>Tweak version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_COUNT</code></p>
<dd>Number of version components, 0 to 4 </p>
<p> The version file must use these variables to check whether it is compatible or an exact match for the requested version and set the following variables with results:</p>
<dt><code>PACKAGE_VERSION</code></p>
<dd>Full provided version string</p>
<dt><code>PACKAGE_VERSION_EXACT</code></p>
<dd>True if version is exact match</p>
<dt><code>PACKAGE_VERSION_COMPATIBLE</code></p>
<dd>True if version is compatible</p>
<dt><code>PACKAGE_VERSION_UNSUITABLE</code></p>
<dd>True if unsuitable as any version </p>
<p> Version files are loaded in a nested scope so they are free to set any variables they wish as part of their computation. The find_package command wipes out the scope when the version file has completed and it has checked the output variables. When the version file claims to be an acceptable match for the requested version the find_package command sets the following variables for use by the project:</p>
<dt><code>&lt;package&gt;_VERSION</code></p>
<dd>Full provided version string</p>
<dt><code>&lt;package&gt;_VERSION_MAJOR</code></p>
<dd>Major version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_MINOR</code></p>
<dd>Minor version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_PATCH</code></p>
<dd>Patch version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_TWEAK</code></p>
<dd>Tweak version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_COUNT</code></p>
<dd>Number of version components, 0 to 4 </p>
<p> The variables report the version of the package that was actually found. The <code>&lt;package&gt;</code> part of their name matches the argument given to the <code>find_package()</code> command.</dl>
<h2>Creating Packages</h2>
<p>Usually, the upstream depends on CMake itself and can use some CMake facilities for creating the package files. Consider an upstream which provides a single shared library: </p>
<pre>project(UpstreamLib)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE ON)
set(Upstream_VERSION 3.4.1)
include(GenerateExportHeader)
add_library(ClimbingStats SHARED climbingstats.cpp)
generate_export_header(ClimbingStats)
set_property(TARGET ClimbingStats PROPERTY VERSION ${Upstream_VERSION})
set_property(TARGET ClimbingStats PROPERTY SOVERSION 3)
set_property(TARGET ClimbingStats PROPERTY
 INTERFACE_ClimbingStats_MAJOR_VERSION 3)
set_property(TARGET ClimbingStats APPEND PROPERTY
 COMPATIBLE_INTERFACE_STRING ClimbingStats_MAJOR_VERSION
)
install(TARGETS ClimbingStats EXPORT ClimbingStatsTargets
 LIBRARY DESTINATION lib
 ARCHIVE DESTINATION lib
 RUNTIME DESTINATION bin
 INCLUDES DESTINATION include
)
install(
 FILES
 climbingstats.h
 &quot;${CMAKE_CURRENT_BINARY_DIR}/climbingstats_export.h&quot;
 DESTINATION
 include
 COMPONENT
 Devel
)
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
 &quot;${CMAKE_CURRENT_BINARY_DIR}/ClimbingStats/ClimbingStatsConfigVersion.cmake&quot;
 VERSION ${Upstream_VERSION}
 COMPATIBILITY AnyNewerVersion
)
export(EXPORT ClimbingStatsTargets
 FILE &quot;${CMAKE_CURRENT_BINARY_DIR}/ClimbingStats/ClimbingStatsTargets.cmake&quot;
 NAMESPACE Upstream::
)
configure_file(cmake/ClimbingStatsConfig.cmake
 &quot;${CMAKE_CURRENT_BINARY_DIR}/ClimbingStats/ClimbingStatsConfig.cmake&quot;
 COPYONLY
)
set(ConfigPackageLocation lib/cmake/ClimbingStats)
install(EXPORT ClimbingStatsTargets
 FILE
 ClimbingStatsTargets.cmake
 NAMESPACE
 Upstream::
 DESTINATION
 ${ConfigPackageLocation}
)
install(
 FILES
 cmake/ClimbingStatsConfig.cmake
 &quot;${CMAKE_CURRENT_BINARY_DIR}/ClimbingStats/ClimbingStatsConfigVersion.cmake&quot;
 DESTINATION
 ${ConfigPackageLocation}
 COMPONENT
 Devel
)</pre>
<p>The <code>CMakePackageConfigHelpers</code> module provides a macro for creating a simple <code>ConfigVersion.cmake</code> file. This file sets the version of the package. It is read by CMake when <code>find_package()</code> is called to determine the compatibility with the requested version, and to set some version-specific variables <code>&lt;Package&gt;_VERSION</code>, <code>&lt;Package&gt;_VERSION_MAJOR</code>, <code>&lt;Package&gt;_VERSION_MINOR</code> etc. The <code>install(EXPORT)</code> command is used to export the targets in the <code>ClimbingStatsTargets</code> export-set, defined previously by the <code>install(TARGETS)</code> command. This command generates the <code>ClimbingStatsTargets.cmake</code> file to contain <code>IMPORTED</code> targets, suitable for use by downstreams and arranges to install it to <code>lib/cmake/ClimbingStats</code>. The generated <code>ClimbingStatsConfigVersion.cmake</code> and a <code>cmake/ClimbingStatsConfig.cmake</code> are installed to the same location, completing the package. </p>
<p> The generated <code>IMPORTED</code> targets have appropriate properties set to define their <i>usage requirements</i>, such as <code>INTERFACE_INCLUDE_DIRECTORIES</code>, <code>INTERFACE_COMPILE_DEFINITIONS</code> and other relevant built-in <code>INTERFACE_</code> properties. The <code>INTERFACE</code> variant of user-defined properties listed in <code>COMPATIBLE_INTERFACE_STRING</code> and other <i>Compatible Interface Properties</i> are also propagated to the generated <code>IMPORTED</code> targets. In the above case, <code>ClimbingStats_MAJOR_VERSION</code> is defined as a string which must be compatible among the dependencies of any depender. By setting this custom defined user property in this version and in the next version of <code>ClimbingStats</code>, <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> will issue a diagnostic if there is an attempt to use version 3 together with version 4. Packages can choose to employ such a pattern if different major versions of the package are designed to be incompatible. </p>
<p> A <code>NAMESPACE</code> with double-colons is specified when exporting the targets for installation. This convention of double-colons gives CMake a hint that the name is an <code>IMPORTED</code> target when it is used by downstreams with the <code>target_link_libraries()</code> command. This way, CMake can issue a diagnostic if the package providing it has not yet been found. </p>
<p> In this case, when using <code>install(TARGETS)</code> the <code>INCLUDES DESTINATION</code> was specified. This causes the <code>IMPORTED</code> targets to have their <code>INTERFACE_INCLUDE_DIRECTORIES</code> populated with the <code>include</code> directory in the <code>CMAKE_INSTALL_PREFIX</code>. When the <code>IMPORTED</code> target is used by downstream, it automatically consumes the entries from that property.</p>
<h3>Creating a Package Configuration File</h3>
<p>In this case, the <code>ClimbingStatsConfig.cmake</code> file could be as simple as: </p>
<pre>include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStatsTargets.cmake&quot;)</pre>
<p>As this allows downstreams to use the <code>IMPORTED</code> targets. If any macros should be provided by the <code>ClimbingStats</code> package, they should be in a separate file which is installed to the same location as the <code>ClimbingStatsConfig.cmake</code> file, and included from there. </p>
<p> This can also be extended to cover dependencies: </p>
<pre># ...
add_library(ClimbingStats SHARED climbingstats.cpp)
generate_export_header(ClimbingStats)
find_package(Stats 2.6.4 REQUIRED)
target_link_libraries(ClimbingStats PUBLIC Stats::Types)</pre>
<p>As the <code>Stats::Types</code> target is a <code>PUBLIC</code> dependency of <code>ClimbingStats</code>, downstreams must also find the <code>Stats</code> package and link to the <code>Stats::Types</code> library. The <code>Stats</code> package should be found in the <code>ClimbingStatsConfig.cmake</code> file to ensure this. The <code>find_dependency</code> macro from the <code>CMakeFindDependencyMacro</code> helps with this by propagating whether the package is <code>REQUIRED</code>, or <code>QUIET</code> etc. All <code>REQUIRED</code> dependencies of a package should be found in the <code>Config.cmake</code> file: </p>
<pre>include(CMakeFindDependencyMacro)
find_dependency(Stats 2.6.4)
include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStatsTargets.cmake&quot;)
include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStatsMacros.cmake&quot;)</pre>
<p>The <code>find_dependency</code> macro also sets <code>ClimbingStats_FOUND</code> to <code>False</code> if the dependency is not found, along with a diagnostic that the <code>ClimbingStats</code> package can not be used without the <code>Stats</code> package. </p>
<p> If <code>COMPONENTS</code> are specified when the downstream uses <code>find_package()</code>, they are listed in the <code>&lt;Package&gt;_FIND_COMPONENTS</code> variable. If a particular component is non-optional, then the <code>&lt;Package&gt;_FIND_REQUIRED_&lt;comp&gt;</code> will be true. This can be tested with logic in the package configuration file: </p>
<pre>include(CMakeFindDependencyMacro)
find_dependency(Stats 2.6.4)
include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStatsTargets.cmake&quot;)
include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStatsMacros.cmake&quot;)
set(_supported_components Plot Table)
foreach(_comp ${ClimbingStats_FIND_COMPONENTS})
 if (NOT &quot;;${_supported_components};&quot; MATCHES _comp)
 set(ClimbingStats_FOUND False)
 set(ClimbingStats_NOTFOUND_MESSAGE &quot;Unsupported component: ${_comp}&quot;)
 endif()
 include(&quot;${CMAKE_CURRENT_LIST_DIR}/ClimbingStats${_comp}Targets.cmake&quot;)
endforeach()</pre>
<p>Here, the <code>ClimbingStats_NOTFOUND_MESSAGE</code> is set to a diagnosis that the package could not be found because an invalid component was specified. This message variable can be set for any case where the <code>_FOUND</code> variable is set to <code>False</code>, and will be displayed to the user.</p>
<h3>Creating a Package Configuration File for the Build Tree</h3>
<p>The <code>export(EXPORT)</code> command creates an <code>IMPORTED</code> targets definition file which is specific to the build-tree, and is not relocatable. This can similarly be used with a suitable package configuration file and package version file to define a package for the build tree which may be used without installation. Consumers of the build tree can simply ensure that the <code>CMAKE_PREFIX_PATH</code> contains the build directory, or set the <code>ClimbingStats_DIR</code> to <code>&lt;build_dir&gt;/ClimbingStats</code> in the cache.</p>
<h3>Creating Relocatable Packages</h3>
<p>A relocatable package must not reference absolute paths of files on the machine where the package is built that will not exist on the machines where the package may be installed. </p>
<p> Packages created by <code>install(EXPORT)</code> are designed to be relocatable, using paths relative to the location of the package itself. When defining the interface of a target for <code>EXPORT</code>, keep in mind that the include directories should be specified as relative paths which are relative to the <code>CMAKE_INSTALL_PREFIX</code>: </p>
<pre>target_include_directories(tgt INTERFACE
 # Wrong, not relocatable:
 $&lt;INSTALL_INTERFACE:${CMAKE_INSTALL_PREFIX}/include/TgtName&gt;
)
target_include_directories(tgt INTERFACE
 # Ok, relocatable:
 $&lt;INSTALL_INTERFACE:include/TgtName&gt;
)</pre>
<p>The <code>$&lt;INSTALL_PREFIX&gt;</code> <code>generator expression</code> may be used as a placeholder for the install prefix without resulting in a non-relocatable package. This is necessary if complex generator expressions are used: </p>
<pre>target_include_directories(tgt INTERFACE
 # Ok, relocatable:
 $&lt;INSTALL_INTERFACE:$&lt;$&lt;CONFIG:Debug&gt;:$&lt;INSTALL_PREFIX&gt;/include/TgtName&gt;&gt;
)</pre>
<p>This also applies to paths referencing external dependencies. It is not advisable to populate any properties which may contain paths, such as <code>INTERFACE_INCLUDE_DIRECTORIES</code> and <code>INTERFACE_LINK_LIBRARIES</code>, with paths relevant to dependencies. For example, this code may not work well for a relocatable package: </p>
<pre>target_link_libraries(ClimbingStats INTERFACE
 ${Foo_LIBRARIES} ${Bar_LIBRARIES}
 )
target_include_directories(ClimbingStats INTERFACE
 &quot;$&lt;INSTALL_INTERFACE:${Foo_INCLUDE_DIRS};${Bar_INCLUDE_DIRS}&gt;&quot;
 )</pre>
<p>The referenced variables may contain the absolute paths to libraries and include directories <code>as found on the machine the package was made on</code>. This would create a package with hard-coded paths to dependencies and not suitable for relocation. </p>
<p> Ideally such dependencies should be used through their own <i>IMPORTED targets</i> that have their own <code>IMPORTED_LOCATION</code> and usage requirement properties such as <code>INTERFACE_INCLUDE_DIRECTORIES</code> populated appropriately. Those imported targets may then be used with the <code>target_link_libraries()</code> command for <code>ClimbingStats</code>: </p>
<pre>target_link_libraries(ClimbingStats INTERFACE Foo::Foo Bar::Bar)</pre>
<p>With this approach the package references its external dependencies only through the names of <i>IMPORTED targets</i>. When a consumer uses the installed package, the consumer will run the appropriate <code>find_package()</code> commands (via the <code>find_dependency</code> macro described above) to find the dependencies and populate the imported targets with appropriate paths on their own machine. </p>
<p> Unfortunately many <code>modules</code> shipped with CMake do not yet provide <i>IMPORTED targets</i> because their development pre-dated this approach. This may improve incrementally over time. Workarounds to create relocatable packages using such modules include:</p>
<dl>
<dt>&bull;</p>
<dd>When building the package, specify each <code>Foo_LIBRARY</code> cache entry as just a library name, e.g. <code>-DFoo_LIBRARY=foo</code>. This tells the corresponding find module to populate the <code>Foo_LIBRARIES</code> with just <code>foo</code> to ask the linker to search for the library instead of hard-coding a path.</p>
<dt>&bull;</p>
<dd>Or, after installing the package content but before creating the package installation binary for redistribution, manually replace the absolute paths with placeholders for substitution by the installation tool when the package is installed.</dl>
<h2>Package Registry</h2>
<p>CMake provides two central locations to register packages that have been built or installed anywhere on a system:</p>
<dl>
<dt>&bull;</p>
<dd><i>User Package Registry</i></p>
<dt>&bull;</p>
<dd><i>System Package Registry</i> </p>
<p> The registries are especially useful to help projects find packages in non-standard install locations or directly in their own build trees. A project may populate either the user or system registry (using its own means, see below) to refer to its location. In either case the package should store at the registered location a <i>Package Configuration File</i> (<code>&lt;package&gt;Config.cmake</code>) and optionally a <i>Package Version File</i> (<code>&lt;package&gt;ConfigVersion.cmake</code>). </p>
<p> The <code>find_package()</code> command searches the two package registries as two of the search steps specified in its documentation. If it has sufficient permissions it also removes stale package registry entries that refer to directories that do not exist or do not contain a matching package configuration file.</dl>
<h3>User Package Registry</h3>
<p>The User Package Registry is stored in a per-user location. The <code>export(PACKAGE)</code> command may be used to register a project build tree in the user package registry. CMake currently provides no interface to add install trees to the user package registry. Installers must be manually taught to register their packages if desired. </p>
<p> On Windows the user package registry is stored in the Windows registry under a key in <code>HKEY_CURRENT_USER</code>. </p>
<p> A <code>&lt;package&gt;</code> may appear under registry key: </p>
<pre>HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\&lt;package&gt;</pre>
<p>as a <code>REG_SZ</code> value, with arbitrary name, that specifies the directory containing the package configuration file. </p>
<p> On UNIX platforms the user package registry is stored in the user home directory under <code>~/.cmake/packages</code>. A <code>&lt;package&gt;</code> may appear under the directory: </p>
<pre>~/.cmake/packages/&lt;package&gt;</pre>
<p>as a file, with arbitrary name, whose content specifies the directory containing the package configuration file.</p>
<h3>System Package Registry</h3>
<p>The System Package Registry is stored in a system-wide location. CMake currently provides no interface to add to the system package registry. Installers must be manually taught to register their packages if desired. </p>
<p> On Windows the system package registry is stored in the Windows registry under a key in <code>HKEY_LOCAL_MACHINE</code>. A <code>&lt;package&gt;</code> may appear under registry key: </p>
<pre>HKEY_LOCAL_MACHINE\Software\Kitware\CMake\Packages\&lt;package&gt;</pre>
<p>as a <code>REG_SZ</code> value, with arbitrary name, that specifies the directory containing the package configuration file. </p>
<p> There is no system package registry on non-Windows platforms.</p>
<h3>Disabling the Package Registry</h3>
<p>In some cases using the Package Registries is not desirable. CMake allows one to disable them using the following variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> disables the <code>export(PACKAGE)</code> command.</p>
<dt>&bull;</p>
<dd><code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> disables the User Package Registry in all the <code>find_package()</code> calls.</p>
<dt>&bull;</p>
<dd><code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> disables the System Package Registry in all the <code>find_package()</code> calls.</dl>
<h3>Package Registry Example</h3>
<p>A simple convention for naming package registry entries is to use content hashes. They are deterministic and unlikely to collide (<code>export(PACKAGE)</code> uses this approach). The name of an entry referencing a specific directory is simply the content hash of the directory path itself. </p>
<p> If a project arranges for package registry entries to exist, such as: </p>
<pre>&gt; reg query HKCU\Software\Kitware\CMake\Packages\MyPackage
HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\MyPackage
 45e7d55f13b87179bb12f907c8de6fc4 REG_SZ c:/Users/Me/Work/lib/cmake/MyPackage
 7b4a9844f681c80ce93190d4e3185db9 REG_SZ c:/Users/Me/Work/MyPackage-build</pre>
<p>or: </p>
<pre>$ cat ~/.cmake/packages/MyPackage/7d1fb77e07ce59a81bed093bbee945bd
/home/me/work/lib/cmake/MyPackage
$ cat ~/.cmake/packages/MyPackage/f92c1db873a1937f3100706657c63e07
/home/me/work/MyPackage-build</pre>
<p>then the <code>CMakeLists.txt</code> code: </p>
<pre>find_package(MyPackage)</pre>
<p>will search the registered locations for package configuration files (<code>MyPackageConfig.cmake</code>). The search order among package registry entries for a single package is unspecified and the entry names (hashes in this example) have no meaning. Registered locations may contain package version files (<code>MyPackageConfigVersion.cmake</code>) to tell <code>find_package()</code> whether a specific location is suitable for the version requested.</p>
<h3>Package Registry Ownership</h3>
<p>Package registry entries are individually owned by the project installations that they reference. A package installer is responsible for adding its own entry and the corresponding uninstaller is responsible for removing it. </p>
<p> The <code>export(PACKAGE)</code> command populates the user package registry with the location of a project build tree. Build trees tend to be deleted by developers and have no &quot;uninstall&quot; event that could trigger removal of their entries. In order to keep the registries clean the <code>find_package()</code> command automatically removes stale entries it encounters if it has sufficient permissions. CMake provides no interface to remove an entry referencing an existing build tree once <code>export(PACKAGE)</code> has been invoked. However, if the project removes its package configuration file from the build tree then the entry referencing the location will be considered stale.</p>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
