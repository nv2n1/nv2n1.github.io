---
title: "pamfile(1)"
name: "pamfile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pamfile/"
description: "pamfile – describe a Netpbm (PAM or PNM) file"
---

<h2 class="name">NAME</h2>
<p> pamfile &#8211; describe a Netpbm (PAM or PNM) file </p>
<h2>SYNOPSIS</h2>
<p> <code>pamfile</code> [<code>-allimages</code>] [<i>file &#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> Reads one or more Netpbm files as input. Writes out short descriptions of the image type, size, etc. This is mostly for use in shell scripts, so the format is not particularly pretty. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-allimages</code></p>
<dd> Describe every image in each input file. Without this option, <code>pamfile</code> describes only the first image in each input file. Note that before July 2000, a file could not contain more than one image and many programs ignore all but the first. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-pam/">pam</a></code>(5), <code><a href="/docs/linux/man/1-file/">file</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1991 by Jef Poskanzer. </p>
<h2>Index</h2>
