---
title: "imhead(1)"
name: "imhead"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imhead/"
description: "imhead – Print FITS or IRAF image header"
---

<h2>Name</h2>
<p> imhead &#8211; Print FITS or IRAF image header</p>
<h2>Synopsis</h2>
<p> imhead [options] FITS or IRAF filename</p>
<h2>Description</h2>
<p> <i>imhead</i> is a utility for listing IRAF and FITS image headers. It converts IRAF .imh image headers to a FITS format before listing them. For IRAF files, the BITPIX, NAXIS, NAXIS1, NAXIS2, OBJECT, and PIXFILE keywords are set from the binary portion of the header. IMHFILE is set from the actual filename for internal purposes.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd> Write exact FITS header, with no inserted newlines and including trailing blanks</p>
<dt><code>-v</code></p>
<dd> Print name of file and program version before header</p>
<dt><code>-z</code></p>
<dd> Set BITPIX to 0 to output a dataless header </p>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO jmink [at] cfa.harvard.edu </p>
<h2>Index</h2>
