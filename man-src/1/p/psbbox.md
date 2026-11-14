---
title: "psbbox(1)"
name: "psbbox"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psbbox/"
description: "psbbox.sh – Replace BoundingBox line in PostScript files by \"real\" BoundingBox"
---

<h2>NAME</h2>
<p> psbbox.sh &#8211; Replace BoundingBox line in PostScript files by &quot;real&quot; BoundingBox</p>
<h2>SYNOPSIS</h2>
<p> <code>psbbox.sh</code> <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> This program replaces the BoundingBox line in all PostScript files specified on the command line by a BoundingBox determined by the bbox modules of Ghostscript.</p>
<h2>KNOWN LIMITATIONS</h2>
<p> Works only for single-page PostScript files. Other limitations are the limitations of the Ghostscript bbox module.<br />
 EPS Ghostscript 7.07 occasionally produces no BoundingBox at all. Try using AFPL Ghostscipt 8.00 or later instead.</p>
<h2>OBSOLETE</h2>
<p> With the production of <code>ps2raster</code>, this script became obsolete.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-ps2raster/">ps2raster</a></i>(1) </p>
<h2>Index</h2>
