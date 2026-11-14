---
title: "achfile(1)"
name: "achfile"
section: "1"
letter: "a"
url: "/docs/linux/man/1-achfile/"
description: "achfile – change type and/or creator of Apple Macintosh files (netatalk format)"
---

<h2 class="name">NAME</h2>
<p> achfile &#8211; change type and/or creator of Apple Macintosh files (netatalk format) </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>achfile</code> [-t&nbsp;<wbr><i>type</i>] [-c&nbsp;<wbr><i>creator</i>] <i>file</i>&#8230;</dl>
<h2>DESCRIPTION</h2>
<p> <code>achfile</code></p>
<dd>changes the Macintosh type and/or creator of the <i>file</i> arguments which have a corresponding .AppleDouble file.</p>
<h2>OPTIONS</h2>
<p> <code>-t</code> <i>type</i> change the type. </p>
<p> <code>-c</code> <i>creator</i> change the creator.</p>
<h2>DIAGNOSTICS</h2>
<p> returns exit status 0 if all files changed successfully</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afile/">afile</a></code>(1), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
<h2>Index</h2>
