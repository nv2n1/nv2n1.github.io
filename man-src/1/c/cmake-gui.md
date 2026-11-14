---
title: "cmake-gui(1)"
name: "cmake-gui"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmake-gui/"
description: "cmake-gui - CMake GUI. USAGE cmake - gui[options] cmake - gui[options]<path - to - source> cmake - gui[options]<path - to - existing - build> DESCRIPTION The \"cmake-gui\" executable is the CMake GUI..."
---

<h2>NAME</h2>
<pre>
  cmake-gui - CMake GUI.
</pre>
<h2>USAGE</h2>
<pre><code>
cmake - gui[options] cmake - gui[options]&lt;path - to - source&gt; cmake - gui[options]&lt;path - to - existing - build&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The &quot;cmake-gui&quot; executable is the CMake GUI. Project configuration settings may be specified interactively. Brief instructions are provided at the bottom of the window when the program is running. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;copyright [file]</code></p>
<dd> Print the CMake copyright and exit. </p>
<p> If a file is specified, the copyright is written into it. </p>
<dt><code>&#8211;help</code></p>
<dd> Print usage information and exit. </p>
<p> Usage describes the basic command line interface and its options. </p>
<dt><code>&#8211;help-full [file]</code></p>
<dd> Print full help and exit. </p>
<p> Full help displays most of the documentation provided by the UNIX man page. It is provided for use on non-UNIX platforms, but is also convenient if the man page is not installed. If a file is specified, the help is written into it. </p>
<dt><code>&#8211;help-html [file]</code></p>
<dd> Print full help in HTML format. </p>
<p> This option is used by CMake authors to help produce web pages. If a file is specified, the help is written into it. </p>
<dt><code>&#8211;help-man [file]</code></p>
<dd> Print full help as a UNIX man page and exit. </p>
<p> This option is used by the cmake build to generate the UNIX man page. If a file is specified, the help is written into it. </p>
<dt><code>&#8211;version [file]</code></p>
<dd> Show program name/version banner and exit. </p>
<p> If a file is specified, the version is written into it. </p>
</dl>
<h2>GENERATORS</h2>
<p> The following generators are available on this platform: </p>
<dl>
<dt><code>Unix Makefiles</code></p>
<dd> Generates standard UNIX makefiles. </p>
<p> A hierarchy of UNIX makefiles is generated into the build tree. Any standard UNIX-style make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<dt><code>CodeBlocks &#8211; Unix Makefiles</code></p>
<dd> Generates CodeBlocks project files. </p>
<p> Project files for CodeBlocks will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<dt><code>Eclipse CDT4 &#8211; Unix Makefiles</code></p>
<dd> Generates Eclipse CDT 4.0 project files. </p>
<p> Project files for Eclipse will be created in the top directory and will have a linked resource to every subdirectory which features a CMakeLists.txt file containing a PROJECT() call.Additionally a hierarchy of makefiles is generated into the build tree. The appropriate make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<dt><code>KDevelop3</code></p>
<dd> Generates KDevelop 3 project files. </p>
<p> Project files for KDevelop 3 will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. If you change the settings using KDevelop cmake will try its best to keep your changes when regenerating the project files. Additionally a hierarchy of UNIX makefiles is generated into the build tree. Any standard UNIX-style make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
<dt><code>KDevelop3 &#8211; Unix Makefiles</code></p>
<dd> Generates KDevelop 3 project files. </p>
<p> Project files for KDevelop 3 will be created in the top directory and in every subdirectory which features a CMakeLists.txt file containing a PROJECT() call. If you change the settings using KDevelop cmake will try its best to keep your changes when regenerating the project files. Additionally a hierarchy of UNIX makefiles is generated into the build tree. Any standard UNIX-style make program can build the project through the default make target. A &quot;make install&quot; target is also provided. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>add_custom_command</code></p>
<dd> Add a custom build rule to the generated build system. </p>
<p> There are two main signatures for add_custom_command The first signature is for adding a custom command to produce an output. </p>
<p>add_custom_command(OUTPUT output1[output2&#8230;] COMMAND command1[ARGS][args1&#8230;]<br />
                                                              [COMMAND command2[ARGS][args2&#8230;]&#8230;]<br />
                                                              [MAIN_DEPENDENCY depend]<br />
                                                              [DEPENDS[depends&#8230;]]<br />
                                                              [IMPLICIT_DEPENDS&lt;lang1&gt; depend1&#8230;]<br />
                                                              [WORKING_DIRECTORY dir]<br />
                                                              [COMMENT comment][VERBATIM][APPEND])</p>
<p> This defines a command to generate specified OUTPUT file(s). A target created in the same directory (CMakeLists.txt file) that specifies any output of the custom command as a source file is given a rule to generate the file using the command at build time. If an output name is a relative path it will be interpreted relative to the build tree directory corresponding to the current source directory. Note that MAIN_DEPENDENCY is completely optional and is used as a suggestion to visual studio about where to hang the custom command. In makefile terms this creates a new target in the following form: </p>
<pre>
  OUTPUT: MAIN_DEPENDENCY DEPENDS
          COMMAND
</pre>
<p> If more than one command is specified they will be executed in order. The optional ARGS argument is for backward compatibility and will be ignored. </p>
<p> The second signature adds a custom command to a target such as a library or executable. This is useful for performing an operation before or after building the target. The command becomes part of the target and will only execute when the target itself is built. If the target is already built, the command will not execute. </p>
<p>add_custom_command(TARGET target<br />
                       PRE_BUILD |<br />
                   PRE_LINK | POST_BUILD COMMAND command1[ARGS][args1&#8230;][COMMAND command2[ARGS][args2&#8230;]&#8230;][WORKING_DIRECTORY dir][COMMENT comment][VERBATIM])</p>
<p> This defines a new command that will be associated with building the specified target. When the command will happen is determined by which of the following is specified: </p>
<pre>
  PRE_BUILD - run before all other dependencies
  PRE_LINK - run after other dependencies
  POST_BUILD - run after the target has been built
</pre>
<p> Note that the PRE_BUILD option is only supported on Visual Studio 7 or later. For all other generators PRE_BUILD will be treated as PRE_LINK. </p>
<p> If WORKING_DIRECTORY is specified the command will be executed in the directory given. If COMMENT is set, the value will be displayed as a message before the commands are executed at build time. If APPEND is specified the COMMAND and DEPENDS option values are appended to the custom command for the first output specified. There must have already been a previous call to this command with the same output. The COMMENT, WORKING_DIRECTORY, and MAIN_DEPENDENCY options are currently ignored when APPEND is given, but may be used in the future. </p>
<p> If VERBATIM is given then all arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before add_custom_command even sees the arguments. Use of VERBATIM is recommended as it enables correct behavior. When VERBATIM is not given the behavior is platform specific because there is no protection of tool-specific special characters. </p>
<p> If the output of the custom command is not actually created as a file on disk it should be marked as SYMBOLIC with SET_SOURCE_FILES_PROPERTIES. </p>
<p> The IMPLICIT_DEPENDS option requests scanning of implicit dependencies of an input file. The language given specifies the programming language whose corresponding dependency scanner should be used. Currently only C and CXX language scanners are supported. Dependencies discovered from the scanning are added to those of the custom command at build time. Note that the IMPLICIT_DEPENDS option is currently supported only for Makefile generators and will be ignored by other generators. </p>
<p> If COMMAND specifies an executable target (created by ADD_EXECUTABLE) it will automatically be replaced by the location of the executable created at build time. Additionally a target-level dependency will be added so that the executable target will be built before any target using this custom command. However this does NOT add a file-level dependency that would cause the custom command to re-run whenever the executable is recompiled. </p>
<p> The DEPENDS option specifies files on which the command depends. If any dependency is an OUTPUT of another custom command in the same directory (CMakeLists.txt file) CMake automatically brings the other custom command into the target in which this command is built. If DEPENDS specifies any target (created by an ADD_* command) a target-level dependency is created to make sure the target is built before any target using this custom command. Additionally, if the target is an executable or library a file-level dependency is created to cause the custom command to re-run whenever the target is recompiled. </p>
<dt><code>add_custom_target</code></p>
<dd> Add a target with no output so it will always be built. </p>
<p>add_custom_target(Name[ALL][command1[args1&#8230;]]<br />
                      [COMMAND command2[args2&#8230;]&#8230;]<br />
                      [DEPENDS depend depend depend&#8230;]<br />
                      [WORKING_DIRECTORY dir]<br />
                      [COMMENT comment][VERBATIM]<br />
                      [SOURCES src1[src2&#8230;]])</p>
<p> Adds a target with the given name that executes the given commands. The target has no output file and is ALWAYS CONSIDERED OUT OF DATE even if the commands try to create a file with the name of the target. Use ADD_CUSTOM_COMMAND to generate a file with dependencies. By default nothing depends on the custom target. Use ADD_DEPENDENCIES to add dependencies to or from other targets. If the ALL option is specified it indicates that this target should be added to the default build target so that it will be run every time (the command cannot be called ALL). The command and arguments are optional and if not specified an empty target will be created. If WORKING_DIRECTORY is set, then the command will be run in that directory. If COMMENT is set, the value will be displayed as a message before the commands are executed at build time. Dependencies listed with the DEPENDS argument may reference files and outputs of custom commands created with add_custom_command() in the same directory (CMakeLists.txt file). </p>
<p> If VERBATIM is given then all arguments to the commands will be escaped properly for the build tool so that the invoked command receives each argument unchanged. Note that one level of escapes is still used by the CMake language processor before add_custom_target even sees the arguments. Use of VERBATIM is recommended as it enables correct behavior. When VERBATIM is not given the behavior is platform specific because there is no protection of tool-specific special characters. </p>
<p> The SOURCES option specifies additional source files to be included in the custom target. Specified source files will be added to IDE project files for convenience in editing even if they have not build rules. </p>
<dt><code>add_definitions</code></p>
<dd> Adds -D define flags to the compilation of source files. </p>
<pre>
  add_definitions(-DFOO -DBAR ...)
</pre>
<p> Adds flags to the compiler command line for sources in the current directory and below. This command can be used to add any flags, but it was originally intended to add preprocessor definitions. Flags beginning in -D or /D that look like preprocessor definitions are automatically added to the COMPILE_DEFINITIONS property for the current directory. Definitions with non-trival values may be left in the set of flags instead of being converted for reasons of backwards compatibility. See documentation of the directory, target, and source file COMPILE_DEFINITIONS properties for details on adding preprocessor definitions to specific scopes and configurations. </p>
<dt><code>add_dependencies</code></p>
<dd> Add a dependency between top-level targets. </p>
<pre>
  add_dependencies(target-name depend-target1
                   depend-target2 ...)
</pre>
<p> Make a top-level target depend on other top-level targets. A top-level target is one created by ADD_EXECUTABLE, ADD_LIBRARY, or ADD_CUSTOM_TARGET. Adding dependencies with this command can be used to make sure one target is built before another target. See the DEPENDS option of ADD_CUSTOM_TARGET and ADD_CUSTOM_COMMAND for adding file-level dependencies in custom rules. See the OBJECT_DEPENDS option in SET_SOURCE_FILES_PROPERTIES to add file-level dependencies to object files. </p>
<dt><code>add_executable</code></p>
<dd> Add an executable to the project using the specified source files. </p>
<p>add_executable(&lt;name&gt;[WIN32][MACOSX_BUNDLE][EXCLUDE_FROM_ALL] source1 source2&#8230; sourceN)</p>
<p> Adds an executable target called &lt;name&gt; to be built from the source files listed in the command invocation. The &lt;name&gt; corresponds to the logical target name and must be globally unique within a project. The actual file name of the executable built is constructed based on conventions of the native platform (such as &lt;name&gt;.exe or just &lt;name&gt;). </p>
<p> By default the executable file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the RUNTIME_OUTPUT_DIRECTORY target property to change this location. See documentation of the OUTPUT_NAME target property to change the &lt;name&gt; part of the final file name. </p>
<p> If WIN32 is given the property WIN32_EXECUTABLE will be set on the target created. See documentation of that target property for details. </p>
<p> If MACOSX_BUNDLE is given the corresponding property will be set on the created target. See documentation of the MACOSX_BUNDLE target property for details. </p>
<p> If EXCLUDE_FROM_ALL is given the corresponding property will be set on the created target. See documentation of the EXCLUDE_FROM_ALL target property for details. </p>
<p> The add_executable command can also create IMPORTED executable targets using this signature: </p>
<pre>
  add_executable(&lt;name&gt; IMPORTED)
</pre>
<p> An IMPORTED executable target references an executable file located outside the project. No rules are generated to build it. The target name has scope in the directory in which it is created and below. It may be referenced like any target built within the project. IMPORTED executables are useful for convenient reference from commands like add_custom_command. Details about the imported executable are specified by setting properties whose names begin in &quot;IMPORTED_&quot;. The most important such property is IMPORTED_LOCATION (and its per-configuration version IMPORTED_LOCATION_&lt;CONFIG&gt;) which specifies the location of the main executable file on disk. See documentation of the IMPORTED_* properties for more information. </p>
<dt><code>add_library</code></p>
<dd> Add a library to the project using the specified source files. </p>
<p>add_library(&lt;name&gt;[STATIC | SHARED | MODULE][EXCLUDE_FROM_ALL] source1 source2&#8230; sourceN)</p>
<p> Adds a library target called &lt;name&gt; to be built from the source files listed in the command invocation. The &lt;name&gt; corresponds to the logical target name and must be globally unique within a project. The actual file name of the library built is constructed based on conventions of the native platform (such as lib&lt;name&gt;.a or &lt;name&gt;.lib). </p>
<p> STATIC, SHARED, or MODULE may be given to specify the type of library to be created. STATIC libraries are archives of object files for use when linking other targets. SHARED libraries are linked dynamically and loaded at runtime. MODULE libraries are plugins that are not linked into other targets but may be loaded dynamically at runtime using dlopen-like functionality. If no type is given explicitly the type is STATIC or SHARED based on whether the current value of the variable BUILD_SHARED_LIBS is true. </p>
<p> By default the library file will be created in the build tree directory corresponding to the source tree directory in which the command was invoked. See documentation of the ARCHIVE_OUTPUT_DIRECTORY, LIBRARY_OUTPUT_DIRECTORY, and RUNTIME_OUTPUT_DIRECTORY target properties to change this location. See documentation of the OUTPUT_NAME target property to change the &lt;name&gt; part of the final file name. </p>
<p> If EXCLUDE_FROM_ALL is given the corresponding property will be set on the created target. See documentation of the EXCLUDE_FROM_ALL target property for details. </p>
<p> The add_library command can also create IMPORTED library targets using this signature: </p>
<pre>
  add_library(&lt;name&gt; &lt;SHARED|STATIC|MODULE|UNKNOWN&gt; IMPORTED)
</pre>
<p> An IMPORTED library target references a library file located outside the project. No rules are generated to build it. The target name has scope in the directory in which it is created and below. It may be referenced like any target built within the project. IMPORTED libraries are useful for convenient reference from commands like target_link_libraries. Details about the imported library are specified by setting properties whose names begin in &quot;IMPORTED_&quot;. The most important such property is IMPORTED_LOCATION (and its per-configuration version IMPORTED_LOCATION_&lt;CONFIG&gt;) which specifies the location of the main library file on disk. See documentation of the IMPORTED_* properties for more information. </p>
<dt><code>add_subdirectory</code></p>
<dd> Add a subdirectory to the build. </p>
<p>add_subdirectory(source_dir[binary_dir]<br />
                           [EXCLUDE_FROM_ALL])</p>
<p> Add a subdirectory to the build. The source_dir specifies the directory in which the source CmakeLists.txt and code files are located. If it is a relative path it will be evaluated with respect to the current directory (the typical usage), but it may also be an absolute path. The binary_dir specifies the directory in which to place the output files. If it is a relative path it will be evaluated with respect to the current output directory, but it may also be an absolute path. If binary_dir is not specified, the value of source_dir, before expanding any relative path, will be used (the typical usage). The CMakeLists.txt file in the specified source directory will be processed immediately by CMake before processing in the current input file continues beyond this command. </p>
<p> If the EXCLUDE_FROM_ALL argument is provided then targets in the subdirectory will not be included in the ALL target of the parent directory by default, and will be excluded from IDE project files. Users must explicitly build targets in the subdirectory. This is meant for use when the subdirectory contains a separate part of the project that is useful but not necessary, such as a set of examples. Typically the subdirectory should contain its own project() command invocation so that a full build system will be generated in the subdirectory (such as a VS IDE solution file). Note that inter-target dependencies supercede this exclusion. If a target built by the parent project depends on a target in the subdirectory, the dependee target will be included in the parent project build system to satisfy the dependency. </p>
<dt><code>add_test</code></p>
<dd> Add a test to the project with the specified arguments. </p>
<pre>
  add_test(testname Exename arg1 arg2 ...)
</pre>
<p> If the ENABLE_TESTING command has been run, this command adds a test target to the current directory. If ENABLE_TESTING has not been run, this command does nothing. The tests are run by the testing subsystem by executing Exename with the specified arguments. Exename can be either an executable built by this project or an arbitrary executable on the system (like tclsh). The test will be run with the current working directory set to the CMakeList.txt files corresponding directory in the binary tree. </p>
<dt><code>aux_source_directory</code></p>
<dd> Find all source files in a directory. </p>
<pre>
  aux_source_directory(&lt;dir&gt; &lt;variable&gt;)
</pre>
<p> Collects the names of all the source files in the specified directory and stores the list in the &lt;variable&gt; provided. This command is intended to be used by projects that use explicit template instantiation. Template instantiation files can be stored in a &quot;Templates&quot; subdirectory and collected automatically using this command to avoid manually listing all instantiations. </p>
<p> It is tempting to use this command to avoid writing the list of source files for a library or executable target. While this seems to work, there is no way for CMake to generate a build system that knows when a new source file has been added. Normally the generated build system knows when it needs to rerun CMake because the CMakeLists.txt file is modified to add a new source. When the source is just added to the directory without modifying this file, one would have to manually rerun CMake to generate a build system incorporating the new file. </p>
<dt><code>break</code></p>
<dd> Break from an enclosing foreach or while loop. </p>
<pre>
  break()
</pre>
<p> Breaks from an enclosing foreach loop or while loop </p>
<dt><code>build_command</code></p>
<dd> Get the command line that will build this project. </p>
<pre>
  build_command(&lt;variable&gt; &lt;makecommand&gt;)
</pre>
<p> Sets the given &lt;variable&gt; to a string containing the command that will build this project from the root of the build tree using the build tool given by &lt;makecommand&gt;. &lt;makecommand&gt; should be msdev, nmake, make or one of the end user build tools. This is useful for configuring testing systems. </p>
<dt><code>cmake_minimum_required</code></p>
<dd> Set the minimum required version of cmake for a project. </p>
<p>cmake_minimum_required(VERSION major[.minor[.patch]]<br />
                                    [FATAL_ERROR])</p>
<p> If the current version of CMake is lower than that required it will stop processing the project and report an error. When a version higher than 2.4 is specified the command implicitly invokes </p>
<p>cmake_policy(VERSION major[.minor[.patch]])</p>
<p> which sets the cmake policy version level to the version specified. When version 2.4 or lower is given the command implicitly invokes </p>
<pre>
  cmake_policy(VERSION 2.4)
</pre>
<p> which enables compatibility features for CMake 2.4 and lower. </p>
<p> The FATAL_ERROR option is accepted but ignored by CMake 2.6 and higher. It should be specified so CMake versions 2.4 and lower fail with an error instead of just a warning. </p>
<dt><code>cmake_policy</code></p>
<dd> Manage CMake Policy settings. </p>
<p> As CMake evolves it is sometimes necessary to change existing behavior in order to fix bugs or improve implementations of existing features. The CMake Policy mechanism is designed to help keep existing projects building as new versions of CMake introduce changes in behavior. Each new policy (behavioral change) is given an identifier of the form &quot;CMP&lt;NNNN&gt;&quot; where &quot;&lt;NNNN&gt;&quot; is an integer index. Documentation associated with each policy describes the OLD and NEW behavior and the reason the policy was introduced. Projects may set each policy to select the desired behavior. When CMake needs to know which behavior to use it checks for a setting specified by the project. If no setting is available the OLD behavior is assumed and a warning is produced requesting that the policy be set. </p>
<p> The cmake_policy command is used to set policies to OLD or NEW behavior. While setting policies individually is supported, we encourage projects to set policies based on CMake versions. </p>
<pre>
  cmake_policy(VERSION major.minor[.patch])
</pre>
<p> Specify that the current CMake list file is written for the given version of CMake. All policies introduced in the specified version or earlier will be set to use NEW behavior. All policies introduced after the specified version will be reset to use OLD behavior with a warning. This effectively requests behavior preferred as of a given CMake version and tells newer CMake versions to warn about their new policies. The policy version specified must be at least 2.4 or the command will report an error. In order to get compatibility features supporting versions earlier than 2.4 see documentation of policy CMP0001. </p>
<pre>
  cmake_policy(SET CMP&lt;NNNN&gt; NEW)
  cmake_policy(SET CMP&lt;NNNN&gt; OLD)
</pre>
<p> Tell CMake to use the OLD or NEW behavior for a given policy. Projects depending on the old behavior of a given policy may silence a policy warning by setting the policy state to OLD. Alternatively one may fix the project to work with the new behavior and set the policy state to NEW. </p>
<pre>
  cmake_policy(GET CMP&lt;NNNN&gt; &lt;variable&gt;)
</pre>
<p> Check whether a given policy is set to OLD or NEW behavior. The output variable value will be &quot;OLD&quot; or &quot;NEW&quot; if the policy is set, and empty otherwise. </p>
<p> CMake keeps policy settings on a stack, so changes made by the cmake_policy command affect only the top of the stack. A new entry on the policy stack is managed automatically for each subdirectory to protect its parents and siblings. CMake also manages a new entry for scripts loaded by include() and find_package() commands except when invoked with the NO_POLICY_SCOPE option (see also policy CMP0011). The cmake_policy command provides an interface to manage custom entries on the policy stack: </p>
<pre>
  cmake_policy(PUSH)
  cmake_policy(POP)
</pre>
<p> Each PUSH must have a matching POP to erase any changes. This is useful to make temporary changes to policy settings. </p>
<p> Functions and macros record policy settings when they are created and use the pre-record policies when they are invoked. If the function or macro implementation sets policies, the changes automatically propagate up through callers until they reach the closest nested policy stack entry. </p>
<dt><code>configure_file</code></p>
<dd> Copy a file to another location and modify its contents. </p>
<p>configure_file(InputFile OutputFile<br />
                   [COPYONLY][ESCAPE_QUOTES][@ONLY])</p>
<p> The Input and Output files have to have full paths. This command replaces any variables in the input file referenced as ${VAR} or @VAR@ with their values as determined by CMake. If a variable is not defined, it will be replaced with nothing. If COPYONLY is specified, then no variable expansion will take place. If ESCAPE_QUOTES is specified then any substituted quotes will be C-style escaped. The file will be configured with the current values of CMake variables. If @ONLY is specified, only variables of the form @VAR@ will be replaces and ${VAR} will be ignored. This is useful for configuring scripts that use ${VAR}. Any occurrences of #cmakedefine VAR will be replaced with either #define VAR or /* #undef VAR */ depending on the setting of VAR in CMake </p>
<dt><code>create_test_sourcelist</code></p>
<dd> Create a test driver and source list for building test programs. </p>
<pre>
  create_test_sourcelist(sourceListName driverName
                         test1 test2 test3
                         EXTRA_INCLUDE include.h
                         FUNCTION function)
</pre>
<p> A test driver is a program that links together many small tests into a single executable. This is useful when building static executables with large libraries to shrink the total required size. The list of source files needed to build the test driver will be in sourceListName. DriverName is the name of the test driver program. The rest of the arguments consist of a list of test source files, can be semicolon separated. Each test source file should have a function in it that is the same name as the file with no extension (foo.cxx should have int foo(int, char*[]);) DriverName will be able to call each of the tests by name on the command line. If EXTRA_INCLUDE is specified, then the next argument is included into the generated file. If FUNCTION is specified, then the next argument is taken as a function name that is passed a pointer to ac and av. This can be used to add extra command line processing to each test. The cmake variable CMAKE_TESTDRIVER_BEFORE_TESTMAIN can be set to have code that will be placed directly before calling the test main function. CMAKE_TESTDRIVER_AFTER_TESTMAIN can be set to have code that will be placed directly after the call to the test main function. </p>
<dt><code>define_property</code></p>
<dd> Define and document custom properties. </p>
<pre>
  define_property(&lt;GLOBAL | DIRECTORY | TARGET | SOURCE |
                   TEST | VARIABLE | CACHED_VARIABLE&gt;
                   PROPERTY &lt;name&gt; [INHERITED]
                   BRIEF_DOCS &lt;brief-doc&gt;
                   FULL_DOCS &lt;full-doc&gt;)
</pre>
<p> Define one property in a scope for use with the set_property and get_property commands. This is primarily useful to associate documentation with property names that may be retrieved with the get_property command. The first argument determines the kind of scope in which the property should be used. It must be one of the following: </p>
<pre>
  GLOBAL    = associated with the global namespace
  DIRECTORY = associated with one directory
  TARGET    = associated with one target
  SOURCE    = associated with one source file
  TEST      = associated with a test named with add_test command
  VARIABLE  = documents a CMake language variable
  CACHED_VARIABLE = documents a CMake cache variable
</pre>
<p> Note that unlike set_property and get_property no actual scope needs to be given; only the kind of scope is important. </p>
<p> The required PROPERTY option is immediately followed by the name of the property being defined. </p>
<p> If the INHERITED option then the get_property command will chain up to the next higher scope when the requested property is not set in the scope given to the command. DIRECTORY scope chains to GLOBAL. TARGET, SOURCE, and TEST chain to DIRECTORY. </p>
<p> The BRIEF_DOCS and FULL_DOCS options are followed by strings to be associated with the property as its brief and full documentation. Corresponding options to the get_property command will retrieve the documentation. </p>
<dt><code>else</code></p>
<dd> Starts the else portion of an if block. </p>
<pre>
  else(expression)
</pre>
<p> See the if command. </p>
<dt><code>elseif</code></p>
<dd> Starts the elseif portion of an if block. </p>
<pre>
  elseif(expression)
</pre>
<p> See the if command. </p>
<dt><code>enable_language</code></p>
<dd> Enable a language (CXX/C/Fortran/etc) </p>
<pre>
  enable_language(languageName [OPTIONAL] )
</pre>
<p> This command enables support for the named language in CMake. This is the same as the project command but does not create any of the extra variables that are created by the project command. Example languages are CXX, C, Fortran. </p>
<p> If OPTIONAL is used, use the CMAKE_&lt;languageName&gt;_COMPILER_WORKS variable to check whether the language has been enabled successfully. </p>
<dt><code>enable_testing</code></p>
<dd> Enable testing for current directory and below. </p>
<pre>
  enable_testing()
</pre>
<p> Enables testing for this directory and below. See also the add_test command. Note that ctest expects to find a test file in the build directory root. Therefore, this command should be in the source directory root. </p>
<dt><code>endforeach</code></p>
<dd> Ends a list of commands in a FOREACH block. </p>
<pre>
  endforeach(expression)
</pre>
<p> See the FOREACH command. </p>
<dt><code>endfunction</code></p>
<dd> Ends a list of commands in a function block. </p>
<pre>
  endfunction(expression)
</pre>
<p> See the function command. </p>
<dt><code>endif</code></p>
<dd> Ends a list of commands in an if block. </p>
<pre>
  endif(expression)
</pre>
<p> See the if command. </p>
<dt><code>endmacro</code></p>
<dd> Ends a list of commands in a macro block. </p>
<pre>
  endmacro(expression)
</pre>
<p> See the macro command. </p>
<dt><code>endwhile</code></p>
<dd> Ends a list of commands in a while block. </p>
<pre>
  endwhile(expression)
</pre>
<p> See the while command. </p>
<dt><code>execute_process</code></p>
<dd> Execute one or more child processes. </p>
<p>  execute_process(COMMAND &lt;cmd1&gt; [args1&#8230;]]<br />
                  [COMMAND &lt;cmd2&gt; [args2&#8230;] [&#8230;]]<br />
                  [WORKING_DIRECTORY &lt;directory&gt;]<br />
                  [TIMEOUT &lt;seconds&gt;]<br />
                  [RESULT_VARIABLE &lt;variable&gt;]<br />
                  [OUTPUT_VARIABLE &lt;variable&gt;]<br />
                  [ERROR_VARIABLE &lt;variable&gt;]<br />
                  [INPUT_FILE &lt;file&gt;]<br />
                  [OUTPUT_FILE &lt;file&gt;]<br />
                  [ERROR_FILE &lt;file&gt;]<br />
                  [OUTPUT_QUIET]<br />
                  [ERROR_QUIET]<br />
                  [OUTPUT_STRIP_TRAILING_WHITESPACE]<br />
                  [ERROR_STRIP_TRAILING_WHITESPACE])</p>
<p> Runs the given sequence of one or more commands with the standard output of each process piped to the standard input of the next. A single standard error pipe is used for all processes. If WORKING_DIRECTORY is given the named directory will be set as the current working directory of the child processes. If TIMEOUT is given the child processes will be terminated if they do not finish in the specified number of seconds (fractions are allowed). If RESULT_VARIABLE is given the variable will be set to contain the result of running the processes. This will be an integer return code from the last child or a string describing an error condition. If OUTPUT_VARIABLE or ERROR_VARIABLE are given the variable named will be set with the contents of the standard output and standard error pipes respectively. If the same variable is named for both pipes their output will be merged in the order produced. If INPUT_FILE, OUTPUT_FILE, or ERROR_FILE is given the file named will be attached to the standard input of the first process, standard output of the last process, or standard error of all processes respectively. If OUTPUT_QUIET or ERROR_QUIET is given then the standard output or standard error results will be quietly ignored. If more than one OUTPUT_* or ERROR_* option is given for the same pipe the precedence is not specified. If no OUTPUT_* or ERROR_* options are given the output will be shared with the corresponding pipes of the CMake process itself. </p>
<p> The execute_process command is a newer more powerful version of exec_program, but the old command has been kept for compatibility. </p>
<dt><code>export</code></p>
<dd> Export targets from the build tree for use by outside projects. </p>
<p>export(TARGETS[target1[target2[&#8230;]]][NAMESPACE&lt;namespace&gt;]<br />
              [APPEND] FILE&lt;filename&gt;)</p>
<p> Create a file &lt;filename&gt; that may be included by outside projects to import targets from the current project&#8217;s build tree. This is useful during cross-compiling to build utility executables that can run on the host platform in one project and then import them into another project being compiled for the target platform. If the NAMESPACE option is given the &lt;namespace&gt; string will be prepended to all target names written to the file. If the APPEND option is given the generated code will be appended to the file instead of overwriting it. If a library target is included in the export but a target to which it links is not included the behavior is unspecified. </p>
<p> The file created by this command is specific to the build tree and should never be installed. See the install(EXPORT) command to export targets from an installation tree. </p>
<dt><code>file</code></p>
<dd> File manipulation command. </p>
<p>file(WRITE filename &#8220;message to write&#8221; &#8230;)<br />
    file(APPEND filename &#8220;message to write&#8221; &#8230;)<br />
        file(READ filename variable[LIMIT numBytes][OFFSET offset][HEX])<br />
            file(STRINGS filename variable[LIMIT_COUNT num]<br />
                                          [LIMIT_INPUT numBytes][LIMIT_OUTPUT numBytes]<br />
                                          [LENGTH_MINIMUM numBytes][LENGTH_MAXIMUM numBytes]<br />
                                          [NEWLINE_CONSUME][REGEX regex]<br />
                                          [NO_HEX_CONVERSION])<br />
                file(GLOB variable[RELATIVE path][globbing expressions]&#8230;)<br />
                    file(GLOB_RECURSE variable[RELATIVE path]<br />
                                              [FOLLOW_SYMLINKS][globbing expressions]&#8230;)<br />
                        file(REMOVE[file1&#8230;])<br />
                            file(REMOVE_RECURSE[file1&#8230;])<br />
                                file(MAKE_DIRECTORY[directory1 directory2&#8230;])<br />
                                    file(RELATIVE_PATH variable directory file)<br />
                                        file(TO_CMAKE_PATH path result)<br />
                                            file(TO_NATIVE_PATH path result)<br />
                                                file(DOWNLOAD url file[TIMEOUT timeout][STATUS status][LOG log])</p>
<p> WRITE will write a message into a file called &#8216;filename&#8217;. It overwrites the file if it already exists, and creates the file if it does not exist. </p>
<p> APPEND will write a message into a file same as WRITE, except it will append it to the end of the file </p>
<p> READ will read the content of a file and store it into the variable. It will start at the given offset and read up to numBytes. If the argument HEX is given, the binary data will be converted to hexadecimal representation and this will be stored in the variable. </p>
<p> STRINGS will parse a list of ASCII strings from a file and store it in a variable. Binary data in the file are ignored. Carriage return (CR) characters are ignored. It works also for Intel Hex and Motorola S-record files, which are automatically converted to binary format when reading them. Disable this using NO_HEX_CONVERSION. </p>
<p> LIMIT_COUNT sets the maximum number of strings to return. LIMIT_INPUT sets the maximum number of bytes to read from the input file. LIMIT_OUTPUT sets the maximum number of bytes to store in the output variable. LENGTH_MINIMUM sets the minimum length of a string to return. Shorter strings are ignored. LENGTH_MAXIMUM sets the maximum length of a string to return. Longer strings are split into strings no longer than the maximum length. NEWLINE_CONSUME allows newlines to be included in strings instead of terminating them. </p>
<p> REGEX specifies a regular expression that a string must match to be returned. Typical usage </p>
<pre>
  file(STRINGS myfile.txt myfile)
</pre>
<p> stores a list in the variable &quot;myfile&quot; in which each item is a line from the input file. </p>
<p> GLOB will generate a list of all files that match the globbing expressions and store it into the variable. Globbing expressions are similar to regular expressions, but much simpler. If RELATIVE flag is specified for an expression, the results will be returned as a relative path to the given path. </p>
<p> Examples of globbing expressions include: </p>
<pre>
   *.cxx      - match all files with extension cxx
   *.vt?      - match all files with extension vta,...,vtz
   f[3-5].txt - match files f3.txt, f4.txt, f5.txt
</pre>
<p> GLOB_RECURSE will generate a list similar to the regular GLOB, except it will traverse all the subdirectories of the matched directory and match the files. Subdirectories that are symlinks are only traversed if FOLLOW_SYMLINKS is given or cmake policy CMP0009 is not set to NEW. See cmake &#8211;help-policy CMP0009 for more information. </p>
<p> Examples of recursive globbing include: </p>
<pre>
   /dir/*.py  - match all python files in /dir and subdirectories
</pre>
<p> MAKE_DIRECTORY will create the given directories, also if their parent directories don&#8217;t exist yet </p>
<p> REMOVE will remove the given files, also in subdirectories </p>
<p> REMOVE_RECURSE will remove the given files and directories, also non-empty directories </p>
<p> RELATIVE_PATH will determine relative path from directory to the given file. </p>
<p> TO_CMAKE_PATH will convert path into a cmake style path with unix /. The input can be a single path or a system path like &quot;$ENV{PATH}&quot;. Note the double quotes around the ENV call TO_CMAKE_PATH only takes one argument. </p>
<p> TO_NATIVE_PATH works just like TO_CMAKE_PATH, but will convert from a cmake style path into the native path style \ for windows and / for UNIX. </p>
<p> DOWNLOAD will download the given URL to the given file. If LOG var is specified a log of the download will be put in var. If STATUS var is specified the status of the operation will be put in var. The status is returned in a list of length 2. The first element is the numeric return value for the operation, and the second element is a string value for the error. A 0 numeric error means no error in the operation. If TIMEOUT time is specified, the operation will timeout after time seconds, time can be specified as a float. </p>
<dt><code>find_file</code></p>
<dd> Find the full path to a file. </p>
<pre>
   find_path(&lt;VAR&gt; name1 [path1 path2 ...])
</pre>
<p> This is the short-hand signature for the command that is sufficient in many cases. It is the same as find_path(&lt;VAR&gt; name1 [PATHS path1 path2 &#8230;]) </p>
<p>find_path(<br />
    &lt;VAR&gt;<br />
        name |<br />
    NAMES name1[name2&#8230;]<br />
               [HINTS path1[path2&#8230; ENV var]]<br />
               [PATHS path1[path2&#8230; ENV var]]<br />
               [PATH_SUFFIXES suffix1[suffix2&#8230;]]<br />
               [DOC &#8220;cache documentation string&#8221;]<br />
               [NO_DEFAULT_PATH]<br />
               [NO_CMAKE_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_PATH]<br />
               [NO_SYSTEM_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_SYSTEM_PATH]<br />
               [CMAKE_FIND_ROOT_PATH_BOTH |<br />
                ONLY_CMAKE_FIND_ROOT_PATH |<br />
                NO_CMAKE_FIND_ROOT_PATH])</p>
<p> This command is used to find a full path to named file. A cache entry named by &lt;VAR&gt; is created to store the result of this command. If the full path to a file is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again the next time find_path is invoked with the same variable. The name of the full path to a file that is searched for is specified by the names listed after the NAMES argument. Additional search locations can be specified after the PATHS argument. If ENV var is found in the HINTS or PATHS section the environment variable var will be read and converted from a system environment variable to a cmake style list of paths. For example ENV PATH would be a way to list the system path variable. The argument after DOC will be used for the documentation string in the cache. PATH_SUFFIXES specifies additional subdirectories to check below each search path. </p>
<p> If NO_DEFAULT_PATH is specified, then no additional paths are added to the search. If NO_DEFAULT_PATH is not specified, the search process is as follows: </p>
<p> 1. Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a -DVAR=value. This can be skipped if NO_CMAKE_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_INCLUDE_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 2. Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_INCLUDE_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 3. Search the paths specified by the HINTS option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the PATHS option. </p>
<p> 4. Search the standard system environment variables. This can be skipped if NO_SYSTEM_ENVIRONMENT_PATH is an argument. </p>
<pre>
   PATH
   INCLUDE
</pre>
<p> 5. Search cmake variables defined in the Platform files for the current system. This can be skipped if NO_CMAKE_SYSTEM_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_SYSTEM_PREFIX_PATH
   CMAKE_SYSTEM_INCLUDE_PATH
   CMAKE_SYSTEM_FRAMEWORK_PATH
</pre>
<p> 6. Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On Darwin or systems supporting OS X Frameworks, the cmake variable CMAKE_FIND_FRAMEWORK can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find frameworks before standard
              libraries or headers. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find frameworks after standard
              libraries or headers.
   &quot;ONLY&quot;   - Only try to find frameworks.
   &quot;NEVER&quot;. - Never try to find frameworks.
</pre>
<p> On Darwin or systems supporting OS X Application Bundles, the cmake variable CMAKE_FIND_APPBUNDLE can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find application bundles before standard
              programs. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find application bundles after standard
              programs.
   &quot;ONLY&quot;   - Only try to find application bundles.
   &quot;NEVER&quot;. - Never try to find application bundles.
</pre>
<p> The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. By default it is empty. It is especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in CMAKE_FIND_ROOT_PATH and then the non-rooted directories will be searched. The default behavior can be adjusted by setting CMAKE_FIND_ROOT_PATH_MODE_INCLUDE. This behavior can be manually overridden on a per-call basis. By using CMAKE_FIND_ROOT_PATH_BOTH the search order will be as described above. If NO_CMAKE_FIND_ROOT_PATH is used then CMAKE_FIND_ROOT_PATH will not be used. If ONLY_CMAKE_FIND_ROOT_PATH is used then only the re-rooted directories will be searched. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the NO_* options: </p>
<pre>
   find_path(&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
   find_path(&lt;VAR&gt; NAMES name)
</pre>
<p> Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<dt><code>find_library</code></p>
<dd> Find a library. </p>
<pre>
   find_library(&lt;VAR&gt; name1 [path1 path2 ...])
</pre>
<p> This is the short-hand signature for the command that is sufficient in many cases. It is the same as find_library(&lt;VAR&gt; name1 [PATHS path1 path2 &#8230;]) </p>
<p>find_library(<br />
    &lt;VAR&gt;<br />
        name |<br />
    NAMES name1[name2&#8230;]<br />
               [HINTS path1[path2&#8230; ENV var]]<br />
               [PATHS path1[path2&#8230; ENV var]]<br />
               [PATH_SUFFIXES suffix1[suffix2&#8230;]]<br />
               [DOC &#8220;cache documentation string&#8221;]<br />
               [NO_DEFAULT_PATH]<br />
               [NO_CMAKE_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_PATH]<br />
               [NO_SYSTEM_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_SYSTEM_PATH]<br />
               [CMAKE_FIND_ROOT_PATH_BOTH |<br />
                ONLY_CMAKE_FIND_ROOT_PATH |<br />
                NO_CMAKE_FIND_ROOT_PATH])</p>
<p> This command is used to find a library. A cache entry named by &lt;VAR&gt; is created to store the result of this command. If the library is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again the next time find_library is invoked with the same variable. The name of the library that is searched for is specified by the names listed after the NAMES argument. Additional search locations can be specified after the PATHS argument. If ENV var is found in the HINTS or PATHS section the environment variable var will be read and converted from a system environment variable to a cmake style list of paths. For example ENV PATH would be a way to list the system path variable. The argument after DOC will be used for the documentation string in the cache. PATH_SUFFIXES specifies additional subdirectories to check below each search path. </p>
<p> If NO_DEFAULT_PATH is specified, then no additional paths are added to the search. If NO_DEFAULT_PATH is not specified, the search process is as follows: </p>
<p> 1. Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a -DVAR=value. This can be skipped if NO_CMAKE_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/lib for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_LIBRARY_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 2. Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/lib for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_LIBRARY_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 3. Search the paths specified by the HINTS option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the PATHS option. </p>
<p> 4. Search the standard system environment variables. This can be skipped if NO_SYSTEM_ENVIRONMENT_PATH is an argument. </p>
<pre>
   PATH
   LIB
</pre>
<p> 5. Search cmake variables defined in the Platform files for the current system. This can be skipped if NO_CMAKE_SYSTEM_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/lib for each &lt;prefix&gt; in CMAKE_SYSTEM_PREFIX_PATH
   CMAKE_SYSTEM_LIBRARY_PATH
   CMAKE_SYSTEM_FRAMEWORK_PATH
</pre>
<p> 6. Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On Darwin or systems supporting OS X Frameworks, the cmake variable CMAKE_FIND_FRAMEWORK can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find frameworks before standard
              libraries or headers. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find frameworks after standard
              libraries or headers.
   &quot;ONLY&quot;   - Only try to find frameworks.
   &quot;NEVER&quot;. - Never try to find frameworks.
</pre>
<p> On Darwin or systems supporting OS X Application Bundles, the cmake variable CMAKE_FIND_APPBUNDLE can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find application bundles before standard
              programs. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find application bundles after standard
              programs.
   &quot;ONLY&quot;   - Only try to find application bundles.
   &quot;NEVER&quot;. - Never try to find application bundles.
</pre>
<p> The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. By default it is empty. It is especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in CMAKE_FIND_ROOT_PATH and then the non-rooted directories will be searched. The default behavior can be adjusted by setting CMAKE_FIND_ROOT_PATH_MODE_LIBRARY. This behavior can be manually overridden on a per-call basis. By using CMAKE_FIND_ROOT_PATH_BOTH the search order will be as described above. If NO_CMAKE_FIND_ROOT_PATH is used then CMAKE_FIND_ROOT_PATH will not be used. If ONLY_CMAKE_FIND_ROOT_PATH is used then only the re-rooted directories will be searched. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the NO_* options: </p>
<pre>
   find_library(&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
   find_library(&lt;VAR&gt; NAMES name)
</pre>
<p> Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> If the library found is a framework, then VAR will be set to the full path to the framework &lt;fullPath&gt;/A.framework. When a full path to a framework is used as a library, CMake will use a -framework A, and a -F&lt;fullPath&gt; to link the framework to the target. </p>
<dt><code>find_package</code></p>
<dd> Load settings for an external project. </p>
<p>find_package(&lt;package&gt;[version][EXACT][QUIET]<br />
             [[REQUIRED | COMPONENTS] [components&#8230;]][NO_POLICY_SCOPE])</p>
<p> Finds and loads settings from an external project. &lt;package&gt;_FOUND will be set to indicate whether the package was found. When the package is found package-specific information is provided through variables documented by the package itself. The QUIET option disables messages if the package cannot be found. The REQUIRED option stops processing with an error message if the package cannot be found. A package-specific list of components may be listed after the REQUIRED option or after the COMPONENTS option if no REQUIRED option is given. The [version] argument requests a version with which the package found should be compatible (format is major[.minor[.patch[.tweak]]]). The EXACT option requests that the version be matched exactly. If no [version] is given to a recursive invocation inside a find-module, the [version] and EXACT arguments are forwarded automatically from the outer call. Version support is currently provided only on a package-by-package basis (details below). </p>
<p> User code should generally look for packages using the above simple signature. The remainder of this command documentation specifies the full command signature and details of the search process. Project maintainers wishing to provide a package to be found by this command are encouraged to read on. </p>
<p> The command has two modes by which it searches for packages: &quot;Module&quot; mode and &quot;Config&quot; mode. Module mode is available when the command is invoked with the above reduced signature. CMake searches for a file called &quot;Find&lt;package&gt;.cmake&quot; in the CMAKE_MODULE_PATH followed by the CMake installation. If the file is found, it is read and processed by CMake. It is responsible for finding the package, checking the version, and producing any needed messages. Many find-modules provide limited or no support for versioning; check the module documentation. If no module is found the command proceeds to Config mode. </p>
<p> The complete Config mode command signature is: </p>
<p>find_package(&lt;package&gt;[version][EXACT][QUIET]<br />
             [[REQUIRED | COMPONENTS] [components&#8230;]][NO_MODULE]<br />
                      [NO_POLICY_SCOPE]<br />
                      [NAMES name1[name2&#8230;]]<br />
                      [CONFIGS config1[config2&#8230;]]<br />
                      [HINTS path1[path2&#8230;]]<br />
                      [PATHS path1[path2&#8230;]]<br />
                      [PATH_SUFFIXES suffix1[suffix2&#8230;]]<br />
                      [NO_DEFAULT_PATH]<br />
                      [NO_CMAKE_ENVIRONMENT_PATH]<br />
                      [NO_CMAKE_PATH]<br />
                      [NO_SYSTEM_ENVIRONMENT_PATH]<br />
                      [NO_CMAKE_BUILDS_PATH]<br />
                      [NO_CMAKE_SYSTEM_PATH]<br />
                      [CMAKE_FIND_ROOT_PATH_BOTH |<br />
                       ONLY_CMAKE_FIND_ROOT_PATH |<br />
                       NO_CMAKE_FIND_ROOT_PATH])</p>
<p> The NO_MODULE option may be used to skip Module mode explicitly. It is also implied by use of options not specified in the reduced signature. </p>
<p> Config mode attempts to locate a configuration file provided by the package to be found. A cache entry called &lt;package&gt;_DIR is created to hold the directory containing the file. By default the command searches for a package with the name &lt;package&gt;. If the NAMES option is given the names following it are used instead of &lt;package&gt;. The command searches for a file called &quot;&lt;name&gt;Config.cmake&quot; or &quot;&lt;lower-case-name&gt;-config.cmake&quot; for each name specified. A replacement set of possible configuration file names may be given using the CONFIGS option. The search procedure is specified below. Once found, the configuration file is read and processed by CMake. Since the file is provided by the package it already knows the location of package contents. The full path to the configuration file is stored in the cmake variable &lt;package&gt;_CONFIG. </p>
<p> If the package configuration file cannot be found CMake will generate an error describing the problem unless the QUIET argument is specified. If REQUIRED is specified and the package is not found a fatal error is generated and the configure step stops executing. If &lt;package&gt;_DIR has been set to a directory not containing a configuration file CMake will ignore it and search from scratch. </p>
<p> When the [version] argument is given Config mode will only find a version of the package that claims compatibility with the requested version (format is major[.minor[.patch[.tweak]]]). If the EXACT option is given only a version of the package claiming an exact match of the requested version may be found. CMake does not establish any convention for the meaning of version numbers. Package version numbers are checked by &quot;version&quot; files provided by the packages themselves. For a candidate package confguration file &quot;&lt;config-file&gt;.cmake&quot; the corresponding version file is located next to it and named either &quot;&lt;config-file&gt;-version.cmake&quot; or &quot;&lt;config-file&gt;Version.cmake&quot;. If no such version file is available then the configuration file is assumed to not be compatible with any requested version. When a version file is found it is loaded to check the requested version number. The version file is loaded in a nested scope in which the following variables have been defined: </p>
<p>PACKAGE_FIND_NAME = the&lt;package&gt; name<br />
    PACKAGE_FIND_VERSION = full requested version string<br />
        PACKAGE_FIND_VERSION_MAJOR = major version if requested,<br />
    else 0 PACKAGE_FIND_VERSION_MINOR = minor version if requested, else 0 PACKAGE_FIND_VERSION_PATCH = patch version if requested, else 0 PACKAGE_FIND_VERSION_TWEAK = tweak version if requested, else 0 PACKAGE_FIND_VERSION_COUNT = number of version components, 0 to 4</p>
<p> The version file checks whether it satisfies the requested version and sets these variables: </p>
<pre>
  PACKAGE_VERSION            = full provided version string
  PACKAGE_VERSION_EXACT      = true if version is exact match
  PACKAGE_VERSION_COMPATIBLE = true if version is compatible
  PACKAGE_VERSION_UNSUITABLE = true if unsuitable as any version
</pre>
<p> These variables are checked by the find_package command to determine whether the configuration file provides an acceptable version. They are not available after the find_package call returns. If the version is acceptable the following variables are set: </p>
<p>  &lt;package&gt;_VERSION       = full provided version string<br />
  &lt;package&gt;_VERSION_MAJOR = major version if provided, else 0<br />
  &lt;package&gt;_VERSION_MINOR = minor version if provided, else 0<br />
  &lt;package&gt;_VERSION_PATCH = patch version if provided, else 0<br />
  &lt;package&gt;_VERSION_TWEAK = tweak version if provided, else 0<br />
  &lt;package&gt;_VERSION_COUNT = number of version components, 0 to 4</p>
<p> and the corresponding package configuration file is loaded. When multiple package configuration files are available whose version files claim compatibility with the version requested it is unspecified which one is chosen. No attempt is made to choose a highest or closest version number. </p>
<p> Config mode provides an elaborate interface and search procedure. Much of the interface is provided for completeness and for use internally by find-modules loaded by Module mode. Most user code should simply call </p>
<p>find_package(&lt;package&gt;[major[.minor]][EXACT][REQUIRED | QUIET])</p>
<p> in order to find a package. Package maintainers providing CMake package configuration files are encouraged to name and install them such that the procedure outlined below will find them without requiring use of additional options. </p>
<p> CMake constructs a set of possible installation prefixes for the package. Under each prefix several directories are searched for a configuration file. The tables below show the directories searched. Each entry is meant for installation trees following Windows (W), UNIX (U), or Apple (A) conventions. </p>
<pre>
  &lt;prefix&gt;/                                               (W)
  &lt;prefix&gt;/(cmake|CMake)/                                 (W)
  &lt;prefix&gt;/&lt;name&gt;*/                                       (W)
  &lt;prefix&gt;/&lt;name&gt;*/(cmake|CMake)/                         (W)
  &lt;prefix&gt;/(share|lib)/cmake/&lt;name&gt;*/                     (U)
  &lt;prefix&gt;/(share|lib)/&lt;name&gt;*/                           (U)
  &lt;prefix&gt;/(share|lib)/&lt;name&gt;*/(cmake|CMake)/             (U)
</pre>
<p> On systems supporting OS X Frameworks and Application Bundles the following directories are searched for frameworks or bundles containing a configuration file: </p>
<pre>
  &lt;prefix&gt;/&lt;name&gt;.framework/Resources/                    (A)
  &lt;prefix&gt;/&lt;name&gt;.framework/Resources/CMake/              (A)
  &lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/         (A)
  &lt;prefix&gt;/&lt;name&gt;.framework/Versions/*/Resources/CMake/   (A)
  &lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/                 (A)
  &lt;prefix&gt;/&lt;name&gt;.app/Contents/Resources/CMake/           (A)
</pre>
<p> In all cases the &lt;name&gt; is treated as case-insensitive and corresponds to any of the names specified (&lt;package&gt; or names given by NAMES). If PATH_SUFFIXES is specified the suffixes are appended to each (W) or (U) directory entry one-by-one. </p>
<p> This set of directories is intended to work in cooperation with projects that provide configuration files in their installation trees. Directories above marked with (W) are intended for installations on Windows where the prefix may point at the top of an application&#8217;s installation directory. Those marked with (U) are intended for installations on UNIX platforms where the prefix is shared by multiple packages. This is merely a convention, so all (W) and (U) directories are still searched on all platforms. Directories marked with (A) are intended for installations on Apple platforms. The cmake variables CMAKE_FIND_FRAMEWORK and CMAKE_FIND_APPBUNDLE determine the order of preference as specified below. </p>
<p> The set of installation prefixes is constructed using the following steps. If NO_DEFAULT_PATH is specified all NO_* options are enabled. </p>
<p> 1. Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a -DVAR=value. This can be skipped if NO_CMAKE_PATH is passed. </p>
<pre>
   CMAKE_PREFIX_PATH
   CMAKE_FRAMEWORK_PATH
   CMAKE_APPBUNDLE_PATH
</pre>
<p> 2. Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed. </p>
<pre>
   CMAKE_PREFIX_PATH
   CMAKE_FRAMEWORK_PATH
   CMAKE_APPBUNDLE_PATH
</pre>
<p> 3. Search paths specified by the HINTS option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the PATHS option. </p>
<p> 4. Search the standard system environment variables. This can be skipped if NO_SYSTEM_ENVIRONMENT_PATH is passed. Path entries ending in &quot;/bin&quot; or &quot;/sbin&quot; are automatically converted to their parent directories. </p>
<pre>
   PATH
</pre>
<p> 5. Search project build trees recently configured in a CMake GUI. This can be skipped if NO_CMAKE_BUILDS_PATH is passed. It is intended for the case when a user is building multiple dependent projects one after another. </p>
<p> 6. Search cmake variables defined in the Platform files for the current system. This can be skipped if NO_CMAKE_SYSTEM_PATH is passed. </p>
<pre>
   CMAKE_SYSTEM_PREFIX_PATH
   CMAKE_SYSTEM_FRAMEWORK_PATH
   CMAKE_SYSTEM_APPBUNDLE_PATH
</pre>
<p> 7. Search paths specified by the PATHS option. These are typically hard-coded guesses. </p>
<p> On Darwin or systems supporting OS X Frameworks, the cmake variable CMAKE_FIND_FRAMEWORK can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find frameworks before standard
              libraries or headers. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find frameworks after standard
              libraries or headers.
   &quot;ONLY&quot;   - Only try to find frameworks.
   &quot;NEVER&quot;. - Never try to find frameworks.
</pre>
<p> On Darwin or systems supporting OS X Application Bundles, the cmake variable CMAKE_FIND_APPBUNDLE can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find application bundles before standard
              programs. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find application bundles after standard
              programs.
   &quot;ONLY&quot;   - Only try to find application bundles.
   &quot;NEVER&quot;. - Never try to find application bundles.
</pre>
<p> The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. By default it is empty. It is especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in CMAKE_FIND_ROOT_PATH and then the non-rooted directories will be searched. The default behavior can be adjusted by setting CMAKE_FIND_ROOT_PATH_MODE_PACKAGE. This behavior can be manually overridden on a per-call basis. By using CMAKE_FIND_ROOT_PATH_BOTH the search order will be as described above. If NO_CMAKE_FIND_ROOT_PATH is used then CMAKE_FIND_ROOT_PATH will not be used. If ONLY_CMAKE_FIND_ROOT_PATH is used then only the re-rooted directories will be searched. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the NO_* options: </p>
<pre>
   find_package(&lt;package&gt; PATHS paths... NO_DEFAULT_PATH)
   find_package(&lt;package&gt;)
</pre>
<p> Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> See the cmake_policy() command documentation for discussion of the NO_POLICY_SCOPE option. </p>
<dt><code>find_path</code></p>
<dd> Find the directory containing a file. </p>
<pre>
   find_path(&lt;VAR&gt; name1 [path1 path2 ...])
</pre>
<p> This is the short-hand signature for the command that is sufficient in many cases. It is the same as find_path(&lt;VAR&gt; name1 [PATHS path1 path2 &#8230;]) </p>
<p>find_path(<br />
    &lt;VAR&gt;<br />
        name |<br />
    NAMES name1[name2&#8230;]<br />
               [HINTS path1[path2&#8230; ENV var]]<br />
               [PATHS path1[path2&#8230; ENV var]]<br />
               [PATH_SUFFIXES suffix1[suffix2&#8230;]]<br />
               [DOC &#8220;cache documentation string&#8221;]<br />
               [NO_DEFAULT_PATH]<br />
               [NO_CMAKE_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_PATH]<br />
               [NO_SYSTEM_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_SYSTEM_PATH]<br />
               [CMAKE_FIND_ROOT_PATH_BOTH |<br />
                ONLY_CMAKE_FIND_ROOT_PATH |<br />
                NO_CMAKE_FIND_ROOT_PATH])</p>
<p> This command is used to find a directory containing the named file. A cache entry named by &lt;VAR&gt; is created to store the result of this command. If the file in a directory is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again the next time find_path is invoked with the same variable. The name of the file in a directory that is searched for is specified by the names listed after the NAMES argument. Additional search locations can be specified after the PATHS argument. If ENV var is found in the HINTS or PATHS section the environment variable var will be read and converted from a system environment variable to a cmake style list of paths. For example ENV PATH would be a way to list the system path variable. The argument after DOC will be used for the documentation string in the cache. PATH_SUFFIXES specifies additional subdirectories to check below each search path. </p>
<p> If NO_DEFAULT_PATH is specified, then no additional paths are added to the search. If NO_DEFAULT_PATH is not specified, the search process is as follows: </p>
<p> 1. Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a -DVAR=value. This can be skipped if NO_CMAKE_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_INCLUDE_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 2. Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_INCLUDE_PATH
   CMAKE_FRAMEWORK_PATH
</pre>
<p> 3. Search the paths specified by the HINTS option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the PATHS option. </p>
<p> 4. Search the standard system environment variables. This can be skipped if NO_SYSTEM_ENVIRONMENT_PATH is an argument. </p>
<pre>
   PATH
   INCLUDE
</pre>
<p> 5. Search cmake variables defined in the Platform files for the current system. This can be skipped if NO_CMAKE_SYSTEM_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/include for each &lt;prefix&gt; in CMAKE_SYSTEM_PREFIX_PATH
   CMAKE_SYSTEM_INCLUDE_PATH
   CMAKE_SYSTEM_FRAMEWORK_PATH
</pre>
<p> 6. Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On Darwin or systems supporting OS X Frameworks, the cmake variable CMAKE_FIND_FRAMEWORK can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find frameworks before standard
              libraries or headers. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find frameworks after standard
              libraries or headers.
   &quot;ONLY&quot;   - Only try to find frameworks.
   &quot;NEVER&quot;. - Never try to find frameworks.
</pre>
<p> On Darwin or systems supporting OS X Application Bundles, the cmake variable CMAKE_FIND_APPBUNDLE can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find application bundles before standard
              programs. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find application bundles after standard
              programs.
   &quot;ONLY&quot;   - Only try to find application bundles.
   &quot;NEVER&quot;. - Never try to find application bundles.
</pre>
<p> The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. By default it is empty. It is especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in CMAKE_FIND_ROOT_PATH and then the non-rooted directories will be searched. The default behavior can be adjusted by setting CMAKE_FIND_ROOT_PATH_MODE_INCLUDE. This behavior can be manually overridden on a per-call basis. By using CMAKE_FIND_ROOT_PATH_BOTH the search order will be as described above. If NO_CMAKE_FIND_ROOT_PATH is used then CMAKE_FIND_ROOT_PATH will not be used. If ONLY_CMAKE_FIND_ROOT_PATH is used then only the re-rooted directories will be searched. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the NO_* options: </p>
<pre>
   find_path(&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
   find_path(&lt;VAR&gt; NAMES name)
</pre>
<p> Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<p> When searching for frameworks, if the file is specified as A/b.h, then the framework search will look for A.framework/Headers/b.h. If that is found the path will be set to the path to the framework. CMake will convert this to the correct -F option to include the file. </p>
<dt><code>find_program</code></p>
<dd> Find an executable program. </p>
<pre>
   find_program(&lt;VAR&gt; name1 [path1 path2 ...])
</pre>
<p> This is the short-hand signature for the command that is sufficient in many cases. It is the same as find_program(&lt;VAR&gt; name1 [PATHS path1 path2 &#8230;]) </p>
<p>find_program(<br />
    &lt;VAR&gt;<br />
        name |<br />
    NAMES name1[name2&#8230;]<br />
               [HINTS path1[path2&#8230; ENV var]]<br />
               [PATHS path1[path2&#8230; ENV var]]<br />
               [PATH_SUFFIXES suffix1[suffix2&#8230;]]<br />
               [DOC &#8220;cache documentation string&#8221;]<br />
               [NO_DEFAULT_PATH]<br />
               [NO_CMAKE_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_PATH]<br />
               [NO_SYSTEM_ENVIRONMENT_PATH]<br />
               [NO_CMAKE_SYSTEM_PATH]<br />
               [CMAKE_FIND_ROOT_PATH_BOTH |<br />
                ONLY_CMAKE_FIND_ROOT_PATH |<br />
                NO_CMAKE_FIND_ROOT_PATH])</p>
<p> This command is used to find a program. A cache entry named by &lt;VAR&gt; is created to store the result of this command. If the program is found the result is stored in the variable and the search will not be repeated unless the variable is cleared. If nothing is found, the result will be &lt;VAR&gt;-NOTFOUND, and the search will be attempted again the next time find_program is invoked with the same variable. The name of the program that is searched for is specified by the names listed after the NAMES argument. Additional search locations can be specified after the PATHS argument. If ENV var is found in the HINTS or PATHS section the environment variable var will be read and converted from a system environment variable to a cmake style list of paths. For example ENV PATH would be a way to list the system path variable. The argument after DOC will be used for the documentation string in the cache. PATH_SUFFIXES specifies additional subdirectories to check below each search path. </p>
<p> If NO_DEFAULT_PATH is specified, then no additional paths are added to the search. If NO_DEFAULT_PATH is not specified, the search process is as follows: </p>
<p> 1. Search paths specified in cmake-specific cache variables. These are intended to be used on the command line with a -DVAR=value. This can be skipped if NO_CMAKE_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/[s]bin for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_PROGRAM_PATH
   CMAKE_APPBUNDLE_PATH
</pre>
<p> 2. Search paths specified in cmake-specific environment variables. These are intended to be set in the user&#8217;s shell configuration. This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/[s]bin for each &lt;prefix&gt; in CMAKE_PREFIX_PATH
   CMAKE_PROGRAM_PATH
   CMAKE_APPBUNDLE_PATH
</pre>
<p> 3. Search the paths specified by the HINTS option. These should be paths computed by system introspection, such as a hint provided by the location of another item already found. Hard-coded guesses should be specified with the PATHS option. </p>
<p> 4. Search the standard system environment variables. This can be skipped if NO_SYSTEM_ENVIRONMENT_PATH is an argument. </p>
<pre>
   PATH
   
</pre>
<p> 5. Search cmake variables defined in the Platform files for the current system. This can be skipped if NO_CMAKE_SYSTEM_PATH is passed. </p>
<pre>
   &lt;prefix&gt;/[s]bin for each &lt;prefix&gt; in CMAKE_SYSTEM_PREFIX_PATH
   CMAKE_SYSTEM_PROGRAM_PATH
   CMAKE_SYSTEM_APPBUNDLE_PATH
</pre>
<p> 6. Search the paths specified by the PATHS option or in the short-hand version of the command. These are typically hard-coded guesses. </p>
<p> On Darwin or systems supporting OS X Frameworks, the cmake variable CMAKE_FIND_FRAMEWORK can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find frameworks before standard
              libraries or headers. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find frameworks after standard
              libraries or headers.
   &quot;ONLY&quot;   - Only try to find frameworks.
   &quot;NEVER&quot;. - Never try to find frameworks.
</pre>
<p> On Darwin or systems supporting OS X Application Bundles, the cmake variable CMAKE_FIND_APPBUNDLE can be set to empty or one of the following: </p>
<pre>
   &quot;FIRST&quot;  - Try to find application bundles before standard
              programs. This is the default on Darwin.
   &quot;LAST&quot;   - Try to find application bundles after standard
              programs.
   &quot;ONLY&quot;   - Only try to find application bundles.
   &quot;NEVER&quot;. - Never try to find application bundles.
</pre>
<p> The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more directories to be prepended to all other search directories. This effectively &quot;re-roots&quot; the entire search under given locations. By default it is empty. It is especially useful when cross-compiling to point to the root directory of the target environment and CMake will search there too. By default at first the directories listed in CMAKE_FIND_ROOT_PATH and then the non-rooted directories will be searched. The default behavior can be adjusted by setting CMAKE_FIND_ROOT_PATH_MODE_PROGRAM. This behavior can be manually overridden on a per-call basis. By using CMAKE_FIND_ROOT_PATH_BOTH the search order will be as described above. If NO_CMAKE_FIND_ROOT_PATH is used then CMAKE_FIND_ROOT_PATH will not be used. If ONLY_CMAKE_FIND_ROOT_PATH is used then only the re-rooted directories will be searched. </p>
<p> The default search order is designed to be most-specific to least-specific for common use cases. Projects may override the order by simply calling the command multiple times and using the NO_* options: </p>
<pre>
   find_program(&lt;VAR&gt; NAMES name PATHS paths... NO_DEFAULT_PATH)
   find_program(&lt;VAR&gt; NAMES name)
</pre>
<p> Once one of the calls succeeds the result variable will be set and stored in the cache so that no call will search again. </p>
<dt><code>fltk_wrap_ui</code></p>
<dd> Create FLTK user interfaces Wrappers. </p>
<pre>
  fltk_wrap_ui(resultingLibraryName source1
               source2 ... sourceN )
</pre>
<p> Produce .h and .cxx files for all the .fl and .fld files listed. The resulting .h and .cxx files will be added to a variable named resultingLibraryName_FLTK_UI_SRCS which should be added to your library. </p>
<dt><code>foreach</code></p>
<dd> Evaluate a group of commands for each value in a list. </p>
<pre>
  foreach(loop_var arg1 arg2 ...)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
  endforeach(loop_var)
  foreach(loop_var RANGE total)
  foreach(loop_var RANGE start stop [step])
</pre>
<p> All commands between foreach and the matching endforeach are recorded without being invoked. Once the endforeach is evaluated, the recorded list of commands is invoked once for each argument listed in the original foreach command. Before each iteration of the loop &quot;${loop_var}&quot; will be set as a variable with the current value in the list. </p>
<p> Foreach can also iterate over a generated range of numbers. There are three types of this iteration: </p>
<p> * When specifying single number, the range will have elements 0 to &quot;total&quot;. </p>
<p> * When specifying two numbers, the range will have elements from the first number to the second number. </p>
<p> * The third optional number is the increment used to iterate from the first number to the second number. </p>
<dt><code>function</code></p>
<dd> Start recording a function for later invocation as a command. </p>
<p>function(&lt;name&gt;[arg1[arg2[arg3&#8230;]]])<br />
    COMMAND1(ARGS&#8230;)<br />
        COMMAND2(ARGS&#8230;)&#8230; endfunction(&lt;name&gt;)</p>
<p> Define a function named &lt;name&gt; that takes arguments named arg1 arg2 arg3 (&#8230;). Commands listed after function, but before the matching endfunction, are not invoked until the function is invoked. When it is invoked, the commands recorded in the function are first modified by replacing formal parameters (${arg1}) with the arguments passed, and then invoked as normal commands. In addition to referencing the formal parameters you can reference the variable ARGC which will be set to the number of arguments passed into the function as well as ARGV0 ARGV1 ARGV2 &#8230; which will have the actual values of the arguments passed in. This facilitates creating functions with optional arguments. Additionally ARGV holds the list of all arguments given to the function and ARGN holds the list of argument pass the last expected argument. </p>
<p> See the cmake_policy() command documentation for the behavior of policies inside functions. </p>
<dt><code>get_cmake_property</code></p>
<dd> Get a property of the CMake instance. </p>
<pre>
  get_cmake_property(VAR property)
</pre>
<p> Get a property from the CMake instance. The value of the property is stored in the variable VAR. If the property is not found, CMake will report an error. Some supported properties include: VARIABLES, CACHE_VARIABLES, COMMANDS, MACROS, and COMPONENTS. </p>
<dt><code>get_directory_property</code></p>
<dd> Get a property of the directory. </p>
<pre>
  get_directory_property(VAR [DIRECTORY dir] property)
</pre>
<p> Get a property from the Directory. The value of the property is stored in the variable VAR. If the property is not found, CMake will report an error. The properties include: VARIABLES, CACHE_VARIABLES, COMMANDS, MACROS, INCLUDE_DIRECTORIES, LINK_DIRECTORIES, DEFINITIONS, INCLUDE_REGULAR_EXPRESSION, LISTFILE_STACK, PARENT_DIRECTORY, and DEFINITION varname. If the DIRECTORY argument is provided then the property of the provided directory will be retrieved instead of the current directory. You can only get properties of a directory during or after it has been traversed by cmake. </p>
<dt><code>get_filename_component</code></p>
<dd> Get a specific component of a full filename. </p>
<pre>
  get_filename_component(VarName FileName
                         PATH|ABSOLUTE|NAME|EXT|NAME_WE|REALPATH
                         [CACHE])
</pre>
<p> Set VarName to be the path (PATH), file name (NAME), file extension (EXT), file name without extension (NAME_WE) of FileName, the full path (ABSOLUTE), or the full path with all symlinks resolved (REALPATH). Note that the path is converted to Unix slashes format and has no trailing slashes. The longest file extension is always considered. If the optional CACHE argument is specified, the result variable is added to the cache. </p>
<p>get_filename_component(VarName FileName<br />
                           PROGRAM[PROGRAM_ARGS ArgVar]<br />
                                  [CACHE])</p>
<p> The program in FileName will be found in the system search path or left as a full path. If PROGRAM_ARGS is present with PROGRAM, then any command-line arguments present in the FileName string are split from the program name and stored in ArgVar. This is used to separate a program name from its arguments in a command line string. </p>
<dt><code>get_property</code></p>
<dd> Get a property. </p>
<p>get_property(&lt;variable&gt;<br />
             &lt;GLOBAL |<br />
              DIRECTORY[dir] |<br />
              TARGET&lt;target&gt; |<br />
              SOURCE&lt;source&gt; |<br />
              TEST&lt;test&gt; |<br />
              VARIABLE&gt;<br />
                 PROPERTY&lt;name&gt;[SET | DEFINED | BRIEF_DOCS | FULL_DOCS])</p>
<p> Get one property from one object in a scope. The first argument specifies the variable in which to store the result. The second argument determines the scope from which to get the property. It must be one of the following: </p>
<p> GLOBAL scope is unique and does not accept a name. </p>
<p> DIRECTORY scope defaults to the current directory but another directory (already processed by CMake) may be named by full or relative path. </p>
<p> TARGET scope must name one existing target. </p>
<p> SOURCE scope must name one source file. </p>
<p> TEST scope must name one existing test. </p>
<p> VARIABLE scope is unique and does not accept a name. </p>
<p> The required PROPERTY option is immediately followed by the name of the property to get. If the property is not set an empty value is returned. If the SET option is given the variable is set to a boolean value indicating whether the property has been set. If the DEFINED option is given the variable is set to a boolean value indicating whether the property has been defined such as with define_property. If BRIEF_DOCS or FULL_DOCS is given then the variable is set to a string containing documentation for the requested property. If documentation is requested for a property that has not been defined NOTFOUND is returned. </p>
<dt><code>get_source_file_property</code></p>
<dd> Get a property for a source file. </p>
<pre>
  get_source_file_property(VAR file property)
</pre>
<p> Get a property from a source file. The value of the property is stored in the variable VAR. If the property is not found, VAR will be set to &quot;NOTFOUND&quot;. Use set_source_files_properties to set property values. Source file properties usually control how the file is built. One property that is always there is LOCATION </p>
<dt><code>get_target_property</code></p>
<dd> Get a property from a target. </p>
<pre>
  get_target_property(VAR target property)
</pre>
<p> Get a property from a target. The value of the property is stored in the variable VAR. If the property is not found, VAR will be set to &quot;NOTFOUND&quot;. Use set_target_properties to set property values. Properties are usually used to control how a target is built, but some query the target instead. This command can get properties for any target so far created. The targets do not need to be in the current CMakeLists.txt file. </p>
<dt><code>get_test_property</code></p>
<dd> Get a property of the test. </p>
<pre>
  get_test_property(test VAR property)
</pre>
<p> Get a property from the Test. The value of the property is stored in the variable VAR. If the property is not found, CMake will report an error. For a list of standard properties you can type cmake &#8211;help-property-list </p>
<dt><code>if</code></p>
<dd> Conditionally execute a group of commands. </p>
<p>if (expression)<br />
#then section.<br />
    COMMAND1(ARGS&#8230;)<br />
COMMAND2(ARGS&#8230;)<br />
&#8230; elseif(expression2)<br />
#elseif section.<br />
    COMMAND1(ARGS&#8230;)<br />
        COMMAND2(ARGS&#8230;)&#8230; else(expression)<br />
#else section.<br />
            COMMAND1(ARGS&#8230;)<br />
                COMMAND2(ARGS&#8230;)&#8230; endif(expression)</p>
<p> Evaluates the given expression. If the result is true, the commands in the THEN section are invoked. Otherwise, the commands in the else section are invoked. The elseif and else sections are optional. You may have multiple elseif clauses. Note that the same expression must be given to if, and endif. Long expressions can be used and the order or precedence is that the EXISTS, COMMAND, and DEFINED operators will be evaluated first. Then any EQUAL, LESS, GREATER, STRLESS, STRGREATER, STREQUAL, MATCHES will be evaluated. Then NOT operators and finally AND, OR operators will be evaluated. Possible expressions are: </p>
<pre>
  if(variable)
</pre>
<p> True if the variable&#8217;s value is not empty, 0, N, NO, OFF, FALSE, NOTFOUND, or &lt;variable&gt;-NOTFOUND. </p>
<pre>
  if(NOT variable)
</pre>
<p> True if the variable&#8217;s value is empty, 0, N, NO, OFF, FALSE, NOTFOUND, or &lt;variable&gt;-NOTFOUND. </p>
<pre>
  if(variable1 AND variable2)
</pre>
<p> True if both variables would be considered true individually. </p>
<pre>
  if(variable1 OR variable2)
</pre>
<p> True if either variable would be considered true individually. </p>
<pre>
  if(COMMAND command-name)
</pre>
<p> True if the given name is a command, macro or function that can be invoked. </p>
<pre>
  if(POLICY policy-id)
</pre>
<p> True if the given name is an existing policy (of the form CMP&lt;NNNN&gt;). </p>
<pre>
  if(TARGET target-name)
</pre>
<p> True if the given name is an existing target, built or imported. </p>
<pre>
  if(EXISTS file-name)
  if(EXISTS directory-name)
</pre>
<p> True if the named file or directory exists. Behavior is well-defined only for full paths. </p>
<pre>
  if(file1 IS_NEWER_THAN file2)
</pre>
<p> True if file1 is newer than file2 or if one of the two files doesn&#8217;t exist. Behavior is well-defined only for full paths. </p>
<pre>
  if(IS_DIRECTORY directory-name)
</pre>
<p> True if the given name is a directory. Behavior is well-defined only for full paths. </p>
<pre>
  if(IS_ABSOLUTE path)
</pre>
<p> True if the given path is an absolute path. </p>
<pre>
   if(variable MATCHES regex)
  if(string MATCHES regex)
</pre>
<p> True if the given string or variable&#8217;s value matches the given regular expression. </p>
<p>if (variable LESS number)<br />
    if (string LESS number)<br />
        if (variable GREATER number)<br />
            if (string GREATER number)<br />
                if (variable EQUAL number)<br />
                    if (string EQUAL number)</p>
<p> True if the given string or variable&#8217;s value is a valid number and the inequality or equality is true. </p>
<p>if (variable STRLESS string)<br />
    if (string STRLESS string)<br />
        if (variable STRGREATER string)<br />
            if (string STRGREATER string)<br />
                if (variable STREQUAL string)<br />
                    if (string STREQUAL string)</p>
<p> True if the given string or variable&#8217;s value is lexicographically less (or greater, or equal) than the string on the right. </p>
<pre>
  if(version1 VERSION_LESS version2)
  if(version1 VERSION_EQUAL version2)
  if(version1 VERSION_GREATER version2)
</pre>
<p> Component-wise integer version number comparison (version format is major[.minor[.patch[.tweak]]]). </p>
<pre>
  if(DEFINED variable)
</pre>
<p> True if the given variable is defined. It does not matter if the variable is true or false just if it has been set. </p>
<dt><code>include</code></p>
<dd> Read CMake listfile code from the given file. </p>
<p>include(&lt;file | module&gt;[OPTIONAL][RESULT_VARIABLE&lt;VAR&gt;]<br />
                       [NO_POLICY_SCOPE])</p>
<p> Reads CMake listfile code from the given file. Commands in the file are processed immediately as if they were written in place of the include command. If OPTIONAL is present, then no error is raised if the file does not exist. If RESULT_VARIABLE is given the variable will be set to the full filename which has been included or NOTFOUND if it failed. </p>
<p> If a module is specified instead of a file, the file with name &lt;modulename&gt;.cmake is searched in the CMAKE_MODULE_PATH. </p>
<p> See the cmake_policy() command documentation for discussion of the NO_POLICY_SCOPE option. </p>
<dt><code>include_directories</code></p>
<dd> Add include directories to the build. </p>
<p>include_directories([AFTER | BEFORE][SYSTEM] dir1 dir2&#8230;)</p>
<p> Add the given directories to those searched by the compiler for include files. By default the directories are appended onto the current list of directories. This default behavior can be changed by setting CMAKE_include_directories_BEFORE to ON. By using BEFORE or AFTER you can select between appending and prepending, independent from the default. If the SYSTEM option is given the compiler will be told that the directories are meant as system include directories on some platforms. </p>
<dt><code>include_external_msproject</code></p>
<dd> Include an external Microsoft project file in a workspace. </p>
<pre>
  include_external_msproject(projectname location
                             dep1 dep2 ...)
</pre>
<p> Includes an external Microsoft project in the generated workspace file. Currently does nothing on UNIX. This will create a target named INCLUDE_EXTERNAL_MSPROJECT_[projectname]. This can be used in the add_dependencies command to make things depend on the external project. </p>
<dt><code>include_regular_expression</code></p>
<dd> Set the regular expression used for dependency checking. </p>
<pre>
  include_regular_expression(regex_match [regex_complain])
</pre>
<p> Set the regular expressions used in dependency checking. Only files matching regex_match will be traced as dependencies. Only files matching regex_complain will generate warnings if they cannot be found (standard header paths are not searched). The defaults are: </p>
<pre>
  regex_match    = &quot;^.*$&quot; (match everything)
  regex_complain = &quot;^$&quot; (match empty string only)
</pre>
<dt><code>install</code></p>
<dd> Specify rules to run at install time. </p>
<p> This command generates installation rules for a project. Rules specified by calls to this command within a source directory are executed in order during installation. The order across directories is not defined. </p>
<p> There are multiple signatures for this command. Some of them define installation properties for files and targets. Properties common to multiple signatures are covered here but they are valid only for signatures that specify them. </p>
<p> DESTINATION arguments specify the directory on disk to which a file will be installed. If a full path (with a leading slash or drive letter) is given it is used directly. If a relative path is given it is interpreted relative to the value of CMAKE_INSTALL_PREFIX. </p>
<p> PERMISSIONS arguments specify permissions for installed files. Valid permissions are OWNER_READ, OWNER_WRITE, OWNER_EXECUTE, GROUP_READ, GROUP_WRITE, GROUP_EXECUTE, WORLD_READ, WORLD_WRITE, WORLD_EXECUTE, SETUID, and SETGID. Permissions that do not make sense on certain platforms are ignored on those platforms. </p>
<p> The CONFIGURATIONS argument specifies a list of build configurations for which the install rule applies (Debug, Release, etc.). </p>
<p> The COMPONENT argument specifies an installation component name with which the install rule is associated, such as &quot;runtime&quot; or &quot;development&quot;. During component-specific installation only install rules associated with the given component name will be executed. During a full installation all components are installed. </p>
<p> The RENAME argument specifies a name for an installed file that may be different from the original file. Renaming is allowed only when a single file is installed by the command. </p>
<p> The OPTIONAL argument specifies that it is not an error if the file to be installed does not exist. </p>
<p> The TARGETS signature: </p>
<p>install(TARGETS targets&#8230;[EXPORT&lt;export &#8211; name&gt;]<br />
                          [[ARCHIVE | LIBRARY | RUNTIME | FRAMEWORK | BUNDLE |<br />
                              PRIVATE_HEADER | PUBLIC_HEADER |<br />
                              RESOURCE]<br />
                               [DESTINATION&lt;dir&gt;]<br />
                               [PERMISSIONS permissions&#8230;]<br />
                               [CONFIGURATIONS[Debug | Release | &#8230;]]<br />
                               [COMPONENT&lt;component&gt;]<br />
                               [OPTIONAL][NAMELINK_ONLY | NAMELINK_SKIP]][&#8230;])</p>
<p> The TARGETS form specifies rules for installing targets from a project. There are five kinds of target files that may be installed: ARCHIVE, LIBRARY, RUNTIME, FRAMEWORK, and BUNDLE. Executables are treated as RUNTIME targets, except that those marked with the MACOSX_BUNDLE property are treated as BUNDLE targets on OS X. Static libraries are always treated as ARCHIVE targets. Module libraries are always treated as LIBRARY targets. For non-DLL platforms shared libraries are treated as LIBRARY targets, except that those marked with the FRAMEWORK property are treated as FRAMEWORK targets on OS X. For DLL platforms the DLL part of a shared library is treated as a RUNTIME target and the corresponding import library is treated as an ARCHIVE target. All Windows-based systems including Cygwin are DLL platforms. The ARCHIVE, LIBRARY, RUNTIME, and FRAMEWORK arguments change the type of target to which the subsequent properties apply. If none is given the installation properties apply to all target types. If only one is given then only targets of that type will be installed (which can be used to install just a DLL or just an import library). </p>
<p> The PRIVATE_HEADER, PUBLIC_HEADER, and RESOURCE arguments cause subsequent properties to be applied to installing a FRAMEWORK shared library target&#8217;s associated files on non-Apple platforms. Rules defined by these arguments are ignored on Apple platforms because the associated files are installed into the appropriate locations inside the framework folder. See documentation of the PRIVATE_HEADER, PUBLIC_HEADER, and RESOURCE target properties for details. </p>
<p> Either NAMELINK_ONLY or NAMELINK_SKIP may be specified as a LIBRARY option. On some platforms a versioned shared library has a symbolic link such as </p>
<pre>
  lib&lt;name&gt;.so -&gt; lib&lt;name&gt;.so.1
</pre>
<p> where &quot;lib&lt;name&gt;.so.1&quot; is the soname of the library and &quot;lib&lt;name&gt;.so&quot; is a &quot;namelink&quot; allowing linkers to find the library when given &quot;-l&lt;name&gt;&quot;. The NAMELINK_ONLY option causes installation of only the namelink when a library target is installed. The NAMELINK_SKIP option causes installation of library files other than the namelink when a library target is installed. When neither option is given both portions are installed. On platforms where versioned shared libraries do not have namelinks or when a library is not versioned the NAMELINK_SKIP option installs the library and the NAMELINK_ONLY option installs nothing. See the VERSION and SOVERSION target properties for details on creating versioned shared libraries. </p>
<p> One or more groups of properties may be specified in a single call to the TARGETS form of this command. A target may be installed more than once to different locations. Consider hypothetical targets &quot;myExe&quot;, &quot;mySharedLib&quot;, and &quot;myStaticLib&quot;. The code </p>
<pre>
    install(TARGETS myExe mySharedLib myStaticLib
            RUNTIME DESTINATION bin
            LIBRARY DESTINATION lib
            ARCHIVE DESTINATION lib/static)
    install(TARGETS mySharedLib DESTINATION /some/full/path)
</pre>
<p> will install myExe to &lt;prefix&gt;/bin and myStaticLib to &lt;prefix&gt;/lib/static. On non-DLL platforms mySharedLib will be installed to &lt;prefix&gt;/lib and /some/full/path. On DLL platforms the mySharedLib DLL will be installed to &lt;prefix&gt;/bin and /some/full/path and its import library will be installed to &lt;prefix&gt;/lib/static and /some/full/path. On non-DLL platforms mySharedLib will be installed to &lt;prefix&gt;/lib and /some/full/path. </p>
<p> The EXPORT option associates the installed target files with an export called &lt;export-name&gt;. It must appear before any RUNTIME, LIBRARY, or ARCHIVE options. See documentation of the install(EXPORT &#8230;) signature below for details. </p>
<p> Installing a target with EXCLUDE_FROM_ALL set to true has undefined behavior. </p>
<p> The FILES signature: </p>
<p>install(FILES files&#8230; DESTINATION&lt;dir&gt;[PERMISSIONS permissions&#8230;]<br />
                                       [CONFIGURATIONS[Debug | Release | &#8230;]]<br />
                                       [COMPONENT&lt;component&gt;]<br />
                                       [RENAME&lt;name&gt;][OPTIONAL])</p>
<p> The FILES form specifies rules for installing files for a project. File names given as relative paths are interpreted with respect to the current source directory. Files installed by this form are by default given permissions OWNER_WRITE, OWNER_READ, GROUP_READ, and WORLD_READ if no PERMISSIONS argument is given. </p>
<p> The PROGRAMS signature: </p>
<p>install(PROGRAMS files&#8230; DESTINATION&lt;dir&gt;[PERMISSIONS permissions&#8230;]<br />
                                          [CONFIGURATIONS[Debug | Release | &#8230;]]<br />
                                          [COMPONENT&lt;component&gt;]<br />
                                          [RENAME&lt;name&gt;][OPTIONAL])</p>
<p> The PROGRAMS form is identical to the FILES form except that the default permissions for the installed file also include OWNER_EXECUTE, GROUP_EXECUTE, and WORLD_EXECUTE. This form is intended to install programs that are not targets, such as shell scripts. Use the TARGETS form to install targets built within the project. </p>
<p> The DIRECTORY signature: </p>
<p>install(DIRECTORY dirs&#8230; DESTINATION&lt;dir&gt;[FILE_PERMISSIONS permissions&#8230;]<br />
                                          [DIRECTORY_PERMISSIONS permissions&#8230;]<br />
                                          [USE_SOURCE_PERMISSIONS]<br />
                                          [CONFIGURATIONS[Debug | Release | &#8230;]]<br />
                                          [COMPONENT&lt;component&gt;][FILES_MATCHING]<br />
                                          [[PATTERN&lt;pattern&gt; | REGEX&lt;regex&gt;]<br />
                                               [EXCLUDE][PERMISSIONS permissions&#8230;]][&#8230;])</p>
<p> The DIRECTORY form installs contents of one or more directories to a given destination. The directory structure is copied verbatim to the destination. The last component of each directory name is appended to the destination directory but a trailing slash may be used to avoid this because it leaves the last component empty. Directory names given as relative paths are interpreted with respect to the current source directory. If no input directory names are given the destination directory will be created but nothing will be installed into it. The FILE_PERMISSIONS and DIRECTORY_PERMISSIONS options specify permissions given to files and directories in the destination. If USE_SOURCE_PERMISSIONS is specified and FILE_PERMISSIONS is not, file permissions will be copied from the source directory structure. If no permissions are specified files will be given the default permissions specified in the FILES form of the command, and the directories will be given the default permissions specified in the PROGRAMS form of the command. </p>
<p> Installation of directories may be controlled with fine granularity using the PATTERN or REGEX options. These &quot;match&quot; options specify a globbing pattern or regular expression to match directories or files encountered within input directories. They may be used to apply certain options (see below) to a subset of the files and directories encountered. The full path to each input file or directory (with forward slashes) is matched against the expression. A PATTERN will match only complete file names: the portion of the full path matching the pattern must occur at the end of the file name and be preceded by a slash. A REGEX will match any portion of the full path but it may use &#8216;/&#8217; and &#8216;$&#8217; to simulate the PATTERN behavior. By default all files and directories are installed whether or not they are matched. The FILES_MATCHING option may be given before the first match option to disable installation of files (but not directories) not matched by any expression. For example, the code </p>
<pre>
  install(DIRECTORY src/ DESTINATION include/myproj
          FILES_MATCHING PATTERN &quot;*.h&quot;)
</pre>
<p> will extract and install header files from a source tree. </p>
<p> Some options may follow a PATTERN or REGEX expression and are applied only to files or directories matching them. The EXCLUDE option will skip the matched file or directory. The PERMISSIONS option overrides the permissions setting for the matched file or directory. For example the code </p>
<pre>
  install(DIRECTORY icons scripts/ DESTINATION share/myproj
          PATTERN &quot;CVS&quot; EXCLUDE
          PATTERN &quot;scripts/*&quot;
          PERMISSIONS OWNER_EXECUTE OWNER_WRITE OWNER_READ
                      GROUP_EXECUTE GROUP_READ)
</pre>
<p> will install the icons directory to share/myproj/icons and the scripts directory to share/myproj. The icons will get default file permissions, the scripts will be given specific permissions, and any CVS directories will be excluded. </p>
<p> The SCRIPT and CODE signature: </p>
<p>install([[SCRIPT&lt;file&gt;] [CODE&lt;code&gt;]][&#8230;])</p>
<p> The SCRIPT form will invoke the given CMake script files during installation. If the script file name is a relative path it will be interpreted with respect to the current source directory. The CODE form will invoke the given CMake code during installation. Code is specified as a single argument inside a double-quoted string. For example, the code </p>
<pre>
  install(CODE &quot;MESSAGE(\&quot;Sample install message.\&quot;)&quot;)
</pre>
<p> will print a message during installation. </p>
<p> The EXPORT signature: </p>
<p>install(EXPORT&lt;export &#8211; name&gt; DESTINATION&lt;dir&gt;[NAMESPACE&lt;namespace&gt;][FILE&lt;name&gt;.cmake]<br />
                                              [PERMISSIONS permissions&#8230;]<br />
                                              [CONFIGURATIONS[Debug | Release | &#8230;]]<br />
                                              [COMPONENT&lt;component&gt;])</p>
<p> The EXPORT form generates and installs a CMake file containing code to import targets from the installation tree into another project. Target installations are associated with the export &lt;export-name&gt; using the EXPORT option of the install(TARGETS &#8230;) signature documented above. The NAMESPACE option will prepend &lt;namespace&gt; to the target names as they are written to the import file. By default the generated file will be called &lt;export-name&gt;.cmake but the FILE option may be used to specify a different name. The value given to the FILE option must be a file name with the &quot;.cmake&quot; extension. If a CONFIGURATIONS option is given then the file will only be installed when one of the named configurations is installed. Additionally, the generated import file will reference only the matching target configurations. If a COMPONENT option is specified that does not match that given to the targets associated with &lt;export-name&gt; the behavior is undefined. If a library target is included in the export but a target to which it links is not included the behavior is unspecified. </p>
<p> The EXPORT form is useful to help outside projects use targets built and installed by the current project. For example, the code </p>
<pre>
  install(TARGETS myexe EXPORT myproj DESTINATION bin)
  install(EXPORT myproj NAMESPACE mp_ DESTINATION lib/myproj)
</pre>
<p> will install the executable myexe to &lt;prefix&gt;/bin and code to import it in the file &quot;&lt;prefix&gt;/lib/myproj/myproj.cmake&quot;. An outside project may load this file with the include command and reference the myexe executable from the installation tree using the imported target name mp_myexe as if the target were built in its own tree. </p>
<p> NOTE: This command supercedes the INSTALL_TARGETS command and the target properties PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT. It also replaces the FILES forms of the INSTALL_FILES and INSTALL_PROGRAMS commands. The processing order of these install rules relative to those generated by INSTALL_TARGETS, INSTALL_FILES, and INSTALL_PROGRAMS commands is not defined. </p>
<dt><code>link_directories</code></p>
<dd> Specify directories in which the linker will look for libraries. </p>
<pre>
  link_directories(directory1 directory2 ...)
</pre>
<p> Specify the paths in which the linker should search for libraries. The command will apply only to targets created after it is called. For historical reasons, relative paths given to this command are passed to the linker unchanged (unlike many CMake commands which interpret them relative to the current source directory). </p>
<dt><code>list</code></p>
<dd> List operations. </p>
<p>list(LENGTH&lt;list&gt;&lt;output variable&gt;)<br />
    list(GET&lt;list&gt;&lt;element index&gt;[&lt;element index&gt;&#8230;]&lt;output variable&gt;)<br />
        list(APPEND&lt;list&gt;&lt;element&gt;[&lt;element&gt;&#8230;])<br />
            list(FIND&lt;list&gt;&lt;value&gt;&lt;output variable&gt;)<br />
                list(INSERT&lt;list&gt;&lt;element_index&gt;&lt;element&gt;[&lt;element&gt;&#8230;])<br />
                    list(REMOVE_ITEM&lt;list&gt;&lt;value&gt;[&lt;value&gt;&#8230;])<br />
                        list(REMOVE_AT&lt;list&gt;&lt;index&gt;[&lt;index&gt;&#8230;])<br />
                            list(REMOVE_DUPLICATES&lt;list&gt;)<br />
                                list(REVERSE&lt;list&gt;)<br />
                                    list(SORT&lt;list&gt;)</p>
<p> LENGTH will return a given list&#8217;s length. </p>
<p> GET will return list of elements specified by indices from the list. </p>
<p> APPEND will append elements to the list. </p>
<p> FIND will return the index of the element specified in the list or -1 if it wasn&#8217;t found. </p>
<p> INSERT will insert elements to the list to the specified location. </p>
<p> REMOVE_AT and REMOVE_ITEM will remove items from the list. The difference is that REMOVE_ITEM will remove the given items, while REMOVE_AT will remove the items at the given indices. </p>
<p> REMOVE_DUPLICATES will remove duplicated items in the list. </p>
<p> REVERSE reverses the contents of the list in-place. </p>
<p> SORT sorts the list in-place alphabetically. </p>
<p> NOTES: A list in cmake is a ; separated group of strings. To create a list the set command can be used. For example, set(var a b c d e) creates a list with a;b;c;d;e, and set(var &quot;a b c d e&quot;) creates a string or a list with one item in it. </p>
<p> When specifying index values, if &lt;element index&gt; is 0 or greater, it is indexed from the beginning of the list, with 0 representing the first list element. If &lt;element index&gt; is -1 or lesser, it is indexed from the end of the list, with -1 representing the last list element. Be careful when counting with negative indices: they do not start from 0. -0 is equivalent to 0, the first list element. </p>
<dt><code>load_cache</code></p>
<dd> Load in the values from another project&#8217;s CMake cache. </p>
<pre>
  load_cache(pathToCacheFile READ_WITH_PREFIX
             prefix entry1...)
</pre>
<p> Read the cache and store the requested entries in variables with their name prefixed with the given prefix. This only reads the values, and does not create entries in the local project&#8217;s cache. </p>
<p>load_cache(pathToCacheFile[EXCLUDE entry1&#8230;]<br />
                          [INCLUDE_INTERNALS entry1&#8230;])</p>
<p> Load in the values from another cache and store them in the local project&#8217;s cache as internal entries. This is useful for a project that depends on another project built in a different tree. EXCLUDE option can be used to provide a list of entries to be excluded. INCLUDE_INTERNALS can be used to provide a list of internal entries to be included. Normally, no internal entries are brought in. Use of this form of the command is strongly discouraged, but it is provided for backward compatibility. </p>
<dt><code>load_command</code></p>
<dd> Load a command into a running CMake. </p>
<pre>
  load_command(COMMAND_NAME &lt;loc1&gt; [loc2 ...])
</pre>
<p> The given locations are searched for a library whose name is cmCOMMAND_NAME. If found, it is loaded as a module and the command is added to the set of available CMake commands. Usually, TRY_COMPILE is used before this command to compile the module. If the command is successfully loaded a variable named </p>
<pre>
  CMAKE_LOADED_COMMAND_&lt;COMMAND_NAME&gt;
</pre>
<p> will be set to the full path of the module that was loaded. Otherwise the variable will not be set. </p>
<dt><code>macro</code></p>
<dd> Start recording a macro for later invocation as a command. </p>
<p>macro(&lt;name&gt;[arg1[arg2[arg3&#8230;]]])<br />
    COMMAND1(ARGS&#8230;)<br />
        COMMAND2(ARGS&#8230;)&#8230; endmacro(&lt;name&gt;)</p>
<p> Define a macro named &lt;name&gt; that takes arguments named arg1 arg2 arg3 (&#8230;). Commands listed after macro, but before the matching endmacro, are not invoked until the macro is invoked. When it is invoked, the commands recorded in the macro are first modified by replacing formal parameters (${arg1}) with the arguments passed, and then invoked as normal commands. In addition to referencing the formal parameters you can reference the values ${ARGC} which will be set to the number of arguments passed into the function as well as ${ARGV0} ${ARGV1} ${ARGV2} &#8230; which will have the actual values of the arguments passed in. This facilitates creating macros with optional arguments. Additionally ${ARGV} holds the list of all arguments given to the macro and ${ARGN} holds the list of argument pass the last expected argument. Note that the parameters to a macro and values such as ARGN are not variables in the usual CMake sense. They are string replacements much like the c preprocessor would do with a macro. If you want true CMake variables you should look at the function command. </p>
<p> See the cmake_policy() command documentation for the behavior of policies inside macros. </p>
<dt><code>mark_as_advanced</code></p>
<dd> Mark cmake cached variables as advanced. </p>
<pre>
  mark_as_advanced([CLEAR|FORCE] VAR VAR2 VAR...)
</pre>
<p> Mark the named cached variables as advanced. An advanced variable will not be displayed in any of the cmake GUIs unless the show advanced option is on. If CLEAR is the first argument advanced variables are changed back to unadvanced. If FORCE is the first argument, then the variable is made advanced. If neither FORCE nor CLEAR is specified, new values will be marked as advanced, but if the variable already has an advanced/non-advanced state, it will not be changed. </p>
<p> It does nothing in script mode. </p>
<dt><code>math</code></p>
<dd> Mathematical expressions. </p>
<pre>
  math(EXPR &lt;output variable&gt; &lt;math expression&gt;)
</pre>
<p> EXPR evaluates mathematical expression and return result in the output variable. Example mathematical expression is &#8216;5 * ( 10 + 13 )&#8217;. Supported operators are + &#8211; * / % | &amp; ^ ~ &lt;&lt; &gt;&gt; * / %. They have the same meaning as they do in c code. </p>
<dt><code>message</code></p>
<dd> Display a message to the user. </p>
<pre>
  message([SEND_ERROR | STATUS | FATAL_ERROR]
          &quot;message to display&quot; ...)
</pre>
<p> By default the message is displayed in a pop up window (CMakeSetup), or in the stdout of cmake, or the error section of ccmake. If the first argument is SEND_ERROR then an error is raised, and the generate phase will be skipped. If the first argument is FATAL_ERROR, all processing is halted. If the first argument is STATUS then the message is displayed in the progress line for the GUI, or with a &#8212; in the command line cmake. </p>
<dt><code>option</code></p>
<dd> Provides an option that the user can optionally select. </p>
<pre>
  option(&lt;option_variable&gt; &quot;help string describing option&quot;
         [initial value])
</pre>
<p> Provide an option for the user to select as ON or OFF. If no initial value is provided, OFF is used. </p>
<dt><code>output_required_files</code></p>
<dd> Output a list of required source files for a specified source file. </p>
<pre>
  output_required_files(srcfile outputfile)
</pre>
<p> Outputs a list of all the source files that are required by the specified srcfile. This list is written into outputfile. This is similar to writing out the dependencies for srcfile except that it jumps from .h files into .cxx, .c and .cpp files if possible. </p>
<dt><code>project</code></p>
<dd> Set a name for the entire project. </p>
<pre>
  project(&lt;projectname&gt; [languageName1 languageName2 ... ] )
</pre>
<p> Sets the name of the project. Additionally this sets the variables &lt;projectName&gt;_BINARY_DIR and &lt;projectName&gt;_SOURCE_DIR to the respective values. </p>
<p> Optionally you can specify which languages your project supports. Example languages are CXX (i.e. C++), C, Fortran, etc. By default C and CXX are enabled. E.g. if you do not have a C++ compiler, you can disable the check for it by explicitely listing the languages you want to support, e.g. C. By using the special language &quot;NONE&quot; all checks for any language can be disabled. </p>
<dt><code>qt_wrap_cpp</code></p>
<dd> Create Qt Wrappers. </p>
<pre>
  qt_wrap_cpp(resultingLibraryName DestName
              SourceLists ...)
</pre>
<p> Produce moc files for all the .h files listed in the SourceLists. The moc files will be added to the library using the DestName source list. </p>
<dt><code>qt_wrap_ui</code></p>
<dd> Create Qt user interfaces Wrappers. </p>
<pre>
  qt_wrap_ui(resultingLibraryName HeadersDestName
             SourcesDestName SourceLists ...)
</pre>
<p> Produce .h and .cxx files for all the .ui files listed in the SourceLists. The .h files will be added to the library using the HeadersDestNamesource list. The .cxx files will be added to the library using the SourcesDestNamesource list. </p>
<dt><code>remove_definitions</code></p>
<dd> Removes -D define flags added by add_definitions. </p>
<pre>
  remove_definitions(-DFOO -DBAR ...)
</pre>
<p> Removes flags (added by add_definitions) from the compiler command line for sources in the current directory and below. </p>
<dt><code>return</code></p>
<dd> Return from a file, directory or function. </p>
<pre>
  return()
</pre>
<p> Returns from a file, directory or function. When this command is encountered in an included file (via include() or find_package()), it causes processing of the current file to stop and control is returned to the including file. If it is encountered in a file which is not included by another file, e.g. a CMakeLists.txt, control is returned to the parent directory if there is one. If return is called in a function, control is returned to the caller of the function. Note that a macro is not a function and does not handle return like a function does. </p>
<dt><code>separate_arguments</code></p>
<dd> Split space separated arguments into a semi-colon separated list. </p>
<pre>
  separate_arguments(VARIABLE)
</pre>
<p> Convert the value of VARIABLE to a semi-colon separated list. All spaces are replaced with &#8216;;&#8217;. This helps with generating command lines. </p>
<dt><code>set</code></p>
<dd> Set a CMAKE variable to a given value. </p>
<p>set(&lt;variable&gt;&lt;value&gt; [[CACHE&lt;type&gt;&lt;docstring&gt; [FORCE]] | PARENT_SCOPE])</p>
<p> Within CMake sets &lt;variable&gt; to the value &lt;value&gt;. &lt;value&gt; is expanded before &lt;variable&gt; is set to it. If CACHE is present, then the &lt;variable&gt; is put in the cache. &lt;type&gt; and &lt;docstring&gt; are then required. &lt;type&gt; is used by the CMake GUI to choose a widget with which the user sets a value. The value for &lt;type&gt; may be one of </p>
<pre>
  FILEPATH = File chooser dialog.
  PATH     = Directory chooser dialog.
  STRING   = Arbitrary string.
  BOOL     = Boolean ON/OFF checkbox.
  INTERNAL = No GUI entry (used for persistent variables).
</pre>
<p> If &lt;type&gt; is INTERNAL, then the &lt;value&gt; is always written into the cache, replacing any values existing in the cache. If it is not a cache variable, then this always writes into the current makefile. The FORCE option will overwrite the cache value removing any changes by the user. </p>
<p> If PARENT_SCOPE is present, the variable will be set in the scope above the current scope. Each new directory or function creates a new scope. This command will set the value of a variable into the parent directory or calling function (whichever is applicable to the case at hand) If VALUE is not specified then the variable is removed from the parent scope. </p>
<pre>
  set(&lt;variable&gt; &lt;value1&gt; ... &lt;valueN&gt;)
</pre>
<p> In this case &lt;variable&gt; is set to a semicolon separated list of values. </p>
<p> &lt;variable&gt; can be an environment variable such as: </p>
<pre>
  set( ENV{PATH} /home/martink )
</pre>
<p> in which case the environment variable will be set. </p>
<dt><code>set_directory_properties</code></p>
<dd> Set a property of the directory. </p>
<pre>
  set_directory_properties(PROPERTIES prop1 value1 prop2 value2)
</pre>
<p> Set a property for the current directory and subdirectories. If the property is not found, CMake will report an error. The properties include: INCLUDE_DIRECTORIES, LINK_DIRECTORIES, INCLUDE_REGULAR_EXPRESSION, and ADDITIONAL_MAKE_CLEAN_FILES. </p>
<p> ADDITIONAL_MAKE_CLEAN_FILES is a list of files that will be cleaned as a part of &quot;make clean&quot; stage. </p>
<dt><code>set_property</code></p>
<dd> Set a named property in a given scope. </p>
<p>set_property(&lt;GLOBAL |<br />
              DIRECTORY[dir] |<br />
              TARGET[target1[target2&#8230;]] |<br />
              SOURCE[src1[src2&#8230;]] |<br />
              TEST[test1[test2&#8230;]]&gt;[APPEND] PROPERTY&lt;name&gt;[value1[value2&#8230;]])</p>
<p> Set one property on zero or more objects of a scope. The first argument determines the scope in which the property is set. It must be one of the following: </p>
<p> GLOBAL scope is unique and does not accept a name. </p>
<p> DIRECTORY scope defaults to the current directory but another directory (already processed by CMake) may be named by full or relative path. </p>
<p> TARGET scope may name zero or more existing targets. </p>
<p> SOURCE scope may name zero or more source files. </p>
<p> TEST scope may name zero or more existing tests. </p>
<p> The required PROPERTY option is immediately followed by the name of the property to set. Remaining arguments are used to compose the property value in the form of a semicolon-separated list. If the APPEND option is given the list is appended to any existing property value. </p>
<dt><code>set_source_files_properties</code></p>
<dd> Source files can have properties that affect how they are built. </p>
<pre>
  set_source_files_properties(file1 file2 ...
                              PROPERTIES prop1 value1
                              prop2 value2 ...)
</pre>
<p> Set properties on a file. The syntax for the command is to list all the files you want to change, and then provide the values you want to set next. You can make up your own properties as well. The following are used by CMake. The ABSTRACT flag (boolean) is used by some class wrapping commands. If WRAP_EXCLUDE (boolean) is true then many wrapping commands will ignore this file. If GENERATED (boolean) is true then it is not an error if this source file does not exist when it is added to a target. Obviously, it must be created (presumably by a custom command) before the target is built. If the HEADER_FILE_ONLY (boolean) property is true then the file is not compiled. This is useful if you want to add extra non build files to an IDE. OBJECT_DEPENDS (string) adds dependencies to the object file. COMPILE_FLAGS (string) is passed to the compiler as additional command line arguments when the source file is compiled. LANGUAGE (string) CXX|C will change the default compiler used to compile the source file. The languages used need to be enabled in the PROJECT command. If SYMBOLIC (boolean) is set to true the build system will be informed that the source file is not actually created on disk but instead used as a symbolic name for a build rule. </p>
<dt><code>set_target_properties</code></p>
<dd> Targets can have properties that affect how they are built. </p>
<pre>
  set_target_properties(target1 target2 ...
                        PROPERTIES prop1 value1
                        prop2 value2 ...)
</pre>
<p> Set properties on a target. The syntax for the command is to list all the files you want to change, and then provide the values you want to set next. You can use any prop value pair you want and extract it later with the GET_TARGET_PROPERTY command. </p>
<p> Properties that affect the name of a target&#8217;s output file are as follows. The PREFIX and SUFFIX properties override the default target name prefix (such as &quot;lib&quot;) and suffix (such as &quot;.so&quot;). IMPORT_PREFIX and IMPORT_SUFFIX are the equivalent properties for the import library corresponding to a DLL (for SHARED library targets). OUTPUT_NAME sets the real name of a target when it is built and can be used to help create two targets of the same name even though CMake requires unique logical target names. There is also a &lt;CONFIG&gt;_OUTPUT_NAME that can set the output name on a per-configuration basis. &lt;CONFIG&gt;_POSTFIX sets a postfix for the real name of the target when it is built under the configuration named by &lt;CONFIG&gt; (in upper-case, such as &quot;DEBUG_POSTFIX&quot;). The value of this property is initialized when the target is created to the value of the variable CMAKE_&lt;CONFIG&gt;_POSTFIX (except for executable targets because earlier CMake versions which did not use this variable for executables). </p>
<p> The LINK_FLAGS property can be used to add extra flags to the link step of a target. LINK_FLAGS_&lt;CONFIG&gt; will add to the configuration &lt;CONFIG&gt;, for example, DEBUG, RELEASE, MINSIZEREL, RELWITHDEBINFO. DEFINE_SYMBOL sets the name of the preprocessor symbol defined when compiling sources in a shared library. If not set here then it is set to target_EXPORTS by default (with some substitutions if the target is not a valid C identifier). This is useful for headers to know whether they are being included from inside their library our outside to properly setup dllexport/dllimport decorations. The COMPILE_FLAGS property sets additional compiler flags used to build sources within the target. It may also be used to pass additional preprocessor definitions. </p>
<p> The LINKER_LANGUAGE property is used to change the tool used to link an executable or shared library. The default is set the language to match the files in the library. CXX and C are common values for this property. </p>
<p> For shared libraries VERSION and SOVERSION can be used to specify the build version and api version respectively. When building or installing appropriate symlinks are created if the platform supports symlinks and the linker supports so-names. If only one of both is specified the missing is assumed to have the same version number. For executables VERSION can be used to specify the build version. When building or installing appropriate symlinks are created if the platform supports symlinks. For shared libraries and executables on Windows the VERSION attribute is parsed to extract a &quot;major.minor&quot; version number. These numbers are used as the image version of the binary. </p>
<p> There are a few properties used to specify RPATH rules. INSTALL_RPATH is a semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). INSTALL_RPATH_USE_LINK_PATH is a boolean that if set to true will append directories in the linker search path and outside the project to the INSTALL_RPATH. SKIP_BUILD_RPATH is a boolean specifying whether to skip automatic generation of an rpath allowing the target to run from the build tree. BUILD_WITH_INSTALL_RPATH is a boolean specifying whether to link the target in the build tree with the INSTALL_RPATH. This takes precedence over SKIP_BUILD_RPATH and avoids the need for relinking before installation. INSTALL_NAME_DIR is a string specifying the directory portion of the &quot;install_name&quot; field of shared libraries on Mac OSX to use in the installed targets. When the target is created the values of the variables CMAKE_INSTALL_RPATH, CMAKE_INSTALL_RPATH_USE_LINK_PATH, CMAKE_SKIP_BUILD_RPATH, CMAKE_BUILD_WITH_INSTALL_RPATH, and CMAKE_INSTALL_NAME_DIR are used to initialize these properties. </p>
<p> PROJECT_LABEL can be used to change the name of the target in an IDE like visual studio. VS_KEYWORD can be set to change the visual studio keyword, for example QT integration works better if this is set to Qt4VSv1.0. </p>
<p> VS_SCC_PROJECTNAME, VS_SCC_LOCALPATH, VS_SCC_PROVIDER can be set to add support for source control bindings in a Visual Studio project file. </p>
<p> When a library is built CMake by default generates code to remove any existing library using all possible names. This is needed to support libraries that switch between STATIC and SHARED by a user option. However when using OUTPUT_NAME to build a static and shared library of the same name using different logical target names the two targets will remove each other&#8217;s files. This can be prevented by setting the CLEAN_DIRECT_OUTPUT property to 1. </p>
<p> The PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT properties are the old way to specify CMake scripts to run before and after installing a target. They are used only when the old INSTALL_TARGETS command is used to install the target. Use the INSTALL command instead. </p>
<p> The EXCLUDE_FROM_DEFAULT_BUILD property is used by the visual studio generators. If it is set to 1 the target will not be part of the default build when you select &quot;Build Solution&quot;. </p>
<dt><code>set_tests_properties</code></p>
<dd> Set a property of the tests. </p>
<pre>
  set_tests_properties(test1 [test2...] PROPERTIES prop1 value1 prop2 value2)
</pre>
<p> Set a property for the tests. If the property is not found, CMake will report an error. The properties include: </p>
<p> WILL_FAIL: If set to true, this will invert the pass/fail flag of the test. </p>
<p> PASS_REGULAR_EXPRESSION: If set, the test output will be checked against the specified regular expressions and at least one of the regular expressions has to match, otherwise the test will fail. </p>
<pre>
  Example: PASS_REGULAR_EXPRESSION &quot;TestPassed;All ok&quot;
</pre>
<p> FAIL_REGULAR_EXPRESSION: If set, if the output will match to one of specified regular expressions, the test will fail. </p>
<p>Example : PASS_REGULAR_EXPRESSION &#8220;[^a-z]Error;ERROR;Failed&#8221;</p>
<p> Both PASS_REGULAR_EXPRESSION and FAIL_REGULAR_EXPRESSION expect a list of regular expressions. </p>
<dt><code>site_name</code></p>
<dd> Set the given variable to the name of the computer. </p>
<pre>
  site_name(variable)
</pre>
<dt><code>source_group</code></p>
<dd> Define a grouping for sources in the makefile. </p>
<p>source_group(name[REGULAR_EXPRESSION regex][FILES src1 src2&#8230;])</p>
<p> Defines a group into which sources will be placed in project files. This is mainly used to setup file tabs in Visual Studio. Any file whose name is listed or matches the regular expression will be placed in this group. If a file matches multiple groups, the LAST group that explicitly lists the file will be favored, if any. If no group explicitly lists the file, the LAST group whose regular expression matches the file will be favored. </p>
<p> The name of the group may contain backslashes to specify subgroups: </p>
<pre>
  source_group(outer\inner ...)
</pre>
<p> For backwards compatibility, this command is also supports the format: </p>
<pre>
  source_group(name regex)
</pre>
<dt><code>string</code></p>
<dd> String operations. </p>
<p>string(REGEX MATCH&lt;regular_expression&gt;<br />
       &lt;output variable&gt;&lt;input&gt;[&lt;input&gt;&#8230;])<br />
    string(REGEX MATCHALL&lt;regular_expression&gt;<br />
           &lt;output variable&gt;&lt;input&gt;[&lt;input&gt;&#8230;])<br />
        string(REGEX REPLACE&lt;regular_expression&gt;<br />
               &lt;replace_expression&gt;&lt;output variable&gt;<br />
               &lt;input&gt;[&lt;input&gt;&#8230;])<br />
            string(REPLACE&lt;match_string&gt;<br />
                   &lt;replace_string&gt;&lt;output variable&gt;<br />
                   &lt;input&gt;[&lt;input&gt;&#8230;])<br />
                string(COMPARE EQUAL&lt;string1&gt;&lt;string2&gt;&lt;output variable&gt;)<br />
                    string(COMPARE NOTEQUAL&lt;string1&gt;&lt;string2&gt;&lt;output variable&gt;)<br />
                        string(COMPARE LESS&lt;string1&gt;&lt;string2&gt;&lt;output variable&gt;)<br />
                            string(COMPARE GREATER&lt;string1&gt;&lt;string2&gt;&lt;output variable&gt;)<br />
                                string(ASCII&lt;number&gt;[&lt;number&gt;&#8230;]&lt;output variable&gt;)<br />
                                    string(CONFIGURE&lt;string1&gt;&lt;output variable&gt;[@ONLY][ESCAPE_QUOTES])<br />
                                        string(TOUPPER&lt;string1&gt;&lt;output variable&gt;)<br />
                                            string(TOLOWER&lt;string1&gt;&lt;output variable&gt;)<br />
                                                string(LENGTH&lt;string&gt;&lt;output variable&gt;)<br />
                                                    string(SUBSTRING&lt;string&gt;&lt;begin&gt;&lt;length&gt;&lt;output variable&gt;)<br />
                                                        string(STRIP&lt;string&gt;&lt;output variable&gt;)<br />
                                                            string(RANDOM[LENGTH&lt;length&gt;][ALPHABET&lt;alphabet&gt;]&lt;output variable&gt;)</p>
<p> REGEX MATCH will match the regular expression once and store the match in the output variable. </p>
<p> REGEX MATCHALL will match the regular expression as many times as possible and store the matches in the output variable as a list. </p>
<p> REGEX REPLACE will match the regular expression as many times as possible and substitute the replacement expression for the match in the output. The replace expression may refer to paren-delimited subexpressions of the match using \1, \2, &#8230;, \9. Note that two backslashes (\1) are required in CMake code to get a backslash through argument parsing. </p>
<p> REPLACE will replace all occurrences of match_string in the input with replace_string and store the result in the output. </p>
<p> COMPARE EQUAL/NOTEQUAL/LESS/GREATER will compare the strings and store true or false in the output variable. </p>
<p> ASCII will convert all numbers into corresponding ASCII characters. </p>
<p> CONFIGURE will transform a string like CONFIGURE_FILE transforms a file. </p>
<p> TOUPPER/TOLOWER will convert string to upper/lower characters. </p>
<p> LENGTH will return a given string&#8217;s length. </p>
<p> SUBSTRING will return a substring of a given string. </p>
<p> STRIP will return a substring of a given string with leading and trailing spaces removed. </p>
<p> RANDOM will return a random string of given length consisting of characters from the given alphabet. Default length is 5 characters and default alphabet is all numbers and upper and lower case letters. </p>
<p> The following characters have special meaning in regular expressions: </p>
<p>^Matches at beginning of a line<br />
     $ Matches at end of a line<br />
         .Matches any single character<br />
             [] Matches any<br />
             character(s)<br />
inside the brackets<br />
            [^] Matches any<br />
            character(s) not inside the brackets<br />
        &#8211; Matches any character in range on either side of a dash<br />
              * Matches preceding pattern zero<br />
    or more times + Matches preceding pattern one or more times<br />
    ? Matches preceding pattern zero or once only<br />
                                            | Matches a pattern on either side of the |<br />
                                            () Saves a matched subexpression,<br />
    which can be referenced<br />
        in the REGEX REPLACE operation.Additionally it is saved<br />
        by all regular expression<br />
        &#8211; related commands,<br />
    including<br />
    e.g.if (MATCHES),<br />
    in the variables CMAKE_MATCH_(0..9).</p>
<dt><code>target_link_libraries</code></p>
<dd> Link a target to given libraries. </p>
<p>target_link_libraries(&lt;target&gt;[lib1[lib2[&#8230;]]]<br />
                      [[debug | optimized | general]&lt;lib&gt;]&#8230;)</p>
<p> Specify a list of libraries to be linked into the specified target. If any library name matches that of a target in the current project a dependency will automatically be added in the build system to make sure the library being linked is up-to-date before the target links. </p>
<p> A &quot;debug&quot;, &quot;optimized&quot;, or &quot;general&quot; keyword indicates that the library immediately following it is to be used only for the corresponding build configuration. The &quot;debug&quot; keyword corresponds to the Debug configuration (or to configurations named in the DEBUG_CONFIGURATIONS global property if it is set). The &quot;optimized&quot; keyword corresponds to all other configurations. The &quot;general&quot; keyword corresponds to all configurations, and is purely optional (assumed if omitted). Higher granularity may be achieved for per-configuration rules by creating and linking to IMPORTED library targets. See the IMPORTED mode of the add_library command for more information. </p>
<p> Library dependencies are transitive by default. When this target is linked into another target then the libraries linked to this target will appear on the link line for the other target too. See the LINK_INTERFACE_LIBRARIES target property to override the set of transitive link dependencies for a target. </p>
<p>target_link_libraries(&lt;target&gt; LINK_INTERFACE_LIBRARIES<br />
                      [[debug | optimized | general]&lt;lib&gt;]&#8230;)</p>
<p> The LINK_INTERFACE_LIBRARIES mode appends the libraries to the LINK_INTERFACE_LIBRARIES and its per-configuration equivalent target properties instead of using them for linking. Libraries specified as &quot;debug&quot; are appended to the the LINK_INTERFACE_LIBRARIES_DEBUG property (or to the properties corresponding to configurations listed in the DEBUG_CONFIGURATIONS global property if it is set). Libraries specified as &quot;optimized&quot; are appended to the the LINK_INTERFACE_LIBRARIES property. Libraries specified as &quot;general&quot; (or without any keyword) are treated as if specified for both &quot;debug&quot; and &quot;optimized&quot;. </p>
<dt><code>try_compile</code></p>
<dd> Try compiling some code. </p>
<p>try_compile(RESULT_VAR bindir srcdir<br />
                projectName&lt;targetname&gt;[CMAKE_FLAGS&lt;Flags&gt;]<br />
                                       [OUTPUT_VARIABLE var])</p>
<p> Try compiling a program. In this form, srcdir should contain a complete CMake project with a CMakeLists.txt file and all sources. The bindir and srcdir will not be deleted after this command is run. If &lt;target name&gt; is specified then build just that target otherwise the all or ALL_BUILD target is built. </p>
<p>  try_compile(RESULT_VAR bindir srcfile<br />
              [CMAKE_FLAGS &lt;Flags&gt;]<br />
              [COMPILE_DEFINITIONS &lt;flags&gt; &#8230;]<br />
              [OUTPUT_VARIABLE var]<br />
              [COPY_FILE &lt;filename&gt; )</p>
<p> Try compiling a srcfile. In this case, the user need only supply a source file. CMake will create the appropriate CMakeLists.txt file to build the source. If COPY_FILE is used, the compiled file will be copied to the given file. </p>
<p> In this version all files in bindir/CMakeFiles/CMakeTmp, will be cleaned automatically, for debugging a &#8211;debug-trycompile can be passed to cmake to avoid the clean. Some extra flags that can be included are, INCLUDE_DIRECTORIES, LINK_DIRECTORIES, and LINK_LIBRARIES. COMPILE_DEFINITIONS are -Ddefinition that will be passed to the compile line. try_compile creates a CMakeList.txt file on the fly that looks like this: </p>
<p>add_definitions(&lt;expanded COMPILE_DEFINITIONS from calling cmake&gt;)<br />
    include_directories(${INCLUDE_DIRECTORIES})<br />
        link_directories(${LINK_DIRECTORIES})<br />
            add_executable(cmTryCompileExec sources)<br />
                target_link_libraries(cmTryCompileExec ${LINK_LIBRARIES})</p>
<p> In both versions of the command, if OUTPUT_VARIABLE is specified, then the output from the build process is stored in the given variable. Return the success or failure in RESULT_VAR. CMAKE_FLAGS can be used to pass -DVAR:TYPE=VALUE flags to the cmake that is run during the build. </p>
<dt><code>try_run</code></p>
<dd> Try compiling and then running some code. </p>
<p>try_run(RUN_RESULT_VAR COMPILE_RESULT_VAR<br />
            bindir srcfile[CMAKE_FLAGS&lt;Flags&gt;]<br />
                          [COMPILE_DEFINITIONS&lt;flags&gt;]<br />
                          [COMPILE_OUTPUT_VARIABLE comp]<br />
                          [RUN_OUTPUT_VARIABLE run]<br />
                          [OUTPUT_VARIABLE var]<br />
                          [ARGS&lt;arg1&gt;&lt;arg2&gt;&#8230;])</p>
<p> Try compiling a srcfile. Return TRUE or FALSE for success or failure in COMPILE_RESULT_VAR. Then if the compile succeeded, run the executable and return its exit code in RUN_RESULT_VAR. If the executable was built, but failed to run, then RUN_RESULT_VAR will be set to FAILED_TO_RUN. COMPILE_OUTPUT_VARIABLE specifies the variable where the output from the compile step goes. RUN_OUTPUT_VARIABLE specifies the variable where the output from the running executable goes. </p>
<p> For compatibility reasons OUTPUT_VARIABLE is still supported, which gives you the output from the compile and run step combined. </p>
<p> Cross compiling issues </p>
<p> When cross compiling, the executable compiled in the first step usually cannot be run on the build host. try_run() checks the CMAKE_CROSSCOMPILING variable to detect whether CMake is in crosscompiling mode. If that&#8217;s the case, it will still try to compile the executable, but it will not try to run the executable. Instead it will create cache variables which must be filled by the user or by presetting them in some CMake script file to the values the executable would have produced if it would have been run on its actual target platform. These variables are RUN_RESULT_VAR (explanation see above) and if RUN_OUTPUT_VARIABLE (or OUTPUT_VARIABLE) was used, an additional cache variable RUN_RESULT_VAR__COMPILE_RESULT_VAR__TRYRUN_OUTPUT.This is intended to hold stdout and stderr from the executable. </p>
<p> In order to make cross compiling your project easier, use try_run only if really required. If you use try_run, use RUN_OUTPUT_VARIABLE (or OUTPUT_VARIABLE) only if really required. Using them will require that when crosscompiling, the cache variables will have to be set manually to the output of the executable. You can also &quot;guard&quot; the calls to try_run with if(CMAKE_CROSSCOMPILING) and provide an easy-to-preset alternative for this case. </p>
<dt><code>unset</code></p>
<dd> Unset a variable, cache variable, or environment variable. </p>
<pre>
  unset(&lt;variable&gt; [CACHE])
</pre>
<p> Removes the specified variable causing it to become undefined. If CACHE is present then the variable is removed from the cache instead of the current scope. </p>
<p> &lt;variable&gt; can be an environment variable such as: </p>
<pre>
  unset(ENV{LD_LIBRARY_PATH})
</pre>
<p> in which case the variable will be removed from the current environment. </p>
<dt><code>variable_watch</code></p>
<dd> Watch the CMake variable for change. </p>
<pre>
  variable_watch(&lt;variable name&gt; [&lt;command to execute&gt;])
</pre>
<p> If the specified variable changes, the message will be printed about the variable being changed. If the command is specified, the command will be executed. The command will receive the following arguments: COMMAND(&lt;variable&gt; &lt;access&gt; &lt;value&gt; &lt;current list file&gt; &lt;stack&gt;) </p>
<dt><code>while</code></p>
<dd> Evaluate a group of commands while a condition is true </p>
<pre>
  while(condition)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
  endwhile(condition)
</pre>
<p> All commands between while and the matching endwhile are recorded without being invoked. Once the endwhile is evaluated, the recorded list of commands is invoked as long as the condition is true. The condition is evaluated using the same logic as the if command. </p>
</dl>
<h2>PROPERTIES</h2>
<pre>
  CMake Properties - Properties supported by CMake, the Cross-Platform Makefile Generator.
</pre>
<p> This is the documentation for the properties supported by CMake. Properties can have different scopes. They can either be assigned to a source file, a directory, a target or globally to CMake. By modifying the values of properties the behaviour of the build system can be customized. </p>
<h2>PROPERTIES OF GLOBAL SCOPE</h2>
<dl>
<dt><code>ALLOW_DUPLICATE_CUSTOM_TARGETS</code></p>
<dd> Allow duplicate custom targets to be created. </p>
<p> Normally CMake requires that all targets built in a project have globally unique logical names (see policy CMP0002). This is necessary to generate meaningful project file names in Xcode and VS IDE generators. It also allows the target names to be referenced unambiguously. </p>
<p> Makefile generators are capable of supporting duplicate custom target names. For projects that care only about Makefile generators and do not wish to support Xcode or VS IDE generators, one may set this property to true to allow duplicate custom targets. The property allows multiple add_custom_target command calls in different directories to specify the same target name. However, setting this property will cause non-Makefile generators to produce an error and refuse to generate the project. </p>
<dt><code>DEBUG_CONFIGURATIONS</code></p>
<dd> Specify which configurations are for debugging. </p>
<p> The value must be a semi-colon separated list of configuration names. Currently this property is used only by the target_link_libraries command (see its documentation for details). Additional uses may be defined in the future. </p>
<p> This property must be set at the top level of the project and before the first target_link_libraries command invocation. If any entry in the list does not match a valid configuration for the project the behavior is undefined. </p>
<dt><code>DISABLED_FEATURES</code></p>
<dd> List of features which are disabled during the CMake run. </p>
<p> List of features which are disabled during the CMake run. Be default it contains the names of all packages which were not found. This is determined using the &lt;NAME&gt;_FOUND variables. Packages which are searched QUIET are not listed. A project can add its own features to this list.This property is used by the macros in FeatureSummary.cmake. </p>
<dt><code>ENABLED_FEATURES</code></p>
<dd> List of features which are enabled during the CMake run. </p>
<p> List of features which are enabled during the CMake run. Be default it contains the names of all packages which were found. This is determined using the &lt;NAME&gt;_FOUND variables. Packages which are searched QUIET are not listed. A project can add its own features to this list.This property is used by the macros in FeatureSummary.cmake. </p>
<dt><code>ENABLED_LANGUAGES</code></p>
<dd> Read-only property that contains the list of currently enabled languages </p>
<p> Set to list of currently enabled lanauges. </p>
<dt><code>FIND_LIBRARY_USE_LIB64_PATHS</code></p>
<dd> Whether FIND_LIBRARY should automatically search lib64 directories. </p>
<p> FIND_LIBRARY_USE_LIB64_PATHS is a boolean specifying whether the FIND_LIBRARY command should automatically search the lib64 variant of directories called lib in the search path when building 64-bit binaries. </p>
<dt><code>GLOBAL_DEPENDS_DEBUG_MODE</code></p>
<dd> Enable global target dependency graph debug mode. </p>
<p> CMake automatically analyzes the global inter-target dependency graph at the beginning of native build system generation. This property causes it to display details of its analysis to stderr. </p>
<dt><code>IN_TRY_COMPILE</code></p>
<dd> Read-only property that is true during a try-compile configuration. </p>
<p> True when building a project inside a TRY_COMPILE or TRY_RUN command. </p>
<dt><code>PACKAGES_FOUND</code></p>
<dd> List of packages which were found during the CMake run. </p>
<p> List of packages which were found during the CMake run. Whether a package has been found is determined using the &lt;NAME&gt;_FOUND variables. </p>
<dt><code>PACKAGES_NOT_FOUND</code></p>
<dd> List of packages which were not found during the CMake run. </p>
<p> List of packages which were not found during the CMake run. Whether a package has been found is determined using the &lt;NAME&gt;_FOUND variables. </p>
<dt><code>REPORT_UNDEFINED_PROPERTIES</code></p>
<dd> If set, report any undefined properties to this file. </p>
<p> If this property is set to a filename then when CMake runs it will report any properties or variables that were accessed but not defined into the filename specified in this property. </p>
<dt><code>TARGET_ARCHIVES_MAY_BE_SHARED_LIBS</code></p>
<dd> Set if shared libraries may be named like archives. </p>
<p> On AIX shared libraries may be named &quot;lib&lt;name&gt;.a&quot;. This property is set to true on such platforms. </p>
<dt><code>TARGET_SUPPORTS_SHARED_LIBS</code></p>
<dd> Does the target platform support shared libraries. </p>
<p> TARGET_SUPPORTS_SHARED_LIBS is a boolean specifying whether the target platform supports shared libraries. Basically all current general general purpose OS do so, the exception are usually embedded systems with no or special OSs. </p>
<dt><code>__CMAKE_DELETE_CACHE_CHANGE_VARS_</code></p>
<dd> Internal property </p>
<p> Used to detect compiler changes, Do not set. </p>
</dl>
<h2>PROPERTIES ON DIRECTORIES</h2>
<dl>
<dt><code>ADDITIONAL_MAKE_CLEAN_FILES</code></p>
<dd> Additional files to clean during the make clean stage. </p>
<p> A list of files that will be cleaned as a part of the &quot;make clean&quot; stage. </p>
<dt><code>CACHE_VARIABLES</code></p>
<dd> List of cache variables available in the current directory. </p>
<p> This read-only property specifies the list of CMake cache variables currently defined. It is intended for debugging purposes. </p>
<dt><code>CLEAN_NO_CUSTOM</code></p>
<dd> Should the output of custom commands be left. </p>
<p> If this is true then the outputs of custom commands for this directory will not be removed during the &quot;make clean&quot; stage. </p>
<dt><code>COMPILE_DEFINITIONS</code></p>
<dd> Preprocessor definitions for compiling a directory&#8217;s sources. </p>
<p> The COMPILE_DEFINITIONS property may be set to a list of preprocessor definitions using the syntax VAR or VAR=value. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). This property may be set on a per-configuration basis using the name COMPILE_DEFINITIONS_&lt;CONFIG&gt; where &lt;CONFIG&gt; is an upper-case name (ex. &quot;COMPILE_DEFINITIONS_DEBUG&quot;). This property will be initialized in each directory by its value in the directory&#8217;s parent. </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. The VS6 IDE does not support definition values with spaces (but NMake does). </p>
<p> Dislaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. </p>
<dt><code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration preprocessor definitions in a directory. </p>
<p> This is the configuration-specific version of COMPILE_DEFINITIONS. This property will be initialized in each directory by its value in the directory&#8217;s parent. </p>
<dt><code>DEFINITIONS</code></p>
<dd> For CMake 2.4 compatibility only. Use COMPILE_DEFINITIONS instead. </p>
<p> This read-only property specifies the list of flags given so far to the add_definitions command. It is intended for debugging purposes. Use the COMPILE_DEFINITIONS instead. </p>
<dt><code>EXCLUDE_FROM_ALL</code></p>
<dd> Exclude the directory from the all target of its parent. </p>
<p> A property on a directory that indicates if its targets are excluded from the default build target. If it is not, then with a Makefile for example typing make will cause the targets to be built. The same concept applies to the default build of other generators. </p>
<dt><code>IMPLICIT_DEPENDS_INCLUDE_TRANSFORM</code></p>
<dd> Specify #include line transforms for dependencies in a directory. </p>
<p> This property specifies rules to transform macro-like #include lines during implicit dependency scanning of C and C++ source files. The list of rules must be semicolon-separated with each entry of the form &quot;A_MACRO(%)=value-with-%&quot; (the % must be literal). During dependency scanning occurrences of A_MACRO(&#8230;) on #include lines will be replaced by the value given with the macro argument substituted for &#8216;%&#8217;. For example, the entry </p>
<pre>
  MYDIR(%)=&lt;mydir/%&gt;
</pre>
<p> will convert lines of the form </p>
<p>#include MYDIR(myheader.h)</p>
<p> to </p>
<p>#include &lt;mydir/myheader.h&gt;</p>
<p> allowing the dependency to be followed. </p>
<p> This property applies to sources in all targets within a directory. The property value is initialized in each directory by its value in the directory&#8217;s parent. </p>
<dt><code>INCLUDE_DIRECTORIES</code></p>
<dd> List of preprocessor include file search directories. </p>
<p> This read-only property specifies the list of directories given so far to the include_directories command. It is intended for debugging purposes. </p>
<dt><code>INCLUDE_REGULAR_EXPRESSION</code></p>
<dd> Include file scanning regular expression. </p>
<p> This read-only property specifies the regular expression used during dependency scanning to match include files that should be followed. See the include_regular_expression command. </p>
<dt><code>LINK_DIRECTORIES</code></p>
<dd> List of linker search directories. </p>
<p> This read-only property specifies the list of directories given so far to the link_directories command. It is intended for debugging purposes. </p>
<dt><code>LISTFILE_STACK</code></p>
<dd> The current stack of listfiles being processed. </p>
<p> This property is mainly useful when trying to debug errors in your CMake scripts. It returns a list of what list files are currently being processed, in order. So if one listfile does an INCLUDE command then that is effectively pushing the included listfile onto the stack. </p>
<dt><code>MACROS</code></p>
<dd> List of macro commands available in the current directory. </p>
<p> This read-only property specifies the list of CMake macros currently defined. It is intended for debugging purposes. See the macro command. </p>
<dt><code>PARENT_DIRECTORY</code></p>
<dd> Source directory that added current subdirectory. </p>
<p> This read-only property specifies the source directory that added the current source directory as a subdirectory of the build. In the top-level directory the value is the empty-string. </p>
<dt><code>TEST_INCLUDE_FILE</code></p>
<dd> A cmake file that will be included when ctest is run. </p>
<p> If you specify TEST_INCLUDE_FILE, that file will be included and processed when ctest is run on the directory. </p>
<dt><code>VARIABLES</code></p>
<dd> List of variables defined in the current directory. </p>
<p> This read-only property specifies the list of CMake variables currently defined. It is intended for debugging purposes. </p>
</dl>
<h2>PROPERTIES ON TARGETS</h2>
<dl>
<dt><code>&lt;CONFIG&gt;_POSTFIX</code></p>
<dd> Postfix to append to the target file name for configuration &lt;CONFIG&gt;. </p>
<p> When building with configuration &lt;CONFIG&gt; the value of this property is appended to the target file name built on disk. For non-executable targets, this property is initialized by the value of the variable CMAKE_&lt;CONFIG&gt;_POSTFIX if it is set when a target is created. This property is ignored on the Mac for Frameworks and App Bundles. </p>
<dt><code>ARCHIVE_OUTPUT_DIRECTORY</code></p>
<dd> Output directory in which to build ARCHIVE target files. </p>
<p> This property specifies the directory into which archive target files should be built. There are three kinds of target files that may be built: archive, library, and runtime. Executables are always treated as runtime targets. Static libraries are always treated as archive targets. Module libraries are always treated as library targets. For non-DLL platforms shared libraries are treated as library targets. For DLL platforms the DLL part of a shared library is treated as a runtime target and the corresponding import library is treated as an archive target. All Windows-based systems including Cygwin are DLL platforms. This property is initialized by the value of the variable CMAKE_ARCHIVE_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<dt><code>BUILD_WITH_INSTALL_RPATH</code></p>
<dd> Should build tree targets have install tree rpaths. </p>
<p> BUILD_WITH_INSTALL_RPATH is a boolean specifying whether to link the target in the build tree with the INSTALL_RPATH. This takes precedence over SKIP_BUILD_RPATH and avoids the need for relinking before installation. This property is initialized by the value of the variable CMAKE_BUILD_WITH_INSTALL_RPATH if it is set when a target is created. </p>
<dt><code>CLEAN_DIRECT_OUTPUT</code></p>
<dd> Do not delete other variants of this target. </p>
<p> When a library is built CMake by default generates code to remove any existing library using all possible names. This is needed to support libraries that switch between STATIC and SHARED by a user option. However when using OUTPUT_NAME to build a static and shared library of the same name using different logical target names the two targets will remove each other&#8217;s files. This can be prevented by setting the CLEAN_DIRECT_OUTPUT property to 1. </p>
<dt><code>COMPILE_DEFINITIONS</code></p>
<dd> Preprocessor definitions for compiling a target&#8217;s sources. </p>
<p> The COMPILE_DEFINITIONS property may be set to a list of preprocessor definitions using the syntax VAR or VAR=value. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). This property may be set on a per-configuration basis using the name COMPILE_DEFINITIONS_&lt;CONFIG&gt; where &lt;CONFIG&gt; is an upper-case name (ex. &quot;COMPILE_DEFINITIONS_DEBUG&quot;). </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. The VS6 IDE does not support definition values with spaces (but NMake does). </p>
<p> Dislaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. </p>
<dt><code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration preprocessor definitions on a target. </p>
<p> This is the configuration-specific version of COMPILE_DEFINITIONS. </p>
<dt><code>COMPILE_FLAGS</code></p>
<dd> Additional flags to use when compiling this target&#8217;s sources. </p>
<p> The COMPILE_FLAGS property sets additional compiler flags used to build sources within the target. Use COMPILE_DEFINITIONS to pass additional preprocessor definitions. </p>
<dt><code>DEBUG_POSTFIX</code></p>
<dd> See target property &lt;CONFIG&gt;_POSTFIX. </p>
<p> This property is a special case of the more-general &lt;CONFIG&gt;_POSTFIX property for the DEBUG configuration. </p>
<dt><code>DEFINE_SYMBOL</code></p>
<dd> Define a symbol when compiling this target&#8217;s sources. </p>
<p> DEFINE_SYMBOL sets the name of the preprocessor symbol defined when compiling sources in a shared library. If not set here then it is set to target_EXPORTS by default (with some substitutions if the target is not a valid C identifier). This is useful for headers to know whether they are being included from inside their library our outside to properly setup dllexport/dllimport decorations. </p>
<dt><code>ENABLE_EXPORTS</code></p>
<dd> Specify whether an executable exports symbols for loadable modules. </p>
<p> Normally an executable does not export any symbols because it is the final program. It is possible for an executable to export symbols to be used by loadable modules. When this property is set to true CMake will allow other targets to &quot;link&quot; to the executable with the TARGET_LINK_LIBRARIES command. On all platforms a target-level dependency on the executable is created for targets that link to it. For non-DLL platforms the link rule is simply ignored since the dynamic loader will automatically bind symbols when the module is loaded. For DLL platforms an import library will be created for the exported symbols and then used for linking. All Windows-based systems including Cygwin are DLL platforms. </p>
<dt><code>EXCLUDE_FROM_ALL</code></p>
<dd> Exclude the target from the all target. </p>
<p> A property on a target that indicates if the target is excluded from the default build target. If it is not, then with a Makefile for example typing make will cause this target to be built. The same concept applies to the default build of other generators. Installing a target with EXCLUDE_FROM_ALL set to true has undefined behavior. </p>
<dt><code>EchoString</code></p>
<dd> A message to be displayed when the target is built. </p>
<p> A message to display on some generators (such as makefiles) when the target is built. </p>
<dt><code>FRAMEWORK</code></p>
<dd> This target is a framework on the Mac. </p>
<p> If a shared library target has this property set to true it will be built as a framework when built on the mac. It will have the directory structure required for a framework and will be suitable to be used with the -framework option </p>
<dt><code>Fortran_MODULE_DIRECTORY</code></p>
<dd> Specify output directory for Fortran modules provided by the target. </p>
<p> If the target contains Fortran source files that provide modules and the compiler supports a module output directory this specifies the directory in which the modules will be placed. When this property is not set the modules will be placed in the build directory corresponding to the target&#8217;s source directory. If the variable CMAKE_Fortran_MODULE_DIRECTORY is set when a target is created its value is used to initialize this property. </p>
<dt><code>GENERATOR_FILE_NAME</code></p>
<dd> Generator&#8217;s file for this target. </p>
<p> An internal property used by some generators to record the name of project or dsp file associated with this target. </p>
<dt><code>HAS_CXX</code></p>
<dd> Force a target to use the CXX linker. </p>
<p> Setting HAS_CXX on a target will force the target to use the C++ linker (and C++ runtime libraries) for linking even if the target has no C++ code in it. </p>
<dt><code>IMPLICIT_DEPENDS_INCLUDE_TRANSFORM</code></p>
<dd> Specify #include line transforms for dependencies in a target. </p>
<p> This property specifies rules to transform macro-like #include lines during implicit dependency scanning of C and C++ source files. The list of rules must be semicolon-separated with each entry of the form &quot;A_MACRO(%)=value-with-%&quot; (the % must be literal). During dependency scanning occurrences of A_MACRO(&#8230;) on #include lines will be replaced by the value given with the macro argument substituted for &#8216;%&#8217;. For example, the entry </p>
<pre>
  MYDIR(%)=&lt;mydir/%&gt;
</pre>
<p> will convert lines of the form </p>
<p>#include MYDIR(myheader.h)</p>
<p> to </p>
<p>#include &lt;mydir/myheader.h&gt;</p>
<p> allowing the dependency to be followed. </p>
<p> This property applies to sources in the target on which it is set. </p>
<dt><code>IMPORTED</code></p>
<dd> Read-only indication of whether a target is IMPORTED. </p>
<p> The boolean value of this property is true for targets created with the IMPORTED option to add_executable or add_library. It is false for targets built within the project. </p>
<dt><code>IMPORTED_CONFIGURATIONS</code></p>
<dd> Configurations provided for an IMPORTED target. </p>
<p> Lists configuration names available for an IMPORTED target. The names correspond to configurations defined in the project from which the target is imported. If the importing project uses a different set of configurations the names may be mapped using the MAP_IMPORTED_CONFIG_&lt;CONFIG&gt; property. Ignored for non-imported targets. </p>
<dt><code>IMPORTED_IMPLIB</code></p>
<dd> Full path to the import library for an IMPORTED target. </p>
<p> Specifies the location of the &quot;.lib&quot; part of a windows DLL. Ignored for non-imported targets. </p>
<dt><code>IMPORTED_IMPLIB_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration version of IMPORTED_IMPLIB property. </p>
<p> This property is used when loading settings for the &lt;CONFIG&gt; configuration of an imported target. Configuration names correspond to those provided by the project from which the target is imported. </p>
<dt><code>IMPORTED_LINK_DEPENDENT_LIBRARIES</code></p>
<dd> Dependent shared libraries of an imported shared library. </p>
<p> Shared libraries may be linked to other shared libraries as part of their implementation. On some platforms the linker searches for the dependent libraries of shared libraries they are including in the link. This property lists the dependent shared libraries of an imported library. The list should be disjoint from the list of interface libraries in the IMPORTED_LINK_INTERFACE_LIBRARIES property. On platforms requiring dependent shared libraries to be found at link time CMake uses this list to add appropriate files or paths to the link command line. Ignored for non-imported targets. </p>
<dt><code>IMPORTED_LINK_DEPENDENT_LIBRARIES_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration version of IMPORTED_LINK_DEPENDENT_LIBRARIES. </p>
<p> This property is used when loading settings for the &lt;CONFIG&gt; configuration of an imported target. Configuration names correspond to those provided by the project from which the target is imported. If set, this property completely overrides the generic property for the named configuration. </p>
<dt><code>IMPORTED_LINK_INTERFACE_LIBRARIES</code></p>
<dd> Transitive link interface of an IMPORTED target. </p>
<p> Lists libraries whose interface is included when an IMPORTED library target is linked to another target. The libraries will be included on the link line for the target. Unlike the LINK_INTERFACE_LIBRARIES property, this property applies to all imported target types, including STATIC libraries. This property is ignored for non-imported targets. </p>
<dt><code>IMPORTED_LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration version of IMPORTED_LINK_INTERFACE_LIBRARIES. </p>
<p> This property is used when loading settings for the &lt;CONFIG&gt; configuration of an imported target. Configuration names correspond to those provided by the project from which the target is imported. If set, this property completely overrides the generic property for the named configuration. </p>
<dt><code>IMPORTED_LOCATION</code></p>
<dd> Full path to the main file on disk for an IMPORTED target. </p>
<p> Specifies the location of an IMPORTED target file on disk. For executables this is the location of the executable file. For bundles on OS X this is the location of the executable file inside Contents/MacOS under the application bundle folder. For static libraries and modules this is the location of the library or module. For shared libraries on non-DLL platforms this is the location of the shared library. For frameworks on OS X this is the location of the library file symlink just inside the framework folder. For DLLs this is the location of the &quot;.dll&quot; part of the library. For UNKNOWN libraries this is the location of the file to be linked. Ignored for non-imported targets. </p>
<dt><code>IMPORTED_LOCATION_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration version of IMPORTED_LOCATION property. </p>
<p> This property is used when loading settings for the &lt;CONFIG&gt; configuration of an imported target. Configuration names correspond to those provided by the project from which the target is imported. </p>
<dt><code>IMPORTED_SONAME</code></p>
<dd> The &quot;soname&quot; of an IMPORTED target of shared library type. </p>
<p> Specifies the &quot;soname&quot; embedded in an imported shared library. This is meaningful only on platforms supporting the feature. Ignored for non-imported targets. </p>
<dt><code>IMPORTED_SONAME_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration version of IMPORTED_SONAME property. </p>
<p> This property is used when loading settings for the &lt;CONFIG&gt; configuration of an imported target. Configuration names correspond to those provided by the project from which the target is imported. </p>
<dt><code>IMPORT_PREFIX</code></p>
<dd> What comes before the import library name. </p>
<p> Similar to the target property PREFIX, but used for import libraries (typically corresponding to a DLL) instead of regular libraries. A target property that can be set to override the prefix (such as &quot;lib&quot;) on an import library name. </p>
<dt><code>IMPORT_SUFFIX</code></p>
<dd> What comes after the import library name. </p>
<p> Similar to the target property SUFFIX, but used for import libraries (typically corresponding to a DLL) instead of regular libraries. A target property that can be set to override the suffix (such as &quot;.lib&quot;) on an import library name. </p>
<dt><code>INSTALL_NAME_DIR</code></p>
<dd> Mac OSX directory name for installed targets. </p>
<p> INSTALL_NAME_DIR is a string specifying the directory portion of the &quot;install_name&quot; field of shared libraries on Mac OSX to use in the installed targets. </p>
<dt><code>INSTALL_RPATH</code></p>
<dd> The rpath to use for installed targets. </p>
<p> A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This property is initialized by the value of the variable CMAKE_INSTALL_RPATH if it is set when a target is created. </p>
<dt><code>INSTALL_RPATH_USE_LINK_PATH</code></p>
<dd> Add paths to linker search and installed rpath. </p>
<p> INSTALL_RPATH_USE_LINK_PATH is a boolean that if set to true will append directories in the linker search path and outside the project to the INSTALL_RPATH. This property is initialized by the value of the variable CMAKE_INSTALL_RPATH_USE_LINK_PATH if it is set when a target is created. </p>
<dt><code>LIBRARY_OUTPUT_DIRECTORY</code></p>
<dd> Output directory in which to build LIBRARY target files. </p>
<p> This property specifies the directory into which library target files should be built. There are three kinds of target files that may be built: archive, library, and runtime. Executables are always treated as runtime targets. Static libraries are always treated as archive targets. Module libraries are always treated as library targets. For non-DLL platforms shared libraries are treated as library targets. For DLL platforms the DLL part of a shared library is treated as a runtime target and the corresponding import library is treated as an archive target. All Windows-based systems including Cygwin are DLL platforms. This property is initialized by the value of the variable CMAKE_LIBRARY_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<dt><code>LINKER_LANGUAGE</code></p>
<dd> What tool to use for linking, based on language. </p>
<p> The LINKER_LANGUAGE property is used to change the tool used to link an executable or shared library. The default is set the language to match the files in the library. CXX and C are common values for this property. </p>
<dt><code>LINK_FLAGS</code></p>
<dd> Additional flags to use when linking this target. </p>
<p> The LINK_FLAGS property can be used to add extra flags to the link step of a target. LINK_FLAGS_&lt;CONFIG&gt; will add to the configuration &lt;CONFIG&gt;, for example, DEBUG, RELEASE, MINSIZEREL, RELWITHDEBINFO. </p>
<dt><code>LINK_FLAGS_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration linker flags for a target. </p>
<p> This is the configuration-specific version of LINK_FLAGS. </p>
<dt><code>LINK_INTERFACE_LIBRARIES</code></p>
<dd> List public interface libraries for a shared library or executable. </p>
<p> By default linking to a shared library target transitively links to targets with which the library itself was linked. For an executable with exports (see the ENABLE_EXPORTS property) no default transitive link dependencies are used. This property replaces the default transitive link dependencies with an explict list. When the target is linked into another target the libraries listed (and recursively their link interface libraries) will be provided to the other target also. If the list is empty then no transitive link dependencies will be incorporated when this target is linked into another target even if the default set is non-empty. This property is ignored for STATIC libraries. </p>
<dt><code>LINK_INTERFACE_LIBRARIES_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration list of public interface libraries for a target. </p>
<p> This is the configuration-specific version of LINK_INTERFACE_LIBRARIES. If set, this property completely overrides the generic property for the named configuration. </p>
<dt><code>LINK_SEARCH_END_STATIC</code></p>
<dd> End a link line such that static system libraries are used. </p>
<p> Some linkers support switches such as -Bstatic and -Bdynamic to determine whether to use static or shared libraries for -lXXX options. CMake uses these options to set the link type for libraries whose full paths are not known or (in some cases) are in implicit link directories for the platform. By default the linker search type is left at -Bdynamic by the end of the library list. This property switches the final linker search type to -Bstatic. </p>
<dt><code>LOCATION</code></p>
<dd> Read-only location of a target on disk. </p>
<p> For an imported target, this read-only property returns the value of the LOCATION_&lt;CONFIG&gt; property for an unspecified configuration &lt;CONFIG&gt; provided by the target. </p>
<p> For a non-imported target, this property is provided for compatibility with CMake 2.4 and below. It was meant to get the location of an executable target&#8217;s output file for use in add_custom_command. The path may contain a build-system-specific portion that is replaced at build time with the configuration getting built (such as &quot;$(ConfigurationName)&quot; in VS). In CMake 2.6 and above add_custom_command automatically recognizes a target name in its COMMAND and DEPENDS options and computes the target location. Therefore this property is not needed for creating custom commands. </p>
<dt><code>LOCATION_&lt;CONFIG&gt;</code></p>
<dd> Read-only property providing a target location on disk. </p>
<p> A read-only property that indicates where a target&#8217;s main file is located on disk for the configuration &lt;CONFIG&gt;. The property is defined only for library and executable targets. An imported target may provide a set of configurations different from that of the importing project. By default CMake looks for an exact-match but otherwise uses an arbitrary available configuration. Use the MAP_IMPORTED_CONFIG_&lt;CONFIG&gt; property to map imported configurations explicitly. </p>
<dt><code>MACOSX_BUNDLE</code></p>
<dd> Build an executable as an application bundle on Mac OS X. </p>
<p> When this property is set to true the executable when built on Mac OS X will be created as an application bundle. This makes it a GUI executable that can be launched from the Finder. See the MACOSX_BUNDLE_INFO_PLIST target property for information about creation of the Info.plist file for the application bundle. </p>
<dt><code>MACOSX_BUNDLE_INFO_PLIST</code></p>
<dd> Specify a custom Info.plist template for a Mac OS X App Bundle. </p>
<p> An executable target with MACOSX_BUNDLE enabled will be built as an application bundle on Mac OS X. By default its Info.plist file is created by configuring a template called MacOSXBundleInfo.plist.in located in the CMAKE_MODULE_PATH. This property specifies an alternative template file name which may be a full path. </p>
<p> The following target properties may be set to specify content to be configured into the file: </p>
<pre>
  MACOSX_BUNDLE_INFO_STRING
  MACOSX_BUNDLE_ICON_FILE
  MACOSX_BUNDLE_GUI_IDENTIFIER
  MACOSX_BUNDLE_LONG_VERSION_STRING
  MACOSX_BUNDLE_BUNDLE_NAME
  MACOSX_BUNDLE_SHORT_VERSION_STRING
  MACOSX_BUNDLE_BUNDLE_VERSION
  MACOSX_BUNDLE_COPYRIGHT
</pre>
<p> CMake variables of the same name may be set to affect all targets in a directory that do not have each specific property set. If a custom Info.plist is specified by this property it may of course hard-code all the settings instead of using the target properties. </p>
<dt><code>MACOSX_FRAMEWORK_INFO_PLIST</code></p>
<dd> Specify a custom Info.plist template for a Mac OS X Framework. </p>
<p> An library target with FRAMEWORK enabled will be built as a framework on Mac OS X. By default its Info.plist file is created by configuring a template called MacOSXFrameworkInfo.plist.in located in the CMAKE_MODULE_PATH. This property specifies an alternative template file name which may be a full path. </p>
<p> The following target properties may be set to specify content to be configured into the file: </p>
<pre>
  MACOSX_FRAMEWORK_ICON_FILE
  MACOSX_FRAMEWORK_IDENTIFIER
  MACOSX_FRAMEWORK_SHORT_VERSION_STRING
  MACOSX_FRAMEWORK_BUNDLE_VERSION
</pre>
<p> CMake variables of the same name may be set to affect all targets in a directory that do not have each specific property set. If a custom Info.plist is specified by this property it may of course hard-code all the settings instead of using the target properties. </p>
<dt><code>MAP_IMPORTED_CONFIG_&lt;CONFIG&gt;</code></p>
<dd> Map from project configuration to IMPORTED target&#8217;s configuration. </p>
<p> List configurations of an imported target that may be used for the current project&#8217;s &lt;CONFIG&gt; configuration. Targets imported from another project may not provide the same set of configuration names available in the current project. Setting this property tells CMake what imported configurations are suitable for use when building the &lt;CONFIG&gt; configuration. The first configuration in the list found to be provided by the imported target is selected. If no matching configurations are available the imported target is considered to be not found. This property is ignored for non-imported targets. </p>
<dt><code>OUTPUT_NAME</code></p>
<dd> Sets the real name of a target when it is built. </p>
<p> Sets the real name of a target when it is built and can be used to help create two targets of the same name even though CMake requires unique logical target names. There is also a &lt;CONFIG&gt;_OUTPUT_NAME that can set the output name on a per-configuration basis. </p>
<dt><code>POST_INSTALL_SCRIPT</code></p>
<dd> Deprecated install support. </p>
<p> The PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT properties are the old way to specify CMake scripts to run before and after installing a target. They are used only when the old INSTALL_TARGETS command is used to install the target. Use the INSTALL command instead. </p>
<dt><code>PREFIX</code></p>
<dd> What comes before the library name. </p>
<p> A target property that can be set to override the prefix (such as &quot;lib&quot;) on a library name. </p>
<dt><code>PRE_INSTALL_SCRIPT</code></p>
<dd> Deprecated install support. </p>
<p> The PRE_INSTALL_SCRIPT and POST_INSTALL_SCRIPT properties are the old way to specify CMake scripts to run before and after installing a target. They are used only when the old INSTALL_TARGETS command is used to install the target. Use the INSTALL command instead. </p>
<dt><code>PRIVATE_HEADER</code></p>
<dd> Specify private header files in a FRAMEWORK shared library target. </p>
<p> Shared library targets marked with the FRAMEWORK property generate frameworks on OS X and normal shared libraries on other platforms. This property may be set to a list of header files to be placed in the PrivateHeaders directory inside the framework folder. On non-Apple platforms these headers may be installed using the PRIVATE_HEADER option to the install(TARGETS) command. </p>
<dt><code>PROJECT_LABEL</code></p>
<dd> Change the name of a target in an IDE. </p>
<p> Can be used to change the name of the target in an IDE like visual stuido. </p>
<dt><code>PUBLIC_HEADER</code></p>
<dd> Specify public header files in a FRAMEWORK shared library target. </p>
<p> Shared library targets marked with the FRAMEWORK property generate frameworks on OS X and normal shared libraries on other platforms. This property may be set to a list of header files to be placed in the Headers directory inside the framework folder. On non-Apple platforms these headers may be installed using the PUBLIC_HEADER option to the install(TARGETS) command. </p>
<dt><code>RESOURCE</code></p>
<dd> Specify resource files in a FRAMEWORK shared library target. </p>
<p> Shared library targets marked with the FRAMEWORK property generate frameworks on OS X and normal shared libraries on other platforms. This property may be set to a list of files to be placed in the Resources directory inside the framework folder. On non-Apple platforms these files may be installed using the RESOURCE option to the install(TARGETS) command. </p>
<dt><code>RUNTIME_OUTPUT_DIRECTORY</code></p>
<dd> Output directory in which to build RUNTIME target files. </p>
<p> This property specifies the directory into which runtime target files should be built. There are three kinds of target files that may be built: archive, library, and runtime. Executables are always treated as runtime targets. Static libraries are always treated as archive targets. Module libraries are always treated as library targets. For non-DLL platforms shared libraries are treated as library targets. For DLL platforms the DLL part of a shared library is treated as a runtime target and the corresponding import library is treated as an archive target. All Windows-based systems including Cygwin are DLL platforms. This property is initialized by the value of the variable CMAKE_RUNTIME_OUTPUT_DIRECTORY if it is set when a target is created. </p>
<dt><code>SKIP_BUILD_RPATH</code></p>
<dd> Should rpaths be used for the build tree. </p>
<p> SKIP_BUILD_RPATH is a boolean specifying whether to skip automatic generation of an rpath allowing the target to run from the build tree. This property is initialized by the value of the variable CMAKE_SKIP_BUILD_RPATH if it is set when a target is created. </p>
<dt><code>SOURCES</code></p>
<dd> Source names specified for a target. </p>
<p> Read-only list of sources specified for a target. The names returned are suitable for passing to the set_source_files_properties command. </p>
<dt><code>SOVERSION</code></p>
<dd> What version number is this target. </p>
<p> For shared libraries VERSION and SOVERSION can be used to specify the build version and api version respectively. When building or installing appropriate symlinks are created if the platform supports symlinks and the linker supports so-names. If only one of both is specified the missing is assumed to have the same version number. For shared libraries and executables on Windows the VERSION attribute is parsed to extract a &quot;major.minor&quot; version number. These numbers are used as the image version of the binary. </p>
<dt><code>STATIC_LIBRARY_FLAGS</code></p>
<dd> Extra flags to use when linking static libraries. </p>
<p> Extra flags to use when linking a static library. </p>
<dt><code>SUFFIX</code></p>
<dd> What comes after the library name. </p>
<p> A target property that can be set to override the suffix (such as &quot;.so&quot;) on a library name. </p>
<dt><code>TYPE</code></p>
<dd> The type of the target. </p>
<p> This read-only property can be used to test the type of the given target. It will be one of STATIC_LIBRARY, MODULE_LIBRARY, SHARED_LIBRARY, EXECUTABLE or one of the internal target types. </p>
<dt><code>VERSION</code></p>
<dd> What version number is this target. </p>
<p> For shared libraries VERSION and SOVERSION can be used to specify the build version and api version respectively. When building or installing appropriate symlinks are created if the platform supports symlinks and the linker supports so-names. If only one of both is specified the missing is assumed to have the same version number. For executables VERSION can be used to specify the build version. When building or installing appropriate symlinks are created if the platform supports symlinks. For shared libraries and executables on Windows the VERSION attribute is parsed to extract a &quot;major.minor&quot; version number. These numbers are used as the image version of the binary. </p>
<dt><code>VS_KEYWORD</code></p>
<dd> Visual Studio project keyword. </p>
<p> Can be set to change the visual studio keyword, for example QT integration works better if this is set to Qt4VSv1.0. </p>
<dt><code>VS_SCC_LOCALPATH</code></p>
<dd> Visual Studio Source Code Control Provider. </p>
<p> Can be set to change the visual studio source code control local path property. </p>
<dt><code>VS_SCC_PROJECTNAME</code></p>
<dd> Visual Studio Source Code Control Project. </p>
<p> Can be set to change the visual studio source code control project name property. </p>
<dt><code>VS_SCC_PROVIDER</code></p>
<dd> Visual Studio Source Code Control Provider. </p>
<p> Can be set to change the visual studio source code control provider property. </p>
<dt><code>WIN32_EXECUTABLE</code></p>
<dd> Build an executable with a WinMain entry point on windows. </p>
<p> When this property is set to true the executable when linked on Windows will be created with a WinMain() entry point instead of of just main().This makes it a GUI executable instead of a console application. See the CMAKE_MFC_FLAG variable documentation to configure use of MFC for WinMain executables. </p>
<dt><code>XCODE_ATTRIBUTE_&lt;an-attribute&gt;</code></p>
<dd> Set Xcode target attributes directly. </p>
<p> Tell the Xcode generator to set &#8216;&lt;an-attribute&gt;&#8217; to a given value in the generated Xcode project. Ignored on other generators. </p>
</dl>
<h2>PROPERTIES ON TESTS</h2>
<dl>
<dt><code>FAIL_REGULAR_EXPRESSION</code></p>
<dd> If the output matches this regular expression the test will fail. </p>
<p> If set, if the output matches one of specified regular expressions, the test will fail.For example: PASS_REGULAR_EXPRESSION &quot;[^a-z]Error;ERROR;Failed&quot; </p>
<dt><code>MEASUREMENT</code></p>
<dd> Specify a DART measurement and value to be reported for a test. </p>
<p> If set to a name then that name will be reported to DART as a named measurement with a value of 1. You may also specify a value by setting MEASUREMENT to &quot;measurement=value&quot;. </p>
<dt><code>PASS_REGULAR_EXPRESSION</code></p>
<dd> The output must match this regular expression for the test to pass. </p>
<p> If set, the test output will be checked against the specified regular expressions and at least one of the regular expressions has to match, otherwise the test will fail. </p>
<dt><code>TIMEOUT</code></p>
<dd> How many seconds to allow for this test. </p>
<p> This property if set will limit a test to not take more than the specified number of seconds to run. If it exceeds that the test process will be killed and ctest will move to the next test. This setting takes precedence over DART_TESTING_TIMEOUT and CTEST_TESTING_TIMEOUT. </p>
<dt><code>WILL_FAIL</code></p>
<dd> If set to true, this will invert the pass/fail flag of the test. </p>
<p> This property can be used for tests that are expected to fail and return a non zero return code. </p>
</dl>
<h2>PROPERTIES ON SOURCE FILES</h2>
<dl>
<dt><code>ABSTRACT</code></p>
<dd> Is this source file an abstract class. </p>
<p> A property on a source file that indicates if the source file represents a class that is abstract. This only makes sense for languages that have a notion of an abstract class and it is only used by some tools that wrap classes into other languages. </p>
<dt><code>COMPILE_DEFINITIONS</code></p>
<dd> Preprocessor definitions for compiling a source file. </p>
<p> The COMPILE_DEFINITIONS property may be set to a list of preprocessor definitions using the syntax VAR or VAR=value. Function-style definitions are not supported. CMake will automatically escape the value correctly for the native build system (note that CMake language syntax may require escapes to specify some values). This property may be set on a per-configuration basis using the name COMPILE_DEFINITIONS_&lt;CONFIG&gt; where &lt;CONFIG&gt; is an upper-case name (ex. &quot;COMPILE_DEFINITIONS_DEBUG&quot;). </p>
<p> CMake will automatically drop some definitions that are not supported by the native build tool. The VS6 IDE does not support definition values with spaces (but NMake does). Xcode does not support per-configuration definitions on source files. </p>
<p> Dislaimer: Most native build tools have poor support for escaping certain values. CMake has work-arounds for many cases but some values may just not be possible to pass correctly. If a value does not seem to be escaped correctly, do not attempt to work-around the problem by adding escape sequences to the value. Your work-around may break in a future version of CMake that has improved escape support. Instead consider defining the macro in a (configured) header file. Then report the limitation. </p>
<dt><code>COMPILE_DEFINITIONS_&lt;CONFIG&gt;</code></p>
<dd> Per-configuration preprocessor definitions on a source file. </p>
<p> This is the configuration-specific version of COMPILE_DEFINITIONS. Note that Xcode does not support per-configuration source file flags so this property will be ignored by the Xcode generator. </p>
<dt><code>COMPILE_FLAGS</code></p>
<dd> Additional flags to be added when compiling this source file. </p>
<p> These flags will be added to the list of compile flags when this source file builds. Use COMPILE_DEFINITIONS to pass additional preprocessor definitions. </p>
<dt><code>EXTERNAL_OBJECT</code></p>
<dd> If set to true then this is an object file. </p>
<p> If this property is set to true then the source file is really an object file and should not be compiled. It will still be linked into the target though. </p>
<dt><code>GENERATED</code></p>
<dd> Is this source file generated as part of the build process. </p>
<p> If a source file is generated by the build process CMake will handle it differently in temrs of dependency checking etc. Otherwise having a non-existent source file could create problems. </p>
<dt><code>HEADER_FILE_ONLY</code></p>
<dd> Is this source file only a header file. </p>
<p> A property on a source file that indicates if the source file is a header file with no associated implementation. This is set automatically based on the file extension and is used by CMake to determine is certain dependency information should be computed. </p>
<dt><code>KEEP_EXTENSION</code></p>
<dd> Make the output file have the same extension as the source file. </p>
<p> If this property is set then the file extension of the output file will be the same as that of the source file. Normally the output file extension is computed based on the language of the source file, for example .cxx will go to a .o extension. </p>
<dt><code>LANGUAGE</code></p>
<dd> What programming language is the file. </p>
<p> A property that can be set to indicate what programming language the source file is. If it is not set the language is determined based on the file extension. Typical values are CXX C etc. </p>
<dt><code>LOCATION</code></p>
<dd> The full path to a source file. </p>
<p> A read only property on a SOURCE FILE that contains the full path to the source file. </p>
<dt><code>MACOSX_PACKAGE_LOCATION</code></p>
<dd> Place a source file inside a Mac OS X bundle or framework. </p>
<p> Executable targets with the MACOSX_BUNDLE property set are built as Mac OS X application bundles on Apple platforms. Shared library targets with the FRAMEWORK property set are built as Mac OS X frameworks on Apple platforms. Source files listed in the target with this property set will be copied to a directory inside the bundle or framework content folder specified by the property value. For bundles the content folder is &quot;&lt;name&gt;.app/Contents&quot;. For frameworks the content folder is &quot;&lt;name&gt;.framework/Versions/&lt;version&gt;&quot;. See the PUBLIC_HEADER, PRIVATE_HEADER, and RESOURCE target properties for specifying files meant for Headers, PrivateHeadres, or Resources directories. </p>
<dt><code>OBJECT_DEPENDS</code></p>
<dd> Additional files on which a compiled object file depends. </p>
<p> Specifies a semicolon-separated list of full-paths to files on which any object files compiled from this source file depend. An object file will be recompiled if any of the named files is newer than it. </p>
<p> This property need not be used to specify the dependency of a source file on a generated header file that it includes. Although the property was originally introduced for this purpose, it is no longer necessary. If the generated header file is created by a custom command in the same target as the source file, the automatic dependency scanning process will recognize the dependency. If the generated header file is created by another target, an inter-target dependency should be created with the add_dependencies command (if one does not already exist due to linking relationships). </p>
<dt><code>OBJECT_OUTPUTS</code></p>
<dd> Additional outputs for a Makefile rule. </p>
<p> Additional outputs created by compilation of this source file. If any of these outputs is missing the object will be recompiled. This is supported only on Makefile generators and will be ignored on other generators. </p>
<dt><code>SYMBOLIC</code></p>
<dd> Is this just a name for a rule. </p>
<p> If SYMBOLIC (boolean) is set to true the build system will be informed that the source file is not actually created on disk but instead used as a symbolic name for a build rule. </p>
<dt><code>WRAP_EXCLUDE</code></p>
<dd> Exclude this source file from any code wrapping techniques. </p>
<p> Some packages can wrap source files into alternate languages to provide additional functionality. For example, C++ code can be wrapped into Java or Python etc using SWIG etc. If WRAP_EXCLUDE is set to true (1 etc) that indicates then this source file should not be wrapped. </p>
</dl>
<h2>COMPATIBILITY COMMANDS</h2>
<pre>
  CMake Compatibility Listfile Commands - Obsolete commands supported by CMake for compatibility.
</pre>
<p> This is the documentation for now obsolete listfile commands from previous CMake versions, which are still supported for compatibility reasons. You should instead use the newer, faster and shinier new commands. ;-) </p>
<h2>COMPATILBILITY COMMANDS</h2>
<dl>
<dt><code>build_name</code></p>
<dd> Deprecated. Use ${CMAKE_SYSTEM} and ${CMAKE_CXX_COMPILER} instead. </p>
<pre>
  build_name(variable)
</pre>
<p> Sets the specified variable to a string representing the platform and compiler settings. These values are now available through the CMAKE_SYSTEM and CMAKE_CXX_COMPILER variables. </p>
<dt><code>exec_program</code></p>
<dd> Deprecated. Use the execute_process() command instead. </p>
<p> Run an executable program during the processing of the CMakeList.txt file. </p>
<p>exec_program(Executable[directory in which to run]<br />
                       [ARGS&lt;arguments to executable&gt;]<br />
                       [OUTPUT_VARIABLE&lt;var&gt;]<br />
                       [RETURN_VALUE&lt;var&gt;])</p>
<p> The executable is run in the optionally specified directory. The executable can include arguments if it is double quoted, but it is better to use the optional ARGS argument to specify arguments to the program. This is because cmake will then be able to escape spaces in the executable path. An optional argument OUTPUT_VARIABLE specifies a variable in which to store the output. To capture the return value of the execution, provide a RETURN_VALUE. If OUTPUT_VARIABLE is specified, then no output will go to the stdout/stderr of the console running cmake. </p>
<dt><code>export_library_dependencies</code></p>
<dd> Deprecated. Use INSTALL(EXPORT) or EXPORT command. </p>
<p> This command generates an old-style library dependencies file. Projects requiring CMake 2.6 or later should not use the command. Use instead the install(EXPORT) command to help export targets from an installation tree and the export() command to export targets from a build tree. </p>
<p> The old-style library dependencies file does not take into account per-configuration names of libraries or the LINK_INTERFACE_LIBRARIES target property. </p>
<pre>
  export_library_dependencies(&lt;file&gt; [APPEND])
</pre>
<p> Create a file named &lt;file&gt; that can be included into a CMake listfile with the INCLUDE command. The file will contain a number of SET commands that will set all the variables needed for library dependency information. This should be the last command in the top level CMakeLists.txt file of the project. If the APPEND option is specified, the SET commands will be appended to the given file instead of replacing it. </p>
<dt><code>install_files</code></p>
<dd> Deprecated. Use the install(FILES ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. The FILES form is directly replaced by the FILES form of the install command. The regexp form can be expressed more clearly using the GLOB form of the file command. </p>
<pre>
  install_files(&lt;dir&gt; extension file file ...)
</pre>
<p> Create rules to install the listed files with the given extension into the given directory. Only files existing in the current source tree or its corresponding location in the binary tree may be listed. If a file specified already has an extension, that extension will be removed first. This is useful for providing lists of source files such as foo.cxx when you want the corresponding foo.h to be installed. A typical extension is &#8216;.h&#8217;. </p>
<pre>
  install_files(&lt;dir&gt; regexp)
</pre>
<p> Any files in the current source directory that match the regular expression will be installed. </p>
<pre>
  install_files(&lt;dir&gt; FILES file file ...)
</pre>
<p> Any files listed after the FILES keyword will be installed explicitly from the names given. Full paths are allowed in this form. </p>
<p> The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. </p>
<dt><code>install_programs</code></p>
<dd> Deprecated. Use the install(PROGRAMS ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. The FILES form is directly replaced by the PROGRAMS form of the INSTALL command. The regexp form can be expressed more clearly using the GLOB form of the FILE command. </p>
<p>install_programs(&lt;dir&gt; file1 file2[file3&#8230;])<br />
    install_programs(&lt;dir&gt; FILES file1[file2&#8230;])</p>
<p> Create rules to install the listed programs into the given directory. Use the FILES argument to guarantee that the file list version of the command will be used even when there is only one argument. </p>
<pre>
  install_programs(&lt;dir&gt; regexp)
</pre>
<p> In the second form any program in the current source directory that matches the regular expression will be installed. </p>
<p> This command is intended to install programs that are not built by cmake, such as shell scripts. See the TARGETS form of the INSTALL command to create installation rules for targets built by cmake. </p>
<p> The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. </p>
<dt><code>install_targets</code></p>
<dd> Deprecated. Use the install(TARGETS ) command instead. </p>
<p> This command has been superceded by the install command. It is provided for compatibility with older CMake code. </p>
<pre>
  install_targets(&lt;dir&gt; [RUNTIME_DIRECTORY dir] target target)
</pre>
<p> Create rules to install the listed targets into the given directory. The directory &lt;dir&gt; is relative to the installation prefix, which is stored in the variable CMAKE_INSTALL_PREFIX. If RUNTIME_DIRECTORY is specified, then on systems with special runtime files (Windows DLL), the files will be copied to that directory. </p>
<dt><code>link_libraries</code></p>
<dd> Deprecated. Use the target_link_libraries() command instead. </p>
<p> Link libraries to all targets added later. </p>
<pre>
  link_libraries(library1 &lt;debug | optimized&gt; library2 ...)
</pre>
<p> Specify a list of libraries to be linked into any following targets (typically added with the add_executable or add_library calls). This command is passed down to all subdirectories. The debug and optimized strings may be used to indicate that the next library listed is to be used only for that specific type of build. </p>
<dt><code>make_directory</code></p>
<dd> Deprecated. Use the file(MAKE_DIRECTORY ) command instead. </p>
<pre>
  make_directory(directory)
</pre>
<p> Creates the specified directory. Full paths should be given. Any parent directories that do not exist will also be created. Use with care. </p>
<dt><code>remove</code></p>
<dd> Deprecated. Use the list(REMOVE_ITEM ) command instead. </p>
<pre>
  remove(VAR VALUE VALUE ...)
</pre>
<p> Removes VALUE from the variable VAR. This is typically used to remove entries from a vector (e.g. semicolon separated list). VALUE is expanded. </p>
<dt><code>subdir_depends</code></p>
<dd> Deprecated. Does nothing. </p>
<pre>
  subdir_depends(subdir dep1 dep2 ...)
</pre>
<p> Does not do anything. This command used to help projects order parallel builds correctly. This functionality is now automatic. </p>
<dt><code>subdirs</code></p>
<dd> Deprecated. Use the add_subdirectory() command instead. </p>
<p> Add a list of subdirectories to the build. </p>
<p>subdirs(dir1 dir2&#8230;[EXCLUDE_FROM_ALL exclude_dir1 exclude_dir2&#8230;][PREORDER])</p>
<p> Add a list of subdirectories to the build. The add_subdirectory command should be used instead of subdirs although subdirs will still work. This will cause any CMakeLists.txt files in the sub directories to be processed by CMake. Any directories after the PREORDER flag are traversed first by makefile builds, the PREORDER flag has no effect on IDE projects. Any directories after the EXCLUDE_FROM_ALL marker will not be included in the top level makefile or project file. This is useful for having CMake create makefiles or projects for a set of examples in a project. You would want CMake to generate makefiles or project files for all the examples at the same time, but you would not want them to show up in the top level project or be built each time make is run from the top. </p>
<dt><code>use_mangled_mesa</code></p>
<dd> Copy mesa headers for use in combination with system GL. </p>
<pre>
  use_mangled_mesa(PATH_TO_MESA OUTPUT_DIRECTORY)
</pre>
<p> The path to mesa includes, should contain gl_mangle.h. The mesa headers are copied to the specified output directory. This allows mangled mesa headers to override other GL headers by being added to the include directory path earlier. </p>
<dt><code>utility_source</code></p>
<dd> Specify the source tree of a third-party utility. </p>
<pre>
  utility_source(cache_entry executable_name
                 path_to_source [file1 file2 ...])
</pre>
<p> When a third-party utility&#8217;s source is included in the distribution, this command specifies its location and name. The cache entry will not be set unless the path_to_source and all listed files exist. It is assumed that the source tree of the utility will have been built before it is needed. </p>
<p> When cross compiling CMake will print a warning if a utility_source() command is executed, because in many cases it is used to build an executable which is executed later on. This doesn&#8217;t work when cross compiling, since the executable can run only on their target platform. So in this case the cache entry has to be adjusted manually so it points to an executable which is runnable on the build host. </p>
<dt><code>variable_requires</code></p>
<dd> Deprecated. Use the if() command instead. </p>
<p> Assert satisfaction of an option&#8217;s required variables. </p>
<pre>
  variable_requires(TEST_VARIABLE RESULT_VARIABLE
                    REQUIRED_VARIABLE1
                    REQUIRED_VARIABLE2 ...)
</pre>
<p> The first argument (TEST_VARIABLE) is the name of the variable to be tested, if that variable is false nothing else is done. If TEST_VARIABLE is true, then the next argument (RESULT_VARIABLE) is a variable that is set to true if all the required variables are set. The rest of the arguments are variables that must be true or not set to NOTFOUND to avoid an error. If any are not true, an error is reported. </p>
<dt><code>write_file</code></p>
<dd> Deprecated. Use the file(WRITE ) command instead. </p>
<pre>
  write_file(filename &quot;message to write&quot;... [APPEND])
</pre>
<p> The first argument is the file name, the rest of the arguments are messages to write. If the argument APPEND is specified, then the message will be appended. </p>
<p> NOTE 1: file(WRITE &#8230; and file(APPEND &#8230; do exactly the same as this one but add some more functionality. </p>
<p> NOTE 2: When using write_file the produced file cannot be used as an input to CMake (CONFIGURE_FILE, source file &#8230;) because it will lead to an infinite loop. Use configure_file if you want to generate input files to CMake. </p>
</dl>
<h2>MODULES</h2>
<p> The following modules are provided with CMake. They can be used with INCLUDE(ModuleName). </p>
<pre>
  CMake Modules - Modules coming with CMake, the Cross-Platform Makefile Generator.
</pre>
<p> This is the documentation for the modules and scripts coming with CMake. Using these modules you can check the computer system for installed software packages, features of the compiler and the existance of headers to name just a few. </p>
<dl>
<dt><code>AddFileDependencies</code></p>
<dd> ADD_FILE_DEPENDENCIES(source_file depend_files&#8230;) </p>
<p> Adds the given files as dependencies to source_file </p>
<dt><code>BundleUtilities</code></p>
<dd>
<p> BundleUtilities.cmake </p>
<p> A collection of CMake utility functions useful for dealing with .app bundles on the Mac and bundle-like directories on any OS. </p>
<p> The following functions are provided by this script: </p>
<pre>
   get_bundle_main_executable
   get_dotapp_dir
   get_bundle_and_executable
   get_bundle_all_executables
   get_item_key
   clear_bundle_keys
   set_bundle_key_values
   get_bundle_keys
   copy_resolved_item_into_bundle
   fixup_bundle_item
   fixup_bundle
   copy_and_fixup_bundle
   verify_bundle_prerequisites
   verify_bundle_symlinks
   verify_app
</pre>
<p> Requires CMake 2.6 or greater because it uses function, break and PARENT_SCOPE. Also depends on GetPrerequisites.cmake. </p>
<dt><code>CMakeASM-ATTInformation</code></p>
<dd>
<p> support for AT&amp;T syntax assemblers, e.g. GNU as </p>
<dt><code>CMakeASM_MASMInformation</code></p>
<dd>
<p> support for the MS assembler, masm and masm64 </p>
<dt><code>CMakeBackwardCompatibilityCXX</code></p>
<dd> define a bunch of backwards compatibility variables </p>
<pre>
  CMAKE_ANSI_CXXFLAGS - flag for ansi c++ 
  CMAKE_HAS_ANSI_STRING_STREAM - has &lt;strstream&gt;
  INCLUDE(TestForANSIStreamHeaders)
  INCLUDE(CheckIncludeFileCXX)
  INCLUDE(TestForSTDNamespace)
  INCLUDE(TestForANSIForScope)
</pre>
<dt><code>CMakeDependentOption</code></p>
<dd> Macro to provide an option dependent on other options. </p>
<p> This macro presents an option to the user only if a set of other conditions are true. When the option is not presented a default value is used, but any value set by the user is preserved for when the option is presented again. Example invocation: </p>
<pre>
  CMAKE_DEPENDENT_OPTION(USE_FOO &quot;Use Foo&quot; ON
                         &quot;USE_BAR;NOT USE_ZOT&quot; OFF)
</pre>
<p> If USE_BAR is true and USE_ZOT is false, this provides an option called USE_FOO that defaults to ON. Otherwise, it sets USE_FOO to OFF. If the status of USE_BAR or USE_ZOT ever changes, any value for the USE_FOO option is saved so that when the option is re-enabled it retains its old value. </p>
<dt><code>CMakeDetermineASM-ATTCompiler</code></p>
<dd>
<p> determine the compiler to use for ASM using AT&amp;T syntax, e.g. GNU as </p>
<dt><code>CMakeDetermineASMCompiler</code></p>
<dd>
<p> determine the compiler to use for ASM programs </p>
<dt><code>CMakeDetermineASM_MASMCompiler</code></p>
<dd>
<p> Find the MS assembler (masm or masm64) </p>
<dt><code>CMakeExportBuildSettings</code></p>
<dd> export build settings from a project. </p>
<pre>
  CMAKE_EXPORT_BUILD_SETTINGS(SETTINGS_FILE)
</pre>
<p> macro defined to export the build settings for use by another project. </p>
<pre>
  SETTINGS_FILE - the file into which the settings are to be stored.
</pre>
<dt><code>CMakeFindFrameworks</code></p>
<dd> helper module to find OSX frameworks </p>
<dt><code>CMakeForceCompiler</code></p>
<dd>
<p> This module defines macros intended for use by cross-compiling toolchain files when CMake is not able to automatically detect the compiler identification. </p>
<p> Macro CMAKE_FORCE_C_COMPILER has the following signature: </p>
<pre>
   CMAKE_FORCE_C_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)
</pre>
<p> It sets CMAKE_C_COMPILER to the given compiler and the cmake internal variable CMAKE_C_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> Macro CMAKE_FORCE_CXX_COMPILER has the following signature: </p>
<pre>
   CMAKE_FORCE_CXX_COMPILER(&lt;compiler&gt; &lt;compiler-id&gt;)
</pre>
<p> It sets CMAKE_CXX_COMPILER to the given compiler and the cmake internal variable CMAKE_CXX_COMPILER_ID to the given compiler-id. It also bypasses the check for working compiler and basic compiler information tests. </p>
<p> So a simple toolchain file could look like this: </p>
<pre>
   INCLUDE (CMakeForceCompiler)
   SET(CMAKE_SYSTEM_NAME Generic)
   CMAKE_FORCE_C_COMPILER   (chc12 MetrowerksHicross)
   CMAKE_FORCE_CXX_COMPILER (chc12 MetrowerksHicross)
</pre>
<dt><code>CMakeImportBuildSettings</code></p>
<dd> import build settings from another project </p>
<pre>
  CMAKE_IMPORT_BUILD_SETTINGS(SETTINGS_FILE) 
</pre>
<p> macro defined to import the build settings from another project. SETTINGS_FILE is a file created by the other project&#8217;s call to the CMAKE_EXPORT_BUILD_SETTINGS macro, see CMakeExportBuildSettings. </p>
<dt><code>CMakeJavaInformation</code></p>
<dd>
<p> This should be included before the _INIT variables are used to initialize the cache. Since the rule variables have if blocks on them, users can still define them here. But, it should still be after the platform file so changes can be made to those values. </p>
<dt><code>CMakePrintSystemInformation</code></p>
<dd> print system information </p>
<p> This file can be used for diagnostic purposes just include it in a project to see various internal CMake variables. </p>
<dt><code>CPack</code></p>
<dd> Build binary and source package installers </p>
<p> The CPack module generates binary and source installers in a variety of formats using the cpack program. Inclusion of the CPack module adds two new targets to the resulting makefiles, package and package_source, which build the binary and source installers, respectively. The generated binary installers contain everything installed via CMake&#8217;s INSTALL command (and the deprecated INSTALL_FILES, INSTALL_PROGRAMS, and INSTALL_TARGETS commands). </p>
<p> For certain kinds of binary installers (including the graphical installers on Mac OS X and Windows), CPack generates installers that allow users to select individual application components to install. The contents of each of the components are identified by the COMPONENT argument of CMake&#8217;s INSTALL command. These components can be annotated with user-friendly names and descriptions, inter-component dependencies, etc., and grouped in various ways to customize the resulting installer. See the cpack_add_* commands, described below, for more information about component-specific installations. </p>
<p> Before including the CPack module, there are a variety of variables that can be set to customize the resulting installers. The most commonly-used variables are: </p>
<pre>
   CPACK_PACKAGE_NAME - The name of the package (or application). If
   not specified, defaults to the project name.
</pre>
<pre>
   CPACK_PACKAGE_VENDOR - The name of the package vendor (e.g.,
   &quot;Kitware&quot;).
</pre>
<pre>
   CPACK_PACKAGE_VERSION_MAJOR - Package major Version
</pre>
<pre>
   CPACK_PACKAGE_VERSION_MINOR - Package minor Version
</pre>
<pre>
   CPACK_PACKAGE_VERSION_PATCH - Package patch Version
</pre>
<pre>
   CPACK_PACKAGE_DESCRIPTION_FILE - A text file used to describe the
   project. Used, for example, the introduction screen of a
   CPack-generated Windows installer to describe the project.
</pre>
<pre>
   CPACK_PACKAGE_DESCRIPTION_SUMMARY - Short description of the
   project (only a few words).
</pre>
<pre>
   CPACK_PACKAGE_FILE_NAME - The name of the package file to generate,
   not including the extension. For example, cmake-2.6.1-Linux-i686.
</pre>
<pre>
   CPACK_PACKAGE_INSTALL_DIRECTORY - Installation directory on the
   target system, e.g., &quot;CMake 2.5&quot;.
</pre>
<pre>
   CPACK_RESOURCE_FILE_LICENSE - License file for the project, which
   will typically be displayed to the user (often with an explicit
   &quot;Accept&quot; button, for graphical installers) prior to installation.
</pre>
<pre>
   CPACK_RESOURCE_FILE_README - ReadMe file for the project, which
   typically describes in some detail
</pre>
<pre>
   CPACK_RESOURCE_FILE_WELCOME - Welcome file for the project, which
   welcomes users to this installer. Typically used in the graphical
   installers on Windows and Mac OS X.
</pre>
<pre>
   CPACK_MONOLITHIC_INSTALL - Disables the component-based 
   installation mechanism, so that all components are always installed.
</pre>
<pre>
   CPACK_GENERATOR - List of CPack generators to use. If not
   specified, CPack will create a set of options (e.g.,
   CPACK_BINARY_NSIS) allowing the user to enable/disable individual
   generators.
</pre>
<pre>
   CPACK_OUTPUT_CONFIG_FILE - The name of the CPack configuration file
   for binary installers that will be generated by the CPack
   module. Defaults to CPackConfig.cmake.
</pre>
<pre>
   CPACK_PACKAGE_EXECUTABLES - Lists each of the executables along
   with a text label, to be used to create Start Menu shortcuts on
   Windows. For example, setting this to the list ccmake;CMake will
   create a shortcut named &quot;CMake&quot; that will execute the installed
   executable ccmake.
</pre>
<pre>
   CPACK_STRIP_FILES - List of files to be stripped. Starting with
   CMake 2.6.0 CPACK_STRIP_FILES will be a boolean variable which
   enables stripping of all files (a list of files evaluates to TRUE
   in CMake, so this change is compatible).
</pre>
<p> The following CPack variables are specific to source packages, and will not affect binary packages: </p>
<pre>
   CPACK_SOURCE_PACKAGE_FILE_NAME - The name of the source package,
   e.g., cmake-2.6.1
</pre>
<pre>
   CPACK_SOURCE_STRIP_FILES - List of files in the source tree that
   will be stripped. Starting with CMake 2.6.0
   CPACK_SOURCE_STRIP_FILES will be a boolean variable which enables
   stripping of all files (a list of files evaluates to TRUE in CMake,
   so this change is compatible).
</pre>
<pre>
   CPACK_SOURCE_GENERATOR - List of generators used for the source
   packages. As with CPACK_GENERATOR, if this is not specified then
   CPack will create a set of options (e.g., CPACK_SOURCE_ZIP)
   allowing users to select which packages will be generated.
</pre>
<pre>
   CPACK_SOURCE_OUTPUT_CONFIG_FILE - The name of the CPack
   configuration file for source installers that will be generated by
   the CPack module. Defaults to CPackSourceConfig.cmake.
</pre>
<pre>
   CPACK_SOURCE_IGNORE_FILES - Pattern of files in the source tree
   that won't be packaged when building a source package. This is a
   list of patterns, e.g., /CVS/;/\.svn/;\.swp$;\.#;/#;.*~;cscope.*
</pre>
<p> The following variables are specific to the graphical installers built on Windows using the Nullsoft Installation System. </p>
<pre>
   CPACK_PACKAGE_INSTALL_REGISTRY_KEY - Registry key used when
   installing this project.
</pre>
<pre>
   CPACK_NSIS_MUI_ICON - The icon file (.ico) for the generated
   install program.
</pre>
<pre>
   CPACK_NSIS_MUI_UNIICON - The icon file (.ico) for the generated
   uninstall program.
</pre>
<pre>
   CPACK_PACKAGE_ICON - A branding image that will be displayed inside
   the installer.
</pre>
<pre>
   CPACK_NSIS_EXTRA_INSTALL_COMMANDS - Extra NSIS commands that will
   be added to the install Section.
</pre>
<pre>
   CPACK_NSIS_EXTRA_UNINSTALL_COMMANDS - Extra NSIS commands that will
   be added to the uninstall Section.
</pre>
<pre>
   CPACK_NSIS_COMPRESSOR - The arguments that will be passed to the
   NSIS SetCompressor command.
</pre>
<pre>
   CPACK_NSIS_MODIFY_PATH - If this is set to &quot;ON&quot;, then an extra page
   will appear in the installer that will allow the user to choose
   whether the program directory should be added to the system PATH
   variable.
</pre>
<pre>
   CPACK_NSIS_DISPLAY_NAME - The title displayed at the top of the
   installer.
</pre>
<pre>
   CPACK_NSIS_INSTALLED_ICON_NAME - A path to the executable that
   contains the installer icon.
</pre>
<pre>
   CPACK_NSIS_HELP_LINK - URL to a web site providing assistance in
   installing your application.
</pre>
<pre>
   CPACK_NSIS_URL_INFO_ABOUT - URL to a web site providing more
   information about your application.
</pre>
<pre>
   CPACK_NSIS_CONTACT - Contact information for questions and comments
   about the installation process.
</pre>
<pre>
   CPACK_NSIS_CREATE_ICONS_EXTRA - Additional NSIS commands for
   creating start menu shortcuts.
</pre>
<pre>
   CPACK_NSIS_DELETE_ICONS_EXTRA -Additional NSIS commands to
   uninstall start menu shortcuts.
</pre>
<p> The following variable is specific to installers build on Mac OS X using PackageMaker: </p>
<pre>
   CPACK_OSX_PACKAGE_VERSION - The version of Mac OS X that the
   resulting PackageMaker archive should be compatible
   with. Different versions of Mac OS X support different
   features. For example, CPack can only build component-based
   installers for Mac OS X 10.4 or newer, and can only build
   installers that download component son-the-fly for Mac OS X 10.5
   or newer. If left blank, this value will be set to the minimum
   version of Mac OS X that supports the requested features. Set this
   variable to some value (e.g., 10.4) only if you want to guarantee
   that your installer will work on that version of Mac OS X, and
   don't mind missing extra features available in the installer
   shipping with later versions of Mac OS X.
</pre>
<p> The following variables are for advanced uses of CPack: </p>
<pre>
   CPACK_CMAKE_GENERATOR - What CMake generator should be used if the
   project is CMake project. Defaults to the value of CMAKE_GENERATOR;
   few users will want to change this setting.
</pre>
<pre>
   CPACK_INSTALL_CMAKE_PROJECTS - List of four values that specify
   what project to install. The four values are: Build directory,
   Project Name, Project Component, Directory. If omitted, CPack will
   build an installer that installers everything.
</pre>
<pre>
   CPACK_SYSTEM_NAME - System name, defaults to the value of
   ${CMAKE_SYSTEM_NAME}.
</pre>
<pre>
   CPACK_PACKAGE_VERSION - Package full version, used internally. By
   default, this is built from CPACK_PACKAGE_VERSION_MAJOR,
   CPACK_PACKAGE_VERSION_MINOR, and CPACK_PACKAGE_VERSION_PATCH.
</pre>
<pre>
   CPACK_TOPLEVEL_TAG - Directory for the installed files.
</pre>
<pre>
   CPACK_INSTALL_COMMANDS - Extra commands to install components.
</pre>
<pre>
   CPACK_INSTALL_DIRECTORIES - Extra directories to install.
</pre>
<p> Component-specific installation allows users to select specific sets of components to install during the install process. Installation components are identified by the COMPONENT argument of CMake&#8217;s INSTALL commands, and should be further described by the following CPack commands: </p>
<pre>
   cpack_add_component - Describes a CPack installation component
   named by the COMPONENT argument to a CMake INSTALL command.
</pre>
<p>cpack_add_component(compname<br />
                        [DISPLAY_NAME name]<br />
                        [DESCRIPTION description]<br />
                        [HIDDEN | REQUIRED | DISABLED]<br />
                        [GROUP group]<br />
                        [DEPENDS comp1 comp2&#8230;]<br />
                        [INSTALL_TYPES type1 type2&#8230;]<br />
                        [DOWNLOADED]<br />
                        [ARCHIVE_FILE filename])</p>
<pre>
   The cmake_add_component command describes an installation
   component, which the user can opt to install or remove as part of
   the graphical installation process. compname is the name of the
   component, as provided to the COMPONENT argument of one or more
   CMake INSTALL commands.
</pre>
<pre>
   DISPLAY_NAME is the displayed name of the component, used in
   graphical installers to display the component name. This value can
   be any string.
</pre>
<pre>
   DESCRIPTION is an extended description of the component, used in
   graphical installers to give the user additional information about
   the component. Descriptions can span multiple lines using &quot;
&quot; as
   the line separator. Typically, these descriptions should be no
   more than a few lines long.
</pre>
<pre>
   HIDDEN indicates that this component will be hidden in the
   graphical installer, so that the user cannot directly change
   whether it is installed or not.
</pre>
<pre>
   REQUIRED indicates that this component is required, and therefore
   will always be installed. It will be visible in the graphical
   installer, but it cannot be unselected. (Typically, required
   components are shown greyed out).
</pre>
<pre>
   DISABLED indicates that this component should be disabled
   (unselected) by default. The user is free to select this component
   for installation, unless it is also HIDDEN.
</pre>
<pre>
   DEPENDS lists the components on which this component depends. If
   this component is selected, then each of the components listed
   must also be selected. The dependency information is encoded
   within the installer itself, so that users cannot install
   inconsitent sets of components.
</pre>
<pre>
   GROUP names the component group of which this component is a
   part. If not provided, the component will be a standalone
   component, not part of any component group. Component groups are
   described with the cpack_add_component_group command, detailed
   below.
</pre>
<pre>
   INSTALL_TYPES lists the installation types of which this component
   is a part. When one of these installations types is selected, this
   component will automatically be selected. Installation types are
   described with the cpack_add_install_type command, detailed below.
</pre>
<pre>
   DOWNLOADED indicates that this component should be downloaded
   on-the-fly by the installer, rather than packaged in with the
   installer itself. For more information, see the cpack_configure_downloads
   command.
</pre>
<pre>
   ARCHIVE_FILE provides a name for the archive file created by CPack
   to be used for downloaded components. If not supplied, CPack will
   create a file with some name based on CPACK_PACKAGE_FILE_NAME and
   the name of the component. See cpack_configure_downloads for more
   information.
</pre>
<pre>
   cpack_add_component_group - Describes a group of related CPack
   installation components.
</pre>
<p>cpack_add_component_group(groupname<br />
                              [DISPLAY_NAME name]<br />
                              [DESCRIPTION description]<br />
                              [PARENT_GROUP parent]<br />
                              [EXPANDED]<br />
                              [BOLD_TITLE])</p>
<pre>
   The cpack_add_component_group describes a group of installation
   components, which will be placed together within the listing of
   options. Typically, component groups allow the user to
   select/deselect all of the components within a single group via a
   single group-level option. Use component groups to reduce the
   complexity of installers with many options. groupname is an
   arbitrary name used to identify the group in the GROUP argument of
   the cpack_add_component command, which is used to place a
   component in a group. The name of the group must not conflict with
   the name of any component.
</pre>
<pre>
   DISPLAY_NAME is the displayed name of the component group, used in
   graphical installers to display the component group name. This
   value can be any string.
</pre>
<pre>
   DESCRIPTION is an extended description of the component group,
   used in graphical installers to give the user additional
   information about the components within that group. Descriptions
   can span multiple lines using &quot;
&quot; as the line
   separator. Typically, these descriptions should be no more than a
   few lines long.
</pre>
<pre>
   PARENT_GROUP, if supplied, names the parent group of this group. 
   Parent groups are used to establish a hierarchy of groups, 
   providing an arbitrary hierarchy of groups.
</pre>
<pre>
   EXPANDED indicates that, by default, the group should show up as
   &quot;expanded&quot;, so that the user immediately sees all of the
   components within the group. Otherwise, the group will initially
   show up as a single entry.
</pre>
<pre>
   BOLD_TITLE indicates that the group title should appear in bold,
   to call the user's attention to the group.
</pre>
<pre>
   cpack_add_install_type - Add a new installation type containing a
   set of predefined component selections to the graphical installer.
                      
     cpack_add_install_type(typename
                            [DISPLAY_NAME name])   
</pre>
<p>   The cpack_add_install_type command identifies a set of preselected<br />
   components that represents a common use case for an<br />
   application. For example, a &#8220;Developer&#8221; install type might include<br />
   an application along with its header and library files, while an<br />
   &#8220;End user&#8221; install type might just include the application&#8217;s<br />
   executable. Each component identifies itself with one or more<br />
   install types via the INSTALL_TYPES argument to<br />
   cpack_add_component.</p>
<pre>
   DISPLAY_NAME is the displayed name of the install type, which will
   typically show up in a drop-down box within a graphical
   installer. This value can be any string.
</pre>
<pre>
   cpack_configure_downloads - Configure CPack to download selected
   components on-the-fly as part of the installation process.
</pre>
<p>cpack_configure_downloads(site<br />
                              [UPLOAD_DIRECTORY dirname]<br />
                              [ALL]<br />
                              [ADD_REMOVE | NO_ADD_REMOVE])</p>
<pre>
   The cpack_configure_downloads command configures installation-time
   downloads of selected components. For each downloadable component,
   CPack will create an archive containing the contents of that
   component, which should be uploaded to the given site. When the
   user selects that component for installation, the installer will
   download and extract the component in place. This feature is
   useful for creating small installers that only download the
   requested components, saving bandwidth. Additionally, the
   installers are small enough that they will be installed as part of
   the normal installation process, and the &quot;Change&quot; button in
   Windows Add/Remove Programs control panel will allow one to add or
   remove parts of the application after the original
   installation. On Windows, the downloaded-components functionality
   requires the ZipDLL plug-in for NSIS, available at:
</pre>
<pre>
     <a rel="nofollow" href="http://nsis.sourceforge.net/ZipDLL_plug-in">http://nsis.sourceforge.net/ZipDLL_plug-in</a>
</pre>
<pre>
   On Mac OS X, installers that download components on-the-fly can
   only be built and installed on system using Mac OS X 10.5 or
   later.
</pre>
<pre>
   The site argument is a URL where the archives for downloadable 
   components will reside, e.g., <a rel="nofollow" href="http://www.cmake.org/files/2.6.1/installer/">http://www.cmake.org/files/2.6.1/installer/</a>
   All of the archives produced by CPack should be uploaded to that location.
</pre>
<pre>
   UPLOAD_DIRECTORY is the local directory where CPack will create the 
   various archives for each of the components. The contents of this
   directory should be uploaded to a location accessible by the URL given
   in the site argument. If omitted, CPack will use the directory CPackUploads
   inside the CMake binary directory to store the generated archives.
</pre>
<pre>
   The ALL flag indicates that all components be downloaded. Otherwise, only 
   those components explicitly marked as DOWNLOADED or that have a specified 
   ARCHIVE_FILE will be downloaded. Additionally, the ALL option implies
   ADD_REMOVE (unless NO_ADD_REMOVE is specified).
</pre>
<pre>
   ADD_REMOVE indicates that CPack should install a copy of the installer
   that can be called from Windows' Add/Remove Programs dialog (via the 
   &quot;Modify&quot; button) to change the set of installed components. NO_ADD_REMOVE
   turns off this behavior. This option is ignored on Mac OS X.
</pre>
<dt><code>CPackRPM</code></p>
<dd>
<p> CPack script for creating RPM package Author: Eric Noulard with the help of Alexander Neundorf. All variables used by CPackRPM begins with CPACK_RPM_ prefix </p>
<p> Here comes the list of used variables: </p>
<dt><code>CTest</code></p>
<dd> Configure a project for testing with CTest/CDash </p>
<p> This file configures a project to use the CTest/CDash/Dart testing/dashboard process. This module should be included in the CMakeLists.txt file at the top of a project. Typical usage: </p>
<pre>
  INCLUDE(CTest)
  IF(BUILD_TESTING)
    # ... testing related CMake code ...
  ENDIF(BUILD_TESTING)
</pre>
<p> The BUILD_TESTING option is created by the CTest module to determine whether testing support should be enabled. The default is ON. </p>
<dt><code>CTestTestfile</code></p>
<dd>
<p> CMake generated Testfile for Source directory: /builddir/build/BUILD/cmake-2.6.4/Modules Build directory: /builddir/build/BUILD/cmake-2.6.4/Modules </p>
<p> This file replicates the SUBDIRS() and ADD_TEST() commands from the source tree CMakeLists.txt file, skipping any SUBDIRS() or ADD_TEST() commands that are excluded by CMake control structures, i.e. IF() commands. </p>
<dt><code>CheckCCompilerFlag</code></p>
<dd> Check whether the C compiler supports a given flag. </p>
<p> CHECK_C_COMPILER_FLAG(FLAG VARIABLE) </p>
<pre>
  FLAG - the compiler flag
  VARIABLE - variable to store the result
</pre>
<pre>
  This actually calls the check_c_source_compiles macro.
  See help for CheckCSourceCompiles for a listing of variables
  that can modify the build.
</pre>
<dt><code>CheckCSourceCompiles</code></p>
<dd> Check if the C source code provided in the SOURCE argument compiles. </p>
<p> CHECK_C_SOURCE_COMPILES(SOURCE VAR) </p>
<pre>
  SOURCE   - source code to try to compile
  VAR      - variable to store whether the source code compiled
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCSourceRuns</code></p>
<dd> Check if the C source code provided in the SOURCE argument compiles and runs. </p>
<p> CHECK_C_SOURCE_RUNS(SOURCE VAR) </p>
<pre>
  SOURCE   - source code to try to compile
  VAR      - variable to store the result, 1 for success, empty for failure
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXCompilerFlag</code></p>
<dd> Check whether the CXX compiler supports a given flag. </p>
<p> CHECK_CXX_COMPILER_FLAG(FLAG VARIABLE) </p>
<pre>
  FLAG - the compiler flag
  VARIABLE - variable to store the result
</pre>
<dt><code>CheckCXXSourceCompiles</code></p>
<dd> Check if the C++ source code provided in the SOURCE argument compiles. </p>
<p> CHECK_CXX_SOURCE_COMPILES(SOURCE VAR) </p>
<pre>
  SOURCE - source code to try to compile
  VAR    - variable to store whether the source code compiled
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckCXXSourceRuns</code></p>
<dd> Check if the C++ source code provided in the SOURCE argument compiles and runs. </p>
<p> CHECK_CXX_SOURCE_RUNS(SOURCE VAR) </p>
<pre>
  SOURCE - source code to try to compile
  VAR    - variable to store the result, 1 for success, empty for failure
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckFortranFunctionExists</code></p>
<dd> macro which checks if the Fortran function exists </p>
<p> CHECK_FORTRAN_FUNCTION_EXISTS(FUNCTION VARIABLE) </p>
<pre>
  FUNCTION - the name of the Fortran function
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckFunctionExists</code></p>
<dd> macro which checks if the function exists </p>
<p> CHECK_FUNCTION_EXISTS(FUNCTION VARIABLE) </p>
<pre>
  FUNCTION - the name of the function
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckIncludeFile</code></p>
<dd> macro which checks the include file exists. </p>
<p> CHECK_INCLUDE_FILE(INCLUDE VARIABLE) </p>
<pre>
  INCLUDE  - name of include file
  VARIABLE - variable to return result
   
</pre>
<p> an optional third argument is the CFlags to add to the compile line or you can use CMAKE_REQUIRED_FLAGS </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckIncludeFileCXX</code></p>
<dd> Check if the include file exists. </p>
<pre>
  CHECK_INCLUDE_FILE_CXX(INCLUDE VARIABLE)
</pre>
<pre>
  INCLUDE  - name of include file
  VARIABLE - variable to return result
  
</pre>
<p> An optional third argument is the CFlags to add to the compile line or you can use CMAKE_REQUIRED_FLAGS. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckIncludeFiles</code></p>
<dd> Check if the files can be included </p>
<p> CHECK_INCLUDE_FILES(INCLUDE VARIABLE) </p>
<pre>
  INCLUDE  - list of files to include
  VARIABLE - variable to return result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<dt><code>CheckLibraryExists</code></p>
<dd> Check if the function exists. </p>
<p> CHECK_LIBRARY_EXISTS (LIBRARY FUNCTION LOCATION VARIABLE) </p>
<pre>
  LIBRARY  - the name of the library you are looking for
  FUNCTION - the name of the function
  LOCATION - location where the library should be found
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckStructHasMember</code></p>
<dd> Check if the given struct or class has the specified member variable </p>
<p> CHECK_STRUCT_HAS_MEMBER (STRUCT MEMBER HEADER VARIABLE) </p>
<pre>
  STRUCT - the name of the struct or class you are interested in
  MEMBER - the member which existence you want to check
  HEADER - the header(s) where the prototype should be declared
  VARIABLE - variable to store the result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
</pre>
<p> Example: CHECK_STRUCT_HAS_MEMBER(&quot;struct timeval&quot; tv_sec sys/select.h HAVE_TIMEVAL_TV_SEC) </p>
<dt><code>CheckSymbolExists</code></p>
<dd> Check if the symbol exists in include files </p>
<p> CHECK_SYMBOL_EXISTS(SYMBOL FILES VARIABLE) </p>
<pre>
  SYMBOL   - symbol
  FILES    - include files to check
  VARIABLE - variable to return result
</pre>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckTypeSize</code></p>
<dd> Check sizeof a type </p>
<pre>
  CHECK_TYPE_SIZE(TYPE VARIABLE [BUILTIN_TYPES_ONLY])
</pre>
<p> Check if the type exists and determine size of type. if the type exists, the size will be stored to the variable. This also calls check_include_file for sys/types.h stdint.h and stddef.h, setting HAVE_SYS_TYPES_H, HAVE_STDINT_H, and HAVE_STDDEF_H. This is because many types are stored in these include files. </p>
<p>  VARIABLE &#8211; variable to store size if the type exists.<br />
  HAVE_${VARIABLE} &#8211; does the variable exists or not<br />
  BUILTIN_TYPES_ONLY &#8211; The third argument is optional and if<br />
                       it is set to the string BUILTIN_TYPES_ONLY<br />
                       this macro will not check for any header files.</p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_INCLUDES = list of include directories
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>CheckVariableExists</code></p>
<dd> Check if the variable exists. </p>
<pre>
  CHECK_VARIABLE_EXISTS(VAR VARIABLE)
  
  VAR      - the name of the variable
  VARIABLE - variable to store the result
</pre>
<p> This macro is only for C variables. </p>
<p> The following variables may be set before calling this macro to modify the way the check is run: </p>
<pre>
  CMAKE_REQUIRED_FLAGS = string of compile command line flags
  CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
  CMAKE_REQUIRED_LIBRARIES = list of libraries to link
</pre>
<dt><code>Dart</code></p>
<dd> Configure a project for testing with CTest or old Dart Tcl Client </p>
<p> This file is the backwards-compatibility version of the CTest module. It supports using the old Dart 1 Tcl client for driving dashboard submissions as well as testing with CTest. This module should be included in the CMakeLists.txt file at the top of a project. Typical usage: </p>
<pre>
  INCLUDE(Dart)
  IF(BUILD_TESTING)
    # ... testing related CMake code ...
  ENDIF(BUILD_TESTING)
</pre>
<p> The BUILD_TESTING option is created by the Dart module to determine whether testing support should be enabled. The default is ON. </p>
<dt><code>Documentation</code></p>
<dd> DocumentationVTK.cmake </p>
<p> This file provides support for the VTK documentation framework. It relies on several tools (Doxygen, Perl, etc). </p>
<dt><code>FeatureSummary</code></p>
<dd> Macros for generating a summary of enabled/disabled features </p>
<p> PRINT_ENABLED_FEATURES() </p>
<pre>
   Print a summary of all enabled features. By default all successfull
   FIND_PACKAGE() calls will appear here, except the ones which used the QUIET keyword.
   Additional features can be added by appending an entry to the global ENABLED_FEATURES
   property. If SET_FEATURE_INFO() is used for that feature, the output will be much 
   more informative.
</pre>
<p> PRINT_DISABLED_FEATURES() </p>
<pre>
   Same as PRINT_ENABLED_FEATURES(), but for disabled features. It can be extended
   the same way by adding to the global property DISABLED_FEATURES.
</pre>
<p> SET_FEATURE_INFO(NAME DESCRIPTION [URL [COMMENT] ] ) </p>
<pre>
    Use this macro to set up information about the named feature, which will
    then be displayed by PRINT_ENABLED/DISABLED_FEATURES().
    Example: SET_FEATURE_INFO(LibXml2 &quot;XML processing library.&quot; &quot;<a rel="nofollow" href="http://xmlsoft.org/">http://xmlsoft.org/</a>&quot;)
</pre>
<dt><code>FindASPELL</code></p>
<dd> Try to find ASPELL </p>
<p> Once done this will define </p>
<pre>
  ASPELL_FOUND - system has ASPELL
  ASPELL_INCLUDE_DIR - the ASPELL include directory
  ASPELL_LIBRARIES - The libraries needed to use ASPELL
  ASPELL_DEFINITIONS - Compiler switches required for using ASPELL
</pre>
<dt><code>FindAVIFile</code></p>
<dd> Locate AVIFILE library and include paths </p>
<p> AVIFILE (<a rel="nofollow" href="http://avifile.sourceforge.net/)is">http://avifile.sourceforge.net/)is</a> a set of libraries for i386 machines to use various AVI codecs. Support is limited beyond Linux. Windows provides native AVI support, and so doesn&#8217;t need this library. This module defines </p>
<pre>
  AVIFILE_INCLUDE_DIR, where to find avifile.h , etc.
  AVIFILE_LIBRARIES, the libraries to link against
  AVIFILE_DEFINITIONS, definitions to use when compiling
  AVIFILE_FOUND, If false, don't try to use AVIFILE
</pre>
<dt><code>FindBLAS</code></p>
<dd> Find BLAS library </p>
<p> This module finds an installed fortran library that implements the BLAS linear-algebra interface (see <a rel="nofollow" href="http://www.netlib.org/blas/">http://www.netlib.org/blas/</a>). The list of libraries searched for is taken from the autoconf macro file, acx_blas.m4 (distributed at <a href="http://ac-archive.sourceforge.net/ac-archive/acx_blas.html">http://ac-archive.sourceforge.net/ac-archive/acx_blas.html</a>). </p>
<p> This module sets the following variables: </p>
<p>  BLAS_FOUND &#8211; set to true if a library implementing the BLAS interface<br />
    is found<br />
  BLAS_LINKER_FLAGS &#8211; uncached list of required linker flags (excluding -l<br />
    and -L).<br />
  BLAS_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use BLAS<br />
  BLAS95_LIBRARIES &#8211; uncached list of libraries (using full path name)<br />
    to link against to use BLAS95 interface<br />
  BLAS95_FOUND &#8211; set to true if a library implementing the BLAS f95 interface<br />
    is found<br />
  BLA_STATIC  if set on this determines what kind of linkage we do (static)<br />
  BLA_VENDOR  if set checks only the specified vendor, if not set checks<br />
     all the posibilities<br />
  BLA_F95     if set on tries to find the f95 interfaces for BLAS/LAPACK</p>
<p> ######### ## List of vendors (BLA_VENDOR) valid in this module # ATLAS, PhiPACK,CXML,DXML,SunPerf,SCSL,SGIMATH,IBMESSL,Intel10_32 (intel mkl v10 32 bit),Intel10_64lp (intel mkl v10 64 bit,lp thread model, lp64 model), # Intel( older versions of mkl 32 and 64 bit), ACML,Apple, NAS, Generic C/CXX should be enabled to use Intel mkl </p>
<dt><code>FindBZip2</code></p>
<dd> Try to find BZip2 </p>
<p> Once done this will define </p>
<pre>
  BZIP2_FOUND - system has BZip2
  BZIP2_INCLUDE_DIR - the BZip2 include directory
  BZIP2_LIBRARIES - Link these to use BZip2
  BZIP2_DEFINITIONS - Compiler switches required for using BZip2
  BZIP2_NEED_PREFIX - this is set if the functions are prefixed with BZ2_
</pre>
<dt><code>FindBoost</code></p>
<dd> Try to find Boost include dirs and libraries </p>
<p> Usage of this module as follows: </p>
<p> == Using Header-Only libraries from within Boost: == </p>
<p>find_package(Boost 1.36.0) if (Boost_FOUND)<br />
    include_directories(${Boost_INCLUDE_DIRS})<br />
        add_executable(foo foo.cc)<br />
            endif()</p>
<p> == Using actual libraries from within Boost: == </p>
<pre>
   set(Boost_USE_STATIC_LIBS   ON)
   set(Boost_USE_MULTITHREADED ON)
   find_package( Boost 1.36.0 COMPONENTS date_time filesystem system ... )
</pre>
<p>if (Boost_FOUND)<br />
include_directories(${Boost_INCLUDE_DIRS})<br />
    add_executable(foo foo.cc)<br />
        target_link_libraries(foo ${Boost_LIBRARIES})<br />
            endif()</p>
<p> The components list needs to contain actual names of boost libraries only, such as &quot;date_time&quot; for &quot;libboost_date_time&quot;. If you&#8217;re using parts of Boost that contain header files only (e.g. foreach) you do not need to specify COMPONENTS. </p>
<p> You should provide a minimum version number that should be used. If you provide this version number and specify the REQUIRED attribute, this module will fail if it can&#8217;t find the specified or a later version. If you specify a version number this is automatically put into the considered list of version numbers and thus doesn&#8217;t need to be specified in the Boost_ADDITIONAL_VERSIONS variable (see below). </p>
<p> NOTE for Visual Studio Users: </p>
<pre>
     Automatic linking is used on MSVC &amp; Borland compilers by default when
     #including things in Boost.  It's important to note that setting
     Boost_USE_STATIC_LIBS to OFF is NOT enough to get you dynamic linking,
     should you need this feature.  Automatic linking typically uses static
     libraries with a few exceptions (Boost.Python is one).
</pre>
<pre>
     Please see the section below near Boost_LIB_DIAGNOSTIC_DEFINITIONS for
     more details.  Adding a TARGET_LINK_LIBRARIES() as shown in the example
     above appears to cause VS to link dynamically if Boost_USE_STATIC_LIBS
     gets set to OFF.  It is suggested you avoid automatic linking since it
     will make your application less portable.
</pre>
<p> =========== The mess that is Boost_ADDITIONAL_VERSIONS (sorry?) ============ </p>
<p> OK, so the Boost_ADDITIONAL_VERSIONS variable can be used to specify a list of boost version numbers that should be taken into account when searching for Boost. Unfortunately boost puts the version number into the actual filename for the libraries, so this variable will certainly be needed in the future when new Boost versions are released. </p>
<p> Currently this module searches for the following version numbers: 1.33, 1.33.0, 1.33.1, 1.34, 1.34.0, 1.34.1, 1.35, 1.35.0, 1.35.1, 1.36, 1.36.0, 1.36.1, 1.37, 1.37.0, 1.38, 1.38.0 </p>
<p> NOTE: If you add a new major 1.x version in Boost_ADDITIONAL_VERSIONS you should add both 1.x and 1.x.0 as shown above. Official Boost include directories omit the 3rd version number from include paths if it is 0 although not all binary Boost releases do so. </p>
<p> SET(Boost_ADDITIONAL_VERSIONS &quot;0.99&quot; &quot;0.99.0&quot; &quot;1.78&quot; &quot;1.78.0&quot;) </p>
<p> ============================================================================ </p>
<p> Variables used by this module, they can change the default behaviour and need to be set before calling find_package: </p>
<pre>
   Boost_USE_MULTITHREADED      Can be set to OFF to use the non-multithreaded
                                boost libraries.  If not specified, defaults
                                to ON.
</pre>
<pre>
   Boost_USE_STATIC_LIBS        Can be set to ON to force the use of the static
                                boost libraries. Defaults to OFF.
</pre>
<p> Other Variables used by this module which you may want to set. </p>
<pre>
   Boost_ADDITIONAL_VERSIONS    A list of version numbers to use for searching
                                the boost include directory.  Please see
                                the documentation above regarding this
                                annoying, but necessary variable :(
</pre>
<pre>
   Boost_DEBUG                  Set this to TRUE to enable debugging output
                                of FindBoost.cmake if you are having problems.
                                Please enable this before filing any bug
                                reports.
</pre>
<pre>
   Boost_COMPILER               Set this to the compiler suffix used by Boost
                                (e.g. &quot;-gcc43&quot;) if FindBoost has problems finding
                                the proper Boost installation
</pre>
<p> These last three variables are available also as environment variables: </p>
<pre>
   BOOST_ROOT or BOOSTROOT      The preferred installation prefix for searching for
                                Boost.  Set this if the module has problems finding
                                the proper Boost installation.
</pre>
<pre>
   BOOST_INCLUDEDIR             Set this to the include directory of Boost, if the
                                module has problems finding the proper Boost installation
</pre>
<pre>
   BOOST_LIBRARYDIR             Set this to the lib directory of Boost, if the
                                module has problems finding the proper Boost installation
</pre>
<p> Variables defined by this module: </p>
<pre>
   Boost_FOUND                         System has Boost, this means the include dir was
                                       found, as well as all the libraries specified in
                                       the COMPONENTS list.
</pre>
<pre>
   Boost_INCLUDE_DIRS                  Boost include directories: not cached
</pre>
<pre>
   Boost_INCLUDE_DIR                   This is almost the same as above, but this one is
                                       cached and may be modified by advanced users
</pre>
<pre>
   Boost_LIBRARIES                     Link to these to use the Boost libraries that you
                                       specified: not cached
</pre>
<pre>
   Boost_LIBRARY_DIRS                  The path to where the Boost library files are.
</pre>
<pre>
   Boost_VERSION                       The version number of the boost libraries that
                                       have been found, same as in version.hpp from Boost
</pre>
<pre>
   Boost_LIB_VERSION                   The version number in filename form as
                                       it's appended to the library filenames
</pre>
<pre>
   Boost_MAJOR_VERSION                 major version number of boost
   Boost_MINOR_VERSION                 minor version number of boost
   Boost_SUBMINOR_VERSION              subminor version number of boost
</pre>
<p>Boost_LIB_DIAGNOSTIC_DEFINITIONS[WIN32 Only] You can call<br />
add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINTIIONS})<br />
    to have diagnostic information about Boost&#8217;s automatic linking outputted during compilation time.</p>
<p> For each component you specify in find_package(), the following (UPPER-CASE) variables are set. You can use these variables if you would like to pick and choose components for your targets instead of just using Boost_LIBRARIES. </p>
<pre>
   Boost_${COMPONENT}_FOUND            True IF the Boost library &quot;component&quot; was found.
</pre>
<pre>
   Boost_${COMPONENT}_LIBRARY          Contains the libraries for the specified Boost
                                       &quot;component&quot; (includes debug and optimized keywords
                                       when needed).
</pre>
<p> ===================================================================== </p>
<p>Copyright(c) 2006 &#8211; 2008 Andreas Schneider&lt;mail[at] cynapses.org&gt; Copyright(c) 2007 Wengo<br />
    Copyright(c) 2007 Mike Jackson<br />
    Copyright(c) 2008 Andreas Pakulat&lt;apaku[at] gmx.de&gt;</p>
<pre>
  Redistribution AND use is allowed according to the terms of the New
  BSD license.
  For details see the accompanying COPYING-CMAKE-SCRIPTS file.
</pre>
<dt><code>FindCABLE</code></p>
<dd> Find CABLE </p>
<p> This module finds if CABLE is installed and determines where the include files and libraries are. This code sets the following variables: </p>
<pre>
  CABLE             the path to the cable executable
  CABLE_TCL_LIBRARY the path to the Tcl wrapper library
  CABLE_INCLUDE_DIR the path to the include directory
</pre>
<p> To build Tcl wrappers, you should add shared library and link it to ${CABLE_TCL_LIBRARY}. You should also add ${CABLE_INCLUDE_DIR} as an include directory. </p>
<dt><code>FindCURL</code></p>
<dd> Find curl </p>
<p> Find the native CURL headers and libraries. </p>
<pre>
  CURL_INCLUDE_DIRS - where to find curl/curl.h, etc.
  CURL_LIBRARIES    - List of libraries when using curl.
  CURL_FOUND        - True if curl found.
</pre>
<dt><code>FindCVS</code></p>
<dd>
<p> The module defines the following variables: </p>
<pre>
   CVS_EXECUTABLE - path to cvs command line client
   CVS_FOUND - true if the command line client was found
</pre>
<p> Example usage: </p>
<p>find_package(CVS) if (CVS_FOUND)<br />
    message(&#8220;CVS found: ${CVS_EXECUTABLE}&#8221;)<br />
        endif(CVS_FOUND)</p>
<dt><code>FindCoin3D</code></p>
<dd> Find Coin3D (Open Inventor) </p>
<p> Coin3D is an implementation of the Open Inventor API. It provides data structures and algorithms for 3D visualization <a rel="nofollow" href="http://www.coin3d.org/">http://www.coin3d.org/</a> </p>
<p> This module defines the following variables </p>
<pre>
  COIN3D_FOUND         - system has Coin3D - Open Inventor
  COIN3D_INCLUDE_DIRS  - where the Inventor include directory can be found
  COIN3D_LIBRARIES     - Link to this to use Coin3D
</pre>
<dt><code>FindCups</code></p>
<dd> Try to find the Cups printing system </p>
<p> Once done this will define </p>
<pre>
  CUPS_FOUND - system has Cups
  CUPS_INCLUDE_DIR - the Cups include directory
  CUPS_LIBRARIES - Libraries needed to use Cups
  Set CUPS_REQUIRE_IPP_DELETE_ATTRIBUTE to TRUE if you need a version which 
  features this function (i.e. at least 1.1.19)
</pre>
<dt><code>FindCurses</code></p>
<dd> Find the curses include file and library </p>
<p>  CURSES_FOUND &#8211; system has Curses<br />
  CURSES_INCLUDE_DIR &#8211; the Curses include directory<br />
  CURSES_LIBRARIES &#8211; The libraries needed to use Curses<br />
  CURSES_HAVE_CURSES_H &#8211; true if curses.h is available<br />
  CURSES_HAVE_NCURSES_H &#8211; true if ncurses.h is available<br />
  CURSES_HAVE_NCURSES_NCURSES_H &#8211; true if ncurses/ncurses.h is available<br />
  CURSES_HAVE_NCURSES_CURSES_H &#8211; true if ncurses/curses.h is available<br />
  CURSES_LIBRARY &#8211; set for backwards compatibility with 2.4 CMake</p>
<p> Set CURSES_NEED_NCURSES to TRUE before the FIND_PACKAGE() command if NCurses functionality is required. </p>
<dt><code>FindCxxTest</code></p>
<dd> Find CxxTest </p>
<p> Find the CxxTest suite and declare a helper macro for creating unit tests and integrating them with CTest. For more details on CxxTest see <a rel="nofollow" href="http://cxxtest.tigris.org">http://cxxtest.tigris.org</a> </p>
<p> INPUT Variables </p>
<pre>
   CXXTEST_USE_PYTHON
       If true, the CXXTEST_ADD_TEST macro will use
       the Python test generator instead of Perl.
</pre>
<p> OUTPUT Variables </p>
<pre>
   CXXTEST_FOUND
       True if the CxxTest framework was found
   CXXTEST_INCLUDE_DIR
       Where to find the CxxTest include directory
   CXXTEST_PERL_TESTGEN_EXECUTABLE
       The perl-based test generator.
   CXXTEST_PYTHON_TESTGEN_EXECUTABLE
       The python-based test generator.
</pre>
<p> MACROS for use by CMake users: </p>
<p>CXXTEST_ADD_TEST(&lt;test_name&gt;&lt;gen_source_file&gt;&lt;input_files_to_testgen&#8230;&gt;)<br />
Creates a CxxTest runner and adds it to the CTest testing suite<br />
    Parameters : test_name The name of the test<br />
                     gen_source_file The generated source filename to be generated by CxxTest<br />
                         input_files_to_testgen The list of header files containing the<br />
                             CxxTest::TestSuite&#8217;s to be included in this runner</p>
<p>#== == == == == == ==<br />
                 Example Usage:</p>
<pre>
           FIND_PACKAGE(CxxTest)
           INCLUDE_DIRECTORIES(${CXXTEST_INCLUDE_DIR})
</pre>
<pre>
           ENABLE_TESTING()
           CXXTEST_ADD_TEST(unittest_foo foo_test.cc ${CMAKE_CURRENT_SOURCE_DIR}/foo_test.h)
</pre>
<pre>
              This will:
              1. Invoke the testgen executable to autogenerate foo_test.cc in the
                 binary tree from &quot;foo_test.h&quot; in the current source directory.
              2. Create an executable and test called unittest_foo.
               
      #=============
      Example foo_test.h:
</pre>
<p>#include &lt;cxxtest/TestSuite.h&gt;</p>
<p>class MyTestSuite : public CxxTest::TestSuite<br />
{<br />
  public:<br />
    void testAddition(void)<br />
    {<br />
        TS_ASSERT(1 + 1 &gt; 1);<br />
        TS_ASSERT_EQUALS(1 + 1, 2);<br />
    }<br />
};</p>
<p> FindCxxTest.cmake Copyright (c) 2008 </p>
<pre>
     Philip Lowman &lt;philip [at] yhbt.com&gt;
</pre>
<p> Version 1.0 (1/8/08) </p>
<pre>
     Fixed CXXTEST_INCLUDE_DIRS so it will work properly
     Eliminated superfluous CXXTEST_FOUND assignment
     Cleaned up and added more documentation
</pre>
<dt><code>FindCygwin</code></p>
<dd> this module looks for Cygwin </p>
<dt><code>FindDCMTK</code></p>
<dd> find DCMTK libraries </p>
<dt><code>FindDart</code></p>
<dd> Find DART </p>
<p> This module looks for the dart testing software and sets DART_ROOT to point to where it found it. </p>
<dt><code>FindDevIL</code></p>
<dd>
<p> This module locates the developer&#8217;s image library. <a rel="nofollow" href="http://openil.sourceforge.net/">http://openil.sourceforge.net/</a> </p>
<p> This module sets: IL_LIBRARY the name of the IL library. ILU_LIBRARY the name of the ILU library. ILUT_LIBRARY the name of the ILUT library. IL_INCLUDE_DIR where to find the il.h, ilu.h and ilut.h files. IL_FOUND this is set to TRUE if all the above variables were set. </p>
<dt><code>FindDoxygen</code></p>
<dd> This module looks for Doxygen and the path to Graphviz&#8217;s dot </p>
<p> Doxygen is a documentation generation tool. Please see <a rel="nofollow" href="http://www.doxygen.org">http://www.doxygen.org</a> </p>
<p> This module accepts the following optional variables: </p>
<pre>
   DOXYGEN_SKIP_DOT       = If true this module will skip trying to find Dot
                            (an optional component often used by Doxygen)
</pre>
<p> This modules defines the following variables: </p>
<pre>
   DOXYGEN_EXECUTABLE     = The path to the doxygen command.
   DOXYGEN_FOUND          = Was Doxygen found or not?
</pre>
<pre>
   DOXYGEN_DOT_EXECUTABLE = The path to the dot program used by doxygen.
   DOXYGEN_DOT_FOUND      = Was Dot found or not?
   DOXYGEN_DOT_PATH       = The path to dot not including the executable
</pre>
<dt><code>FindEXPAT</code></p>
<dd> Find expat </p>
<p> Find the native EXPAT headers and libraries. </p>
<pre>
  EXPAT_INCLUDE_DIRS - where to find expat.h, etc.
  EXPAT_LIBRARIES    - List of libraries when using expat.
  EXPAT_FOUND        - True if expat found.
</pre>
<dt><code>FindFLTK</code></p>
<dd> Find the native FLTK includes and library </p>
<p> By default FindFLTK.cmake will search for all of the FLTK components and add them to the FLTK_LIBRARIES variable. </p>
<pre>
   You can limit the components which get placed in FLTK_LIBRARIES by
   defining one or more of the following three options:
</pre>
<pre>
     FLTK_SKIP_OPENGL, set to true to disable searching for opengl and
                       the FLTK GL library
     FLTK_SKIP_FORMS, set to true to disable searching for fltk_forms
     FLTK_SKIP_IMAGES, set to true to disable searching for fltk_images
</pre>
<pre>
     FLTK_SKIP_FLUID, set to true if the fluid binary need not be present
                      at build time
</pre>
<p> The following variables will be defined: </p>
<pre>
     FLTK_FOUND, True if all components not skipped were found
     FLTK_INCLUDE_DIR, where to find include files
     FLTK_LIBRARIES, list of fltk libraries you should link against
     FLTK_FLUID_EXECUTABLE, where to find the Fluid tool
     FLTK_WRAP_UI, This enables the FLTK_WRAP_UI command
</pre>
<p> The following cache variables are assigned but should not be used. See the FLTK_LIBRARIES variable instead. </p>
<pre>
     FLTK_BASE_LIBRARY   = the full path to fltk.lib
     FLTK_GL_LIBRARY     = the full path to fltk_gl.lib
     FLTK_FORMS_LIBRARY  = the full path to fltk_forms.lib
     FLTK_IMAGES_LIBRARY = the full path to fltk_images.lib
</pre>
<dt><code>FindFLTK2</code></p>
<dd> Find the native FLTK2 includes and library </p>
<p> The following settings are defined </p>
<pre>
  FLTK2_FLUID_EXECUTABLE, where to find the Fluid tool
  FLTK2_WRAP_UI, This enables the FLTK2_WRAP_UI command
  FLTK2_INCLUDE_DIR, where to find include files
  FLTK2_LIBRARIES, list of fltk2 libraries
  FLTK2_FOUND, Don't use FLTK2 if false.
</pre>
<p> The following settings should not be used in general. </p>
<pre>
  FLTK2_BASE_LIBRARY   = the full path to fltk2.lib
  FLTK2_GL_LIBRARY     = the full path to fltk2_gl.lib
  FLTK2_IMAGES_LIBRARY = the full path to fltk2_images.lib
</pre>
<dt><code>FindFreetype</code></p>
<dd> Locate FreeType library </p>
<p> This module defines </p>
<pre>
  FREETYPE_LIBRARIES, the library to link against
  FREETYPE_FOUND, if false, do not try to link to FREETYPE
  FREETYPE_INCLUDE_DIRS, where to find headers.
  This is the concatenation of the paths:
  FREETYPE_INCLUDE_DIR_ft2build
  FREETYPE_INCLUDE_DIR_freetype2
</pre>
<p> $FREETYPE_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$FREETYPE_DIR used in building FREETYPE. </p>
<dt><code>FindGCCXML</code></p>
<dd> Find the GCC-XML front-end executable. </p>
<dt><code>FindGDAL</code></p>
<dd>
<p> Locate gdal </p>
<p> This module accepts the following environment variables: </p>
<pre>
    GDAL_DIR or GDAL_ROOT - Specify the location of GDAL
</pre>
<p> This module defines the following CMake variables: </p>
<pre>
    GDAL_FOUND - True if libgdal is found
    GDAL_LIBRARY - A variable pointing to the GDAL library
    GDAL_INCLUDE_DIR - Where to find the headers
</pre>
<p> $GDALDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$GDAL_DIR used in building gdal. </p>
<p> Created by Eric Wing. I&#8217;m not a gdal user, but OpenSceneGraph uses it for osgTerrain so I whipped this module together for completeness. I actually don&#8217;t know the conventions or where files are typically placed in distros. Any real gdal users are encouraged to correct this (but please don&#8217;t break the OS X framework stuff when doing so which is what usually seems to happen). </p>
<dt><code>FindGIF</code></p>
<dd>
<p> This module defines GIF_LIBRARIES &#8211; libraries to link to in order to use GIF GIF_FOUND, if false, do not try to link GIF_INCLUDE_DIR, where to find the headers </p>
<p> $GIF_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$GIF_DIR </p>
<dt><code>FindGLUT</code></p>
<dd> try to find glut library and include files </p>
<pre>
  GLUT_INCLUDE_DIR, where to find GL/glut.h, etc.
  GLUT_LIBRARIES, the libraries to link against
  GLUT_FOUND, If false, do not try to use GLUT.
</pre>
<p> Also defined, but not for general use are: </p>
<pre>
  GLUT_glut_LIBRARY = the full path to the glut library.
  GLUT_Xmu_LIBRARY  = the full path to the Xmu library.
  GLUT_Xi_LIBRARY   = the full path to the Xi Library.
</pre>
<dt><code>FindGTK</code></p>
<dd> try to find GTK (and glib) and GTKGLArea </p>
<pre>
  GTK_INCLUDE_DIR   - Directories to include to use GTK
  GTK_LIBRARIES     - Files to link against to use GTK
  GTK_FOUND         - GTK was found
  GTK_GL_FOUND      - GTK's GL features were found
</pre>
<dt><code>FindGettext</code></p>
<dd> Find GNU gettext tools </p>
<p> This module looks for the GNU gettext tools. This module defines the following values: </p>
<pre>
  GETTEXT_MSGMERGE_EXECUTABLE: the full path to the msgmerge tool.
  GETTEXT_MSGFMT_EXECUTABLE: the full path to the msgfmt tool.
  GETTEXT_FOUND: True if gettext has been found.
</pre>
<p> Additionally it provides the following macros: GETTEXT_CREATE_TRANSLATIONS ( outputFile [ALL] file1 &#8230; fileN ) </p>
<pre>
    This will create a target &quot;translations&quot; which will convert the 
    given input po files into the binary output mo file. If the 
    ALL option is used, the translations will also be created when
    building the default target.
</pre>
<dt><code>FindGnuplot</code></p>
<dd> this module looks for gnuplot </p>
<p> Once done this will define </p>
<pre>
  GNUPLOT_FOUND - system has Gnuplot
  GNUPLOT_EXECUTABLE - the Gnuplot executable
</pre>
<dt><code>FindHSPELL</code></p>
<dd> Try to find HSPELL </p>
<p> Once done this will define </p>
<pre>
  HSPELL_FOUND - system has HSPELL
  HSPELL_INCLUDE_DIR - the HSPELL include directory
  HSPELL_LIBRARIES - The libraries needed to use HSPELL
  HSPELL_DEFINITIONS - Compiler switches required for using HSPELL
</pre>
<dt><code>FindHTMLHelp</code></p>
<dd> This module looks for Microsoft HTML Help Compiler </p>
<p> It defines: </p>
<pre>
   HTML_HELP_COMPILER     : full path to the Compiler (hhc.exe)
   HTML_HELP_INCLUDE_PATH : include path to the API (htmlhelp.h)
   HTML_HELP_LIBRARY      : full path to the library (htmlhelp.lib)
</pre>
<dt><code>FindITK</code></p>
<dd> Find an ITK installation or build tree. </p>
<dt><code>FindImageMagick</code></p>
<dd> Find the ImageMagick binary suite. </p>
<p> This module will search for a set of ImageMagick tools specified as components in the FIND_PACKAGE call. Typical components include, but are not limited to (future versions of ImageMagick might have additional components not listed here): </p>
<pre>
  animate
  compare
  composite
  conjure
  convert
  display
  identify
  import
  mogrify
  montage
  stream
</pre>
<p> If no component is specified in the FIND_PACKAGE call, then it only searches for the ImageMagick executable directory. This code defines the following variables: </p>
<pre>
  ImageMagick_FOUND                  - TRUE if all components are found.
  ImageMagick_EXECUTABLE_DIR         - Full path to executables directory.
  ImageMagick_&lt;component&gt;_FOUND      - TRUE if &lt;component&gt; is found.
  ImageMagick_&lt;component&gt;_EXECUTABLE - Full path to &lt;component&gt; executable.
</pre>
<p> There are also components for the following ImageMagick APIs: </p>
<pre>
  Magick++
  MagickWand
  MagickCore
</pre>
<p> For these components the following variables are set: </p>
<p>ImageMagick_FOUND &#8211; TRUE if all components are found.ImageMagick_INCLUDE_DIRS &#8211; Full paths to all include dirs.ImageMagick_LIBRARIES &#8211; Full paths to all libraries.ImageMagick_&lt;component&gt; _FOUND &#8211; TRUE if&lt;component&gt; is found.ImageMagick_&lt;component&gt; _INCLUDE_DIRS &#8211; Full path to&lt;component&gt; include dirs.ImageMagick_&lt;component&gt; _LIBRARIES &#8211; Full path to&lt;component&gt; libraries.</p>
<p> Example Usages: </p>
<pre>
  FIND_PACKAGE(ImageMagick)
  FIND_PACKAGE(ImageMagick COMPONENTS convert)
  FIND_PACKAGE(ImageMagick COMPONENTS convert mogrify display)
  FIND_PACKAGE(ImageMagick COMPONENTS Magick++)
  FIND_PACKAGE(ImageMagick COMPONENTS Magick++ convert)
</pre>
<p> Note that the standard FIND_PACKAGE features are supported (i.e., QUIET, REQUIRED, etc.). </p>
<dt><code>FindJNI</code></p>
<dd> Find JNI java libraries. </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<p>JNI_INCLUDE_DIRS = the include dirs to use<br />
    JNI_LIBRARIES = the libraries to use<br />
        JAVA_AWT_LIBRARY = the path to the jawt library<br />
            JAVA_JVM_LIBRARY = the path to the jvm library<br />
                JAVA_INCLUDE_PATH = the include path to jni.h<br />
                                        JAVA_INCLUDE_PATH2 = the include path to jni_md.h<br />
                                                                 JAVA_AWT_INCLUDE_PATH = the include path to jawt.h</p>
<dt><code>FindJPEG</code></p>
<dd> Find JPEG </p>
<p> Find the native JPEG includes and library This module defines </p>
<pre>
  JPEG_INCLUDE_DIR, where to find jpeglib.h, etc.
  JPEG_LIBRARIES, the libraries needed to use JPEG.
  JPEG_FOUND, If false, do not try to use JPEG.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  JPEG_LIBRARY, where to find the JPEG library.
</pre>
<dt><code>FindJasper</code></p>
<dd> Try to find the Jasper JPEG2000 library </p>
<p> Once done this will define </p>
<pre>
  JASPER_FOUND - system has Jasper
  JASPER_INCLUDE_DIR - the Jasper include directory
  JASPER_LIBRARIES - The libraries needed to use Jasper
</pre>
<dt><code>FindJava</code></p>
<dd> Find Java </p>
<p> This module finds if Java is installed and determines where the include files and libraries are. This code sets the following variables: </p>
<pre>
  JAVA_RUNTIME    = the full path to the Java runtime
  JAVA_COMPILE    = the full path to the Java compiler
  JAVA_ARCHIVE    = the full path to the Java archiver
</pre>
<dt><code>FindKDE3</code></p>
<dd> Find the KDE3 include and library dirs, KDE preprocessors and define a some macros </p>
<p> This module defines the following variables: </p>
<p>  KDE3_DEFINITIONS         &#8211; compiler definitions required for compiling KDE software<br />
  KDE3_INCLUDE_DIR         &#8211; the KDE include directory<br />
  KDE3_INCLUDE_DIRS        &#8211; the KDE and the Qt include directory, for use with INCLUDE_DIRECTORIES()<br />
  KDE3_LIB_DIR             &#8211; the directory where the KDE libraries are installed, for use with LINK_DIRECTORIES()<br />
  QT_AND_KDECORE_LIBS      &#8211; this contains both the Qt and the kdecore library<br />
  KDE3_DCOPIDL_EXECUTABLE  &#8211; the dcopidl executable<br />
  KDE3_DCOPIDL2CPP_EXECUTABLE &#8211; the dcopidl2cpp executable<br />
  KDE3_KCFGC_EXECUTABLE    &#8211; the kconfig_compiler executable<br />
  KDE3_FOUND               &#8211; set to TRUE if all of the above has been found</p>
<p> The following user adjustable options are provided: </p>
<pre>
  KDE3_BUILD_TESTS - enable this to build KDE testcases
</pre>
<p> It also adds the following macros (from KDE3Macros.cmake) SRCS_VAR is always the variable which contains the list of source files for your application or library. </p>
<p> KDE3_AUTOMOC(file1 &#8230; fileN) </p>
<pre>
    Call this if you want to have automatic moc file handling.
    This means if you include &quot;foo.moc&quot; in the source file foo.cpp
    a moc file for the header foo.h will be created automatically.
    You can set the property SKIP_AUTOMAKE using SET_SOURCE_FILES_PROPERTIES()
    to exclude some files in the list from being processed.
</pre>
<p> KDE3_ADD_MOC_FILES(SRCS_VAR file1 &#8230; fileN ) </p>
<pre>
    If you don't use the KDE3_AUTOMOC() macro, for the files
    listed here moc files will be created (named &quot;foo.moc.cpp&quot;)
</pre>
<p> KDE3_ADD_DCOP_SKELS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>
    Use this to generate DCOP skeletions from the listed headers.
</pre>
<p> KDE3_ADD_DCOP_STUBS(SRCS_VAR header1.h &#8230; headerN.h ) </p>
<pre>
     Use this to generate DCOP stubs from the listed headers.
</pre>
<p> KDE3_ADD_UI_FILES(SRCS_VAR file1.ui &#8230; fileN.ui ) </p>
<pre>
    Use this to add the Qt designer ui files to your application/library.
</pre>
<p> KDE3_ADD_KCFG_FILES(SRCS_VAR file1.kcfgc &#8230; fileN.kcfgc ) </p>
<pre>
    Use this to add KDE kconfig compiler files to your application/library.
</pre>
<p> KDE3_INSTALL_LIBTOOL_FILE(target) </p>
<pre>
    This will create and install a simple libtool file for the given target.
</pre>
<p> KDE3_ADD_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>
    Currently identical to ADD_EXECUTABLE(), may provide some advanced features in the future.
</pre>
<p> KDE3_ADD_KPART(name [WITH_PREFIX] file1 &#8230; fileN ) </p>
<pre>
    Create a KDE plugin (KPart, kioslave, etc.) from the given source files.
    If WITH_PREFIX is given, the resulting plugin will have the prefix &quot;lib&quot;, otherwise it won't.
    It creates and installs an appropriate libtool la-file.
</pre>
<p> KDE3_ADD_KDEINIT_EXECUTABLE(name file1 &#8230; fileN ) </p>
<pre>
    Create a KDE application in the form of a module loadable via kdeinit.
    A library named kdeinit_&lt;name&gt; will be created and a small executable which links to it.
</pre>
<p> The option KDE3_ENABLE_FINAL to enable all-in-one compilation is no longer supported. </p>
<p> Author: Alexander Neundorf &lt;neundorf [at] kde.org&gt; </p>
<dt><code>FindKDE4</code></p>
<dd>
<p> Find KDE4 and provide all necessary variables and macros to compile software for it. It looks for KDE 4 in the following directories in the given order: </p>
<pre>
  CMAKE_INSTALL_PREFIX
  KDEDIRS
  /opt/kde4
</pre>
<p> Please look in FindKDE4Internal.cmake and KDE4Macros.cmake for more information. They are installed with the KDE 4 libraries in $KDEDIRS/share/apps/cmake/modules/. </p>
<p> Author: Alexander Neundorf &lt;neundorf [at] kde.org&gt; </p>
<dt><code>FindLAPACK</code></p>
<dd> Find LAPACK library </p>
<p> This module finds an installed fortran library that implements the LAPACK linear-algebra interface (see <a rel="nofollow" href="http://www.netlib.org/lapack/">http://www.netlib.org/lapack/</a>). </p>
<p> The approach follows that taken for the autoconf macro file, acx_lapack.m4 (distributed at <a rel="nofollow" href="http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html">http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html</a>). </p>
<p> This module sets the following variables: </p>
<p>  LAPACK_FOUND &#8211; set to true if a library implementing the LAPACK interface<br />
    is found<br />
  LAPACK_LINKER_FLAGS &#8211; uncached list of required linker flags (excluding -l<br />
    and -L).<br />
  LAPACK_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use LAPACK<br />
  LAPACK95_LIBRARIES &#8211; uncached list of libraries (using full path name) to<br />
    link against to use LAPACK95<br />
  LAPACK95_FOUND &#8211; set to true if a library implementing the LAPACK f95<br />
    interface is found<br />
  BLA_STATIC  if set on this determines what kind of linkage we do (static)<br />
  BLA_VENDOR  if set checks only the specified vendor, if not set checks<br />
     all the posibilities<br />
  BLA_F95     if set on tries to find the f95 interfaces for BLAS/LAPACK</p>
<p> ## List of vendors (BLA_VENDOR) valid in this module # Intel(mkl), ACML,Apple, NAS, Generic </p>
<dt><code>FindLATEX</code></p>
<dd> Find Latex </p>
<p> This module finds if Latex is installed and determines where the executables are. This code sets the following variables: </p>
<pre>
  
  LATEX_COMPILER:       path to the LaTeX compiler
  PDFLATEX_COMPILER:    path to the PdfLaTeX compiler
  BIBTEX_COMPILER:      path to the BibTeX compiler
  MAKEINDEX_COMPILER:   path to the MakeIndex compiler
  DVIPS_CONVERTER:      path to the DVIPS converter
  PS2PDF_CONVERTER:     path to the PS2PDF converter
  LATEX2HTML_CONVERTER: path to the LaTeX2Html converter 
</pre>
<dt><code>FindLibXml2</code></p>
<dd> Try to find LibXml2 </p>
<p> Once done this will define </p>
<pre>
  LIBXML2_FOUND - System has LibXml2
  LIBXML2_INCLUDE_DIR - The LibXml2 include directory
  LIBXML2_LIBRARIES - The libraries needed to use LibXml2
  LIBXML2_DEFINITIONS - Compiler switches required for using LibXml2
  LIBXML2_XMLLINT_EXECUTABLE - The XML checking tool xmllint coming with LibXml2
</pre>
<dt><code>FindLibXslt</code></p>
<dd> Try to find LibXslt </p>
<p> Once done this will define </p>
<pre>
  LIBXSLT_FOUND - system has LibXslt
  LIBXSLT_INCLUDE_DIR - the LibXslt include directory
  LIBXSLT_LIBRARIES - Link these to LibXslt
  LIBXSLT_DEFINITIONS - Compiler switches required for using LibXslt
</pre>
<dt><code>FindLua50</code></p>
<dd>
<p> Locate Lua library This module defines </p>
<pre>
  LUA50_FOUND, if false, do not try to link to Lua 
  LUA_LIBRARIES, both lua and lualib
  LUA_INCLUDE_DIR, where to find lua.h and lualib.h (and probably lauxlib.h)
</pre>
<p> Note that the expected include convention is </p>
<p>#include &#8220;lua.h&#8221;</p>
<p> and not </p>
<p>#include &lt;lua/lua.h&gt;</p>
<p> This is because, the lua location is not standardized and may exist in locations other than lua/ </p>
<dt><code>FindLua51</code></p>
<dd>
<p> Locate Lua library This module defines </p>
<pre>
  LUA51_FOUND, if false, do not try to link to Lua 
  LUA_LIBRARIES
  LUA_INCLUDE_DIR, where to find lua.h 
</pre>
<p> Note that the expected include convention is </p>
<p>#include &#8220;lua.h&#8221;</p>
<p> and not </p>
<p>#include &lt;lua/lua.h&gt;</p>
<p> This is because, the lua location is not standardized and may exist in locations other than lua/ </p>
<dt><code>FindMFC</code></p>
<dd> Find MFC on Windows </p>
<p> Find the native MFC &#8211; i.e. decide if an application can link to the MFC libraries. </p>
<pre>
  MFC_FOUND - Was MFC support found
</pre>
<p> You don&#8217;t need to include anything or link anything to use it. </p>
<dt><code>FindMPEG</code></p>
<dd> Find the native MPEG includes and library </p>
<p> This module defines </p>
<pre>
  MPEG_INCLUDE_DIR, where to find MPEG.h, etc.
  MPEG_LIBRARIES, the libraries required to use MPEG.
  MPEG_FOUND, If false, do not try to use MPEG.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  MPEG_mpeg2_LIBRARY, where to find the MPEG library.
  MPEG_vo_LIBRARY, where to find the vo library.
</pre>
<dt><code>FindMPEG2</code></p>
<dd> Find the native MPEG2 includes and library </p>
<p> This module defines </p>
<pre>
  MPEG2_INCLUDE_DIR, path to mpeg2dec/mpeg2.h, etc.
  MPEG2_LIBRARIES, the libraries required to use MPEG2.
  MPEG2_FOUND, If false, do not try to use MPEG2.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  MPEG2_mpeg2_LIBRARY, where to find the MPEG2 library.
  MPEG2_vo_LIBRARY, where to find the vo library.
</pre>
<dt><code>FindMPI</code></p>
<dd> Message Passing Interface (MPI) module. </p>
<p> The Message Passing Interface (MPI) is a library used to write high-performance parallel applications that use message passing, and is typically deployed on a cluster. MPI is a standard interface (defined by the MPI forum) for which many implementations are available. All of these implementations have somewhat different compilation approaches (different include paths, libraries to link against, etc.), and this module tries to smooth out those differences. </p>
<p> This module will set the following variables: </p>
<p>   MPI_FOUND                  TRUE if we have found MPI<br />
   MPI_COMPILE_FLAGS          Compilation flags for MPI programs<br />
   MPI_INCLUDE_PATH           Include path(s) for MPI header<br />
   MPI_LINK_FLAGS             Linking flags for MPI programs<br />
   MPI_LIBRARY                First MPI library to link against (cached)<br />
   MPI_EXTRA_LIBRARY Extra MPI libraries to link against(cached)<br />
   MPI_LIBRARIES              All libraries to link MPI programs against<br />
   MPIEXEC                    Executable for running MPI programs<br />
   MPIEXEC_NUMPROC_FLAG       Flag to pass to MPIEXEC before giving it the<br />
                              number of processors to run on<br />
   MPIEXEC_PREFLAGS           Flags to pass to MPIEXEC directly before the<br />
                              executable to run.<br />
   MPIEXEC_POSTFLAGS          Flags to pass to MPIEXEC after all other flags.</p>
<p> This module will attempt to auto-detect these settings, first by looking for a MPI compiler, which many MPI implementations provide as a pass-through to the native compiler to simplify the compilation of MPI programs. The MPI compiler is stored in the cache variable MPI_COMPILER, and will attempt to look for commonly-named drivers mpic++, mpicxx, mpiCC, or mpicc. If the compiler driver is found and recognized, it will be used to set all of the module variables. To skip this auto-detection, set MPI_LIBRARY and MPI_INCLUDE_PATH in the CMake cache. </p>
<p> If no compiler driver is found or the compiler driver is not recognized, this module will then search for common include paths and library names to try to detect MPI. </p>
<p> If CMake initially finds a different MPI than was intended, and you want to use the MPI compiler auto-detection for a different MPI implementation, set MPI_COMPILER to the MPI compiler driver you want to use (e.g., mpicxx) and then set MPI_LIBRARY to the string MPI_LIBRARY-NOTFOUND. When you re-configure, auto-detection of MPI will run again with the newly-specified MPI_COMPILER. </p>
<p> When using MPIEXEC to execute MPI applications, you should typically use all of the MPIEXEC flags as follows: </p>
<p>${MPIEXEC} ${MPIEXEC_NUMPROC_FLAG} PROCS ${MPIEXEC_PREFLAGS} EXECUTABLE<br />
    ${MPIEXEC_POSTFLAGS} ARGS</p>
<p> where PROCS is the number of processors on which to execute the program, EXECUTABLE is the MPI program, and ARGS are the arguments to pass to the MPI program. </p>
<dt><code>FindMatlab</code></p>
<dd> this module looks for Matlab </p>
<p> Defines: </p>
<pre>
  MATLAB_INCLUDE_DIR: include path for mex.h, engine.h
  MATLAB_LIBRARIES:   required libraries: libmex, etc
  MATLAB_MEX_LIBRARY: path to libmex.lib
  MATLAB_MX_LIBRARY:  path to libmx.lib
  MATLAB_ENG_LIBRARY: path to libeng.lib
</pre>
<dt><code>FindMotif</code></p>
<dd> Try to find Motif (or lesstif) </p>
<p> Once done this will define: </p>
<pre>
  MOTIF_FOUND        - system has MOTIF
  MOTIF_INCLUDE_DIR  - incude paths to use Motif
  MOTIF_LIBRARIES    - Link these to use Motif
</pre>
<dt><code>FindOpenAL</code></p>
<dd>
<p> Locate OpenAL This module defines OPENAL_LIBRARY OPENAL_FOUND, if false, do not try to link to OpenAL OPENAL_INCLUDE_DIR, where to find the headers </p>
<p> $OPENALDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENALDIR used in building OpenAL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module. </p>
<dt><code>FindOpenGL</code></p>
<dd> Try to find OpenGL </p>
<p> Once done this will define </p>
<pre>
  
  OPENGL_FOUND        - system has OpenGL
  OPENGL_XMESA_FOUND  - system has XMESA
  OPENGL_GLU_FOUND    - system has GLU
  OPENGL_INCLUDE_DIR  - the GL include directory
  OPENGL_LIBRARIES    - Link these to use OpenGL and GLU
   
</pre>
<p> If you want to use just GL you can use these values </p>
<pre>
  OPENGL_gl_LIBRARY   - Path to OpenGL Library
  OPENGL_glu_LIBRARY  - Path to GLU Library
  
</pre>
<p> On OSX default to using the framework version of opengl People will have to change the cache values of OPENGL_glu_LIBRARY and OPENGL_gl_LIBRARY to use OpenGL with X11 on OSX </p>
<dt><code>FindOpenMP</code></p>
<dd> Finds OpenMP support </p>
<p> This module can be used to detect OpenMP support in a compiler. If the compiler supports OpenMP, the flags required to compile with openmp support are set. </p>
<p> The following variables are set: </p>
<pre>
   OpenMP_C_FLAGS - flags to add to the C compiler for OpenMP support
   OpenMP_CXX_FLAGS - flags to add to the CXX compiler for OpenMP support
   OPENMP_FOUND - true if openmp is detected
</pre>
<p> Supported compilers can be found at <a rel="nofollow" href="http://openmp.org/wp/openmp-compilers/">http://openmp.org/wp/openmp-compilers/</a> </p>
<dt><code>FindOpenSSL</code></p>
<dd> Try to find the OpenSSL encryption library </p>
<p> Once done this will define </p>
<pre>
  OPENSSL_FOUND - system has the OpenSSL library
  OPENSSL_INCLUDE_DIR - the OpenSSL include directory
  OPENSSL_LIBRARIES - The libraries needed to use OpenSSL
</pre>
<dt><code>FindOpenSceneGraph</code></p>
<dd> Find OpenSceneGraph </p>
<p> This module searches for the OpenSceneGraph core &quot;osg&quot; library as well as OpenThreads, and whatever additional COMPONENTS that you specify. </p>
<pre>
    See <a rel="nofollow" href="http://www.openscenegraph.org">http://www.openscenegraph.org</a>
</pre>
<p> NOTE: If you would like to use this module in your CMAKE_MODULE_PATH instead of requiring CMake &gt;= 2.6.3, you will also need to download FindOpenThreads.cmake, Findosg_functions.cmake, Findosg.cmake, as well as files for any Components you need to call (FindosgDB.cmake, FindosgUtil.cmake, etc.) </p>
<p> ================================== </p>
<p> This module accepts the following variables (note mixed case) </p>
<pre>
    OpenSceneGraph_DEBUG - Enable debugging output
</pre>
<pre>
    OpenSceneGraph_MARK_AS_ADVANCED - Mark cache variables as advanced 
                                      automatically
</pre>
<p> The following environment variables are also respected for finding the OSG and it&#8217;s various components. CMAKE_PREFIX_PATH can also be used for this (see find_library() CMake documentation). </p>
<pre>
    &lt;MODULE&gt;_DIR (where MODULE is of the form &quot;OSGVOLUME&quot; and there is a FindosgVolume.cmake file)
    OSG_DIR
    OSGDIR
    OSG_ROOT
</pre>
<p> This module defines the following output variables: </p>
<pre>
    OPENSCENEGRAPH_FOUND - Was the OSG and all of the specified components found?
</pre>
<pre>
    OPENSCENEGRAPH_VERSION - The version of the OSG which was found
</pre>
<pre>
    OPENSCENEGRAPH_INCLUDE_DIRS - Where to find the headers
</pre>
<pre>
    OPENSCENEGRAPH_LIBRARIES - The OSG libraries
</pre>
<p> ================================== Example Usage: </p>
<pre>
  find_package(OpenSceneGraph 2.0.0 COMPONENTS osgDB osgUtil)
  include_directories(${OPENSCENEGRAPH_INCLUDE_DIRS})
</pre>
<pre>
  add_executable(foo foo.cc)
  target_link_libraries(foo ${OPENSCENEGRAPH_LIBRARIES})
</pre>
<p> ================================== </p>
<p> Naming convention: </p>
<pre>
  Local variables of the form _osg_foo
  Input variables of the form OpenSceneGraph_FOO
  Output variables of the form OPENSCENEGRAPH_FOO
</pre>
<p> Copyright (c) 2009, Philip Lowman &lt;philip [at] yhbt.com&gt; </p>
<p> Redistribution AND use is allowed according to the terms of the New BSD license. For details see the accompanying COPYING-CMAKE-SCRIPTS file. </p>
<p> ================================== </p>
<dt><code>FindOpenThreads</code></p>
<dd>
<p> OpenThreads is a C++ based threading library. Its largest userbase seems to OpenSceneGraph so you might notice I accept OSGDIR as an environment path. I consider this part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. </p>
<p> Locate OpenThreads This module defines OPENTHREADS_LIBRARY OPENTHREADS_FOUND, if false, do not try to link to OpenThreads OPENTHREADS_INCLUDE_DIR, where to find the headers </p>
<p> $OPENTHREADS_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OPENTHREADS_DIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindPHP4</code></p>
<dd> Find PHP4 </p>
<p> This module finds if PHP4 is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PHP4_INCLUDE_PATH       = path to where php.h can be found
  PHP4_EXECUTABLE         = full path to the php4 binary
</pre>
<dt><code>FindPNG</code></p>
<dd> Find the native PNG includes and library </p>
<p> This module defines </p>
<pre>
  PNG_INCLUDE_DIR, where to find png.h, etc.
  PNG_LIBRARIES, the libraries to link against to use PNG.
  PNG_DEFINITIONS - You should ADD_DEFINITONS(${PNG_DEFINITIONS}) before compiling code that includes png library files.
  PNG_FOUND, If false, do not try to use PNG.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  PNG_LIBRARY, where to find the PNG library.
</pre>
<p> None of the above will be defined unles zlib can be found. PNG depends on Zlib </p>
<dt><code>FindPackageHandleStandardArgs</code></p>
<dd>
<p> FIND_PACKAGE_HANDLE_STANDARD_ARGS(NAME (DEFAULT_MSG|&quot;Custom failure message&quot;) VAR1 &#8230; ) </p>
<pre>
    This macro is intended to be used in FindXXX.cmake modules files.
    It handles the REQUIRED and QUIET argument to FIND_PACKAGE() and
    it also sets the &lt;UPPERCASED_NAME&gt;_FOUND variable.
    The package is found if all variables listed are TRUE.
    Example:
</pre>
<pre>
    FIND_PACKAGE_HANDLE_STANDARD_ARGS(LibXml2 DEFAULT_MSG LIBXML2_LIBRARIES LIBXML2_INCLUDE_DIR)
</pre>
<pre>
    LibXml2 is considered to be found, if both LIBXML2_LIBRARIES and 
    LIBXML2_INCLUDE_DIR are valid. Then also LIBXML2_FOUND is set to TRUE.
    If it is not found and REQUIRED was used, it fails with FATAL_ERROR, 
    independent whether QUIET was used or not.
    If it is found, the location is reported using the VAR1 argument, so 
    here a message &quot;Found LibXml2: /usr/lib/libxml2.so&quot; will be printed out.
    If the second argument is DEFAULT_MSG, the message in the failure case will 
    be &quot;Could NOT find LibXml2&quot;, if you don't like this message you can specify
    your own custom failure message there.
</pre>
<dt><code>FindPackageMessage</code></p>
<dd>
<p> FIND_PACKAGE_MESSAGE(&lt;name&gt; &quot;message for user&quot; &quot;find result details&quot;) </p>
<p> This macro is intended to be used in FindXXX.cmake modules files. It will print a message once for each unique find result. This is useful for telling the user where a package was found. The first argument specifies the name (XXX) of the package. The second argument specifies the message to display. The third argument lists details about the find result so that if they change the message will be displayed again. The macro also obeys the QUIET argument to the find_package command. </p>
<p> Example: </p>
<p>IF(X11_FOUND)<br />
FIND_PACKAGE_MESSAGE(X11 &#8220;Found X11: ${X11_X11_LIB}&#8221;<br />
                         &#8220;[${X11_X11_LIB}][${X11_INCLUDE_DIR}]&#8221;)<br />
ELSE(X11_FOUND)<br />
&#8230; ENDIF(X11_FOUND)</p>
<dt><code>FindPerl</code></p>
<dd> Find perl </p>
<p> this module looks for Perl </p>
<pre>
  PERL_EXECUTABLE - the full path to perl
  PERL_FOUND      - If false, don't attempt to use perl.
</pre>
<dt><code>FindPerlLibs</code></p>
<dd> Find Perl libraries </p>
<p> This module finds if PERL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PERL_INCLUDE_PATH = path to where perl.h is found
  PERL_EXECUTABLE   = full path to the perl binary
</pre>
<dt><code>FindPhysFS</code></p>
<dd>
<p> Locate PhysFS library This module defines PHYSFS_LIBRARY, the name of the library to link against PHYSFS_FOUND, if false, do not try to link to PHYSFS PHYSFS_INCLUDE_DIR, where to find physfs.h </p>
<p> $PHYSFSDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PHYSFSDIR used in building PHYSFS. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindPike</code></p>
<dd> Find Pike </p>
<p> This module finds if PIKE is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PIKE_INCLUDE_PATH       = path to where program.h is found
  PIKE_EXECUTABLE         = full path to the pike binary
</pre>
<dt><code>FindPkgConfig</code></p>
<dd> a pkg-config module for CMake </p>
<p> Usage: </p>
<p>   pkg_check_modules(&lt;PREFIX&gt; [REQUIRED] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for all the given modules</p>
<p>   pkg_search_module(&lt;PREFIX&gt; [REQUIRED] &lt;MODULE&gt; [&lt;MODULE&gt;]*)<br />
     checks for given modules and uses the first working one</p>
<p> When the &#8216;REQUIRED&#8217; argument was set, macros will fail with an error when module(s) could not be found </p>
<p> It sets the following variables: </p>
<pre>
   PKG_CONFIG_FOUND         ... true if pkg-config works on the system
   PKG_CONFIG_EXECUTABLE    ... pathname of the pkg-config program
   &lt;PREFIX&gt;_FOUND           ... set to 1 if module(s) exist
</pre>
<p> For the following variables two sets of values exist; first one is the common one and has the given PREFIX. The second set contains flags which are given out when pkgconfig was called with the &#8216;&#8211;static&#8217; option. </p>
<pre>
   &lt;XPREFIX&gt;_LIBRARIES      ... only the libraries (w/o the '-l')
   &lt;XPREFIX&gt;_LIBRARY_DIRS   ... the paths of the libraries (w/o the '-L')
   &lt;XPREFIX&gt;_LDFLAGS        ... all required linker flags
   &lt;XPREFIX&gt;_LDFLAGS_OTHER  ... all other linker flags
   &lt;XPREFIX&gt;_INCLUDE_DIRS   ... the '-I' preprocessor flags (w/o the '-I')
   &lt;XPREFIX&gt;_CFLAGS         ... all required cflags
   &lt;XPREFIX&gt;_CFLAGS_OTHER   ... the other compiler flags
</pre>
<p>   &lt;XPREFIX&gt; = &lt;PREFIX&gt;        for common case<br />
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;_STATIC for static linking</p>
<p> There are some special variables whose prefix depends on the count of given modules. When there is only one module, &lt;PREFIX&gt; stays unchanged. When there are multiple modules, the prefix will be changed to &lt;PREFIX&gt;_&lt;MODNAME&gt;: </p>
<pre>
   &lt;XPREFIX&gt;_VERSION    ... version of the module
   &lt;XPREFIX&gt;_PREFIX     ... prefix-directory of the module
   &lt;XPREFIX&gt;_INCLUDEDIR ... include-dir of the module
   &lt;XPREFIX&gt;_LIBDIR     ... lib-dir of the module
</pre>
<pre>
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;  when |MODULES| == 1, else
   &lt;XPREFIX&gt; = &lt;PREFIX&gt;_&lt;MODNAME&gt;
</pre>
<p> A &lt;MODULE&gt; parameter can have the following formats: </p>
<p>{MODNAME}&#8230; matches any version{MODNAME} &gt;= {VERSION}&#8230; at least version&lt;VERSION&gt; is required{MODNAME} = {VERSION}&#8230; exactly version&lt;VERSION&gt; is required{MODNAME} &lt;= {VERSION}&#8230; modules must not be newer than&lt;VERSION&gt;</p>
<p> Examples </p>
<pre>
   pkg_check_modules (GLIB2   glib-2.0)
</pre>
<pre>
   pkg_check_modules (GLIB2   glib-2.0&gt;=2.10)
     requires at least version 2.10 of glib2 and defines e.g.
       GLIB2_VERSION=2.10.3
</pre>
<pre>
   pkg_check_modules (FOO     glib-2.0&gt;=2.10 gtk+-2.0)
     requires both glib2 and gtk2, and defines e.g.
       FOO_glib-2.0_VERSION=2.10.3
       FOO_gtk+-2.0_VERSION=2.8.20
</pre>
<p>pkg_check_modules(XRENDER REQUIRED xrender)<br />
    defines e.g. : XRENDER_LIBRARIES = Xrender;<br />
X11<br />
    XRENDER_STATIC_LIBRARIES = Xrender;<br />
X11;<br />
pthread;<br />
Xau;<br />
Xdmcp</p>
<pre>
   pkg_search_module (BAR     libxml-2.0 libxml2 libxml&gt;=2)
</pre>
<dt><code>FindProducer</code></p>
<dd>
<p> Though Producer isn&#8217;t directly part of OpenSceneGraph, its primary user is OSG so I consider this part of the Findosg* suite used to find OpenSceneGraph components. You&#8217;ll notice that I accept OSGDIR as an environment path. </p>
<p> Each component is separate and you must opt in to each module. You must also opt into OpenGL (and OpenThreads?) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate Producer This module defines PRODUCER_LIBRARY PRODUCER_FOUND, if false, do not try to link to Producer PRODUCER_INCLUDE_DIR, where to find the headers </p>
<p> $PRODUCER_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$PRODUCER_DIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindPythonInterp</code></p>
<dd> Find python interpreter </p>
<p> This module finds if Python interpreter is installed and determines where the executables are. This code sets the following variables: </p>
<pre>
  PYTHONINTERP_FOUND - Was the Python executable found
  PYTHON_EXECUTABLE  - path to the Python interpreter
</pre>
<dt><code>FindPythonLibs</code></p>
<dd> Find python libraries </p>
<p> This module finds if Python is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  PYTHONLIBS_FOUND     = have the Python libs been found
  PYTHON_LIBRARIES     = path to the python library
  PYTHON_INCLUDE_PATH  = path to where Python.h is found
  PYTHON_DEBUG_LIBRARIES = path to the debug library
</pre>
<dt><code>FindQt</code></p>
<dd> Searches for all installed versions of QT. </p>
<p> This should only be used if your project can work with multiple versions of QT. If not, you should just directly use FindQt4 or FindQt3. If multiple versions of QT are found on the machine, then The user must set the option DESIRED_QT_VERSION to the version they want to use. If only one version of qt is found on the machine, then the DESIRED_QT_VERSION is set to that version and the matching FindQt3 or FindQt4 module is included. Once the user sets DESIRED_QT_VERSION, then the FindQt3 or FindQt4 module is included. </p>
<pre>
  QT_REQUIRED if this is set to TRUE then if CMake can 
              not find QT4 or QT3 an error is raised 
              and a message is sent to the user.
</pre>
<pre>
  DESIRED_QT_VERSION OPTION is created
  QT4_INSTALLED is set to TRUE if qt4 is found.
  QT3_INSTALLED is set to TRUE if qt3 is found.
</pre>
<dt><code>FindQt3</code></p>
<dd> Locate Qt include paths and libraries </p>
<p> This module defines: </p>
<pre>
  QT_INCLUDE_DIR - where to find qt.h, etc.
  QT_LIBRARIES   - the libraries to link against to use Qt.
  QT_DEFINITIONS - definitions to use when
                   compiling code that uses Qt.
  QT_FOUND       - If false, don't try to use Qt.
</pre>
<p> If you need the multithreaded version of Qt, set QT_MT_REQUIRED to TRUE </p>
<p> Also defined, but not for general use are: </p>
<pre>
  QT_MOC_EXECUTABLE, where to find the moc tool.
  QT_UIC_EXECUTABLE, where to find the uic tool.
  QT_QT_LIBRARY, where to find the Qt library.
  QT_QTMAIN_LIBRARY, where to find the qtmain
   library. This is only required by Qt3 on Windows.
</pre>
<dt><code>FindQt4</code></p>
<dd> Find QT 4 </p>
<p> This module can be used to find Qt4. The most important issue is that the Qt4 qmake is available via the system path. This qmake is then used to detect basically everything else. This module defines a number of key variables and macros. The variable QT_USE_FILE is set which is the path to a CMake file that can be included to compile Qt 4 applications and libraries. It sets up the compilation environment for include directories, preprocessor defines and populates a QT_LIBRARIES variable. </p>
<p> Typical usage could be something like: </p>
<p>find_package(Qt4 4.4.3 COMPONENTS QtCore QtGui QtXml REQUIRED)<br />
    include(${QT_USE_FILE})<br />
        add_executable(myexe main.cpp)<br />
            target_link_libraries(myexe ${QT_LIBRARIES})</p>
<p> When using the components argument, QT_USE_QT* variables are automatically set for the QT_USE_FILE to pick up. If one wishes to manually set them, the available ones to set include: </p>
<pre>
                    QT_DONT_USE_QTCORE
                    QT_DONT_USE_QTGUI
                    QT_USE_QT3SUPPORT
                    QT_USE_QTASSISTANT
                    QT_USE_QAXCONTAINER
                    QT_USE_QAXSERVER
                    QT_USE_QTDESIGNER
                    QT_USE_QTMOTIF
                    QT_USE_QTMAIN
                    QT_USE_QTNETWORK
                    QT_USE_QTNSPLUGIN
                    QT_USE_QTOPENGL
                    QT_USE_QTSQL
                    QT_USE_QTXML
                    QT_USE_QTSVG
                    QT_USE_QTTEST
                    QT_USE_QTUITOOLS
                    QT_USE_QTDBUS
                    QT_USE_QTSCRIPT
                    QT_USE_QTASSISTANTCLIENT
                    QT_USE_QTHELP
                    QT_USE_QTWEBKIT
                    QT_USE_QTXMLPATTERNS
                    QT_USE_PHONON
</pre>
<p> There are also some files that need processing by some Qt tools such as moc and uic. Listed below are macros that may be used to process those files. </p>
<pre>
  
  macro QT4_WRAP_CPP(outfiles inputfile ... OPTIONS ...)
        create moc code from a list of files containing Qt class with
        the Q_OBJECT declaration.  Per-direcotry preprocessor definitions 
        are also added.  Options may be given to moc, such as those found
        when executing &quot;moc -help&quot;.  
</pre>
<pre>
  macro QT4_WRAP_UI(outfiles inputfile ... OPTIONS ...)
        create code from a list of Qt designer ui files.
        Options may be given to uic, such as those found
        when executing &quot;uic -help&quot;
</pre>
<pre>
  macro QT4_ADD_RESOURCES(outfiles inputfile ... OPTIONS ...)
        create code from a list of Qt resource files.
        Options may be given to rcc, such as those found
        when executing &quot;rcc -help&quot;
</pre>
<pre>
  macro QT4_GENERATE_MOC(inputfile outputfile )
        creates a rule to run moc on infile and create outfile.
        Use this if for some reason QT4_WRAP_CPP() isn't appropriate, e.g.
        because you need a custom filename for the moc file or something similar.
</pre>
<p>  macro QT4_AUTOMOC(sourcefile1 sourcefile2 &#8230; )<br />
        This macro is still experimental.<br />
        It can be used to have moc automatically handled.<br />
        So if you have the files foo.h and foo.cpp, and in foo.h a<br />
        a class uses the Q_OBJECT macro, moc has to run on it. If you don&#8217;t<br />
        want to use QT4_WRAP_CPP() (which is reliable and mature), you can insert<br />
#include &#8220;foo.moc&#8221;<br />
        in foo.cpp and then give foo.cpp as argument to QT4_AUTOMOC(). This will the<br />
        scan all listed files at cmake-time for such included moc files and if it finds<br />
        them cause a rule to be generated to run moc at build time on the<br />
        accompanying header file foo.h.<br />
        If a source file has the SKIP_AUTOMOC property set it will be ignored by this macro.</p>
<pre>
  macro QT4_ADD_DBUS_INTERFACE(outfiles interface basename)
        create a the interface header and implementation files with the 
        given basename from the given interface xml file and add it to 
        the list of sources
</pre>
<pre>
  macro QT4_ADD_DBUS_INTERFACES(outfiles inputfile ... )
        create the interface header and implementation files 
        for all listed interface xml files
        the name will be automatically determined from the name of the xml file
</pre>
<p>macro QT4_ADD_DBUS_ADAPTOR(outfiles xmlfile parentheader parentclassname[basename])<br />
    create a dbus adaptor(header and implementation file) from the xml file<br />
    describing the interface,<br />
    and add it to the list of sources.The adaptor<br />
        forwards the calls to a parent class,<br />
    defined in parentheader and named<br />
    parentclassname.The name of the generated files will be&lt;basename&gt; adaptor.{cpp, h} where basename is the basename of the xml file.</p>
<pre>
  macro QT4_GENERATE_DBUS_INTERFACE( header [interfacename] )
        generate the xml interface file from the given header.
        If the optional argument interfacename is omitted, the name of the 
        interface file is constructed from the basename of the header with
        the suffix .xml appended.
</pre>
<pre>
  macro QT4_CREATE_TRANSLATION( qm_files directories ... sources ... 
                                ts_files ... OPTIONS ...)
        out: qm_files
        in:  directories sources ts_files
        options: flags to pass to lupdate, such as -extensions to specify
        extensions for a directory scan.
        generates commands to create .ts (vie lupdate) and .qm
        (via lrelease) - files from directories and/or sources. The ts files are 
        created and/or updated in the source tree (unless given with full paths).
        The qm files are generated in the build tree.
        Updating the translations can be done by adding the qm_files
        to the source list of your library/executable, so they are
        always updated, or by adding a custom target to control when
        they get updated/generated.
</pre>
<pre>
  macro QT4_ADD_TRANSLATION( qm_files ts_files ... )
        out: qm_files
        in:  ts_files
        generates commands to create .qm from .ts - files. The generated
        filenames can be found in qm_files. The ts_files
        must exists and are not updated in any way.
</pre>
<pre>
  Below is a detailed list of variables that FindQt4.cmake sets.
  QT_FOUND         If false, don't try to use Qt.
  QT4_FOUND        If false, don't try to use Qt 4.
</pre>
<pre>
  QT_VERSION_MAJOR The major version of Qt found.
  QT_VERSION_MINOR The minor version of Qt found.
  QT_VERSION_PATCH The patch version of Qt found.
</pre>
<p>QT_EDITION Set to the edition of Qt(i.e.DesktopLight)<br />
        QT_EDITION_DESKTOPLIGHT True if QT_EDITION<br />
    == DesktopLight<br />
       QT_QTCORE_FOUND True if QtCore was found.QT_QTGUI_FOUND True if QtGui was found.QT_QT3SUPPORT_FOUND True if Qt3Support was found.QT_QTASSISTANT_FOUND True if QtAssistant was found.QT_QAXCONTAINER_FOUND True if QAxContainer was found(Windows only)<br />
           .QT_QAXSERVER_FOUND True if QAxServer was found(Windows only)<br />
           .QT_QTDBUS_FOUND True if QtDBus was found.QT_QTDESIGNER_FOUND True if QtDesigner was found.QT_QTDESIGNERCOMPONENTS True if QtDesignerComponents was found.QT_QTMOTIF_FOUND True if QtMotif was found.QT_QTNETWORK_FOUND True if QtNetwork was found.QT_QTNSPLUGIN_FOUND True if QtNsPlugin was found.QT_QTOPENGL_FOUND True if QtOpenGL was found.QT_QTSQL_FOUND True if QtSql was found.QT_QTXML_FOUND True if QtXml was found.QT_QTSVG_FOUND True if QtSvg was found.QT_QTSCRIPT_FOUND True if QtScript was found.QT_QTTEST_FOUND True if QtTest was found.QT_QTUITOOLS_FOUND True if QtUiTools was found.QT_QTASSISTANTCLIENT_FOUND True if QtAssistantClient was found.QT_QTHELP_FOUND True if QtHelp was found.QT_QTWEBKIT_FOUND True if QtWebKit was found.QT_QTXMLPATTERNS_FOUND True if QtXmlPatterns was found.QT_PHONON_FOUND True if phonon was found.</p>
<p>QT_DEFINITIONS Definitions to use when compiling code that uses Qt.You do not need to use this if you include QT_USE_FILE.The QT_USE_FILE will also define QT_DEBUG and QT_NO_DEBUG to fit your current build type.Those are not contained in QT_DEFINITIONS.</p>
<p>                                                                                                                                                                        QT_INCLUDES List of paths to all include directories of Qt4 QT_INCLUDE_DIR and<br />
    QT_QTCORE_INCLUDE_DIR are<br />
        always in this variable even if NOTFOUND,<br />
    all other INCLUDE_DIRS are<br />
        only added if they are found.You do not need to use this if you include QT_USE_FILE.</p>
<pre>
  Include directories for the Qt modules are listed here.
  You do not need to use these variables if you include QT_USE_FILE.
</pre>
<p>  QT_INCLUDE_DIR              Path to &#8220;include&#8221; of Qt4<br />
  QT_QT3SUPPORT_INCLUDE_DIR   Path to &#8220;include/Qt3Support&#8221;<br />
  QT_QTASSISTANT_INCLUDE_DIR  Path to &#8220;include/QtAssistant&#8221;<br />
  QT_QAXCONTAINER_INCLUDE_DIR  Path to &#8220;include/ActiveQt&#8221; (Windows only)<br />
  QT_QAXSERVER_INCLUDE_DIR  Path to &#8220;include/ActiveQt&#8221; (Windows only)<br />
  QT_QTCORE_INCLUDE_DIR       Path to &#8220;include/QtCore&#8221;<br />
  QT_QTDESIGNER_INCLUDE_DIR   Path to &#8220;include/QtDesigner&#8221;<br />
  QT_QTDESIGNERCOMPONENTS_INCLUDE_DIR   Path to &#8220;include/QtDesigner&#8221;<br />
  QT_QTDBUS_INCLUDE_DIR       Path to &#8220;include/QtDBus&#8221;<br />
  QT_QTGUI_INCLUDE_DIR        Path to &#8220;include/QtGui&#8221;<br />
  QT_QTMOTIF_INCLUDE_DIR      Path to &#8220;include/QtMotif&#8221;<br />
  QT_QTNETWORK_INCLUDE_DIR    Path to &#8220;include/QtNetwork&#8221;<br />
  QT_QTNSPLUGIN_INCLUDE_DIR   Path to &#8220;include/QtNsPlugin&#8221;<br />
  QT_QTOPENGL_INCLUDE_DIR     Path to &#8220;include/QtOpenGL&#8221;<br />
  QT_QTSQL_INCLUDE_DIR        Path to &#8220;include/QtSql&#8221;<br />
  QT_QTXML_INCLUDE_DIR        Path to &#8220;include/QtXml&#8221;<br />
  QT_QTSVG_INCLUDE_DIR        Path to &#8220;include/QtSvg&#8221;<br />
  QT_QTSCRIPT_INCLUDE_DIR     Path to &#8220;include/QtScript&#8221;<br />
  QT_QTTEST_INCLUDE_DIR       Path to &#8220;include/QtTest&#8221;<br />
  QT_QTASSISTANTCLIENT_INCLUDE_DIR       Path to &#8220;include/QtAssistant&#8221;<br />
  QT_QTHELP_INCLUDE_DIR       Path to &#8220;include/QtHelp&#8221;<br />
  QT_QTWEBKIT_INCLUDE_DIR     Path to &#8220;include/QtWebKit&#8221;<br />
  QT_QTXMLPATTERNS_INCLUDE_DIR  Path to &#8220;include/QtXmlPatterns&#8221;<br />
  QT_PHONON_INCLUDE_DIR       Path to &#8220;include/phonon&#8221;</p>
<p>  QT_BINARY_DIR               Path to &#8220;bin&#8221; of Qt4<br />
  QT_LIBRARY_DIR              Path to &#8220;lib&#8221; of Qt4<br />
  QT_PLUGINS_DIR              Path to &#8220;plugins&#8221; for Qt4<br />
  QT_TRANSLATIONS_DIR         Path to &#8220;translations&#8221; of Qt4<br />
  QT_DOC_DIR                  Path to &#8220;doc&#8221; of Qt4<br />
  QT_MKSPECS_DIR              Path to &#8220;mkspecs&#8221; of Qt4</p>
<p> The Qt toolkit may contain both debug and release libraries. In that case, the following library variables will contain both. You do not need to use these variables if you include QT_USE_FILE, and use QT_LIBRARIES. </p>
<pre>
  QT_QT3SUPPORT_LIBRARY            The Qt3Support library
  QT_QTASSISTANT_LIBRARY           The QtAssistant library
  QT_QAXCONTAINER_LIBRARY           The QAxContainer library (Windows only)
  QT_QAXSERVER_LIBRARY                The QAxServer library (Windows only)
  QT_QTCORE_LIBRARY                The QtCore library
  QT_QTDBUS_LIBRARY                The QtDBus library
  QT_QTDESIGNER_LIBRARY            The QtDesigner library
  QT_QTDESIGNERCOMPONENTS_LIBRARY  The QtDesignerComponents library
  QT_QTGUI_LIBRARY                 The QtGui library
  QT_QTMOTIF_LIBRARY               The QtMotif library
  QT_QTNETWORK_LIBRARY             The QtNetwork library
  QT_QTNSPLUGIN_LIBRARY            The QtNsPLugin library
  QT_QTOPENGL_LIBRARY              The QtOpenGL library
  QT_QTSQL_LIBRARY                 The QtSql library
  QT_QTXML_LIBRARY                 The QtXml library
  QT_QTSVG_LIBRARY                 The QtSvg library
  QT_QTSCRIPT_LIBRARY              The QtScript library
  QT_QTTEST_LIBRARY                The QtTest library
  QT_QTMAIN_LIBRARY                The qtmain library for Windows
  QT_QTUITOOLS_LIBRARY             The QtUiTools library
  QT_QTASSISTANTCLIENT_LIBRARY     The QtAssistantClient library
  QT_QTHELP_LIBRARY                The QtHelp library
  QT_QTWEBKIT_LIBRARY              The QtWebKit library
  QT_QTXMLPATTERNS_LIBRARY         The QtXmlPatterns library
  QT_PHONON_LIBRARY                The phonon library
  
</pre>
<p> also defined, but NOT for general use are </p>
<pre>
  QT_MOC_EXECUTABLE          Where to find the moc tool.
  QT_UIC_EXECUTABLE          Where to find the uic tool.
  QT_UIC3_EXECUTABLE         Where to find the uic3 tool.
  QT_RCC_EXECUTABLE          Where to find the rcc tool
  QT_DBUSCPP2XML_EXECUTABLE  Where to find the qdbuscpp2xml tool.
  QT_DBUSXML2CPP_EXECUTABLE  Where to find the qdbusxml2cpp tool.
  QT_LUPDATE_EXECUTABLE      Where to find the lupdate tool.
  QT_LRELEASE_EXECUTABLE     Where to find the lrelease tool.
  
</pre>
<p> These are around for backwards compatibility they will be set </p>
<pre>
  QT_WRAP_CPP  Set true if QT_MOC_EXECUTABLE is found
  QT_WRAP_UI   Set true if QT_UIC_EXECUTABLE is found
  
</pre>
<p> These variables do _NOT_ have any effect anymore (compared to FindQt.cmake) </p>
<pre>
  QT_MT_REQUIRED         Qt4 is now always multithreaded
  
</pre>
<p> These variables are set to &quot;&quot; Because Qt structure changed (They make no sense in Qt4) </p>
<pre>
  QT_QT_LIBRARY        Qt-Library is now split
</pre>
<dt><code>FindQuickTime</code></p>
<dd>
<p> Locate QuickTime This module defines QUICKTIME_LIBRARY QUICKTIME_FOUND, if false, do not try to link to gdal QUICKTIME_INCLUDE_DIR, where to find the headers </p>
<p> $QUICKTIME_DIR is an environment variable that would correspond to the ./configure &#8211;prefix=$QUICKTIME_DIR </p>
<p> Created by Eric Wing. </p>
<dt><code>FindRTI</code></p>
<dd> Try to find M&amp;S HLA RTI libraries </p>
<p> This module finds if any HLA RTI is installed and locates the standard RTI include files and libraries. </p>
<p> RTI is a simulation infrastructure standartized by IEEE and SISO. It has a well defined C++ API that assures that simulation applications are independent on a particular RTI implementation. <a rel="nofollow" href="http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)">http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)</a> </p>
<p> This code sets the following variables: </p>
<pre>
  RTI_INCLUDE_DIR = the directory where RTI includes file are found
  RTI_LIBRARIES = The libraries to link against to use RTI
  RTI_DEFINITIONS = -DRTI_USES_STD_FSTREAM
  RTI_FOUND = Set to FALSE if any HLA RTI was not found
</pre>
<p> Report problems to &lt;certi-devel [at] nongnu.org&gt; </p>
<dt><code>FindRuby</code></p>
<dd> Find Ruby </p>
<p> This module finds if Ruby is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  RUBY_INCLUDE_PATH = path to where ruby.h can be found
  RUBY_EXECUTABLE   = full path to the ruby binary
  RUBY_LIBRARY      = full path to the ruby library
</pre>
<dt><code>FindSDL</code></p>
<dd>
<p> Locate SDL library This module defines SDL_LIBRARY, the name of the library to link against SDL_FOUND, if false, do not try to link to SDL SDL_INCLUDE_DIR, where to find SDL.h </p>
<p> This module responds to the the flag: SDL_BUILDING_LIBRARY If this is defined, then no SDL_main will be linked in because only applications need main(). Otherwise, it is assumed you are building an application and this module will attempt to locate and set the the proper link flags as part of the returned SDL_LIBRARY variable. </p>
<p> Don&#8217;t forget to include SDLmain.h and SDLmain.m your project for the OS X framework based version. (Other versions link to -lSDLmain which this module will try to find on your behalf.) Also for OS X, this module will automatically add the -framework Cocoa on your behalf. </p>
<p> Additional Note: If you see an empty SDL_LIBRARY_TEMP in your configuration and no SDL_LIBRARY, it means CMake did not find your SDL library (SDL.dll, libsdl.so, SDL.framework, etc). Set SDL_LIBRARY_TEMP to point to your SDL library, and configure again. Similarly, if you see an empty SDLMAIN_LIBRARY, you should set this value as appropriate. These values are used to generate the final SDL_LIBRARY variable, but when these values are unset, SDL_LIBRARY does not get created. </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. l.e.galup 9-20-02 </p>
<p> Modified by Eric Wing. Added code to assist with automated building by using environmental variables and providing a more controlled/consistent search behavior. Added new modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). Also corrected the header search path to follow &quot;proper&quot; SDL guidelines. Added a search for SDLmain which is needed by some platforms. Added a search for threads which is needed by some platforms. Added needed compile switches for MinGW. </p>
<p> On OSX, this will prefer the Framework version (if found) over others. People will have to manually change the cache values of SDL_LIBRARY to override this selection or set the CMake environment CMAKE_INCLUDE_PATH to modify the search paths. </p>
<p> Note that the header path has changed from SDL/SDL.h to just SDL.h This needed to change because &quot;proper&quot; SDL convention is #include &quot;SDL.h&quot;, not &lt;<a href="file:/usr/include/SDL/SDL.h">SDL/SDL.h</a>&gt;. This is done for portability reasons because not all systems place things in SDL/ (see FreeBSD). </p>
<dt><code>FindSDL_image</code></p>
<dd>
<p> Locate SDL_image library This module defines SDLIMAGE_LIBRARY, the name of the library to link against SDLIMAGE_FOUND, if false, do not try to link to SDL SDLIMAGE_INCLUDE_DIR, where to find SDL/SDL.h </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_mixer</code></p>
<dd>
<p> Locate SDL_mixer library This module defines SDLMIXER_LIBRARY, the name of the library to link against SDLMIXER_FOUND, if false, do not try to link to SDL SDLMIXER_INCLUDE_DIR, where to find SDL/SDL.h </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_net</code></p>
<dd>
<p> Locate SDL_net library This module defines SDLNET_LIBRARY, the name of the library to link against SDLNET_FOUND, if false, do not try to link against SDLNET_INCLUDE_DIR, where to find the headers </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSDL_sound</code></p>
<dd>
<p> Locates the SDL_sound library </p>
<dt><code>FindSDL_ttf</code></p>
<dd>
<p> Locate SDL_ttf library This module defines SDLTTF_LIBRARY, the name of the library to link against SDLTTF_FOUND, if false, do not try to link to SDL SDLTTF_INCLUDE_DIR, where to find SDL/SDL.h </p>
<p> $SDLDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$SDLDIR used in building SDL. </p>
<p> Created by Eric Wing. This was influenced by the FindSDL.cmake module, but with modifications to recognize OS X frameworks and additional Unix paths (FreeBSD, etc). </p>
<dt><code>FindSWIG</code></p>
<dd> Find SWIG </p>
<p> This module finds an installed SWIG. It sets the following variables: </p>
<pre>
  SWIG_FOUND - set to true if SWIG is found
  SWIG_DIR - the directory where swig is installed
  SWIG_EXECUTABLE - the path to the swig executable
  SWIG_VERSION   - the version number of the swig executable
</pre>
<p> All informations are collected from the SWIG_EXECUTABLE so the version to be found can be changed from the command line by means of setting SWIG_EXECUTABLE </p>
<dt><code>FindSelfPackers</code></p>
<dd> Find upx </p>
<p> This module looks for some executable packers (i.e. softwares that compress executables or shared libs into on-the-fly self-extracting executables or shared libs. Examples: </p>
<pre>
  UPX: <a rel="nofollow" href="http://wildsau.idv.uni-linz.ac.at/mfx/upx.html">http://wildsau.idv.uni-linz.ac.at/mfx/upx.html</a>
</pre>
<dt><code>FindSquish</code></p>
<dd> &#8212; Typical Use </p>
<p> This module can be used to find Squish (currently support is aimed at version 3). </p>
<p> SQUISH_FOUND If false, don&#8217;t try to use Squish SQUISH_VERSION_MAJOR The major version of Squish found SQUISH_VERSION_MINOR The minor version of Squish found SQUISH_VERSION_PATCH The patch version of Squish found </p>
<p> SQUISH_INSTALL_DIR The Squish installation directory (containing bin, lib, etc) SQUISH_SERVER_EXECUTABLE The squishserver executable SQUISH_CLIENT_EXECUTABLE The squishrunner executable </p>
<p> SQUISH_INSTALL_DIR_FOUND Was the install directory found? SQUISH_SERVER_EXECUTABLE_FOUND Was the server executable found? SQUISH_CLIENT_EXECUTABLE_FOUND Was the client executable found? </p>
<p> macro SQUISH_ADD_TEST(testName applicationUnderTest testSuite testCase) </p>
<p> ENABLE_TESTING() FIND_PACKAGE(Squish) IF (SQUISH_FOUND) </p>
<pre>
   SQUISH_ADD_TEST(myTestName myApplication testSuiteName testCaseName)
</pre>
<p> ENDIF (SQUISH_FOUND) </p>
<dt><code>FindSubversion</code></p>
<dd> Extract information from a subversion working copy </p>
<p> The module defines the following variables: </p>
<pre>
  Subversion_SVN_EXECUTABLE - path to svn command line client
  Subversion_VERSION_SVN - version of svn command line client
  Subversion_FOUND - true if the command line client was found
</pre>
<p> If the command line client executable is found the macro </p>
<pre>
  Subversion_WC_INFO(&lt;dir&gt; &lt;var-prefix&gt;)
</pre>
<p> is defined to extract information of a subversion working copy at a given location. The macro defines the following variables: </p>
<pre>
  &lt;var-prefix&gt;_WC_URL - url of the repository (at &lt;dir&gt;)
  &lt;var-prefix&gt;_WC_ROOT - root url of the repository
  &lt;var-prefix&gt;_WC_REVISION - current revision
  &lt;var-prefix&gt;_WC_LAST_CHANGED_AUTHOR - author of last commit
  &lt;var-prefix&gt;_WC_LAST_CHANGED_DATE - date of last commit
  &lt;var-prefix&gt;_WC_LAST_CHANGED_REV - revision of last commit
  &lt;var-prefix&gt;_WC_LAST_CHANGED_LOG - last log of base revision
  &lt;var-prefix&gt;_WC_INFO - output of command `svn info &lt;dir&gt;'
</pre>
<p> Example usage: </p>
<p>FIND_PACKAGE(Subversion)<br />
IF(Subversion_FOUND)<br />
Subversion_WC_INFO(${PROJECT_SOURCE_DIR} Project)<br />
    MESSAGE(&#8220;Current revision is ${Project_WC_REVISION}&#8221;)<br />
        Subversion_WC_LOG(${PROJECT_SOURCE_DIR} Project)<br />
            MESSAGE(&#8220;Last changed log is ${Project_LAST_CHANGED_LOG}&#8221;)<br />
                ENDIF(Subversion_FOUND)</p>
<dt><code>FindTCL</code></p>
<dd> TK_INTERNAL_PATH was removed. </p>
<p> This module finds if Tcl is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TCL_FOUND              = Tcl was found
  TK_FOUND               = Tk was found
  TCLTK_FOUND            = Tcl and Tk were found
  TCL_LIBRARY            = path to Tcl library (tcl tcl80)
  TCL_INCLUDE_PATH       = path to where tcl.h can be found
  TCL_TCLSH              = path to tclsh binary (tcl tcl80)
  TK_LIBRARY             = path to Tk library (tk tk80 etc)
  TK_INCLUDE_PATH        = path to where tk.h can be found
  TK_WISH                = full path to the wish executable
</pre>
<p> In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>
   =&gt; they were only useful for people writing Tcl/Tk extensions.
   =&gt; these libs are not packaged by default with Tcl/Tk distributions. 
      Even when Tcl/Tk is built from source, several flavors of debug libs
      are created and there is no real reason to pick a single one
      specifically (say, amongst tcl84g, tcl84gs, or tcl84sgx). 
      Let's leave that choice to the user by allowing him to assign 
      TCL_LIBRARY to any Tcl library, debug or not.
   =&gt; this ended up being only a Win32 variable, and there is a lot of
      confusion regarding the location of this file in an installed Tcl/Tk
      tree anyway (see 8.5 for example). If you need the internal path at
      this point it is safer you ask directly where the *source* tree is
      and dig from there.
</pre>
<dt><code>FindTIFF</code></p>
<dd> Find TIFF library </p>
<p> Find the native TIFF includes and library This module defines </p>
<pre>
  TIFF_INCLUDE_DIR, where to find tiff.h, etc.
  TIFF_LIBRARIES, libraries to link against to use TIFF.
  TIFF_FOUND, If false, do not try to use TIFF.
</pre>
<p> also defined, but not for general use are </p>
<pre>
  TIFF_LIBRARY, where to find the TIFF library.
</pre>
<dt><code>FindTclStub</code></p>
<dd> TCL_STUB_LIBRARY_DEBUG and TK_STUB_LIBRARY_DEBUG were removed. </p>
<p> This module finds Tcl stub libraries. It first finds Tcl include files and libraries by calling FindTCL.cmake. How to Use the Tcl Stubs Library: </p>
<pre>
   <a rel="nofollow" href="http://tcl.activestate.com/doc/howto/stubs.html">http://tcl.activestate.com/doc/howto/stubs.html</a>
</pre>
<p> Using Stub Libraries: </p>
<pre>
   <a rel="nofollow" href="http://safari.oreilly.com/0130385603/ch48lev1sec3">http://safari.oreilly.com/0130385603/ch48lev1sec3</a>
</pre>
<p> This code sets the following variables: </p>
<pre>
  TCL_STUB_LIBRARY       = path to Tcl stub library
  TK_STUB_LIBRARY        = path to Tk stub library
  TTK_STUB_LIBRARY       = path to ttk stub library
</pre>
<p> In an effort to remove some clutter and clear up some issues for people who are not necessarily Tcl/Tk gurus/developpers, some variables were moved or removed. Changes compared to CMake 2.4 are: </p>
<pre>
   =&gt; these libs are not packaged by default with Tcl/Tk distributions. 
      Even when Tcl/Tk is built from source, several flavors of debug libs
      are created and there is no real reason to pick a single one
      specifically (say, amongst tclstub84g, tclstub84gs, or tclstub84sgx). 
      Let's leave that choice to the user by allowing him to assign 
      TCL_STUB_LIBRARY to any Tcl library, debug or not.
</pre>
<dt><code>FindTclsh</code></p>
<dd> Find tclsh </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TCLSH_FOUND = TRUE if tclsh has been found
  TCL_TCLSH = the path to the tclsh executable
</pre>
<p> In cygwin, look for the cygwin version first. Don&#8217;t look for it later to avoid finding the cygwin version on a Win32 build. </p>
<dt><code>FindThreads</code></p>
<dd> This module determines the thread library of the system. </p>
<p> The following variables are set </p>
<pre>
  CMAKE_THREAD_LIBS_INIT     - the thread library
  CMAKE_USE_SPROC_INIT       - are we using sproc?
  CMAKE_USE_WIN32_THREADS_INIT - using WIN32 threads?
  CMAKE_USE_PTHREADS_INIT    - are we using pthreads
  CMAKE_HP_PTHREADS_INIT     - are we using hp pthreads
</pre>
<dt><code>FindUnixCommands</code></p>
<dd> Find unix commands from cygwin </p>
<p> This module looks for some usual Unix commands. </p>
<dt><code>FindVTK</code></p>
<dd> Find a VTK installation or build tree. </p>
<p> The following variables are set if VTK is found. If VTK is not found, VTK_FOUND is set to false. </p>
<pre>
  VTK_FOUND         - Set to true when VTK is found.
  VTK_USE_FILE      - CMake file to use VTK.
  VTK_MAJOR_VERSION - The VTK major version number.
  VTK_MINOR_VERSION - The VTK minor version number 
                       (odd non-release).
  VTK_BUILD_VERSION - The VTK patch level 
                       (meaningless for odd minor).
  VTK_INCLUDE_DIRS  - Include directories for VTK
  VTK_LIBRARY_DIRS  - Link directories for VTK libraries
  VTK_KITS          - List of VTK kits, in CAPS 
                      (COMMON,IO,) etc.
  VTK_LANGUAGES     - List of wrapped languages, in CAPS
                      (TCL, PYHTON,) etc.
</pre>
<p> The following cache entries must be set by the user to locate VTK: </p>
<pre>
  VTK_DIR  - The directory containing VTKConfig.cmake.  
             This is either the root of the build tree,
             or the lib/vtk directory.  This is the 
             only cache entry.
</pre>
<p> The following variables are set for backward compatibility and should not be used in new code: </p>
<pre>
  USE_VTK_FILE - The full path to the UseVTK.cmake file.
                 This is provided for backward 
                 compatibility.  Use VTK_USE_FILE 
                 instead.
</pre>
<dt><code>FindWget</code></p>
<dd> Find wget </p>
<p> This module looks for wget. This module defines the following values: </p>
<pre>
  WGET_EXECUTABLE: the full path to the wget tool.
  WGET_FOUND: True if wget has been found.
</pre>
<dt><code>FindWish</code></p>
<dd> Find wish installation </p>
<p> This module finds if TCL is installed and determines where the include files and libraries are. It also determines what the name of the library is. This code sets the following variables: </p>
<pre>
  TK_WISH = the path to the wish executable
</pre>
<p> if UNIX is defined, then it will look for the cygwin version first </p>
<dt><code>FindX11</code></p>
<dd> Find X11 installation </p>
<p> Try to find X11 on UNIX systems. The following values are defined </p>
<pre>
  X11_FOUND        - True if X11 is available
  X11_INCLUDE_DIR  - include directories to use X11
  X11_LIBRARIES    - link against these to use X11
</pre>
<p> and also the following more fine grained variables: Include paths: X11_ICE_INCLUDE_PATH, X11_ICE_LIB, X11_ICE_FOUND </p>
<pre>
                X11_Xaccessrules_INCLUDE_PATH,                     X11_Xaccess_FOUND
                X11_Xaccessstr_INCLUDE_PATH,                       X11_Xaccess_FOUND
                X11_Xau_INCLUDE_PATH,          X11_Xau_LIB,        X11_Xau_FOUND
                X11_Xcomposite_INCLUDE_PATH,   X11_Xcomposite_LIB, X11_Xcomposite_FOUND
                X11_Xcursor_INCLUDE_PATH,      X11_Xcursor_LIB,    X11_Xcursor_FOUND
                X11_Xdamage_INCLUDE_PATH,      X11_Xdamage_LIB,    X11_Xdamage_FOUND
                X11_Xdmcp_INCLUDE_PATH,        X11_Xdmcp_LIB,      X11_Xdmcp_FOUND
                                               X11_Xext_LIB,       X11_Xext_FOUND
                X11_dpms_INCLUDE_PATH,         (in X11_Xext_LIB),  X11_dpms_FOUND
                X11_XShm_INCLUDE_PATH,         (in X11_Xext_LIB),  X11_XShm_FOUND
                X11_Xshape_INCLUDE_PATH,       (in X11_Xext_LIB),  X11_Xshape_FOUND
                X11_xf86misc_INCLUDE_PATH,     X11_Xxf86misc_LIB,  X11_xf86misc_FOUND
                X11_xf86vmode_INCLUDE_PATH,                        X11_xf86vmode_FOUND
                X11_Xfixes_INCLUDE_PATH,       X11_Xfixes_LIB,     X11_Xfixes_FOUND
                X11_Xft_INCLUDE_PATH,          X11_Xft_LIB,        X11_Xft_FOUND
                X11_Xinerama_INCLUDE_PATH,     X11_Xinerama_LIB,   X11_Xinerama_FOUND
                X11_Xinput_INCLUDE_PATH,       X11_Xinput_LIB,     X11_Xinput_FOUND
                X11_Xkb_INCLUDE_PATH,                              X11_Xkb_FOUND
                X11_Xkblib_INCLUDE_PATH,                           X11_Xkb_FOUND
                X11_Xpm_INCLUDE_PATH,          X11_Xpm_LIB,        X11_Xpm_FOUND
                X11_XTest_INCLUDE_PATH,        X11_XTest_LIB,      X11_XTest_FOUND
                X11_Xrandr_INCLUDE_PATH,       X11_Xrandr_LIB,     X11_Xrandr_FOUND
                X11_Xrender_INCLUDE_PATH,      X11_Xrender_LIB,    X11_Xrender_FOUND
                X11_Xscreensaver_INCLUDE_PATH, X11_Xscreensaver_LIB, X11_Xscreensaver_FOUND
                X11_Xt_INCLUDE_PATH,           X11_Xt_LIB,         X11_Xt_FOUND
                X11_Xutil_INCLUDE_PATH,                            X11_Xutil_FOUND
                X11_Xv_INCLUDE_PATH,           X11_Xv_LIB,         X11_Xv_FOUND
</pre>
<dt><code>FindXMLRPC</code></p>
<dd> Find xmlrpc </p>
<p> Find the native XMLRPC headers and libraries. </p>
<pre>
  XMLRPC_INCLUDE_DIRS      - where to find xmlrpc.h, etc.
  XMLRPC_LIBRARIES         - List of libraries when using xmlrpc.
  XMLRPC_FOUND             - True if xmlrpc found.
</pre>
<p> XMLRPC modules may be specified as components for this find module. Modules may be listed by running &quot;xmlrpc-c-config&quot;. Modules include: </p>
<pre>
  c++            C++ wrapper code
  libwww-client  libwww-based client
  cgi-server     CGI-based server
  abyss-server   ABYSS-based server
</pre>
<p> Typical usage: </p>
<pre>
  FIND_PACKAGE(XMLRPC REQUIRED libwww-client)
</pre>
<dt><code>FindZLIB</code></p>
<dd> Find zlib </p>
<p> Find the native ZLIB includes and library </p>
<pre>
  ZLIB_INCLUDE_DIR - where to find zlib.h, etc.
  ZLIB_LIBRARIES   - List of libraries when using zlib.
  ZLIB_FOUND       - True if zlib found.
</pre>
<dt><code>Findosg</code></p>
<dd>
<p> NOTE: It is highly recommended that you use the new FindOpenSceneGraph.cmake introduced in CMake 2.6.3 and not use this Find module directly. </p>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osg This module defines </p>
<p> OSG_FOUND &#8211; Was the Osg found? OSG_INCLUDE_DIR &#8211; Where to find the headers OSG_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSG_LIBRARY &#8211; The OSG library OSG_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgAnimation</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgAnimation This module defines </p>
<p> OSGANIMATION_FOUND &#8211; Was osgAnimation found? OSGANIMATION_INCLUDE_DIR &#8211; Where to find the headers OSGANIMATION_LIBRARIES &#8211; The libraries to link against for the OSG (use this) </p>
<p> OSGANIMATION_LIBRARY &#8211; The OSG library OSGANIMATION_LIBRARY_DEBUG &#8211; The OSG debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgDB</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgDB This module defines </p>
<p> OSGDB_FOUND &#8211; Was osgDB found? OSGDB_INCLUDE_DIR &#8211; Where to find the headers OSGDB_LIBRARIES &#8211; The libraries to link against for the osgDB (use this) </p>
<p> OSGDB_LIBRARY &#8211; The osgDB library OSGDB_LIBRARY_DEBUG &#8211; The osgDB debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgFX</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgFX This module defines </p>
<p> OSGFX_FOUND &#8211; Was osgFX found? OSGFX_INCLUDE_DIR &#8211; Where to find the headers OSGFX_LIBRARIES &#8211; The libraries to link against for the osgFX (use this) </p>
<p> OSGFX_LIBRARY &#8211; The osgFX library OSGFX_LIBRARY_DEBUG &#8211; The osgFX debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgGA</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgGA This module defines </p>
<p> OSGGA_FOUND &#8211; Was osgGA found? OSGGA_INCLUDE_DIR &#8211; Where to find the headers OSGGA_LIBRARIES &#8211; The libraries to link against for the osgGA (use this) </p>
<p> OSGGA_LIBRARY &#8211; The osgGA library OSGGA_LIBRARY_DEBUG &#8211; The osgGA debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgIntrospection</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgINTROSPECTION This module defines </p>
<p> OSGINTROSPECTION_FOUND &#8211; Was osgIntrospection found? OSGINTROSPECTION_INCLUDE_DIR &#8211; Where to find the headers OSGINTROSPECTION_LIBRARIES &#8211; The libraries to link for osgIntrospection (use this) </p>
<p> OSGINTROSPECTION_LIBRARY &#8211; The osgIntrospection library OSGINTROSPECTION_LIBRARY_DEBUG &#8211; The osgIntrospection debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgManipulator</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgManipulator This module defines </p>
<p> OSGMANIPULATOR_FOUND &#8211; Was osgManipulator found? OSGMANIPULATOR_INCLUDE_DIR &#8211; Where to find the headers OSGMANIPULATOR_LIBRARIES &#8211; The libraries to link for osgManipulator (use this) </p>
<p> OSGMANIPULATOR_LIBRARY &#8211; The osgManipulator library OSGMANIPULATOR_LIBRARY_DEBUG &#8211; The osgManipulator debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgParticle</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgParticle This module defines </p>
<p> OSGPARTICLE_FOUND &#8211; Was osgParticle found? OSGPARTICLE_INCLUDE_DIR &#8211; Where to find the headers OSGPARTICLE_LIBRARIES &#8211; The libraries to link for osgParticle (use this) </p>
<p> OSGPARTICLE_LIBRARY &#8211; The osgParticle library OSGPARTICLE_LIBRARY_DEBUG &#8211; The osgParticle debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgProducer</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgProducer This module defines </p>
<p> OSGPRODUCER_FOUND &#8211; Was osgProducer found? OSGPRODUCER_INCLUDE_DIR &#8211; Where to find the headers OSGPRODUCER_LIBRARIES &#8211; The libraries to link for osgProducer (use this) </p>
<p> OSGPRODUCER_LIBRARY &#8211; The osgProducer library OSGPRODUCER_LIBRARY_DEBUG &#8211; The osgProducer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgShadow</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgShadow This module defines </p>
<p> OSGSHADOW_FOUND &#8211; Was osgShadow found? OSGSHADOW_INCLUDE_DIR &#8211; Where to find the headers OSGSHADOW_LIBRARIES &#8211; The libraries to link for osgShadow (use this) </p>
<p> OSGSHADOW_LIBRARY &#8211; The osgShadow library OSGSHADOW_LIBRARY_DEBUG &#8211; The osgShadow debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgSim</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgSim This module defines </p>
<p> OSGSIM_FOUND &#8211; Was osgSim found? OSGSIM_INCLUDE_DIR &#8211; Where to find the headers OSGSIM_LIBRARIES &#8211; The libraries to link for osgSim (use this) </p>
<p> OSGSIM_LIBRARY &#8211; The osgSim library OSGSIM_LIBRARY_DEBUG &#8211; The osgSim debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgTerrain</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgTerrain This module defines </p>
<p> OSGTERRAIN_FOUND &#8211; Was osgTerrain found? OSGTERRAIN_INCLUDE_DIR &#8211; Where to find the headers OSGTERRAIN_LIBRARIES &#8211; The libraries to link for osgTerrain (use this) </p>
<p> OSGTERRAIN_LIBRARY &#8211; The osgTerrain library OSGTERRAIN_LIBRARY_DEBUG &#8211; The osgTerrain debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgText</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgText This module defines </p>
<p> OSGTEXT_FOUND &#8211; Was osgText found? OSGTEXT_INCLUDE_DIR &#8211; Where to find the headers OSGTEXT_LIBRARIES &#8211; The libraries to link for osgText (use this) </p>
<p> OSGTEXT_LIBRARY &#8211; The osgText library OSGTEXT_LIBRARY_DEBUG &#8211; The osgText debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgUtil</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgUtil This module defines </p>
<p> OSGUTIL_FOUND &#8211; Was osgUtil found? OSGUTIL_INCLUDE_DIR &#8211; Where to find the headers OSGUTIL_LIBRARIES &#8211; The libraries to link for osgUtil (use this) </p>
<p> OSGUTIL_LIBRARY &#8211; The osgUtil library OSGUTIL_LIBRARY_DEBUG &#8211; The osgUtil debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgViewer</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgViewer This module defines </p>
<p> OSGVIEWER_FOUND &#8211; Was osgViewer found? OSGVIEWER_INCLUDE_DIR &#8211; Where to find the headers OSGVIEWER_LIBRARIES &#8211; The libraries to link for osgViewer (use this) </p>
<p> OSGVIEWER_LIBRARY &#8211; The osgViewer library OSGVIEWER_LIBRARY_DEBUG &#8211; The osgViewer debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgVolume</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgVolume This module defines </p>
<p> OSGVOLUME_FOUND &#8211; Was osgVolume found? OSGVOLUME_INCLUDE_DIR &#8211; Where to find the headers OSGVOLUME_LIBRARIES &#8211; The libraries to link for osgVolume (use this) </p>
<p> OSGVOLUME_LIBRARY &#8211; The osgVolume library OSGVOLUME_LIBRARY_DEBUG &#8211; The osgVolume debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> Created by Eric Wing. </p>
<dt><code>FindosgWidget</code></p>
<dd>
<p> This is part of the Findosg* suite used to find OpenSceneGraph components. Each component is separate and you must opt in to each module. You must also opt into OpenGL and OpenThreads (and Producer if needed) as these modules won&#8217;t do it for you. This is to allow you control over your own system piece by piece in case you need to opt out of certain components or change the Find behavior for a particular module (perhaps because the default FindOpenGL.cmake module doesn&#8217;t work with your system as an example). If you want to use a more convenient module that includes everything, use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake modules. </p>
<p> Locate osgWidget This module defines </p>
<p> OSGWIDGET_FOUND &#8211; Was osgWidget found? OSGWIDGET_INCLUDE_DIR &#8211; Where to find the headers OSGWIDGET_LIBRARIES &#8211; The libraries to link for osgWidget (use this) </p>
<p> OSGWIDGET_LIBRARY &#8211; The osgWidget library OSGWIDGET_LIBRARY_DEBUG &#8211; The osgWidget debug library </p>
<p> $OSGDIR is an environment variable that would correspond to the ./configure &#8211;prefix=$OSGDIR used in building osg. </p>
<p> FindosgWidget.cmake tweaked from Findosg* suite as created by Eric Wing. </p>
<dt><code>Findosg_functions</code></p>
<dd>
<p> This CMake file contains two macros to assist with searching for OSG libraries and nodekits. </p>
<dt><code>FindwxWidgets</code></p>
<dd> Find a wxWidgets (a.k.a., wxWindows) installation. </p>
<p> This module finds if wxWidgets is installed and selects a default configuration to use. wxWidgets is a modular library. To specify the modules that you will use, you need to name them as components to the package: </p>
<p> FIND_PACKAGE(wxWidgets COMPONENTS base core &#8230;) </p>
<p> There are two search branches: a windows style and a unix style. For windows, the following variables are searched for and set to defaults in case of multiple choices. Change them if the defaults are not desired (i.e., these are the only variables you should change to select a configuration): </p>
<pre>
  wxWidgets_ROOT_DIR      - Base wxWidgets directory
                            (e.g., C:/wxWidgets-2.6.3).
  wxWidgets_LIB_DIR       - Path to wxWidgets libraries
                            (e.g., C:/wxWidgets-2.6.3/lib/vc_lib).
  wxWidgets_CONFIGURATION - Configuration to use
                            (e.g., msw, mswd, mswu, mswunivud, etc.)
</pre>
<p> For unix style it uses the wx-config utility. You can select between debug/release, unicode/ansi, universal/non-universal, and static/shared in the QtDialog or ccmake interfaces by turning ON/OFF the following variables: </p>
<pre>
  wxWidgets_USE_DEBUG
  wxWidgets_USE_UNICODE
  wxWidgets_USE_UNIVERSAL
  wxWidgets_USE_STATIC
  
</pre>
<p> The following are set after the configuration is done for both windows and unix style: </p>
<p>  wxWidgets_FOUND            &#8211; Set to TRUE if wxWidgets was found.<br />
  wxWidgets_INCLUDE_DIRS     &#8211; Include directories for WIN32<br />
                               i.e., where to find &#8220;wx/wx.h&#8221; and<br />
                               &#8220;wx/setup.h&#8221;; possibly empty for unices.<br />
  wxWidgets_LIBRARIES        &#8211; Path to the wxWidgets libraries.<br />
  wxWidgets_LIBRARY_DIRS     &#8211; compile time link dirs, useful for<br />
                               rpath on UNIX. Typically an empty string<br />
                               in WIN32 environment.<br />
  wxWidgets_DEFINITIONS      &#8211; Contains defines required to compile/link<br />
                               against WX, e.g. -DWXUSINGDLL<br />
  wxWidgets_CXX_FLAGS        &#8211; Include dirs and ompiler flags for<br />
                               unices, empty on WIN32. Esentially<br />
                               &#8220;`wx-config &#8211;cxxflags`&#8221;.<br />
  wxWidgets_USE_FILE         &#8211; Convenience include file.</p>
<p> Sample usage: </p>
<p>FIND_PACKAGE(wxWidgets COMPONENTS base core gl net)<br />
IF(wxWidgets_FOUND)<br />
INCLUDE(${wxWidgets_USE_FILE})<br />
#and for each of your dependant executable / library targets:<br />
TARGET_LINK_LIBRARIES(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})<br />
ENDIF(wxWidgets_FOUND)</p>
<p> If wxWidgets is required (i.e., not an optional part): </p>
<p>FIND_PACKAGE(wxWidgets REQUIRED base core gl net)<br />
INCLUDE(${wxWidgets_USE_FILE})<br />
#and for each of your dependant executable / library targets:<br />
TARGET_LINK_LIBRARIES(&lt;YourTarget&gt; ${wxWidgets_LIBRARIES})</p>
<dt><code>FindwxWindows</code></p>
<dd> Find wxWindows (wxWidgets) installation </p>
<p> This module finds if wxWindows/wxWidgets is installed and determines where the include files and libraries are. It also determines what the name of the library is. Please note this file is DEPRECATED and replaced by FindwxWidgets.cmake. This code sets the following variables: </p>
<p>  WXWINDOWS_FOUND     = system has WxWindows<br />
  WXWINDOWS_LIBRARIES = path to the wxWindows libraries<br />
                        on Unix/Linux with additional<br />
                        linker flags from<br />
                        &#8220;wx-config &#8211;libs&#8221;<br />
  CMAKE_WXWINDOWS_CXX_FLAGS  = Compiler flags for wxWindows,<br />
                               essentially &#8220;`wx-config &#8211;cxxflags`&#8221;<br />
                               on Linux<br />
  WXWINDOWS_INCLUDE_DIR      = where to find &#8220;wx/wx.h&#8221; and &#8220;wx/setup.h&#8221;<br />
  WXWINDOWS_LINK_DIRECTORIES = link directories, useful for rpath on<br />
                                Unix<br />
  WXWINDOWS_DEFINITIONS      = extra defines</p>
<p> OPTIONS If you need OpenGL support please </p>
<pre>
  SET(WXWINDOWS_USE_GL 1)
</pre>
<p> in your CMakeLists.txt *before* you include this file. </p>
<pre>
  HAVE_ISYSTEM      - true required to replace -I by -isystem on g++
</pre>
<p> For convenience include Use_wxWindows.cmake in your project&#8217;s CMakeLists.txt using INCLUDE(Use_wxWindows). </p>
<p> USAGE </p>
<pre>
  SET(WXWINDOWS_USE_GL 1)
  FIND_PACKAGE(wxWindows)
</pre>
<p> NOTES wxWidgets 2.6.x is supported for monolithic builds e.g. compiled in wx/build/msw dir as: </p>
<pre>
  nmake -f makefile.vc BUILD=debug SHARED=0 USE_OPENGL=1 MONOLITHIC=1
</pre>
<p> DEPRECATED </p>
<pre>
  CMAKE_WX_CAN_COMPILE
  WXWINDOWS_LIBRARY
  CMAKE_WX_CXX_FLAGS
  WXWINDOWS_INCLUDE_PATH
</pre>
<p> AUTHOR Jan Woetzel &lt;<a rel="nofollow" href="http://www.mip.informatik.uni-kiel.de/~jw">http://www.mip.informatik.uni-kiel.de/~jw</a>&gt; (07/2003-01/2006) </p>
<dt><code>FortranCInterface</code></p>
<dd>
<p> FortranCInterface.cmake </p>
<p> This file defines the function create_fortran_c_interface. this function is used to create a configured header file that contains a mapping from C to a Fortran function using the correct name mangling scheme as defined by the current fortran compiler. </p>
<p> The function tages a list of functions and the name of a header file to configure. </p>
<p> This file also defines some helper functions that are used to detect the fortran name mangling scheme used by the current Fortran compiler. </p>
<pre>
  test_fortran_mangling - test a single fortran mangling 
  discover_fortran_mangling - loop over all combos of fortran
   name mangling and call test_fortran_mangling until one of them
   works.
  discover_fortran_module_mangling - try different types of 
  fortran modle name mangling to find one that works
</pre>
<p> this function tests a single fortran mangling. CODE &#8211; test code to try should define a subroutine called &quot;sub&quot; PREFIX &#8211; string to put in front of sub POSTFIX &#8211; string to put after sub ISUPPER &#8211; if TRUE then sub will be called as SUB DOC &#8211; string used in status checking Fortran ${DOC} linkage SUB &#8211; the name of the SUB to call RESULT place to store result TRUE if this linkage works, FALSE </p>
<pre>
        if not.
</pre>
<dt><code>GetPrerequisites</code></p>
<dd>
<p> GetPrerequisites.cmake </p>
<p> This script provides functions to list the .dll, .dylib or .so files that an executable or shared library file depends on. (Its prerequisites.) </p>
<p> It uses various tools to obtain the list of required shared library files: </p>
<pre>
   dumpbin (Windows)
   ldd (Linux/Unix)
   otool (Mac OSX)
</pre>
<p> The following functions are provided by this script: </p>
<pre>
   gp_append_unique
   gp_file_type
   is_file_executable
   gp_item_default_embedded_path
     (projects can override with gp_item_default_embedded_path_override)
   gp_resolve_item
     (projects can override with gp_resolve_item_override)
   get_prerequisites
   list_prerequisites
   list_prerequisites_by_glob
</pre>
<p> Requires CMake 2.6 or greater because it uses function, break, return and PARENT_SCOPE. </p>
<dt><code>ITKCompatibility</code></p>
<dd>
<p> work around an old bug in ITK prior to verison 3.0 </p>
<dt><code>InstallRequiredSystemLibraries</code></p>
<dd>
<p> By including this file, all files in the CMAKE_INSTALL_DEBUG_LIBRARIES, will be installed with INSTALL_PROGRAMS into /bin for WIN32 and /lib for non-win32. If CMAKE_SKIP_INSTALL_RULES is set to TRUE before including this file, then the INSTALL command is not called. The use can use the variable CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS to use a custom install command and install them into any directory they want. If it is the MSVC compiler, then the microsoft run time libraries will be found add automatically added to the CMAKE_INSTALL_DEBUG_LIBRARIES, and installed. If CMAKE_INSTALL_DEBUG_LIBRARIES is set and it is the MSVC compiler, then the debug libraries are installed when available. If CMAKE_INSTALL_MFC_LIBRARIES is set then the MFC run time libraries are installed as well as the CRT run time libraries. </p>
<dt><code>MacroAddFileDependencies</code></p>
<dd> MACRO_ADD_FILE_DEPENDENCIES(&lt;_file&gt; depend_files&#8230;) </p>
<p> MACRO_OPTIONAL_FIND_PACKAGE( &lt;name&gt; [QUIT] ) </p>
<dt><code>SquishTestScript</code></p>
<dd>
<p> This script launches a GUI test using Squish. You should not call the script directly; instead, you should acces it via the SQUISH_ADD_TEST macro that is defined in FindSquish.cmake. </p>
<p> This script starts the Squish server, launches the test on the client, and finally stops the squish server. If any of these steps fail (including if the tests do not pass) then a fatal error is raised. </p>
<dt><code>TestBigEndian</code></p>
<dd> Define macro to determine endian type </p>
<p> Check if the system is big endian or little endian </p>
<pre>
  TEST_BIG_ENDIAN(VARIABLE)
  VARIABLE - variable to store the result to
</pre>
<dt><code>TestCXXAcceptsFlag</code></p>
<dd> Test CXX compiler for a flag </p>
<p> Check if the CXX compiler accepts a flag </p>
<pre>
  Macro CHECK_CXX_ACCEPTS_FLAG(FLAGS VARIABLE) -
     checks if the function exists
  FLAGS - the flags to try
  VARIABLE - variable to store the result
</pre>
<dt><code>TestForANSIForScope</code></p>
<dd> Check for ANSI for scope support </p>
<p> Check if the compiler supports std:: on stl classes. </p>
<pre>
  CMAKE_NO_ANSI_FOR_SCOPE - holds result
</pre>
<dt><code>TestForANSIStreamHeaders</code></p>
<dd> Test for compiler support of ANSI stream headers iostream, etc. </p>
<p> check if we they have the standard ansi stream files (without the .h) </p>
<pre>
  CMAKE_NO_ANSI_STREAM_HEADERS - defined by the results
</pre>
<dt><code>TestForSSTREAM</code></p>
<dd>
<p> # &#8211; Test for std:: namespace support check if the compiler supports std:: on stl classes </p>
<pre>
  CMAKE_NO_ANSI_STRING_STREAM - defined by the results
</pre>
<dt><code>TestForSTDNamespace</code></p>
<dd> Test for std:: namespace support </p>
<p> check if the compiler supports std:: on stl classes </p>
<pre>
  CMAKE_NO_STD_NAMESPACE - defined by the results
</pre>
<dt><code>UseEcos</code></p>
<dd> This module defines variables and macros required to build eCos application. </p>
<p> This file contains the following macros: ECOS_ADD_INCLUDE_DIRECTORIES() &#8211; add the eCos include dirs ECOS_ADD_EXECUTABLE(name source1 &#8230; sourceN ) &#8211; create an eCos executable ECOS_ADJUST_DIRECTORY(VAR source1 &#8230; sourceN ) &#8211; adjusts the path of the source files and puts the result into VAR </p>
<p> Macros for selecting the toolchain: ECOS_USE_ARM_ELF_TOOLS() &#8211; enable the ARM ELF toolchain for the directory where it is called ECOS_USE_I386_ELF_TOOLS() &#8211; enable the i386 ELF toolchain for the directory where it is called ECOS_USE_PPC_EABI_TOOLS() &#8211; enable the PowerPC toolchain for the directory where it is called </p>
<p> It contains the following variables: ECOS_DEFINITIONS ECOSCONFIG_EXECUTABLE ECOS_CONFIG_FILE &#8211; defaults to ecos.ecc, if your eCos configuration file has a different name, adjust this variable for internal use only: </p>
<pre>
  ECOS_ADD_TARGET_LIB
</pre>
<dt><code>UsePkgConfig</code></p>
<dd> obsolete pkg-config module for CMake </p>
<p> Defines the following macros: </p>
<p> PKGCONFIG(package includedir libdir linkflags cflags) </p>
<p> Calling PKGCONFIG will fill the desired information into the 4 given arguments, e.g. PKGCONFIG(libart-2.0 LIBART_INCLUDE_DIR LIBART_LINK_DIR LIBART_LINK_FLAGS LIBART_CFLAGS) if pkg-config was NOT found or the specified software package doesn&#8217;t exist, the variable will be empty when the function returns, otherwise they will contain the respective information </p>
<dt><code>UseQt4</code></p>
<dd> Use Module for QT4 </p>
<p> Sets up C and C++ to use Qt 4. It is assumed that FindQt.cmake has already been loaded. See FindQt.cmake for information on how to load Qt 4 into your CMake project. </p>
<dt><code>UseSWIG</code></p>
<dd> SWIG module for CMake </p>
<p> Defines the following macros: </p>
<p>SWIG_ADD_MODULE(name language[files])<br />
&#8211; Define swig module with given name and specified language<br />
    SWIG_LINK_LIBRARIES(name[libraries]) &#8211;<br />
    Link libraries to swig module</p>
<p> All other macros are for internal use only. To get the actual name of the swig module, use: ${SWIG_MODULE_name_REAL_NAME}. Set Source files properties such as CPLUSPLUS and SWIG_FLAGS to specify special behavior of SWIG. Also global CMAKE_SWIG_FLAGS can be used to add special flags to all swig calls. Another special variable is CMAKE_SWIG_OUTDIR, it allows one to specify where to write all the swig generated module (swig -outdir option) The name-specific variable SWIG_MODULE_&lt;name&gt;_EXTRA_DEPS may be used to specify extra dependencies for the generated modules. </p>
<dt><code>Use_wxWindows</code></p>
<dd> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; </p>
<p> This convenience include finds if wxWindows is installed and set the appropriate libs, incdirs, flags etc. author Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt; (07/2003) </p>
<p> USAGE: </p>
<pre>
   just include Use_wxWindows.cmake
   in your projects CMakeLists.txt
</pre>
<p> INCLUDE( ${CMAKE_MODULE_PATH}/Use_wxWindows.cmake) </p>
<pre>
   if you are sure you need GL then
</pre>
<p> SET(WXWINDOWS_USE_GL 1) </p>
<pre>
   *before* you include this file.
</pre>
<p> 16.Feb.2004: changed INCLUDE to FIND_PACKAGE to read from users own non-system CMAKE_MODULE_PATH (Jan Woetzel JW) 07/2006: rewrite as FindwxWidgets.cmake, kept for backward compatibilty JW </p>
<dt><code>UsewxWidgets</code></p>
<dd> Convenience include for using wxWidgets library </p>
<p> Finds if wxWidgets is installed and set the appropriate libs, incdirs, flags etc. INCLUDE_DIRECTORIES, LINK_DIRECTORIES and ADD_DEFINITIONS are called. </p>
<p> USAGE </p>
<pre><code>
SET(wxWidgets_USE_LIBS gl xml xrc)
#optionally : more than wx std libs
              FIND_PACKAGE(wxWidgets REQUIRED)
                  INCLUDE(${xWidgets_USE_FILE})... add your targets here,
              e.g.ADD_EXECUTABLE / ADD_LIBRARY... TARGET_LINK_LIBRARIERS(&lt;yourWxDependantTarget&gt; ${wxWidgets_LIBRARIES})
</code></pre>
<p> DEPRECATED </p>
<pre>
  LINK_LIBRARIES is not called in favor of adding dependencies per target.
</pre>
<p> AUTHOR </p>
<pre>
  Jan Woetzel &lt;jw -at- mip.informatik.uni-kiel.de&gt;
</pre>
<dt><code>cmake_install</code></p>
<dd>
<p> Install script for directory: /builddir/build/BUILD/cmake-2.6.4/Modules </p>
</dl>
<h2>VARIABLES</h2>
<h2>VARIABLES THAT CHANGE BEHAVIOR</h2>
<dl>
<dt><code>BUILD_SHARED_LIBS</code></p>
<dd> Global flag to cause add_library to create shared libraries if on. </p>
<p> If present and true, this will cause all libraries to be built shared unless the library was explicitly added as a static library. This variable is often added to projects as an OPTION so that each user of a project can decide if they want to build the project using shared or static libraries. </p>
<dt><code>CMAKE_BACKWARDS_COMPATIBILITY</code></p>
<dd> Version of cmake required to build project </p>
<p> From the point of view of backwards compatibility, this specifies what version of CMake should be supported. By default this value is the version number of CMake that you are running. You can set this to an older version of CMake to support deprecated commands of CMake in projects that were written to use older versions of CMake. This can be set by the user or set at the beginning of a CMakeLists file. </p>
<dt><code>CMAKE_BUILD_TYPE</code></p>
<dd> Specifies the build type for make based generators. </p>
<p> This specifies what build type will be built in this tree. Possible values are empty, Debug, Release, RelWithDebInfo and MinSizeRel. This variable is only supported for make based generators. If this variable is supported, then CMake will also provide initial values for the variables with the name CMAKE_C_FLAGS_[Debug|Release|RelWithDebInfo|MinSizeRel]. For example, if CMAKE_BUILD_TYPE is Debug, then CMAKE_C_FLAGS_DEBUG will be added to the CMAKE_C_FLAGS. </p>
<dt><code>CMAKE_COLOR_MAKEFILE</code></p>
<dd> Enables color output when using the Makefile generator. </p>
<p> When enabled, the generated Makefiles will produce colored output. Default is ON. </p>
<dt><code>CMAKE_CONFIGURATION_TYPES</code></p>
<dd> Specifies the available build types. </p>
<p> This specifies what build types will be available such as Debug, Release, RelWithDebInfo etc. This has reasonable defaults on most platforms. But can be extended to provide other build types. See also CMAKE_BUILD_TYPE. </p>
<dt><code>CMAKE_FIND_LIBRARY_PREFIXES</code></p>
<dd> Prefixes to prepend when looking for libraries. </p>
<p> This specifies what prefixes to add to library names when the find_library command looks for libraries. On UNIX systems this is typically lib, meaning that when trying to find the foo library it will look for libfoo. </p>
<dt><code>CMAKE_FIND_LIBRARY_SUFFIXES</code></p>
<dd> Suffixes to append when looking for libraries. </p>
<p> This specifies what suffixes to add to library names when the find_library command looks for libraries. On Windows systems this is typically .lib and .dll, meaning that when trying to find the foo library it will look for foo.dll etc. </p>
<dt><code>CMAKE_INCLUDE_PATH</code></p>
<dd> Path used for searching by FIND_FILE() and FIND_PATH(). </p>
<p> Specifies a path which will be used both by FIND_FILE() and FIND_PATH(). Both commands will check each of the contained directories for the existence of the file which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_INCLUDE_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_INSTALL_PREFIX</code></p>
<dd> Install directory used by install. </p>
<p> If &quot;make install&quot; is invoked or INSTALL is built, this directory is pre-pended onto all install directories. This variable defaults to /usr/local on UNIX and c:/Program Files on Windows. </p>
<dt><code>CMAKE_LIBRARY_PATH</code></p>
<dd> Path used for searching by FIND_LIBRARY(). </p>
<p> Specifies a path which will be used by FIND_LIBRARY(). FIND_LIBRARY() will check each of the contained directories for the existence of the library which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_MFC_FLAG</code></p>
<dd> Tell cmake to use MFC for an executable or dll. </p>
<p> This can be set in a CMakeLists.txt file and will enable MFC in the application. It should be set to 1 for static the static MFC library, and 2 for the shared MFC library. This is used in visual studio 6 and 7 project files. The CMakeSetup dialog uses MFC and the CMakeLists.txt looks like this: </p>
<p> ADD_DEFINITIONS(-D_AFXDLL) </p>
<p> set(CMAKE_MFC_FLAG 2) </p>
<p> add_executable(CMakeSetup WIN32 ${SRCS}) </p>
<dt><code>CMAKE_MODULE_PATH</code></p>
<dd> Path to look for cmake modules to load. </p>
<p> Specifies a path to override the default seach path for CMake modules. For example include commands will look in this path first for modules to include. </p>
<dt><code>CMAKE_NOT_USING_CONFIG_FLAGS</code></p>
<dd> Skip _BUILD_TYPE flags if true. </p>
<p> This is an internal flag used by the generators in CMake to tell CMake to skip the _BUILD_TYPE flags. </p>
<dt><code>CMAKE_PREFIX_PATH</code></p>
<dd> Path used for searching by FIND_XXX(), with appropriate suffixes added. </p>
<p> Specifies a path which will be used by the FIND_XXX() commands. It contains the &quot;base&quot; directories, the FIND_XXX() commands append appropriate subdirectories to the base directories. So FIND_PROGRAM() adds /bin to each of the directories in the path, FIND_LIBRARY() appends /lib to each of the directories, and FIND_PATH() and FIND_FILE() append /include . By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_PREFIX_PATH, CMAKE_INCLUDE_PATH, CMAKE_LIBRARY_PATH, CMAKE_PROGRAM_PATH. </p>
<dt><code>CMAKE_PROGRAM_PATH</code></p>
<dd> Path used for searching by FIND_PROGRAM(). </p>
<p> Specifies a path which will be used by FIND_PROGRAM(). FIND_PROGRAM() will check each of the contained directories for the existence of the program which is currently searched. By default it is empty, it is intended to be set by the project. See also CMAKE_SYSTEM_PROGRAM_PATH, CMAKE_PREFIX_PATH. </p>
<dt><code>CMAKE_SYSTEM_INCLUDE_PATH</code></p>
<dd> Path used for searching by FIND_FILE() and FIND_PATH(). </p>
<p> Specifies a path which will be used both by FIND_FILE() and FIND_PATH(). Both commands will check each of the contained directories for the existence of the file which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_INCLUDE_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_SYSTEM_LIBRARY_PATH</code></p>
<dd> Path used for searching by FIND_LIBRARY(). </p>
<p> Specifies a path which will be used by FIND_LIBRARY(). FIND_LIBRARY() will check each of the contained directories for the existence of the library which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_SYSTEM_LIBRARY_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_SYSTEM_PREFIX_PATH</code></p>
<dd> Path used for searching by FIND_XXX(), with appropriate suffixes added. </p>
<p> Specifies a path which will be used by the FIND_XXX() commands. It contains the &quot;base&quot; directories, the FIND_XXX() commands append appropriate subdirectories to the base directories. So FIND_PROGRAM() adds /bin to each of the directories in the path, FIND_LIBRARY() appends /lib to each of the directories, and FIND_PATH() and FIND_FILE() append /include . By default this contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_PREFIX_PATH for this. See also CMAKE_SYSTEM_INCLUDE_PATH, CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_SYSTEM_PROGRAM_PATH. </p>
<dt><code>CMAKE_SYSTEM_PROGRAM_PATH</code></p>
<dd> Path used for searching by FIND_PROGRAM(). </p>
<p> Specifies a path which will be used by FIND_PROGRAM(). FIND_PROGRAM() will check each of the contained directories for the existence of the program which is currently searched. By default it contains the standard directories for the current system. It is NOT intended to be modified by the project, use CMAKE_PROGRAM_PATH for this. See also CMAKE_SYSTEM_PREFIX_PATH. </p>
<dt><code>CMAKE_USER_MAKE_RULES_OVERRIDE</code></p>
<dd> Specify a file that can change the build rule variables. </p>
<p> If this variable is set, it should to point to a CMakeLists.txt file that will be read in by CMake after all the system settings have been set, but before they have been used. This would allow you to override any variables that need to be changed for some special project. </p>
</dl>
<h2>VARIABLES THAT DESCRIBE THE SYSTEM</h2>
<dl>
<dt><code>APPLE</code></p>
<dd> True if running on Mac OSX. </p>
<p> Set to true on Mac OSX. </p>
<dt><code>BORLAND</code></p>
<dd> True of the borland compiler is being used. </p>
<p> This is set to true if the Borland compiler is being used. </p>
<dt><code>CMAKE_CL_64</code></p>
<dd> Using the 64 bit compiler from Microsoft </p>
<p> Set to true when using the 64 bit cl compiler from Microsoft. </p>
<dt><code>CMAKE_COMPILER_2005</code></p>
<dd> Using the Visual Studio 2005 compiler from Microsoft </p>
<p> Set to true when using the Visual Studio 2005 compiler from Microsoft. </p>
<dt><code>CMAKE_HOST_APPLE</code></p>
<dd> True for Apple OSXoperating systems. </p>
<p> Set to true when the host system is Apple OSX. </p>
<dt><code>CMAKE_HOST_SYSTEM</code></p>
<dd> Name of system cmake is being run on. </p>
<p> The same as CMAKE_SYSTEM but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_NAME</code></p>
<dd> Name of the OS CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_NAME but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_PROCESSOR</code></p>
<dd> The name of the CPU CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_PROCESSOR but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_SYSTEM_VERSION</code></p>
<dd> OS version CMake is running on. </p>
<p> The same as CMAKE_SYSTEM_VERSION but for the host system instead of the target system when cross compiling. </p>
<dt><code>CMAKE_HOST_UNIX</code></p>
<dd> True for UNIX and UNIX like operating systems. </p>
<p> Set to true when the host system is UNIX or UNIX like (i.e. APPLE and CYGWIN). </p>
<dt><code>CMAKE_HOST_WIN32</code></p>
<dd> True on windows systems, including win64. </p>
<p> Set to true when the host system is Windows and on cygwin. </p>
<dt><code>CMAKE_OBJECT_PATH_MAX</code></p>
<dd> Maximum object file full-path length allowed by native build tools. </p>
<p> CMake computes for every source file an object file name that is unique to the source file and deterministic with respect to the full path to the source file. This allows multiple source files in a target to share the same name if they lie in different directories without rebuilding when one is added or removed. However, it can produce long full paths in a few cases, so CMake shortens the path using a hashing scheme when the full path to an object file exceeds a limit. CMake has a built-in limit for each platform that is sufficient for common tools, but some native tools may have a lower limit. This variable may be set to specify the limit explicitly. The value must be an integer no less than 128. </p>
<dt><code>CMAKE_SYSTEM</code></p>
<dd> Name of system cmake is compiling for. </p>
<p> This variable is the composite of CMAKE_SYSTEM_NAMEand CMAKE_SYSTEM_VERSION, like this ${CMAKE_SYSTEM_NAME}-${CMAKE_SYSTEM_VERSION}. If CMAKE_SYSTEM_VERSION is not set, then CMAKE_SYSTEM is the same as CMAKE_SYSTEM_NAME. </p>
<dt><code>CMAKE_SYSTEM_NAME</code></p>
<dd> Name of the OS CMake is building for. </p>
<p> This is the name of the operating system on which CMake is targeting. On systems that have the uname command, this variable is set to the output of uname -s. Linux, Windows, and Darwin for Mac OSX are the values found on the big three operating systems. </p>
<dt><code>CMAKE_SYSTEM_PROCESSOR</code></p>
<dd> The name of the CPU CMake is building for. </p>
<p> On systems that support uname, this variable is set to the output of uname -p, on windows it is set to the value of the environment variable PROCESSOR_ARCHITECTURE </p>
<dt><code>CMAKE_SYSTEM_VERSION</code></p>
<dd> OS version CMake is building for. </p>
<p> A numeric version string for the system, on systems that support uname, this variable is set to the output of uname -r. On other systems this is set to major-minor version numbers. </p>
<dt><code>CYGWIN</code></p>
<dd> True for cygwin. </p>
<p> Set to true when using CYGWIN. </p>
<dt><code>MSVC</code></p>
<dd> True when using Microsoft Visual C </p>
<p> Set to true when the compiler is some version of Microsoft Visual C. </p>
<dt><code>MSVC80</code></p>
<dd> True when using Microsoft Visual C 8.0 </p>
<p> Set to true when the compiler is version 8.0 of Microsoft Visual C. </p>
<dt><code>MSVC_IDE</code></p>
<dd> True when using the Microsoft Visual C IDE </p>
<p> Set to true when the target platform is the Microsoft Visual C IDE, as opposed to the command line compiler. </p>
<dt><code>MSVC_VERSION</code></p>
<dd> The version of Microsoft Visual C/C++ being used if any. </p>
<p> The version of Microsoft Visual C/C++ being used if any. For example 1300 is MSVC 6.0. </p>
<dt><code>UNIX</code></p>
<dd> True for UNIX and UNIX like operating systems. </p>
<p> Set to true when the target system is UNIX or UNIX like (i.e. APPLE and CYGWIN). </p>
<dt><code>WIN32</code></p>
<dd> True on windows systems, including win64. </p>
<p> Set to true when the target system is Windows and on cygwin. </p>
</dl>
<h2>VARIABLES FOR LANGUAGES</h2>
<dl>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND</code></p>
<dd> Rule variable to append to a static archive. </p>
<p> This is a rule variable that tells CMake how to append to a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE and CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH. </p>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE</code></p>
<dd> Rule variable to create a new static archive. </p>
<p> This is a rule variable that tells CMake how to create a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND and CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH. </p>
<dt><code>CMAKE_&lt;LANG&gt;_ARCHIVE_FINISH</code></p>
<dd> Rule variable to finish an existing static archive. </p>
<p> This is a rule variable that tells CMake how to finish a static archive. It is used in place of CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY on some platforms in order to support large object counts. See also CMAKE_&lt;LANG&gt;_ARCHIVE_CREATE and CMAKE_&lt;LANG&gt;_ARCHIVE_APPEND. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER</code></p>
<dd> The full path to the compiler for LANG. </p>
<p> This is the command that will be used as the &lt;LANG&gt; compiler. Once set, you can not change this variable. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_ABI</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILER_ID</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the compiler and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_COMPILE_OBJECT</code></p>
<dd> Rule variable to compile a single object file. </p>
<p> This is a rule variable that tells CMake how to compile a single object file for for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_SHARED_LIBRARY</code></p>
<dd> Rule variable to create a shared library. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_SHARED_MODULE</code></p>
<dd> Rule variable to create a shared module. </p>
<p> This is a rule variable that tells CMake how to create a shared library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_CREATE_STATIC_LIBRARY</code></p>
<dd> Rule variable to create a static library. </p>
<p> This is a rule variable that tells CMake how to create a static library for the language &lt;LANG&gt;. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_DEBUG</code></p>
<dd> Flags for Debug build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is Debug. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_MINSIZEREL</code></p>
<dd> Flags for MinSizeRel build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is MinSizeRel.Short for minimum size release. </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_RELEASE</code></p>
<dd> Flags for Release build type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is Release </p>
<dt><code>CMAKE_&lt;LANG&gt;_FLAGS_RELWITHDEBINFO</code></p>
<dd> Flags for RelWithDebInfo type or configuration. </p>
<p> &lt;LANG&gt; flags used when CMAKE_BUILD_TYPE is RelWithDebInfo. Short for Release With Debug Information. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IGNORE_EXTENSIONS</code></p>
<dd> File extensions that should be ignored by the build. </p>
<p> This is a list of file extensions that may be part of a project for a given language but are not compiled. </p>
<dt><code>CMAKE_&lt;LANG&gt;_IMPLICIT_INCLUDE_DIRECTORIES</code></p>
<dd> Directories implicitly searched by the compiler for header files. </p>
<p> CMake does not explicitly specify these directories on compiler command lines for language &lt;LANG&gt;. This prevents system include directories from being treated as user include directories on some compilers. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LINKER_PREFERENCE</code></p>
<dd> Determine if a language should be used for linking. </p>
<p> If this is &quot;Preferred&quot; then if there is a mixed language shared library or executable, then this languages linker command will be used. </p>
<dt><code>CMAKE_&lt;LANG&gt;_LINK_EXECUTABLE </code></p>
<dd> Rule variable to link and executable. </p>
<p> Rule variable to link and executable for the given language. </p>
<dt><code>CMAKE_&lt;LANG&gt;_OUTPUT_EXTENSION</code></p>
<dd> Extension for the output of a compile for a single file. </p>
<p> This is the extension for an object file for the given &lt;LANG&gt;. For example .obj for C on Windows. </p>
<dt><code>CMAKE_&lt;LANG&gt;_PLATFORM_ID</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the platform and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_SIZEOF_DATA_PTR</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the architecture and is subject to change. </p>
<dt><code>CMAKE_&lt;LANG&gt;_SOURCE_FILE_EXTENSIONS</code></p>
<dd> Extensions of source files for the given language. </p>
<p> This is the list of extensions for a given languages source files. </p>
<dt><code>CMAKE_COMPILER_IS_GNU&lt;LANG&gt;</code></p>
<dd> True if the compiler is GNU. </p>
<p> If the selected &lt;LANG&gt; compiler is the GNU compiler then this is TRUE, if not it is FALSE. </p>
<dt><code>CMAKE_INTERNAL_PLATFORM_ABI</code></p>
<dd> An internal variable subject to change. </p>
<p> This is used in determining the compiler ABI and is subject to change. </p>
<dt><code>CMAKE_USER_MAKE_RULES_OVERRIDE_&lt;LANG&gt;</code></p>
<dd> Specify a file that can change the build rule variables. </p>
<p> If this variable is set, it should to point to a CMakeLists.txt file that will be read in by CMake after all the system settings have been set, but before they have been used. This would allow you to override any variables that need to be changed for some language. </p>
</dl>
<h2>VARIABLES THAT CONTROL THE BUILD</h2>
<dl>
<dt><code>CMAKE_&lt;CONFIG&gt;_POSTFIX</code></p>
<dd> Default filename postfix for libraries under configuration &lt;CONFIG&gt;. </p>
<p> When a non-executable target is created its &lt;CONFIG&gt;_POSTFIX target property is initialized with the value of this variable if it is set. </p>
<dt><code>CMAKE_ARCHIVE_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the ARCHIVE targets when built. </p>
<p> This variable is used to initialize the ARCHIVE_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_BUILD_WITH_INSTALL_RPATH</code></p>
<dd> Use the install path for the RPATH </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with the install path for the RPATH and does not need to be relinked when installed. </p>
<dt><code>CMAKE_DEBUG_POSTFIX</code></p>
<dd> See variable CMAKE_&lt;CONFIG&gt;_POSTFIX. </p>
<p> This variable is a special case of the more-general CMAKE_&lt;CONFIG&gt;_POSTFIX variable for the DEBUG configuration. </p>
<dt><code>CMAKE_EXE_LINKER_FLAGS</code></p>
<dd> Linker flags used to create executables. </p>
<p> Flags used by the linker when creating an executable. </p>
<dt><code>CMAKE_EXE_LINKER_FLAGS_[CMAKE_BUILD_TYPE]</code></p>
<dd> Flag used when linking an executable. </p>
<p> Same as CMAKE_C_FLAGS_* but used by the linker when creating executables. </p>
<dt><code>CMAKE_Fortran_MODULE_DIRECTORY</code></p>
<dd> Fortran module output directory. </p>
<p> This variable is used to initialize the Fortran_MODULE_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_INSTALL_NAME_DIR</code></p>
<dd> Mac OSX directory name for installed targets. </p>
<p> CMAKE_INSTALL_NAME_DIR is used to initialize the INSTALL_NAME_DIR property on all targets. See that target property for more information. </p>
<dt><code>CMAKE_INSTALL_RPATH</code></p>
<dd> The rpath to use for installed targets. </p>
<p> A semicolon-separated list specifying the rpath to use in installed targets (for platforms that support it). This is used to initialize the target property INSTALL_RPATH for all targets. </p>
<dt><code>CMAKE_INSTALL_RPATH_USE_LINK_PATH</code></p>
<dd> Add paths to linker search and installed rpath. </p>
<p> CMAKE_INSTALL_RPATH_USE_LINK_PATH is a boolean that if set to true will append directories in the linker search path and outside the project to the INSTALL_RPATH. This is used to initialize the target property INSTALL_RPATH_USE_LINK_PATH for all targets. </p>
<dt><code>CMAKE_LIBRARY_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the LIBRARY targets when built. </p>
<p> This variable is used to initialize the LIBRARY_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_LIBRARY_PATH_FLAG</code></p>
<dd> The flag used to add a library search path to a compiler. </p>
<p> The flag used to specify a library directory to the compiler. On most compilers this is &quot;-L&quot;. </p>
<dt><code>CMAKE_LINK_DEF_FILE_FLAG </code></p>
<dd> Linker flag used to specify a .def file for dll creation. </p>
<p> The flag used to add a .def file when creating a dll on Windows, this is only defined on Windows. </p>
<dt><code>CMAKE_LINK_LIBRARY_FILE_FLAG</code></p>
<dd> Flag used to link a library specified by a path to its file. </p>
<p> The flag used before a library file path is given to the linker. This is needed only on very few platforms. </p>
<dt><code>CMAKE_LINK_LIBRARY_FLAG</code></p>
<dd> Flag used to link a library into an executable. </p>
<p> The flag used to specify a library to link to an executable. On most compilers this is &quot;-l&quot;. </p>
<dt><code>CMAKE_RUNTIME_OUTPUT_DIRECTORY</code></p>
<dd> Where to put all the RUNTIME targets when built. </p>
<p> This variable is used to initialize the RUNTIME_OUTPUT_DIRECTORY property on all the targets. See that target property for additional information. </p>
<dt><code>CMAKE_SKIP_BUILD_RPATH</code></p>
<dd> Do not include RPATHs in the build tree. </p>
<p> Normally CMake uses the build tree for the RPATH when building executables etc on systems that use RPATH. When the software is installed the executables etc are relinked by CMake to have the install RPATH. If this variable is set to true then the software is always built with no RPATH. </p>
<dt><code>CMAKE_USE_RELATIVE_PATHS</code></p>
<dd> Use relative paths (May not work!). </p>
<p> If this is set to TRUE, then the CMake will use relative paths between the source and binary tree. This option does not work for more complicated projects, and relative paths are used when possible. In general, it is not possible to move CMake generated makefiles to a different location regardless of the value of this variable. </p>
<dt><code>EXECUTABLE_OUTPUT_PATH</code></p>
<dd> Old executable location variable. </p>
<p> The target property RUNTIME_OUTPUT_DIRECTORY supercedes this variable for a target if it is set. Executable targets are otherwise placed in this directory. </p>
<dt><code>LIBRARY_OUTPUT_PATH</code></p>
<dd> Old library location variable. </p>
<p> The target properties ARCHIVE_OUTPUT_DIRECTORY, LIBRARY_OUTPUT_DIRECTORY, and RUNTIME_OUTPUT_DIRECTORY supercede this variable for a target if they are set. Library targets are otherwise placed in this directory. </p>
</dl>
<h2>VARIABLES THAT PROVIDE INFORMATION</h2>
<dl>
<dt><code>CMAKE_AR</code></p>
<dd> Name of archiving tool for static libraries. </p>
<p> This specifies name of the program that creates archive or static libraries. </p>
<dt><code>CMAKE_BINARY_DIR</code></p>
<dd> The path to the top level of the build tree. </p>
<p> This is the full path to the top level of the current CMake build tree. For an in-source build, this would be the same as CMAKE_SOURCE_DIR. </p>
<dt><code>CMAKE_BUILD_TOOL</code></p>
<dd> Tool used for the acutal build process. </p>
<p> This variable is set to the program that will be needed to build the output of CMake. If the generator selected was Visual Studio 6, the CMAKE_MAKE_PROGRAM will be set to msdev, for Unix makefiles it will be set to make or gmake, and for Visual Studio 7 it set to devenv. For Nmake Makefiles the value is nmake. This can be useful for adding special flags and commands based on the final build environment. </p>
<dt><code>CMAKE_CACHEFILE_DIR</code></p>
<dd> The directory with the CMakeCache.txt file. </p>
<p> This is the full path to the directory that has the CMakeCache.txt file in it. This is the same as CMAKE_BINARY_DIR. </p>
<dt><code>CMAKE_CACHE_MAJOR_VERSION</code></p>
<dd> Major version of CMake used to create the CMakeCache.txt file </p>
<p> This is stores the major version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CACHE_MINOR_VERSION</code></p>
<dd> Minor version of CMake used to create the CMakeCache.txt file </p>
<p> This is stores the minor version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CACHE_RELEASE_VERSION</code></p>
<dd> Release version of CMake used to create the CMakeCache.txt file </p>
<p> This is stores the release version of CMake used to write a CMake cache file. It is only different when a different version of CMake is run on a previously created cache file. </p>
<dt><code>CMAKE_CFG_INTDIR</code></p>
<dd> Build time configuration directory for project. </p>
<p> This is a variable that is used to provide developers access to the intermediate directory used by Visual Studio IDE projects. For example, if building Debug all executables and libraries end up in a Debug directory. On UNIX systems this variable is set to &quot;.&quot;. However, with Visual Studio this variable is set to $(IntDir). $(IntDir) is expanded by the IDE only. So this variable should only be used in custom commands that will be run during the build process. This variable should not be used directly in a CMake command. CMake has no way of knowing if Debug or Release will be picked by the IDE for a build type. If a program needs to know the directory it was built in, it can use CMAKE_INTDIR. CMAKE_INTDIR is a C/C++ preprocessor macro that is defined on the command line of the compiler. If it has a value, it will be the intermediate directory used to build the file. This way an executable or a library can find files that are located in the build directory. </p>
<dt><code>CMAKE_COMMAND</code></p>
<dd> The full path to the cmake executable. </p>
<p> This is the full path to the CMake executable cmake which is useful from custom commands that want to use the cmake -E option for portable system commands. (e.g. /usr/local/bin/cmake </p>
<dt><code>CMAKE_CROSSCOMPILING</code></p>
<dd> Is CMake currently cross compiling. </p>
<p> This variable will be set to true by CMake if CMake is cross compiling. Specifically if the build platform is different from the target platform. </p>
<dt><code>CMAKE_CTEST_COMMAND</code></p>
<dd> Full path to ctest command installed with cmake. </p>
<p> This is the full path to the CTest executable ctest which is useful from custom commands that want to use the cmake -E option for portable system commands. </p>
<dt><code>CMAKE_CURRENT_BINARY_DIR</code></p>
<dd> The path to the binary directory currently being processed. </p>
<p> This the full path to the build directory that is currently being processed by cmake. Each directory added by add_subdirectory will create a binary directory in the build tree, and as it is being processed this variable will be set. For in-source builds this is the current source directory being processed. </p>
<dt><code>CMAKE_CURRENT_LIST_FILE</code></p>
<dd> Full path to the listfile currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the one currently being processed. See also CMAKE_PARENT_LIST_FILE. </p>
<dt><code>CMAKE_CURRENT_LIST_LINE</code></p>
<dd> The line number of the current file being processed. </p>
<p> This is the line number of the file currently being processed by cmake. </p>
<dt><code>CMAKE_CURRENT_SOURCE_DIR</code></p>
<dd> The path to the source directory currently being processed. </p>
<p> This the full path to the source directory that is currently being processed by cmake. </p>
<dt><code>CMAKE_DL_LIBS</code></p>
<dd> Name of library containing dlopen and dlcose. </p>
<p> The name of the library that has dlopen and dlclose in it, usually -ldl on most UNIX machines. </p>
<dt><code>CMAKE_EDIT_COMMAND</code></p>
<dd> Full path to CMakeSetup or ccmake. </p>
<p> This is the full path to the CMake executable that can graphically edit the cache. For example, CMakeSetup, ccmake, or cmake -i. </p>
<dt><code>CMAKE_EXECUTABLE_SUFFIX</code></p>
<dd> The suffix for executables on this platform. </p>
<p> The suffix to use for the end of an executable if any, .exe on Windows. </p>
<dt><code>CMAKE_GENERATOR</code></p>
<dd> The generator used to build the project. </p>
<p> The name of the generator that is being used to generate the build files. (e.g. &quot;Unix Makefiles&quot;, &quot;Visual Studio 6&quot;, etc.) </p>
<dt><code>CMAKE_HOME_DIRECTORY</code></p>
<dd> Path to top of source tree. </p>
<p> This is the path to the top level of the source tree. </p>
<dt><code>CMAKE_IMPORT_LIBRARY_PREFIX</code></p>
<dd> The prefix for import libraries that you link to. </p>
<p> The prefix to use for the name of an import library if used on this platform. </p>
<dt><code>CMAKE_IMPORT_LIBRARY_SUFFIX</code></p>
<dd> The suffix for import libraries that you link to. </p>
<p> The suffix to use for the end of an import library if used onthis platform. </p>
<dt><code>CMAKE_LINK_LIBRARY_SUFFIX</code></p>
<dd> The suffix for libraries that you link to. </p>
<p> The suffix to use for the end of a library, .lib on Windows. </p>
<dt><code>CMAKE_MAJOR_VERSION</code></p>
<dd> The Major version of cmake (i.e. the 2 in 2.X.X) </p>
<p> This specifies the major version of the CMake executable being run. </p>
<dt><code>CMAKE_MAKE_PROGRAM</code></p>
<dd> See CMAKE_BUILD_TOOL. </p>
<p> This variable is around for backwards compatibility, see CMAKE_BUILD_TOOL. </p>
<dt><code>CMAKE_MINOR_VERSION</code></p>
<dd> The Minor version of cmake (i.e. the 4 in X.4.X). </p>
<p> This specifies the minor version of the CMake executable being run. </p>
<dt><code>CMAKE_PARENT_LIST_FILE</code></p>
<dd> Full path to the parent listfile of the one currently being processed. </p>
<p> As CMake processes the listfiles in your project this variable will always be set to the listfile that included or somehow invoked the one currently being processed. See also CMAKE_CURRENT_LIST_FILE. </p>
<dt><code>CMAKE_PATCH_VERSION</code></p>
<dd> The patch version of cmake (i.e. the 3 in X.X.3). </p>
<p> This specifies the patch version of the CMake executable being run. </p>
<dt><code>CMAKE_PROJECT_NAME</code></p>
<dd> The name of the current project. </p>
<p> This specifies name of the current project from the closest inherited PROJECT command. </p>
<dt><code>CMAKE_RANLIB</code></p>
<dd> Name of randomizing tool for static libraries. </p>
<p> This specifies name of the program that randomizes libraries on UNIX, not used on Windows, but may be present. </p>
<dt><code>CMAKE_ROOT</code></p>
<dd> Install directory for running cmake. </p>
<p> This is the install root for the running CMake and the Modules directory can be found here. This is commonly used in this format: ${CMAKE_ROOT}/Modules </p>
<dt><code>CMAKE_SHARED_LIBRARY_PREFIX</code></p>
<dd> The prefix for shared libraries that you link to. </p>
<p> The prefix to use for the name of a shared library, lib on UNIX. </p>
<dt><code>CMAKE_SHARED_LIBRARY_SUFFIX</code></p>
<dd> The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a shared library, .dll on Windows. </p>
<dt><code>CMAKE_SHARED_MODULE_PREFIX</code></p>
<dd> The prefix for loadable modules that you link to. </p>
<p> The prefix to use for the name of a loadable module on this platform. </p>
<dt><code>CMAKE_SHARED_MODULE_SUFFIX</code></p>
<dd> The suffix for shared libraries that you link to. </p>
<p> The suffix to use for the end of a loadable module on this platform </p>
<dt><code>CMAKE_SIZEOF_VOID_P</code></p>
<dd> Size of a void pointer. </p>
<p> This is set to the size of a pointer on the machine, and is determined by a try compile. If a 64 bit size is found, then the library search path is modified to look for 64 bit libraries first. </p>
<dt><code>CMAKE_SKIP_RPATH</code></p>
<dd> If true, do not add run time path information. </p>
<p> If this is set to TRUE, then the rpath information is not added to compiled executables. The defaultis to add rpath information if the platform supports it.This allows for easy running from the build tree. </p>
<dt><code>CMAKE_SOURCE_DIR</code></p>
<dd> The path to the top level of the source tree. </p>
<p> This is the full path to the top level of the current CMake source tree. For an in-source build, this would be the same as CMAKE_BINARY_DIR. </p>
<dt><code>CMAKE_STANDARD_LIBRARIES</code></p>
<dd> Libraries linked into every executable and shared library. </p>
<p> This is the list of libraries that are linked into all executables and libraries. </p>
<dt><code>CMAKE_STATIC_LIBRARY_PREFIX</code></p>
<dd> The prefix for static libraries that you link to. </p>
<p> The prefix to use for the name of a static library, lib on UNIX. </p>
<dt><code>CMAKE_STATIC_LIBRARY_SUFFIX</code></p>
<dd> The suffix for static libraries that you link to. </p>
<p> The suffix to use for the end of a static library, .lib on Windows. </p>
<dt><code>CMAKE_USING_VC_FREE_TOOLS</code></p>
<dd> True if free visual studio tools being used. </p>
<p> This is set to true if the compiler is Visual Studio free tools. </p>
<dt><code>CMAKE_VERBOSE_MAKEFILE</code></p>
<dd> Create verbose makefiles if on. </p>
<p> This variable defaults to false. You can set this variable to true to make CMake produce verbose makefiles that show each command line as it is used. </p>
<dt><code>CMAKE_VERSION</code></p>
<dd> The full version of cmake in major.minor.patch format. </p>
<p> This specifies the full version of the CMake executable being run. This variable is defined by versions 2.6.3 and higher. See variables CMAKE_MAJOR_VERSION, CMAKE_MINOR_VERSION, and CMAKE_PATCH_VERSION for individual version components. </p>
<dt><code>PROJECT_BINARY_DIR</code></p>
<dd> Full path to build directory for project. </p>
<p> This is the binary directory of the most recent PROJECT command. </p>
<dt><code>PROJECT_NAME</code></p>
<dd> Name of the project given to the project command. </p>
<p> This is the name given to the most recent PROJECT command. </p>
<dt><code>PROJECT_SOURCE_DIR</code></p>
<dd> Top level source directory for the current project. </p>
<p> This is the source directory of the most recent PROJECT command. </p>
<dt><code>[Project name]_BINARY_DIR</code></p>
<dd> Top level binary directory for the named project. </p>
<p> A variable is created with the name used in the PROJECT command, and is the binary directory for the project. This can be useful when SUBDIR is used to connect several projects. </p>
<dt><code>[Project name]_SOURCE_DIR</code></p>
<dd> Top level source directory for the named project. </p>
<p> A variable is created with the name used in the PROJECT command, and is the source directory for the project. This can be useful when add_subdirectory is used to connect several projects. </p>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2002 Kitware, Inc., Insight Consortium. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. </p>
<p> The names of Kitware, Inc., the Insight Consortium, or the names of any consortium members, or of any contributors, may not be used to endorse or promote products derived from this software without specific prior written permission. </p>
<p> Modified source versions must be plainly marked as such, and must not be misrepresented as being the original software. </p>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS &#8220;AS IS&#8221; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<h2>AUTHOR</h2>
<p> This manual page was generated by the &quot;&#8211;help-man&quot; option. </p>
<h2>Index</h2>
