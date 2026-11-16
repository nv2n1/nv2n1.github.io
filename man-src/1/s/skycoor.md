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
<dt><code>-b</code></dt>
<dd> B1950 (FK4) output</dd>
<dt><code>-d</code></dt>
<dd> RA and Dec output in degrees</dd>
<dt><code>-e</code></dt>
<dd> Ecliptic longitude and latitude output</dd>
<dt><code>-g</code></dt>
<dd> Galactic longitude and latitude output</dd>
<dt><code>-i r|d|</code></dt>
<dd> Input units (r=radians, d=degrees, else hh:mm:sss dd:mm:sss)</dd>
<dt><code>-j</code></dt>
<dd> J2000 (FK5) output</dd>
<dt><code>-n &lt;num&gt;</code></dt>
<dd> Number of decimal places in output RA seconds</dd>
<dt><code>-o &lt;num&gt;</code></dt>
<dd> Offset coordinates by this many arcseconds</dd>
<dt><code>-p</code></dt>
<dd> RA and Dec proper motion in milliarcseconds/year</dd>
<dt><code>-q</code></dt>
<dd> Output system, including equinox</dd>
<dt><code>-r &lt;RA&gt; &lt;Dec&gt; &lt;RA&gt; &lt;Dec&gt;</code></dt>
<dd> Angular separation between two RA, Dec pairs</dd>
<dt><code>-s</code></dt>
<dd> Output ra= dec= epoch= radecsys= for sethead</dd>
<dt><code>-v</code></dt>
<dd> Print more intermediate information</dd>
<dt><code>-w</code></dt>
<dd> Convert RA, Dec equatorial coordinates to x,y,z</dd>
<dt><code>-x</code></dt>
<dd> Convert x,y,z equatorial coordinates to RA, Dec</dd>
<dt><code>-y &lt;epoch&gt;</code></dt>
<dd> Epoch of coordinates in years </dd>
</dl>
<h2>Author</h2>
<p> Jessica Mink, SAO (jmink [at] cfa.harvard.edu) </p>
<h2>Index</h2>
