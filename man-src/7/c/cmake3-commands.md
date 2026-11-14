---
title: "cmake3-commands(7)"
name: "cmake3-commands"
section: "7"
letter: "c"
url: "/docs/linux/man/7-cmake3-commands/"
description: "cmake-commands – CMake Language Command Reference"
---

<p>cmake-commands &#8211; CMake Language Command Reference</p>
<h2>Normal Commands</h2>
<p>These commands may be used freely in CMake projects.</p>
<h3>add_compile_options</h3>
<p>Adds options to the compilation of source files. </p>
<pre>add_compile_options(&lt;option&gt; ...)</pre>
<p>Adds options to the compiler command line for targets in the current directory and below that are added after this command is invoked. See documentation of the <code>directory</code> and <code>target</code> <code>COMPILE_OPTIONS</code> properties. </p>
<p> This command can be used to add any options, but alternative commands exist to add preprocessor definitions (<code>target_compile_definitions()</code> and <code>add_definitions()</code>) or include directories (<code>target_include_directories()</code> and <code>include_directories()</code>). </p>
<p> Arguments to <code>add_compile_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>add_custom_command</h3>
<p>Add a custom build rule to the generated build system. </p>
<p> There are two main signatures for <code>add_custom_command</code>.</p>
<h3>Generating Files</h3>
<p>The first signature is for adding a custom command to produce an output: </p>
<pre>add_custom_command(OUTPUT output1 [output2 ...]
 COMMAND command1 [ARGS] [args1...]
 [COMMAND command2 [ARGS] [args2...] ...]
 [MAIN_DEPENDENCY depend]
 [DEPENDS [depends...]]
 [BYPRODUCTS [files...]]
 [IMPLICIT_DEPENDS &lt;lang1&gt; depend1
 [&lt;lang2&gt; depend2] ...]
 [WORKING_DIRECTORY dir]
 [COMMENT comment]
 [VERBATIM] [APPEND] [USES_TERMINAL])</pre>
<p>This defines a command to generate specified <code>OUTPUT</code> file(s). A target created in the same directory (<code>CMakeLists.txt</code> file) that specifies any output of the custom command as a source file is given a rule to generate the file using the command at build time. Do not list the output in more than one independent target that may build in parallel or the two instances of the rule may conflict (instead use the <code>add_custom_target()</code> command to drive the command and make the other targets depend on that one). In makefile terms this creates a new target in the following form: </p>
<pre>OUTPUT: MAIN_DEPENDENCY DEPENDS
 COMMAND</pre>
<p>The options are:</p>
<dl>
<dt><code>APPEND</code></p>
<dd>Append the <code>COMMAND</code> and <code>DEPENDS</code> option values to the custom command for the first output specified. There must have already been a previous call to this command with the same output. The <code>COMMENT</code>, <code>MAIN_DEPENDENCY</code>, and <code>WORKING_DIRECTORY</code> options are currently ignored when APPEND is given, but may be used in the future.</p>
<dt><code>BYPRODUCTS</code></p>
<dd>Specify the files the command is expected to produce but whose modification time may or may not be newer than the dependencies. If a byproduct name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each byproduct file will be marked with the <code>GENERATED</code> source file property automatically. </p>
<p> Explicit specification of byproducts is supported by the <code>Ninja</code> generator to tell the <code>ninja</code> build tool how to regenerate byproducts when they are missing. It is also useful when other build rules (e.g. custom commands) depend on the byproducts. Ninja requires a build rule for any generated file on which another rule depends even if there are order-only dependencies to ensure the byproducts will be available before their dependents build. </p>
<p> The <code>BYPRODUCTS</code> option is ignored on non-Ninja generators except to mark byproducts <code>GENERATED</code>.</p>
<dt><code>COMMAND</code></p>
<dd>Specify the command-line(s) to execute at build time. If more than one <code>COMMAND</code> is specified they will be executed in order, but <i>not</i> necessarily composed into a stateful shell or batch script. (To run a full script, use the <code>configure_file()</code> command or the <code>file(GENERATE)</code> command to create it, and then specify a <code>COMMAND</code> to launch it.) The optional <code>ARGS</code> argument is for backward compatibility and will be ignored. </p>
<p> If <code>COMMAND</code> specifies an executable target name (created by the <code>add_executable()</code> command) it will automatically be replaced by the location of the executable created at build time. If set, the <code>CROSSCOMPILING_EMULATOR</code> executable target property will also be prepended to the command to allow the executable to run on the host. (Use the <code>TARGET_FILE</code> <code>generator expression</code> to reference an executable later in the command line.) Additionally a target-level dependency will be added so that the executable target will be built before any target using this custom command. However this does NOT add a file-level dependency that would cause the custom command to re-run whenever the executable is recompiled. </p>
<p> Arguments to <code>COMMAND</code> may use <code>generator expressions</code>. References to target names in generator expressions imply target-level dependencies, but NOT file-level dependencies. List target names with the <code>DEPENDS</code> option to add file-level dependencies.</p>
<dt><code>COMMENT</code></p>
<dd>Display the given message before the commands are executed at build time.</p>
<dt><code>DEPENDS</code></p>
<dd>Specify files on which the command depends. If any dependency is an <code>OUTPUT</code> of another custom command in the same directory (<code>CMakeLists.txt</code> file) CMake automatically brings the other custom command into the target in which this command is built. If <code>DEPENDS</code> is not specified the command will run whenever the <code>OUTPUT</code> is missing; if the command does not actually create the <code>OUTPUT</code> then the rule will always run. If <code>DEPENDS</code> specifies any target (created by the <code>add_custom_target()</code>, <code>add_executable()</code>, or <code>add_library()</code> command) a target-level dependency is created to make sure the target is built before any target using this custom command. Additionally, if the target is an executable or library a file-level dependency is created to cause the custom command to re-run whenever the target is recompiled. </p>
<p> Arguments to <code>DEPENDS</code> may use <code>generator expressions</code>.</p>
<dt><code>IMPLICIT_DEPENDS</code></p>
<dd>Request scanning of implicit dependencies of an input file. The language given specifies the programming language whose corresponding dependency scanner should be used. Currently only <code>C</code> and <code>CXX</code> language scanners are supported. The language has to be specified for every file in the <code>IMPLICIT_DEPENDS</code> list. Dependencies discovered from the scanning are added to those of the custom command at build time. Note that the <code>IMPLICIT_DEPENDS</code> option is currently supported only for Makefile generators and will be ignored by other generators.</p>
<dt><code>MAIN_DEPENDENCY</code></p>
<dd>Specify the primary input source file to the command. This is treated just like any value given to the <code>DEPENDS</code> option but also suggests to Visual Studio generators where to hang the custom command. At most one custom command may specify a given source file as its main dependency.</p>
<dt><code>OUTPUT</code></p>
<dd>Specify the output files the command is expected to produce. If an output name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each output file will be marked with the <code>GENERATED</code> source file property automatically. If the output of the custom command is not actually created as a file on disk it should be marked with the <code>SYMBOLIC</code> source file property.</p>
<dt><code>USES_TERMINAL</code></p>
<dd>The command will be given direct access to the terminal if possible. With the <code>Ninja</code> generator, this places the command in the <code>console</code> <code>pool</code>.</p>
<dt><code>VERBATIM</code></p>
<dd>All arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before add_custom_command even sees the arguments. Use of <code>VERBATIM</code> is recommended as it enables correct behavior. When <code>VERBATIM</code> is not given the behavior is platform specific because there is no protection of tool-specific special characters.</p>
<dt><code>WORKING_DIRECTORY</code></p>
<dd>Execute the command with the given current working directory. If it is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory.</dl>
<h3>Build Events</h3>
<p>The second signature adds a custom command to a target such as a library or executable. This is useful for performing an operation before or after building the target. The command becomes part of the target and will only execute when the target itself is built. If the target is already built, the command will not execute. </p>
<pre>add_custom_command(TARGET &lt;target&gt;
 PRE_BUILD | PRE_LINK | POST_BUILD
 COMMAND command1 [ARGS] [args1...]
 [COMMAND command2 [ARGS] [args2...] ...]
 [BYPRODUCTS [files...]]
 [WORKING_DIRECTORY dir]
 [COMMENT comment]
 [VERBATIM] [USES_TERMINAL])</pre>
<p>This defines a new command that will be associated with building the specified <code>&lt;target&gt;</code>. The <code>&lt;target&gt;</code> must be defined in the current directory; targets defined in other directories may not be specified. </p>
<p> When the command will happen is determined by which of the following is specified:</p>
<dl>
<dt><code>PRE_BUILD</code></p>
<dd>Run before any other rules are executed within the target. This is supported only on Visual Studio 7 or later. For all other generators <code>PRE_BUILD</code> will be treated as <code>PRE_LINK</code>.</p>
<dt><code>PRE_LINK</code></p>
<dd>Run after sources have been compiled but before linking the binary or running the librarian or archiver tool of a static library. This is not defined for targets created by the <code>add_custom_target()</code> command.</p>
<dt><code>POST_BUILD</code></p>
<dd>Run after all other rules within the target have been executed.</dl>
<h3>add_custom_target</h3>
<p>Add a target with no output so it will always be built. </p>
<pre>add_custom_target(Name [ALL] [command1 [args1...]]
 [COMMAND command2 [args2...] ...]
 [DEPENDS depend depend depend ... ]
 [BYPRODUCTS [files...]]
 [WORKING_DIRECTORY dir]
 [COMMENT comment]
 [VERBATIM] [USES_TERMINAL]
 [SOURCES src1 [src2...]])</pre>
<p>Adds a target with the given name that executes the given commands. The target has no output file and is <i>always considered out of date</i> even if the commands try to create a file with the name of the target. Use the <code>add_custom_command()</code> command to generate a file with dependencies. By default nothing depends on the custom target. Use the <code>add_dependencies()</code> command to add dependencies to or from other targets. </p>
<p> The options are:</p>
<dl>
<dt><code>ALL</code></p>
<dd>Indicate that this target should be added to the default build target so that it will be run every time (the command cannot be called <code>ALL</code>).</p>
<dt><code>BYPRODUCTS</code></p>
<dd>Specify the files the command is expected to produce but whose modification time may or may not be updated on subsequent builds. If a byproduct name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Each byproduct file will be marked with the <code>GENERATED</code> source file property automatically. </p>
<p> Explicit specification of byproducts is supported by the <code>Ninja</code> generator to tell the <code>ninja</code> build tool how to regenerate byproducts when they are missing. It is also useful when other build rules (e.g. custom commands) depend on the byproducts. Ninja requires a build rule for any generated file on which another rule depends even if there are order-only dependencies to ensure the byproducts will be available before their dependents build. </p>
<p> The <code>BYPRODUCTS</code> option is ignored on non-Ninja generators except to mark byproducts <code>GENERATED</code>.</p>
<dt><code>COMMAND</code></p>
<dd>Specify the command-line(s) to execute at build time. If more than one <code>COMMAND</code> is specified they will be executed in order, but <i>not</i> necessarily composed into a stateful shell or batch script. (To run a full script, use the <code>configure_file()</code> command or the <code>file(GENERATE)</code> command to create it, and then specify a <code>COMMAND</code> to launch it.) </p>
<p> If <code>COMMAND</code> specifies an executable target name (created by the <code>add_executable()</code> command) it will automatically be replaced by the location of the executable created at build time. If set, the <code>CROSSCOMPILING_EMULATOR</code> executable target property will also be prepended to the command to allow the executable to run on the host. Additionally a target-level dependency will be added so that the executable target will be built before this custom target. </p>
<p> Arguments to <code>COMMAND</code> may use <code>generator expressions</code>. References to target names in generator expressions imply target-level dependencies. </p>
<p> The command and arguments are optional and if not specified an empty target will be created.</p>
<dt><code>COMMENT</code></p>
<dd>Display the given message before the commands are executed at build time.</p>
<dt><code>DEPENDS</code></p>
<dd>Reference files and outputs of custom commands created with <code>add_custom_command()</code> command calls in the same directory (<code>CMakeLists.txt</code> file). They will be brought up to date when the target is built. </p>
<p> Use the <code>add_dependencies()</code> command to add dependencies on other targets.</p>
<dt><code>SOURCES</code></p>
<dd>Specify additional source files to be included in the custom target. Specified source files will be added to IDE project files for convenience in editing even if they have no build rules.</p>
<dt><code>VERBATIM</code></p>
<dd>All arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before <code>add_custom_target</code> even sees the arguments. Use of <code>VERBATIM</code> is recommended as it enables correct behavior. When <code>VERBATIM</code> is not given the behavior is platform specific because there is no protection of tool-specific special characters.</p>
<dt><code>USES_TERMINAL</code></p>
<dd>The command will be given direct access to the terminal if possible. With the <code>Ninja</code> generator, this places the command in the <code>console</code> <code>pool</code>.</p>
<dt><code>WORKING_DIRECTORY</code></p>
<dd>Execute the command with the given current working directory. If it is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory.</dl>
<h3>add_definitions</h3>
<p>Adds -D define flags to the compilation of source files. </p>
<pre>add_definitions(-DFOO -DBAR ...)</pre>
<p>Adds definitions to the compiler command line for targets in the current directory and below (whether added before or after this command is invoked). This command can be used to add any flags, but it is intended to add preprocessor definitions (see the <code>add_compile_options()</code> command to add other flags). Flags beginning in -D or /D that look like preprocessor definitions are automatically added to the <code>COMPILE_DEFINITIONS</code> directory property for the current directory. Definitions with non-trivial values may be left in the set of flags instead of being converted for reasons of backwards compatibility. See documentation of the <code>directory</code>, <code>target</code>, <code>source file</code> <code>COMPILE_DEFINITIONS</code> properties for details on adding preprocessor definitions to specific scopes and configurations. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>add_dependencies</h3>
<p>Add a dependency between top-level targets. </p>
<pre>add_dependencies(&lt;target&gt; [&lt;target-dependency&gt;]...)</pre>
<p>Make a top-level <code>&lt;target&gt;</code> depend on other top-level targets to ensure that they build before <code>&lt;target&gt;</code> does. A top-level target is one created by one of the <code>add_executable()</code>, <code>add_library()</code>, or <code>add_custom_target()</code> commands (but not targets generated by CMake like <code>install</code>). </p>
<p> Dependencies added to an <i>imported target</i> or an <i>interface library</i> are followed transitively in its place since the target itself does not build. </p>
<p> See the <code>DEPENDS</code> option of <code>add_custom_target()</code> and <code>add_custom_command()</code> commands for adding file-level dependencies in custom rules. See the <code>OBJECT_DEPENDS</code> source file property to add file-level dependencies to object files.</p>
<h3>add_executable</h3>
<p>Add an executable to the project using the specified source files. </p>
<pre>add_executable(&lt;name&gt; [WIN32] [MACOSX_BUNDLE]
 [EXCLUDE_FROM_ALL]
 source1 [source2 ...])</pre>
<p>Adds an executable target called <code>&lt;name&gt;</code> to be built from the source files listed in the command invocation. The <code>&lt;name&gt;</code> corresponds to the logical target name and must be globally unique within a project. The actual file name of the executable built is constructed based on conventions of the native platform (such as <code>&lt;name&gt;.exe</code> or just <code>&lt;name&gt;</code>). </p>
<p> By default the executable file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the <code>RUNTIME_OUTPUT_DIRECTORY</code> target property to change this location. See documentation of the <code>OUTPUT_NAME</code> target property to change the <code>&lt;name&gt;</code> part of the final file name. </p>
<p> If <code>WIN32</code> is given the property <code>WIN32_EXECUTABLE</code> will be set on the target created. See documentation of that target property for details. </p>
<p> If <code>MACOSX_BUNDLE</code> is given the corresponding property will be set on the created target. See documentation of the <code>MACOSX_BUNDLE</code> target property for details. </p>
<p> If <code>EXCLUDE_FROM_ALL</code> is given the corresponding property will be set on the created target. See documentation of the <code>EXCLUDE_FROM_ALL</code> target property for details. </p>
<p> Source arguments to <code>add_executable</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>add_executable(&lt;name&gt; IMPORTED [GLOBAL])</pre>
<p>An <i>IMPORTED executable target</i> references an executable file located outside the project. No rules are generated to build it, and the <code>IMPORTED</code> target property is <code>True</code>. The target name has scope in the directory in which it is created and below, but the <code>GLOBAL</code> option extends visibility. It may be referenced like any target built within the project. <code>IMPORTED</code> executables are useful for convenient reference from commands like <code>add_custom_command()</code>. Details about the imported executable are specified by setting properties whose names begin in <code>IMPORTED_</code>. The most important such property is <code>IMPORTED_LOCATION</code> (and its per-configuration version <code>IMPORTED_LOCATION_&lt;CONFIG&gt;</code>) which specifies the location of the main executable file on disk. See documentation of the <code>IMPORTED_*</code> properties for more information. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>add_executable(&lt;name&gt; ALIAS &lt;target&gt;)</pre>
<p>Creates an <i>Alias Target</i>, such that <code>&lt;name&gt;</code> can be used to refer to <code>&lt;target&gt;</code> in subsequent commands. The <code>&lt;name&gt;</code> does not appear in the generated buildsystem as a make target. The <code>&lt;target&gt;</code> may not be an <i>Imported Target</i> or an <code>ALIAS</code>. <code>ALIAS</code> targets can be used as targets to read properties from, executables for custom commands and custom targets. They can also be tested for existence with the regular <code>if(TARGET)</code> subcommand. The <code>&lt;name&gt;</code> may not be used to modify properties of <code>&lt;target&gt;</code>, that is, it may not be used as the operand of <code>set_property()</code>, <code>set_target_properties()</code>, <code>target_link_libraries()</code> etc. An <code>ALIAS</code> target may not be installed or exported.</p>
<h3>add_library</h3>
<p>Add a library to the project using the specified source files.</p>
<h3>Normal Libraries</h3>
<pre>add_library(&lt;name&gt; [STATIC | SHARED | MODULE]
 [EXCLUDE_FROM_ALL]
 source1 [source2 ...])</pre>
<p>Adds a library target called <code>&lt;name&gt;</code> to be built from the source files listed in the command invocation. The <code>&lt;name&gt;</code> corresponds to the logical target name and must be globally unique within a project. The actual file name of the library built is constructed based on conventions of the native platform (such as <code>lib&lt;name&gt;.a</code> or <code>&lt;name&gt;.lib</code>). </p>
<p> <code>STATIC</code>, <code>SHARED</code>, or <code>MODULE</code> may be given to specify the type of library to be created. <code>STATIC</code> libraries are archives of object files for use when linking other targets. <code>SHARED</code> libraries are linked dynamically and loaded at runtime. <code>MODULE</code> libraries are plugins that are not linked into other targets but may be loaded dynamically at runtime using dlopen-like functionality. If no type is given explicitly the type is <code>STATIC</code> or <code>SHARED</code> based on whether the current value of the variable <code>BUILD_SHARED_LIBS</code> is <code>ON</code>. For <code>SHARED</code> and <code>MODULE</code> libraries the <code>POSITION_INDEPENDENT_CODE</code> target property is set to <code>ON</code> automatically. A <code>SHARED</code> library may be marked with the <code>FRAMEWORK</code> target property to create an OS X Framework. </p>
<p> If a library does not export any symbols, it must not be declared as a <code>SHARED</code> library. For example, a Windows resource DLL or a managed C++/CLI DLL that exports no unmanaged symbols would need to be a <code>MODULE</code> library. This is because CMake expects a <code>SHARED</code> library to always have an associated import library on Windows. </p>
<p> By default the library file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the <code>ARCHIVE_OUTPUT_DIRECTORY</code>, <code>LIBRARY_OUTPUT_DIRECTORY</code>, and <code>RUNTIME_OUTPUT_DIRECTORY</code> target properties to change this location. See documentation of the <code>OUTPUT_NAME</code> target property to change the <code>&lt;name&gt;</code> part of the final file name. </p>
<p> If <code>EXCLUDE_FROM_ALL</code> is given the corresponding property will be set on the created target. See documentation of the <code>EXCLUDE_FROM_ALL</code> target property for details. </p>
<p> Source arguments to <code>add_library</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>Imported Libraries</h3>
<pre>add_library(&lt;name&gt; &lt;SHARED|STATIC|MODULE|UNKNOWN&gt; IMPORTED
 [GLOBAL])</pre>
<p>An <i>IMPORTED library target</i> references a library file located outside the project. No rules are generated to build it, and the <code>IMPORTED</code> target property is <code>True</code>. The target name has scope in the directory in which it is created and below, but the <code>GLOBAL</code> option extends visibility. It may be referenced like any target built within the project. <code>IMPORTED</code> libraries are useful for convenient reference from commands like <code>target_link_libraries()</code>. Details about the imported library are specified by setting properties whose names begin in <code>IMPORTED_</code> and <code>INTERFACE_</code>. The most important such property is <code>IMPORTED_LOCATION</code> (and its per-configuration variant <code>IMPORTED_LOCATION_&lt;CONFIG&gt;</code>) which specifies the location of the main library file on disk. See documentation of the <code>IMPORTED_*</code> and <code>INTERFACE_*</code> properties for more information.</p>
<h3>Object Libraries</h3>
<pre>add_library(&lt;name&gt; OBJECT &lt;src&gt;...)</pre>
<p>Creates an <i>Object Library</i>. An object library compiles source files but does not archive or link their object files into a library. Instead other targets created by <code>add_library()</code> or <code>add_executable()</code> may reference the objects using an expression of the form <code>$&lt;TARGET_OBJECTS:objlib&gt;</code> as a source, where <code>objlib</code> is the object library name. For example: </p>
<pre>add_library(... $&lt;TARGET_OBJECTS:objlib&gt; ...)
add_executable(... $&lt;TARGET_OBJECTS:objlib&gt; ...)</pre>
<p>will include objlib&#8217;s object files in a library and an executable along with those compiled from their own sources. Object libraries may contain only sources that compile, header files, and other files that would not affect linking of a normal library (e.g. <code>.txt</code>). They may contain custom commands generating such sources, but not <code>PRE_BUILD</code>, <code>PRE_LINK</code>, or <code>POST_BUILD</code> commands. Object libraries cannot be imported, exported, installed, or linked. Some native build systems may not like targets that have only object files, so consider adding at least one real source file to any target that references <code>$&lt;TARGET_OBJECTS:objlib&gt;</code>.</p>
<h3>Alias Libraries</h3>
<pre>add_library(&lt;name&gt; ALIAS &lt;target&gt;)</pre>
<p>Creates an <i>Alias Target</i>, such that <code>&lt;name&gt;</code> can be used to refer to <code>&lt;target&gt;</code> in subsequent commands. The <code>&lt;name&gt;</code> does not appear in the generatedbuildsystem as a make target. The <code>&lt;target&gt;</code> may not be an <i>Imported Target</i> or an <code>ALIAS</code>. <code>ALIAS</code> targets can be used as linkable targets and as targets to read properties from. They can also be tested for existence with the regular <code>if(TARGET)</code> subcommand. The <code>&lt;name&gt;</code> may not be used to modify properties of <code>&lt;target&gt;</code>, that is, it may not be used as the operand of <code>set_property()</code>, <code>set_target_properties()</code>, <code>target_link_libraries()</code> etc. An <code>ALIAS</code> target may not be installed or exported.</p>
<h3>Interface Libraries</h3>
<pre>add_library(&lt;name&gt; INTERFACE [IMPORTED [GLOBAL]])</pre>
<p>Creates an <i>Interface Library</i>. An <code>INTERFACE</code> library target does not directly create build output, though it may have properties set on it and it may be installed, exported and imported. Typically the <code>INTERFACE_*</code> properties are populated on the interface target using the commands:</p>
<dl>
<dt>&bull;</p>
<dd><code>set_property()</code>,</p>
<dt>&bull;</p>
<dd><code>target_link_libraries(INTERFACE)</code>,</p>
<dt>&bull;</p>
<dd><code>target_include_directories(INTERFACE)</code>,</p>
<dt>&bull;</p>
<dd><code>target_compile_options(INTERFACE)</code>,</p>
<dt>&bull;</p>
<dd><code>target_compile_definitions(INTERFACE)</code>, and</p>
<dt>&bull;</p>
<dd><code>target_sources(INTERFACE)</code>, </p>
<p> and then it is used as an argument to <code>target_link_libraries()</code> like any other target. </p>
<p> An <code>INTERFACE</code> <i>Imported Target</i> may also be created with this signature. An <code>IMPORTED</code> library target references a library defined outside the project. The target name has scope in the directory in which it is created and below, but the <code>GLOBAL</code> option extends visibility. It may be referenced like any target built within the project. <code>IMPORTED</code> libraries are useful for convenient reference from commands like <code>target_link_libraries()</code>.</dl>
<h3>add_subdirectory</h3>
<p>Add a subdirectory to the build. </p>
<pre>add_subdirectory(source_dir [binary_dir]
 [EXCLUDE_FROM_ALL])</pre>
<p>Add a subdirectory to the build. The source_dir specifies the directory in which the source CMakeLists.txt and code files are located. If it is a relative path it will be evaluated with respect to the current directory (the typical usage), but it may also be an absolute path. The <code>binary_dir</code> specifies the directory in which to place the output files. If it is a relative path it will be evaluated with respect to the current output directory, but it may also be an absolute path. If <code>binary_dir</code> is not specified, the value of <code>source_dir</code>, before expanding any relative path, will be used (the typical usage). The CMakeLists.txt file in the specified source directory will be processed immediately by CMake before processing in the current input file continues beyond this command. </p>
<p> If the <code>EXCLUDE_FROM_ALL</code> argument is provided then targets in the subdirectory will not be included in the <code>ALL</code> target of the parent directory by default, and will be excluded from IDE project files. Users must explicitly build targets in the subdirectory. This is meant for use when the subdirectory contains a separate part of the project that is useful but not necessary, such as a set of examples. Typically the subdirectory should contain its own <code>project()</code> command invocation so that a full build system will be generated in the subdirectory (such as a VS IDE solution file). Note that inter-target dependencies supercede this exclusion. If a target built by the parent project depends on a target in the subdirectory, the dependee target will be included in the parent project build system to satisfy the dependency.</p>
<h3>add_test</h3>
<p>Add a test to the project to be run by <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code>. </p>
<pre>add_test(NAME &lt;name&gt; COMMAND &lt;command&gt; [&lt;arg&gt;...]
 [CONFIGURATIONS &lt;config&gt;...]
 [WORKING_DIRECTORY &lt;dir&gt;])</pre>
<p>Add a test called <code>&lt;name&gt;</code>. The test name may not contain spaces, quotes, or other characters special in CMake syntax. The options are:</p>
<dl>
<dt><code>COMMAND</code></p>
<dd>Specify the test command-line. If <code>&lt;command&gt;</code> specifies an executable target (created by <code>add_executable()</code>) it will automatically be replaced by the location of the executable created at build time.</p>
<dt><code>CONFIGURATIONS</code></p>
<dd>Restrict execution of the test only to the named configurations.</p>
<dt><code>WORKING_DIRECTORY</code></p>
<dd>Set the <code>WORKING_DIRECTORY</code> test property to specify the working directory in which to execute the test. If not specified the test will be run with the current working directory set to the build directory corresponding to the current source directory. </p>
<p> The given test command is expected to exit with code <code>0</code> to pass and non-zero to fail, or vice-versa if the <code>WILL_FAIL</code> test property is set. Any output written to stdout or stderr will be captured by <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> but does not affect the pass/fail status unless the <code>PASS_REGULAR_EXPRESSION</code> or <code>FAIL_REGULAR_EXPRESSION</code> test property is used. </p>
<p> The <code>COMMAND</code> and <code>WORKING_DIRECTORY</code> options may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. </p>
<p> Example usage: </p>
<pre>add_test(NAME mytest
 COMMAND testDriver --config $&lt;CONFIGURATION&gt;
 --exe $&lt;TARGET_FILE:myexe&gt;)</pre>
<p>This creates a test <code>mytest</code> whose command runs a <code>testDriver</code> tool passing the configuration name and the full path to the executable file produced by target <code>myexe</code>. </p>
<p> <code>NOTE:</code> CMake will generate tests only if the <code>enable_testing()</code> command has been invoked. The <code>CTest</code> module invokes the command automatically when the <code>BUILD_TESTING</code> option is <code>ON</code>. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>add_test(&lt;name&gt; &lt;command&gt; [&lt;arg&gt;...])</pre>
<p>Add a test called <code>&lt;name&gt;</code> with the given command-line. Unlike the above <code>NAME</code> signature no transformation is performed on the command-line to support target names or generator expressions.</dl>
<h3>aux_source_directory</h3>
<p>Find all source files in a directory. </p>
<pre>aux_source_directory(&lt;dir&gt; &lt;variable&gt;)</pre>
<p>Collects the names of all the source files in the specified directory and stores the list in the <code>&lt;variable&gt;</code> provided. This command is intended to be used by projects that use explicit template instantiation. Template instantiation files can be stored in a &quot;Templates&quot; subdirectory and collected automatically using this command to avoid manually listing all instantiations. </p>
<p> It is tempting to use this command to avoid writing the list of source files for a library or executable target. While this seems to work, there is no way for CMake to generate a build system that knows when a new source file has been added. Normally the generated build system knows when it needs to rerun CMake because the CMakeLists.txt file is modified to add a new source. When the source is just added to the directory without modifying this file, one would have to manually rerun CMake to generate a build system incorporating the new file.</p>
<h3>break</h3>
<p>Break from an enclosing foreach or while loop. </p>
<pre>break()</pre>
<p>Breaks from an enclosing foreach loop or while loop </p>
<p> See also the <code>continue()</code> command.</p>
<h3>build_command</h3>
<p>Get a command line to build the current project. This is mainly intended for internal use by the <code>CTest</code> module. </p>
<pre>build_command(&lt;variable&gt;
 [CONFIGURATION &lt;config&gt;]
 [TARGET &lt;target&gt;]
 [PROJECT_NAME &lt;projname&gt;] # legacy, causes warning
 )</pre>
<p>Sets the given <code>&lt;variable&gt;</code> to a command-line string of the form: </p>
<pre>&lt;cmake&gt; --build . [--config &lt;config&gt;] [--target &lt;target&gt;] [-- -i]</pre>
<p>where <code>&lt;cmake&gt;</code> is the location of the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> command-line tool, and <code>&lt;config&gt;</code> and <code>&lt;target&gt;</code> are the values provided to the <code>CONFIGURATION</code> and <code>TARGET</code> options, if any. The trailing <code>&#8212; -i</code> option is added for <i>Makefile Generators</i> if policy <code>CMP0061</code> is not set to <code>NEW</code>. </p>
<p> When invoked, this <code>cmake &#8211;build</code> command line will launch the underlying build system tool. </p>
<pre>build_command(&lt;cachevariable&gt; &lt;makecommand&gt;)</pre>
<p>This second signature is deprecated, but still available for backwards compatibility. Use the first signature instead. </p>
<p> It sets the given <code>&lt;cachevariable&gt;</code> to a command-line string as above but without the <code>&#8211;target</code> option. The <code>&lt;makecommand&gt;</code> is ignored but should be the full path to devenv, nmake, make or one of the end user build tools for legacy invocations. </p>
<p> <code>NOTE:</code> In CMake versions prior to 3.0 this command returned a command line that directly invokes the native build tool for the current generator. Their implementation of the <code>PROJECT_NAME</code> option had no useful effects, so CMake now warns on use of the option.</p>
<h3>cmake_host_system_information</h3>
<p>Query host system specific information. </p>
<pre>cmake_host_system_information(RESULT &lt;variable&gt; QUERY &lt;key&gt; ...)</pre>
<p>Queries system information of the host system on which cmake runs. One or more <code>&lt;key&gt;</code> can be provided to select the information to be queried. The list of queried values is stored in <code>&lt;variable&gt;</code>. </p>
<p> <code>&lt;key&gt;</code> can be one of the following values: </p>
<pre>NUMBER_OF_LOGICAL_CORES = Number of logical cores.
NUMBER_OF_PHYSICAL_CORES = Number of physical cores.
HOSTNAME = Hostname.
FQDN = Fully qualified domain name.
TOTAL_VIRTUAL_MEMORY = Total virtual memory in megabytes.
AVAILABLE_VIRTUAL_MEMORY = Available virtual memory in megabytes.
TOTAL_PHYSICAL_MEMORY = Total physical memory in megabytes.
AVAILABLE_PHYSICAL_MEMORY = Available physical memory in megabytes.</pre>
<h3>cmake_minimum_required</h3>
<p>Set the minimum required version of cmake for a project and update <i>Policy Settings</i> to match the version given: </p>
<pre>cmake_minimum_required(VERSION major.minor[.patch[.tweak]]
 [FATAL_ERROR])</pre>
<p>If the current version of CMake is lower than that required it will stop processing the project and report an error. </p>
<p> The <code>FATAL_ERROR</code> option is accepted but ignored by CMake 2.6 and higher. It should be specified so CMake versions 2.4 and lower fail with an error instead of just a warning. </p>
<p> <code>NOTE:</code> Call the <code>cmake_minimum_required()</code> command at the beginning of the top-level <code>CMakeLists.txt</code> file even before calling the <code>project()</code> command. It is important to establish version and policy settings before invoking other commands whose behavior they may affect. See also policy <code>CMP0000</code>. </p>
<p> Calling <code>cmake_minimum_required()</code> inside a <code>function()</code> limits some effects to the function scope when invoked. Such calls should not be made with the intention of having global effects.</p>
<h3>Policy Settings</h3>
<p>The <code>cmake_minimum_required(VERSION)</code> command implicitly invokes the <code>cmake_policy(VERSION)</code> command to specify that the current project code is written for the given version of CMake. All policies introduced in the specified version or earlier will be set to use NEW behavior. All policies introduced after the specified version will be unset. This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. </p>
<p> When a version higher than 2.4 is specified the command implicitly invokes: </p>
<pre>cmake_policy(VERSION major[.minor[.patch[.tweak]]])</pre>
<p>which sets the cmake policy version level to the version specified. When version 2.4 or lower is given the command implicitly invokes: </p>
<pre>cmake_policy(VERSION 2.4)</pre>
<p>which enables compatibility features for CMake 2.4 and lower.</p>
<h3>cmake_parse_arguments</h3>
<p><code>cmake_parse_arguments</code> is intended to be used in macros or functions for parsing the arguments given to that macro or function. It processes the arguments and defines a set of variables which hold the values of the respective options. </p>
<pre>cmake_parse_arguments(&lt;prefix&gt; &lt;options&gt; &lt;one_value_keywords&gt;
 &lt;multi_value_keywords&gt; args...)</pre>
<p>The <code>&lt;options&gt;</code> argument contains all options for the respective macro, i.e. keywords which can be used when calling the macro without any value following, like e.g. the <code>OPTIONAL</code> keyword of the <code>install()</code> command. </p>
<p> The <code>&lt;one_value_keywords&gt;</code> argument contains all keywords for this macro which are followed by one value, like e.g. <code>DESTINATION</code> keyword of the <code>install()</code> command. </p>
<p> The <code>&lt;multi_value_keywords&gt;</code> argument contains all keywords for this macro which can be followed by more than one value, like e.g. the <code>TARGETS</code> or <code>FILES</code> keywords of the <code>install()</code> command. </p>
<p> <code>NOTE:</code> All keywords shall be unique. I.e. every keyword shall only be specified once in either <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> or <code>&lt;multi_value_keywords&gt;</code>. A warning will be emitted if uniqueness is violated. </p>
<p> When done, <code>cmake_parse_arguments</code> will have defined for each of the keywords listed in <code>&lt;options&gt;</code>, <code>&lt;one_value_keywords&gt;</code> and <code>&lt;multi_value_keywords&gt;</code> a variable composed of the given <code>&lt;prefix&gt;</code> followed by <code>&quot;_&quot;</code> and the name of the respective keyword. These variables will then hold the respective value from the argument list. For the <code>&lt;options&gt;</code> keywords this will be <code>TRUE</code> or <code>FALSE</code>. </p>
<p> All remaining arguments are collected in a variable <code>&lt;prefix&gt;_UNPARSED_ARGUMENTS</code>, this can be checked afterwards to see whether your macro was called with unrecognized parameters. </p>
<p> As an example here a <code>my_install()</code> macro, which takes similar arguments as the real <code>install()</code> command: </p>
<pre>function(MY_INSTALL)
 set(options OPTIONAL FAST)
 set(oneValueArgs DESTINATION RENAME)
 set(multiValueArgs TARGETS CONFIGURATIONS)
 cmake_parse_arguments(MY_INSTALL &quot;${options}&quot; &quot;${oneValueArgs}&quot;
 &quot;${multiValueArgs}&quot; ${ARGN} )
 # ...</pre>
<p>Assume <code>my_install()</code> has been called like this: </p>
<pre>my_install(TARGETS foo bar DESTINATION bin OPTIONAL blub)</pre>
<p>After the <code>cmake_parse_arguments</code> call the macro will have set the following variables: </p>
<pre>MY_INSTALL_OPTIONAL = TRUE
MY_INSTALL_FAST = FALSE (was not used in call to my_install)
MY_INSTALL_DESTINATION = &quot;bin&quot;
MY_INSTALL_RENAME = &quot;&quot; (was not used)
MY_INSTALL_TARGETS = &quot;foo;bar&quot;
MY_INSTALL_CONFIGURATIONS = &quot;&quot; (was not used)
MY_INSTALL_UNPARSED_ARGUMENTS = &quot;blub&quot; (nothing expected after &quot;OPTIONAL&quot;)</pre>
<p>You can then continue and process these variables. </p>
<p> Keywords terminate lists of values, e.g. if directly after a one_value_keyword another recognized keyword follows, this is interpreted as the beginning of the new option. E.g. <code>my_install(TARGETS foo DESTINATION OPTIONAL)</code> would result in <code>MY_INSTALL_DESTINATION</code> set to <code>&quot;OPTIONAL&quot;</code>, but as <code>OPTIONAL</code> is a keyword itself <code>MY_INSTALL_DESTINATION</code> will be empty and <code>MY_INSTALL_OPTIONAL</code> will therefore be set to <code>TRUE</code>.</p>
<h3>cmake_policy</h3>
<p>Manage CMake Policy settings. See the <code><a href="/docs/linux/man/7-cmake3-policies/">cmake3-policies</a>(7)</code> manual for defined policies. </p>
<p> As CMake evolves it is sometimes necessary to change existing behavior in order to fix bugs or improve implementations of existing features. The CMake Policy mechanism is designed to help keep existing projects building as new versions of CMake introduce changes in behavior. Each new policy (behavioral change) is given an identifier of the form <code>CMP&lt;NNNN&gt;</code> where <code>&lt;NNNN&gt;</code> is an integer index. Documentation associated with each policy describes the <code>OLD</code> and <code>NEW</code> behavior and the reason the policy was introduced. Projects may set each policy to select the desired behavior. When CMake needs to know which behavior to use it checks for a setting specified by the project. If no setting is available the <code>OLD</code> behavior is assumed and a warning is produced requesting that the policy be set.</p>
<h3>Setting Policies by CMake Version</h3>
<p>The <code>cmake_policy</code> command is used to set policies to <code>OLD</code> or <code>NEW</code> behavior. While setting policies individually is supported, we encourage projects to set policies based on CMake versions: </p>
<pre>cmake_policy(VERSION major.minor[.patch[.tweak]])</pre>
<p>Specify that the current CMake code is written for the given version of CMake. All policies introduced in the specified version or earlier will be set to use <code>NEW</code> behavior. All policies introduced after the specified version will be unset (unless the <code>CMAKE_POLICY_DEFAULT_CMP&lt;NNNN&gt;</code> variable sets a default). This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. The policy version specified must be at least 2.4 or the command will report an error. </p>
<p> Note that the <code>cmake_minimum_required(VERSION)</code> command implicitly calls <code>cmake_policy(VERSION)</code> too.</p>
<h3>Setting Policies Explicitly</h3>
<pre>cmake_policy(SET CMP&lt;NNNN&gt; NEW)
cmake_policy(SET CMP&lt;NNNN&gt; OLD)</pre>
<p>Tell CMake to use the <code>OLD</code> or <code>NEW</code> behavior for a given policy. Projects depending on the old behavior of a given policy may silence a policy warning by setting the policy state to <code>OLD</code>. Alternatively one may fix the project to work with the new behavior and set the policy state to <code>NEW</code>. </p>
<p> <code>NOTE:</code> The <code>OLD</code> behavior of a policy is <code>deprecated by definition</code> and may be removed in a future version of CMake.</p>
<h3>Checking Policy Settings</h3>
<pre>cmake_policy(GET CMP&lt;NNNN&gt; &lt;variable&gt;)</pre>
<p>Check whether a given policy is set to <code>OLD</code> or <code>NEW</code> behavior. The output <code>&lt;variable&gt;</code> value will be <code>OLD</code> or <code>NEW</code> if the policy is set, and empty otherwise.</p>
<h3>CMake Policy Stack</h3>
<p>CMake keeps policy settings on a stack, so changes made by the cmake_policy command affect only the top of the stack. A new entry on the policy stack is managed automatically for each subdirectory to protect its parents and siblings. CMake also manages a new entry for scripts loaded by <code>include()</code> and <code>find_package()</code> commands except when invoked with the <code>NO_POLICY_SCOPE</code> option (see also policy <code>CMP0011</code>). The <code>cmake_policy</code> command provides an interface to manage custom entries on the policy stack: </p>
<pre>cmake_policy(PUSH)
cmake_policy(POP)</pre>
<p>Each <code>PUSH</code> must have a matching <code>POP</code> to erase any changes. This is useful to make temporary changes to policy settings. Calls to the <code>cmake_minimum_required(VERSION)</code>, <code>cmake_policy(VERSION)</code>, or <code>cmake_policy(SET)</code> commands influence only the current top of the policy stack. </p>
<p> Commands created by the <code>function()</code> and <code>macro()</code> commands record policy settings when they are created and use the pre-record policies when they are invoked. If the function or macro implementation sets policies, the changes automatically propagate up through callers until they reach the closest nested policy stack entry.</p>
<h3>configure_file</h3>
<p>Copy a file to another location and modify its contents. </p>
<pre>configure_file(&lt;input&gt; &lt;output&gt;
 [COPYONLY] [ESCAPE_QUOTES] [@ONLY]
 [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF] ])</pre>
<p>Copies an <code>&lt;input&gt;</code> file to an <code>&lt;output&gt;</code> file and substitutes variable values referenced as <code>@VAR@</code> or <code>${VAR}</code> in the input file content. Each variable reference will be replaced with the current value of the variable, or the empty string if the variable is not defined. Furthermore, input lines of the form: </p>
<pre>#cmakedefine VAR ...</pre>
<p>will be replaced with either: </p>
<pre>#define VAR ...</pre>
<p>or: </p>
<pre>/* #undef VAR */</pre>
<p>depending on whether <code>VAR</code> is set in CMake to any value not considered a false constant by the <code>if()</code> command. The &quot;&#8230;&quot; content on the line after the variable name, if any, is processed as above. Input file lines of the form <code>#cmakedefine01 VAR</code> will be replaced with either <code>#define VAR 1</code> or <code>#define VAR 0</code> similarly. </p>
<p> If the input file is modified the build system will re-run CMake to re-configure the file and generate the build system again. </p>
<p> The arguments are:</p>
<dl>
<dt><code>&lt;input&gt;</code></p>
<dd>Path to the input file. A relative path is treated with respect to the value of <code>CMAKE_CURRENT_SOURCE_DIR</code>. The input path must be a file, not a directory.</p>
<dt><code>&lt;output&gt;</code></p>
<dd>Path to the output file or directory. A relative path is treated with respect to the value of <code>CMAKE_CURRENT_BINARY_DIR</code>. If the path names an existing directory the output file is placed in that directory with the same file name as the input file.</p>
<dt><code>COPYONLY</code></p>
<dd>Copy the file without replacing any variable references or other content. This option may not be used with <code>NEWLINE_STYLE</code>.</p>
<dt><code>ESCAPE_QUOTES</code></p>
<dd>Escape any substituted quotes with backslashes (C-style).</p>
<dt><code>@ONLY</code></p>
<dd>Restrict variable replacement to references of the form <code>@VAR@</code>. This is useful for configuring scripts that use <code>${VAR}</code> syntax.</p>
<dt><code>NEWLINE_STYLE &lt;style&gt;</code></p>
<dd>Specify the newline style for the output file. Specify <code>UNIX</code> or <code>LF</code> for <code>
</code> newlines, or specify <code>DOS</code>, <code>WIN32</code>, or <code>CRLF</code> for <code>
</code> newlines. This option may not be used with <code>COPYONLY</code>.</dl>
<h3>Example</h3>
<p>Consider a source tree containing a <code>foo.h.in</code> file: </p>
<pre>#cmakedefine FOO_ENABLE
#cmakedefine FOO_STRING &quot;@FOO_STRING@&quot;</pre>
<p>An adjacent <code>CMakeLists.txt</code> may use <code>configure_file</code> to configure the header: </p>
<pre>option(FOO_ENABLE &quot;Enable Foo&quot; ON)
if(FOO_ENABLE)
 set(FOO_STRING &quot;foo&quot;)
endif()
configure_file(foo.h.in foo.h @ONLY)</pre>
<p>This creates a <code>foo.h</code> in the build directory corresponding to this source directory. If the <code>FOO_ENABLE</code> option is on, the configured file will contain: </p>
<pre>#define FOO_ENABLE
#define FOO_STRING &quot;foo&quot;</pre>
<p>Otherwise it will contain: </p>
<pre>/* #undef FOO_ENABLE */
/* #undef FOO_STRING */</pre>
<p>One may then use the <code>include_directories()</code> command to specify the output directory as an include directory: </p>
<pre>include_directories(${CMAKE_CURRENT_BINARY_DIR})</pre>
<p>so that sources may include the header as <code>#include &lt;foo.h&gt;</code>.</p>
<h3>continue</h3>
<p>Continue to the top of enclosing foreach or while loop. </p>
<pre>continue()</pre>
<p>The <code>continue</code> command allows a cmake script to abort the rest of a block in a <code>foreach()</code> or <code>while()</code> loop, and start at the top of the next iteration. See also the <code>break()</code> command.</p>
<h3>create_test_sourcelist</h3>
<p>Create a test driver and source list for building test programs. </p>
<pre>create_test_sourcelist(sourceListName driverName
 test1 test2 test3
 EXTRA_INCLUDE include.h
 FUNCTION function)</pre>
<p>A test driver is a program that links together many small tests into a single executable. This is useful when building static executables with large libraries to shrink the total required size. The list of source files needed to build the test driver will be in <code>sourceListName</code>. <code>driverName</code> is the name of the test driver program. The rest of the arguments consist of a list of test source files, can be semicolon separated. Each test source file should have a function in it that is the same name as the file with no extension (foo.cxx should have int foo(int, char*[]);) <code>driverName</code> will be able to call each of the tests by name on the command line. If <code>EXTRA_INCLUDE</code> is specified, then the next argument is included into the generated file. If <code>FUNCTION</code> is specified, then the next argument is taken as a function name that is passed a pointer to ac and av. This can be used to add extra command line processing to each test. The <code>CMAKE_TESTDRIVER_BEFORE_TESTMAIN</code> cmake variable can be set to have code that will be placed directly before calling the test main function. <code>CMAKE_TESTDRIVER_AFTER_TESTMAIN</code> can be set to have code that will be placed directly after the call to the test main function.</p>
<h3>define_property</h3>
<p>Define and document custom properties. </p>
<pre>define_property(&lt;GLOBAL | DIRECTORY | TARGET | SOURCE |
 TEST | VARIABLE | CACHED_VARIABLE&gt;
 PROPERTY &lt;name&gt; [INHERITED]
 BRIEF_DOCS &lt;brief-doc&gt; [docs...]
 FULL_DOCS &lt;full-doc&gt; [docs...])</pre>
<p>Define one property in a scope for use with the <code>set_property()</code> and <code>get_property()</code> commands. This is primarily useful to associate documentation with property names that may be retrieved with the <code>get_property()</code> command. The first argument determines the kind of scope in which the property should be used. It must be one of the following: </p>
<pre>GLOBAL = associated with the global namespace
DIRECTORY = associated with one directory
TARGET = associated with one target
SOURCE = associated with one source file
TEST = associated with a test named with add_test
VARIABLE = documents a CMake language variable
CACHED_VARIABLE = documents a CMake cache variable</pre>
<p>Note that unlike <code>set_property()</code> and <code>get_property()</code> no actual scope needs to be given; only the kind of scope is important. </p>
<p> The required <code>PROPERTY</code> option is immediately followed by the name of the property being defined. </p>
<p> If the <code>INHERITED</code> option then the <code>get_property()</code> command will chain up to the next higher scope when the requested property is not set in the scope given to the command. <code>DIRECTORY</code> scope chains to <code>GLOBAL</code>. <code>TARGET</code>, <code>SOURCE</code>, and <code>TEST</code> chain to <code>DIRECTORY</code>. </p>
<p> The <code>BRIEF_DOCS</code> and <code>FULL_DOCS</code> options are followed by strings to be associated with the property as its brief and full documentation. Corresponding options to the <code>get_property()</code> command will retrieve the documentation.</p>
<h3>elseif</h3>
<p>Starts the elseif portion of an if block. </p>
<pre>elseif(expression)</pre>
<p>See the <code>if()</code> command.</p>
<h3>else</h3>
<p>Starts the else portion of an if block. </p>
<pre>else(expression)</pre>
<p>See the <code>if()</code> command.</p>
<h3>enable_language</h3>
<p>Enable a language (CXX/C/Fortran/etc) </p>
<pre>enable_language(&lt;lang&gt; [OPTIONAL] )</pre>
<p>This command enables support for the named language in CMake. This is the same as the project command but does not create any of the extra variables that are created by the project command. Example languages are CXX, C, Fortran. </p>
<p> This command must be called in file scope, not in a function call. Furthermore, it must be called in the highest directory common to all targets using the named language directly for compiling sources or indirectly through link dependencies. It is simplest to enable all needed languages in the top-level directory of a project. </p>
<p> The <code>OPTIONAL</code> keyword is a placeholder for future implementation and does not currently work.</p>
<h3>enable_testing</h3>
<p>Enable testing for current directory and below. </p>
<pre>enable_testing()</pre>
<p>Enables testing for this directory and below. See also the <code>add_test()</code> command. Note that ctest expects to find a test file in the build directory root. Therefore, this command should be in the source directory root.</p>
<h3>endforeach</h3>
<p>Ends a list of commands in a foreach block. </p>
<pre>endforeach(expression)</pre>
<p>See the <code>foreach()</code> command.</p>
<h3>endfunction</h3>
<p>Ends a list of commands in a function block. </p>
<pre>endfunction(expression)</pre>
<p>See the <code>function()</code> command.</p>
<h3>endif</h3>
<p>Ends a list of commands in an if block. </p>
<pre>endif(expression)</pre>
<p>See the <code>if()</code> command.</p>
<h3>endmacro</h3>
<p>Ends a list of commands in a macro block. </p>
<pre>endmacro(expression)</pre>
<p>See the <code>macro()</code> command.</p>
<h3>endwhile</h3>
<p>Ends a list of commands in a while block. </p>
<pre>endwhile(expression)</pre>
<p>See the <code>while()</code> command.</p>
<h3>execute_process</h3>
<p>Execute one or more child processes. </p>
<pre>execute_process(COMMAND &lt;cmd1&gt; [args1...]]
 [COMMAND &lt;cmd2&gt; [args2...] [...]]
 [WORKING_DIRECTORY &lt;directory&gt;]
 [TIMEOUT &lt;seconds&gt;]
 [RESULT_VARIABLE &lt;variable&gt;]
 [OUTPUT_VARIABLE &lt;variable&gt;]
 [ERROR_VARIABLE &lt;variable&gt;]
 [INPUT_FILE &lt;file&gt;]
 [OUTPUT_FILE &lt;file&gt;]
 [ERROR_FILE &lt;file&gt;]
 [OUTPUT_QUIET]
 [ERROR_QUIET]
 [OUTPUT_STRIP_TRAILING_WHITESPACE]
 [ERROR_STRIP_TRAILING_WHITESPACE])</pre>
<p>Runs the given sequence of one or more commands with the standard output of each process piped to the standard input of the next. A single standard error pipe is used for all processes. </p>
<p> Options:</p>
<dl>
<dt><code>COMMAND</code></p>
<dd>A child process command line. </p>
<p> CMake executes the child process using operating system APIs directly. All arguments are passed VERBATIM to the child process. No intermediate shell is used, so shell operators such as <code>&gt;</code> are treated as normal arguments. (Use the <code>INPUT_*</code>, <code>OUTPUT_*</code>, and <code>ERROR_*</code> options to redirect stdin, stdout, and stderr.)</p>
<dt><code>WORKING_DIRECTORY</code></p>
<dd>The named directory will be set as the current working directory of the child processes.</p>
<dt><code>TIMEOUT</code></p>
<dd>The child processes will be terminated if they do not finish in the specified number of seconds (fractions are allowed).</p>
<dt><code>RESULT_VARIABLE</code></p>
<dd>The variable will be set to contain the result of running the processes. This will be an integer return code from the last child or a string describing an error condition.</p>
<dt><code>OUTPUT_VARIABLE</code>, <code>ERROR_VARIABLE</code></p>
<dd>The variable named will be set with the contents of the standard output and standard error pipes, respectively. If the same variable is named for both pipes their output will be merged in the order produced.</p>
<dt><code>INPUT_FILE, OUTPUT_FILE</code>, <code>ERROR_FILE</code></p>
<dd>The file named will be attached to the standard input of the first process, standard output of the last process, or standard error of all processes, respectively. If the same file is named for both output and error then it will be used for both.</p>
<dt><code>OUTPUT_QUIET</code>, <code>ERROR_QUIET</code></p>
<dd>The standard output or standard error results will be quietly ignored. </p>
<p> If more than one <code>OUTPUT_*</code> or <code>ERROR_*</code> option is given for the same pipe the precedence is not specified. If no <code>OUTPUT_*</code> or <code>ERROR_*</code> options are given the output will be shared with the corresponding pipes of the CMake process itself. </p>
<p> The <code>execute_process()</code> command is a newer more powerful version of <code>exec_program()</code>, but the old command has been kept for compatibility. Both commands run while CMake is processing the project prior to build system generation. Use <code>add_custom_target()</code> and <code>add_custom_command()</code> to create custom commands that run at build time.</dl>
<h3>export</h3>
<p>Export targets from the build tree for use by outside projects. </p>
<pre>export(EXPORT &lt;export-name&gt; [NAMESPACE &lt;namespace&gt;] [FILE &lt;filename&gt;])</pre>
<p>Create a file <code>&lt;filename&gt;</code> that may be included by outside projects to import targets from the current project&#8217;s build tree. This is useful during cross-compiling to build utility executables that can run on the host platform in one project and then import them into another project being compiled for the target platform. If the <code>NAMESPACE</code> option is given the <code>&lt;namespace&gt;</code> string will be prepended to all target names written to the file. </p>
<p> Target installations are associated with the export <code>&lt;export-name&gt;</code> using the <code>EXPORT</code> option of the <code>install(TARGETS)</code> command. </p>
<p> The file created by this command is specific to the build tree and should never be installed. See the <code>install(EXPORT)</code> command to export targets from an installation tree. </p>
<p> The properties set on the generated IMPORTED targets will have the same values as the final values of the input TARGETS. </p>
<pre>export(TARGETS [target1 [target2 [...]]] [NAMESPACE &lt;namespace&gt;]
 [APPEND] FILE &lt;filename&gt; [EXPORT_LINK_INTERFACE_LIBRARIES])</pre>
<p>This signature is similar to the <code>EXPORT</code> signature, but targets are listed explicitly rather than specified as an export-name. If the APPEND option is given the generated code will be appended to the file instead of overwriting it. The EXPORT_LINK_INTERFACE_LIBRARIES keyword, if present, causes the contents of the properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code> to be exported, when policy CMP0022 is NEW. If a library target is included in the export but a target to which it links is not included the behavior is unspecified. </p>
<pre>export(PACKAGE &lt;name&gt;)</pre>
<p>Store the current build directory in the CMake user package registry for package <code>&lt;name&gt;</code>. The find_package command may consider the directory while searching for package <code>&lt;name&gt;</code>. This helps dependent projects find and use a package from the current project&#8217;s build tree without help from the user. Note that the entry in the package registry that this command creates works only in conjunction with a package configuration file (<code>&lt;name&gt;Config.cmake</code>) that works with the build tree. In some cases, for example for packaging and for system wide installations, it is not desirable to write the user package registry. If the <code>CMAKE_EXPORT_NO_PACKAGE_REGISTRY</code> variable is enabled, the <code>export(PACKAGE)</code> command will do nothing.</p>
<h3>file</h3>
<p>File manipulation command. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(WRITE &lt;filename&gt; &lt;content&gt;...)
file(APPEND &lt;filename&gt; &lt;content&gt;...)</pre>
<p>Write <code>&lt;content&gt;</code> into a file called <code>&lt;filename&gt;</code>. If the file does not exist, it will be created. If the file already exists, <code>WRITE</code> mode will overwrite it and <code>APPEND</code> mode will append to the end. (If the file is a build input, use the <code>configure_file()</code> command to update the file only when its content changes.) </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(READ &lt;filename&gt; &lt;variable&gt;
 [OFFSET &lt;offset&gt;] [LIMIT &lt;max-in&gt;] [HEX])</pre>
<p>Read content from a file called <code>&lt;filename&gt;</code> and store it in a <code>&lt;variable&gt;</code>. Optionally start from the given <code>&lt;offset&gt;</code> and read at most <code>&lt;max-in&gt;</code> bytes. The <code>HEX</code> option causes data to be converted to a hexadecimal representation (useful for binary data). </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(STRINGS &lt;filename&gt; &lt;variable&gt; [&lt;options&gt;...])</pre>
<p>Parse a list of ASCII strings from <code>&lt;filename&gt;</code> and store it in <code>&lt;variable&gt;</code>. Binary data in the file are ignored. Carriage return (<code></code>, CR) characters are ignored. The options are:</p>
<dl>
<dt><code>LENGTH_MAXIMUM &lt;max-len&gt;</code></p>
<dd>Consider only strings of at most a given length.</p>
<dt><code>LENGTH_MINIMUM &lt;min-len&gt;</code></p>
<dd>Consider only strings of at least a given length.</p>
<dt><code>LIMIT_COUNT &lt;max-num&gt;</code></p>
<dd>Limit the number of distinct strings to be extracted.</p>
<dt><code>LIMIT_INPUT &lt;max-in&gt;</code></p>
<dd>Limit the number of input bytes to read from the file.</p>
<dt><code>LIMIT_OUTPUT &lt;max-out&gt;</code></p>
<dd>Limit the number of total bytes to store in the <code>&lt;variable&gt;</code>.</p>
<dt><code>NEWLINE_CONSUME</code></p>
<dd>Treat newline characters (<code>
</code>, LF) as part of string content instead of terminating at them.</p>
<dt><code>NO_HEX_CONVERSION</code></p>
<dd>Intel Hex and Motorola S-record files are automatically converted to binary while reading unless this option is given.</p>
<dt><code>REGEX &lt;regex&gt;</code></p>
<dd>Consider only strings that match the given regular expression.</p>
<dt><code>ENCODING &lt;encoding-type&gt;</code></p>
<dd>Consider strings of a given encoding. Currently supported encodings are: UTF-8, UTF-16LE, UTF-16BE, UTF-32LE, UTF-32BE. If the ENCODING option is not provided and the file has a Byte Order Mark, the ENCODING option will be defaulted to respect the Byte Order Mark. </p>
<p> For example, the code </p>
<pre>file(STRINGS myfile.txt myfile)</pre>
<p>stores a list in the variable <code>myfile</code> in which each item is a line from the input file. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(&lt;MD5|SHA1|SHA224|SHA256|SHA384|SHA512&gt; &lt;filename&gt; &lt;variable&gt;)</pre>
<p>Compute a cryptographic hash of the content of <code>&lt;filename&gt;</code> and store it in a <code>&lt;variable&gt;</code>. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(GLOB &lt;variable&gt;
 [LIST_DIRECTORIES true|false] [RELATIVE &lt;path&gt;]
 [&lt;globbing-expressions&gt;...])
file(GLOB_RECURSE &lt;variable&gt; [FOLLOW_SYMLINKS]
 [LIST_DIRECTORIES true|false] [RELATIVE &lt;path&gt;]
 [&lt;globbing-expressions&gt;...])</pre>
<p>Generate a list of files that match the <code>&lt;globbing-expressions&gt;</code> and store it into the <code>&lt;variable&gt;</code>. Globbing expressions are similar to regular expressions, but much simpler. If <code>RELATIVE</code> flag is specified, the results will be returned as relative paths to the given path. No specific order of results is defined other than that it is deterministic. If order is important then sort the list explicitly (e.g. using the <code>list(SORT)</code> command). </p>
<p> By default <code>GLOB</code> lists directories &#8211; directories are omited in result if <code>LIST_DIRECTORIES</code> is set to false. </p>
<p> <code>NOTE:</code> We do not recommend using GLOB to collect a list of source files from your source tree. If no CMakeLists.txt file changes when a source is added or removed then the generated build system cannot know when to ask CMake to regenerate. </p>
<p> Examples of globbing expressions include: </p>
<pre>*.cxx - match all files with extension cxx
*.vt? - match all files with extension vta,...,vtz
f[3-5].txt - match files f3.txt, f4.txt, f5.txt</pre>
<p>The <code>GLOB_RECURSE</code> mode will traverse all the subdirectories of the matched directory and match the files. Subdirectories that are symlinks are only traversed if <code>FOLLOW_SYMLINKS</code> is given or policy <code>CMP0009</code> is not set to <code>NEW</code>. </p>
<p> By default <code>GLOB_RECURSE</code> omits directories from result list &#8211; setting <code>LIST_DIRECTORIES</code> to true adds directories to result list. If <code>FOLLOW_SYMLINKS</code> is given or policy <code>CMP0009</code> is not set to <code>OLD</code> then <code>LIST_DIRECTORIES</code> treats symlinks as directories. </p>
<p> Examples of recursive globbing include: </p>
<pre>/dir/*.py - match all python files in /dir and subdirectories</pre>
<p><center> &#8212;-<br />
 </center> </p>
<pre>file(RENAME &lt;oldname&gt; &lt;newname&gt;)</pre>
<p>Move a file or directory within a filesystem from <code>&lt;oldname&gt;</code> to <code>&lt;newname&gt;</code>, replacing the destination atomically. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(REMOVE [&lt;files&gt;...])
file(REMOVE_RECURSE [&lt;files&gt;...])</pre>
<p>Remove the given files. The <code>REMOVE_RECURSE</code> mode will remove the given files and directories, also non-empty directories </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(MAKE_DIRECTORY [&lt;directories&gt;...])</pre>
<p>Create the given directories and their parents as needed. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(RELATIVE_PATH &lt;variable&gt; &lt;directory&gt; &lt;file&gt;)</pre>
<p>Compute the relative path from a <code>&lt;directory&gt;</code> to a <code>&lt;file&gt;</code> and store it in the <code>&lt;variable&gt;</code>. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(TO_CMAKE_PATH &quot;&lt;path&gt;&quot; &lt;variable&gt;)
file(TO_NATIVE_PATH &quot;&lt;path&gt;&quot; &lt;variable&gt;)</pre>
<p>The <code>TO_CMAKE_PATH</code> mode converts a native <code>&lt;path&gt;</code> into a cmake-style path with forward-slashes (<code>/</code>). The input can be a single path or a system search path like <code>$ENV{PATH}</code>. A search path will be converted to a cmake-style list separated by <code>;</code> characters. </p>
<p> The <code>TO_NATIVE_PATH</code> mode converts a cmake-style <code>&lt;path&gt;</code> into a native path with platform-specific slashes (<code>\</code> on Windows and <code>/</code> elsewhere). </p>
<p> Always use double quotes around the <code>&lt;path&gt;</code> to be sure it is treated as a single argument to this command. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(DOWNLOAD &lt;url&gt; &lt;file&gt; [&lt;options&gt;...])
file(UPLOAD &lt;file&gt; &lt;url&gt; [&lt;options&gt;...])</pre>
<p>The <code>DOWNLOAD</code> mode downloads the given <code>&lt;url&gt;</code> to a local <code>&lt;file&gt;</code>. The <code>UPLOAD</code> mode uploads a local <code>&lt;file&gt;</code> to a given <code>&lt;url&gt;</code>. </p>
<p> Options to both <code>DOWNLOAD</code> and <code>UPLOAD</code> are:</p>
<dt><code>INACTIVITY_TIMEOUT &lt;seconds&gt;</code></p>
<dd>Terminate the operation after a period of inactivity.</p>
<dt><code>LOG &lt;variable&gt;</code></p>
<dd>Store a human-readable log of the operation in a variable.</p>
<dt><code>SHOW_PROGRESS</code></p>
<dd>Print progress information as status messages until the operation is complete.</p>
<dt><code>STATUS &lt;variable&gt;</code></p>
<dd>Store the resulting status of the operation in a variable. The status is a <code>;</code> separated list of length 2. The first element is the numeric return value for the operation, and the second element is a string value for the error. A <code>0</code> numeric error means no error in the operation.</p>
<dt><code>TIMEOUT &lt;seconds&gt;</code></p>
<dd>Terminate the operation after a given total time has elapsed. </p>
<p> Additional options to <code>DOWNLOAD</code> are: </p>
<p> <code>EXPECTED_HASH ALGO=&lt;value&gt;</code> Verify that the downloaded content hash matches the expected value, where <code>ALGO</code> is one of <code>MD5</code>, <code>SHA1</code>, <code>SHA224</code>, <code>SHA256</code>, <code>SHA384</code>, or <code>SHA512</code>. If it does not match, the operation fails with an error.</p>
<dt><code>EXPECTED_MD5 &lt;value&gt;</code></p>
<dd>Historical short-hand for <code>EXPECTED_HASH MD5=&lt;value&gt;</code>.</p>
<dt><code>TLS_VERIFY &lt;ON|OFF&gt;</code></p>
<dd>Specify whether to verify the server certificate for <code>https://</code> URLs. The default is to <i>not</i> verify.</p>
<dt><code>TLS_CAINFO &lt;file&gt;</code></p>
<dd>Specify a custom Certificate Authority file for <code>https://</code> URLs. </p>
<p> For <code>https://</code> URLs CMake must be built with OpenSSL support. <code>TLS/SSL</code> certificates are not checked by default. Set <code>TLS_VERIFY</code> to <code>ON</code> to check certificates and/or use <code>EXPECTED_HASH</code> to verify downloaded content. If neither <code>TLS</code> option is given CMake will check variables <code>CMAKE_TLS_VERIFY</code> and <code>CMAKE_TLS_CAINFO</code>, respectively. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(TIMESTAMP &lt;filename&gt; &lt;variable&gt; [&lt;format&gt;] [UTC])</pre>
<p>Compute a string representation of the modification time of <code>&lt;filename&gt;</code> and store it in <code>&lt;variable&gt;</code>. Should the command be unable to obtain a timestamp variable will be set to the empty string (&quot;&quot;). </p>
<p> See the <code>string(TIMESTAMP)</code> command for documentation of the <code>&lt;format&gt;</code> and <code>UTC</code> options. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(GENERATE OUTPUT output-file
 &lt;INPUT input-file|CONTENT content&gt;
 [CONDITION expression])</pre>
<p>Generate an output file for each build configuration supported by the current <code>CMake Generator</code>. Evaluate <code>generator expressions</code> from the input content to produce the output content. The options are:</p>
<dt><code>CONDITION &lt;condition&gt;</code></p>
<dd>Generate the output file for a particular configuration only if the condition is true. The condition must be either <code>0</code> or <code>1</code> after evaluating generator expressions.</p>
<dt><code>CONTENT &lt;content&gt;</code></p>
<dd>Use the content given explicitly as input.</p>
<dt><code>INPUT &lt;input-file&gt;</code></p>
<dd>Use the content from a given file as input.</p>
<dt><code>OUTPUT &lt;output-file&gt;</code></p>
<dd>Specify the output file name to generate. Use generator expressions such as <code>$&lt;CONFIG&gt;</code> to specify a configuration-specific output file name. Multiple configurations may generate the same output file only if the generated content is identical. Otherwise, the <code>&lt;output-file&gt;</code> must evaluate to an unique name for each configuration. </p>
<p> Exactly one <code>CONTENT</code> or <code>INPUT</code> option must be given. A specific <code>OUTPUT</code> file may be named by at most one invocation of <code>file(GENERATE)</code>. Generated files are modified on subsequent cmake runs only if their content is changed. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(&lt;COPY|INSTALL&gt; &lt;files&gt;... DESTINATION &lt;dir&gt;
 [FILE_PERMISSIONS &lt;permissions&gt;...]
 [DIRECTORY_PERMISSIONS &lt;permissions&gt;...]
 [NO_SOURCE_PERMISSIONS] [USE_SOURCE_PERMISSIONS]
 [FILES_MATCHING]
 [[PATTERN &lt;pattern&gt; | REGEX &lt;regex&gt;]
 [EXCLUDE] [PERMISSIONS &lt;permissions&gt;...]] [...])</pre>
<p>The <code>COPY</code> signature copies files, directories, and symlinks to a destination folder. Relative input paths are evaluated with respect to the current source directory, and a relative destination is evaluated with respect to the current build directory. Copying preserves input file timestamps, and optimizes out a file if it exists at the destination with the same timestamp. Copying preserves input permissions unless explicit permissions or <code>NO_SOURCE_PERMISSIONS</code> are given (default is <code>USE_SOURCE_PERMISSIONS</code>). </p>
<p> See the <code>install(DIRECTORY)</code> command for documentation of permissions, <code>FILES_MATCHING</code>, <code>PATTERN</code>, <code>REGEX</code>, and <code>EXCLUDE</code> options. Copying directories preserves the structure of their content even if options are used to select a subset of files. </p>
<p> The <code>INSTALL</code> signature differs slightly from <code>COPY</code>: it prints status messages (subject to the <code>CMAKE_INSTALL_MESSAGE</code> variable), and <code>NO_SOURCE_PERMISSIONS</code> is default. Installation scripts generated by the <code>install()</code> command use this signature (with some undocumented options for internal use). </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>file(LOCK &lt;path&gt; [DIRECTORY] [RELEASE]
 [GUARD &lt;FUNCTION|FILE|PROCESS&gt;]
 [RESULT_VARIABLE &lt;variable&gt;]
 [TIMEOUT &lt;seconds&gt;])</pre>
<p>Lock a file specified by <code>&lt;path&gt;</code> if no <code>DIRECTORY</code> option present and file <code>&lt;path&gt;/cmake.lock</code> otherwise. File will be locked for scope defined by <code>GUARD</code> option (default value is <code>PROCESS</code>). <code>RELEASE</code> option can be used to unlock file explicitly. If option <code>TIMEOUT</code> is not specified CMake will wait until lock succeed or until fatal error occurs. If <code>TIMEOUT</code> is set to <code>0</code> lock will be tried once and result will be reported immediately. If <code>TIMEOUT</code> is not <code>0</code> CMake will try to lock file for the period specified by <code>&lt;seconds&gt;</code> value. Any errors will be interpreted as fatal if there is no <code>RESULT_VARIABLE</code> option. Otherwise result will be stored in <code>&lt;variable&gt;</code> and will be <code>0</code> on success or error message on failure. </p>
<p> Note that lock is advisory &#8211; there is no guarantee that other processes will respect this lock, i.e. lock synchronize two or more CMake instances sharing some modifiable resources. Similar logic applied to <code>DIRECTORY</code> option &#8211; locking parent directory doesn&#8217;t prevent other <code>LOCK</code> commands to lock any child directory or file. </p>
<p> Trying to lock file twice is not allowed. Any intermediate directories and file itself will be created if they not exist. <code>GUARD</code> and <code>TIMEOUT</code> options ignored on <code>RELEASE</code> operation.</dl>
<h3>find_file</h3>
<p>A short-hand signature is: </p>
<pre>find_file (&lt;VAR&gt; name1 [path1 path2 ...])</pre>
<p>The general signature is: </p>
<pre>find_file (
 &lt;VAR&gt;
 name | NAMES name1 [name2 ...]
 [HINTS path1 [path2 ... ENV var]]
 [PATHS path1 [path2 ... ENV var]]
 [PATH_SUFFIXES suffix1 [suffix2 ...]]
 [DOC &quot;cache documentation string&quot;]
 [NO_DEFAULT_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [NO_CMAKE_PATH]
 [NO_SYSTEM_ENVIRONMENT_PATH]
 [NO_CMAKE_SYSTEM_PATH]
 [CMAKE_FIND_ROOT_PATH_BOTH |
 ONLY_CMAKE_FIND_ROOT_PATH |
 NO_CMAKE_FIND_ROOT_PATH]
 )</pre>
<p>This command is used to find a full path to named file. A cache entry named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the full path to a file is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>, and the search will be attempted again the next time find_file is invoked with the same variable. </p>
<p> Options include:</p>
<dl>
<dt><code>NAMES</code></p>
<dd>Specify one or more possible names for the full path to a file. </p>
<p> When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions.</p>
<dt><code>HINTS</code>, <code>PATHS</code></p>
<dd>Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable.</p>
<dt><code>PATH_SUFFIXES</code></p>
<dd>Specify additional subdirectories to check below each directory location otherwise considered.</p>
<dt><code>DOC</code></p>
<dd>Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
<p> If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows:</p>
<dt>1.</p>
<dd>Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. This can be skipped if <code>NO_CMAKE_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>2.</p>
<dd>Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>3.</p>
<dd>Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option.</p>
<dt>4.</p>
<dd>Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is an argument.</p>
<dt>&bull;</p>
<dd>Directories in <code>INCLUDE</code>. On Windows hosts: <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/include</code> for other entries in <code>PATH</code>, and the directories in <code>PATH</code> itself.</p>
<dt>5.</p>
<dd>Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_FRAMEWORK_PATH</code></p>
<dt>6.</p>
<dd>Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On OS X the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p> The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p> The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p> These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_INCLUDE</code>. This behavior can be manually overridden on a per-call basis using options:</p>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></p>
<dd>Search in the order described above.</p>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable.</p>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre>find_file (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_file (&lt;VAR&gt; NAMES name)</pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again.</dl>
<h3>find_library</h3>
<p>A short-hand signature is: </p>
<pre>find_library (&lt;VAR&gt; name1 [path1 path2 ...])</pre>
<p>The general signature is: </p>
<pre>find_library (
 &lt;VAR&gt;
 name | NAMES name1 [name2 ...] [NAMES_PER_DIR]
 [HINTS path1 [path2 ... ENV var]]
 [PATHS path1 [path2 ... ENV var]]
 [PATH_SUFFIXES suffix1 [suffix2 ...]]
 [DOC &quot;cache documentation string&quot;]
 [NO_DEFAULT_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [NO_CMAKE_PATH]
 [NO_SYSTEM_ENVIRONMENT_PATH]
 [NO_CMAKE_SYSTEM_PATH]
 [CMAKE_FIND_ROOT_PATH_BOTH |
 ONLY_CMAKE_FIND_ROOT_PATH |
 NO_CMAKE_FIND_ROOT_PATH]
 )</pre>
<p>This command is used to find a library. A cache entry named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the library is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>, and the search will be attempted again the next time find_library is invoked with the same variable. </p>
<p> Options include:</p>
<dl>
<dt><code>NAMES</code></p>
<dd>Specify one or more possible names for the library. </p>
<p> When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions.</p>
<dt><code>HINTS</code>, <code>PATHS</code></p>
<dd>Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable.</p>
<dt><code>PATH_SUFFIXES</code></p>
<dd>Specify additional subdirectories to check below each directory location otherwise considered.</p>
<dt><code>DOC</code></p>
<dd>Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
<p> If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows:</p>
<dt>1.</p>
<dd>Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. This can be skipped if <code>NO_CMAKE_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_LIBRARY_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>2.</p>
<dd>Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_LIBRARY_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>3.</p>
<dd>Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option.</p>
<dt>4.</p>
<dd>Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is an argument.</p>
<dt>&bull;</p>
<dd>Directories in <code>LIB</code>. On Windows hosts: <code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/lib</code> for other entries in <code>PATH</code>, and the directories in <code>PATH</code> itself.</p>
<dt>5.</p>
<dd>Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/lib/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/lib</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_LIBRARY_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_FRAMEWORK_PATH</code></p>
<dt>6.</p>
<dd>Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On OS X the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p> The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p> The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p> These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_LIBRARY</code>. This behavior can be manually overridden on a per-call basis using options:</p>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></p>
<dd>Search in the order described above.</p>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable.</p>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre>find_library (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_library (&lt;VAR&gt; NAMES name)</pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> When more than one value is given to the <code>NAMES</code> option this command by default will consider one name at a time and search every directory for it. The <code>NAMES_PER_DIR</code> option tells this command to consider one directory at a time and search for all names in it. </p>
<p> Each library name given to the <code>NAMES</code> option is first considered as a library file name and then considered with platform-specific prefixes (e.g. <code>lib</code>) and suffixes (e.g. <code>.so</code>). Therefore one may specify library file names such as <code>libfoo.a</code> directly. This can be used to locate static libraries on UNIX-like systems. </p>
<p> If the library found is a framework, then <code>&lt;VAR&gt;</code> will be set to the full path to the framework <code>&lt;fullPath&gt;/A.framework</code>. When a full path to a framework is used as a library, CMake will use a <code>-framework A</code>, and a <code>-F&lt;fullPath&gt;</code> to link the framework to the target. </p>
<p> If the <code>FIND_LIBRARY_USE_LIB64_PATHS</code> global property is set all search paths will be tested as normal, with <code>64/</code> appended, and with all matches of <code>lib/</code> replaced with <code>lib64/</code>. This property is automatically set for the platforms that are known to need it if at least one of the languages supported by the <code>project()</code> command is enabled.</dl>
<h3>find_package</h3>
<p>Load settings for an external project. </p>
<pre>find_package(&lt;package&gt; [version] [EXACT] [QUIET] [MODULE]
 [REQUIRED] [[COMPONENTS] [components...]]
 [OPTIONAL_COMPONENTS components...]
 [NO_POLICY_SCOPE])</pre>
<p>Finds and loads settings from an external project. <code>&lt;package&gt;_FOUND</code> will be set to indicate whether the package was found. When the package is found package-specific information is provided through variables and <i>Imported Targets</i> documented by the package itself. The <code>QUIET</code> option disables messages if the package cannot be found. The <code>MODULE</code> option disables the second signature documented below. The <code>REQUIRED</code> option stops processing with an error message if the package cannot be found. </p>
<p> A package-specific list of required components may be listed after the <code>COMPONENTS</code> option (or after the <code>REQUIRED</code> option if present). Additional optional components may be listed after <code>OPTIONAL_COMPONENTS</code>. Available components and their influence on whether a package is considered to be found are defined by the target package. </p>
<p> The <code>[version]</code> argument requests a version with which the package found should be compatible (format is <code>major[.minor[.patch[.tweak]]]</code>). The <code>EXACT</code> option requests that the version be matched exactly. If no <code>[version]</code> and/or component list is given to a recursive invocation inside a find-module, the corresponding arguments are forwarded automatically from the outer call (including the <code>EXACT</code> flag for <code>[version]</code>). Version support is currently provided only on a package-by-package basis (details below). </p>
<p> User code should generally look for packages using the above simple signature. The remainder of this command documentation specifies the full command signature and details of the search process. Project maintainers wishing to provide a package to be found by this command are encouraged to read on. </p>
<p> The command has two modes by which it searches for packages: &quot;Module&quot; mode and &quot;Config&quot; mode. Module mode is available when the command is invoked with the above reduced signature. CMake searches for a file called <code>Find&lt;package&gt;.cmake</code> in the <code>CMAKE_MODULE_PATH</code> followed by the CMake installation. If the file is found, it is read and processed by CMake. It is responsible for finding the package, checking the version, and producing any needed messages. Many find-modules provide limited or no support for versioning; check the module documentation. If no module is found and the <code>MODULE</code> option is not given the command proceeds to Config mode. </p>
<p> The complete Config mode command signature is: </p>
<pre>find_package(&lt;package&gt; [version] [EXACT] [QUIET]
 [REQUIRED] [[COMPONENTS] [components...]]
 [CONFIG|NO_MODULE]
 [NO_POLICY_SCOPE]
 [NAMES name1 [name2 ...]]
 [CONFIGS config1 [config2 ...]]
 [HINTS path1 [path2 ... ]]
 [PATHS path1 [path2 ... ]]
 [PATH_SUFFIXES suffix1 [suffix2 ...]]
 [NO_DEFAULT_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [NO_CMAKE_PATH]
 [NO_SYSTEM_ENVIRONMENT_PATH]
 [NO_CMAKE_PACKAGE_REGISTRY]
 [NO_CMAKE_BUILDS_PATH] # Deprecated; does nothing.
 [NO_CMAKE_SYSTEM_PATH]
 [NO_CMAKE_SYSTEM_PACKAGE_REGISTRY]
 [CMAKE_FIND_ROOT_PATH_BOTH |
 ONLY_CMAKE_FIND_ROOT_PATH |
 NO_CMAKE_FIND_ROOT_PATH])</pre>
<p>The <code>CONFIG</code> option may be used to skip Module mode explicitly and switch to Config mode. It is synonymous to using <code>NO_MODULE</code>. Config mode is also implied by use of options not specified in the reduced signature. </p>
<p> Config mode attempts to locate a configuration file provided by the package to be found. A cache entry called <code>&lt;package&gt;_DIR</code> is created to hold the directory containing the file. By default the command searches for a package with the name <code>&lt;package&gt;</code>. If the <code>NAMES</code> option is given the names following it are used instead of <code>&lt;package&gt;</code>. The command searches for a file called <code>&lt;name&gt;Config.cmake</code> or <code>&lt;lower-case-name&gt;-config.cmake</code> for each name specified. A replacement set of possible configuration file names may be given using the <code>CONFIGS</code> option. The search procedure is specified below. Once found, the configuration file is read and processed by CMake. Since the file is provided by the package it already knows the location of package contents. The full path to the configuration file is stored in the cmake variable <code>&lt;package&gt;_CONFIG</code>. </p>
<p> All configuration files which have been considered by CMake while searching for an installation of the package with an appropriate version are stored in the cmake variable <code>&lt;package&gt;_CONSIDERED_CONFIGS</code>, the associated versions in <code>&lt;package&gt;_CONSIDERED_VERSIONS</code>. </p>
<p> If the package configuration file cannot be found CMake will generate an error describing the problem unless the <code>QUIET</code> argument is specified. If <code>REQUIRED</code> is specified and the package is not found a fatal error is generated and the configure step stops executing. If <code>&lt;package&gt;_DIR</code> has been set to a directory not containing a configuration file CMake will ignore it and search from scratch. </p>
<p> When the <code>[version]</code> argument is given Config mode will only find a version of the package that claims compatibility with the requested version (format is <code>major[.minor[.patch[.tweak]]]</code>). If the <code>EXACT</code> option is given only a version of the package claiming an exact match of the requested version may be found. CMake does not establish any convention for the meaning of version numbers. Package version numbers are checked by &quot;version&quot; files provided by the packages themselves. For a candidate package configuration file <code>&lt;config-file&gt;.cmake</code> the corresponding version file is located next to it and named either <code>&lt;config-file&gt;-version.cmake</code> or <code>&lt;config-file&gt;Version.cmake</code>. If no such version file is available then the configuration file is assumed to not be compatible with any requested version. A basic version file containing generic version matching code can be created using the <code>CMakePackageConfigHelpers</code> module. When a version file is found it is loaded to check the requested version number. The version file is loaded in a nested scope in which the following variables have been defined:</p>
<dl>
<dt><code>PACKAGE_FIND_NAME</code></p>
<dd>the <code>&lt;package&gt;</code> name</p>
<dt><code>PACKAGE_FIND_VERSION</code></p>
<dd>full requested version string</p>
<dt><code>PACKAGE_FIND_VERSION_MAJOR</code></p>
<dd>major version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_MINOR</code></p>
<dd>minor version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_PATCH</code></p>
<dd>patch version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_TWEAK</code></p>
<dd>tweak version if requested, else 0</p>
<dt><code>PACKAGE_FIND_VERSION_COUNT</code></p>
<dd>number of version components, 0 to 4 </p>
<p> The version file checks whether it satisfies the requested version and sets these variables:</p>
<dt><code>PACKAGE_VERSION</code></p>
<dd>full provided version string</p>
<dt><code>PACKAGE_VERSION_EXACT</code></p>
<dd>true if version is exact match</p>
<dt><code>PACKAGE_VERSION_COMPATIBLE</code></p>
<dd>true if version is compatible</p>
<dt><code>PACKAGE_VERSION_UNSUITABLE</code></p>
<dd>true if unsuitable as any version </p>
<p> These variables are checked by the <code>find_package</code> command to determine whether the configuration file provides an acceptable version. They are not available after the find_package call returns. If the version is acceptable the following variables are set:</p>
<dt><code>&lt;package&gt;_VERSION</code></p>
<dd>full provided version string</p>
<dt><code>&lt;package&gt;_VERSION_MAJOR</code></p>
<dd>major version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_MINOR</code></p>
<dd>minor version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_PATCH</code></p>
<dd>patch version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_TWEAK</code></p>
<dd>tweak version if provided, else 0</p>
<dt><code>&lt;package&gt;_VERSION_COUNT</code></p>
<dd>number of version components, 0 to 4 </p>
<p> and the corresponding package configuration file is loaded. When multiple package configuration files are available whose version files claim compatibility with the version requested it is unspecified which one is chosen. No attempt is made to choose a highest or closest version number. </p>
<p> Config mode provides an elaborate interface and search procedure. Much of the interface is provided for completeness and for use internally by find-modules loaded by Module mode. Most user code should simply call: </p>
<pre>find_package(&lt;package&gt; [major[.minor]] [EXACT] [REQUIRED|QUIET])</pre>
<p>in order to find a package. Package maintainers providing CMake package configuration files are encouraged to name and install them such that the procedure outlined below will find them without requiring use of additional options. </p>
<p> CMake constructs a set of possible installation prefixes for the package. Under each prefix several directories are searched for a configuration file. The tables below show the directories searched. Each entry is meant for installation trees following Windows (W), UNIX (U), or Apple (A) conventions: </p>
<pre>&lt;prefix&gt;/ (W)
&lt;prefix&gt;/(cmake|CMake)/ (W)
&lt;prefix&gt;/&lt;name&gt;*/ (W)
&lt;prefix&gt;/&lt;name&gt;*/(cmake|CMake)/ (W)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib|share)/cmake/&lt;name&gt;*/ (U)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib|share)/&lt;name&gt;*/ (U)
&lt;prefix&gt;/(lib/&lt;arch&gt;|lib|share)/&lt;name&gt;*/(cmake|CMake)/ (U)</pre>
<p>On systems supporting OS X Frameworks and Application Bundles the following directories are searched for frameworks or bundles containing a configuration file: </p>
<pre>&lt;prefix&gt;/&lt;name&gt;.framework/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Resources/CMake/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/CMake/ (A)
&lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/ (A)
&lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/CMake/ (A)</pre>
<p>In all cases the <code>&lt;name&gt;</code> is treated as case-insensitive and corresponds to any of the names specified (<code>&lt;package&gt;</code> or names given by <code>NAMES</code>). Paths with <code>lib/&lt;arch&gt;</code> are enabled if the <code>CMAKE_LIBRARY_ARCHITECTURE</code> variable is set. If <code>PATH_SUFFIXES</code> is specified the suffixes are appended to each (W) or (U) directory entry one-by-one. </p>
<p> This set of directories is intended to work in cooperation with projects that provide configuration files in their installation trees. Directories above marked with (W) are intended for installations on Windows where the prefix may point at the top of an application&#8217;s installation directory. Those marked with (U) are intended for installations on UNIX platforms where the prefix is shared by multiple packages. This is merely a convention, so all (W) and (U) directories are still searched on all platforms. Directories marked with (A) are intended for installations on Apple platforms. The <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference. </p>
<p> The set of installation prefixes is constructed using the following steps. If <code>NO_DEFAULT_PATH</code> is specified all <code>NO_*</code> options are enabled.</p>
<dt>1.</p>
<dd>Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. This can be skipped if <code>NO_CMAKE_PATH</code> is passed: </p>
<pre>CMAKE_PREFIX_PATH
CMAKE_FRAMEWORK_PATH
CMAKE_APPBUNDLE_PATH</pre>
<dt>2.</p>
<dd>Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed: </p>
<pre>&lt;package&gt;_DIR
CMAKE_PREFIX_PATH
CMAKE_FRAMEWORK_PATH
CMAKE_APPBUNDLE_PATH</pre>
<dt>3.</p>
<dd>Search paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option.</p>
<dt>4.</p>
<dd>Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is passed. Path entries ending in <code>/bin</code> or <code>/sbin</code> are automatically converted to their parent directories: </p>
<pre>PATH</pre>
<dt>5.</p>
<dd>Search paths stored in the CMake <i>User Package Registry</i>. This can be skipped if <code>NO_CMAKE_PACKAGE_REGISTRY</code> is passed or by setting the <code>CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY</code> to <code>TRUE</code>. See the <code><a href="/docs/linux/man/7-cmake3-packages/">cmake3-packages</a>(7)</code> manual for details on the user package registry.</p>
<dt>6.</p>
<dd>Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed: </p>
<pre>CMAKE_SYSTEM_PREFIX_PATH
CMAKE_SYSTEM_FRAMEWORK_PATH
CMAKE_SYSTEM_APPBUNDLE_PATH</pre>
<dt>7.</p>
<dd>Search paths stored in the CMake <i>System Package Registry</i>. This can be skipped if <code>NO_CMAKE_SYSTEM_PACKAGE_REGISTRY</code> is passed or by setting the <code>CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY</code> to <code>TRUE</code>. See the <code><a href="/docs/linux/man/7-cmake3-packages/">cmake3-packages</a>(7)</code> manual for details on the system package registry.</p>
<dt>8.</p>
<dd>Search paths specified by the <code>PATHS</code> option. These are typically hard-coded guesses. </p>
<p> The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p> The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p> These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_PACKAGE</code>. This behavior can be manually overridden on a per-call basis using options:</p>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></p>
<dd>Search in the order described above.</p>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable.</p>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre>find_package (&lt;package&gt; PATHS paths... NO_DEFAULT_PATH)
find_package (&lt;package&gt;)</pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> Every non-REQUIRED <code>find_package</code> call can be disabled by setting the <code>CMAKE_DISABLE_FIND_PACKAGE_&lt;PackageName&gt;</code> variable to <code>TRUE</code>. </p>
<p> When loading a find module or package configuration file <code>find_package</code> defines variables to provide information about the call arguments (and restores their original state before returning):</p>
<dt><code>CMAKE_FIND_PACKAGE_NAME</code></p>
<dd>the <code>&lt;package&gt;</code> name which is searched for</p>
<dt><code>&lt;package&gt;_FIND_REQUIRED</code></p>
<dd>true if <code>REQUIRED</code> option was given</p>
<dt><code>&lt;package&gt;_FIND_QUIETLY</code></p>
<dd>true if <code>QUIET</code> option was given</p>
<dt><code>&lt;package&gt;_FIND_VERSION</code></p>
<dd>full requested version string</p>
<dt><code>&lt;package&gt;_FIND_VERSION_MAJOR</code></p>
<dd>major version if requested, else 0</p>
<dt><code>&lt;package&gt;_FIND_VERSION_MINOR</code></p>
<dd>minor version if requested, else 0</p>
<dt><code>&lt;package&gt;_FIND_VERSION_PATCH</code></p>
<dd>patch version if requested, else 0</p>
<dt><code>&lt;package&gt;_FIND_VERSION_TWEAK</code></p>
<dd>tweak version if requested, else 0</p>
<dt><code>&lt;package&gt;_FIND_VERSION_COUNT</code></p>
<dd>number of version components, 0 to 4</p>
<dt><code>&lt;package&gt;_FIND_VERSION_EXACT</code></p>
<dd>true if <code>EXACT</code> option was given</p>
<dt><code>&lt;package&gt;_FIND_COMPONENTS</code></p>
<dd>list of requested components</p>
<dt><code>&lt;package&gt;_FIND_REQUIRED_&lt;c&gt;</code></p>
<dd>true if component <code>&lt;c&gt;</code> is required, false if component <code>&lt;c&gt;</code> is optional </p>
<p> In Module mode the loaded find module is responsible to honor the request detailed by these variables; see the find module for details. In Config mode <code>find_package</code> handles <code>REQUIRED</code>, <code>QUIET</code>, and <code>[version]</code> options automatically but leaves it to the package configuration file to handle components in a way that makes sense for the package. The package configuration file may set <code>&lt;package&gt;_FOUND</code> to false to tell <code>find_package</code> that component requirements are not satisfied. </p>
<p> See the <code>cmake_policy()</code> command documentation for discussion of the <code>NO_POLICY_SCOPE</code> option.</dl>
<h3>find_path</h3>
<p>A short-hand signature is: </p>
<pre>find_path (&lt;VAR&gt; name1 [path1 path2 ...])</pre>
<p>The general signature is: </p>
<pre>find_path (
 &lt;VAR&gt;
 name | NAMES name1 [name2 ...]
 [HINTS path1 [path2 ... ENV var]]
 [PATHS path1 [path2 ... ENV var]]
 [PATH_SUFFIXES suffix1 [suffix2 ...]]
 [DOC &quot;cache documentation string&quot;]
 [NO_DEFAULT_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [NO_CMAKE_PATH]
 [NO_SYSTEM_ENVIRONMENT_PATH]
 [NO_CMAKE_SYSTEM_PATH]
 [CMAKE_FIND_ROOT_PATH_BOTH |
 ONLY_CMAKE_FIND_ROOT_PATH |
 NO_CMAKE_FIND_ROOT_PATH]
 )</pre>
<p>This command is used to find a directory containing the named file. A cache entry named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the file in a directory is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>, and the search will be attempted again the next time find_path is invoked with the same variable. </p>
<p> Options include:</p>
<dl>
<dt><code>NAMES</code></p>
<dd>Specify one or more possible names for the file in a directory. </p>
<p> When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions.</p>
<dt><code>HINTS</code>, <code>PATHS</code></p>
<dd>Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable.</p>
<dt><code>PATH_SUFFIXES</code></p>
<dd>Specify additional subdirectories to check below each directory location otherwise considered.</p>
<dt><code>DOC</code></p>
<dd>Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
<p> If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows:</p>
<dt>1.</p>
<dd>Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. This can be skipped if <code>NO_CMAKE_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>2.</p>
<dd>Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_FRAMEWORK_PATH</code></p>
<dt>3.</p>
<dd>Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option.</p>
<dt>4.</p>
<dd>Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is an argument.</p>
<dt>&bull;</p>
<dd>Directories in <code>INCLUDE</code>. On Windows hosts: <code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;/[s]bin</code> in <code>PATH</code>, and <code>&lt;entry&gt;/include</code> for other entries in <code>PATH</code>, and the directories in <code>PATH</code> itself.</p>
<dt>5.</p>
<dd>Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/include/&lt;arch&gt;</code> if <code>CMAKE_LIBRARY_ARCHITECTURE</code> is set, and <code>&lt;prefix&gt;/include</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_INCLUDE_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_FRAMEWORK_PATH</code></p>
<dt>6.</p>
<dd>Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On OS X the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p> The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p> The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p> These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_INCLUDE</code>. This behavior can be manually overridden on a per-call basis using options:</p>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></p>
<dd>Search in the order described above.</p>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable.</p>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre>find_path (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_path (&lt;VAR&gt; NAMES name)</pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> When searching for frameworks, if the file is specified as <code>A/b.h</code>, then the framework search will look for <code>A.framework/Headers/b.h</code>. If that is found the path will be set to the path to the framework. CMake will convert this to the correct <code>-F</code> option to include the file.</dl>
<h3>find_program</h3>
<p>A short-hand signature is: </p>
<pre>find_program (&lt;VAR&gt; name1 [path1 path2 ...])</pre>
<p>The general signature is: </p>
<pre>find_program (
 &lt;VAR&gt;
 name | NAMES name1 [name2 ...] [NAMES_PER_DIR]
 [HINTS path1 [path2 ... ENV var]]
 [PATHS path1 [path2 ... ENV var]]
 [PATH_SUFFIXES suffix1 [suffix2 ...]]
 [DOC &quot;cache documentation string&quot;]
 [NO_DEFAULT_PATH]
 [NO_CMAKE_ENVIRONMENT_PATH]
 [NO_CMAKE_PATH]
 [NO_SYSTEM_ENVIRONMENT_PATH]
 [NO_CMAKE_SYSTEM_PATH]
 [CMAKE_FIND_ROOT_PATH_BOTH |
 ONLY_CMAKE_FIND_ROOT_PATH |
 NO_CMAKE_FIND_ROOT_PATH]
 )</pre>
<p>This command is used to find a program. A cache entry named by <code>&lt;VAR&gt;</code> is created to store the result of this command. If the program is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be <code>&lt;VAR&gt;-NOTFOUND</code>, and the search will be attempted again the next time find_program is invoked with the same variable. </p>
<p> Options include:</p>
<dl>
<dt><code>NAMES</code></p>
<dd>Specify one or more possible names for the program. </p>
<p> When using this to specify names with and without a version suffix, we recommend specifying the unversioned name first so that locally-built packages can be found before those provided by distributions.</p>
<dt><code>HINTS</code>, <code>PATHS</code></p>
<dd>Specify directories to search in addition to the default locations. The <code>ENV var</code> sub-option reads paths from a system environment variable.</p>
<dt><code>PATH_SUFFIXES</code></p>
<dd>Specify additional subdirectories to check below each directory location otherwise considered.</p>
<dt><code>DOC</code></p>
<dd>Specify the documentation string for the <code>&lt;VAR&gt;</code> cache entry. </p>
<p> If <code>NO_DEFAULT_PATH</code> is specified, then no additional paths are added to the search. If <code>NO_DEFAULT_PATH</code> is not specified, the search process is as follows:</p>
<dt>1.</p>
<dd>Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a <code>-DVAR=value</code>. This can be skipped if <code>NO_CMAKE_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_PROGRAM_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_APPBUNDLE_PATH</code></p>
<dt>2.</p>
<dd>Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if <code>NO_CMAKE_ENVIRONMENT_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_PROGRAM_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_APPBUNDLE_PATH</code></p>
<dt>3.</p>
<dd>Search the paths specified by the <code>HINTS</code> option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the <code>PATHS</code> option.</p>
<dt>4.</p>
<dd>Search the standard system environment variables. This can be skipped if <code>NO_SYSTEM_ENVIRONMENT_PATH</code> is an argument.</p>
<dt>&bull;</p>
<dd><code>PATH</code></p>
<dt>5.</p>
<dd>Search cmake variables defined in the Platform files for the current system. This can be skipped if <code>NO_CMAKE_SYSTEM_PATH</code> is passed.</p>
<dt>&bull;</p>
<dd><code>&lt;prefix&gt;/[s]bin</code> for each <code>&lt;prefix&gt;</code> in <code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_PROGRAM_PATH</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_SYSTEM_APPBUNDLE_PATH</code></p>
<dt>6.</p>
<dd>Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On OS X the <code>CMAKE_FIND_FRAMEWORK</code> and <code>CMAKE_FIND_APPBUNDLE</code> variables determine the order of preference between Apple-style and unix-style package components. </p>
<p> The CMake variable <code>CMAKE_FIND_ROOT_PATH</code> specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. Paths which are descendants of the <code>CMAKE_STAGING_PREFIX</code> are excluded from this re-rooting, because that variable is always a path on the host system. By default the <code>CMAKE_FIND_ROOT_PATH</code> is empty. </p>
<p> The <code>CMAKE_SYSROOT</code> variable can also be used to specify exactly one directory to use as a prefix. Setting <code>CMAKE_SYSROOT</code> also has other effects. See the documentation for that variable for more. </p>
<p> These variables are especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in <code>CMAKE_FIND_ROOT_PATH</code> are searched, then the <code>CMAKE_SYSROOT</code> directory is searched, and then the non-rooted directories will be searched. The default behavior can be adjusted by setting <code>CMAKE_FIND_ROOT_PATH_MODE_PROGRAM</code>. This behavior can be manually overridden on a per-call basis using options:</p>
<dt><code>CMAKE_FIND_ROOT_PATH_BOTH</code></p>
<dd>Search in the order described above.</p>
<dt><code>NO_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Do not use the <code>CMAKE_FIND_ROOT_PATH</code> variable.</p>
<dt><code>ONLY_CMAKE_FIND_ROOT_PATH</code></p>
<dd>Search only the re-rooted directories and directories below <code>CMAKE_STAGING_PREFIX</code>. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the <code>NO_*</code> options: </p>
<pre>find_program (&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
find_program (&lt;VAR&gt; NAMES name)</pre>
<p>Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> When more than one value is given to the <code>NAMES</code> option this command by default will consider one name at a time and search every directory for it. The <code>NAMES_PER_DIR</code> option tells this command to consider one directory at a time and search for all names in it.</dl>
<h3>fltk_wrap_ui</h3>
<p>Create FLTK user interfaces Wrappers. </p>
<pre>fltk_wrap_ui(resultingLibraryName source1
 source2 ... sourceN )</pre>
<p>Produce .h and .cxx files for all the .fl and .fld files listed. The resulting .h and .cxx files will be added to a variable named <code>resultingLibraryName_FLTK_UI_SRCS</code> which should be added to your library.</p>
<h3>foreach</h3>
<p>Evaluate a group of commands for each value in a list. </p>
<pre>foreach(loop_var arg1 arg2 ...)
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
endforeach(loop_var)</pre>
<p>All commands between foreach and the matching endforeach are recorded without being invoked. Once the endforeach is evaluated, the recorded list of commands is invoked once for each argument listed in the original foreach command. Before each iteration of the loop <code>${loop_var}</code> will be set as a variable with the current value in the list. </p>
<pre>foreach(loop_var RANGE total)
foreach(loop_var RANGE start stop [step])</pre>
<p>Foreach can also iterate over a generated range of numbers. There are three types of this iteration:</p>
<dl>
<dt>&bull;</p>
<dd>When specifying single number, the range will have elements 0 to &quot;total&quot;.</p>
<dt>&bull;</p>
<dd>When specifying two numbers, the range will have elements from the first number to the second number.</p>
<dt>&bull;</p>
<dd>The third optional number is the increment used to iterate from the first number to the second number. </p>
<pre>foreach(loop_var IN [LISTS [list1 [...]]]
 [ITEMS [item1 [...]]])</pre>
<p>Iterates over a precise list of items. The <code>LISTS</code> option names list-valued variables to be traversed, including empty elements (an empty string is a zero-length list). (Note macro arguments are not variables.) The <code>ITEMS</code> option ends argument parsing and includes all arguments following it in the iteration.</dl>
<h3>function</h3>
<p>Start recording a function for later invocation as a command: </p>
<pre>function(&lt;name&gt; [arg1 [arg2 [arg3 ...]]])
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
endfunction(&lt;name&gt;)</pre>
<p>Define a function named <code>&lt;name&gt;</code> that takes arguments named <code>arg1</code>, <code>arg2</code>, <code>arg3</code>, (&#8230;). Commands listed after function, but before the matching <code>endfunction()</code>, are not invoked until the function is invoked. When it is invoked, the commands recorded in the function are first modified by replacing formal parameters (<code>${arg1}</code>) with the arguments passed, and then invoked as normal commands. In addition to referencing the formal parameters you can reference the <code>ARGC</code> variable which will be set to the number of arguments passed into the function as well as <code>ARGV0</code>, <code>ARGV1</code>, <code>ARGV2</code>, &#8230; which will have the actual values of the arguments passed in. This facilitates creating functions with optional arguments. Additionally <code>ARGV</code> holds the list of all arguments given to the function and <code>ARGN</code> holds the list of arguments past the last expected argument. Referencing to <code>ARGV#</code> arguments beyond <code>ARGC</code> have undefined behavior. Checking that <code>ARGC</code> is greater than <code>#</code> is the only way to ensure that <code>ARGV#</code> was passed to the function as an extra argument. </p>
<p> A function opens a new scope: see <code>set(var PARENT_SCOPE)</code> for details. </p>
<p> See the <code>cmake_policy()</code> command documentation for the behavior of policies inside functions.</p>
<h3>get_cmake_property</h3>
<p>Get a property of the CMake instance. </p>
<pre>get_cmake_property(VAR property)</pre>
<p>Get a property from the CMake instance. The value of the property is stored in the variable <code>VAR</code>. If the property is not found, <code>VAR</code> will be set to &quot;NOTFOUND&quot;. See the <code><a href="/docs/linux/man/7-cmake3-properties/">cmake3-properties</a>(7)</code> manual for available properties. </p>
<p> See also the more general <code>get_property()</code> command.</p>
<h3>get_directory_property</h3>
<p>Get a property of <code>DIRECTORY</code> scope. </p>
<pre>get_directory_property(&lt;variable&gt; [DIRECTORY &lt;dir&gt;] &lt;prop-name&gt;)</pre>
<p>Store a property of directory scope in the named variable. If the property is not defined the empty-string is returned. The <code>DIRECTORY</code> argument specifies another directory from which to retrieve the property value. The specified directory must have already been traversed by CMake. </p>
<pre>get_directory_property(&lt;variable&gt; [DIRECTORY &lt;dir&gt;]
 DEFINITION &lt;var-name&gt;)</pre>
<p>Get a variable definition from a directory. This form is useful to get a variable definition from another directory. </p>
<p> See also the more general <code>get_property()</code> command.</p>
<h3>get_filename_component</h3>
<p>Get a specific component of a full filename. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>get_filename_component(&lt;VAR&gt; &lt;FileName&gt; &lt;COMP&gt; [CACHE])</pre>
<p>Set <code>&lt;VAR&gt;</code> to a component of <code>&lt;FileName&gt;</code>, where <code>&lt;COMP&gt;</code> is one of: </p>
<pre>DIRECTORY = Directory without file name
NAME = File name without directory
EXT = File name longest extension (.b.c from d/a.b.c)
NAME_WE = File name without directory or longest extension
PATH = Legacy alias for DIRECTORY (use for CMake &lt;= 2.8.11)</pre>
<p>Paths are returned with forward slashes and have no trailing slashes. The longest file extension is always considered. If the optional <code>CACHE</code> argument is specified, the result variable is added to the cache. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>get_filename_component(&lt;VAR&gt; &lt;FileName&gt;
 &lt;COMP&gt; [BASE_DIR &lt;BASE_DIR&gt;]
 [CACHE])</pre>
<p>Set <code>&lt;VAR&gt;</code> to the absolute path of <code>&lt;FileName&gt;</code>, where <code>&lt;COMP&gt;</code> is one of: </p>
<pre>ABSOLUTE = Full path to file
REALPATH = Full path to existing file with symlinks resolved</pre>
<p>If the provided <code>&lt;FileName&gt;</code> is a relative path, it is evaluated relative to the given base directory <code>&lt;BASE_DIR&gt;</code>. If no base directory is provided, the default base directory will be <code>CMAKE_CURRENT_SOURCE_DIR</code>. </p>
<p> Paths are returned with forward slashes and have no trailing slahes. If the optional <code>CACHE</code> argument is specified, the result variable is added to the cache. </p>
<p> <center> &#8212;-<br />
 </center> </p>
<pre>get_filename_component(&lt;VAR&gt; &lt;FileName&gt;
 PROGRAM [PROGRAM_ARGS &lt;ARG_VAR&gt;]
 [CACHE])</pre>
<p>The program in <code>&lt;FileName&gt;</code> will be found in the system search path or left as a full path. If <code>PROGRAM_ARGS</code> is present with <code>PROGRAM</code>, then any command-line arguments present in the <code>&lt;FileName&gt;</code> string are split from the program name and stored in <code>&lt;ARG_VAR&gt;</code>. This is used to separate a program name from its arguments in a command line string.</p>
<h3>get_property</h3>
<p>Get a property. </p>
<pre>get_property(&lt;variable&gt;
 &lt;GLOBAL |
 DIRECTORY [dir] |
 TARGET &lt;target&gt; |
 SOURCE &lt;source&gt; |
 INSTALL &lt;file&gt; |
 TEST &lt;test&gt; |
 CACHE &lt;entry&gt; |
 VARIABLE&gt;
 PROPERTY &lt;name&gt;
 [SET | DEFINED | BRIEF_DOCS | FULL_DOCS])</pre>
<p>Get one property from one object in a scope. The first argument specifies the variable in which to store the result. The second argument determines the scope from which to get the property. It must be one of the following:</p>
<dl>
<dt><code>GLOBAL</code></p>
<dd>Scope is unique and does not accept a name.</p>
<dt><code>DIRECTORY</code></p>
<dd>Scope defaults to the current directory but another directory (already processed by CMake) may be named by full or relative path.</p>
<dt><code>TARGET</code></p>
<dd>Scope must name one existing target.</p>
<dt><code>SOURCE</code></p>
<dd>Scope must name one source file.</p>
<dt><code>INSTALL</code></p>
<dd>Scope must name one installed file path.</p>
<dt><code>TEST</code></p>
<dd>Scope must name one existing test.</p>
<dt><code>CACHE</code></p>
<dd>Scope must name one cache entry.</p>
<dt><code>VARIABLE</code></p>
<dd>Scope is unique and does not accept a name. </p>
<p> The required <code>PROPERTY</code> option is immediately followed by the name of the property to get. If the property is not set an empty value is returned. If the <code>SET</code> option is given the variable is set to a boolean value indicating whether the property has been set. If the <code>DEFINED</code> option is given the variable is set to a boolean value indicating whether the property has been defined such as with the <code>define_property()</code> command. If <code>BRIEF_DOCS</code> or <code>FULL_DOCS</code> is given then the variable is set to a string containing documentation for the requested property. If documentation is requested for a property that has not been defined <code>NOTFOUND</code> is returned.</dl>
<h3>get_source_file_property</h3>
<p>Get a property for a source file. </p>
<pre>get_source_file_property(VAR file property)</pre>
<p>Get a property from a source file. The value of the property is stored in the variable <code>VAR</code>. If the property is not found, <code>VAR</code> will be set to &quot;NOTFOUND&quot;. Use <code>set_source_files_properties()</code> to set property values. Source file properties usually control how the file is built. One property that is always there is <code>LOCATION</code> </p>
<p> See also the more general <code>get_property()</code> command.</p>
<h3>get_target_property</h3>
<p>Get a property from a target. </p>
<pre>get_target_property(VAR target property)</pre>
<p>Get a property from a target. The value of the property is stored in the variable <code>VAR</code>. If the property is not found, <code>VAR</code> will be set to &quot;NOTFOUND&quot;. Use <code>set_target_properties()</code> to set property values. Properties are usually used to control how a target is built, but some query the target instead. This command can get properties for any target so far created. The targets do not need to be in the current <code>CMakeLists.txt</code> file. </p>
<p> See also the more general <code>get_property()</code> command.</p>
<h3>get_test_property</h3>
<p>Get a property of the test. </p>
<pre>get_test_property(test property VAR)</pre>
<p>Get a property from the test. The value of the property is stored in the variable <code>VAR</code>. If the test or property is not found, <code>VAR</code> will be set to &quot;NOTFOUND&quot;. For a list of standard properties you can type <code>cmake &#8211;help-property-list</code>. </p>
<p> See also the more general <code>get_property()</code> command.</p>
<h3>if</h3>
<p>Conditionally execute a group of commands. </p>
<pre>if(expression)
 # then section.
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
elseif(expression2)
 # elseif section.
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
else(expression)
 # else section.
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
endif(expression)</pre>
<p>Evaluates the given expression. If the result is true, the commands in the THEN section are invoked. Otherwise, the commands in the else section are invoked. The elseif and else sections are optional. You may have multiple elseif clauses. Note that the expression in the else and endif clause is optional. Long expressions can be used and there is a traditional order of precedence. Parenthetical expressions are evaluated first followed by unary tests such as <code>EXISTS</code>, <code>COMMAND</code>, and <code>DEFINED</code>. Then any binary tests such as <code>EQUAL</code>, <code>LESS</code>, <code>GREATER</code>, <code>STRLESS</code>, <code>STRGREATER</code>, <code>STREQUAL</code>, and <code>MATCHES</code> will be evaluated. Then boolean <code>NOT</code> operators and finally boolean <code>AND</code> and then <code>OR</code> operators will be evaluated. </p>
<p> Possible expressions are:</p>
<dl>
<dt><code>if(&lt;constant&gt;)</code></p>
<dd>True if the constant is <code>1</code>, <code>ON</code>, <code>YES</code>, <code>TRUE</code>, <code>Y</code>, or a non-zero number. False if the constant is <code>0</code>, <code>OFF</code>, <code>NO</code>, <code>FALSE</code>, <code>N</code>, <code>IGNORE</code>, <code>NOTFOUND</code>, the empty string, or ends in the suffix <code>-NOTFOUND</code>. Named boolean constants are case-insensitive. If the argument is not one of these specific constants, it is treated as a variable or string and the following signature is used.</p>
<dt><code>if(&lt;variable|string&gt;)</code></p>
<dd>True if given a variable that is defined to a value that is not a false constant. False otherwise. (Note macro arguments are not variables.)</p>
<dt><code>if(NOT &lt;expression&gt;)</code></p>
<dd>True if the expression is not true.</p>
<dt><code>if(&lt;expr1&gt; AND &lt;expr2&gt;)</code></p>
<dd>True if both expressions would be considered true individually.</p>
<dt><code>if(&lt;expr1&gt; OR &lt;expr2&gt;)</code></p>
<dd>True if either expression would be considered true individually.</p>
<dt><code>if(COMMAND command-name)</code></p>
<dd>True if the given name is a command, macro or function that can be invoked.</p>
<dt><code>if(POLICY policy-id)</code></p>
<dd>True if the given name is an existing policy (of the form <code>CMP&lt;NNNN&gt;</code>).</p>
<dt><code>if(TARGET target-name)</code></p>
<dd>True if the given name is an existing logical target name created by a call to the <code>add_executable()</code>, <code>add_library()</code>, or <code>add_custom_target()</code> command that has already been invoked (in any directory).</p>
<dt><code>if(TEST test-name)</code></p>
<dd>True if the given name is an existing test name created by the <code>add_test()</code> command.</p>
<dt><code>if(EXISTS path-to-file-or-directory)</code></p>
<dd>True if the named file or directory exists. Behavior is well-defined only for full paths.</p>
<dt><code>if(file1 IS_NEWER_THAN file2)</code></p>
<dd>True if <code>file1</code> is newer than <code>file2</code> or if one of the two files doesn&#8217;t exist. Behavior is well-defined only for full paths. If the file time stamps are exactly the same, an <code>IS_NEWER_THAN</code> comparison returns true, so that any dependent build operations will occur in the event of a tie. This includes the case of passing the same file name for both file1 and file2.</p>
<dt><code>if(IS_DIRECTORY path-to-directory)</code></p>
<dd>True if the given name is a directory. Behavior is well-defined only for full paths.</p>
<dt><code>if(IS_SYMLINK file-name)</code></p>
<dd>True if the given name is a symbolic link. Behavior is well-defined only for full paths.</p>
<dt><code>if(IS_ABSOLUTE path)</code></p>
<dd>True if the given path is an absolute path.</p>
<dt><code>if(&lt;variable|string&gt; MATCHES regex)</code></p>
<dd>True if the given string or variable&#8217;s value matches the given regular expression.</p>
<dt><code>if(&lt;variable|string&gt; LESS &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is a valid number and less than that on the right.</p>
<dt><code>if(&lt;variable|string&gt; GREATER &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is a valid number and greater than that on the right.</p>
<dt><code>if(&lt;variable|string&gt; EQUAL &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is a valid number and equal to that on the right.</p>
<dt><code>if(&lt;variable|string&gt; STRLESS &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is lexicographically less than the string or variable on the right.</p>
<dt><code>if(&lt;variable|string&gt; STRGREATER &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is lexicographically greater than the string or variable on the right.</p>
<dt><code>if(&lt;variable|string&gt; STREQUAL &lt;variable|string&gt;)</code></p>
<dd>True if the given string or variable&#8217;s value is lexicographically equal to the string or variable on the right.</p>
<dt><code>if(&lt;variable|string&gt; VERSION_LESS &lt;variable|string&gt;)</code></p>
<dd>Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>).</p>
<dt><code>if(&lt;variable|string&gt; VERSION_EQUAL &lt;variable|string&gt;)</code></p>
<dd>Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>).</p>
<dt><code>if(&lt;variable|string&gt; VERSION_GREATER &lt;variable|string&gt;)</code></p>
<dd>Component-wise integer version number comparison (version format is <code>major[.minor[.patch[.tweak]]]</code>).</p>
<dt><code>if(&lt;variable|string&gt; IN_LIST &lt;variable&gt;)</code></p>
<dd>True if the given element is contained in the named list variable.</p>
<dt><code>if(DEFINED &lt;variable&gt;)</code></p>
<dd>True if the given variable is defined. It does not matter if the variable is true or false just if it has been set. (Note macro arguments are not variables.)</p>
<dt><code>if((expression) AND (expression OR (expression)))</code></p>
<dd>The expressions inside the parenthesis are evaluated first and then the remaining expression is evaluated as in the previous examples. Where there are nested parenthesis the innermost are evaluated as part of evaluating the expression that contains them. </p>
<p> The if command was written very early in CMake&#8217;s history, predating the <code>${}</code> variable evaluation syntax, and for convenience evaluates variables named by its arguments as shown in the above signatures. Note that normal variable evaluation with <code>${}</code> applies before the if command even receives the arguments. Therefore code like: </p>
<pre>set(var1 OFF)
set(var2 &quot;var1&quot;)
if(${var2})</pre>
<p>appears to the if command as: </p>
<pre>if(var1)</pre>
<p>and is evaluated according to the <code>if(&lt;variable&gt;)</code> case documented above. The result is <code>OFF</code> which is false. However, if we remove the <code>${}</code> from the example then the command sees: </p>
<pre>if(var2)</pre>
<p>which is true because <code>var2</code> is defined to &quot;var1&quot; which is not a false constant. </p>
<p> Automatic evaluation applies in the other cases whenever the above-documented signature accepts <code>&lt;variable|string&gt;</code>:</p>
<dt>&bull;</p>
<dd>The left hand argument to <code>MATCHES</code> is first checked to see if it is a defined variable, if so the variable&#8217;s value is used, otherwise the original value is used.</p>
<dt>&bull;</p>
<dd>If the left hand argument to <code>MATCHES</code> is missing it returns false without error</p>
<dt>&bull;</p>
<dd>Both left and right hand arguments to <code>LESS</code>, <code>GREATER</code>, and <code>EQUAL</code> are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used.</p>
<dt>&bull;</p>
<dd>Both left and right hand arguments to <code>STRLESS</code>, <code>STREQUAL</code>, and <code>STRGREATER</code> are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used.</p>
<dt>&bull;</p>
<dd>Both left and right hand arguments to <code>VERSION_LESS</code>, <code>VERSION_EQUAL</code>, and <code>VERSION_GREATER</code> are independently tested to see if they are defined variables, if so their defined values are used otherwise the original value is used.</p>
<dt>&bull;</p>
<dd>The right hand argument to <code>NOT</code> is tested to see if it is a boolean constant, if so the value is used, otherwise it is assumed to be a variable and it is dereferenced.</p>
<dt>&bull;</p>
<dd>The left and right hand arguments to <code>AND</code> and <code>OR</code> are independently tested to see if they are boolean constants, if so they are used as such, otherwise they are assumed to be variables and are dereferenced. </p>
<p> To prevent ambiguity, potential variable or keyword names can be specified in a <i>Quoted Argument</i> or a <i>Bracket Argument</i>. A quoted or bracketed variable or keyword will be interpreted as a string and not dereferenced or interpreted. See policy <code>CMP0054</code>.</dl>
<h3>include_directories</h3>
<p>Add include directories to the build. </p>
<pre>include_directories([AFTER|BEFORE] [SYSTEM] dir1 [dir2 ...])</pre>
<p>Add the given directories to those the compiler uses to search for include files. Relative paths are interpreted as relative to the current source directory. </p>
<p> The include directories are added to the <code>INCLUDE_DIRECTORIES</code> directory property for the current <code>CMakeLists</code> file. They are also added to the <code>INCLUDE_DIRECTORIES</code> target property for each target in the current <code>CMakeLists</code> file. The target property values are the ones used by the generators. </p>
<p> By default the directories specified are appended onto the current list of directories. This default behavior can be changed by setting <code>CMAKE_INCLUDE_DIRECTORIES_BEFORE</code> to <code>ON</code>. By using <code>AFTER</code> or <code>BEFORE</code> explicitly, you can select between appending and prepending, independent of the default. </p>
<p> If the <code>SYSTEM</code> option is given, the compiler will be told the directories are meant as system include directories on some platforms. Signalling this setting might achieve effects such as the compiler skipping warnings, or these fixed-install system files not being considered in dependency calculations &#8211; see compiler docs. </p>
<p> Arguments to <code>include_directories</code> may use &quot;generator expressions&quot; with the syntax &quot;$&lt;&#8230;&gt;&quot;. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>include_external_msproject</h3>
<p>Include an external Microsoft project file in a workspace. </p>
<pre>include_external_msproject(projectname location
 [TYPE projectTypeGUID]
 [GUID projectGUID]
 [PLATFORM platformName]
 dep1 dep2 ...)</pre>
<p>Includes an external Microsoft project in the generated workspace file. Currently does nothing on UNIX. This will create a target named [projectname]. This can be used in the <code>add_dependencies()</code> command to make things depend on the external project. </p>
<p> <code>TYPE</code>, <code>GUID</code> and <code>PLATFORM</code> are optional parameters that allow one to specify the type of project, id (GUID) of the project and the name of the target platform. This is useful for projects requiring values other than the default (e.g. WIX projects).</p>
<h3>include_regular_expression</h3>
<p>Set the regular expression used for dependency checking. </p>
<pre>include_regular_expression(regex_match [regex_complain])</pre>
<p>Set the regular expressions used in dependency checking. Only files matching <code>regex_match</code> will be traced as dependencies. Only files matching <code>regex_complain</code> will generate warnings if they cannot be found (standard header paths are not searched). The defaults are: </p>
<pre>regex_match = &quot;^.*$&quot; (match everything)
regex_complain = &quot;^$&quot; (match empty string only)</pre>
<h3>include</h3>
<p>Load and run CMake code from a file or module. </p>
<pre>include(&lt;file|module&gt; [OPTIONAL] [RESULT_VARIABLE &lt;VAR&gt;]
 [NO_POLICY_SCOPE])</pre>
<p>Load and run CMake code from the file given. Variable reads and writes access the scope of the caller (dynamic scoping). If <code>OPTIONAL</code> is present, then no error is raised if the file does not exist. If <code>RESULT_VARIABLE</code> is given the variable will be set to the full filename which has been included or NOTFOUND if it failed. </p>
<p> If a module is specified instead of a file, the file with name &lt;modulename&gt;.cmake is searched first in <code>CMAKE_MODULE_PATH</code>, then in the CMake module directory. There is one exception to this: if the file which calls <code>include()</code> is located itself in the CMake module directory, then first the CMake module directory is searched and <code>CMAKE_MODULE_PATH</code> afterwards. See also policy <code>CMP0017</code>. </p>
<p> See the <code>cmake_policy()</code> command documentation for discussion of the <code>NO_POLICY_SCOPE</code> option.</p>
<h3>install</h3>
<p>Specify rules to run at install time.</p>
<h3>Introduction</h3>
<p>This command generates installation rules for a project. Rules specified by calls to this command within a source directory are executed in order during installation. The order across directories is not defined. </p>
<p> There are multiple signatures for this command. Some of them define installation options for files and targets. Options common to multiple signatures are covered here but they are valid only for signatures that specify them. The common options are:</p>
<dl>
<dt><code>DESTINATION</code></p>
<dd>Specify the directory on disk to which a file will be installed. If a full path (with a leading slash or drive letter) is given it is used directly. If a relative path is given it is interpreted relative to the value of the <code>CMAKE_INSTALL_PREFIX</code> variable. The prefix can be relocated at install time using the <code>DESTDIR</code> mechanism explained in the <code>CMAKE_INSTALL_PREFIX</code> variable documentation.</p>
<dt><code>PERMISSIONS</code></p>
<dd>Specify permissions for installed files. Valid permissions are <code>OWNER_READ</code>, <code>OWNER_WRITE</code>, <code>OWNER_EXECUTE</code>, <code>GROUP_READ</code>, <code>GROUP_WRITE</code>, <code>GROUP_EXECUTE</code>, <code>WORLD_READ</code>, <code>WORLD_WRITE</code>, <code>WORLD_EXECUTE</code>, <code>SETUID</code>, and <code>SETGID</code>. Permissions that do not make sense on certain platforms are ignored on those platforms.</p>
<dt><code>CONFIGURATIONS</code></p>
<dd>Specify a list of build configurations for which the install rule applies (Debug, Release, etc.).</p>
<dt><code>COMPONENT</code></p>
<dd>Specify an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;. During component-specific installation only install rules associated with the given component name will be executed. During a full installation all components are installed unless marked with <code>EXCLUDE_FROM_ALL</code>. If <code>COMPONENT</code> is not provided a default component &quot;Unspecified&quot; is created. The default component name may be controlled with the <code>CMAKE_INSTALL_DEFAULT_COMPONENT_NAME</code> variable.</p>
<dt><code>EXCLUDE_FROM_ALL</code></p>
<dd>Specify that the file is excluded from a full installation and only installed as part of a component-specific installation</p>
<dt><code>RENAME</code></p>
<dd>Specify a name for an installed file that may be different from the original file. Renaming is allowed only when a single file is installed by the command.</p>
<dt><code>OPTIONAL</code></p>
<dd>Specify that it is not an error if the file to be installed does not exist. </p>
<p> Command signatures that install files may print messages during installation. Use the <code>CMAKE_INSTALL_MESSAGE</code> variable to control which messages are printed.</dl>
<h3>Installing Targets</h3>
<pre>install(TARGETS targets... [EXPORT &lt;export-name&gt;]
 [[ARCHIVE|LIBRARY|RUNTIME|FRAMEWORK|BUNDLE|
 PRIVATE_HEADER|PUBLIC_HEADER|RESOURCE]
 [DESTINATION &lt;dir&gt;]
 [PERMISSIONS permissions...]
 [CONFIGURATIONS [Debug|Release|...]]
 [COMPONENT &lt;component&gt;]
 [OPTIONAL] [EXCLUDE_FROM_ALL]
 [NAMELINK_ONLY|NAMELINK_SKIP]
 ] [...]
 [INCLUDES DESTINATION [&lt;dir&gt; ...]]
 )</pre>
<p>The <code>TARGETS</code> form specifies rules for installing targets from a project. There are five kinds of target files that may be installed: <code>ARCHIVE</code>, <code>LIBRARY</code>, <code>RUNTIME</code>, <code>FRAMEWORK</code>, and <code>BUNDLE</code>. Executables are treated as <code>RUNTIME</code> targets, except that those marked with the <code>MACOSX_BUNDLE</code> property are treated as <code>BUNDLE</code> targets on OS X. Static libraries are always treated as <code>ARCHIVE</code> targets. Module libraries are always treated as <code>LIBRARY</code> targets. For non-DLL platforms shared libraries are treated as <code>LIBRARY</code> targets, except that those marked with the <code>FRAMEWORK</code> property are treated as <code>FRAMEWORK</code> targets on OS X. For DLL platforms the DLL part of a shared library is treated as a <code>RUNTIME</code> target and the corresponding import library is treated as an <code>ARCHIVE</code> target. All Windows-based systems including Cygwin are DLL platforms. The <code>ARCHIVE</code>, <code>LIBRARY</code>, <code>RUNTIME</code>, and <code>FRAMEWORK</code> arguments change the type of target to which the subsequent properties apply. If none is given the installation properties apply to all target types. If only one is given then only targets of that type will be installed (which can be used to install just a DLL or just an import library). </p>
<p> The <code>PRIVATE_HEADER</code>, <code>PUBLIC_HEADER</code>, and <code>RESOURCE</code> arguments cause subsequent properties to be applied to installing a <code>FRAMEWORK</code> shared library target&#8217;s associated files on non-Apple platforms. Rules defined by these arguments are ignored on Apple platforms because the associated files are installed into the appropriate locations inside the framework folder. See documentation of the <code>PRIVATE_HEADER</code>, <code>PUBLIC_HEADER</code>, and <code>RESOURCE</code> target properties for details. </p>
<p> Either <code>NAMELINK_ONLY</code> or <code>NAMELINK_SKIP</code> may be specified as a <code>LIBRARY</code> option. On some platforms a versioned shared library has a symbolic link such as: </p>
<pre>lib&lt;name&gt;.so -&gt; lib&lt;name&gt;.so.1</pre>
<p>where <code>lib&lt;name&gt;.so.1</code> is the soname of the library and <code>lib&lt;name&gt;.so</code> is a &quot;namelink&quot; allowing linkers to find the library when given <code>-l&lt;name&gt;</code>. The <code>NAMELINK_ONLY</code> option causes installation of only the namelink when a library target is installed. The <code>NAMELINK_SKIP</code> option causes installation of library files other than the namelink when a library target is installed. When neither option is given both portions are installed. On platforms where versioned shared libraries do not have namelinks or when a library is not versioned the <code>NAMELINK_SKIP</code> option installs the library and the <code>NAMELINK_ONLY</code> option installs nothing. See the <code>VERSION</code> and <code>SOVERSION</code> target properties for details on creating versioned shared libraries. </p>
<p> The <code>INCLUDES DESTINATION</code> specifies a list of directories which will be added to the <code>INTERFACE_INCLUDE_DIRECTORIES</code> target property of the <code>&lt;targets&gt;</code> when exported by the <code>install(EXPORT)</code> command. If a relative path is specified, it is treated as relative to the <code>$&lt;INSTALL_PREFIX&gt;</code>. This is independent of the rest of the argument groups and does not actually install anything. </p>
<p> One or more groups of properties may be specified in a single call to the <code>TARGETS</code> form of this command. A target may be installed more than once to different locations. Consider hypothetical targets <code>myExe</code>, <code>mySharedLib</code>, and <code>myStaticLib</code>. The code: </p>
<pre>install(TARGETS myExe mySharedLib myStaticLib
 RUNTIME DESTINATION bin
 LIBRARY DESTINATION lib
 ARCHIVE DESTINATION lib/static)
install(TARGETS mySharedLib DESTINATION /some/full/path)</pre>
<p>will install <code>myExe</code> to <code>&lt;prefix&gt;/bin</code> and <code>myStaticLib</code> to <code>&lt;prefix&gt;/lib/static</code>. On non-DLL platforms <code>mySharedLib</code> will be installed to <code>&lt;prefix&gt;/lib</code> and <code>/some/full/path</code>. On DLL platforms the <code>mySharedLib</code> DLL will be installed to <code>&lt;prefix&gt;/bin</code> and <code>/some/full/path</code> and its import library will be installed to <code>&lt;prefix&gt;/lib/static</code> and <code>/some/full/path</code>. </p>
<p> The <code>EXPORT</code> option associates the installed target files with an export called <code>&lt;export-name&gt;</code>. It must appear before any <code>RUNTIME</code>, <code>LIBRARY</code>, or <code>ARCHIVE</code> options. To actually install the export file itself, call <code>install(EXPORT)</code>, documented below. </p>
<p> Installing a target with the <code>EXCLUDE_FROM_ALL</code> target property set to <code>TRUE</code> has undefined behavior. </p>
<p> The install destination given to the target install <code>DESTINATION</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Installing Files</h3>
<pre>install(&lt;FILES|PROGRAMS&gt; files... DESTINATION &lt;dir&gt;
 [PERMISSIONS permissions...]
 [CONFIGURATIONS [Debug|Release|...]]
 [COMPONENT &lt;component&gt;]
 [RENAME &lt;name&gt;] [OPTIONAL] [EXCLUDE_FROM_ALL])</pre>
<p>The <code>FILES</code> form specifies rules for installing files for a project. File names given as relative paths are interpreted with respect to the current source directory. Files installed by this form are by default given permissions <code>OWNER_WRITE</code>, <code>OWNER_READ</code>, <code>GROUP_READ</code>, and <code>WORLD_READ</code> if no <code>PERMISSIONS</code> argument is given. </p>
<p> The <code>PROGRAMS</code> form is identical to the <code>FILES</code> form except that the default permissions for the installed file also include <code>OWNER_EXECUTE</code>, <code>GROUP_EXECUTE</code>, and <code>WORLD_EXECUTE</code>. This form is intended to install programs that are not targets, such as shell scripts. Use the <code>TARGETS</code> form to install targets built within the project. </p>
<p> The list of <code>files&#8230;</code> given to <code>FILES</code> or <code>PROGRAMS</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. However, if any item begins in a generator expression it must evaluate to a full path. </p>
<p> The install destination given to the files install <code>DESTINATION</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Installing Directories</h3>
<pre>install(DIRECTORY dirs... DESTINATION &lt;dir&gt;
 [FILE_PERMISSIONS permissions...]
 [DIRECTORY_PERMISSIONS permissions...]
 [USE_SOURCE_PERMISSIONS] [OPTIONAL] [MESSAGE_NEVER]
 [CONFIGURATIONS [Debug|Release|...]]
 [COMPONENT &lt;component&gt;] [EXCLUDE_FROM_ALL]
 [FILES_MATCHING]
 [[PATTERN &lt;pattern&gt; | REGEX &lt;regex&gt;]
 [EXCLUDE] [PERMISSIONS permissions...]] [...])</pre>
<p>The <code>DIRECTORY</code> form installs contents of one or more directories to a given destination. The directory structure is copied verbatim to the destination. The last component of each directory name is appended to the destination directory but a trailing slash may be used to avoid this because it leaves the last component empty. Directory names given as relative paths are interpreted with respect to the current source directory. If no input directory names are given the destination directory will be created but nothing will be installed into it. The <code>FILE_PERMISSIONS</code> and <code>DIRECTORY_PERMISSIONS</code> options specify permissions given to files and directories in the destination. If <code>USE_SOURCE_PERMISSIONS</code> is specified and <code>FILE_PERMISSIONS</code> is not, file permissions will be copied from the source directory structure. If no permissions are specified files will be given the default permissions specified in the <code>FILES</code> form of the command, and the directories will be given the default permissions specified in the <code>PROGRAMS</code> form of the command. </p>
<p> The <code>MESSAGE_NEVER</code> option disables file installation status output. </p>
<p> Installation of directories may be controlled with fine granularity using the <code>PATTERN</code> or <code>REGEX</code> options. These &quot;match&quot; options specify a globbing pattern or regular expression to match directories or files encountered within input directories. They may be used to apply certain options (see below) to a subset of the files and directories encountered. The full path to each input file or directory (with forward slashes) is matched against the expression. A <code>PATTERN</code> will match only complete file names: the portion of the full path matching the pattern must occur at the end of the file name and be preceded by a slash. A <code>REGEX</code> will match any portion of the full path but it may use <code>/</code> and <code>$</code> to simulate the <code>PATTERN</code> behavior. By default all files and directories are installed whether or not they are matched. The <code>FILES_MATCHING</code> option may be given before the first match option to disable installation of files (but not directories) not matched by any expression. For example, the code </p>
<pre>install(DIRECTORY src/ DESTINATION include/myproj
 FILES_MATCHING PATTERN &quot;*.h&quot;)</pre>
<p>will extract and install header files from a source tree. </p>
<p> Some options may follow a <code>PATTERN</code> or <code>REGEX</code> expression and are applied only to files or directories matching them. The <code>EXCLUDE</code> option will skip the matched file or directory. The <code>PERMISSIONS</code> option overrides the permissions setting for the matched file or directory. For example the code </p>
<pre>install(DIRECTORY icons scripts/ DESTINATION share/myproj
 PATTERN &quot;CVS&quot; EXCLUDE
 PATTERN &quot;scripts/*&quot;
 PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
 GROUP_EXECUTE GROUP_READ)</pre>
<p>will install the <code>icons</code> directory to <code>share/myproj/icons</code> and the <code>scripts</code> directory to <code>share/myproj</code>. The icons will get default file permissions, the scripts will be given specific permissions, and any <code>CVS</code> directories will be excluded. </p>
<p> The list of <code>dirs&#8230;</code> given to <code>DIRECTORY</code> and the install destination given to the directory install <code>DESTINATION</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions.</p>
<h3>Custom Installation Logic</h3>
<pre>install([[SCRIPT &lt;file&gt;] [CODE &lt;code&gt;]]
 [COMPONENT &lt;component&gt;] [EXCLUDE_FROM_ALL] [...])</pre>
<p>The <code>SCRIPT</code> form will invoke the given CMake script files during installation. If the script file name is a relative path it will be interpreted with respect to the current source directory. The <code>CODE</code> form will invoke the given CMake code during installation. Code is specified as a single argument inside a double-quoted string. For example, the code </p>
<pre>install(CODE &quot;MESSAGE(\&quot;Sample install message.\&quot;)&quot;)</pre>
<p>will print a message during installation.</p>
<h3>Installing Exports</h3>
<pre>install(EXPORT &lt;export-name&gt; DESTINATION &lt;dir&gt;
 [NAMESPACE &lt;namespace&gt;] [FILE &lt;name&gt;.cmake]
 [PERMISSIONS permissions...]
 [CONFIGURATIONS [Debug|Release|...]]
 [EXPORT_LINK_INTERFACE_LIBRARIES]
 [COMPONENT &lt;component&gt;]
 [EXCLUDE_FROM_ALL])</pre>
<p>The <code>EXPORT</code> form generates and installs a CMake file containing code to import targets from the installation tree into another project. Target installations are associated with the export <code>&lt;export-name&gt;</code> using the <code>EXPORT</code> option of the <code>install(TARGETS)</code> signature documented above. The <code>NAMESPACE</code> option will prepend <code>&lt;namespace&gt;</code> to the target names as they are written to the import file. By default the generated file will be called <code>&lt;export-name&gt;.cmake</code> but the <code>FILE</code> option may be used to specify a different name. The value given to the <code>FILE</code> option must be a file name with the <code>.cmake</code> extension. If a <code>CONFIGURATIONS</code> option is given then the file will only be installed when one of the named configurations is installed. Additionally, the generated import file will reference only the matching target configurations. The <code>EXPORT_LINK_INTERFACE_LIBRARIES</code> keyword, if present, causes the contents of the properties matching <code>(IMPORTED_)?LINK_INTERFACE_LIBRARIES(_&lt;CONFIG&gt;)?</code> to be exported, when policy <code>CMP0022</code> is <code>NEW</code>. If a <code>COMPONENT</code> option is specified that does not match that given to the targets associated with <code>&lt;export-name&gt;</code> the behavior is undefined. If a library target is included in the export but a target to which it links is not included the behavior is unspecified. </p>
<p> The <code>EXPORT</code> form is useful to help outside projects use targets built and installed by the current project. For example, the code </p>
<pre>install(TARGETS myexe EXPORT myproj DESTINATION bin)
install(EXPORT myproj NAMESPACE mp_ DESTINATION lib/myproj)</pre>
<p>will install the executable myexe to <code>&lt;prefix&gt;/bin</code> and code to import it in the file <code>&lt;prefix&gt;/lib/myproj/myproj.cmake</code>. An outside project may load this file with the include command and reference the <code>myexe</code> executable from the installation tree using the imported target name <code>mp_myexe</code> as if the target were built in its own tree. </p>
<p> <code>NOTE:</code> This command supercedes the <code>install_targets()</code> command and the <code>PRE_INSTALL_SCRIPT</code> and <code>POST_INSTALL_SCRIPT</code> target properties. It also replaces the <code>FILES</code> forms of the <code>install_files()</code> and <code>install_programs()</code> commands. The processing order of these install rules relative to those generated by <code>install_targets()</code>, <code>install_files()</code>, and <code>install_programs()</code> commands is not defined.</p>
<h3>link_directories</h3>
<p>Specify directories in which the linker will look for libraries. </p>
<pre>link_directories(directory1 directory2 ...)</pre>
<p>Specify the paths in which the linker should search for libraries. The command will apply only to targets created after it is called. Relative paths given to this command are interpreted as relative to the current source directory, see <code>CMP0015</code>. </p>
<p> Note that this command is rarely necessary. Library locations returned by <code>find_package()</code> and <code>find_library()</code> are absolute paths. Pass these absolute library file paths directly to the <code>target_link_libraries()</code> command. CMake will ensure the linker finds them.</p>
<h3>link_libraries</h3>
<p>Link libraries to all targets added later. </p>
<pre>link_libraries([item1 [item2 [...]]]
 [[debug|optimized|general] &lt;item&gt;] ...)</pre>
<p>Specify libraries or flags to use when linking any targets created later in the current directory or below by commands such as <code>add_executable()</code> or <code>add_library()</code>. See the <code>target_link_libraries()</code> command for meaning of arguments. </p>
<p> <code>NOTE:</code> The <code>target_link_libraries()</code> command should be preferred whenever possible. Library dependencies are chained automatically, so directory-wide specification of link libraries is rarely needed.</p>
<h3>list</h3>
<p>List operations. </p>
<pre>list(LENGTH &lt;list&gt; &lt;output variable&gt;)
list(GET &lt;list&gt; &lt;element index&gt; [&lt;element index&gt; ...]
 &lt;output variable&gt;)
list(APPEND &lt;list&gt; [&lt;element&gt; ...])
list(FILTER &lt;list&gt; &lt;INCLUDE|EXCLUDE&gt; REGEX &lt;regular_expression&gt;)
list(FIND &lt;list&gt; &lt;value&gt; &lt;output variable&gt;)
list(INSERT &lt;list&gt; &lt;element_index&gt; &lt;element&gt; [&lt;element&gt; ...])
list(REMOVE_ITEM &lt;list&gt; &lt;value&gt; [&lt;value&gt; ...])
list(REMOVE_AT &lt;list&gt; &lt;index&gt; [&lt;index&gt; ...])
list(REMOVE_DUPLICATES &lt;list&gt;)
list(REVERSE &lt;list&gt;)
list(SORT &lt;list&gt;)</pre>
<p><code>LENGTH</code> will return a given list&#8217;s length. </p>
<p> <code>GET</code> will return list of elements specified by indices from the list. </p>
<p> <code>APPEND</code> will append elements to the list. </p>
<p> <code>FILTER</code> will include or remove items from the list that match the mode&#8217;s pattern. In <code>REGEX</code> mode, items will be matched against the given regular expression. For more information on regular expressions see also the <code>string()</code> command. </p>
<p> <code>FIND</code> will return the index of the element specified in the list or -1 if it wasn&#8217;t found. </p>
<p> <code>INSERT</code> will insert elements to the list to the specified location. </p>
<p> <code>REMOVE_AT</code> and <code>REMOVE_ITEM</code> will remove items from the list. The difference is that <code>REMOVE_ITEM</code> will remove the given items, while <code>REMOVE_AT</code> will remove the items at the given indices. </p>
<p> <code>REMOVE_DUPLICATES</code> will remove duplicated items in the list. </p>
<p> <code>REVERSE</code> reverses the contents of the list in-place. </p>
<p> <code>SORT</code> sorts the list in-place alphabetically. </p>
<p> The list subcommands <code>APPEND</code>, <code>INSERT</code>, <code>FILTER</code>, <code>REMOVE_AT</code>, <code>REMOVE_ITEM</code>, <code>REMOVE_DUPLICATES</code>, <code>REVERSE</code> and <code>SORT</code> may create new values for the list within the current CMake variable scope. Similar to the <code>set()</code> command, the LIST command creates new variable values in the current scope, even if the list itself is actually defined in a parent scope. To propagate the results of these operations upwards, use <code>set()</code> with <code>PARENT_SCOPE</code>, <code>set()</code> with <code>CACHE INTERNAL</code>, or some other means of value propagation. </p>
<p> NOTES: A list in cmake is a <code>;</code> separated group of strings. To create a list the set command can be used. For example, <code>set(var a b c d e)</code> creates a list with <code>a;b;c;d;e</code>, and <code>set(var &quot;a b c d e&quot;)</code> creates a string or a list with one item in it. (Note macro arguments are not variables, and therefore cannot be used in LIST commands.) </p>
<p> When specifying index values, if <code>&lt;element index&gt;</code> is 0 or greater, it is indexed from the beginning of the list, with 0 representing the first list element. If <code>&lt;element index&gt;</code> is -1 or lesser, it is indexed from the end of the list, with -1 representing the last list element. Be careful when counting with negative indices: they do not start from 0. -0 is equivalent to 0, the first list element.</p>
<h3>load_cache</h3>
<p>Load in the values from another project&#8217;s CMake cache. </p>
<pre>load_cache(pathToCacheFile READ_WITH_PREFIX
 prefix entry1...)</pre>
<p>Read the cache and store the requested entries in variables with their name prefixed with the given prefix. This only reads the values, and does not create entries in the local project&#8217;s cache. </p>
<pre>load_cache(pathToCacheFile [EXCLUDE entry1...]
 [INCLUDE_INTERNALS entry1...])</pre>
<p>Load in the values from another cache and store them in the local project&#8217;s cache as internal entries. This is useful for a project that depends on another project built in a different tree. <code>EXCLUDE</code> option can be used to provide a list of entries to be excluded. <code>INCLUDE_INTERNALS</code> can be used to provide a list of internal entries to be included. Normally, no internal entries are brought in. Use of this form of the command is strongly discouraged, but it is provided for backward compatibility.</p>
<h3>macro</h3>
<p>Start recording a macro for later invocation as a command: </p>
<pre>macro(&lt;name&gt; [arg1 [arg2 [arg3 ...]]])
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
endmacro(&lt;name&gt;)</pre>
<p>Define a macro named <code>&lt;name&gt;</code> that takes arguments named <code>arg1</code>, <code>arg2</code>, <code>arg3</code>, (&#8230;). Commands listed after macro, but before the matching <code>endmacro()</code>, are not invoked until the macro is invoked. When it is invoked, the commands recorded in the macro are first modified by replacing formal parameters (<code>${arg1}</code>) with the arguments passed, and then invoked as normal commands. In addition to referencing the formal parameters you can reference the values <code>${ARGC}</code> which will be set to the number of arguments passed into the function as well as <code>${ARGV0}</code>, <code>${ARGV1}</code>, <code>${ARGV2}</code>, This facilitates creating macros with optional arguments. Additionally <code>${ARGV}</code> holds the list of all arguments given to the macro and <code>${ARGN}</code> holds the list of arguments past the last expected argument. Referencing to <code>${ARGV#}</code> arguments beyond <code>${ARGC}</code> have undefined behavior. Checking that <code>${ARGC}</code> is greater than <code>#</code> is the only way to ensure that <code>${ARGV#}</code> was passed to the function as an extra argument. </p>
<p> See the <code>cmake_policy()</code> command documentation for the behavior of policies inside macros.</p>
<h3>Macro Argument Caveats</h3>
<p>Note that the parameters to a macro and values such as <code>ARGN</code> are not variables in the usual CMake sense. They are string replacements much like the C preprocessor would do with a macro. Therefore you will NOT be able to use commands like: </p>
<pre>if(ARGV1) # ARGV1 is not a variable
if(DEFINED ARGV2) # ARGV2 is not a variable
if(ARGC GREATER 2) # ARGC is not a variable
foreach(loop_var IN LISTS ARGN) # ARGN is not a variable</pre>
<p>In the first case, you can use <code>if(${ARGV1})</code>. In the second and third case, the proper way to check if an optional variable was passed to the macro is to use <code>if(${ARGC} GREATER 2)</code>. In the last case, you can use <code>foreach(loop_var ${ARGN})</code> but this will skip empty arguments. If you need to include them, you can use: </p>
<pre>set(list_var &quot;${ARGN}&quot;)
foreach(loop_var IN LISTS list_var)</pre>
<p>Note that if you have a variable with the same name in the scope from which the macro is called, using unreferenced names will use the existing variable instead of the arguments. For example: </p>
<pre>macro(_BAR)
 foreach(arg IN LISTS ARGN)
 [...]
 endforeach()
endmacro()
function(_FOO)
 _bar(x y z)
endfunction()
_foo(a b c)</pre>
<p>Will loop over <code>a;b;c</code> and not over <code>x;y;z</code> as one might be expecting. If you want true CMake variables and/or better CMake scope control you should look at the function command.</p>
<h3>mark_as_advanced</h3>
<p>Mark cmake cached variables as advanced. </p>
<pre>mark_as_advanced([CLEAR|FORCE] VAR [VAR2 ...])</pre>
<p>Mark the named cached variables as advanced. An advanced variable will not be displayed in any of the cmake GUIs unless the show advanced option is on. If <code>CLEAR</code> is the first argument advanced variables are changed back to unadvanced. If <code>FORCE</code> is the first argument, then the variable is made advanced. If neither <code>FORCE</code> nor <code>CLEAR</code> is specified, new values will be marked as advanced, but if the variable already has an advanced/non-advanced state, it will not be changed. </p>
<p> It does nothing in script mode.</p>
<h3>math</h3>
<p>Mathematical expressions. </p>
<pre>math(EXPR &lt;output variable&gt; &lt;math expression&gt;)</pre>
<p><code>EXPR</code> evaluates mathematical expression and returns result in the output variable. Example mathematical expression is &#8216;5 * ( 10 + 13 )&#8217;. Supported operators are + &#8211; * / % | &amp; ^ ~ &lt;&lt; &gt;&gt; * / %. They have the same meaning as they do in C code.</p>
<h3>message</h3>
<p>Display a message to the user. </p>
<pre>message([&lt;mode&gt;] &quot;message to display&quot; ...)</pre>
<p>The optional <code>&lt;mode&gt;</code> keyword determines the type of message: </p>
<pre>(none) = Important information
STATUS = Incidental information
WARNING = CMake Warning, continue processing
AUTHOR_WARNING = CMake Warning (dev), continue processing
SEND_ERROR = CMake Error, continue processing,
 but skip generation
FATAL_ERROR = CMake Error, stop processing and generation
DEPRECATION = CMake Deprecation Error or Warning if variable
 CMAKE_ERROR_DEPRECATED or CMAKE_WARN_DEPRECATED
 is enabled, respectively, else no message.</pre>
<p>The CMake command-line tool displays STATUS messages on stdout and all other message types on stderr. The CMake GUI displays all messages in its log area. The interactive dialogs (ccmake and CMakeSetup) show STATUS messages one at a time on a status line and other messages in interactive pop-up boxes. </p>
<p> CMake Warning and Error message text displays using a simple markup language. Non-indented text is formatted in line-wrapped paragraphs delimited by newlines. Indented text is considered pre-formatted.</p>
<h3>option</h3>
<p>Provides an option that the user can optionally select. </p>
<pre>option(&lt;option_variable&gt; &quot;help string describing option&quot;
 [initial value])</pre>
<p>Provide an option for the user to select as <code>ON</code> or <code>OFF</code>. If no initial value is provided, <code>OFF</code> is used. </p>
<p> If you have options that depend on the values of other options, see the module help for <code>CMakeDependentOption</code>.</p>
<h3>project</h3>
<p>Set a name, version, and enable languages for the entire project. </p>
<pre>project(&lt;PROJECT-NAME&gt; [LANGUAGES] [&lt;language-name&gt;...])
project(&lt;PROJECT-NAME&gt;
 [VERSION &lt;major&gt;[.&lt;minor&gt;[.&lt;patch&gt;[.&lt;tweak&gt;]]]]
 [LANGUAGES &lt;language-name&gt;...])</pre>
<p>Sets the name of the project and stores the name in the <code>PROJECT_NAME</code> variable. Additionally this sets variables</p>
<dl>
<dt>&bull;</p>
<dd><code>PROJECT_SOURCE_DIR</code>, <code>&lt;PROJECT-NAME&gt;_SOURCE_DIR</code></p>
<dt>&bull;</p>
<dd><code>PROJECT_BINARY_DIR</code>, <code>&lt;PROJECT-NAME&gt;_BINARY_DIR</code> </p>
<p> If <code>VERSION</code> is specified, given components must be non-negative integers. If <code>VERSION</code> is not specified, the default version is the empty string. The <code>VERSION</code> option may not be used unless policy <code>CMP0048</code> is set to <code>NEW</code>. </p>
<p> The <code>project()</code> command stores the version number and its components in variables</p>
<dt>&bull;</p>
<dd><code>PROJECT_VERSION</code>, <code>&lt;PROJECT-NAME&gt;_VERSION</code></p>
<dt>&bull;</p>
<dd><code>PROJECT_VERSION_MAJOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MAJOR</code></p>
<dt>&bull;</p>
<dd><code>PROJECT_VERSION_MINOR</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_MINOR</code></p>
<dt>&bull;</p>
<dd><code>PROJECT_VERSION_PATCH</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_PATCH</code></p>
<dt>&bull;</p>
<dd><code>PROJECT_VERSION_TWEAK</code>, <code>&lt;PROJECT-NAME&gt;_VERSION_TWEAK</code> </p>
<p> Variables corresponding to unspecified versions are set to the empty string (if policy <code>CMP0048</code> is set to <code>NEW</code>). </p>
<p> Optionally you can specify which languages your project supports. Example languages are <code>C</code>, <code>CXX</code> (i.e. C++), <code>Fortran</code>, etc. By default <code>C</code> and <code>CXX</code> are enabled if no language options are given. Specify language <code>NONE</code>, or use the <code>LANGUAGES</code> keyword and list no languages, to skip enabling any languages. </p>
<p> If a variable exists called <code>CMAKE_PROJECT_&lt;PROJECT-NAME&gt;_INCLUDE</code>, the file pointed to by that variable will be included as the last step of the project command. </p>
<p> The top-level <code>CMakeLists.txt</code> file for a project must contain a literal, direct call to the <code>project()</code> command; loading one through the <code>include()</code> command is not sufficient. If no such call exists CMake will implicitly add one to the top that enables the default languages (<code>C</code> and <code>CXX</code>). </p>
<p> <code>NOTE:</code> Call the <code>cmake_minimum_required()</code> command at the beginning of the top-level <code>CMakeLists.txt</code> file even before calling the <code>project()</code> command. It is important to establish version and policy settings before invoking other commands whose behavior they may affect. See also policy <code>CMP0000</code>.</dl>
<h3>qt_wrap_cpp</h3>
<p>Create Qt Wrappers. </p>
<pre>qt_wrap_cpp(resultingLibraryName DestName
 SourceLists ...)</pre>
<p>Produce moc files for all the .h files listed in the SourceLists. The moc files will be added to the library using the <code>DestName</code> source list.</p>
<h3>qt_wrap_ui</h3>
<p>Create Qt user interfaces Wrappers. </p>
<pre>qt_wrap_ui(resultingLibraryName HeadersDestName
 SourcesDestName SourceLists ...)</pre>
<p>Produce .h and .cxx files for all the .ui files listed in the <code>SourceLists</code>. The .h files will be added to the library using the <code>HeadersDestNamesource</code> list. The .cxx files will be added to the library using the <code>SourcesDestNamesource</code> list.</p>
<h3>remove_definitions</h3>
<p>Removes -D define flags added by <code>add_definitions()</code>. </p>
<pre>remove_definitions(-DFOO -DBAR ...)</pre>
<p>Removes flags (added by <code>add_definitions()</code>) from the compiler command line for sources in the current directory and below.</p>
<h3>return</h3>
<p>Return from a file, directory or function. </p>
<pre>return()</pre>
<p>Returns from a file, directory or function. When this command is encountered in an included file (via <code>include()</code> or <code>find_package()</code>), it causes processing of the current file to stop and control is returned to the including file. If it is encountered in a file which is not included by another file, e.g. a <code>CMakeLists.txt</code>, control is returned to the parent directory if there is one. If return is called in a function, control is returned to the caller of the function. Note that a macro is not a function and does not handle return like a function does.</p>
<h3>separate_arguments</h3>
<p>Parse space-separated arguments into a semicolon-separated list. </p>
<pre>separate_arguments(&lt;var&gt; &lt;UNIX|WINDOWS&gt;_COMMAND &quot;&lt;args&gt;&quot;)</pre>
<p>Parses a unix- or windows-style command-line string &quot;&lt;args&gt;&quot; and stores a semicolon-separated list of the arguments in <code>&lt;var&gt;</code>. The entire command line must be given in one &quot;&lt;args&gt;&quot; argument. </p>
<p> The <code>UNIX_COMMAND</code> mode separates arguments by unquoted whitespace. It recognizes both single-quote and double-quote pairs. A backslash escapes the next literal character (&quot; is &quot;); there are no special escapes (n is just n). </p>
<p> The <code>WINDOWS_COMMAND</code> mode parses a windows command-line using the same syntax the runtime library uses to construct argv at startup. It separates arguments by whitespace that is not double-quoted. Backslashes are literal unless they precede double-quotes. See the MSDN article &quot;Parsing C Command-Line Arguments&quot; for details. </p>
<pre>separate_arguments(VARIABLE)</pre>
<p>Convert the value of <code>VARIABLE</code> to a semi-colon separated list. All spaces are replaced with &#8216;;&#8217;. This helps with generating command lines.</p>
<h3>set_directory_properties</h3>
<p>Set a property of the directory. </p>
<pre>set_directory_properties(PROPERTIES prop1 value1 prop2 value2)</pre>
<p>Set a property for the current directory and subdirectories. See <i>Directory Properties</i> for the list of properties known to CMake.</p>
<h3>set_property</h3>
<p>Set a named property in a given scope. </p>
<pre>set_property(&lt;GLOBAL |
 DIRECTORY [dir] |
 TARGET [target1 [target2 ...]] |
 SOURCE [src1 [src2 ...]] |
 INSTALL [file1 [file2 ...]] |
 TEST [test1 [test2 ...]] |
 CACHE [entry1 [entry2 ...]]&gt;
 [APPEND] [APPEND_STRING]
 PROPERTY &lt;name&gt; [value1 [value2 ...]])</pre>
<p>Set one property on zero or more objects of a scope. The first argument determines the scope in which the property is set. It must be one of the following:</p>
<dl>
<dt><code>GLOBAL</code></p>
<dd>Scope is unique and does not accept a name.</p>
<dt><code>DIRECTORY</code></p>
<dd>Scope defaults to the current directory but another directory (already processed by CMake) may be named by full or relative path.</p>
<dt><code>TARGET</code></p>
<dd>Scope may name zero or more existing targets.</p>
<dt><code>SOURCE</code></p>
<dd>Scope may name zero or more source files. Note that source file properties are visible only to targets added in the same directory (CMakeLists.txt).</p>
<dt><code>INSTALL</code></p>
<dd>Scope may name zero or more installed file paths. These are made available to CPack to influence deployment. </p>
<p> Both the property key and value may use generator expressions. Specific properties may apply to installed files and/or directories. </p>
<p> Path components have to be separated by forward slashes, must be normalized and are case sensitive. </p>
<p> To reference the installation prefix itself with a relative path use &quot;.&quot;. </p>
<p> Currently installed file properties are only defined for the WIX generator where the given paths are relative to the installation prefix.</p>
<dt><code>TEST</code></p>
<dd>Scope may name zero or more existing tests.</p>
<dt><code>CACHE</code></p>
<dd>Scope must name zero or more cache existing entries. </p>
<p> The required <code>PROPERTY</code> option is immediately followed by the name of the property to set. Remaining arguments are used to compose the property value in the form of a semicolon-separated list. If the <code>APPEND</code> option is given the list is appended to any existing property value. If the <code>APPEND_STRING</code> option is given the string is append to any existing property value as string, i.e. it results in a longer string and not a list of strings. </p>
<p> See the <code><a href="/docs/linux/man/7-cmake3-properties/">cmake3-properties</a>(7)</code> manual for a list of properties in each scope.</dl>
<h3>set</h3>
<p>Set a normal, cache, or environment variable to a given value. See the <i><a href="/docs/linux/man/7-cmake3-language/">cmake3-language</a>(7) variables</i> documentation for the scopes and interaction of normal variables and cache entries. </p>
<p> Signatures of this command that specify a <code>&lt;value&gt;&#8230;</code> placeholder expect zero or more arguments. Multiple arguments will be joined as a <i>;-list</i> to form the actual variable value to be set. Zero arguments will cause normal variables to be unset. See the <code>unset()</code> command to unset variables explicitly.</p>
<h3>Set Normal Variable</h3>
<pre>set(&lt;variable&gt; &lt;value&gt;... [PARENT_SCOPE])</pre>
<p>Set the given <code>&lt;variable&gt;</code> in the current function or directory scope. </p>
<p> If the <code>PARENT_SCOPE</code> option is given the variable will be set in the scope above the current scope. Each new directory or function creates a new scope. This command will set the value of a variable into the parent directory or calling function (whichever is applicable to the case at hand).</p>
<h3>Set Cache Entry</h3>
<pre>set(&lt;variable&gt; &lt;value&gt;... CACHE &lt;type&gt; &lt;docstring&gt; [FORCE])</pre>
<p>Set the given cache <code>&lt;variable&gt;</code> (cache entry). Since cache entries are meant to provide user-settable values this does not overwrite existing cache entries by default. Use the <code>FORCE</code> option to overwrite existing entries. </p>
<p> The <code>&lt;type&gt;</code> must be specified as one of:</p>
<dl>
<dt><code>BOOL</code></p>
<dd>Boolean <code>ON/OFF</code> value. <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> offers a checkbox.</p>
<dt><code>FILEPATH</code></p>
<dd>Path to a file on disk. <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> offers a file dialog.</p>
<dt><code>PATH</code></p>
<dd>Path to a directory on disk. <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> offers a file dialog.</p>
<dt><code>STRING</code></p>
<dd>A line of text. <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> offers a text field or a drop-down selection if the <code>STRINGS</code> cache entry property is set.</p>
<dt><code>INTERNAL</code></p>
<dd>A line of text. <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> does not show internal entries. They may be used to store variables persistently across runs. Use of this type implies <code>FORCE</code>. </p>
<p> The <code>&lt;docstring&gt;</code> must be specified as a line of text providing a quick summary of the option for presentation to <code><a href="/docs/linux/man/1-cmake3-gui/">cmake3-gui</a>(1)</code> users. </p>
<p> If the cache entry does not exist prior to the call or the <code>FORCE</code> option is given then the cache entry will be set to the given value. Furthermore, any normal variable binding in the current scope will be removed to expose the newly cached value to any immediately following evaluation. </p>
<p> It is possible for the cache entry to exist prior to the call but have no type set if it was created on the <code><a href="/docs/linux/man/1-cmake3/">cmake3</a>(1)</code> command line by a user through the <code>-D&lt;var&gt;=&lt;value&gt;</code> option without specifying a type. In this case the <code>set</code> command will add the type. Furthermore, if the <code>&lt;type&gt;</code> is <code>PATH</code> or <code>FILEPATH</code> and the <code>&lt;value&gt;</code> provided on the command line is a relative path, then the <code>set</code> command will treat the path as relative to the current working directory and convert it to an absolute path.</dl>
<h3>Set Environment Variable</h3>
<pre>set(ENV{&lt;variable&gt;} &lt;value&gt;...)</pre>
<p>Set the current process environment <code>&lt;variable&gt;</code> to the given value.</p>
<h3>set_source_files_properties</h3>
<p>Source files can have properties that affect how they are built. </p>
<pre>set_source_files_properties([file1 [file2 [...]]]
 PROPERTIES prop1 value1
 [prop2 value2 [...]])</pre>
<p>Set properties associated with source files using a key/value paired list. See <i>Source File Properties</i> for the list of properties known to CMake. Source file properties are visible only to targets added in the same directory (CMakeLists.txt).</p>
<h3>set_target_properties</h3>
<p>Targets can have properties that affect how they are built. </p>
<pre>set_target_properties(target1 target2 ...
 PROPERTIES prop1 value1
 prop2 value2 ...)</pre>
<p>Set properties on a target. The syntax for the command is to list all the files you want to change, and then provide the values you want to set next. You can use any prop value pair you want and extract it later with the <code>get_property()</code> or <code>get_target_property()</code> command. </p>
<p> See <i>Target Properties</i> for the list of properties known to CMake.</p>
<h3>set_tests_properties</h3>
<p>Set a property of the tests. </p>
<pre>set_tests_properties(test1 [test2...] PROPERTIES prop1 value1 prop2 value2)</pre>
<p>Set a property for the tests. If the test is not found, CMake will report an error. <code>Generator expressions</code> will be expanded the same as supported by the test&#8217;s <code>add_test()</code> call. See <i>Test Properties</i> for the list of properties known to CMake.</p>
<h3>site_name</h3>
<p>Set the given variable to the name of the computer. </p>
<pre>site_name(variable)</pre>
<h3>source_group</h3>
<p>Define a grouping for source files in IDE project generation. </p>
<pre>source_group(&lt;name&gt; [FILES &lt;src&gt;...] [REGULAR_EXPRESSION &lt;regex&gt;])</pre>
<p>Defines a group into which sources will be placed in project files. This is intended to set up file tabs in Visual Studio. The options are:</p>
<dl>
<dt><code>FILES</code></p>
<dd>Any source file specified explicitly will be placed in group <code>&lt;name&gt;</code>. Relative paths are interpreted with respect to the current source directory.</p>
<dt><code>REGULAR_EXPRESSION</code></p>
<dd>Any source file whose name matches the regular expression will be placed in group <code>&lt;name&gt;</code>. </p>
<p> If a source file matches multiple groups, the <i>last</i> group that explicitly lists the file with <code>FILES</code> will be favored, if any. If no group explicitly lists the file, the <i>last</i> group whose regular expression matches the file will be favored. </p>
<p> The <code>&lt;name&gt;</code> of the group may contain backslashes to specify subgroups: </p>
<pre>source_group(outer\inner ...)</pre>
<p>For backwards compatibility, the short-hand signature </p>
<pre>source_group(&lt;name&gt; &lt;regex&gt;)</pre>
<p>is equivalent to </p>
<pre>source_group(&lt;name&gt; REGULAR_EXPRESSION &lt;regex&gt;)</pre>
</dl>
<h3>string</h3>
<p>String operations.</p>
<h3>Search and Replace</h3>
<h3>Find</h3>
<pre>string(FIND &lt;string&gt; &lt;substring&gt; &lt;output variable&gt; [REVERSE])</pre>
<p>Return the position where the given substring was found in the supplied string. If the <code>REVERSE</code> flag was used, the command will search for the position of the last occurrence of the specified substring. If the substring is not found, a position of -1 is returned.</p>
<h3>Replace</h3>
<pre>string(REPLACE &lt;match_string&gt;
 &lt;replace_string&gt; &lt;output variable&gt;
 &lt;input&gt; [&lt;input&gt;...])</pre>
<p>Replace all occurrences of <code>match_string</code> in the input with <code>replace_string</code> and store the result in the output.</p>
<h3>Regular Expressions</h3>
<h3>Regex Match</h3>
<pre>string(REGEX MATCH &lt;regular_expression&gt;
 &lt;output variable&gt; &lt;input&gt; [&lt;input&gt;...])</pre>
<p>Match the regular expression once and store the match in the output variable. All <code>&lt;input&gt;</code> arguments are concatenated before matching.</p>
<h3>Regex Matchall</h3>
<pre>string(REGEX MATCHALL &lt;regular_expression&gt;
 &lt;output variable&gt; &lt;input&gt; [&lt;input&gt;...])</pre>
<p>Match the regular expression as many times as possible and store the matches in the output variable as a list. All <code>&lt;input&gt;</code> arguments are concatenated before matching.</p>
<h3>Regex Replace</h3>
<pre>string(REGEX REPLACE &lt;regular_expression&gt;
 &lt;replace_expression&gt; &lt;output variable&gt;
 &lt;input&gt; [&lt;input&gt;...])</pre>
<p>Match the regular expression as many times as possible and substitute the replacement expression for the match in the output. All <code>&lt;input&gt;</code> arguments are concatenated before matching. </p>
<p> The replace expression may refer to paren-delimited subexpressions of the match using <code>\1</code>, <code>\2</code>, &#8230;, <code>\9</code>. Note that two backslashes (<code>\1</code>) are required in CMake code to get a backslash through argument parsing.</p>
<h3>Regex Specification</h3>
<p>The following characters have special meaning in regular expressions: </p>
<pre>^ Matches at beginning of input
$ Matches at end of input
. Matches any single character
[ ] Matches any character(s) inside the brackets
[^ ] Matches any character(s) not inside the brackets
 - Inside brackets, specifies an inclusive range between
 characters on either side e.g. [a-f] is [abcdef]
 To match a literal - using brackets, make it the first
 or the last character e.g. [+*/-] matches basic
 mathematical operators.
* Matches preceding pattern zero or more times
+ Matches preceding pattern one or more times
? Matches preceding pattern zero or once only
| Matches a pattern on either side of the |
() Saves a matched subexpression, which can be referenced
 in the REGEX REPLACE operation. Additionally it is saved
 by all regular expression-related commands, including
 e.g. if( MATCHES ), in the variables CMAKE_MATCH_(0..9).</pre>
<p><code>*</code>, <code>+</code> and <code>?</code> have higher precedence than concatenation. <code>|</code> has lower precedence than concatenation. This means that the regular expression <code>^ab+d$</code> matches <code>abbd</code> but not <code>ababd</code>, and the regular expression <code>^(ab|cd)$</code> matches <code>ab</code> but not <code>abd</code>.</p>
<h3>Manipulation</h3>
<h3>Append</h3>
<pre>string(APPEND &lt;string variable&gt; [&lt;input&gt;...])</pre>
<p>Append all the input arguments to the string.</p>
<h3>Concat</h3>
<pre>string(CONCAT &lt;output variable&gt; [&lt;input&gt;...])</pre>
<p>Concatenate all the input arguments together and store the result in the named output variable.</p>
<h3>Tolower</h3>
<pre>string(TOLOWER &lt;string1&gt; &lt;output variable&gt;)</pre>
<p>Convert string to lower characters.</p>
<h3>Toupper</h3>
<pre>string(TOUPPER &lt;string1&gt; &lt;output variable&gt;)</pre>
<p>Convert string to upper characters.</p>
<h3>Length</h3>
<pre>string(LENGTH &lt;string&gt; &lt;output variable&gt;)</pre>
<p>Store in an output variable a given string&#8217;s length.</p>
<h3>Substring</h3>
<pre>string(SUBSTRING &lt;string&gt; &lt;begin&gt; &lt;length&gt; &lt;output variable&gt;)</pre>
<p>Store in an output variable a substring of a given string. If length is <code>-1</code> the remainder of the string starting at begin will be returned. If string is shorter than length then end of string is used instead. </p>
<p> <code>NOTE:</code> CMake 3.1 and below reported an error if length pointed past the end of string.</p>
<h3>Strip</h3>
<pre>string(STRIP &lt;string&gt; &lt;output variable&gt;)</pre>
<p>Store in an output variable a substring of a given string with leading and trailing spaces removed.</p>
<h3>Genex_Strip</h3>
<pre>string(GENEX_STRIP &lt;input string&gt; &lt;output variable&gt;)</pre>
<p>Strip any <code>generator expressions</code> from the <code>input string</code> and store the result in the <code>output variable</code>.</p>
<h3>Comparison</h3>
<pre>string(COMPARE EQUAL &lt;string1&gt; &lt;string2&gt; &lt;output variable&gt;)
string(COMPARE NOTEQUAL &lt;string1&gt; &lt;string2&gt; &lt;output variable&gt;)
string(COMPARE LESS &lt;string1&gt; &lt;string2&gt; &lt;output variable&gt;)
string(COMPARE GREATER &lt;string1&gt; &lt;string2&gt; &lt;output variable&gt;)</pre>
<p>Compare the strings and store true or false in the output variable.</p>
<h3>Hashing</h3>
<pre>string(&lt;MD5|SHA1|SHA224|SHA256|SHA384|SHA512&gt;
 &lt;output variable&gt; &lt;input&gt;)</pre>
<p>Compute a cryptographic hash of the input string.</p>
<h3>Generation</h3>
<h3>Ascii</h3>
<pre>string(ASCII &lt;number&gt; [&lt;number&gt; ...] &lt;output variable&gt;)</pre>
<p>Convert all numbers into corresponding ASCII characters.</p>
<h3>Configure</h3>
<pre>string(CONFIGURE &lt;string1&gt; &lt;output variable&gt;
 [@ONLY] [ESCAPE_QUOTES])</pre>
<p>Transform a string like <code>configure_file()</code> transforms a file.</p>
<h3>Random</h3>
<pre>string(RANDOM [LENGTH &lt;length&gt;] [ALPHABET &lt;alphabet&gt;]
 [RANDOM_SEED &lt;seed&gt;] &lt;output variable&gt;)</pre>
<p>Return a random string of given length consisting of characters from the given alphabet. Default length is 5 characters and default alphabet is all numbers and upper and lower case letters. If an integer <code>RANDOM_SEED</code> is given, its value will be used to seed the random number generator.</p>
<h3>Timestamp</h3>
<pre>string(TIMESTAMP &lt;output variable&gt; [&lt;format string&gt;] [UTC])</pre>
<p>Write a string representation of the current date and/or time to the output variable. </p>
<p> Should the command be unable to obtain a timestamp the output variable will be set to the empty string &quot;&quot;. </p>
<p> The optional <code>UTC</code> flag requests the current date/time representation to be in Coordinated Universal Time (UTC) rather than local time. </p>
<p> The optional <code>&lt;format string&gt;</code> may contain the following format specifiers: </p>
<pre>%d The day of the current month (01-31).
%H The hour on a 24-hour clock (00-23).
%I The hour on a 12-hour clock (01-12).
%j The day of the current year (001-366).
%m The month of the current year (01-12).
%M The minute of the current hour (00-59).
%s Seconds since midnight (UTC) 1-Jan-1970 (UNIX time).
%S The second of the current minute.
 60 represents a leap second. (00-60)
%U The week number of the current year (00-53).
%w The day of the current week. 0 is Sunday. (0-6)
%y The last two digits of the current year (00-99)
%Y The current year.</pre>
<p>Unknown format specifiers will be ignored and copied to the output as-is. </p>
<p> If no explicit <code>&lt;format string&gt;</code> is given it will default to: </p>
<pre>%Y-%m-%dT%H:%M:%S for local time.
%Y-%m-%dT%H:%M:%SZ for UTC.</pre>
<pre>string(MAKE_C_IDENTIFIER &lt;input string&gt; &lt;output variable&gt;)</pre>
<p>Write a string which can be used as an identifier in C.</p>
<h3>Uuid</h3>
<pre>string(UUID &lt;output variable&gt; NAMESPACE &lt;namespace&gt; NAME &lt;name&gt;
 TYPE &lt;MD5|SHA1&gt; [UPPER])</pre>
<p>Create a univerally unique identifier (aka GUID) as per RFC4122 based on the hash of the combined values of <code>&lt;namespace&gt;</code> (which itself has to be a valid UUID) and <code>&lt;name&gt;</code>. The hash algorithm can be either <code>MD5</code> (Version 3 UUID) or <code>SHA1</code> (Version 5 UUID). A UUID has the format <code>xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx</code> where each <i>x</i> represents a lower case hexadecimal character. Where required an uppercase representation can be requested with the optional <code>UPPER</code> flag.</p>
<h3>target_compile_definitions</h3>
<p>Add compile definitions to a target. </p>
<pre>target_compile_definitions(&lt;target&gt;
 &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
 [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])</pre>
<p>Specify compile definitions to use when compiling a given <code>&lt;target&gt;</code>. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an <i>Imported Target</i>. </p>
<p> The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_DEFINITIONS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_DEFINITIONS</code> property of <code>&lt;target&gt;</code>. The following arguments specify compile definitions. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p> Arguments to <code>target_compile_definitions</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>target_compile_features</h3>
<p>Add expected compiler features to a target. </p>
<pre>target_compile_features(&lt;target&gt; &lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;feature&gt; [...])</pre>
<p>Specify compiler features required when compiling a given target. If the feature is not listed in the <code>CMAKE_C_COMPILE_FEATURES</code> variable or <code>CMAKE_CXX_COMPILE_FEATURES</code> variable, then an error will be reported by CMake. If the use of the feature requires an additional compiler flag, such as <code>-std=gnu++11</code>, the flag will be added automatically. </p>
<p> The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the features. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_FEATURES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_FEATURES</code> property of <code>&lt;target&gt;</code>. Repeated calls for the same <code>&lt;target&gt;</code> append items. </p>
<p> The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an <code>IMPORTED</code> target. </p>
<p> Arguments to <code>target_compile_features</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-compile-features/">cmake3-compile-features</a>(7)</code> manual for information on compile features and a list of supported compilers.</p>
<h3>target_compile_options</h3>
<p>Add compile options to a target. </p>
<pre>target_compile_options(&lt;target&gt; [BEFORE]
 &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
 [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])</pre>
<p>Specify compile options to use when compiling a given target. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an <i>IMPORTED Target</i>. If <code>BEFORE</code> is specified, the content will be prepended to the property instead of being appended. </p>
<p> This command can be used to add any options, but alternative commands exist to add preprocessor definitions (<code>target_compile_definitions()</code> and <code>add_definitions()</code>) or include directories (<code>target_include_directories()</code> and <code>include_directories()</code>). See documentation of the <code>directory</code> and <code>target</code> <code>COMPILE_OPTIONS</code> properties. </p>
<p> The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>COMPILE_OPTIONS</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_COMPILE_OPTIONS</code> property of <code>&lt;target&gt;</code>. The following arguments specify compile options. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p> Arguments to <code>target_compile_options</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>target_include_directories</h3>
<p>Add include directories to a target. </p>
<pre>target_include_directories(&lt;target&gt; [SYSTEM] [BEFORE]
 &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
 [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])</pre>
<p>Specify include directories to use when compiling a given target. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an <code>IMPORTED</code> target. </p>
<p> If <code>BEFORE</code> is specified, the content will be prepended to the property instead of being appended. </p>
<p> The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>INCLUDE_DIRECTORIES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_INCLUDE_DIRECTORIES</code> property of <code>&lt;target&gt;</code>. The following arguments specify include directories. </p>
<p> Specified include directories may be absolute paths or relative paths. Repeated calls for the same &lt;target&gt; append items in the order called. If <code>SYSTEM</code> is specified, the compiler will be told the directories are meant as system include directories on some platforms (signalling this setting might achieve effects such as the compiler skipping warnings, or these fixed-install system files not being considered in dependency calculations &#8211; see compiler docs). If <code>SYSTEM</code> is used together with <code>PUBLIC</code> or <code>INTERFACE</code>, the <code>INTERFACE_SYSTEM_INCLUDE_DIRECTORIES</code> target property will be populated with the specified directories. </p>
<p> Arguments to <code>target_include_directories</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties. </p>
<p> Include directories usage requirements commonly differ between the build-tree and the install-tree. The <code>BUILD_INTERFACE</code> and <code>INSTALL_INTERFACE</code> generator expressions can be used to describe separate usage requirements based on the usage location. Relative paths are allowed within the <code>INSTALL_INTERFACE</code> expression and are interpreted relative to the installation prefix. For example: </p>
<pre>target_include_directories(mylib PUBLIC
 $&lt;BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/mylib&gt;
 $&lt;INSTALL_INTERFACE:include/mylib&gt; # &lt;prefix&gt;/include/mylib
)</pre>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> of a target with absolute paths to the include directories of dependencies. That would hard-code into installed packages the include directory paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> The <code>INSTALL_INTERFACE</code> of the <code>INTERFACE_INCLUDE_DIRECTORIES</code> is only suitable for specifying the required include directories for headers provided with the target itself, not those provided by the transitive dependencies listed in its <code>INTERFACE_LINK_LIBRARIES</code> target property. Those dependencies should themselves be targets that specify their own header locations in <code>INTERFACE_INCLUDE_DIRECTORIES</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>target_link_libraries</h3>
<p>Specify libraries or flags to use when linking a given target and/or its dependents. <i>Usage requirements</i> from linked library targets will be propagated. Usage requirements of a target&#8217;s dependencies affect compilation of its own sources.</p>
<h3>Overview</h3>
<p>This command has several signatures as detailed in subsections below. All of them have the general form: </p>
<pre>target_link_libraries(&lt;target&gt; ... &lt;item&gt;... ...)</pre>
<p>The named <code>&lt;target&gt;</code> must have been created in the current directory by a command such as <code>add_executable()</code> or <code>add_library()</code>. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. Each <code>&lt;item&gt;</code> may be:</p>
<dl>
<dt>&bull;</p>
<dd><code>A library target name</code>: The generated link line will have the full path to the linkable library file associated with the target. The buildsystem will have a dependency to re-link <code>&lt;target&gt;</code> if the library file changes. </p>
<p> The named target must be created by <code>add_library()</code> within the project or as an <i>IMPORTED library</i>. If it is created within the project an ordering dependency will automatically be added in the build system to make sure the named library target is up-to-date before the <code>&lt;target&gt;</code> links. </p>
<p> If an imported library has the <code>IMPORTED_NO_SONAME</code> target property set, CMake may ask the linker to search for the library instead of using the full path (e.g. <code>/usr/lib/libfoo.so</code> becomes <code>-lfoo</code>).</p>
<dt>&bull;</p>
<dd><code>A full path to a library file</code>: The generated link line will normally preserve the full path to the file. The buildsystem will have a dependency to re-link <code>&lt;target&gt;</code> if the library file changes. </p>
<p> There are some cases where CMake may ask the linker to search for the library (e.g. <code>/usr/lib/libfoo.so</code> becomes <code>-lfoo</code>), such as when a shared library is detected to have no <code>SONAME</code> field. See policy <code>CMP0060</code> for discussion of another case. </p>
<p> If the library file is in a Mac OSX framework, the <code>Headers</code> directory of the framework will also be processed as a <i>usage requirement</i>. This has the same effect as passing the framework directory as an include directory.</p>
<dt>&bull;</p>
<dd><code>A plain library name</code>: The generated link line will ask the linker to search for the library (e.g. <code>foo</code> becomes <code>-lfoo</code> or <code>foo.lib</code>).</p>
<dt>&bull;</p>
<dd><code>A link flag</code>: Item names starting with <code>&#8211;</code>, but not <code>-l</code> or <code>-framework</code>, are treated as linker flags. Note that such flags will be treated like any other library link item for purposes of transitive dependencies, so they are generally safe to specify only as private link items that will not propagate to dependents.</p>
<dt>&bull;</p>
<dd>A <code>debug</code>, <code>optimized</code>, or <code>general</code> keyword immediately followed by another <code>&lt;item&gt;</code>. The item following such a keyword will be used only for the corresponding build configuration. The <code>debug</code> keyword corresponds to the <code>Debug</code> configuration (or to configurations named in the <code>DEBUG_CONFIGURATIONS</code> global property if it is set). The <code>optimized</code> keyword corresponds to all other configurations. The <code>general</code> keyword corresponds to all configurations, and is purely optional. Higher granularity may be achieved for per-configuration rules by creating and linking to <i>IMPORTED library targets</i>. </p>
<p> Items containing <code>::</code>, such as <code>Foo::Bar</code>, are assumed to be <i>IMPORTED</i> or <i>ALIAS</i> library target names and will cause an error if no such target exists. See policy <code>CMP0028</code>. </p>
<p> Arguments to <code>target_link_libraries</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. Note however, that generator expressions will not be used in OLD handling of <code>CMP0003</code> or <code>CMP0004</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</dl>
<h3>Libraries for a Target and/or its Dependents</h3>
<pre>target_link_libraries(&lt;target&gt;
 &lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;item&gt;...
 [&lt;PRIVATE|PUBLIC|INTERFACE&gt; &lt;item&gt;...]...)</pre>
<p>The <code>PUBLIC</code>, <code>PRIVATE</code> and <code>INTERFACE</code> keywords can be used to specify both the link dependencies and the link interface in one command. Libraries and targets following <code>PUBLIC</code> are linked to, and are made part of the link interface. Libraries and targets following <code>PRIVATE</code> are linked to, but are not made part of the link interface. Libraries following <code>INTERFACE</code> are appended to the link interface and are not used for linking <code>&lt;target&gt;</code>.</p>
<h3>Libraries for both a Target and its Dependents</h3>
<pre>target_link_libraries(&lt;target&gt; &lt;item&gt;...)</pre>
<p>Library dependencies are transitive by default with this signature. When this target is linked into another target then the libraries linked to this target will appear on the link line for the other target too. This transitive &quot;link interface&quot; is stored in the <code>INTERFACE_LINK_LIBRARIES</code> target property and may be overridden by setting the property directly. When <code>CMP0022</code> is not set to <code>NEW</code>, transitive linking is built in but may be overridden by the <code>LINK_INTERFACE_LIBRARIES</code> property. Calls to other signatures of this command may set the property making any libraries linked exclusively by this signature private.</p>
<h3>Libraries for a Target and/or its Dependents (Legacy)</h3>
<pre>target_link_libraries(&lt;target&gt;
 &lt;LINK_PRIVATE|LINK_PUBLIC&gt; &lt;lib&gt;...
 [&lt;LINK_PRIVATE|LINK_PUBLIC&gt; &lt;lib&gt;...]...)</pre>
<p>The <code>LINK_PUBLIC</code> and <code>LINK_PRIVATE</code> modes can be used to specify both the link dependencies and the link interface in one command. </p>
<p> This signature is for compatibility only. Prefer the <code>PUBLIC</code> or <code>PRIVATE</code> keywords instead. </p>
<p> Libraries and targets following <code>LINK_PUBLIC</code> are linked to, and are made part of the <code>INTERFACE_LINK_LIBRARIES</code>. If policy <code>CMP0022</code> is not <code>NEW</code>, they are also made part of the <code>LINK_INTERFACE_LIBRARIES</code>. Libraries and targets following <code>LINK_PRIVATE</code> are linked to, but are not made part of the <code>INTERFACE_LINK_LIBRARIES</code> (or <code>LINK_INTERFACE_LIBRARIES</code>).</p>
<h3>Libraries for Dependents Only (Legacy)</h3>
<pre>target_link_libraries(&lt;target&gt; LINK_INTERFACE_LIBRARIES &lt;item&gt;...)</pre>
<p>The <code>LINK_INTERFACE_LIBRARIES</code> mode appends the libraries to the <code>INTERFACE_LINK_LIBRARIES</code> target property instead of using them for linking. If policy <code>CMP0022</code> is not <code>NEW</code>, then this mode also appends libraries to the <code>LINK_INTERFACE_LIBRARIES</code> and its per-configuration equivalent. </p>
<p> This signature is for compatibility only. Prefer the <code>INTERFACE</code> mode instead. </p>
<p> Libraries specified as <code>debug</code> are wrapped in a generator expression to correspond to debug builds. If policy <code>CMP0022</code> is not <code>NEW</code>, the libraries are also appended to the <code>LINK_INTERFACE_LIBRARIES_DEBUG</code> property (or to the properties corresponding to configurations listed in the <code>DEBUG_CONFIGURATIONS</code> global property if it is set). Libraries specified as <code>optimized</code> are appended to the <code>INTERFACE_LINK_LIBRARIES</code> property. If policy <code>CMP0022</code> is not <code>NEW</code>, they are also appended to the <code>LINK_INTERFACE_LIBRARIES</code> property. Libraries specified as <code>general</code> (or without any keyword) are treated as if specified for both <code>debug</code> and <code>optimized</code>.</p>
<h3>Cyclic Dependencies of Static Libraries</h3>
<p>The library dependency graph is normally acyclic (a DAG), but in the case of mutually-dependent <code>STATIC</code> libraries CMake allows the graph to contain cycles (strongly connected components). When another target links to one of the libraries, CMake repeats the entire connected component. For example, the code </p>
<pre>add_library(A STATIC a.c)
add_library(B STATIC b.c)
target_link_libraries(A B)
target_link_libraries(B A)
add_executable(main main.c)
target_link_libraries(main A)</pre>
<p>links <code>main</code> to <code>A B A B</code>. While one repetition is usually sufficient, pathological object file and symbol arrangements can require more. One may handle such cases by using the <code>LINK_INTERFACE_MULTIPLICITY</code> target property or by manually repeating the component in the last <code>target_link_libraries</code> call. However, if two archives are really so interdependent they should probably be combined into a single archive, perhaps by using <i>Object Libraries</i>.</p>
<h3>Creating Relocatable Packages</h3>
<p>Note that it is not advisable to populate the <code>INTERFACE_LINK_LIBRARIES</code> of a target with absolute paths to dependencies. That would hard-code into installed packages the library file paths for dependencies <code>as found on the machine the package was made on</code>. </p>
<p> See the <i>Creating Relocatable Packages</i> section of the <code><a href="/docs/linux/man/7-cmake-packages/">cmake-packages</a>(7)</code> manual for discussion of additional care that must be taken when specifying usage requirements while creating packages for redistribution.</p>
<h3>target_sources</h3>
<p>Add sources to a target. </p>
<pre>target_sources(&lt;target&gt;
 &lt;INTERFACE|PUBLIC|PRIVATE&gt; [items1...]
 [&lt;INTERFACE|PUBLIC|PRIVATE&gt; [items2...] ...])</pre>
<p>Specify sources to use when compiling a given target. The named <code>&lt;target&gt;</code> must have been created by a command such as <code>add_executable()</code> or <code>add_library()</code> and must not be an <i>IMPORTED Target</i>. </p>
<p> The <code>INTERFACE</code>, <code>PUBLIC</code> and <code>PRIVATE</code> keywords are required to specify the scope of the following arguments. <code>PRIVATE</code> and <code>PUBLIC</code> items will populate the <code>SOURCES</code> property of <code>&lt;target&gt;</code>. <code>PUBLIC</code> and <code>INTERFACE</code> items will populate the <code>INTERFACE_SOURCES</code> property of <code>&lt;target&gt;</code>. The following arguments specify sources. Repeated calls for the same <code>&lt;target&gt;</code> append items in the order called. </p>
<p> Arguments to <code>target_sources</code> may use &quot;generator expressions&quot; with the syntax <code>$&lt;&#8230;&gt;</code>. See the <code><a href="/docs/linux/man/7-cmake3-generator-expressions/">cmake3-generator-expressions</a>(7)</code> manual for available expressions. See the <code><a href="/docs/linux/man/7-cmake3-buildsystem/">cmake3-buildsystem</a>(7)</code> manual for more on defining buildsystem properties.</p>
<h3>try_compile</h3>
<p>Try building some code.</p>
<h3>Try Compiling Whole Projects</h3>
<pre>try_compile(RESULT_VAR &lt;bindir&gt; &lt;srcdir&gt;
 &lt;projectName&gt; [&lt;targetName&gt;] [CMAKE_FLAGS &lt;flags&gt;...]
 [OUTPUT_VARIABLE &lt;var&gt;])</pre>
<p>Try building a project. The success or failure of the <code>try_compile</code>, i.e. <code>TRUE</code> or <code>FALSE</code> respectively, is returned in <code>RESULT_VAR</code>. </p>
<p> In this form, <code>&lt;srcdir&gt;</code> should contain a complete CMake project with a <code>CMakeLists.txt</code> file and all sources. The <code>&lt;bindir&gt;</code> and <code>&lt;srcdir&gt;</code> will not be deleted after this command is run. Specify <code>&lt;targetName&gt;</code> to build a specific target instead of the <code>all</code> or <code>ALL_BUILD</code> target. See below for the meaning of other options.</p>
<h3>Try Compiling Source Files</h3>
<pre>try_compile(RESULT_VAR &lt;bindir&gt; &lt;srcfile|SOURCES srcfile...&gt;
 [CMAKE_FLAGS &lt;flags&gt;...]
 [COMPILE_DEFINITIONS &lt;defs&gt;...]
 [LINK_LIBRARIES &lt;libs&gt;...]
 [OUTPUT_VARIABLE &lt;var&gt;]
 [COPY_FILE &lt;fileName&gt; [COPY_FILE_ERROR &lt;var&gt;]])</pre>
<p>Try building an executable from one or more source files. The success or failure of the <code>try_compile</code>, i.e. <code>TRUE</code> or <code>FALSE</code> respectively, is returned in <code>RESULT_VAR</code>. </p>
<p> In this form the user need only supply one or more source files that include a definition for <code>main</code>. CMake will create a <code>CMakeLists.txt</code> file to build the source(s) as an executable that looks something like this: </p>
<pre>add_definitions(&lt;expanded COMPILE_DEFINITIONS from caller&gt;)
include_directories(${INCLUDE_DIRECTORIES})
link_directories(${LINK_DIRECTORIES})
add_executable(cmTryCompileExec &lt;srcfile&gt;...)
target_link_libraries(cmTryCompileExec ${LINK_LIBRARIES})</pre>
<p>The options are:</p>
<dl>
<dt><code>CMAKE_FLAGS &lt;flags&gt;&#8230;</code></p>
<dd>Specify flags of the form <code>-DVAR:TYPE=VALUE</code> to be passed to the <code>cmake3</code> command-line used to drive the test build. The above example shows how values for variables <code>INCLUDE_DIRECTORIES</code>, <code>LINK_DIRECTORIES</code>, and <code>LINK_LIBRARIES</code> are used.</p>
<dt><code>COMPILE_DEFINITIONS &lt;defs&gt;&#8230;</code></p>
<dd>Specify <code>-Ddefinition</code> arguments to pass to <code>add_definitions</code> in the generated test project.</p>
<dt><code>COPY_FILE &lt;fileName&gt;</code></p>
<dd>Copy the linked executable to the given <code>&lt;fileName&gt;</code>.</p>
<dt><code>COPY_FILE_ERROR &lt;var&gt;</code></p>
<dd>Use after <code>COPY_FILE</code> to capture into variable <code>&lt;var&gt;</code> any error message encountered while trying to copy the file.</p>
<dt><code>LINK_LIBRARIES &lt;libs&gt;&#8230;</code></p>
<dd>Specify libraries to be linked in the generated project. The list of libraries may refer to system libraries and to <i>Imported Targets</i> from the calling project. </p>
<p> If this option is specified, any <code>-DLINK_LIBRARIES=&#8230;</code> value given to the <code>CMAKE_FLAGS</code> option will be ignored.</p>
<dt><code>OUTPUT_VARIABLE &lt;var&gt;</code></p>
<dd>Store the output from the build process the given variable. </p>
<p> In this version all files in <code>&lt;bindir&gt;/CMakeFiles/CMakeTmp</code> will be cleaned automatically. For debugging, <code>&#8211;debug-trycompile</code> can be passed to <code>cmake3</code> to avoid this clean. However, multiple sequential <code>try_compile</code> operations reuse this single output directory. If you use <code>&#8211;debug-trycompile</code>, you can only debug one <code>try_compile</code> call at a time. The recommended procedure is to protect all <code>try_compile</code> calls in your project by <code>if(NOT DEFINED RESULT_VAR)</code> logic, configure with cmake all the way through once, then delete the cache entry associated with the try_compile call of interest, and then re-run cmake again with <code>&#8211;debug-trycompile</code>.</dl>
<h3>Other Behavior Settings</h3>
<p>If set, the following variables are passed in to the generated try_compile CMakeLists.txt to initialize compile target properties with default values:</p>
<dl>
<dt>&bull;</p>
<dd><code>CMAKE_ENABLE_EXPORTS</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_LINK_SEARCH_START_STATIC</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_LINK_SEARCH_END_STATIC</code></p>
<dt>&bull;</p>
<dd><code>CMAKE_POSITION_INDEPENDENT_CODE</code> </p>
<p> If <code>CMP0056</code> is set to <code>NEW</code>, then <code>CMAKE_EXE_LINKER_FLAGS</code> is passed in as well. </p>
<p> The current setting of <code>CMP0065</code> is set in the generated project. </p>
<p> Set the <code>CMAKE_TRY_COMPILE_CONFIGURATION</code> variable to choose a build configuration. </p>
<p> Set the <code>CMAKE_TRY_COMPILE_TARGET_TYPE</code> variable to specify the type of target used for the source file signature. </p>
<p> Set the <code>CMAKE_TRY_COMPILE_PLATFORM_VARIABLES</code> variable to specify variables that must be propagated into the test project. This variable is meant for use only in toolchain files.</dl>
<h3>try_run</h3>
<p>Try compiling and then running some code.</p>
<h3>Try Compiling and Running Source Files</h3>
<pre>try_run(RUN_RESULT_VAR COMPILE_RESULT_VAR
 bindir srcfile [CMAKE_FLAGS &lt;flags&gt;...]
 [COMPILE_DEFINITIONS &lt;defs&gt;...]
 [LINK_LIBRARIES &lt;libs&gt;...]
 [COMPILE_OUTPUT_VARIABLE &lt;var&gt;]
 [RUN_OUTPUT_VARIABLE &lt;var&gt;]
 [OUTPUT_VARIABLE &lt;var&gt;]
 [ARGS &lt;args&gt;...])</pre>
<p>Try compiling a <code>&lt;srcfile&gt;</code>. Returns <code>TRUE</code> or <code>FALSE</code> for success or failure in <code>COMPILE_RESULT_VAR</code>. If the compile succeeded, runs the executable and returns its exit code in <code>RUN_RESULT_VAR</code>. If the executable was built, but failed to run, then <code>RUN_RESULT_VAR</code> will be set to <code>FAILED_TO_RUN</code>. See the <code>try_compile()</code> command for information on how the test project is constructed to build the source file. </p>
<p> The options are:</p>
<dl>
<dt><code>CMAKE_FLAGS &lt;flags&gt;&#8230;</code></p>
<dd>Specify flags of the form <code>-DVAR:TYPE=VALUE</code> to be passed to the <code>cmake3</code> command-line used to drive the test build. The example in <code>try_compile()</code> shows how values for variables <code>INCLUDE_DIRECTORIES</code>, <code>LINK_DIRECTORIES</code>, and <code>LINK_LIBRARIES</code> are used.</p>
<dt><code>COMPILE_DEFINITIONS &lt;defs&gt;&#8230;</code></p>
<dd>Specify <code>-Ddefinition</code> arguments to pass to <code>add_definitions</code> in the generated test project.</p>
<dt><code>COMPILE_OUTPUT_VARIABLE &lt;var&gt;</code></p>
<dd>Report the compile step build output in a given variable.</p>
<dt><code>LINK_LIBRARIES &lt;libs&gt;&#8230;</code></p>
<dd>Specify libraries to be linked in the generated project. The list of libraries may refer to system libraries and to <i>Imported Targets</i> from the calling project. </p>
<p> If this option is specified, any <code>-DLINK_LIBRARIES=&#8230;</code> value given to the <code>CMAKE_FLAGS</code> option will be ignored.</p>
<dt><code>OUTPUT_VARIABLE &lt;var&gt;</code></p>
<dd>Report the compile build output and the output from running the executable in the given variable. This option exists for legacy reasons. Prefer <code>COMPILE_OUTPUT_VARIABLE</code> and <code>RUN_OUTPUT_VARIABLE</code> instead.</p>
<dt><code>RUN_OUTPUT_VARIABLE &lt;var&gt;</code></p>
<dd>Report the output from running the executable in a given variable.</dl>
<h3>Other Behavior Settings</h3>
<p>Set the <code>CMAKE_TRY_COMPILE_CONFIGURATION</code> variable to choose a build configuration.</p>
<h3>Behavior when Cross Compiling</h3>
<p>When cross compiling, the executable compiled in the first step usually cannot be run on the build host. The <code>try_run</code> command checks the <code>CMAKE_CROSSCOMPILING</code> variable to detect whether CMake is in cross-compiling mode. If that is the case, it will still try to compile the executable, but it will not try to run the executable unless the <code>CMAKE_CROSSCOMPILING_EMULATOR</code> variable is set. Instead it will create cache variables which must be filled by the user or by presetting them in some CMake script file to the values the executable would have produced if it had been run on its actual target platform. These cache entries are:</p>
<dl>
<dt><code>&lt;RUN_RESULT_VAR&gt;</code></p>
<dd>Exit code if the executable were to be run on the target platform.</p>
<dt><code>&lt;RUN_RESULT_VAR&gt;__TRYRUN_OUTPUT</code></p>
<dd>Output from stdout and stderr if the executable were to be run on the target platform. This is created only if the <code>RUN_OUTPUT_VARIABLE</code> or <code>OUTPUT_VARIABLE</code> option was used. </p>
<p> In order to make cross compiling your project easier, use <code>try_run</code> only if really required. If you use <code>try_run</code>, use the <code>RUN_OUTPUT_VARIABLE</code> or <code>OUTPUT_VARIABLE</code> options only if really required. Using them will require that when cross-compiling, the cache variables will have to be set manually to the output of the executable. You can also &quot;guard&quot; the calls to <code>try_run</code> with an <code>if()</code> block checking the <code>CMAKE_CROSSCOMPILING</code> variable and provide an easy-to-preset alternative for this case.</dl>
<h3>unset</h3>
<p>Unset a variable, cache variable, or environment variable. </p>
<pre>unset(&lt;variable&gt; [CACHE | PARENT_SCOPE])</pre>
<p>Removes the specified variable causing it to become undefined. If <code>CACHE</code> is present then the variable is removed from the cache instead of the current scope. </p>
<p> If <code>PARENT_SCOPE</code> is present then the variable is removed from the scope above the current scope. See the same option in the <code>set()</code> command for further details. </p>
<p> <code>&lt;variable&gt;</code> can be an environment variable such as: </p>
<pre>unset(ENV{LD_LIBRARY_PATH})</pre>
<p>in which case the variable will be removed from the current environment.</p>
<h3>variable_watch</h3>
<p>Watch the CMake variable for change. </p>
<pre>variable_watch(&lt;variable name&gt; [&lt;command to execute&gt;])</pre>
<p>If the specified variable changes, the message will be printed about the variable being changed. If the command is specified, the command will be executed. The command will receive the following arguments: COMMAND(&lt;variable&gt; &lt;access&gt; &lt;value&gt; &lt;current list file&gt; &lt;stack&gt;)</p>
<h3>while</h3>
<p>Evaluate a group of commands while a condition is true </p>
<pre>while(condition)
 COMMAND1(ARGS ...)
 COMMAND2(ARGS ...)
 ...
endwhile(condition)</pre>
<p>All commands between while and the matching <code>endwhile()</code> are recorded without being invoked. Once the <code>endwhile()</code> is evaluated, the recorded list of commands is invoked as long as the condition is true. The condition is evaluated using the same logic as the <code>if()</code> command.</p>
<h2>Deprecated Commands</h2>
<p>These commands are available only for compatibility with older versions of CMake. Do not use them in new code.</p>
<h3>build_name</h3>
<p>Disallowed. See CMake Policy <code>CMP0036</code>. </p>
<p> Use <code>${CMAKE_SYSTEM}</code> and <code>${CMAKE_CXX_COMPILER}</code> instead. </p>
<pre>build_name(variable)</pre>
<p>Sets the specified variable to a string representing the platform and compiler settings. These values are now available through the <code>CMAKE_SYSTEM</code> and <code>CMAKE_CXX_COMPILER</code> variables.</p>
<h3>exec_program</h3>
<p>Deprecated. Use the <code>execute_process()</code> command instead. </p>
<p> Run an executable program during the processing of the CMakeList.txt file. </p>
<pre>exec_program(Executable [directory in which to run]
 [ARGS &lt;arguments to executable&gt;]
 [OUTPUT_VARIABLE &lt;var&gt;]
 [RETURN_VALUE &lt;var&gt;])</pre>
<p>The executable is run in the optionally specified directory. The executable can include arguments if it is double quoted, but it is better to use the optional <code>ARGS</code> argument to specify arguments to the program. This is because cmake will then be able to escape spaces in the executable path. An optional argument <code>OUTPUT_VARIABLE</code> specifies a variable in which to store the output. To capture the return value of the execution, provide a <code>RETURN_VALUE</code>. If <code>OUTPUT_VARIABLE</code> is specified, then no output will go to the stdout/stderr of the console running cmake.</p>
<h3>export_library_dependencies</h3>
<p>Disallowed. See CMake Policy <code>CMP0033</code>. </p>
<p> Use <code>install(EXPORT)</code> or <code>export()</code> command. </p>
<p> This command generates an old-style library dependencies file. Projects requiring CMake 2.6 or later should not use the command. Use instead the <code>install(EXPORT)</code> command to help export targets from an installation tree and the <code>export()</code> command to export targets from a build tree. </p>
<p> The old-style library dependencies file does not take into account per-configuration names of libraries or the <code>LINK_INTERFACE_LIBRARIES</code> target property. </p>
<pre>export_library_dependencies(&lt;file&gt; [APPEND])</pre>
<p>Create a file named <code>&lt;file&gt;</code> that can be included into a CMake listfile with the INCLUDE command. The file will contain a number of SET commands that will set all the variables needed for library dependency information. This should be the last command in the top level CMakeLists.txt file of the project. If the <code>APPEND</code> option is specified, the SET commands will be appended to the given file instead of replacing it.</p>
<h3>install_files</h3>
<p>Deprecated. Use the <code>install(FILES)</code> command instead. </p>
<p> This command has been superceded by the <code>install()</code> command. It is provided for compatibility with older CMake code. The <code>FILES</code> form is directly replaced by the <code>FILES</code> form of the <code>install()</code> command. The regexp form can be expressed more clearly using the <code>GLOB</code> form of the <code>file()</code> command. </p>
<pre>install_files(&lt;dir&gt; extension file file ...)</pre>
<p>Create rules to install the listed files with the given extension into the given directory. Only files existing in the current source tree or its corresponding location in the binary tree may be listed. If a file specified already has an extension, that extension will be removed first. This is useful for providing lists of source files such as foo.cxx when you want the corresponding foo.h to be installed. A typical extension is &#8216;.h&#8217;. </p>
<pre>install_files(&lt;dir&gt; regexp)</pre>
<p>Any files in the current source directory that match the regular expression will be installed. </p>
<pre>install_files(&lt;dir&gt; FILES file file ...)</pre>
<p>Any files listed after the <code>FILES</code> keyword will be installed explicitly from the names given. Full paths are allowed in this form. </p>
<p> The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>.</p>
<h3>install_programs</h3>
<p>Deprecated. Use the <code>install(PROGRAMS)</code> command instead. </p>
<p> This command has been superceded by the <code>install()</code> command. It is provided for compatibility with older CMake code. The <code>FILES</code> form is directly replaced by the <code>PROGRAMS</code> form of the <code>install()</code> command. The regexp form can be expressed more clearly using the <code>GLOB</code> form of the <code>file()</code> command. </p>
<pre>install_programs(&lt;dir&gt; file1 file2 [file3 ...])
install_programs(&lt;dir&gt; FILES file1 [file2 ...])</pre>
<p>Create rules to install the listed programs into the given directory. Use the <code>FILES</code> argument to guarantee that the file list version of the command will be used even when there is only one argument. </p>
<pre>install_programs(&lt;dir&gt; regexp)</pre>
<p>In the second form any program in the current source directory that matches the regular expression will be installed. </p>
<p> This command is intended to install programs that are not built by cmake, such as shell scripts. See the <code>TARGETS</code> form of the <code>install()</code> command to create installation rules for targets built by cmake. </p>
<p> The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>.</p>
<h3>install_targets</h3>
<p>Deprecated. Use the <code>install(TARGETS)</code> command instead. </p>
<p> This command has been superceded by the <code>install()</code> command. It is provided for compatibility with older CMake code. </p>
<pre>install_targets(&lt;dir&gt; [RUNTIME_DIRECTORY dir] target target)</pre>
<p>Create rules to install the listed targets into the given directory. The directory <code>&lt;dir&gt;</code> is relative to the installation prefix, which is stored in the variable <code>CMAKE_INSTALL_PREFIX</code>. If <code>RUNTIME_DIRECTORY</code> is specified, then on systems with special runtime files (Windows DLL), the files will be copied to that directory.</p>
<h3>load_command</h3>
<p>Disallowed. See CMake Policy <code>CMP0031</code>. </p>
<p> Load a command into a running CMake. </p>
<pre>load_command(COMMAND_NAME &lt;loc1&gt; [loc2 ...])</pre>
<p>The given locations are searched for a library whose name is cmCOMMAND_NAME. If found, it is loaded as a module and the command is added to the set of available CMake commands. Usually, <code>try_compile()</code> is used before this command to compile the module. If the command is successfully loaded a variable named </p>
<pre>CMAKE_LOADED_COMMAND_&lt;COMMAND_NAME&gt;</pre>
<p>will be set to the full path of the module that was loaded. Otherwise the variable will not be set.</p>
<h3>make_directory</h3>
<p>Deprecated. Use the <code>file(MAKE_DIRECTORY)</code> command instead. </p>
<pre>make_directory(directory)</pre>
<p>Creates the specified directory. Full paths should be given. Any parent directories that do not exist will also be created. Use with care.</p>
<h3>output_required_files</h3>
<p>Disallowed. See CMake Policy <code>CMP0032</code>. </p>
<p> Approximate C preprocessor dependency scanning. </p>
<p> This command exists only because ancient CMake versions provided it. CMake handles preprocessor dependency scanning automatically using a more advanced scanner. </p>
<pre>output_required_files(srcfile outputfile)</pre>
<p>Outputs a list of all the source files that are required by the specified srcfile. This list is written into outputfile. This is similar to writing out the dependencies for srcfile except that it jumps from .h files into .cxx, .c and .cpp files if possible.</p>
<h3>remove</h3>
<p>Deprecated. Use the <code>list(REMOVE_ITEM)</code> command instead. </p>
<pre>remove(VAR VALUE VALUE ...)</pre>
<p>Removes <code>VALUE</code> from the variable <code>VAR</code>. This is typically used to remove entries from a vector (e.g. semicolon separated list). <code>VALUE</code> is expanded.</p>
<h3>subdir_depends</h3>
<p>Disallowed. See CMake Policy <code>CMP0029</code>. </p>
<p> Does nothing. </p>
<pre>subdir_depends(subdir dep1 dep2 ...)</pre>
<p>Does not do anything. This command used to help projects order parallel builds correctly. This functionality is now automatic.</p>
<h3>subdirs</h3>
<p>Deprecated. Use the <code>add_subdirectory()</code> command instead. </p>
<p> Add a list of subdirectories to the build. </p>
<pre>subdirs(dir1 dir2 ...[EXCLUDE_FROM_ALL exclude_dir1 exclude_dir2 ...]
 [PREORDER] )</pre>
<p>Add a list of subdirectories to the build. The <code>add_subdirectory()</code> command should be used instead of <code>subdirs</code> although <code>subdirs</code> will still work. This will cause any CMakeLists.txt files in the sub directories to be processed by CMake. Any directories after the <code>PREORDER</code> flag are traversed first by makefile builds, the <code>PREORDER</code> flag has no effect on IDE projects. Any directories after the <code>EXCLUDE_FROM_ALL</code> marker will not be included in the top level makefile or project file. This is useful for having CMake create makefiles or projects for a set of examples in a project. You would want CMake to generate makefiles or project files for all the examples at the same time, but you would not want them to show up in the top level project or be built each time make is run from the top.</p>
<h3>use_mangled_mesa</h3>
<p>Disallowed. See CMake Policy <code>CMP0030</code>. </p>
<p> Copy mesa headers for use in combination with system GL. </p>
<pre>use_mangled_mesa(PATH_TO_MESA OUTPUT_DIRECTORY)</pre>
<p>The path to mesa includes, should contain gl_mangle.h. The mesa headers are copied to the specified output directory. This allows mangled mesa headers to override other GL headers by being added to the include directory path earlier.</p>
<h3>utility_source</h3>
<p>Disallowed. See CMake Policy <code>CMP0034</code>. </p>
<p> Specify the source tree of a third-party utility. </p>
<pre>utility_source(cache_entry executable_name
 path_to_source [file1 file2 ...])</pre>
<p>When a third-party utility&#8217;s source is included in the distribution, this command specifies its location and name. The cache entry will not be set unless the <code>path_to_source</code> and all listed files exist. It is assumed that the source tree of the utility will have been built before it is needed. </p>
<p> When cross compiling CMake will print a warning if a <code>utility_source()</code> command is executed, because in many cases it is used to build an executable which is executed later on. This doesn&#8217;t work when cross compiling, since the executable can run only on their target platform. So in this case the cache entry has to be adjusted manually so it points to an executable which is runnable on the build host.</p>
<h3>variable_requires</h3>
<p>Disallowed. See CMake Policy <code>CMP0035</code>. </p>
<p> Use the <code>if()</code> command instead. </p>
<p> Assert satisfaction of an option&#8217;s required variables. </p>
<pre>variable_requires(TEST_VARIABLE RESULT_VARIABLE
 REQUIRED_VARIABLE1
 REQUIRED_VARIABLE2 ...)</pre>
<p>The first argument (<code>TEST_VARIABLE</code>) is the name of the variable to be tested, if that variable is false nothing else is done. If <code>TEST_VARIABLE</code> is true, then the next argument (<code>RESULT_VARIABLE</code>) is a variable that is set to true if all the required variables are set. The rest of the arguments are variables that must be true or not set to NOTFOUND to avoid an error. If any are not true, an error is reported.</p>
<h3>write_file</h3>
<p>Deprecated. Use the <code>file(WRITE)</code> command instead. </p>
<pre>write_file(filename &quot;message to write&quot;... [APPEND])</pre>
<p>The first argument is the file name, the rest of the arguments are messages to write. If the argument <code>APPEND</code> is specified, then the message will be appended. </p>
<p> NOTE 1: <code>file(WRITE)</code> and <code>file(APPEND)</code> do exactly the same as this one but add some more functionality. </p>
<p> NOTE 2: When using <code>write_file</code> the produced file cannot be used as an input to CMake (CONFIGURE_FILE, source file &#8230;) because it will lead to an infinite loop. Use <code>configure_file()</code> if you want to generate input files to CMake.</p>
<h2>Ctest Commands</h2>
<p>These commands are available only in ctest scripts.</p>
<h3>ctest_build</h3>
<p>Perform the <i>CTest Build Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_build([BUILD &lt;build-dir&gt;] [APPEND]
 [CONFIGURATION &lt;config&gt;]
 [FLAGS &lt;flags&gt;]
 [PROJECT_NAME &lt;project-name&gt;]
 [TARGET &lt;target-name&gt;]
 [NUMBER_ERRORS &lt;num-err-var&gt;]
 [NUMBER_WARNINGS &lt;num-warn-var&gt;]
 [RETURN_VALUE &lt;result-var&gt;]
 )</pre>
<p>Build the project and store results in <code>Build.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The <code>CTEST_BUILD_COMMAND</code> variable may be set to explicitly specify the build command line. Otherwise the build command line is computed automatically based on the options given. </p>
<p> The options are:</p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></p>
<dd>Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used.</p>
<dt><code>APPEND</code></p>
<dd>Mark results for append to those previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use.</p>
<dt><code>CONFIGURATION &lt;config&gt;</code></p>
<dd>Specify the build configuration (e.g. <code>Debug</code>). If not specified the <code>CTEST_BUILD_CONFIGURATION</code> variable will be checked. Otherwise the <code>-C &lt;cfg&gt;</code> option given to the <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> command will be used, if any.</p>
<dt><code>FLAGS &lt;flags&gt;</code></p>
<dd>Pass additional arguments to the underlying build command. If not specified the <code>CTEST_BUILD_FLAGS</code> variable will be checked. This can, e.g., be used to trigger a parallel build using the <code>-j</code> option of make. See the <code>ProcessorCount</code> module for an example.</p>
<dt><code>PROJECT_NAME &lt;project-name&gt;</code></p>
<dd>Set the name of the project to build. This should correspond to the top-level call to the <code>project()</code> command. If not specified the <code>CTEST_PROJECT_NAME</code> variable will be checked.</p>
<dt><code>TARGET &lt;target-name&gt;</code></p>
<dd>Specify the name of a target to build. If not specified the <code>CTEST_BUILD_TARGET</code> variable will be checked. Otherwise the default target will be built. This is the &quot;all&quot; target (called <code>ALL_BUILD</code> in <i>Visual Studio Generators</i>).</p>
<dt><code>NUMBER_ERRORS &lt;num-err-var&gt;</code></p>
<dd>Store the number of build errors detected in the given variable.</p>
<dt><code>NUMBER_WARNINGS &lt;num-warn-var&gt;</code></p>
<dd>Store the number of build warnings detected in the given variable.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store the return value of the native build tool in the given variable.</p>
<dt><code>QUIET</code></p>
<dd>Suppress any CTest-specific non-error output that would have been printed to the console otherwise. The summary of warnings / errors, as well as the output from the native build tool is unaffected by this option.</dl>
<h3>ctest_configure</h3>
<p>Perform the <i>CTest Configure Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_configure([BUILD &lt;build-dir&gt;] [SOURCE &lt;source-dir&gt;] [APPEND]
 [OPTIONS &lt;options&gt;] [RETURN_VALUE &lt;result-var&gt;] [QUIET])</pre>
<p>Configure the project build tree and record results in <code>Configure.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The options are:</p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></p>
<dd>Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used.</p>
<dt><code>SOURCE &lt;source-dir&gt;</code></p>
<dd>Specify the source directory. If not given, the <code>CTEST_SOURCE_DIRECTORY</code> variable is used.</p>
<dt><code>APPEND</code></p>
<dd>Mark results for append to those previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use.</p>
<dt><code>OPTIONS &lt;options&gt;</code></p>
<dd>Specify command-line arguments to pass to the configuration tool.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store in the <code>&lt;result-var&gt;</code> variable the return value of the native configuration tool.</p>
<dt><code>QUIET</code></p>
<dd>Suppress any CTest-specific non-error messages that would have otherwise been printed to the console. Output from the underlying configure command is not affected.</dl>
<h3>ctest_coverage</h3>
<p>Perform the <i>CTest Coverage Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_coverage([BUILD &lt;build-dir&gt;] [APPEND]
 [LABELS &lt;label&gt;...]
 [RETURN_VALUE &lt;result-var&gt;]
 [QUIET]
 )</pre>
<p>Collect coverage tool results and stores them in <code>Coverage.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The options are:</p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></p>
<dd>Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used.</p>
<dt><code>APPEND</code></p>
<dd>Mark results for append to those previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use.</p>
<dt><code>LABELS</code></p>
<dd>Filter the coverage report to include only source files labeled with at least one of the labels specified.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> if coverage tools ran without error and non-zero otherwise.</p>
<dt><code>QUIET</code></p>
<dd>Suppress any CTest-specific non-error output that would have been printed to the console otherwise. The summary indicating how many lines of code were covered is unaffected by this option.</dl>
<h3>ctest_empty_binary_directory</h3>
<p>empties the binary directory </p>
<pre>ctest_empty_binary_directory( directory )</pre>
<p>Removes a binary directory. This command will perform some checks prior to deleting the directory in an attempt to avoid malicious or accidental directory deletion.</p>
<h3>ctest_memcheck</h3>
<p>Perform the <i>CTest MemCheck Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_memcheck([BUILD &lt;build-dir&gt;] [APPEND]
 [START &lt;start-number&gt;]
 [END &lt;end-number&gt;]
 [STRIDE &lt;stride-number&gt;]
 [EXCLUDE &lt;exclude-regex&gt;]
 [INCLUDE &lt;include-regex&gt;]
 [EXCLUDE_LABEL &lt;label-exclude-regex&gt;]
 [INCLUDE_LABEL &lt;label-include-regex&gt;]
 [PARALLEL_LEVEL &lt;level&gt;]
 [TEST_LOAD &lt;threshold&gt;]
 [SCHEDULE_RANDOM &lt;ON|OFF&gt;]
 [STOP_TIME &lt;time-of-day&gt;]
 [RETURN_VALUE &lt;result-var&gt;]
 [QUIET]
 )</pre>
<p>Run tests with a dynamic analysis tool and store results in <code>MemCheck.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The options are the same as those for the <code>ctest_test()</code> command.</p>
<h3>ctest_read_custom_files</h3>
<p>read CTestCustom files. </p>
<pre>ctest_read_custom_files( directory ... )</pre>
<p>Read all the CTestCustom.ctest or CTestCustom.cmake files from the given directory. </p>
<p> By default, invoking <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code> without a script will read custom files from the binary directory.</p>
<h3>ctest_run_script</h3>
<p>runs a ctest -S script </p>
<pre>ctest_run_script([NEW_PROCESS] script_file_name script_file_name1
 script_file_name2 ... [RETURN_VALUE var])</pre>
<p>Runs a script or scripts much like if it was run from ctest -S. If no argument is provided then the current script is run using the current settings of the variables. If <code>NEW_PROCESS</code> is specified then each script will be run in a separate process.If <code>RETURN_VALUE</code> is specified the return value of the last script run will be put into <code>var</code>.</p>
<h3>ctest_sleep</h3>
<p>sleeps for some amount of time </p>
<pre>ctest_sleep(&lt;seconds&gt;)</pre>
<p>Sleep for given number of seconds. </p>
<pre>ctest_sleep(&lt;time1&gt; &lt;duration&gt; &lt;time2&gt;)</pre>
<p>Sleep for t=(time1 + duration &#8211; time2) seconds if t &gt; 0.</p>
<h3>ctest_start</h3>
<p>Starts the testing for a given model </p>
<pre>ctest_start(Model [TRACK &lt;track&gt;] [APPEND] [source [binary]] [QUIET])</pre>
<p>Starts the testing for a given model. The command should be called after the binary directory is initialized. If the &#8216;source&#8217; and &#8216;binary&#8217; directory are not specified, it reads the <code>CTEST_SOURCE_DIRECTORY</code> and <code>CTEST_BINARY_DIRECTORY</code>. If the track is specified, the submissions will go to the specified track. If APPEND is used, the existing TAG is used rather than creating a new one based on the current time stamp. If <code>QUIET</code> is used, CTest will suppress any non-error messages that it otherwise would have printed to the console. </p>
<p> If the <code>CTEST_CHECKOUT_COMMAND</code> variable (or the <code>CTEST_CVS_CHECKOUT</code> variable) is set, its content is treated as command-line. The command is invoked with the current working directory set to the parent of the source directory, even if the source directory already exists. This can be used to create the source tree from a version control repository.</p>
<h3>ctest_submit</h3>
<p>Perform the <i>CTest Submit Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_submit([PARTS &lt;part&gt;...] [FILES &lt;file&gt;...]
 [RETRY_COUNT &lt;count&gt;]
 [RETRY_DELAY &lt;delay&gt;]
 [RETURN_VALUE &lt;result-var&gt;]
 [QUIET]
 )</pre>
<p>Submit results to a dashboard server. By default all available parts are submitted. </p>
<p> The options are:</p>
<dl>
<dt><code>PARTS &lt;part&gt;&#8230;</code></p>
<dd>Specify a subset of parts to submit. Valid part names are: </p>
<pre>Start = nothing
Update = ctest_update results, in Update.xml
Configure = ctest_configure results, in Configure.xml
Build = ctest_build results, in Build.xml
Test = ctest_test results, in Test.xml
Coverage = ctest_coverage results, in Coverage.xml
MemCheck = ctest_memcheck results, in DynamicAnalysis.xml
Notes = Files listed by CTEST_NOTES_FILES, in Notes.xml
ExtraFiles = Files listed by CTEST_EXTRA_SUBMIT_FILES
Upload = Files prepared for upload by ctest_upload(), in Upload.xml
Submit = nothing</pre>
<dt><code>FILES &lt;file&gt;&#8230;</code></p>
<dd>Specify an explicit list of specific files to be submitted. Each individual file must exist at the time of the call.</p>
<dt><code>RETRY_COUNT &lt;count&gt;</code></p>
<dd>Specify how many times to retry a timed-out submission.</p>
<dt><code>RETRY_DELAY &lt;delay&gt;</code></p>
<dd>Specify how long (in seconds) to wait after a timed-out submission before attempting to re-submit.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> for success and non-zero on failure.</p>
<dt><code>QUIET</code></p>
<dd>Suppress all non-error messages that would have otherwise been printed to the console.</dl>
<h3>Submit to CDash Upload API</h3>
<pre>ctest_submit(CDASH_UPLOAD &lt;file&gt; [CDASH_UPLOAD_TYPE &lt;type&gt;])</pre>
<p>This second signature is used to upload files to CDash via the CDash file upload API. The api first sends a request to upload to CDash along with a content hash of the file. If CDash does not already have the file, then it is uploaded. Along with the file, a CDash type string is specified to tell CDash which handler to use to process the data.</p>
<h3>ctest_test</h3>
<p>Perform the <i>CTest Test Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_test([BUILD &lt;build-dir&gt;] [APPEND]
 [START &lt;start-number&gt;]
 [END &lt;end-number&gt;]
 [STRIDE &lt;stride-number&gt;]
 [EXCLUDE &lt;exclude-regex&gt;]
 [INCLUDE &lt;include-regex&gt;]
 [EXCLUDE_LABEL &lt;label-exclude-regex&gt;]
 [INCLUDE_LABEL &lt;label-include-regex&gt;]
 [PARALLEL_LEVEL &lt;level&gt;]
 [TEST_LOAD &lt;threshold&gt;]
 [SCHEDULE_RANDOM &lt;ON|OFF&gt;]
 [STOP_TIME &lt;time-of-day&gt;]
 [RETURN_VALUE &lt;result-var&gt;]
 [QUIET]
 )</pre>
<p>Run tests in the project build tree and store results in <code>Test.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The options are:</p>
<dl>
<dt><code>BUILD &lt;build-dir&gt;</code></p>
<dd>Specify the top-level build directory. If not given, the <code>CTEST_BINARY_DIRECTORY</code> variable is used.</p>
<dt><code>APPEND</code></p>
<dd>Mark results for append to those previously submitted to a dashboard server since the last <code>ctest_start()</code> call. Append semantics are defined by the dashboard server in use.</p>
<dt><code>START &lt;start-number&gt;</code></p>
<dd>Specify the beginning of a range of test numbers.</p>
<dt><code>END &lt;end-number&gt;</code></p>
<dd>Specify the end of a range of test numbers.</p>
<dt><code>STRIDE &lt;stride-number&gt;</code></p>
<dd>Specify the stride by which to step across a range of test numbers.</p>
<dt><code>EXCLUDE &lt;exclude-regex&gt;</code></p>
<dd>Specify a regular expression matching test names to exclude.</p>
<dt><code>INCLUDE &lt;include-regex&gt;</code></p>
<dd>Specify a regular expression matching test names to include. Tests not matching this expression are excluded.</p>
<dt><code>EXCLUDE_LABEL &lt;label-exclude-regex&gt;</code></p>
<dd>Specify a regular expression matching test labels to exclude.</p>
<dt><code>INCLUDE_LABEL &lt;label-include-regex&gt;</code></p>
<dd>Specify a regular expression matching test labels to include. Tests not matching this expression are excluded.</p>
<dt><code>PARALLEL_LEVEL &lt;level&gt;</code></p>
<dd>Specify a positive number representing the number of tests to be run in parallel.</p>
<dt><code>TEST_LOAD &lt;threshold&gt;</code></p>
<dd>While running tests in parallel, try not to start tests when they may cause the CPU load to pass above a given threshold. If not specified the <code>CTEST_TEST_LOAD</code> variable will be checked, and then the <code>&#8211;test-load</code> command-line argument to <code><a href="/docs/linux/man/1-ctest3/">ctest3</a>(1)</code>. See also the <code>TestLoad</code> setting in the <i>CTest Test Step</i>.</p>
<dt><code>SCHEDULE_RANDOM &lt;ON|OFF&gt;</code></p>
<dd>Launch tests in a random order. This may be useful for detecting implicit test dependencies.</p>
<dt><code>STOP_TIME &lt;time-of-day&gt;</code></p>
<dd>Specify a time of day at which the tests should all stop running.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store in the <code>&lt;result-var&gt;</code> variable <code>0</code> if all tests passed. Store non-zero if anything went wrong.</p>
<dt><code>QUIET</code></p>
<dd>Suppress any CTest-specific non-error messages that would have otherwise been printed to the console. Output from the underlying test command is not affected. Summary info detailing the percentage of passing tests is also unaffected by the <code>QUIET</code> option. </p>
<p> See also the <code>CTEST_CUSTOM_MAXIMUM_PASSED_TEST_OUTPUT_SIZE</code> and <code>CTEST_CUSTOM_MAXIMUM_FAILED_TEST_OUTPUT_SIZE</code> variables.</dl>
<h3>ctest_update</h3>
<p>Perform the <i>CTest Update Step</i> as a <i>Dashboard Client</i>. </p>
<pre>ctest_update([SOURCE &lt;source-dir&gt;] [RETURN_VALUE &lt;result-var&gt;] [QUIET])</pre>
<p>Update the source tree from version control and record results in <code>Update.xml</code> for submission with the <code>ctest_submit()</code> command. </p>
<p> The options are:</p>
<dl>
<dt><code>SOURCE &lt;source-dir&gt;</code></p>
<dd>Specify the source directory. If not given, the <code>CTEST_SOURCE_DIRECTORY</code> variable is used.</p>
<dt><code>RETURN_VALUE &lt;result-var&gt;</code></p>
<dd>Store in the <code>&lt;result-var&gt;</code> variable the number of files updated or <code>-1</code> on error.</p>
<dt><code>QUIET</code></p>
<dd>Tell CTest to suppress most non-error messages that it would have otherwise printed to the console. CTest will still report the new revision of the repository and any conflicting files that were found. </p>
<p> The update always follows the version control branch currently checked out in the source directory. See the <i>CTest Update Step</i> documentation for more information.</dl>
<h3>ctest_upload</h3>
<p>Upload files to a dashboard server as a <i>Dashboard Client</i>. </p>
<pre>ctest_upload(FILES &lt;file&gt;... [QUIET])</pre>
<p>The options are:</p>
<dl>
<dt><code>FILES &lt;file&gt;&#8230;</code></p>
<dd>Specify a list of files to be sent along with the build results to the dashboard server.</p>
<dt><code>QUIET</code></p>
<dd>Suppress any CTest-specific non-error output that would have been printed to the console otherwise.</dl>
<h2>Copyright</h2>
<p>2000-2016 Kitware, Inc.</p>
