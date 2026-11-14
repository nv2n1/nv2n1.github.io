---
title: "cmake(1)"
name: "cmake"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmake/"
description: "cmake – CMake Command-Line Reference"
---

<h2 class="name">NAME</h2>
<p> cmake &#8211; CMake Command-Line Reference </p>
<h2>SYNOPSIS</h2>
<pre><code>
Generate a Project Buildsystem
        cmake[&lt;options&gt;]&lt;path - to - source&gt;
            cmake[&lt;options&gt;]&lt;path - to - existing - build&gt;
                cmake[&lt;options&gt;] - S&lt;path - to - source&gt; - B&lt;path - to - build&gt; Build a Project cmake-- build&lt;dir&gt;[&lt;options&gt;][--&lt;build - tool - options&gt;] Install a Project cmake-- install&lt;dir&gt;[&lt;options&gt;] Open a Project cmake-- open&lt;dir&gt; Run a Script cmake[{-D &lt; var &gt;= &lt;value&gt;}...] - P&lt;cmake - script - file&gt; Run a Command - Line Tool cmake - E&lt;command&gt;[&lt;options&gt;] Run the Find - Package Tool cmake-- find - package[&lt;options&gt;] View Help cmake-- help[-&lt;topic&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>cmake</code> executable is the command-line interface of the cross-platform buildsystem generator CMake. The above <i>Synopsis</i> lists various actions the tool can perform as described in sections below. </p>
<p> To build a software project with CMake, <i>Generate a Project Buildsystem</i>. Optionally use <code>cmake</code> to <i>Build a Project</i>, <i>Install a Project</i> or just run the corresponding build tool (e.g. <code>make</code>) directly. <code>cmake</code> can also be used to <i>View Help</i>. </p>
<p> The other actions are meant for use by software developers writing scripts in the <code>CMake language</code> to support their builds. </p>
<p> For graphical user interfaces that may be used in place of <code>cmake</code>, see <code>ccmake</code> and <code>cmake-gui</code>. For command-line interfaces to the CMake testing and packaging facilities, see <code>ctest</code> and <code>cpack</code>. </p>
<p> For more information on CMake at large, <i>see also</i> the links at the end of this manual.</p>
<h2>INTRODUCTION TO CMAKE BUILDSYSTEMS</h2>
<p> A <i>buildsystem</i> describes how to build a project&#8217;s executables and libraries from its source code using a <i>build tool</i> to automate the process. For example, a buildsystem may be a <code>Makefile</code> for use with a command-line <code>make</code> tool or a project file for an Integrated Development Environment (IDE). In order to avoid maintaining multiple such buildsystems, a project may specify its buildsystem abstractly using files written in the <code>CMake language</code>. From these files CMake generates a preferred buildsystem locally for each user through a backend called a <i>generator</i>. </p>
<p> To generate a buildsystem with CMake, the following must be selected:</p>
<dl>
<dt><code>Source Tree</code></p>
<dd> The top-level directory containing source files provided by the project. The project specifies its buildsystem using files as described in the <code><a href="/docs/linux/man/7-cmake-language/">cmake-language</a>(7)</code> manual, starting with a top-level file named <code>CMakeLists.txt</code>. These files specify build targets and their dependencies as described in the <code><a href="/docs/linux/man/7-cmake-buildsystem/">cmake-buildsystem</a>(7)</code> manual.</p>
<dt><code>Build Tree</code></p>
<dd> The top-level directory in which buildsystem files and build output artifacts (e.g. executables and libraries) are to be stored. CMake will write a <code>CMakeCache.txt</code> file to identify the directory as a build tree and store persistent information such as buildsystem configuration options. </p>
<p> To maintain a pristine source tree, perform an <i>out-of-source</i> build by using a separate dedicated build tree. An <i>in-source</i> build in which the build tree is placed in the same directory as the source tree is also supported, but discouraged.</p>
<dt><code>Generator</code></p>
<dd> This chooses the kind of buildsystem to generate. See the <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code> manual for documentation of all generators. Run <code>cmake &#8211;help</code> to see a list of generators available locally. Optionally use the <code>-G</code> option below to specify a generator, or simply accept the default CMake chooses for the current platform. </p>
<p> When using one of the Command-Line Build Tool Generators CMake expects that the environment needed by the compiler toolchain is already configured in the shell. When using one of the IDE Build Tool Generators, no particular environment is needed.</dl>
<h2>GENERATE A PROJECT BUILDSYSTEM</h2>
<p> Run CMake with one of the following command signatures to specify the source and build trees and generate a buildsystem:</p>
<dl>
<dt><code>cmake [&lt;options&gt;] &lt;path-to-source&gt;</code></p>
<dd> Uses the current working directory as the build tree, and <code>&lt;path-to-source&gt;</code> as the source tree. The specified path may be absolute or relative to the current working directory. The source tree must contain a <code>CMakeLists.txt</code> file and must <i>not</i> contain a <code>CMakeCache.txt</code> file because the latter identifies an existing build tree. For example: </p>
<pre>
$ mkdir build ; cd build
$ cmake ../src
</pre>
<dt><code>cmake [&lt;options&gt;] &lt;path-to-existing-build&gt;</code></p>
<dd> Uses <code>&lt;path-to-existing-build&gt;</code> as the build tree, and loads the path to the source tree from its <code>CMakeCache.txt</code> file, which must have already been generated by a previous run of CMake. The specified path may be absolute or relative to the current working directory. For example: </p>
<pre>
$ cd build
$ cmake .
</pre>
<dt><code>cmake [&lt;options&gt;] -S &lt;path-to-source&gt; -B &lt;path-to-build&gt;</code></p>
<dd> Uses <code>&lt;path-to-build&gt;</code> as the build tree and <code>&lt;path-to-source&gt;</code> as the source tree. The specified paths may be absolute or relative to the current working directory. The source tree must contain a <code>CMakeLists.txt</code> file. The build tree will be created automatically if it does not already exist. For example: </p>
<pre>
$ cmake -S src -B build
</pre>
<p> In all cases the <code>&lt;options&gt;</code> may be zero or more of the <i>Options</i> below. </p>
<p> After generating a buildsystem one may use the corresponding native build tool to build the project. For example, after using the <code>Unix Makefiles</code> generator one may run <code>make</code> directly: </p>
<pre>
$ make
$ make install
</pre>
<p> Alternatively, one may use <code>cmake</code> to <i>Build a Project</i> by automatically choosing and invoking the appropriate native build tool.</dl>
<h3>Options</h3>
<dl>
<dt><code>-S &lt;path-to-source&gt;</code></p>
<dd> Path to root directory of the CMake project to build.</p>
<dt><code>-B &lt;path-to-build&gt;</code></p>
<dd> Path to directory which CMake will use as the root of build directory. </p>
<p> If the directory doesn&#8217;t already exist CMake will make it.</p>
<dt><code>-C &lt;initial-cache&gt;</code></p>
<dd> Pre-load a script to populate the cache. </p>
<p> When CMake is first run in an empty build tree, it creates a <code>CMakeCache.txt</code> file and populates it with customizable settings for the project. This option may be used to specify a file from which to load cache entries before the first pass through the project&#8217;s CMake listfiles. The loaded entries take priority over the project&#8217;s default values. The given file should be a CMake script containing <code>set()</code> commands that use the <code>CACHE</code> option, not a cache-format file. </p>
<p> References to <code>CMAKE_SOURCE_DIR</code> and <code>CMAKE_BINARY_DIR</code> within the script evaluate to the top-level source and build tree.</p>
<dt><code>-D &lt;var&gt;:&lt;type&gt;=&lt;value&gt;, -D &lt;var&gt;=&lt;value&gt;</code></p>
<dd> Create or update a CMake <code>CACHE</code> entry. </p>
<p> When CMake is first run in an empty build tree, it creates a <code>CMakeCache.txt</code> file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project&#8217;s default value. The option may be repeated for as many <code>CACHE</code> entries as desired. </p>
<p> If the <code>:&lt;type&gt;</code> portion is given it must be one of the types specified by the <code>set()</code> command documentation for its <code>CACHE</code> signature. If the <code>:&lt;type&gt;</code> portion is omitted the entry will be created with no type if it does not exist with a type already. If a command in the project sets the type to <code>PATH</code> or <code>FILEPATH</code> then the <code>&lt;value&gt;</code> will be converted to an absolute path. </p>
<p> This option may also be given as a single argument: <code>-D&lt;var&gt;:&lt;type&gt;=&lt;value&gt;</code> or <code>-D&lt;var&gt;=&lt;value&gt;</code>.</p>
<dt><code>-U &lt;globbing_expr&gt;</code></p>
<dd> Remove matching entries from CMake <code>CACHE</code>. </p>
<p> This option may be used to remove one or more variables from the <code>CMakeCache.txt</code> file, globbing expressions using <code>*</code> and <code>?</code> are supported. The option may be repeated for as many <code>CACHE</code> entries as desired. </p>
<p> Use with care, you can make your <code>CMakeCache.txt</code> non-working.</p>
<dt><code>-G &lt;generator-name&gt;</code></p>
<dd> Specify a build system generator. </p>
<p> CMake may support multiple native build systems on certain platforms. A generator is responsible for generating a particular build system. Possible generator names are specified in the <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code> manual. </p>
<p> If not specified, CMake checks the <code>CMAKE_GENERATOR</code> environment variable and otherwise falls back to a builtin default selection.</p>
<dt><code>-T &lt;toolset-spec&gt;</code></p>
<dd> Toolset specification for the generator, if supported. </p>
<p> Some CMake generators support a toolset specification to tell the native build system how to choose a compiler. See the <code>CMAKE_GENERATOR_TOOLSET</code> variable for details.</p>
<dt><code>-A &lt;platform-name&gt;</code></p>
<dd> Specify platform name if supported by generator. </p>
<p> Some CMake generators support a platform name to be given to the native build system to choose a compiler or SDK. See the <code>CMAKE_GENERATOR_PLATFORM</code> variable for details.</p>
<dt><code>&#8211;toolchain &lt;path-to-file&gt;</code></p>
<dd> Specify the cross compiling toolchain file, equivalent to setting <code>CMAKE_TOOLCHAIN_FILE</code> variable.</p>
<dt><code>&#8211;install-prefix &lt;directory&gt;</code></p>
<dd> Specify the installation directory, used by the <code>CMAKE_INSTALL_PREFIX</code> variable. Must be an absolute path.</p>
<dt><code>-Wno-dev</code></p>
<dd> Suppress developer warnings. </p>
<p> Suppress warnings that are meant for the author of the <code>CMakeLists.txt</code> files. By default this will also turn off deprecation warnings.</p>
<dt><code>-Wdev</code></p>
<dd> Enable developer warnings. </p>
<p> Enable warnings that are meant for the author of the <code>CMakeLists.txt</code> files. By default this will also turn on deprecation warnings.</p>
<dt><code>-Werror=dev</code></p>
<dd> Make developer warnings errors. </p>
<p> Make warnings that are meant for the author of the <code>CMakeLists.txt</code> files errors. By default this will also turn on deprecated warnings as errors.</p>
<dt><code>-Wno-error=dev</code></p>
<dd> Make developer warnings not errors. </p>
<p> Make warnings that are meant for the author of the <code>CMakeLists.txt</code> files not errors. By default this will also turn off deprecated warnings as errors.</p>
<dt><code>-Wdeprecated</code></p>
<dd> Enable deprecated functionality warnings. </p>
<p> Enable warnings for usage of deprecated functionality, that are meant for the author of the <code>CMakeLists.txt</code> files.</p>
<dt><code>-Wno-deprecated</code></p>
<dd> Suppress deprecated functionality warnings. </p>
<p> Suppress warnings for usage of deprecated functionality, that are meant for the author of the <code>CMakeLists.txt</code> files.</p>
<dt><code>-Werror=deprecated</code></p>
<dd> Make deprecated macro and function warnings errors. </p>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the <code>CMakeLists.txt</code> files, errors.</p>
<dt><code>-Wno-error=deprecated</code></p>
<dd> Make deprecated macro and function warnings not errors. </p>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the <code>CMakeLists.txt</code> files, not errors.</p>
<dt><code>-L[A][H]</code></p>
<dd> List non-advanced cached variables. </p>
<p> List <code>CACHE</code> variables will run CMake and list all the variables from the CMake <code>CACHE</code> that are not marked as <code>INTERNAL</code> or <code>ADVANCED</code>. This will effectively display current CMake settings, which can then be changed with <code>-D</code> option. Changing some of the variables may result in more variables being created. If <code>A</code> is specified, then it will display also advanced variables. If <code>H</code> is specified, it will also display help for each variable.</p>
<dt><code>-N</code></p>
<dd> View mode only. </p>
<p> Only load the cache. Do not actually run configure and generate steps.</p>
<dt><code>&#8211;graphviz=[file]</code></p>
<dd> Generate graphviz of dependencies, see <code>CMakeGraphVizOptions</code> for more. </p>
<p> Generate a graphviz input file that will contain all the library and executable dependencies in the project. See the documentation for <code>CMakeGraphVizOptions</code> for more details.</p>
<dt><code>&#8211;system-information [file]</code></p>
<dd> Dump information about this system. </p>
<p> Dump a wide range of information about the current system. If run from the top of a binary tree for a CMake project it will dump additional information such as the cache, log files etc.</p>
<dt><code>&#8211;log-level=&lt;ERROR|WARNING|NOTICE|STATUS|VERBOSE|DEBUG|TRACE&gt;</code></p>
<dd> Set the log level. </p>
<p> The <code>message()</code> command will only output messages of the specified log level or higher. The default log level is <code>STATUS</code>. </p>
<p> To make a log level persist between CMake runs, set <code>CMAKE_MESSAGE_LOG_LEVEL</code> as a cache variable instead. If both the command line option and the variable are given, the command line option takes precedence. </p>
<p> For backward compatibility reasons, <code>&#8211;loglevel</code> is also accepted as a synonym for this option.</p>
<dt><code>&#8211;log-context</code></p>
<dd> Enable the <code>message()</code> command outputting context attached to each message. </p>
<p> This option turns on showing context for the current CMake run only. To make showing the context persistent for all subsequent CMake runs, set <code>CMAKE_MESSAGE_CONTEXT_SHOW</code> as a cache variable instead. When this command line option is given, <code>CMAKE_MESSAGE_CONTEXT_SHOW</code> is ignored.</p>
<dt><code>&#8211;debug-trycompile</code></p>
<dd> Do not delete the <code>try_compile()</code> build tree. Only useful on one <code>try_compile()</code> at a time. </p>
<p> Do not delete the files and directories created for <code>try_compile()</code> calls. This is useful in debugging failed try_compiles. It may however change the results of the try-compiles as old junk from a previous try-compile may cause a different test to either pass or fail incorrectly. This option is best used for one try-compile at a time, and only when debugging.</p>
<dt><code>&#8211;debug-output</code></p>
<dd> Put cmake in a debug mode. </p>
<p> Print extra information during the cmake run like stack traces with <code>message(SEND_ERROR)</code> calls.</p>
<dt><code>&#8211;debug-find</code></p>
<dd> Put cmake find commands in a debug mode. </p>
<p> Print extra find call information during the cmake run to standard error. Output is designed for human consumption and not for parsing. See also the <code>CMAKE_FIND_DEBUG_MODE</code> variable for debugging a more local part of the project.</p>
<dt><code>&#8211;trace</code></p>
<dd> Put cmake in trace mode. </p>
<p> Print a trace of all calls made and from where.</p>
<dt><code>&#8211;trace-expand</code></p>
<dd> Put cmake in trace mode. </p>
<p> Like <code>&#8211;trace</code>, but with variables expanded.</p>
<dt><code>&#8211;trace-format=&lt;format&gt;</code></p>
<dd> Put cmake in trace mode and sets the trace output format. </p>
<p> <code>&lt;format&gt;</code> can be one of the following values.</p>
<dt><code>human</code></p>
<dd> Prints each trace line in a human-readable format. This is the default format.</p>
<dt><code>json-v1</code></p>
<dd> Prints each line as a separate JSON document. Each document is separated by a newline ( <code>
</code> ). It is guaranteed that no newline characters will be present inside a JSON document. </p>
<p> JSON trace format: </p>
<p>{<br />
    &#8220;file&#8221; : &#8220;/full/path/to/the/CMake/file.txt&#8221;,<br />
             &#8220;line&#8221; : 0,<br />
             &#8220;cmd&#8221; : &#8220;add_executable&#8221;,<br />
                     &#8220;args&#8221; : [ &#8220;foo&#8221;, &#8220;bar&#8221; ],<br />
                              &#8220;time&#8221; : 1579512535.9687231,<br />
                              &#8220;frame&#8221; : 2<br />
}</p>
<p> The members are:</p>
<dt><code>file</code></p>
<dd> The full path to the CMake source file where the function was called.</p>
<dt><code>line</code></p>
<dd> The line in <code>file</code> of the function call.</p>
<dt><code>defer</code></p>
<dd> Optional member that is present when the function call was deferred by <code>cmake_language(DEFER)</code>. If present, its value is a string containing the deferred call <code>&lt;id&gt;</code>.</p>
<dt><code>cmd</code></p>
<dd> The name of the function that was called.</p>
<dt><code>args</code></p>
<dd> A string list of all function parameters.</p>
<dt><code>time</code></p>
<dd> Timestamp (seconds since epoch) of the function call.</p>
<dt><code>frame</code></p>
<dd> Stack frame depth of the function that was called. </p>
<p> Additionally, the first JSON document outputted contains the <code>version</code> key for the current major and minor version of the </p>
<p> JSON trace format: </p>
<p>{<br />
    &#8220;version&#8221;:<br />
    {<br />
        &#8220;major&#8221; : 1,<br />
            &#8220;minor&#8221; : 1<br />
    }<br />
}</p>
<p> The members are:</p>
<dt><code>version</code></p>
<dd> Indicates the version of the JSON format. The version has a major and minor components following semantic version conventions.</p>
<dt><code>&#8211;trace-source=&lt;file&gt;</code></p>
<dd> Put cmake in trace mode, but output only lines of a specified file. </p>
<p> Multiple options are allowed.</p>
<dt><code>&#8211;trace-redirect=&lt;file&gt;</code></p>
<dd> Put cmake in trace mode and redirect trace output to a file instead of stderr.</p>
<dt><code>&#8211;warn-uninitialized</code></p>
<dd> Warn about uninitialized values. </p>
<p> Print a warning when an uninitialized variable is used.</p>
<dt><code>&#8211;warn-unused-vars</code></p>
<dd> Does nothing. In CMake versions 3.2 and below this enabled warnings about unused variables. In CMake versions 3.3 through 3.18 the option was broken. In CMake 3.19 and above the option has been removed.</p>
<dt><code>&#8211;no-warn-unused-cli</code></p>
<dd> Don&#8217;t warn about command line options. </p>
<p> Don&#8217;t find variables that are declared on the command line, but not used.</p>
<dt><code>&#8211;check-system-vars</code></p>
<dd> Find problems with variable usage in system files. </p>
<p> Normally, unused and uninitialized variables are searched for only in <code>CMAKE_SOURCE_DIR</code> and <code>CMAKE_BINARY_DIR</code>. This flag tells CMake to warn about other files as well.</p>
<dt><code>&#8211;profiling-output=&lt;path&gt;</code></p>
<dd> Used in conjunction with <code>&#8211;profiling-format</code> to output to a given path.</p>
<dt><code>&#8211;profiling-format=&lt;file&gt;</code></p>
<dd> Enable the output of profiling data of CMake script in the given format. </p>
<p> This can aid performance analysis of CMake scripts executed. Third party applications should be used to process the output into human readable format. </p>
<p> Currently supported values are: <code>google-trace</code> Outputs in Google Trace Format, which can be parsed by the <i>about:tracing</i> tab of Google Chrome or using a plugin for a tool like Trace Compass.</p>
<dt><code>&#8211;preset &lt;preset&gt;</code>, <code>&#8211;preset=&lt;preset&gt;</code></p>
<dd> Reads a <code>preset</code> from <code>&lt;path-to-source&gt;/CMakePresets.json</code> and <code>&lt;path-to-source&gt;/CMakeUserPresets.json</code>. The preset may specify the generator and the build directory, and a list of variables and other arguments to pass to CMake. The current working directory must contain CMake preset files. The <code>CMake GUI</code> can also recognize <code>CMakePresets.json</code> and <code>CMakeUserPresets.json</code> files. For full details on these files, see <code><a href="/docs/linux/man/7-cmake-presets/">cmake-presets</a>(7)</code>. </p>
<p> The presets are read before all other command line options. The options specified by the preset (variables, generator, etc.) can all be overridden by manually specifying them on the command line. For example, if the preset sets a variable called <code>MYVAR</code> to <code>1</code>, but the user sets it to <code>2</code> with a <code>-D</code> argument, the value <code>2</code> is preferred.</p>
<dt><code>&#8211;list-presets, &#8211;list-presets=&lt;[configure | build | test | all]&gt;</code></p>
<dd> Lists the available presets. If no option is specified only configure presets will be listed. The current working directory must contain CMake preset files.</dl>
<h2>BUILD A PROJECT</h2>
<p> CMake provides a command-line signature to build an already-generated project binary tree: </p>
<p>cmake&#8211; build&lt;dir&gt;[&lt;options&gt;][&#8211;&lt;build &#8211; tool &#8211; options&gt;] cmake&#8211; build&#8211; preset&lt;preset&gt;[&lt;options&gt;][&#8211;&lt;build &#8211; tool &#8211; options&gt;]</p>
<p> This abstracts a native build tool&#8217;s command-line interface with the following options:</p>
<dl>
<dt><code>&#8211;build &lt;dir&gt;</code></p>
<dd> Project binary directory to be built. This is required (unless a preset is specified) and must be first.</p>
<dt><code>&#8211;preset &lt;preset&gt;</code>, <code>&#8211;preset=&lt;preset&gt;</code></p>
<dd> Use a build preset to specify build options. The project binary directory is inferred from the <code>configurePreset</code> key. The current working directory must contain CMake preset files. See <code>preset</code> for more details.</p>
<dt><code>&#8211;list-presets</code></p>
<dd> Lists the available build presets. The current working directory must contain CMake preset files.</p>
<dt><code>&#8211;parallel [&lt;jobs&gt;], -j [&lt;jobs&gt;]</code></p>
<dd> The maximum number of concurrent processes to use when building. If <code>&lt;jobs&gt;</code> is omitted the native build tool&#8217;s default number is used. </p>
<p> The <code>CMAKE_BUILD_PARALLEL_LEVEL</code> environment variable, if set, specifies a default parallel level when this option is not given. </p>
<p> Some native build tools always build in parallel. The use of <code>&lt;jobs&gt;</code> value of <code>1</code> can be used to limit to a single job.</p>
<dt><code>&#8211;target &lt;tgt&gt;&#8230;, -t &lt;tgt&gt;&#8230;</code></p>
<dd> Build <code>&lt;tgt&gt;</code> instead of the default target. Multiple targets may be given, separated by spaces.</p>
<dt><code>&#8211;config &lt;cfg&gt;</code></p>
<dd> For multi-configuration tools, choose configuration <code>&lt;cfg&gt;</code>.</p>
<dt><code>&#8211;clean-first</code></p>
<dd> Build target <code>clean</code> first, then build. (To clean only, use <code>&#8211;target clean</code>.)</p>
<dt><code>&#8211;use-stderr</code></p>
<dd> Ignored. Behavior is default in CMake &gt;= 3.0.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Enable verbose output &#8211; if supported &#8211; including the build commands to be executed. </p>
<p> This option can be omitted if <code>VERBOSE</code> environment variable or <code>CMAKE_VERBOSE_MAKEFILE</code> cached variable is set.</p>
<dt><code>&#8212;</code></p>
<dd> Pass remaining options to the native tool. </p>
<p> Run <code>cmake &#8211;build</code> with no options for quick help.</dl>
<h2>INSTALL A PROJECT</h2>
<p> CMake provides a command-line signature to install an already-generated project binary tree: </p>
<pre>
cmake --install &lt;dir&gt; [&lt;options&gt;]
</pre>
<p> This may be used after building a project to run installation without using the generated build system or the native build tool. The options are:</p>
<dl>
<dt><code>&#8211;install &lt;dir&gt;</code></p>
<dd> Project binary directory to install. This is required and must be first.</p>
<dt><code>&#8211;config &lt;cfg&gt;</code></p>
<dd> For multi-configuration generators, choose configuration <code>&lt;cfg&gt;</code>.</p>
<dt><code>&#8211;component &lt;comp&gt;</code></p>
<dd> Component-based install. Only install component <code>&lt;comp&gt;</code>.</p>
<dt><code>&#8211;default-directory-permissions &lt;permissions&gt;</code></p>
<dd> Default directory install permissions. Permissions in format <code>&lt;u=rwx,g=rx,o=rx&gt;</code>.</p>
<dt><code>&#8211;prefix &lt;prefix&gt;</code></p>
<dd> Override the installation prefix, <code>CMAKE_INSTALL_PREFIX</code>.</p>
<dt><code>&#8211;strip</code></p>
<dd> Strip before installing.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Enable verbose output. </p>
<p> This option can be omitted if <code>VERBOSE</code> environment variable is set. </p>
<p> Run <code>cmake &#8211;install</code> with no options for quick help.</dl>
<h2>OPEN A PROJECT</h2>
<pre>
cmake --open &lt;dir&gt;
</pre>
<p> Open the generated project in the associated application. This is only supported by some generators.</p>
<h2>RUN A SCRIPT</h2>
<pre><code>
cmake[{-D &lt; var &gt;= &lt;value&gt;}...] - P&lt;cmake - script - file&gt;[--&lt;unparsed - options&gt;...]
</code></pre>
<p> Process the given cmake file as a script written in the CMake language. No configure or generate step is performed and the cache is not modified. If variables are defined using <code>-D</code>, this must be done before the <code>-P</code> argument. </p>
<p> Any options after <code>&#8212;</code> are not parsed by CMake, but they are still included in the set of <code>CMAKE_ARGV&lt;n&gt;</code> variables passed to the script (including the <code>&#8212;</code> itself).</p>
<h2>RUN A COMMAND-LINE TOOL</h2>
<p> CMake provides builtin command-line tools through the signature </p>
<pre>
cmake -E &lt;command&gt; [&lt;options&gt;]
</pre>
<p> Run <code>cmake -E</code> or <code>cmake -E help</code> for a summary of commands. Available commands are:</p>
<dl>
<dt><code>capabilities</code></p>
<dd> Report cmake capabilities in JSON format. The output is a JSON object with the following keys:</p>
<dt><code>version</code></p>
<dd> A JSON object with version information. Keys are:</p>
<dt><code>string</code></p>
<dd> The full version string as displayed by cmake <code>&#8211;version</code>.</p>
<dt><code>major</code></p>
<dd> The major version number in integer form.</p>
<dt><code>minor</code></p>
<dd> The minor version number in integer form.</p>
<dt><code>patch</code></p>
<dd> The patch level in integer form.</p>
<dt><code>suffix</code></p>
<dd> The cmake version suffix string.</p>
<dt><code>isDirty</code></p>
<dd> A bool that is set if the cmake build is from a dirty tree.</p>
<dt><code>generators</code></p>
<dd> A list available generators. Each generator is a JSON object with the following keys:</p>
<dt><code>name</code></p>
<dd> A string containing the name of the generator.</p>
<dt><code>toolsetSupport</code></p>
<dd> <code>true</code> if the generator supports toolsets and <code>false</code> otherwise.</p>
<dt><code>platformSupport</code></p>
<dd> <code>true</code> if the generator supports platforms and <code>false</code> otherwise.</p>
<dt><code>supportedPlatforms</code></p>
<dd> New in version 3.21. </p>
<p> Optional member that may be present when the generator supports platform specification via <code>CMAKE_GENERATOR_PLATFORM</code> (<code>-A &#8230;</code>). The value is a list of platforms known to be supported.</p>
<dt><code>extraGenerators</code></p>
<dd> A list of strings with all the extra generators compatible with the generator.</p>
<dt><code>fileApi</code></p>
<dd> Optional member that is present when the <code><a href="/docs/linux/man/7-cmake-file-api/">cmake-file-api</a>(7)</code> is available. The value is a JSON object with one member:</p>
<dt><code>requests</code></p>
<dd> A JSON array containing zero or more supported file-api requests. Each request is a JSON object with members:</p>
<dt><code>kind</code></p>
<dd> Specifies one of the supported file-api object kinds.</p>
<dt><code>version</code></p>
<dd> A JSON array whose elements are each a JSON object containing <code>major</code> and <code>minor</code> members specifying non-negative integer version components.</p>
<dt><code>serverMode</code></p>
<dd> <code>true</code> if cmake supports server-mode and <code>false</code> otherwise. Always false since CMake 3.20.</p>
<dt><code>cat &lt;files&gt;&#8230;</code></p>
<dd> Concatenate files and print on the standard output.</p>
<dt><code>chdir &lt;dir&gt; &lt;cmd&gt; [&lt;arg&gt;&#8230;]</code></p>
<dd> Change the current working directory and run a command.</p>
<dt><code>compare_files [&#8211;ignore-eol] &lt;file1&gt; &lt;file2&gt;</code></p>
<dd> Check if <code>&lt;file1&gt;</code> is same as <code>&lt;file2&gt;</code>. If files are the same, then returns <code>0</code>, if not it returns <code>1</code>. In case of invalid arguments, it returns 2. The <code>&#8211;ignore-eol</code> option implies line-wise comparison and ignores LF/CRLF differences.</p>
<dt><code>copy &lt;file&gt;&#8230; &lt;destination&gt;</code></p>
<dd> Copy files to <code>&lt;destination&gt;</code> (either file or directory). If multiple files are specified, the <code>&lt;destination&gt;</code> must be directory and it must exist. Wildcards are not supported. <code>copy</code> does follow symlinks. That means it does not copy symlinks, but the files or directories it point to.</p>
<dt><code>copy_directory &lt;dir&gt;&#8230; &lt;destination&gt;</code></p>
<dd> Copy content of <code>&lt;dir&gt;&#8230;</code> directories to <code>&lt;destination&gt;</code> directory. If <code>&lt;destination&gt;</code> directory does not exist it will be created. <code>copy_directory</code> does follow symlinks.</p>
<dt><code>copy_if_different &lt;file&gt;&#8230; &lt;destination&gt;</code></p>
<dd> Copy files to <code>&lt;destination&gt;</code> (either file or directory) if they have changed. If multiple files are specified, the <code>&lt;destination&gt;</code> must be directory and it must exist. <code>copy_if_different</code> does follow symlinks.</p>
<dt><code>create_symlink &lt;old&gt; &lt;new&gt;</code></p>
<dd> Create a symbolic link <code>&lt;new&gt;</code> naming <code>&lt;old&gt;</code>. </p>
<p> <code>NOTE:</code> Path to where <code>&lt;new&gt;</code> symbolic link will be created has to exist beforehand.</p>
<dt><code>create_hardlink &lt;old&gt; &lt;new&gt;</code></p>
<dd> Create a hard link <code>&lt;new&gt;</code> naming <code>&lt;old&gt;</code>. </p>
<p> <code>NOTE:</code> Path to where <code>&lt;new&gt;</code> hard link will be created has to exist beforehand. <code>&lt;old&gt;</code> has to exist beforehand.</p>
<dt><code>echo [&lt;string&gt;&#8230;]</code></p>
<dd> Displays arguments as text.</p>
<dt><code>echo_append [&lt;string&gt;&#8230;]</code></p>
<dd> Displays arguments as text but no new line.</p>
<dt><code>env [&#8211;unset=NAME]&#8230; [NAME=VALUE]&#8230; COMMAND [ARG]&#8230;</code></p>
<dd> Run command in a modified environment.</p>
<dt><code>environment</code></p>
<dd> Display the current environment variables.</p>
<dt><code>false</code></p>
<dd> Do nothing, with an exit code of 1.</p>
<dt><code>make_directory &lt;dir&gt;&#8230;</code></p>
<dd> Create <code>&lt;dir&gt;</code> directories. If necessary, create parent directories too. If a directory already exists it will be silently ignored.</p>
<dt><code>md5sum &lt;file&gt;&#8230;</code></p>
<dd> Create MD5 checksum of files in <code>md5sum</code> compatible format: </p>
<pre>
351abe79cd3800b38cdfb25d45015a15  file1.txt
052f86c15bbde68af55c7f7b340ab639  file2.txt
</pre>
<dt><code>sha1sum &lt;file&gt;&#8230;</code></p>
<dd> Create SHA1 checksum of files in <code>sha1sum</code> compatible format: </p>
<pre>
4bb7932a29e6f73c97bb9272f2bdc393122f86e0  file1.txt
1df4c8f318665f9a5f2ed38f55adadb7ef9f559c  file2.txt
</pre>
<dt><code>sha224sum &lt;file&gt;&#8230;</code></p>
<dd> Create SHA224 checksum of files in <code>sha224sum</code> compatible format: </p>
<pre>
b9b9346bc8437bbda630b0b7ddfc5ea9ca157546dbbf4c613192f930  file1.txt
6dfbe55f4d2edc5fe5c9197bca51ceaaf824e48eba0cc453088aee24  file2.txt
</pre>
<dt><code>sha256sum &lt;file&gt;&#8230;</code></p>
<dd> Create SHA256 checksum of files in <code>sha256sum</code> compatible format: </p>
<pre>
76713b23615d31680afeb0e9efe94d47d3d4229191198bb46d7485f9cb191acc  file1.txt
15b682ead6c12dedb1baf91231e1e89cfc7974b3787c1e2e01b986bffadae0ea  file2.txt
</pre>
<dt><code>sha384sum &lt;file&gt;&#8230;</code></p>
<dd> Create SHA384 checksum of files in <code>sha384sum</code> compatible format: </p>
<pre>
acc049fedc091a22f5f2ce39a43b9057fd93c910e9afd76a6411a28a8f2b8a12c73d7129e292f94fc0329c309df49434  file1.txt
668ddeb108710d271ee21c0f3acbd6a7517e2b78f9181c6a2ff3b8943af92b0195dcb7cce48aa3e17893173c0a39e23d  file2.txt
</pre>
<dt><code>sha512sum &lt;file&gt;&#8230;</code></p>
<dd> Create SHA512 checksum of files in <code>sha512sum</code> compatible format: </p>
<pre>
2a78d7a6c5328cfb1467c63beac8ff21794213901eaadafd48e7800289afbc08e5fb3e86aa31116c945ee3d7bf2a6194489ec6101051083d1108defc8e1dba89  file1.txt
7a0b54896fe5e70cca6dd643ad6f672614b189bf26f8153061c4d219474b05dad08c4e729af9f4b009f1a1a280cb625454bf587c690f4617c27e3aebdf3b7a2d  file2.txt
</pre>
<dt><code>remove [-f] &lt;file&gt;&#8230;</code></p>
<dd> Deprecated since version 3.17. </p>
<p> Remove the file(s). The planned behavior was that if any of the listed files already do not exist, the command returns a non-zero exit code, but no message is logged. The <code>-f</code> option changes the behavior to return a zero exit code (i.e. success) in such situations instead. <code>remove</code> does not follow symlinks. That means it remove only symlinks and not files it point to. </p>
<p> The implementation was buggy and always returned 0. It cannot be fixed without breaking backwards compatibility. Use <code>rm</code> instead.</p>
<dt><code>remove_directory &lt;dir&gt;&#8230;</code></p>
<dd> Deprecated since version 3.17. </p>
<p> Remove <code>&lt;dir&gt;</code> directories and their contents. If a directory does not exist it will be silently ignored. If <code>&lt;dir&gt;</code> is a symlink to a directory, just the symlink will be removed. Use <code>rm</code> instead.</p>
<dt><code>rename &lt;oldname&gt; &lt;newname&gt;</code></p>
<dd> Rename a file or directory (on one volume). If file with the <code>&lt;newname&gt;</code> name already exists, then it will be silently replaced.</p>
<dt><code>rm [-rRf] &lt;file&gt; &lt;dir&gt;&#8230;</code></p>
<dd> Remove the files <code>&lt;file&gt;</code> or directories <code>dir</code>. Use <code>-r</code> or <code>-R</code> to remove directories and their contents recursively. If any of the listed files/directories do not exist, the command returns a non-zero exit code, but no message is logged. The <code>-f</code> option changes the behavior to return a zero exit code (i.e. success) in such situations instead.</p>
<dt><code>server</code></p>
<dd> Launch <code><a href="/docs/linux/man/7-cmake-server/">cmake-server</a>(7)</code> mode.</p>
<dt><code>sleep &lt;number&gt;&#8230;</code></p>
<dd> Sleep for given number of seconds.</p>
<dt><code>tar [cxt][vf][zjJ] file.tar [&lt;options&gt;] [&#8211;] [&lt;pathname&gt;&#8230;]</code></p>
<dd> Create or extract a tar or zip archive. Options are:</p>
<dt><code>c</code></p>
<dd> Create a new archive containing the specified files. If used, the <code>&lt;pathname&gt;&#8230;</code> argument is mandatory.</p>
<dt><code>x</code></p>
<dd> Extract to disk from the archive. The <code>&lt;pathname&gt;&#8230;</code> argument could be used to extract only selected files or directories. When extracting selected files or directories, you must provide their exact names including the path, as printed by list (<code>-t</code>).</p>
<dt><code>t</code></p>
<dd> List archive contents. The <code>&lt;pathname&gt;&#8230;</code> argument could be used to list only selected files or directories.</p>
<dt><code>v</code></p>
<dd> Produce verbose output.</p>
<dt><code>z</code></p>
<dd> Compress the resulting archive with gzip.</p>
<dt><code>j</code></p>
<dd> Compress the resulting archive with bzip2.</p>
<dt><code>J</code></p>
<dd> Compress the resulting archive with XZ.</p>
<dt><code>&#8211;zstd</code></p>
<dd> Compress the resulting archive with Zstandard.</p>
<dt><code>&#8211;files-from=&lt;file&gt;</code></p>
<dd> Read file names from the given file, one per line. Blank lines are ignored. Lines may not start in <code>&#8211;</code> except for <code>&#8211;add-file=&lt;name&gt;</code> to add files whose names start in <code>&#8211;</code>.</p>
<dt><code>&#8211;format=&lt;format&gt;</code></p>
<dd> Specify the format of the archive to be created. Supported formats are: <code>7zip</code>, <code>gnutar</code>, <code>pax</code>, <code>paxr</code> (restricted pax, default), and <code>zip</code>.</p>
<dt><code>&#8211;mtime=&lt;date&gt;</code></p>
<dd> Specify modification time recorded in tarball entries.</p>
<dt><code>&#8212;</code></p>
<dd> Stop interpreting options and treat all remaining arguments as file names, even if they start with <code>&#8211;</code>.</p>
<dt><code>time &lt;command&gt; [&lt;args&gt;&#8230;]</code></p>
<dd> Run command and display elapsed time.</p>
<dt><code>touch &lt;file&gt;&#8230;</code></p>
<dd> Creates <code>&lt;file&gt;</code> if file do not exist. If <code>&lt;file&gt;</code> exists, it is changing <code>&lt;file&gt;</code> access and modification times.</p>
<dt><code>touch_nocreate &lt;file&gt;&#8230;</code></p>
<dd> Touch a file if it exists but do not create it. If a file does not exist it will be silently ignored.</p>
<dt><code>true</code></p>
<dd> Do nothing, with an exit code of 0.</dl>
<h3>Windows-specific Command-Line Tools</h3>
<p> The following <code>cmake -E</code> commands are available only on Windows:</p>
<dl>
<dt><code>delete_regv &lt;key&gt;</code></p>
<dd> Delete Windows registry value.</p>
<dt><code>env_vs8_wince &lt;sdkname&gt;</code></p>
<dd> Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2005.</p>
<dt><code>env_vs9_wince &lt;sdkname&gt;</code></p>
<dd> Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2008.</p>
<dt><code>write_regv &lt;key&gt; &lt;value&gt;</code></p>
<dd> Write Windows registry value.</dl>
<h2>RUN THE FIND-PACKAGE TOOL</h2>
<p> CMake provides a pkg-config like helper for Makefile-based projects: </p>
<pre>
cmake --find-package [&lt;options&gt;]
</pre>
<p> It searches a package using <code>find_package()</code> and prints the resulting flags to stdout. This can be used instead of pkg-config to find installed libraries in plain Makefile-based projects or in autoconf-based projects (via <code>share/aclocal/cmake.m4</code>). </p>
<p> <code>NOTE:</code> This mode is not well-supported due to some technical limitations. It is kept for compatibility but should not be used in new projects.</p>
<h2>VIEW HELP</h2>
<p> To print selected pages from the CMake documentation, use </p>
<pre>
cmake --help[-&lt;topic&gt;]
</pre>
<p> with one of the following options:</p>
<dl>
<dt><code>&#8211;help,-help,-usage,-h,-H,/?</code></p>
<dd> Print usage information and exit. </p>
<p> Usage describes the basic command line interface and its options.</p>
<dt><code>&#8211;version,-version,/V [&lt;f&gt;]</code></p>
<dd> Show program name/version banner and exit. </p>
<p> If a file is specified, the version is written into it. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-full [&lt;f&gt;]</code></p>
<dd> Print all help manuals and exit. </p>
<p> All manuals are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual &lt;man&gt; [&lt;f&gt;]</code></p>
<dd> Print one help manual and exit. </p>
<p> The specified manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual-list [&lt;f&gt;]</code></p>
<dd> List help manuals available and exit. </p>
<p> The list contains all manuals for which help may be obtained by using the <code>&#8211;help-manual</code> option followed by a manual name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command &lt;cmd&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one command and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual entry for <code>&lt;cmd&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command-list [&lt;f&gt;]</code></p>
<dd> List commands with help available and exit. </p>
<p> The list contains all commands for which help may be obtained by using the <code>&#8211;help-command</code> option followed by a command name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-commands [&lt;f&gt;]</code></p>
<dd> Print cmake-commands manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module &lt;mod&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one module and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual entry for <code>&lt;mod&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module-list [&lt;f&gt;]</code></p>
<dd> List modules with help available and exit. </p>
<p> The list contains all modules for which help may be obtained by using the <code>&#8211;help-module</code> option followed by a module name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-modules [&lt;f&gt;]</code></p>
<dd> Print cmake-modules manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy &lt;cmp&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one policy and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual entry for <code>&lt;cmp&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy-list [&lt;f&gt;]</code></p>
<dd> List policies with help available and exit. </p>
<p> The list contains all policies for which help may be obtained by using the <code>&#8211;help-policy</code> option followed by a policy name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policies [&lt;f&gt;]</code></p>
<dd> Print cmake-policies manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property &lt;prop&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one property and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual entries for <code>&lt;prop&gt;</code> are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property-list [&lt;f&gt;]</code></p>
<dd> List properties with help available and exit. </p>
<p> The list contains all properties for which help may be obtained by using the <code>&#8211;help-property</code> option followed by a property name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-properties [&lt;f&gt;]</code></p>
<dd> Print cmake-properties manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable &lt;var&gt; [&lt;f&gt;]</code></p>
<dd> Print help for one variable and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual entry for <code>&lt;var&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable-list [&lt;f&gt;]</code></p>
<dd> List variables with help available and exit. </p>
<p> The list contains all variables for which help may be obtained by using the <code>&#8211;help-variable</code> option followed by a variable name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variables [&lt;f&gt;]</code></p>
<dd> Print cmake-variables manual and exit. </p>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given. </p>
<p> To view the presets available for a project, use </p>
<pre>
cmake &lt;source-dir&gt; --list-presets
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </p>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Online Documentation and Community Resources</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </p>
<p> Links to available documentation and community resources may be found on this web page.</p>
<dt><code>Discourse Forum</code></p>
<dd> <i><a rel="nofollow" href="https://discourse.cmake.org">https://discourse.cmake.org</a></i> </p>
<p> The Discourse Forum hosts discussion and questions about CMake.</dl>
<h2>COPYRIGHT</h2>
<p> 2000-2022 Kitware, Inc. and Contributors </p>
<h2>Index</h2>
