---
title: "kpsereadlink(1)"
name: "kpsereadlink"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpsereadlink/"
description: "kpsereadlink – print contents of symbolic link"
---

<h2 class="name">NAME</h2>
<p> kpsereadlink &#8211; print contents of symbolic link </p>
<h2>SYNOPSIS</h2>
<p> <code>kpsereadlink</code> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> If <i>file</i> is a symbolic link, print its contents (what it links to), and exit successfully. Exit with a failure otherwise. </p>
<p> On systems that do not support symbolic links, <code>kpsereadlink</code> will always fail.</p>
<h2>OPTIONS</h2>
<p> <code>kpsereadlink</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2) </p>
<h2>Index</h2>
