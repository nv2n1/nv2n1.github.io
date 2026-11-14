---
title: "dh_fixperms(1)"
name: "dh_fixperms"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_fixperms/"
description: "dh_fixperms – fix permissions of files in package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_fixperms &#8211; fix permissions of files in package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_fixperms</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_fixperms</code> is a debhelper program that is responsible for setting the permissions of files and directories in package build directories to a sane state &#8212; a state that complies with Debian policy. </p>
<p> <code>dh_fixperms</code> makes all files in <i>usr/share/doc</i> in the package build directory (excluding files in the <i>examples/</i> directory) be mode 644. It also changes the permissions of all man pages to mode 644. It removes group and other write permission from all files. It removes execute permissions from any libraries, headers, Perl modules, or desktop files that have it set. It makes all files in the standard <i>bin</i> and <i>sbin</i> directories, <i>usr/games/</i> and <i>etc/init.d</i> executable (since v4). Finally, it removes the setuid and setgid bits from all files in the package. </p>
<p> When the <i>Rules-Requires-Root</i> field has the (effective) value of <i>binary-targets</i>, <code>dh_fixperms</code> will also reset the ownership of all paths to &#8220;root:root&#8221;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude</code> <i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from having their permissions changed. You may use this option multiple times to build up a list of things to exclude.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
