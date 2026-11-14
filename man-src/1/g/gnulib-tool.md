---
title: "gnulib-tool(1)"
name: "gnulib-tool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnulib-tool/"
description: "gnulib-tool – program for authors or maintainers which want to import modules from gnulib into their packages."
---

<h2 class="name">NAME</h2>
<p> gnulib-tool &#8211; program for authors or maintainers which want to import modules from gnulib into their packages.</p>
<h2>SYNOPSIS</h2>
<p> <code>gnulib-tool</code> &#8211;list </p>
<p> <code>gnulib-tool</code> &#8211;import [module1 &#8230; moduleN] </p>
<p> <code>gnulib-tool</code> &#8211;update </p>
<p> <code>gnulib-tool</code> &#8211;create-testdir &#8211;dir=directory module1 &#8230; moduleN </p>
<p> <code>gnulib-tool</code> &#8211;create-megatestdir &#8211;dir=directory [module1 &#8230; moduleN] </p>
<p> <code>gnulib-tool</code> &#8211;test &#8211;dir=directory module1 &#8230; moduleN </p>
<p> <code>gnulib-tool</code> &#8211;megatest &#8211;dir=directory [module1 &#8230; moduleN] </p>
<p> <code>gnulib-tool</code> &#8211;extract-description module </p>
<p> <code>gnulib-tool</code> &#8211;extract-filelist module </p>
<p> <code>gnulib-tool</code> &#8211;extract-dependencies module </p>
<p> <code>gnulib-tool</code> &#8211;extract-autoconf-snippet module </p>
<p> <code>gnulib-tool</code> &#8211;extract-automake-snippet module </p>
<p> <code>gnulib-tool</code> &#8211;extract-include-directive module </p>
<p> <code>gnulib-tool</code> &#8211;extract-license module </p>
<p> <code>gnulib-tool</code> &#8211;extract-maintainer module </p>
<p> <code>gnulib-tool</code> &#8211;extract-tests-module module </p>
<h2>DESCRIPTION</h2>
<p> The GNU portability library is a macro system and C declarations and definitions for commonly-used API elements and abstracted system behaviors. It can be used to improve portability and other functionality in your programs. </p>
<h2>OPTIONS</h2>
<p> Operation modes:</p>
<dl>
<dt><code>&#8211;list</code></p>
<dd> print the available module names.</p>
<dt><code>&#8211;import</code></p>
<dd> import the given modules into the current package; if no modules are specified, update the current package from the current gnulib.</p>
<dt><code>&#8211;update</code></p>
<dd> update the current package, restore files omitted from CVS.</p>
<dt><code>&#8211;create-testdir</code></p>
<dd> create a scratch package with the given modules.</p>
<dt><code>&#8211;create-megatestdir</code></p>
<dd> create a mega scratch package with the given modules one by one and all together.</p>
<dt><code>&#8211;test</code></p>
<dd> test the combination of the given modules (recommended to use CC=&quot;gcc -Wall&quot; here).</p>
<dt><code>&#8211;megatest</code></p>
<dd> test the given modules one by one and all together (recommended to use CC=&quot;gcc -Wall&quot; here).</p>
<dt><code>&#8211;extract-description</code></p>
<dd> extract the description.</p>
<dt><code>&#8211;extract-filelist</code></p>
<dd> extract the list of files.</p>
<dt><code>&#8211;extract-dependencies</code></p>
<dd> extract the dependencies.</p>
<dt><code>&#8211;extract-autoconf-snippet</code></p>
<dd> extract the snippet for configure.ac.</p>
<dt><code>&#8211;extract-automake-snippet</code></p>
<dd> extract the snippet for lib/Makefile.am.</p>
<dt><code>&#8211;extract-include-directive</code></p>
<dd> extract the #include directive.</p>
<dt><code>&#8211;extract-license</code></p>
<dd> report the license terms of the source files under lib/.</p>
<dt><code>&#8211;extract-maintainer</code></p>
<dd> report the maintainer(s) inside gnulib.</p>
<dt><code>&#8211;extract-tests-module</code></p>
<dd> report the unit test module, if it exists.</dl>
<p> Options:</p>
<dl>
<dt><code>&#8211;dir=DIRECTORY</code></p>
<dd> specify the target directory. For &#8211;import, this specifies where your configure.ac can be found. Defaults to current directory.</p>
<dt><code>&#8211;lib=LIBRARY</code></p>
<dd> Specify the library name. Defaults to &#8216;libgnu&#8217;.</p>
<dt><code>&#8211;source-base=DIRECTORY</code></p>
<dd> Directory relative &#8211;dir where source code is placed (default &quot;lib&quot;), for &#8211;import.</p>
<dt><code>&#8211;m4-base=DIRECTORY</code></p>
<dd> Directory relative &#8211;dir where *.m4 macros are placed (default &quot;m4&quot;), for &#8211;import.</p>
<dt><code>&#8211;tests-base=DIRECTORY</code></p>
<dd> Directory relative &#8211;dir where unit tests are placed (default &quot;tests&quot;), for &#8211;import.</p>
<dt><code>&#8211;aux-dir=DIRECTORY</code></p>
<dd> Directory relative &#8211;dir where auxiliary build tools are placed (default &quot;build-aux&quot;).</p>
<dt><code>&#8211;with-tests</code></p>
<dd> Include unit tests for the included modules.</p>
<dt><code>&#8211;avoid=MODULE</code></p>
<dd> Avoid including the given MODULE. Useful if you have code that provides equivalent functionality. This option can be repeated.</p>
<dt><code>&#8211;lgpl</code></p>
<dd> Abort if modules aren&#8217;t available under the LGPL. Also modify license template from GPL to LGPL.</p>
<dt><code>&#8211;libtool</code></p>
<dd> Use libtool rules, for &#8211;import.</p>
<dt><code>&#8211;macro-prefix=PREFIX</code></p>
<dd> Specify the prefix of the macros &#8216;gl_EARLY&#8217; and &#8216;gl_INIT&#8217;. Default is &#8216;gl&#8217;.</p>
<dt><code>&#8211;no-changelog</code></p>
<dd> don&#8217;t update or create ChangeLog files.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> For &#8211;import, only print what would have been done.</p>
<dt><code>-s, &#8211;symbolic, &#8211;symlink</code></p>
<dd> Make symbolic links instead of copying files.</dl>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;bug-gnulib [at] gnu.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-check-module/">check-module</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> gnulib was written by the Free Software Foundation and others (sources of various origins). </p>
<p> This manual page was written by Daniel Baumann &lt;daniel [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
