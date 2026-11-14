---
title: "sky2xy(1)"
name: "sky2xy"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sky2xy/"
description: "sky2xy – Compute X Y from RA Dec using WCS in FITS and IRAF image files"
---

<h2>Name</h2>
<p> sky2xy &#8211; Compute X Y from RA Dec using WCS in FITS and IRAF image files</p>
<h2>Synopsis</h2>
<p> sky2xy [-vbjg] file.fts ra1 dec1 &#8230; ran decn<br />
 or<br />
 sky2xy [-vbjg] file.fts @listfile</p>
<h2>Description</h2>
<p> <i>sky2xy</i> (pronounced sky-to-X-Y) is a utility for getting the image coordinates of a set of world coordinates in a FITS or IRAF image. World coordinate system (WCS) information in the image header describes, in a standard way, the relationship between sky coordinates and image pixels. This information is used by the program to transform image right ascension and declination sky coordinate pairs to image coordinate (X,Y) pairs. The program prints the coordinates at the same system as is given in the image header, but future versions will allow transformations to B1950/FK4, J2000/FK5, ecliptic or galactic coordinates. Input and output files in the Starbase format will eventually be allowed.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd> B1950 (FK4) input</p>
<dt><code>-e</code></p>
<dd> Ecliptic longitude and latitude input</p>
<dt><code>-g</code></p>
<dd> Galactic longitude and latitude input</p>
<dt><code>-j</code></p>
<dd> J2000 (FK5) input</p>
<dt><code>-g</code></p>
<dd> Galactic longitude and latitude input</p>
<dt><code>-v</code></p>
<dd> More descriptive output</p>
<dt><code>-z</code></p>
<dd> Use AIPS classic projections instead of WCSLIB </p>
</dl>
<h2>See Also</h2>
<p> xy2sky() </p>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
