---
title: "xy2sky(1)"
name: "xy2sky"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xy2sky/"
description: "xy2sky – Compute RA Dec from X Y using WCS in FITS and IRAF image files"
---

<h2>Name</h2>
<p> xy2sky &#8211; Compute RA Dec from X Y using WCS in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> xy2sky [-vbjg] [-n ndec] file.fts x1 y1 &#8230; xn yn<br />
 or<br />
 xy2sky [-bdjgv] [-n ndec] file.fts @listfile</p>
<h2>Description</h2>
<p> <i>xy2sky</i> (pronounced X-Y-to-sky) is a utility for getting the world coordinates of a set of image coordinates in a FITS or IRAF image. World coordinate system (WCS) information in the image header describes, in a standard way, the relationship between sky coordinates and image pixels. This information is used by the program to transform image coordinate (X,Y) pairs to right ascension and declination sky coordinate pairs. The current version of the program prints the coordinates at the same equinox as is given in the image header, but future versions will allow transformations to B1950/FK4, J2000/FK5, or galactic coordinates. Input and output files in the Starbase format will eventually be allowed.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd> Append input line after output position</p>
<dt><code>-b</code></p>
<dd> B1950 (FK4) output</p>
<dt><code>-d</code></p>
<dd> RA and Dec output in degrees</p>
<dt><code>-e</code></p>
<dd> Output in ecliptic longitude and latitude in degrees.</p>
<dt><code>-f &lt;number&gt;</code></p>
<dd> Set third dimension for 3-D projections such as CSC</p>
<dt><code>-g</code></p>
<dd> Galactic longitude and latitude output</p>
<dt><code>-i</code></p>
<dd> First column is star id; 2nd, 3rd are x,y position</p>
<dt><code>-j</code></p>
<dd> J2000 (FK5) output</p>
<dt><code>-m &lt;number&gt;</code></p>
<dd> Set mode for output of LINEAR WCS coordinates: 0: x y linear 1: x units y units 2: x y linear units units</p>
<dt><code>-n &lt;number&gt;</code></p>
<dd> Number of decimal places in output RA seconds</p>
<dt><code>-q &lt;year&gt;</code></p>
<dd> Output equinox if not 2000 (-j) or 1950 (-b)</p>
<dt><code>-t</code></p>
<dd> Output as tab-separated table</p>
<dt><code>-v</code></p>
<dd> More descriptive output <code>-z</code> Use AIPS classic projections instead of WCSLIB </p>
</dl>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-sky2xy/">sky2xy</a>(1)</p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
