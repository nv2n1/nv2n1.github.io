---
title: "delwcs(1)"
name: "delwcs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delwcs/"
description: "delwcs – Delete WCS in FITS and IRAF image files"
---

<h2>Name</h2>
<p> delwcs &#8211; Delete WCS in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> delwcs [-v] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> Delete WCS keywords &quot;CTYPE1&quot;, &quot;CRVAL1&quot;, &quot;CDELT1&quot;, &quot;CRPIX1&quot;, &quot;CROTA1&quot;, &quot;CTYPE2&quot;, &quot;CRVAL2&quot;, &quot;CDELT2&quot;, &quot;CRPIX2&quot;, &quot;CROTA2&quot;, and &quot;IMWCS&quot; from a fits header. If there are &quot;WRA&quot;, WDEC&quot;, and &quot;WEPOCH&quot; or &quot;WEQUINOX&quot; keywords present, their values replace those lf &quot;RA&quot;, &quot;DEC&quot;, and &quot;EPOCH&quot; or &quot;EQUINOX&quot;.</p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd> Write new output file with &quot;e&quot; before the file type extension. The default is to overwrite the input file.</p>
<dt><code>-v</code></p>
<dd> Print names of keywords as they are deleted </p>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
