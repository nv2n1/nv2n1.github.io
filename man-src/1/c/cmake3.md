---
title: "cmake3(1)"
name: "cmake3"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cmake3/"
description: "cmake – CMake Command-Line Reference"
---

<h2>NAME</h2>
<p> cmake &#8211; CMake Command-Line Reference</p>
<h2>SYNOPSIS</h2>
<pre><code>
cmake3[&lt;options&gt;](&lt;path - to - source&gt; | &lt;path - to - existing - build&gt;)
        cmake3[(-D &lt; var &gt;= &lt;value&gt;)...] -
    P&lt;cmake - script - file&gt; cmake3-- build&lt;dir&gt;[&lt;options&gt;...][--&lt;build - tool - options&gt;...] cmake3 - E&lt;command&gt;[&lt;options&gt;...] cmake3-- find - package&lt;options&gt;...
</code></pre>
<h2>DESCRIPTION</h2>
<p> The &quot;cmake3&quot; executable is the CMake command-line interface. It may be used to configure projects in scripts. Project configuration settings may be specified on the command line with the -D option. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C &lt;initial-cache&gt;</code></dt>
<dd> Pre-load a script to populate the cache. </dd>
<p> When cmake is first run in an empty build tree, it creates a CMakeCache.txt file and populates it with customizable settings for the project. This option may be used to specify a file from which to load cache entries before the first pass through the project&#8217;s cmake listfiles. The loaded entries take priority over the project&#8217;s default values. The given file should be a CMake script containing SET commands that use the CACHE option, not a cache-format file.</p>
<dt><code>-D &lt;var&gt;:&lt;type&gt;=&lt;value&gt;, -D &lt;var&gt;=&lt;value&gt;</code></dt>
<dd> Create a cmake cache entry. </dd>
<p> When cmake is first run in an empty build tree, it creates a CMakeCache.txt file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project&#8217;s default value. The option may be repeated for as many cache entries as desired. </p>
<p> If the <code>:&lt;type&gt;</code> portion is given it must be one of the types specified by the <code>set()</code> command documentation for its <code>CACHE</code> signature. If the <code>:&lt;type&gt;</code> portion is omitted the entry will be created with no type if it does not exist with a type already. If a command in the project sets the type to <code>PATH</code> or <code>FILEPATH</code> then the <code>&lt;value&gt;</code> will be converted to an absolute path. </p>
<p> This option may also be given as a single argument: <code>-D&lt;var&gt;:&lt;type&gt;=&lt;value&gt;</code> or <code>-D&lt;var&gt;=&lt;value&gt;</code>.</p>
<dt><code>-U &lt;globbing_expr&gt;</code></dt>
<dd> Remove matching entries from CMake cache. </dd>
<p> This option may be used to remove one or more variables from the CMakeCache.txt file, globbing expressions using * and ? are supported. The option may be repeated for as many cache entries as desired. </p>
<p> Use with care, you can make your CMakeCache.txt non-working.</p>
<dt><code>-G &lt;generator-name&gt;</code></dt>
<dd> Specify a build system generator. </dd>
<p> CMake may support multiple native build systems on certain platforms. A generator is responsible for generating a particular build system. Possible generator names are specified in the <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code> manual.</p>
<dt><code>-T &lt;toolset-name&gt;</code></dt>
<dd> Specify toolset name if supported by generator. </dd>
<p> Some CMake generators support a toolset name to be given to the native build system to choose a compiler. This is supported only on specific generators: </p>
<pre>
Visual Studio &gt;= 10
Xcode &gt;= 3.0
</pre>
<p> See native build system documentation for allowed toolset names.</p>
<dt><code>-A &lt;platform-name&gt;</code></dt>
<dd> Specify platform name if supported by generator. </dd>
<p> Some CMake generators support a platform name to be given to the native build system to choose a compiler or SDK. This is supported only on specific generators: </p>
<pre>
Visual Studio &gt;= 8
</pre>
<p> See native build system documentation for allowed platform names.</p>
<dt><code>-Wno-dev</code></dt>
<dd> Suppress developer warnings. </dd>
<p> Suppress warnings that are meant for the author of the CMakeLists.txt files. By default this will also turn off deprecation warnings.</p>
<dt><code>-Wdev</code></dt>
<dd> Enable developer warnings. </dd>
<p> Enable warnings that are meant for the author of the CMakeLists.txt files. By default this will also turn on deprecation warnings.</p>
<dt><code>-Werror=dev</code></dt>
<dd> Make developer warnings errors. </dd>
<p> Make warnings that are meant for the author of the CMakeLists.txt files errors. By default this will also turn on deprecated warnings as errors.</p>
<dt><code>-Wno-error=dev</code></dt>
<dd> Make developer warnings not errors. </dd>
<p> Make warnings that are meant for the author of the CMakeLists.txt files not errors. By default this will also turn off deprecated warnings as errors.</p>
<dt><code>-Wdeprecated</code></dt>
<dd> Enable deprecated functionality warnings. </dd>
<p> Enable warnings for usage of deprecated functionality, that are meant for the author of the CMakeLists.txt files.</p>
<dt><code>-Wno-deprecated</code></dt>
<dd> Suppress deprecated functionality warnings. </dd>
<p> Suppress warnings for usage of deprecated functionality, that are meant for the author of the CMakeLists.txt files.</p>
<dt><code>-Werror=deprecated</code></dt>
<dd> Make deprecated macro and function warnings errors. </dd>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the CMakeLists.txt files, errors.</p>
<dt><code>-Wno-error=deprecated</code></dt>
<dd> Make deprecated macro and function warnings not errors. </dd>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the CMakeLists.txt files, not errors.</p>
<dt><code>-E &lt;command&gt; [&lt;options&gt;&#8230;]</code></dt>
<dd> See <i>Command-Line Tool Mode</i>.</dd>
<dt><code>-L[A][H]</code></dt>
<dd> List non-advanced cached variables. </dd>
<p> List cache variables will run CMake and list all the variables from the CMake cache that are not marked as INTERNAL or ADVANCED. This will effectively display current CMake settings, which can then be changed with -D option. Changing some of the variables may result in more variables being created. If A is specified, then it will display also advanced variables. If H is specified, it will also display help for each variable.</p>
<dt><code>&#8211;build &lt;dir&gt;</code></dt>
<dd> See <i>Build Tool Mode</i>.</dd>
<dt><code>-N</code></dt>
<dd> View mode only. </dd>
<p> Only load the cache. Do not actually run configure and generate steps.</p>
<dt><code>-P &lt;file&gt;</code></dt>
<dd> Process script mode. </dd>
<p> Process the given cmake file as a script written in the CMake language. No configure or generate step is performed and the cache is not modified. If variables are defined using -D, this must be done before the -P argument.</p>
<dt><code>&#8211;find-package</code></dt>
<dd> See <i>Find-Package Tool Mode</i>.</dd>
<dt><code>&#8211;graphviz=[file]</code></dt>
<dd> Generate graphviz of dependencies, see CMakeGraphVizOptions.cmake for more. </dd>
<p> Generate a graphviz input file that will contain all the library and executable dependencies in the project. See the documentation for CMakeGraphVizOptions.cmake for more details.</p>
<dt><code>&#8211;system-information [file]</code></dt>
<dd> Dump information about this system. </dd>
<p> Dump a wide range of information about the current system. If run from the top of a binary tree for a CMake project it will dump additional information such as the cache, log files etc.</p>
<dt><code>&#8211;debug-trycompile</code></dt>
<dd> Do not delete the try_compile build tree. Only useful on one try_compile at a time. </dd>
<p> Do not delete the files and directories created for try_compile calls. This is useful in debugging failed try_compiles. It may however change the results of the try-compiles as old junk from a previous try-compile may cause a different test to either pass or fail incorrectly. This option is best used for one try-compile at a time, and only when debugging.</p>
<dt><code>&#8211;debug-output</code></dt>
<dd> Put cmake in a debug mode. </dd>
<p> Print extra information during the cmake run like stack traces with message(send_error ) calls.</p>
<dt><code>&#8211;trace</code></dt>
<dd> Put cmake in trace mode. </dd>
<p> Print a trace of all calls made and from where.</p>
<dt><code>&#8211;trace-expand</code></dt>
<dd> Put cmake in trace mode. </dd>
<p> Like <code>&#8211;trace</code>, but with variables expanded.</p>
<dt><code>&#8211;warn-uninitialized</code></dt>
<dd> Warn about uninitialized values. </dd>
<p> Print a warning when an uninitialized variable is used.</p>
<dt><code>&#8211;warn-unused-vars</code></dt>
<dd> Warn about unused variables. </dd>
<p> Find variables that are declared or set, but not used.</p>
<dt><code>&#8211;no-warn-unused-cli</code></dt>
<dd> Don&#8217;t warn about command line options. </dd>
<p> Don&#8217;t find variables that are declared on the command line, but not used.</p>
<dt><code>&#8211;check-system-vars</code></dt>
<dd> Find problems with variable usage in system files. </dd>
<p> Normally, unused and uninitialized variables are searched for only in CMAKE_SOURCE_DIR and CMAKE_BINARY_DIR. This flag tells CMake to warn about other files as well.</p>
<dt><code>&#8211;help,-help,-usage,-h,-H,/?</code></dt>
<dd> Print usage information and exit. </dd>
<p> Usage describes the basic command line interface and its options.</p>
<dt><code>&#8211;version,-version,/V [&lt;f&gt;]</code></dt>
<dd> Show program name/version banner and exit. </dd>
<p> If a file is specified, the version is written into it. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-full [&lt;f&gt;]</code></dt>
<dd> Print all help manuals and exit. </dd>
<p> All manuals are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual &lt;man&gt; [&lt;f&gt;]</code></dt>
<dd> Print one help manual and exit. </dd>
<p> The specified manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-manual-list [&lt;f&gt;]</code></dt>
<dd> List help manuals available and exit. </dd>
<p> The list contains all manuals for which help may be obtained by using the <code>&#8211;help-manual</code> option followed by a manual name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command &lt;cmd&gt; [&lt;f&gt;]</code></dt>
<dd> Print help for one command and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual entry for <code>&lt;cmd&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-command-list [&lt;f&gt;]</code></dt>
<dd> List commands with help available and exit. </dd>
<p> The list contains all commands for which help may be obtained by using the <code>&#8211;help-command</code> option followed by a command name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-commands [&lt;f&gt;]</code></dt>
<dd> Print cmake-commands manual and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-commands/">cmake-commands</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module &lt;mod&gt; [&lt;f&gt;]</code></dt>
<dd> Print help for one module and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual entry for <code>&lt;mod&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-module-list [&lt;f&gt;]</code></dt>
<dd> List modules with help available and exit. </dd>
<p> The list contains all modules for which help may be obtained by using the <code>&#8211;help-module</code> option followed by a module name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-modules [&lt;f&gt;]</code></dt>
<dd> Print cmake-modules manual and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-modules/">cmake-modules</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy &lt;cmp&gt; [&lt;f&gt;]</code></dt>
<dd> Print help for one policy and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual entry for <code>&lt;cmp&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policy-list [&lt;f&gt;]</code></dt>
<dd> List policies with help available and exit. </dd>
<p> The list contains all policies for which help may be obtained by using the <code>&#8211;help-policy</code> option followed by a policy name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-policies [&lt;f&gt;]</code></dt>
<dd> Print cmake-policies manual and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-policies/">cmake-policies</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property &lt;prop&gt; [&lt;f&gt;]</code></dt>
<dd> Print help for one property and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual entries for <code>&lt;prop&gt;</code> are printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-property-list [&lt;f&gt;]</code></dt>
<dd> List properties with help available and exit. </dd>
<p> The list contains all properties for which help may be obtained by using the <code>&#8211;help-property</code> option followed by a property name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-properties [&lt;f&gt;]</code></dt>
<dd> Print cmake-properties manual and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-properties/">cmake-properties</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable &lt;var&gt; [&lt;f&gt;]</code></dt>
<dd> Print help for one variable and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual entry for <code>&lt;var&gt;</code> is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variable-list [&lt;f&gt;]</code></dt>
<dd> List variables with help available and exit. </dd>
<p> The list contains all variables for which help may be obtained by using the <code>&#8211;help-variable</code> option followed by a variable name. The help is printed to a named &lt;f&gt;ile if given.</p>
<dt><code>&#8211;help-variables [&lt;f&gt;]</code></dt>
<dd> Print cmake-variables manual and exit. </dd>
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</dl>
<h2>BUILD TOOL MODE</h2>
<p> CMake provides a command-line signature to build an already-generated project binary tree: </p>
<pre><code>
cmake3-- build&lt;dir&gt;[&lt;options&gt;...][--&lt;build - tool - options&gt;...]
</code></pre>
<p> This abstracts a native build tool&#8217;s command-line interface with the following options:</p>
<dl>
<dt><code>&#8211;build &lt;dir&gt;</code></dt>
<dd> Project binary directory to be built. This is required and must be first.</dd>
<dt><code>&#8211;target &lt;tgt&gt;</code></dt>
<dd> Build <code>&lt;tgt&gt;</code> instead of default targets. May only be specified once.</dd>
<dt><code>&#8211;config &lt;cfg&gt;</code></dt>
<dd> For multi-configuration tools, choose configuration <code>&lt;cfg&gt;</code>.</dd>
<dt><code>&#8211;clean-first</code></dt>
<dd> Build target <code>clean</code> first, then build. (To clean only, use <code>&#8211;target clean</code>.)</dd>
<dt><code>&#8211;use-stderr</code></dt>
<dd> Ignored. Behavior is default in CMake &gt;= 3.0.</dd>
<dt><code>&#8212;</code></dt>
<dd> Pass remaining options to the native tool. </dd>
<p> Run <code>cmake3 &#8211;build</code> with no options for quick help.</dl>
<h2>COMMAND-LINE TOOL MODE</h2>
<p> CMake provides builtin command-line tools through the signature: </p>
<pre>
cmake3 -E &lt;command&gt; [&lt;options&gt;...]
</pre>
<p> Run <code>cmake3 -E</code> or <code>cmake3 -E help</code> for a summary of commands. Available commands are:</p>
<dl>
<dt><code>chdir &lt;dir&gt; &lt;cmd&gt; [&lt;arg&gt;&#8230;]</code></dt>
<dd> Change the current working directory and run a command.</dd>
<dt><code>compare_files &lt;file1&gt; &lt;file2&gt;</code></dt>
<dd> Check if <code>&lt;file1&gt;</code> is same as <code>&lt;file2&gt;</code>. If files are the same, then returns 0, if not it returns 1.</dd>
<dt><code>copy &lt;file&gt;&#8230; &lt;destination&gt;</code></dt>
<dd> Copy files to <code>&lt;destination&gt;</code> (either file or directory). If multiple files are specified, the <code>&lt;destination&gt;</code> must be directory and it must exist.</dd>
<dt><code>copy_directory &lt;dir&gt;&#8230; &lt;destination&gt;</code></dt>
<dd> Copy directories to <code>&lt;destination&gt;</code> directory. If <code>&lt;destination&gt;</code> directory does not exist it will be created.</dd>
<dt><code>copy_if_different &lt;file&gt;&#8230; &lt;destination&gt;</code></dt>
<dd> Copy files to <code>&lt;destination&gt;</code> (either file or directory) if they have changed. If multiple files are specified, the <code>&lt;destination&gt;</code> must be directory and it must exist.</dd>
<dt><code>echo [&lt;string&gt;&#8230;]</code></dt>
<dd> Displays arguments as text.</dd>
<dt><code>echo_append [&lt;string&gt;&#8230;]</code></dt>
<dd> Displays arguments as text but no new line.</dd>
<dt><code>env [&#8211;unset=NAME]&#8230; [NAME=VALUE]&#8230; COMMAND [ARG]&#8230;</code></dt>
<dd> Run command in a modified environment.</dd>
<dt><code>environment</code></dt>
<dd> Display the current environment variables.</dd>
<dt><code>make_directory &lt;dir&gt;&#8230;</code></dt>
<dd> Create <code>&lt;dir&gt;</code> directories. If necessary, create parent directories too. If a directory already exists it will be silently ignored.</dd>
<dt><code>md5sum &lt;file&gt;&#8230;</code></dt>
<dd> Create MD5 checksum of files in <code>md5sum</code> compatible format: </dd>
<pre>
351abe79cd3800b38cdfb25d45015a15  file1.txt
052f86c15bbde68af55c7f7b340ab639  file2.txt
</pre>
<dt><code>remove [-f] &lt;file&gt;&#8230;</code></dt>
<dd> Remove the file(s), use <code>-f</code> to force it. If a file does not exist it will be silently ignored.</dd>
<dt><code>remove_directory &lt;dir&gt;</code></dt>
<dd> Remove a directory and its contents. If a directory does not exist it will be silently ignored.</dd>
<dt><code>rename &lt;oldname&gt; &lt;newname&gt;</code></dt>
<dd> Rename a file or directory (on one volume).</dd>
<dt><code>sleep &lt;number&gt;&#8230;</code></dt>
<dd> Sleep for given number of seconds.</dd>
<dt><code>tar [cxt][vf][zjJ] file.tar [&lt;options&gt;&#8230;] [&#8211;] [&lt;file&gt;&#8230;]</code></dt>
<dd> Create or extract a tar or zip archive. Options are:</dd>
<dt><code>&#8212;</code></dt>
<dd> Stop interpreting options and treat all remaining arguments as file names even if they start in <code>&#8211;</code>.</dd>
<dt><code>&#8211;files-from=&lt;file&gt;</code></dt>
<dd> Read file names from the given file, one per line. Blank lines are ignored. Lines may not start in <code>&#8211;</code> except for <code>&#8211;add-file=&lt;name&gt;</code> to add files whose names start in <code>&#8211;</code>.</dd>
<dt><code>&#8211;mtime=&lt;date&gt;</code></dt>
<dd> Specify modification time recorded in tarball entries.</dd>
<dt><code>&#8211;format=&lt;format&gt;</code></dt>
<dd> Specify the format of the archive to be created. Supported formats are: <code>7zip</code>, <code>gnutar</code>, <code>pax</code>, <code>paxr</code> (restricted pax, default), and <code>zip</code>.</dd>
<dt><code>time &lt;command&gt; [&lt;args&gt;&#8230;]</code></dt>
<dd> Run command and return elapsed time.</dd>
<dt><code>touch &lt;file&gt;</code></dt>
<dd> Touch a file.</dd>
<dt><code>touch_nocreate &lt;file&gt;</code></dt>
<dd> Touch a file if it exists but do not create it. If a file does not exist it will be silently ignored.</dd></dl>
<h3>UNIX-specific Command-Line Tools</h3>
<p> The following <code>cmake3 -E</code> commands are available only on UNIX:</p>
<dl>
<dt><code>create_symlink &lt;old&gt; &lt;new&gt;</code></dt>
<dd> Create a symbolic link <code>&lt;new&gt;</code> naming <code>&lt;old&gt;</code>.</dd></dl>
<h3>Windows-specific Command-Line Tools</h3>
<p> The following <code>cmake3 -E</code> commands are available only on Windows:</p>
<dl>
<dt><code>delete_regv &lt;key&gt;</code></dt>
<dd> Delete Windows registry value.</dd>
<dt><code>env_vs8_wince &lt;sdkname&gt;</code></dt>
<dd> Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2005.</dd>
<dt><code>env_vs9_wince &lt;sdkname&gt;</code></dt>
<dd> Displays a batch file which sets the environment for the provided Windows CE SDK installed in VS2008.</dd>
<dt><code>write_regv &lt;key&gt; &lt;value&gt;</code></dt>
<dd> Write Windows registry value.</dd></dl>
<h2>FIND-PACKAGE TOOL MODE</h2>
<p> CMake provides a helper for Makefile-based projects with the signature: </p>
<pre>
cmake3 --find-package &lt;options&gt;...
</pre>
<p> This runs in a pkg-config like mode. </p>
<p> Search a package using <code>find_package()</code> and print the resulting flags to stdout. This can be used to use cmake instead of pkg-config to find installed libraries in plain Makefile-based projects or in autoconf-based projects (via <code>share/aclocal/cmake3.m4</code>). </p>
<p> <code>NOTE:</code> This mode is not well-supported due to some technical limitations. It is kept for compatibility but should not be used in new projects.</p>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></dt>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </dd>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Frequently Asked Questions</code></dt>
<dd> <i><a rel="nofollow" href="https://cmake.org/Wiki/CMake_FAQ">https://cmake.org/Wiki/CMake_FAQ</a></i> </dd>
<p> A Wiki is provided containing answers to frequently asked questions.</p>
<dt><code>Online Documentation</code></dt>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </dd>
<p> Links to available documentation may be found on this web page.</p>
<dt><code>Mailing List</code></dt>
<dd> <i><a rel="nofollow" href="https://cmake.org/mailing-lists">https://cmake.org/mailing-lists</a></i> </dd>
<p> For help and discussion about using cmake, a mailing list is provided at <i>cmake [at] cmake.org</i>. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> before posting questions to the list.</dl>
<h2>COPYRIGHT</h2>
<p> 2000-2016 Kitware, Inc. </p>
