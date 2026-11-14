---
title: "imua2(1)"
name: "imua2"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imua2/"
description: "imua2 – Find USNO-A2.0 stars in FITS or IRAF image files"
---

<h2>Name</h2>
<p> imua2 &#8211; Find USNO-A2.0 stars in FITS or IRAF image files</p>
<h2>Synopsis</h2>
<p> imua2 [options] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> Search USNO-A2.0 Catalog within the area described by the world coordinate system in an image header. This is a link to imcat rather than a separate executable.</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output in B1950, optional new image center in B1950 (FK4) RA and Dec</p>
<dt><code>-h</code></p>
<dd> Print heading, else do not</p>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output in J2000, optional new image center in J2000 (FK5) RA and Dec</p>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></p>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</p>
<dt><code>-n &lt;num&gt;</code></p>
<dd> Number of brightest stars to print</p>
<dt><code>-p &lt;scale&gt;</code></p>
<dd> Initial plate scale in arcsec per pixel (default 0)</p>
<dt><code>-s</code></p>
<dd> Sort by RA instead of flux</p>
<dt><code>-t</code></p>
<dd> Tab table to standard output as well as file</p>
<dt><code>-u</code></p>
<dd> USNO catalog single plate number to accept</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write tab table output file imagename.cat <code>-z</code> Use AIPS classic projections instead of WCSLIB; use CD matrix or CDELT instead of polynomial solution.</dl>
<h2>See Also</h2>
<p> imgsc(),imuac(),imusac(),scat()</p>
<h2>Author</h2>
<p> Doug Mink, SAO (dmink [at] cfa.harvard.edu)</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output B1950 (FK4) coordinates (optional center)</p>
<dt><code>-u &lt;plate&gt;</code></p>
<dd> Accept only stars from this plate (default all)</p>
<dt><code>-h</code></p>
<dd> Print heading, else do not</p>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></p>
<dd> Output J2000 (FK5) coordinates (optional center)</p>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></p>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</p>
<dt><code>-n &lt;num&gt;</code></p>
<dd> Number of brightest stars to print</p>
<dt><code>-p &lt;scale&gt;</code></p>
<dd> Plate scale in arcsec per pixel (default 0)</p>
<dt><code>-s</code></p>
<dd> Sort by RA instead of flux</p>
<dt><code>-t</code></p>
<dd> Tab table to standard output as well as file</p>
<dt><code>-u &lt;plate&gt;</code></p>
<dd> Accept only stars from thsi plate (default all)</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write tab table output file imagename.uac</dl>
<h2>See Also</h2>
<p> imcat(),imgsc(),imusa2(),scat()</p>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/imcat/imua2.html">http://tdc-www.harvard.edu/software/wcstools/imcat/imua2.html</a></p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
