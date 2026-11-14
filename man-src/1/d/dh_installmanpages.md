---
title: "dh_installmanpages(1)"
name: "dh_installmanpages"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installmanpages/"
description: "dh_installmanpages – old-style man page installer (deprecated)"
---

<h2 class="name">NAME</h2>
<p> dh_installmanpages &#8211; old-style man page installer (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installmanpages</code> [<i>debhelper options</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installmanpages</code> is a debhelper program that is responsible for automatically installing man pages into <i>usr/share/man/</i> in package build directories. </p>
<p> This is a DWIM-style program, with an interface unlike the rest of debhelper. It is deprecated, and you are encouraged to use <i><a href="/docs/linux/man/1-dh_installman/">dh_installman</a></i>(1) instead. </p>
<p> <code>dh_installmanpages</code> scans the current directory and all subdirectories for filenames that look like man pages. (Note that only real files are looked at; symlinks are ignored.) It uses <i><a href="/docs/linux/man/1-file/">file</a></i>(1) to verify that the files are in the correct format. Then, based on the files&#8217; extensions, it installs them into the correct man directory. </p>
<p> All filenames specified as parameters will be skipped by <code>dh_installmanpages</code>. This is useful if by default it installs some man pages that you do not want to be installed. </p>
<p> After the man page installation step, <code>dh_installmanpages</code> will check to see if any of the man pages are <i>.so</i> links. If so, it changes them to symlinks.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>file</i> &#8230;</p>
<dd> Do not install these files as man pages, even if they look like valid man pages.</dl>
<h2>BUGS</h2>
<p> <code>dh_installmanpages</code> will install the man pages it finds into <code>all</code> packages you tell it to act on, since it can&#8217;t tell what package the man pages belong in. This is almost never what you really want (use <code>-p</code> to work around this, or use the much better <i><a href="/docs/linux/man/1-dh_installman/">dh_installman</a></i>(1) program instead). </p>
<p> Files ending in <i>.man</i> will be ignored. </p>
<p> Files specified as parameters that contain spaces in their filenames will not be processed properly.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
