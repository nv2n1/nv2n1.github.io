---
title: "gyp(1)"
name: "gyp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gyp/"
description: "gyp – cross-platform makefile generator for Chromium"
---

<h2 class="name">NAME</h2>
<p> gyp &#8211; cross-platform makefile generator for Chromium </p>
<h2>SYNOPSIS</h2>
<p> <i>gyp</i> [options] [build_file&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Uses the specified build files to generate build scripts or project files in the current platform&#8217;s native format. If no build file is specified, all files in the current directory with a .gyp suffix are used.</p>
<h2>OPTIONS</h2>
<p> -D&lt;variable&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Provide a default value for the given variable. This supplements settings from the <i>GYP_DEFINES</i> environment variable, which should be a space-separated list of &lt;variable&gt;=&lt;value&gt; pairs.</dl>
<p> -f&lt;format&gt;[(,&lt;format&gt;)&#8230;], &#8211;format=&lt;format&gt;[(,&lt;format&gt;)&#8230;]</p>
<dl>
<dt>
<dd> Generate output in the formats listed. Valid formats include make (GNU makefile), xcode (Xcode project file), msvs (Visual Studio project file), scons (SCons rule set), and gypd (<i>gyp</i> input, for debugging). </p>
<p> Defaults to the value of the <i>GYP_GENERATORS</i> environment variable, which should be a comma-separated list of formats, or the platform&#8217;s native format if unset (<i>xcode</i> for Mac OS X, <i>msvs</i> for Windows, including Cygwin, <i>make</i> for other Unix).</dl>
<p> -I&lt;path&gt;, &#8211;include=&lt;path&gt;</p>
<dl>
<dt>
<dd> Implicitly include the contents of the <i>&lt;path&gt;</i> file in all loaded .gyp files.</dl>
<p> &#8211;depth=&lt;path&gt;</p>
<dl>
<dt>
<dd> For Chromium, the gyp &quot;depth&quot; variable should always be a relative path to Chromium&#8217;s top-level src directory. This option allows one to specify a path the DEPTH variable should be set relative to. </p>
<p> Defaults to the first directory named src found as an ancestor of one of the build files passed on the command line.</dl>
<p> -d&lt;debug mode&gt;, &#8211;debug=&lt;debug mode&gt;</p>
<dl>
<dt>
<dd> Turn on debugging output. Valid debugging modes include &quot;general&quot; to list options used, &quot;variables&quot; to trace variable expansion, and &quot;includes&quot; to trace build file include directives.</dl>
<p> -S&lt;suffix&gt;, &#8211;suffix=&lt;suffix&gt;</p>
<dl>
<dt>
<dd> Insert the specified string in the names of generated files before the standard extension. For example, with the <i>make</i> backend and a suffix of &quot;.foo&quot;, <i>gyp</i> will write the main makefile to Makefile.foo and target-specific snippets to target.foo.mk.</dl>
<p> -G&lt;flag&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set a &quot;generator flag&quot;, which is an option specific to the particular output format. All generator flags have names beginning with the name of the output format. This supplements the <i>GYP_GENERATOR_FLAGS</i> environment variable, which should be a space-separated list of &lt;flag&gt;=&lt;value&gt; pairs.</dl>
<p> &#8211;generator-output=&lt;dir&gt;</p>
<dl>
<dt>
<dd> Write the generated build files under the &lt;dir&gt; directory and adjust paths accordingly. This allows building in a separate directory from the source files. </p>
<p> This overrides the <i>GYP_GENERATOR_OUTPUT</i> environment variable.</dl>
<p> &#8211;ignore-environment</p>
<dl>
<dt>
<dd> Do not read options from environment variables.</dl>
<p> &#8211;check</p>
<dl>
<dt>
<dd> Take extra time to verify the syntax of each <i>build_file</i>.</dl>
<p> &#8211;parallel</p>
<dl>
<dt>
<dd> Use multiprocessing for speed (experimental).</dl>
<p> &#8211;toplevel-dir=&lt;dir&gt;</p>
<dl>
<dt>
<dd> Directory to use as the root of the source tree.</dl>
<p> &#8211;build=&lt;configs&gt;</p>
<dl>
<dt>
<dd> Configuration for build after project generation.</dl>
<p> &#8211;no-circular-check</p>
<dl>
<dt>
<dd> Disable the check for circular relationships between .gyp files. These relationships should not exist, but they&#8217;ve only been observed to be harmful with the Xcode output format. Chromium&#8217;s .gyp files currently have some circular relationships on non-Mac platforms, so this option allows the strict behavior to be used on Macs and the lenient behavior to be used elsewhere. </p>
<p> This option is likely to be removed once all circular relationships in Chromium are eliminated.</dl>
<h2>ENVIRONMENT</h2>
<p> GYP_DEFINES, GYP_GENERATORS, GYP_GENERATOR_FLAGS, GYP_GENERATOR_OUTPUT</p>
<dl>
<dt>
<dd> See the -D, &#8211;format, -G, and &#8211;generator-output options.</dl>
<h2>FILES</h2>
<p> ~/.gyp/include.gypi</p>
<dl>
<dt>
<dd> Implicitly included before anything else in every .gyp file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-qmake/">qmake</a></code>(1), <code><a href="/docs/linux/man/1-cmake/">cmake</a></code>(1) </p>
<h2>Index</h2>
