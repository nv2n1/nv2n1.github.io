---
title: "wcsware(1)"
name: "wcsware"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wcsware/"
description: "wcsware – Extract WCS keywords for an image"
---

<h2>NAME</h2>
<p> wcsware &#8211; Extract WCS keywords for an image</p>
<h2>SYNOPSIS</h2>
<p> <code>wcsware</code> [<i>-a&lt;alt&gt;</i>] [<i>-f</i>] [<i>-h&lt;hdu&gt;</i>] [<i>-p</i>] [<i>-x</i>] [<i>&lt;fitsfile&gt;</i>]</p>
<h2>DESCRIPTION</h2>
<p> wcsware extracts the WCS keywords for an image from the specified FITS file, constructs wcsprm structs for each coordinate representation found and performs a variety of operations using them. </p>
<p> The FITS file may be specified according to the syntax understood by cfitsio, for example &quot;file.fits.gz+1&quot; refers to the first extension of a gzip&#8217;d FITS file. Use &quot;-&quot; or omit the file name for input from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>&lt;alt&gt;</p>
<dd> Specify an alternate coordinate representation to be used (ignored if there is only one).</p>
<dt><code>-f</code></p>
<dd> Apply wcsfix() to the header.</p>
<dt><code>-h</code>&lt;hdu&gt;</p>
<dd> Move to HDU number (1-relative) which is expected to contain an image array. (Useful for input from stdin.)</p>
<dt><code>-p</code></p>
<dd> Print the struct(s) using wcsprt() (default operation).</p>
<dt><code>-P</code></p>
<dd> Same as <code>-p</code> but don&#8217;t print a default struct.</p>
<dt><code>-x</code></p>
<dd> Convert pixel coordinates, obtained from stdin, to world coordinates using wcsp2s().</p>
<dt><code>-w</code></p>
<dd> Convert world coordinates, obtained from stdin, to pixel coordinates using wcss2p(). </p>
</dl>
<h2>Index</h2>
