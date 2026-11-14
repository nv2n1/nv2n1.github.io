---
title: "imwcs(1)"
name: "imwcs"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imwcs/"
description: "imwcs – Set WCS in FITS and IRAF image files"
---

<h2>Name</h2>
<p> imwcs &#8211; Set WCS in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> imwcs [options] FITS or IRAF filename</p>
<h2>Description</h2>
<p> <i>imwcs</i> (pronounced im-W-C-S) is a utility for setting the world coordinate system (WCS) of a FITS or IRAF image. The WCS is the relationship between sky coordinates and image pixels and can be described in a standard way in the header of an image. The program was originally written at the University of Iowa, but has been adapted and amplified by Doug Mink at the Smithsonian Astrophysical Observatory. </p>
<p> <i>imwcs</i> currently works only on images where the rotation about the center is known to within a few degrees It has been tested extensively only on images with near-zero rotation. </p>
<p> A plane-tangent projection (center right ascension and declination, plate scale, and rotation angle) is fit based on matches between stars in the image and stars in a reference catalog. The HST Guide Star Catalog, the USNO A 1.0, SA 1.0, or UJ Catalog, or a user-supplied, tab-delimited Starbase catalog may be used. </p>
<h2>Options</h2>
<dl>
<dt><code>-a &lt;angle&gt;</code></p>
<dd> Initial rotation angle in degrees (default 0)</p>
<dt><code>-b &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Initial center in B1950 (FK4) RA and Dec (default=RA,DEC from file)</p>
<dt><code>-c &lt;catalog name&gt;</code></p>
<dd> Reference catalog (gsc(=HST GSC), ua2(=USNO-A2.0), TMC(=2MASS Point Source Catalog), gsc2(=GSC II), ub1(=USNO-B1.0), local file, etc.)</p>
<dt><code>-d &lt;catalog name&gt;</code></p>
<dd> Use this DAOFIND output catalog of X, Y, and magnitude instead of searching for stars in the image. The format is simply white-space-separated X, Y, and magnitue on a line, with # at the beginning of comment lines.</p>
<dt><code>-e</code></p>
<dd> Erase image WCS keywords, getting initial WCS from command line</p>
<dt><code>-f</code></p>
<dd> Write FITS output no matter what input</p>
<dt><code>-g &lt;class&gt;</code></p>
<dd> Guide Star Catalog class (-1=all,0,3) (default -1)</p>
<dt><code>-h &lt;number&gt;</code></p>
<dd> Change the maximum number of reference stars to match from 25 to</p>
<dt><code>-i &lt;counts&gt;</code></p>
<dd> Minimum peak value for star in image. If negative, use -&lt;counts&gt; standard deviations as minimum.</p>
<dt><code>-j &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Initial center in J2000 (FK5) RA and Dec (default=RA,DEC from file)</p>
<dt><code>-k &lt;magnum&gt;</code></p>
<dd> Use this magnitude to sort brightest catalog stars.</p>
<dt><code>-l</code></p>
<dd> Reflect left&lt;-&gt;right before rotating and fitting</p>
<dt><code>-m [&lt;bright magnitude&gt;] &lt;faint magnitude&gt;</code></p>
<dd> Limiting catalog magnitude(s) (default none, bright -2 if only faint is given)</p>
<dt><code>-n &lt;number&gt;</code></p>
<dd> Number of parameters to fit (1-8, or digit string). The default is 2 (RA+Dec) if &lt;3 stars are matched, 3 (RA+Dec+scale) if &lt;5 stars are matched, or 4 (RA+Dec+scale+rot) if 5 or more stars are matched. Alternatively this may be a list of all of the parameters to fit, in the form nnnnnn.., where 1=RA, 2=Dec, 3=RA scale, 4=Dec scale, 5=rotation angle, 6=Y axis rotation (CD matrix), 7=RA reference pixel, and 8=Dec reference pixel.</p>
<dt><code>-o &lt;filename&gt;</code></p>
<dd> Write output to this file; may be the same as input file. This option automatically sets the <code>-w</code> option to write the file.</p>
<dt><code>-p &lt;scale&gt;</code></p>
<dd> Initial plate scale in arcsec per pixel (default 0)</p>
<dt><code>-q &lt;option list&gt;</code></p>
<dd> &lt;i&gt;terate, &lt;r&gt;ecenter, &lt;s&gt;igma clip, &lt;p&gt;olynomial, &lt;t&gt;olerance reduce (half for each iteration). A number following an option repeats the option that many times.</p>
<dt><code>-r &lt;angle&gt;</code></p>
<dd> Rotation angle in degrees before fitting (0, 90, 180, 270) (default 0)</p>
<dt><code>-s &lt;frac&gt;</code></p>
<dd> Use this fraction extra stars (default 1.0)</p>
<dt><code>-t &lt;num&gt;</code></p>
<dd> Offset tolerance in pixels (default 20)</p>
<dt><code>-u &lt;file&gt;</code></p>
<dd> File of X Y RA Dec assignments for initial WCS</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write WCS to a new file (default is read-only) <code>-x</code> X and Y coordinates of reference pixel (default is image center) <code>-y</code> multiply image dimensions by this for search (default is 1) <code>-z</code> Use AIPS classic projections instead of WCSLIB; use CD matrix or CDELT instead of polynomial solution. </p>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/imwcs/">http://tdc-www.harvard.edu/software/wcstools/imwcs/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
