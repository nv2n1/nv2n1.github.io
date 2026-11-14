---
title: "cmake-developer(7)"
name: "cmake-developer"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake-developer/"
description: "cmake-developer – CMake Developer Reference"
---

<p>cmake-developer &#8211; CMake Developer Reference</p>
<h2>Introduction</h2>
<p>This manual is intended for reference by developers working with <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code> code, whether writing their own modules, authoring their own build systems, or working on CMake itself. </p>
<p> See <i><a rel="nofollow" href="https://cmake.org/get-involved/">https://cmake.org/get-involved/</a></i> to get involved in development of CMake upstream. It includes links to contribution instructions, which in turn link to developer guides for CMake itself.</p>
<h2>Find Modules</h2>
<p>A &quot;find module&quot; is a <code>Find&lt;PackageName&gt;.cmake</code> file to be loaded by the <code>find_package()</code> command when invoked for <code>&lt;PackageName&gt;</code>. </p>
<p> The primary task of a find module is to determine whether a package is available, set the <code>&lt;PackageName&gt;_FOUND</code> variable to reflect this and provide any variables, macros and imported targets required to use the package. A find module is useful in cases where an upstream library does not provide a config file package. </p>
<p> The traditional approach is to use variables for everything, including libraries and executables: see the <i>Standard Variable Names</i> section below. This is what most of the existing find modules provided by CMake do. </p>
<p> The more modern approach is to behave as much like config file packages files as possible, by providing imported target. This has the advantage of propagating Target Usage Requirements to consumers. </p>
<p> In either case (or even when providing both variables and imported targets), find modules should provide backwards compatibility with old versions that had the same name. </p>
<p> A FindFoo.cmake module will typically be loaded by the command: </p>
<pre>find_package(Foo [major[.minor[.patch[.tweak]]]]
 [EXACT] [QUIET] [REQUIRED]
 [[COMPONENTS] [components...]]
 [OPTIONAL_COMPONENTS components...]
 [NO_POLICY_SCOPE])</pre>
<p>See the <code>find_package()</code> documentation for details on what variables are set for the find module. Most of these are dealt with by using <code>FindPackageHandleStandardArgs</code>. </p>
<p> Briefly, the module should only locate versions of the package compatible with the requested version, as described by the <code>Foo_FIND_VERSION</code> family of variables. If <code>Foo_FIND_QUIETLY</code> is set to true, it should avoid printing messages, including anything complaining about the package not being found. If <code>Foo_FIND_REQUIRED</code> is set to true, the module should issue a <code>FATAL_ERROR</code> if the package cannot be found. If neither are set to true, it should print a non-fatal message if it cannot find the package. </p>
<p> Packages that find multiple semi-independent parts (like bundles of libraries) should search for the components listed in <code>Foo_FIND_COMPONENTS</code> if it is set , and only set <code>Foo_FOUND</code> to true if for each searched-for component <code>&lt;c&gt;</code> that was not found, <code>Foo_FIND_REQUIRED_&lt;c&gt;</code> is not set to true. The <code>HANDLE_COMPONENTS</code> argument of <code>find_package_handle_standard_args()</code> can be used to implement this. </p>
<p> If <code>Foo_FIND_COMPONENTS</code> is not set, which modules are searched for and required is up to the find module, but should be documented. </p>
<p> For internal implementation, it is a generally accepted convention that variables starting with underscore are for temporary use only.</p>
<h3>Standard Variable Names</h3>
<p>For a <code>FindXxx.cmake</code> module that takes the approach of setting variables (either instead of or in addition to creating imported targets), the following variable names should be used to keep things consistent between Find modules. Note that all variables start with <code>Xxx_</code>, which (unless otherwise noted) must match exactly the name of the <code>FindXxx.cmake</code> file, including upper/lowercase. This prefix on the variable names ensures that they do not conflict with variables of other Find modules. The same pattern should also be followed for any macros, functions and imported targets defined by the Find module.</p>
<dl>
<dt><code>Xxx_INCLUDE_DIRS</code></p>
<dd>The final set of include directories listed in one variable for use by client code. This should not be a cache entry (note that this also means this variable should not be used as the result variable of a <code>find_path()</code> command &#8211; see <code>Xxx_INCLUDE_DIR</code> below for that).</p>
<dt><code>Xxx_LIBRARIES</code></p>
<dd>The libraries to use with the module. These may be CMake targets, full absolute paths to a library binary or the name of a library that the linker must find in its search path. This should not be a cache entry (note that this also means this variable should not be used as the result variable of a <code>find_library()</code> command &#8211; see <code>Xxx_LIBRARY</code> below for that).</p>
<dt><code>Xxx_DEFINITIONS</code></p>
<dd>The compile definitions to use when compiling code that uses the module. This really shouldn&#8217;t include options such as <code>-DHAS_JPEG</code> that a client source-code file uses to decide whether to <code>#include &lt;jpeg.h&gt;</code></p>
<dt><code>Xxx_EXECUTABLE</code></p>
<dd>The full absolute path to an executable. In this case, <code>Xxx</code> might not be the name of the module, it might be the name of the tool (usually converted to all uppercase), assuming that tool has such a well-known name that it is unlikely that another tool with the same name exists. It would be appropriate to use this as the result variable of a <code>find_program()</code> command.</p>
<dt><code>Xxx_YYY_EXECUTABLE</code></p>
<dd>Similar to <code>Xxx_EXECUTABLE</code> except here the <code>Xxx</code> is always the module name and <code>YYY</code> is the tool name (again, usually fully uppercase). Prefer this form if the tool name is not very widely known or has the potential to clash with another tool. For greater consistency, also prefer this form if the module provides more than one executable.</p>
<dt><code>Xxx_LIBRARY_DIRS</code></p>
<dd>Optionally, the final set of library directories listed in one variable for use by client code. This should not be a cache entry.</p>
<dt><code>Xxx_ROOT_DIR</code></p>
<dd>Where to find the base directory of the module.</p>
<dt><code>Xxx_VERSION_VV</code></p>
<dd>Variables of this form specify whether the <code>Xxx</code> module being provided is version <code>VV</code> of the module. There should not be more than one variable of this form set to true for a given module. For example, a module <code>Barry</code> might have evolved over many years and gone through a number of different major versions. Version 3 of the <code>Barry</code> module might set the variable <code>Barry_VERSION_3</code> to true, whereas an older version of the module might set <code>Barry_VERSION_2</code> to true instead. It would be an error for both <code>Barry_VERSION_3</code> and <code>Barry_VERSION_2</code> to both be set to true.</p>
<dt><code>Xxx_WRAP_YY</code></p>
<dd>When a variable of this form is set to false, it indicates that the relevant wrapping command should not be used. The wrapping command depends on the module, it may be implied by the module name or it might be specified by the <code>YY</code> part of the variable.</p>
<dt><code>Xxx_Yy_FOUND</code></p>
<dd>For variables of this form, <code>Yy</code> is the name of a component for the module. It should match exactly one of the valid component names that may be passed to the <code>find_package()</code> command for the module. If a variable of this form is set to false, it means that the <code>Yy</code> component of module <code>Xxx</code> was not found or is not available. Variables of this form would typically be used for optional components so that the caller can check whether an optional component is available.</p>
<dt><code>Xxx_FOUND</code></p>
<dd>When the <code>find_package()</code> command returns to the caller, this variable will be set to true if the module was deemed to have been found successfully.</p>
<dt><code>Xxx_NOT_FOUND_MESSAGE</code></p>
<dd>Should be set by config-files in the case that it has set <code>Xxx_FOUND</code> to FALSE. The contained message will be printed by the <code>find_package()</code> command and by <code>find_package_handle_standard_args()</code> to inform the user about the problem. Use this instead of calling <code>message()</code> directly to report a reason for failing to find the module or package.</p>
<dt><code>Xxx_RUNTIME_LIBRARY_DIRS</code></p>
<dd>Optionally, the runtime library search path for use when running an executable linked to shared libraries. The list should be used by user code to create the <code>PATH</code> on windows or <code>LD_LIBRARY_PATH</code> on UNIX. This should not be a cache entry.</p>
<dt><code>Xxx_VERSION</code></p>
<dd>The full version string of the package found, if any. Note that many existing modules provide <code>Xxx_VERSION_STRING</code> instead.</p>
<dt><code>Xxx_VERSION_MAJOR</code></p>
<dd>The major version of the package found, if any.</p>
<dt><code>Xxx_VERSION_MINOR</code></p>
<dd>The minor version of the package found, if any.</p>
<dt><code>Xxx_VERSION_PATCH</code></p>
<dd>The patch version of the package found, if any. </p>
<p> The following names should not usually be used in <code>CMakeLists.txt</code> files. They are intended for use by Find modules to specify and cache the locations of specific files or directories. Users are typically able to set and edit these variables to control the behavior of Find modules (like entering the path to a library manually):</p>
<dt><code>Xxx_LIBRARY</code></p>
<dd>The path of the library. Use this form only when the module provides a single library. It is appropriate to use this as the result variable in a <code>find_library()</code> command.</p>
<dt><code>Xxx_Yy_LIBRARY</code></p>
<dd>The path of library <code>Yy</code> provided by the module <code>Xxx</code>. Use this form when the module provides more than one library or where other modules may also provide a library of the same name. It is also appropriate to use this form as the result variable in a <code>find_library()</code> command.</p>
<dt><code>Xxx_INCLUDE_DIR</code></p>
<dd>When the module provides only a single library, this variable can be used to specify where to find headers for using the library (or more accurately, the path that consumers of the library should add to their header search path). It would be appropriate to use this as the result variable in a <code>find_path()</code> command.</p>
<dt><code>Xxx_Yy_INCLUDE_DIR</code></p>
<dd>If the module provides more than one library or where other modules may also provide a library of the same name, this form is recommended for specifying where to find headers for using library <code>Yy</code> provided by the module. Again, it would be appropriate to use this as the result variable in a <code>find_path()</code> command. </p>
<p> To prevent users being overwhelmed with settings to configure, try to keep as many options as possible out of the cache, leaving at least one option which can be used to disable use of the module, or locate a not-found library (e.g. <code>Xxx_ROOT_DIR</code>). For the same reason, mark most cache options as advanced. For packages which provide both debug and release binaries, it is common to create cache variables with a <code>_LIBRARY_&lt;CONFIG&gt;</code> suffix, such as <code>Foo_LIBRARY_RELEASE</code> and <code>Foo_LIBRARY_DEBUG</code>. The <code>SelectLibraryConfigurations</code> module can be helpful for such cases. </p>
<p> While these are the standard variable names, you should provide backwards compatibility for any old names that were actually in use. Make sure you comment them as deprecated, so that no-one starts using them.</dl>
<h3>A Sample Find Module</h3>
<p>We will describe how to create a simple find module for a library <code>Foo</code>. </p>
<p> The top of the module should begin with a license notice, followed by a blank line, and then followed by a Bracket Comment. The comment should begin with <code>.rst:</code> to indicate that the rest of its content is reStructuredText-format documentation. For example: </p>
<pre># Distributed under the OSI-approved BSD 3-Clause License. See accompanying
# file Copyright.txt or <a rel="nofollow" href="https://cmake.org/licensing">https://cmake.org/licensing</a> for details.
#[=======================================================================[.rst:
FindFoo
-------
Finds the Foo library.
Imported Targets
^^^^^^^^^^^^^^^^
This module provides the following imported targets, if found:
``Foo::Foo``
 The Foo library
Result Variables
^^^^^^^^^^^^^^^^
This will define the following variables:
``Foo_FOUND``
 True if the system has the Foo library.
``Foo_VERSION``
 The version of the Foo library which was found.
``Foo_INCLUDE_DIRS``
 Include directories needed to use Foo.
``Foo_LIBRARIES``
 Libraries needed to link to Foo.
Cache Variables
^^^^^^^^^^^^^^^
The following cache variables may also be set:
``Foo_INCLUDE_DIR``
 The directory containing ``foo.h``.
``Foo_LIBRARY``
 The path to the Foo library.
#]=======================================================================]</pre>
<p>The module documentation consists of:</p>
<dl>
<dt>&bull;</p>
<dd>An underlined heading specifying the module name.</p>
<dt>&bull;</p>
<dd>A simple description of what the module finds. More description may be required for some packages. If there are caveats or other details users of the module should be aware of, specify them here.</p>
<dt>&bull;</p>
<dd>A section listing imported targets provided by the module, if any.</p>
<dt>&bull;</p>
<dd>A section listing result variables provided by the module.</p>
<dt>&bull;</p>
<dd>Optionally a section listing cache variables used by the module, if any. </p>
<p> If the package provides any macros or functions, they should be listed in an additional section, but can be documented by additional <code>.rst:</code> comment blocks immediately above where those macros or functions are defined. </p>
<p> The find module implementation may begin below the documentation block. Now the actual libraries and so on have to be found. The code here will obviously vary from module to module (dealing with that, after all, is the point of find modules), but there tends to be a common pattern for libraries. </p>
<p> First, we try to use <code>pkg-config</code> to find the library. Note that we cannot rely on this, as it may not be available, but it provides a good starting point. </p>
<pre>find_package(PkgConfig)
pkg_check_modules(PC_Foo QUIET Foo)</pre>
<p>This should define some variables starting <code>PC_Foo_</code> that contain the information from the <code>Foo.pc</code> file. </p>
<p> Now we need to find the libraries and include files; we use the information from <code>pkg-config</code> to provide hints to CMake about where to look. </p>
<pre>find_path(Foo_INCLUDE_DIR
 NAMES foo.h
 PATHS ${PC_Foo_INCLUDE_DIRS}
 PATH_SUFFIXES Foo
)
find_library(Foo_LIBRARY
 NAMES foo
 PATHS ${PC_Foo_LIBRARY_DIRS}
)</pre>
<p>Alternatively, if the library is available with multiple configurations, you can use <code>SelectLibraryConfigurations</code> to automatically set the <code>Foo_LIBRARY</code> variable instead: </p>
<pre>find_library(Foo_LIBRARY_RELEASE
 NAMES foo
 PATHS ${PC_Foo_LIBRARY_DIRS}/Release
)
find_library(Foo_LIBRARY_DEBUG
 NAMES foo
 PATHS ${PC_Foo_LIBRARY_DIRS}/Debug
)
include(SelectLibraryConfigurations)
select_library_configurations(Foo)</pre>
<p>If you have a good way of getting the version (from a header file, for example), you can use that information to set <code>Foo_VERSION</code> (although note that find modules have traditionally used <code>Foo_VERSION_STRING</code>, so you may want to set both). Otherwise, attempt to use the information from <code>pkg-config</code> </p>
<pre>set(Foo_VERSION ${PC_Foo_VERSION})</pre>
<p>Now we can use <code>FindPackageHandleStandardArgs</code> to do most of the rest of the work for us </p>
<pre>include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Foo
 FOUND_VAR Foo_FOUND
 REQUIRED_VARS
 Foo_LIBRARY
 Foo_INCLUDE_DIR
 VERSION_VAR Foo_VERSION
)</pre>
<p>This will check that the <code>REQUIRED_VARS</code> contain values (that do not end in <code>-NOTFOUND</code>) and set <code>Foo_FOUND</code> appropriately. It will also cache those values. If <code>Foo_VERSION</code> is set, and a required version was passed to <code>find_package()</code>, it will check the requested version against the one in <code>Foo_VERSION</code>. It will also print messages as appropriate; note that if the package was found, it will print the contents of the first required variable to indicate where it was found. </p>
<p> At this point, we have to provide a way for users of the find module to link to the library or libraries that were found. There are two approaches, as discussed in the <i>Find Modules</i> section above. The traditional variable approach looks like </p>
<pre>if(Foo_FOUND)
 set(Foo_LIBRARIES ${Foo_LIBRARY})
 set(Foo_INCLUDE_DIRS ${Foo_INCLUDE_DIR})
 set(Foo_DEFINITIONS ${PC_Foo_CFLAGS_OTHER})
endif()</pre>
<p>If more than one library was found, all of them should be included in these variables (see the <i>Standard Variable Names</i> section for more information). </p>
<p> When providing imported targets, these should be namespaced (hence the <code>Foo::</code> prefix); CMake will recognize that values passed to <code>target_link_libraries()</code> that contain <code>::</code> in their name are supposed to be imported targets (rather than just library names), and will produce appropriate diagnostic messages if that target does not exist (see policy <code>CMP0028</code>). </p>
<pre>if(Foo_FOUND AND NOT TARGET Foo::Foo)
 add_library(Foo::Foo UNKNOWN IMPORTED)
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION &quot;${Foo_LIBRARY}&quot;
 INTERFACE_COMPILE_OPTIONS &quot;${PC_Foo_CFLAGS_OTHER}&quot;
 INTERFACE_INCLUDE_DIRECTORIES &quot;${Foo_INCLUDE_DIR}&quot;
 )
endif()</pre>
<p>One thing to note about this is that the <code>INTERFACE_INCLUDE_DIRECTORIES</code> and similar properties should only contain information about the target itself, and not any of its dependencies. Instead, those dependencies should also be targets, and CMake should be told that they are dependencies of this target. CMake will then combine all the necessary information automatically. </p>
<p> The type of the <code>IMPORTED</code> target created in the <code>add_library()</code> command can always be specified as <code>UNKNOWN</code> type. This simplifies the code in cases where static or shared variants may be found, and CMake will determine the type by inspecting the files. </p>
<p> If the library is available with multiple configurations, the <code>IMPORTED_CONFIGURATIONS</code> target property should also be populated: </p>
<pre>if(Foo_FOUND)
 if (NOT TARGET Foo::Foo)
 add_library(Foo::Foo UNKNOWN IMPORTED)
 endif()
 if (Foo_LIBRARY_RELEASE)
 set_property(TARGET Foo::Foo APPEND PROPERTY
 IMPORTED_CONFIGURATIONS RELEASE
 )
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION_RELEASE &quot;${Foo_LIBRARY_RELEASE}&quot;
 )
 endif()
 if (Foo_LIBRARY_DEBUG)
 set_property(TARGET Foo::Foo APPEND PROPERTY
 IMPORTED_CONFIGURATIONS DEBUG
 )
 set_target_properties(Foo::Foo PROPERTIES
 IMPORTED_LOCATION_DEBUG &quot;${Foo_LIBRARY_DEBUG}&quot;
 )
 endif()
 set_target_properties(Foo::Foo PROPERTIES
 INTERFACE_COMPILE_OPTIONS &quot;${PC_Foo_CFLAGS_OTHER}&quot;
 INTERFACE_INCLUDE_DIRECTORIES &quot;${Foo_INCLUDE_DIR}&quot;
 )
endif()</pre>
<p>The <code>RELEASE</code> variant should be listed first in the property so that the variant is chosen if the user uses a configuration which is not an exact match for any listed <code>IMPORTED_CONFIGURATIONS</code>. </p>
<p> Most of the cache variables should be hidden in the <code>ccmake</code> interface unless the user explicitly asks to edit them. </p>
<pre>mark_as_advanced(
 Foo_INCLUDE_DIR
 Foo_LIBRARY
)</pre>
<p>If this module replaces an older version, you should set compatibility variables to cause the least disruption possible. </p>
<pre># compatibility variables
set(Foo_VERSION_STRING ${Foo_VERSION})</pre>
</dl>
<h2>Copyright</h2>
<p>2000-2022 Kitware, Inc. and Contributors</p>
