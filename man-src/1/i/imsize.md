---

title: "imsize(1)"
name: "imsize"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imsize/"
description: "imsize – Print size of image in WCS and pixels"
---

<p> imsize &#8211; Print size of image in WCS and pixels</p>
<h2>Synopsis</h2>
<p> imsize [-vcd] [-p scale] [-b ra dec] [-j ra dec] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> <i>imsize</i> is a utility for printing the region covered by an image using the world coordinate system parameters in IRAF and FITS image headers. It converts IRAF .imh image headers to a FITS format before extracting the information. For IRAF files, the image dimensions and the object name are set from the binary portion of the header.</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output B1950 (B1950) coordinates (optional center)</dd>
<dt><code>-c</code></dt>
<dd> Format output without pixel dimensions (optional size change)</dd>
<dt><code>-d</code></dt>
<dd> Format output as input to DSS getimage (optional size change)</dd>
<dt><code>-e</code></dt>
<dd> Add epoch of image to output line</dd>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output J2000 (J2000) coordinates (optional center)</dd>
<dt><code>-n &lt;number&gt;</code></dt>
<dd> Number of decimal places in output (default 3)</dd>
<dt><code>-p &lt;scale&gt;</code></dt>
<dd> Initial plate scale in arcsec per pixel (default 0)</dd>
<dt><code>-r</code></dt>
<dd> Print range in RA and Dec</dd>
<dt><code>-v</code></dt>
<dd> Print more intermediate information for debugging</dd>
<dt><code>-z</code></dt>
<dd> Use AIPS classic projections instead of WCSLIB </dd>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
