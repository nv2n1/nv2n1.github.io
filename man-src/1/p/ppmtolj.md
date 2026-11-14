---
title: "ppmtolj(1)"
name: "ppmtolj"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ppmtolj/"
description: "ppmtolj – convert a portable pixmap to an HP LaserJet PCL 5 Color file"
---

<h2 class="name">NAME</h2>
<p> ppmtolj &#8211; convert a portable pixmap to an HP LaserJet PCL 5 Color file </p>
<h2>SYNOPSIS</h2>
<p> <code>ppmtolj</code> [-gamma <i>val</i>] [<code>-resolution</code> <code>75|100|150|300|600</code>] [<code>-delta</code>] [<code>-float]</code> <code>[</code>-noreset] [<i>ppmfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> Reads a portable pixmap as input and converts it into a color file suitable to be printed by an HP color PCL 5 printer. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-delta</code></p>
<dd> Apply delta row compression to reduce the size of the pcl file.</p>
<dt><code>-gamma</code><i> int</i></p>
<dd> Gamma correct the image using the integet parameter as a gamma (default 0).</p>
<dt><code>-float</code></p>
<dd> Suppresses positioning information. The default is to write the sequence ESC&amp;l0E to the output.</p>
<dt><code>-noreset</code></p>
<dd> Prevents writing of the reset sequence to the begining and end of the output.</p>
<dt><code>-resolution</code></p>
<dd> Set the required output resolution 75|100|150|300|600</dl>
<h2>REFERENCES</h2>
<p> HP PCL 5 &amp; Color Reference Guide</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2000 by Jonathan Melvin.(jonathan.melvin [at] heywood.co.uk) </p>
<h2>Index</h2>
