---
title: "imgsc(1)"
name: "imgsc"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imgsc/"
description: "imgsc – Find HST GSC stars in FITS or IRAF image files"
---

<h2>Name</h2>
<p> imgsc &#8211; Find HST GSC stars in FITS or IRAF image files</p>
<h2>Synopsis</h2>
<p> imgsc [options] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> Search the HST Guide Star Catalog withing the area described by the world coordinate system in an image header. This is a link to imcat rather than a separate executable.</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output in B1950, optional new image center in B1950 (FK4) RA and Dec</dd>
<dt><code>-c &lt;name&gt;</code></dt>
<dd> Reference catalog (gsc, ujc, or tab table file</dd>
<dt><code>-g &lt;class&gt;</code></dt>
<dd> Guide Star Catalog class (-1=all,0,3 (default -1)</dd>
<dt><code>-h</code></dt>
<dd> Print heading, else do not</dd>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output in J2000, optional new image center in J2000 (FK5) RA and Dec</dd>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></dt>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</dd>
<dt><code>-n &lt;num&gt;</code></dt>
<dd> Number of brightest stars to print</dd>
<dt><code>-p &lt;scale&gt;</code></dt>
<dd> Initial plate scale in arcsec per pixel (default 0)</dd>
<dt><code>-s</code></dt>
<dd> Sort by RA instead of flux</dd>
<dt><code>-t</code></dt>
<dd> Tab table to standard output as well as file</dd>
<dt><code>-v</code></dt>
<dd> Verbose listing of processing intermediate results</dd>
<dt><code>-w</code></dt>
<dd> Write tab table output file imagename.cat <code>-z</code> Use AIPS classic projections instead of WCSLIB; use CD matrix or CDELT instead of polynomial solution.</dd></dl>
<h2>See Also</h2>
<p> imcat(),imuac(),imusac(),scat()</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
