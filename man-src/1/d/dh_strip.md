---
title: "dh_strip(1)"
name: "dh_strip"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_strip/"
description: "dh_strip – strip executables, shared libraries, and some static libraries"
---

<h2 class="name">NAME</h2>
<p> dh_strip &#8211; strip executables, shared libraries, and some static libraries </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_strip</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>] [<code>&#8211;dbg-package=</code><i>package</i>] [<code>&#8211;keep-debug</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_strip</code> is a debhelper program that is responsible for stripping executables, shared libraries, and static libraries that are not used for debugging. </p>
<p> This program examines your package build directories and works out what to strip on its own. It uses <i><a href="/docs/linux/man/1-file/">file</a></i>(1) and file permissions and filenames to figure out what files are shared libraries (<i>*.so</i>), executable binaries, and static (<i>lib*.a</i>) and debugging libraries (<i>lib*_g.a</i>, <i>debug/*.so</i>), and strips each as much as is possible. (Which is not at all for debugging libraries.) In general it seems to make very good guesses, and will do the right thing in almost all cases. </p>
<p> Since it is very hard to automatically guess if a file is a module, and hard to determine how to strip a module, <code>dh_strip</code> does not currently deal with stripping binary modules such as <i>.o</i> files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being stripped. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><code>&#8211;dbg-package=</code><i>package</i></p>
<dd> <code>This option is a now special purpose option that you normally do not need</code>. In most cases, there should be little reason to use this option for new source packages as debhelper automatically generates debug packages (&#8220;dbgsym packages&#8221;). <code>If you have a manual &#8211;dbg-package</code> that you want to replace with an automatically generated debug symbol package, please see the <code>&#8211;dbgsym-migration</code> option. </p>
<p> Causes <code>dh_strip</code> to save debug symbols stripped from the packages it acts on as independent files in the package build directory of the specified debugging package. </p>
<p> For example, if your packages are libfoo and foo and you want to include a <i>foo-dbg</i> package with debugging symbols, use <code>dh_strip &#8211;dbg-package=</code><i>foo-dbg</i>. </p>
<p> This option implies <code>&#8211;no-automatic-dbgsym</code> and <i>cannot</i> be used with <code>&#8211;automatic-dbgsym</code> or <code>&#8211;dbgsym-migration</code>.</p>
<dt><code>-k</code>, <code>&#8211;keep-debug</code></p>
<dd> <code>This option is a now special purpose option that you normally do not need</code>. In most cases, there should be little reason to use this option for new source packages as debhelper automatically generates debug packages (&#8220;dbgsym packages&#8221;). <code>If you have a manual &#8211;dbg-package</code> that you want to replace with an automatically generated debug symbol package, please see the <code>&#8211;dbgsym-migration</code> option. </p>
<p> Debug symbols will be retained, but split into an independent file in <i>usr/lib/debug/</i> in the package build directory. <code>&#8211;dbg-package</code> is easier to use than this option, but this option is more flexible. </p>
<p> This option implies <code>&#8211;no-automatic-dbgsym</code> and <i>cannot</i> be used with <code>&#8211;automatic-dbgsym</code>.</p>
<dt><code>&#8211;dbgsym-migration=</code><i>package-relation</i></p>
<dd> This option is used to migrate from a manual &#8220;-dbg&#8221; package (created with <code>&#8211;dbg-package</code>) to an automatic generated debug symbol package. This option should describe a valid <code>Replaces</code>&#8211; and <code>Breaks</code>-relation, which will be added to the debug symbol package to avoid file conflicts with the (now obsolete) -dbg package. </p>
<p> This option implies <code>&#8211;automatic-dbgsym</code> and <i>cannot</i> be used with <code>&#8211;keep-debug</code>, <code>&#8211;dbg-package</code> or <code>&#8211;no-automatic-dbgsym</code>. </p>
<p> Examples: </p>
<pre>
  dh_strip --dbgsym-migration='libfoo-dbg (&lt;&lt; 2.1-3~)'
  dh_strip --dbgsym-migration='libfoo-tools-dbg (&lt;&lt; 2.1-3~), libfoo2-dbg (&lt;&lt; 2.1-3~)'
</pre>
<dt><code>&#8211;automatic-dbgsym</code>, <code>&#8211;no-automatic-dbgsym</code></p>
<dd> Control whether <code>dh_strip</code> should be creating debug symbol packages when possible. </p>
<p> The default is to create debug symbol packages.</p>
<dt><code>&#8211;ddebs</code>, <code>&#8211;no-ddebs</code></p>
<dd> Historical name for <code>&#8211;automatic-dbgsym</code> and <code>&#8211;no-automatic-dbgsym</code>.</p>
<dt><code>&#8211;ddeb-migration=</code><i>package-relation</i></p>
<dd> Historical name for <code>&#8211;dbgsym-migration</code>.</dl>
<h2>NOTES</h2>
<p> If the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable contains <code>nostrip</code>, nothing will be stripped, in accordance with Debian policy (section 10.1 &#8220;Binaries&#8221;). This will also inhibit the automatic creation of debug symbol packages. </p>
<p> The automatic creation of debug symbol packages can also be prevented by adding <code>noautodbgsym</code> to the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable. However, <code>dh_strip</code> will still add debuglinks to <font SIZE="-1">ELF</font> binaries when this flag is set. This is to ensure that the regular deb package will be identical with and without this flag (assuming it is otherwise &#8220;bit-for-bit&#8221; reproducible).</p>
<h2>CONFORMS TO</h2>
<p> Debian policy, version 3.0.1</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
