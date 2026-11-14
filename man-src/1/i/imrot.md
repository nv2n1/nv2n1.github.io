---
title: "imrot(1)"
name: "imrot"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imrot/"
description: "imrot – Rotate and/or Reflect FITS and IRAF image files"
---

<h2>Name</h2>
<p> imrot &#8211; Rotate and/or Reflect FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> imrot [options] Fits or IRAF file(s)</p>
<h2>Description</h2>
<p> <i>imrot</i> is a utility for rotating and/or reflecting FITS or IRAF images. Images can be rotated only in multiples of 90 degrees. The image may be output with a different data type than that in which it is input, and IRAF files may be written out as FITS files.</p>
<h2>Options</h2>
<p> <code>-a</code> Mirror if IRAF image WCS says to <code>-f</code> Write FITS image from IRAF input <code>-l</code> Reflect image across vertical axis <code>-o</code> Allow overwriting of input image, else write new one <code>-r &lt;angle&gt;</code> Image rotation angle in degrees (default 0) <code>-s</code> Split multi-extension FITS file <code>-v</code> Verbose <code>-x &lt;num&gt;</code> Output pixel size in bits (FITS code, default=input) Allowed values are 8, 16, 32 for integers, -16 for unsigned integers, and -32 and -64 for 4- and 8-byte floating point numbers </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
