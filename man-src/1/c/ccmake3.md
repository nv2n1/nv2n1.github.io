---
title: "ccmake3(1)"
name: "ccmake3"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccmake3/"
description: "ccmake – CMake Curses Dialog Command-Line Reference"
---

<h2>NAME</h2>
<p> ccmake &#8211; CMake Curses Dialog Command-Line Reference</p>
<h2>SYNOPSIS</h2>
<pre>
ccmake3 [&lt;options&gt;] (&lt;path-to-source&gt; | &lt;path-to-existing-build&gt;)
</pre>
<h2>DESCRIPTION</h2>
<p> The &quot;ccmake3&quot; executable is the CMake curses interface. Project configuration settings may be specified interactively through this GUI. Brief instructions are provided at the bottom of the terminal when the program is running. </p>
<p> CMake is a cross-platform build system generator. Projects specify their build process with platform-independent CMake listfiles included in each directory of a source tree with the name CMakeLists.txt. Users build a project by using CMake to generate a build system for a native tool on their platform.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C &lt;initial-cache&gt;</code></p>
<dd> Pre-load a script to populate the cache. </p>
<p> When cmake is first run in an empty build tree, it creates a CMakeCache.txt file and populates it with customizable settings for the project. This option may be used to specify a file from which to load cache entries before the first pass through the project&#8217;s cmake listfiles. The loaded entries take priority over the project&#8217;s default values. The given file should be a CMake script containing SET commands that use the CACHE option, not a cache-format file.</p>
<dt><code>-D &lt;var&gt;:&lt;type&gt;=&lt;value&gt;, -D &lt;var&gt;=&lt;value&gt;</code></p>
<dd> Create a cmake cache entry. </p>
<p> When cmake is first run in an empty build tree, it creates a CMakeCache.txt file and populates it with customizable settings for the project. This option may be used to specify a setting that takes priority over the project&#8217;s default value. The option may be repeated for as many cache entries as desired. </p>
<p> If the <code>:&lt;type&gt;</code> portion is given it must be one of the types specified by the <code>set()</code> command documentation for its <code>CACHE</code> signature. If the <code>:&lt;type&gt;</code> portion is omitted the entry will be created with no type if it does not exist with a type already. If a command in the project sets the type to <code>PATH</code> or <code>FILEPATH</code> then the <code>&lt;value&gt;</code> will be converted to an absolute path. </p>
<p> This option may also be given as a single argument: <code>-D&lt;var&gt;:&lt;type&gt;=&lt;value&gt;</code> or <code>-D&lt;var&gt;=&lt;value&gt;</code>.</p>
<dt><code>-U &lt;globbing_expr&gt;</code></p>
<dd> Remove matching entries from CMake cache. </p>
<p> This option may be used to remove one or more variables from the CMakeCache.txt file, globbing expressions using * and ? are supported. The option may be repeated for as many cache entries as desired. </p>
<p> Use with care, you can make your CMakeCache.txt non-working.</p>
<dt><code>-G &lt;generator-name&gt;</code></p>
<dd> Specify a build system generator. </p>
<p> CMake may support multiple native build systems on certain platforms. A generator is responsible for generating a particular build system. Possible generator names are specified in the <code><a href="/docs/linux/man/7-cmake-generators/">cmake-generators</a>(7)</code> manual.</p>
<dt><code>-T &lt;toolset-name&gt;</code></p>
<dd> Specify toolset name if supported by generator. </p>
<p> Some CMake generators support a toolset name to be given to the native build system to choose a compiler. This is supported only on specific generators: </p>
<pre>
Visual Studio &gt;= 10
Xcode &gt;= 3.0
</pre>
<p> See native build system documentation for allowed toolset names.</p>
<dt><code>-A &lt;platform-name&gt;</code></p>
<dd> Specify platform name if supported by generator. </p>
<p> Some CMake generators support a platform name to be given to the native build system to choose a compiler or SDK. This is supported only on specific generators: </p>
<pre>
Visual Studio &gt;= 8
</pre>
<p> See native build system documentation for allowed platform names.</p>
<dt><code>-Wno-dev</code></p>
<dd> Suppress developer warnings. </p>
<p> Suppress warnings that are meant for the author of the CMakeLists.txt files. By default this will also turn off deprecation warnings.</p>
<dt><code>-Wdev</code></p>
<dd> Enable developer warnings. </p>
<p> Enable warnings that are meant for the author of the CMakeLists.txt files. By default this will also turn on deprecation warnings.</p>
<dt><code>-Werror=dev</code></p>
<dd> Make developer warnings errors. </p>
<p> Make warnings that are meant for the author of the CMakeLists.txt files errors. By default this will also turn on deprecated warnings as errors.</p>
<dt><code>-Wno-error=dev</code></p>
<dd> Make developer warnings not errors. </p>
<p> Make warnings that are meant for the author of the CMakeLists.txt files not errors. By default this will also turn off deprecated warnings as errors.</p>
<dt><code>-Wdeprecated</code></p>
<dd> Enable deprecated functionality warnings. </p>
<p> Enable warnings for usage of deprecated functionality, that are meant for the author of the CMakeLists.txt files.</p>
<dt><code>-Wno-deprecated</code></p>
<dd> Suppress deprecated functionality warnings. </p>
<p> Suppress warnings for usage of deprecated functionality, that are meant for the author of the CMakeLists.txt files.</p>
<dt><code>-Werror=deprecated</code></p>
<dd> Make deprecated macro and function warnings errors. </p>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the CMakeLists.txt files, errors.</p>
<dt><code>-Wno-error=deprecated</code></p>
<dd> Make deprecated macro and function warnings not errors. </p>
<p> Make warnings for usage of deprecated macros and functions, that are meant for the author of the CMakeLists.txt files, not errors.</p>
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
<p> The <code><a href="/docs/linux/man/7-cmake-variables/">cmake-variables</a>(7)</code> manual is printed in a human-readable text format. The help is printed to a named &lt;f&gt;ile if given.</dl>
<h2>SEE ALSO</h2>
<p> The following resources are available to get help using CMake:</p>
<dl>
<dt><code>Home Page</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> </p>
<p> The primary starting point for learning about CMake.</p>
<dt><code>Frequently Asked Questions</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/Wiki/CMake_FAQ">https://cmake.org/Wiki/CMake_FAQ</a></i> </p>
<p> A Wiki is provided containing answers to frequently asked questions.</p>
<dt><code>Online Documentation</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/documentation">https://cmake.org/documentation</a></i> </p>
<p> Links to available documentation may be found on this web page.</p>
<dt><code>Mailing List</code></p>
<dd> <i><a rel="nofollow" href="https://cmake.org/mailing-lists">https://cmake.org/mailing-lists</a></i> </p>
<p> For help and discussion about using cmake, a mailing list is provided at <i>cmake [at] cmake.org</i>. The list is member-post-only but one may sign up on the CMake web page. Please first read the full documentation at <i><a rel="nofollow" href="https://cmake.org">https://cmake.org</a></i> before posting questions to the list.</dl>
<h2>COPYRIGHT</h2>
<p> 2000-2016 Kitware, Inc. </p>
<h2>Index</h2>
