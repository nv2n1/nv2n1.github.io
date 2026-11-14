---
title: "dvdunauthor(1)"
name: "dvdunauthor"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdunauthor/"
description: "dvdunauthor – Decodes DVD-Video file structure"
---

<h2 class="name">NAME</h2>
<p> dvdunauthor &#8211; Decodes DVD-Video file structure </p>
<h2>SYNOPSIS</h2>
<p> <code>dvdunauthor</code> [ <code>path</code> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>dvdunauthor</code> decodes the specified DVD-Video directory structure, putting into the current directory an XML control file and corresponding MPEG-2 files (with a .vob extension) that <code>dvdauthor</code> can (hopefully) interpret to recreate the DVD-Video directory structure.</p>
<h2>USAGE</h2>
<p> <code>dvdunauthor</code> path</p>
<h2>CAVEATS</h2>
<p> None.</p>
<h2>BUGS</h2>
<p> Depends on libdvdread to decode the DVD-Video structure and to report any errors trying to do so. But libdvdread will sometimes just exit without reporting any error.</p>
<h2>AUTHOR</h2>
<p> MarcLeemanThis manual page was written by Marc Leeman &lt;marc.leeman [at] gmail.com&gt;, for the Debian GNU/Linux system (but may be used by others). &lt;marc.leeman [at] gmail.com&gt; MarcLeeman2003Marc Leeman </p>
<h2>Index</h2>
