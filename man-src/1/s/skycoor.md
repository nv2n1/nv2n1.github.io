---
title: "skycoor(1)"
name: "skycoor"
section: "1"
letter: "s"
url: "/docs/linux/man/1-skycoor/"
description: "skycoor – Convert coordinates"
---

<h2>Name</h2>
<p> skycoor &#8211; Convert coordinates</p>
<h2>Synopsis</h2>
<p> skycoor [-bdgjv] [-n ndec] ra1 dec1 sys1 &#8230; ran decn sysn<br />
 or<br />
 skycoor [-vbjg] [-n ndec] @listfile</p>
<h2>Description</h2>
<p> <i>skycoor</i> converts coordinates between the J2000, B1950, and galactic coordinate systems, rounding to a specified number of decimal places and printing in degrees or hh:mm:ss.sss dd:mm:ss.sss. Input coordinates may also be in either format, and the system (J2000, B1950, or galactic) may be in upper or lower case. No spaces are allowed within the individual coordinates</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></p>
<dd> B1950 (FK4) output</p>
<dt><code>-d</code></p>
<dd> RA and Dec output in degrees</p>
<dt><code>-e</code></p>
<dd> Ecliptic longitude and latitude output</p>
<dt><code>-g</code></p>
<dd> Galactic longitude and latitude output</p>
<dt><code>-i r|d|</code></p>
<dd> Input units (r=radians, d=degrees, else hh:mm:sss dd:mm:sss)</p>
<dt><code>-j</code></p>
<dd> J2000 (FK5) output</p>
<dt><code>-n &lt;num&gt;</code></p>
<dd> Number of decimal places in output RA seconds</p>
<dt><code>-o &lt;num&gt;</code></p>
<dd> Offset coordinates by this many arcseconds</p>
<dt><code>-p</code></p>
<dd> RA and Dec proper motion in milliarcseconds/year</p>
<dt><code>-q</code></p>
<dd> Output system, including equinox</p>
<dt><code>-r &lt;RA&gt; &lt;Dec&gt; &lt;RA&gt; &lt;Dec&gt;</code></p>
<dd> Angular separation between two RA, Dec pairs</p>
<dt><code>-s</code></p>
<dd> Output ra= dec= epoch= radecsys= for sethead</p>
<dt><code>-v</code></p>
<dd> Print more intermediate information</p>
<dt><code>-w</code></p>
<dd> Convert RA, Dec equatorial coordinates to x,y,z</p>
<dt><code>-x</code></p>
<dd> Convert x,y,z equatorial coordinates to RA, Dec</p>
<dt><code>-y &lt;epoch&gt;</code></p>
<dd> Epoch of coordinates in years </p>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
