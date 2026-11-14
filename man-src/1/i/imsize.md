---
title: "imsize(1)"
name: "imsize"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imsize/"
description: "imsize – Print size of image in WCS and pixels"
---

<h2>Name</h2>
<p> imsize &#8211; Print size of image in WCS and pixels</p>
<h2>Synopsis</h2>
<p> imsize [-vcd] [-p scale] [-b ra dec] [-j ra dec] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> <i>imsize</i> is a utility for printing the region covered by an image using the world coordinate system parameters in IRAF and FITS image headers. It converts IRAF .imh image headers to a FITS format before extracting the information. For IRAF files, the image dimensions and the object name are set from the binary portion of the header.</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output B1950 (B1950) coordinates (optional center)</p>
<dt><code>-c</code></p>
<dd> Format output without pixel dimensions (optional size change)</p>
<dt><code>-d</code></p>
<dd> Format output as input to DSS getimage (optional size change)</p>
<dt><code>-e</code></p>
<dd> Add epoch of image to output line</p>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output J2000 (J2000) coordinates (optional center)</p>
<dt><code>-n &lt;number&gt;</code></p>
<dd> Number of decimal places in output (default 3)</p>
<dt><code>-p &lt;scale&gt;</code></p>
<dd> Initial plate scale in arcsec per pixel (default 0)</p>
<dt><code>-r</code></p>
<dd> Print range in RA and Dec</p>
<dt><code>-v</code></p>
<dd> Print more intermediate information for debugging</p>
<dt><code>-z</code></p>
<dd> Use AIPS classic projections instead of WCSLIB </p>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
