---
title: "bcp(1)"
name: "bcp"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcp/"
description: "bcp – extract subsets of Boost"
---

<h2 class="name">NAME</h2>
<p> bcp &#8211; extract subsets of Boost </p>
<h2>SYNOPSIS</h2>
<p> <code>bcp</code> <code>&#8211;list</code> [<i>options</i>] <i>module-list</i><br />
 <code>bcp</code> [<i>options</i>] <i>module-list output-path</i><br />
 <code>bcp</code> <code>&#8211;report</code> [<i>options</i>] <i>module-list html-file</i><br />
 <code>bcp</code> <code>&#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> Copies all the files, including dependencies, found in <i>module-list</i> to <i>output-path</i>. <i>output-path</i> must be an existing path. </p>
<p> With <code>&#8211;list</code>, prints the list of all the files in <i>module-list</i>, including dependencies. </p>
<p> With <code>&#8211;report</code>, writes the HTML report to <i>html-file</i>. </p>
<p> With <code>&#8211;help</code>, prints a quick usage reminder. </p>
<p> It is useful for Boost authors who want to distribute their library separately from Boost and for Boost users who want to distribute a subset of Boost with their application.</p>
<h3><i>module-list</i></h3>
<p> When the &#8211;scan option is not used, a list of Boost files or library names to copy. It can be:</p>
<dl>
<dt>
<dd> &#8211; The name of a tool: for example &quot;build&quot; will find &quot;tools/build&quot;.</p>
<dt>
<dd> &#8211; The name of a library: for example &quot;regex&quot;.</p>
<dt>
<dd> &#8211; The title of a header: for example &quot;scoped_ptr&quot; will find &quot;boost/scoped_ptr.hpp&quot;.</p>
<dt>
<dd> &#8211; The name of a header: for example &quot;scoped_ptr.hpp&quot; will find &quot;boost/scoped_ptr.hpp&quot;.</p>
<dt>
<dd> &#8211; The name of a file: for example &quot;boost/regex.hpp&quot;.</dl>
<p> When the &#8211;scan option is used, a list of (probably non-boost) files to scan for Boost dependencies, the files in the module list are not therefore copied/listed.</p>
<h3>File dependencies</h3>
<p> C++ source files are scanned for #includes, all #includes present in the Boost source tree will then be scanned for their dependencies and so on. </p>
<p> C++ source files are associated with the name of a library, if that library has source code (and possibly build data), then include that source in the dependencies. </p>
<p> C++ source files are checked for dependencies on Boost.Test (for example to see if they use cpp_main as an entry point). </p>
<p> HTML files are scanned for immediate dependencies (images and style sheets, but not links).</p>
<h3>HTML report contains:</h3>
<p> &#8211; all the licenses in effect, plus the files using each license, and the copyright holders using each license </p>
<p> &#8211; any files with no recognizable license (please report these to the Boost mailing lists) </p>
<p> &#8211; any files with no recognizable copyright holders (please report these to the Boost mailing lists) </p>
<p> &#8211; all the copyright holders and the files on which they hold copyright </p>
<p> &#8211; file dependency information &#8211; indicates the reason for the inclusion of any particular file in the dependencies found</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;boost</code>=<i>path</i></p>
<dd> sets the location of the Boost tree to path</p>
<dt><code>&#8211;scan</code></p>
<dd> treat the module list as a list of (possibly non-boost) files to scan for Boost dependencies</p>
<dt><code>&#8211;cvs</code></p>
<dd> only copy files under CVS version control</p>
<dt><code>&#8211;unix-lines</code></p>
<dd> make sure that all copied files use Unix style line endings</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>bcp</code> scoped_ptr /foo</p>
<dd> Copies boost/scoped_ptr.hpp and dependencies to /foo.</p>
<dt><code>bcp</code> boost/regex.hpp /foo</p>
<dd> Copies boost/regex.hpp and all dependencies including the regex source code (in libs/regex/src) and build files (in libs/regex/build) to /foo. Does not copy the regex documentation, test or example code.</p>
<dt><code>bcp</code> regex /foo</p>
<dd> Copies the full regex lib (in libs/regex) including dependencies (such as the Boost.Test source required by the regex test programs) to /foo.</p>
<dt><code>bcp</code> regex config build /foo</p>
<dd> Copies the full regex lib (in libs/regex) plus the config lib (libs/config) and the build system (tools/build) to /foo including all the dependencies.</p>
<dt><code>bcp &#8211;scan &#8211;boost</code>=/boost foo.cpp bar.cpp boost</p>
<dd> Scans the [non-boost] files foo.cpp and bar.cpp for Boost dependencies and copies those dependencies to the sub-directory boost.</p>
<dt><code>bcp &#8211;report</code> regex.hpp boost-regex-report.html</p>
<dd> Creates a HTML report called boost-regex-report.html for the Boost module regex.hpp.</dl>
<h2>AUTHORS</h2>
<p> Author of bcp is John Maddock. </p>
<p> Author of this manpage is Domenico Andreoli, who copied stuff from bcp &#8211;help and the HTML documentation. </p>
<h2>Index</h2>
<dt><a href="#lbAH">OPTIONS</a></p>
<dd>
<dt><a href="#lbAI">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAJ">AUTHORS</a></p>
<dd></dl>
