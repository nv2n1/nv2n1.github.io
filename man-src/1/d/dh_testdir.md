---
title: "dh_testdir(1)"
name: "dh_testdir"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_testdir/"
description: "dh_testdir – test directory before building Debian package"
---

<h2 class="name">NAME</h2>
<p> dh_testdir &#8211; test directory before building Debian package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_testdir</code> [<i>debhelper options</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_testdir</code> tries to make sure that you are in the correct directory when building a Debian package. It makes sure that the file <i>debian/control</i> exists, as well as any other files you specify. If not, it exits with an error.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>file</i> &#8230;</p>
<dd> Test for the existence of these files too.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
