---
title: "dh_installdirs(1)"
name: "dh_installdirs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installdirs/"
description: "dh_installdirs – create subdirectories in package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installdirs &#8211; create subdirectories in package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installdirs</code> [<i>debhelper options</i>] [<code>-A</code>] [<i>dir</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installdirs</code> is a debhelper program that is responsible for creating subdirectories in package build directories. </p>
<p> Many packages can get away with omitting the call to <code>dh_installdirs</code> completely. Notably, other <code>dh_*</code> commands are expected to create directories as needed.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.dirs</p>
<dd> Lists directories to be created in <i>package</i>. </p>
<p> Generally, there is no need to list directories created by the upstream build system or directories needed by other <code>debhelper</code> commands.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Create any directories specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on, not just the first.</p>
<dt><i>dir</i> &#8230;</p>
<dd> Create these directories in the package build directory of the first package acted on. (Or in all packages if <code>-A</code> is specified.)</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
