---
title: "dh_clean(1)"
name: "dh_clean"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_clean/"
description: "dh_clean – clean up package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_clean &#8211; clean up package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_clean</code> [<i>debhelper options</i>] [<code>-k</code>] [<code>-d</code>] [<code>-X</code><i>item</i>] [<i>path</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_clean</code> is a debhelper program that is responsible for cleaning up after a package is built. It removes the package build directories, and removes some other files including <i>debian/files</i>, and any detritus left behind by other debhelper commands. It also removes common files that should not appear in a Debian diff:<br />
&nbsp;<wbr>&nbsp;#*#&nbsp;*~&nbsp;<font SIZE="-1">DEADJOE</font>&nbsp;*.orig&nbsp;*.rej&nbsp;*.SUMS&nbsp;<font SIZE="-1">TAGS</font>&nbsp;.deps/*&nbsp;*.P&nbsp;*-stamp </p>
<p> It does not run &#8220;make clean&#8221; to clean up after the build process. Use <i><a href="/docs/linux/man/1-dh_auto_clean/">dh_auto_clean</a></i>(1) to do things like that. </p>
<p> <code>dh_clean</code> should be the last debhelper command run in the <code>clean</code> target in <i>debian/rules</i>.</p>
<h2>FILES</h2>
<dl>
<dt><i>debian/clean</i></p>
<dd> Can list other paths to be removed. </p>
<p> Note that directories listed in this file <code>must</code> end with a trailing slash. Any content in these directories will be removed as well.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> This is deprecated, use <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) instead. </p>
<p> The option is removed in compat 12.</p>
<dt><code>-d</code>, <code>&#8211;dirs-only</code></p>
<dd> Only clean the package build directories, do not clean up any other files at all.</p>
<dt><code>-X</code><i>item</i> <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being deleted, even if they would normally be deleted. You may use this option multiple times to build up a list of things to exclude.</p>
<dt><i>path</i> &#8230;</p>
<dd> Delete these <i>path</i>s too. </p>
<p> Note that directories passed as arguments <code>must</code> end with a trailing slash. Any content in these directories will be removed as well.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
