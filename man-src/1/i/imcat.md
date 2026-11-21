---
title: "imcat(1)"
name: "imcat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imcat/"
description: "imcat – List catalog stars in FITS and IRAF image files"
---

<h2>Name</h2>
<p> imcat &#8211; List catalog stars in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> imcat [options] FITS or IRAF file(s)</p>
<h2>Description</h2>
<p> Search given catalog withing area described by the world coordinate system in an image header. May be called as imuac to search the USNO A 1.0 catalog, imusac to search the USNO SA 1.0 catalog, or imgsc to search the HST Guide Star Catalog.</p>
<h2>Options</h2>
<dl>
<dt><code>-b [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output in B1950, optional new image center in B1950 (FK4) RA and Dec to replace that in image header</dd>
<dt><code>-c &lt;name&gt;</code></dt>
<dd> Reference catalog (gsc(=HST GSC), ua2(=USNO-A2.0), TMC(=2MASS Point Source Catalog), gsc2(=GSC II), ub1(=USNO-B1.0), local file, etc.)</dd>
<dt><code>-d</code></dt>
<dd> Output RA,Dec positions in fractional degrees</dd>
<dt><code>-e</code></dt>
<dd> Output in ecliptic longitude and latitude</dd>
<dt><code>-g</code></dt>
<dd> Output in galactic longitude and latitude</dd>
<dt><code>-h</code></dt>
<dd> Print heading, else do not</dd>
<dt><code>-i</code></dt>
<dd> Print name instead of number in region file</dd>
<dt><code>-j [&lt;RA&gt; &lt;Dec&gt;]</code></dt>
<dd> Output in J2000, optional new image center in J2000 (FK5) RA and Dec to replace that in image header</dd>
<dt><code>-k &lt;keyword&gt;</code></dt>
<dd> Add this keyword to output from tab table search</dd>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></dt>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</dd>
<dt><code>-n &lt;num&gt;</code></dt>
<dd> Number of brightest stars to print</dd>
<dt><code>-o &lt;type&gt;</code></dt>
<dd> Set HST Guide Star object class to print (0=stars, 3=nonstars, -1=all, -2=band)</dd>
<dt><code>-p &lt;scale&gt;</code></dt>
<dd> Initial plate scale in arcsec per pixel (default from file)</dd>
<dt><code>-q &lt;c|d|o|s|x|v|+&gt;</code></dt>
<dd> Write SAOimage region file with this shape, o=circle, s=square, d=diamond, +=cross, and x=X, with the radius scaled with magnitude unless specified with a -r command line entry. v will cause stellar Guide Stars to plot with a + and nonstellar Guide Stars to plot with an x. If character is is preceded by p, the size specified by the -r command is assumed to be in pixels, not arcseconds. A p alone specifies a circle in pixels.</dd>
<dt><code>-r &lt;radius&gt;</code></dt>
<dd> Write SAOimage region file with shapes (default CIRCLE) of this radius in arcseconds. SAOimage can then read this file, with will have positions and radii in pixels and plot it over an image. If the radius is specified as zero, the output radii will scale between 5 and dim/100 over the range of magnitudes of sources found in the image area. If the -q option is specified with a &#8216;p&#8217; in it, this number is assumed to be in pixels instead of arcseconds.</dd>
<dt><code>-s d|m|n|p|r|x|y</code></dt>
<dd> Sort by (d)eclination, (m)agnitude, (n)o sort, (p)distance from center, (r)ight ascension, image (x) or (y).</dd>
<dt><code>-t</code></dt>
<dd> Tab table to standard output as well as file</dd>
<dt><code>-u num</code></dt>
<dd> USNO catalog single plate number to accept</dd>
<dt><code>-v</code></dt>
<dd> Verbose listing of processing intermediate results</dd>
<dt><code>-w</code></dt>
<dd> Write tab table output file imagename.cat</dd>
<dt><code>-x x y</code></dt>
<dd> X and Y coordinates of reference pixel (default is CRPIXn or center of image)</dd>
<dt><code>-y epoch</code></dt>
<dd> Epoch of image for proper motions</dd>
<dt><code>-z</code></dt>
<dd> Use AIPS classic projections instead of WCSLIB; use CD matrix or CDELT instead of polynomial solution.</dd></dl>
<h2>See Also</h2>
<p> scat() </p>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/imcat/">http://tdc-www.harvard.edu/software/wcstools/imcat/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
