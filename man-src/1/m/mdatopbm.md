---
title: "mdatopbm(1)"
name: "mdatopbm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdatopbm/"
description: "mdatopbm – convert a Microdesign .mda or .mdp file into a portable bitmap"
---

<h2 class="name">NAME</h2>
<p> mdatopbm &#8211; convert a Microdesign .mda or .mdp file into a portable bitmap </p>
<h2>SYNOPSIS</h2>
<p> <code>mdatopbm</code> [<code>-a</code>][<code>-d</code>][<code>-i</code>][<code>&#8212;</code>] <i>[ mdafile ]</i></p>
<h2>DESCRIPTION</h2>
<p> Reads a MicroDesign file as input. Reads from stdin if input file is omitted. Produces a portable bitmap as output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Output the PBM in ASCII rather than binary.</p>
<dt><code>-d</code></p>
<dd> Double the height of the output file, to compensate for the aspect ratio used in MicroDesign files.</p>
<dt><code>-i</code></p>
<dd> Invert the colours used.</p>
<dt><code>&#8212;</code></p>
<dd> End of options (use this if the filename starts with &quot;-&quot;)</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pbmtomda/">pbmtomda</a>(1), <a href="/docs/linux/man/5-pbm/">pbm</a>(5)</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 1999 John Elliott &lt;jce [at] seasip.demon.co.uk&gt;. </p>
<h2>Index</h2>
