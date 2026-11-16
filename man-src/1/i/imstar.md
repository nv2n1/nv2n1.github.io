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
<dt><code>&lt;hh:mm:ss&gt; &lt;dd:mm:ss&gt; [J2000, B1950]</code></dt>
<dd> Coordinates for center (or reference pixel if -x is used).</dd>
<dt><code>-a &lt;angle&gt;</code></dt>
<dd> Image rotation angle in degrees (default 0). If multiple of 90, rotate image before search and set WCS angle to zero; if not, put in WCS.</dd>
<dt><code>-b</code></dt>
<dd> Output B1950 (FK4) coordinates (default=image equinox)</dd>
<dt><code>-d &lt;catalog name&gt;</code></dt>
<dd> Read this DAOFIND style catalog of X, Y, and magnitude instead of searching for stars in the image. The format is simply white-space-separated numbers on a line, with # at the beginning of comment lines.</dd>
<dt><code>-e &lt;num&gt;</code></dt>
<dd> Number of pixels to ignore around image edge</dd>
<dt><code>-f</code></dt>
<dd> Write a simple ASCII catalog file instead of tab table or DAOFIND format (number RA DEC mag &#8230; per line, with two lines of header info)</dd>
<dt><code>-h</code></dt>
<dd> Print heading, else do not</dd>
<dt><code>-i &lt;num&gt;</code></dt>
<dd> Minimum peak value for star in image (&lt;0=-sigma) Setting this to reject all but 10-15 stars is a good way to speed up the star-finding process. If num is less than zero, the minimum peak is -num image pixel standard deviations. Setting this number rejects faint stars early in the selection process for a significant saving in computing time.</dd>
<dt><code>-j</code></dt>
<dd> Output J2000 (FK5) coordinates (default=image equinox)</dd>
<dt><code>-k</code></dt>
<dd> Print each star as it is found for debugging</dd>
<dt><code>-l</code></dt>
<dd> Reflect the image left &lt;-&gt; right before rotating (-a) and searching for stars.</dd>
<dt><code>-m &lt;magnitude&gt;</code></dt>
<dd> Magnitude offset</dd>
<dt><code>-n</code></dt>
<dd> Number of brightest stars to print</dd>
<dt><code>-o</code></dt>
<dd> Output star list in DAOFIND format. The first three numbers on each line of the output file are X, Y, and magnitude, separated by one or more blanks or a tab. Lines beginning with # are ignored.</dd>
<dt><code>-p &lt;num&gt;</code></dt>
<dd> Plate scale in arcsec per pixel (default 0)</dd>
<dt><code>-q &lt;c|d|o|s|x|v|+&gt;</code></dt>
<dd> Output region file shape for SAOimage (default o) Characters mean: c&gt;ross, d&gt;iamond, s&gt;quare, o&gt;circle, x=X, v&gt;ary with GSC type, +&gt;cross.</dd>
<dt><code>-r</code></dt>
<dd> Maximum radius for star in pixels</dd>
<dt><code>-s</code></dt>
<dd> Sort by RA instead of flux</dd>
<dt><code>-t</code></dt>
<dd> Output in Starbase tab table format</dd>
<dt><code>-v</code></dt>
<dd> Verbose listing of processing intermediate results</dd>
<dt><code>-w</code></dt>
<dd> Write output to a file in addition to standard out. If DAO format (-o), create the name by adding .dao to the image file name. If Starbase format (-t), create the name by adding .tab to the image file name. If ASCII format (-f), create the name by adding .stars to the image file name.</dd>
<dt><code>-x &lt;X&gt; &lt;Y&gt;</code></dt>
<dd> X and Y coordinates of reference pixel (if not in header or image center)</dd>
<dt><code>-z</code></dt>
<dd> Use AIPS classic projection code (for &quot;-SIN&quot;, &quot;-TAN&quot;, &quot;-ARC&quot;, &quot;-NCP&quot;, &quot;-GLS&quot;, &quot;-MER&quot;, &quot;-AIT&quot; and &quot;-STG&quot; only) instead of WCSLIB proposed standard projection code. </dd>
</dl>
<h2>Web Page</h2>
<p> <a rel="nofollow" href="http://tdc-www.harvard.edu/software/wcstools/imstar/">http://tdc-www.harvard.edu/software/wcstools/imstar/</a> </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
