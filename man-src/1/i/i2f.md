---
title: "i2f(1)"
name: "i2f"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i2f/"
description: "i2f – Write FITS files from IRAF image files"
---

<h2>Name</h2>
<p> i2f &#8211; Write FITS files from IRAF image files</p>
<h2>Synopsis</h2>
<p> i2f [options] file.imh &#8230;</p>
<h2>Description</h2>
<p> <i>i2f</i> is a utility for converting IRAF images to FITS images. If you want to change the number of bits per pixel, use imrot. The BITPIX, NAXIS, NAXIS1, NAXIS2, OBJECT, and PIXFILE keywords are set from the binary portion of the header. IMHFILE and PIXFILE are set from the actual filenames for internal purposes.</p>
<h2>Options</h2>
<p> <code>-d directory</code> Move .imh file to this directory <code>-i</code> Delete unnecessary IRAF keywords <code>-o filename</code> Output name for one file <code>-s</code> Write output to standard output <code>-v</code> Verbose listing of processing intermediate results <code>-x</code> Delete IRAF image file after successfully writing FITS file</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
