---
title: "imstar(1)"
name: "imstar"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imstar/"
description: "imstar – Find stars in FITS and IRAF image files"
---

<h2>Name</h2>
<p> imstar &#8211; Find stars in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> imstar [options] [FITS or IRAF filename] or [@file of image file names]</p>
<h2>Description</h2>
<h2>Options</h2>
<dl>
<dt><code>&lt;hh:mm:ss&gt; &lt;dd:mm:ss&gt; [J2000, B1950]</code></p>
<dd> Coordinates for center (or reference pixel if -x is used).</p>
<dt><code>-a &lt;angle&gt;</code></p>
<dd> Image rotation angle in degrees (default 0). If multiple of 90, rotate image before search and set WCS angle to zero; if not, put in WCS.</p>
<dt><code>-b</code></p>
<dd> Output B1950 (FK4) coordinates (default=image equinox)</p>
<dt><code>-d &lt;catalog name&gt;</code></p>
<dd> Read this DAOFIND style catalog of X, Y, and magnitude instead of searching for stars in the image. The format is simply white-space-separated numbers on a line, with # at the beginning of comment lines.</p>
<dt><code>-e &lt;num&gt;</code></p>
<dd> Number of pixels to ignore around image edge</p>
<dt><code>-f</code></p>
<dd> Write a simple ASCII catalog file instead of tab table or DAOFIND format (number RA DEC mag &#8230; per line, with two lines of header info)</p>
<dt><code>-h</code></p>
<dd> Print heading, else do not</p>
<dt><code>-i &lt;num&gt;</code></p>
<dd> Minimum peak value for star in image (&lt;0=-sigma) Setting this to reject all but 10-15 stars is a good way to speed up the star-finding process. If num is less than zero, the minimum peak is -num image pixel standard deviations. Setting this number rejects faint stars early in the selection process for a significant saving in computing time.</p>
<dt><code>-j</code></p>
<dd> Output J2000 (FK5) coordinates (default=image equinox)</p>
<dt><code>-k</code></p>
<dd> Print each star as it is found for debugging</p>
<dt><code>-l</code></p>
<dd> Reflect the image left &lt;-&gt; right before rotating (-a) and searching for stars.</p>
<dt><code>-m &lt;magnitude&gt;</code></p>
<dd> Magnitude offset</p>
<dt><code>-n</code></p>
<dd> Number of brightest stars to print</p>
<dt><code>-o</code></p>
<dd> Output star list in DAOFIND format. The first three numbers on each line of the output file are X, Y, and magnitude, separated by one or more blanks or a tab. Lines beginning with # are ignored.</p>
<dt><code>-p &lt;num&gt;</code></p>
<dd> Plate scale in arcsec per pixel (default 0)</p>
<dt><code>-q &lt;c|d|o|s|x|v|+&gt;</code></p>
<dd> Output region file shape for SAOimage (default o) Characters mean: c&gt;ross, d&gt;iamond, s&gt;quare, o&gt;circle, x=X, v&gt;ary with GSC type, +&gt;cross.</p>
<dt><code>-r</code></p>
<dd> Maximum radius for star in pixels</p>
<dt><code>-s</code></p>
<dd> Sort by RA instead of flux</p>
<dt><code>-t</code></p>
<dd> Output in Starbase tab table format</p>
<dt><code>-v</code></p>
<dd> Verbose listing of processing intermediate results</p>
<dt><code>-w</code></p>
<dd> Write output to a file in addition to standard out. If DAO format (-o), create the name by adding .dao to the image file name. If Starbase format (-t), create the name by adding .tab to the image file name. If ASCII format (-f), create the name by adding .stars to the image file name.</p>
<dt><code>-x &lt;X&gt; &lt;Y&gt;</code></p>
<dd> X and Y coordinates of reference pixel (if not in header or image center)</p>
<dt><code>-z</code></p>
<dd> Use AIPS classic projection code (for &quot;-SIN&quot;, &quot;-TAN&quot;, &quot;-ARC&quot;, &quot;-NCP&quot;, &quot;-GLS&quot;, &quot;-MER&quot;, &quot;-AIT&quot; and &quot;-STG&quot; only) instead of WCSLIB proposed standard projection code. </p>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/imstar/">http://tdc-www.harvard.edu/software/wcstools/imstar/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
