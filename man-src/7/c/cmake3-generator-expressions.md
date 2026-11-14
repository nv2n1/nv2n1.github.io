---
title: "cmake3-generator-expressions(7)"
name: "cmake3-generator-expressions"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-generator-expressions/"
description: "cmake-generator-expressions – CMake Generator Expressions"
---

<p>cmake-generator-expressions &#8211; CMake Generator Expressions</p>
<h2>Introduction</h2>
<p>Generator expressions are evaluated during build system generation to produce information specific to each build configuration. </p>
<p> Generator expressions are allowed in the context of many target properties, such as <code>LINK_LIBRARIES</code>, <code>INCLUDE_DIRECTORIES</code>, <code>COMPILE_DEFINITIONS</code> and others. They may also be used when using commands to populate those properties, such as <code>target_link_libraries()</code>, <code>target_include_directories()</code>, <code>target_compile_definitions()</code> and others. </p>
<p> This means that they enable conditional linking, conditional definitions used when compiling, and conditional include directories and more. The conditions may be based on the build configuration, target properties, platform information or any other queryable information.</p>
<h2>Logical Expressions</h2>
<p>Logical expressions are used to create conditional output. The basic expressions are the <code>0</code> and <code>1</code> expressions. Because other logical expressions evaluate to either <code>0</code> or <code>1</code>, they can be composed to create conditional output: </p>
<pre>$&lt;$&lt;CONFIG:Debug&gt;:DEBUG_MODE&gt;</pre>
<p>expands to <code>DEBUG_MODE</code> when the <code>Debug</code> configuration is used, and otherwise expands to nothing. </p>
<p> Available logical expressions are:</p>
<dl>
<dt><code>$&lt;BOOL:&#8230;&gt;</code></p>
<dd><code>1</code> if the <code>&#8230;</code> is true, else <code>0</code></p>
<dt><code>$&lt;AND:?[,?]&#8230;&gt;</code></p>
<dd><code>1</code> if all <code>?</code> are <code>1</code>, else <code>0</code> </p>
<p> The <code>?</code> must always be either <code>0</code> or <code>1</code> in boolean expressions.</p>
<dt><code>$&lt;OR:?[,?]&#8230;&gt;</code></p>
<dd><code>0</code> if all <code>?</code> are <code>0</code>, else <code>1</code></p>
<dt><code>$&lt;NOT:?&gt;</code></p>
<dd><code>0</code> if <code>?</code> is <code>1</code>, else <code>1</code></p>
<dt><code>$&lt;STREQUAL:a,b&gt;</code></p>
<dd><code>1</code> if <code>a</code> is STREQUAL <code>b</code>, else <code>0</code></p>
<dt><code>$&lt;EQUAL:a,b&gt;</code></p>
<dd><code>1</code> if <code>a</code> is EQUAL <code>b</code> in a numeric comparison, else <code>0</code></p>
<dt><code>$&lt;CONFIG:cfg&gt;</code></p>
<dd><code>1</code> if config is <code>cfg</code>, else <code>0</code>. This is a case-insensitive comparison. The mapping in <code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code> is also considered by this expression when it is evaluated on a property on an <code>IMPORTED</code> target.</p>
<dt><code>$&lt;PLATFORM_ID:comp&gt;</code></p>
<dd><code>1</code> if the CMake-id of the platform matches <code>comp</code>, otherwise <code>0</code>.</p>
<dt><code>$&lt;C_COMPILER_ID:comp&gt;</code></p>
<dd><code>1</code> if the CMake-id of the C compiler matches <code>comp</code>, otherwise <code>0</code>.</p>
<dt><code>$&lt;CXX_COMPILER_ID:comp&gt;</code></p>
<dd><code>1</code> if the CMake-id of the CXX compiler matches <code>comp</code>, otherwise <code>0</code>.</p>
<dt><code>$&lt;VERSION_GREATER:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is a version greater than <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_LESS:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is a version less than <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;VERSION_EQUAL:v1,v2&gt;</code></p>
<dd><code>1</code> if <code>v1</code> is the same version as <code>v2</code>, else <code>0</code>.</p>
<dt><code>$&lt;C_COMPILER_VERSION:ver&gt;</code></p>
<dd><code>1</code> if the version of the C compiler matches <code>ver</code>, otherwise <code>0</code>.</p>
<dt><code>$&lt;CXX_COMPILER_VERSION:ver&gt;</code></p>
<dd><code>1</code> if the version of the CXX compiler matches <code>ver</code>, otherwise <code>0</code>.</p>
<dt><code>$&lt;TARGET_POLICY:pol&gt;</code></p>
<dd><code>1</code> if the policy <code>pol</code> was NEW when the &#8216;head&#8217; target was created, else <code>0</code>. If the policy was not set, the warning message for the policy will be emitted. This generator expression only works for a subset of policies.</p>
<dt><code>$&lt;COMPILE_FEATURES:feature[,feature]&#8230;&gt;</code></p>
<dd><code>1</code> if all of the <code>feature</code> features are available for the &#8216;head&#8217; target, and <code>0</code> otherwise. If this expression is used while evaluating the link implementation of a target and if any dependency transitively increases the required <code>C_STANDARD</code> or <code>CXX_STANDARD</code> for the &#8216;head&#8217; target, an error is reported. See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<dt><code>$&lt;COMPILE_LANGUAGE:lang&gt;</code></p>
<dd><code>1</code> when the language used for compilation unit matches <code>lang</code>, otherwise <code>0</code>. This expression used to specify compile options for source files of a particular language in a target. For example, to specify the use of the <code>-fno-exceptions</code> compile option (compiler id checks elided): </p>
<pre>add_executable(myapp main.cpp foo.c bar.cpp)
target_compile_options(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:-fno-exceptions&gt;
)</pre>
<p>This generator expression has limited use because it is not possible to use it with the Visual Studio generators. Portable buildsystems would not use this expression, and would create separate libraries for each source file language instead: </p>
<pre>add_library(myapp_c foo.c)
add_library(myapp_cxx foo.c)
target_compile_options(myapp_cxx PUBLIC -fno-exceptions)
add_executable(myapp main.cpp)
target_link_libraries(myapp myapp_c myapp_cxx)</pre>
<p>The <code>Makefile</code> and <code>Ninja</code> based generators can also use this expression to specify compile-language specific compile definitions and include directories: </p>
<pre>add_executable(myapp main.cpp foo.c bar.cpp)
target_compile_definitions(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:COMPILING_CXX&gt;
)
target_include_directories(myapp
 PRIVATE $&lt;$&lt;COMPILE_LANGUAGE:CXX&gt;:/opt/foo/cxx_headers&gt;
)</pre>
</dl>
<h2>Informational Expressions</h2>
<p>These expressions expand to some information. The information may be used directly, eg: </p>
<pre>include_directories(/usr/include/$&lt;CXX_COMPILER_ID&gt;/)</pre>
<p>expands to <code>/usr/include/GNU/</code> or <code>/usr/include/Clang/</code> etc, depending on the Id of the compiler. </p>
<p> These expressions may also may be combined with logical expressions: </p>
<pre>$&lt;$&lt;VERSION_LESS:$&lt;CXX_COMPILER_VERSION&gt;,4.2.0&gt;:OLD_COMPILER&gt;</pre>
<p>expands to <code>OLD_COMPILER</code> if the <code>CMAKE_CXX_COMPILER_VERSION</code> is less than 4.2.0. </p>
<p> Available informational expressions are:</p>
<dl>
<dt><code>$&lt;CONFIGURATION&gt;</code></p>
<dd>Configuration name. Deprecated. Use <code>CONFIG</code> instead.</p>
<dt><code>$&lt;CONFIG&gt;</code></p>
<dd>Configuration name</p>
<dt><code>$&lt;PLATFORM_ID&gt;</code></p>
<dd>The CMake-id of the platform. See also the <code>CMAKE_SYSTEM_NAME</code> variable.</p>
<dt><code>$&lt;C_COMPILER_ID&gt;</code></p>
<dd>The CMake-id of the C compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_ID&gt;</code></p>
<dd>The CMake-id of the CXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code> variable.</p>
<dt><code>$&lt;C_COMPILER_VERSION&gt;</code></p>
<dd>The version of the C compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;CXX_COMPILER_VERSION&gt;</code></p>
<dd>The version of the CXX compiler used. See also the <code>CMAKE_&lt;LANG&gt;_COMPILER_VERSION</code> variable.</p>
<dt><code>$&lt;TARGET_FILE:tgt&gt;</code></p>
<dd>Full path to main file (.exe, .so.1.2, .a) where <code>tgt</code> is the name of a target.</p>
<dt><code>$&lt;TARGET_FILE_NAME:tgt&gt;</code></p>
<dd>Name of main file (.exe, .so.1.2, .a).</p>
<dt><code>$&lt;TARGET_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of main file (.exe, .so.1.2, .a).</p>
<dt><code>$&lt;TARGET_LINKER_FILE:tgt&gt;</code></p>
<dd>File used to link (.a, .lib, .so) where <code>tgt</code> is the name of a target.</p>
<dt><code>$&lt;TARGET_LINKER_FILE_NAME:tgt&gt;</code></p>
<dd>Name of file used to link (.a, .lib, .so).</p>
<dt><code>$&lt;TARGET_LINKER_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of file used to link (.a, .lib, .so).</p>
<dt><code>$&lt;TARGET_SONAME_FILE:tgt&gt;</code></p>
<dd>File with soname (.so.3) where <code>tgt</code> is the name of a target.</p>
<dt><code>$&lt;TARGET_SONAME_FILE_NAME:tgt&gt;</code></p>
<dd>Name of file with soname (.so.3).</p>
<dt><code>$&lt;TARGET_SONAME_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of with soname (.so.3).</p>
<dt><code>$&lt;TARGET_PDB_FILE:tgt&gt;</code></p>
<dd>Full path to the linker generated program database file (.pdb) where <code>tgt</code> is the name of a target. </p>
<p> See also the <code>PDB_NAME</code> and <code>PDB_OUTPUT_DIRECTORY</code> target properties and their configuration specific variants <code>PDB_NAME_&lt;CONFIG&gt;</code> and <code>PDB_OUTPUT_DIRECTORY_&lt;CONFIG&gt;</code>.</p>
<dt><code>$&lt;TARGET_PDB_FILE_NAME:tgt&gt;</code></p>
<dd>Name of the linker generated program database file (.pdb).</p>
<dt><code>$&lt;TARGET_PDB_FILE_DIR:tgt&gt;</code></p>
<dd>Directory of the linker generated program database file (.pdb).</p>
<dt><code>$&lt;TARGET_PROPERTY:tgt,prop&gt;</code></p>
<dd>Value of the property <code>prop</code> on the target <code>tgt</code>. </p>
<p> Note that <code>tgt</code> is not added as a dependency of the target this expression is evaluated on.</p>
<dt><code>$&lt;TARGET_PROPERTY:prop&gt;</code></p>
<dd>Value of the property <code>prop</code> on the target on which the generator expression is evaluated.</p>
<dt><code>$&lt;INSTALL_PREFIX&gt;</code></p>
<dd>Content of the install prefix when the target is exported via <code>install(EXPORT)</code> and empty otherwise.</p>
<dt><code>$&lt;COMPILE_LANGUAGE&gt;</code></p>
<dd>The compile language of source files when evaluating compile options. See the unary version for notes about portability of this generator expression.</dl>
<h2>Output Expressions</h2>
<p>These expressions generate output, in some cases depending on an input. These expressions may be combined with other expressions for information or logical comparison: </p>
<pre>-I$&lt;JOIN:$&lt;TARGET_PROPERTY:INCLUDE_DIRECTORIES&gt;, -I&gt;</pre>
<p>generates a string of the entries in the <code>INCLUDE_DIRECTORIES</code> target property with each entry preceded by <code>-I</code>. Note that a more-complete use in this situation would require first checking if the INCLUDE_DIRECTORIES property is non-empty: </p>
<pre>$&lt;$&lt;BOOL:${prop}&gt;:-I$&lt;JOIN:${prop}, -I&gt;&gt;</pre>
<p>where <code>${prop}</code> refers to a helper variable: </p>
<pre>set(prop &quot;$&lt;TARGET_PROPERTY:INCLUDE_DIRECTORIES&gt;&quot;)</pre>
<p>Available output expressions are:</p>
<dl>
<dt><code>$&lt;0:&#8230;&gt;</code></p>
<dd>Empty string (ignores <code>&#8230;</code>)</p>
<dt><code>$&lt;1:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code></p>
<dt><code>$&lt;JOIN:list,&#8230;&gt;</code></p>
<dd>Joins the list with the content of <code>&#8230;</code></p>
<dt><code>$&lt;ANGLE-R&gt;</code></p>
<dd>A literal <code>&gt;</code>. Used to compare strings which contain a <code>&gt;</code> for example.</p>
<dt><code>$&lt;COMMA&gt;</code></p>
<dd>A literal <code>,</code>. Used to compare strings which contain a <code>,</code> for example.</p>
<dt><code>$&lt;SEMICOLON&gt;</code></p>
<dd>A literal <code>;</code>. Used to prevent list expansion on an argument with <code>;</code>.</p>
<dt><code>$&lt;TARGET_NAME:&#8230;&gt;</code></p>
<dd>Marks <code>&#8230;</code> as being the name of a target. This is required if exporting targets to multiple dependent export sets. The <code>&#8230;</code> must be a literal name of a target- it may not contain generator expressions.</p>
<dt><code>$&lt;LINK_ONLY:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> except when evaluated in a link interface while propagating <i>Target Usage Requirements</i>, in which case it is the empty string. Intended for use only in an <code>INTERFACE_LINK_LIBRARIES</code> target property, perhaps via the <code>target_link_libraries()</code> command, to specify private link dependencies without other usage requirements.</p>
<dt><code>$&lt;INSTALL_INTERFACE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> when the property is exported using <code>install(EXPORT)</code>, and empty otherwise.</p>
<dt><code>$&lt;BUILD_INTERFACE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> when the property is exported using <code>export()</code>, or when the target is used by another target in the same buildsystem. Expands to the empty string otherwise.</p>
<dt><code>$&lt;LOWER_CASE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> converted to lower case.</p>
<dt><code>$&lt;UPPER_CASE:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> converted to upper case.</p>
<dt><code>$&lt;MAKE_C_IDENTIFIER:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> converted to a C identifier.</p>
<dt><code>$&lt;TARGET_OBJECTS:objLib&gt;</code></p>
<dd>List of objects resulting from build of <code>objLib</code>. <code>objLib</code> must be an object of type <code>OBJECT_LIBRARY</code>. This expression may only be used in the sources of <code>add_library()</code> and <code>add_executable()</code> commands.</p>
<dt><code>$&lt;SHELL_PATH:&#8230;&gt;</code></p>
<dd>Content of <code>&#8230;</code> converted to shell path style. For example, slashes are converted to backslashes in Windows shells and drive letters are converted to posix paths in MSYS shells. The <code>&#8230;</code> must be an absolute path.</dl>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
