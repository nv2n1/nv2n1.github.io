---
title: "d(1)"
name: "d"
section: "1"
letter: "d"
url: "/docs/linux/man/1-d/"
description: "d.zoom – Allows the user to change the current geographic region settings interactively, with a mouse."
---

<h2>NAME</h2>
<p> <i></i><code>d.zoom</code> &#8211; Allows the user to change the current geographic region settings interactively, with a mouse.</p>
<h2>KEYWORDS</h2>
<p> display</p>
<h2>SYNOPSIS</h2>
<p> <code>d.zoom</code><br />
 <code>d.zoom help</code><br />
 <code>d.zoom</code> [-<code>fphjr</code>] <code>rast</code>=<i>string</i>[,<i>string</i>,&#8230;] [<code>vector</code>=<i>string</i>[,<i>string</i>,&#8230;]] [<code>zoom</code>=<i>float</i>] [&#8211;<code>verbose</code>] [&#8211;<code>quiet</code>]</p>
<h3>Flags:</h3>
<dl>
<dt><code>-f</code></p>
<dd>
 Full menu (zoom + pan) &amp; Quit menu</p>
<dt><code>-p</code></p>
<dd>
 Pan mode</p>
<dt><code>-h</code></p>
<dd>
 Handheld mode</p>
<dt><code>-j</code></p>
<dd>
 Just redraw given maps using default colors</p>
<dt><code>-r</code></p>
<dd>
 Return to previous zoom</p>
<dt><code>&#8211;verbose</code></p>
<dd>
 Verbose module output</p>
<dt><code>&#8211;quiet</code></p>
<dd>
 Quiet module output</dl>
<h3>Parameters:</h3>
<dl>
<dt><code>rast</code>=<i>string[,string</i>,&#8230;]</p>
<dd>
 Name of raster map</p>
<dt><code>vector</code>=<i>string[,string</i>,&#8230;]</p>
<dd>
 Name of vector map</p>
<dt><code>zoom</code>=<i>float</i></p>
<dd>
 Magnification: &gt;1.0 zooms in, &lt;1.0 zooms out<br />
 Options: <i>0.001-1000.0</i><br />
 Default: <i>0.75</i></dl>
<h2>DESCRIPTION</h2>
<p> <i>d.zoom</i> allows the user to interactively adjust the settings of the current geographic region using a pointing device such as a mouse. Like <i>g.region</i>, <i>d.zoom</i> re-defines the settings of the geographic region. However, <i>d.zoom</i> allows the user to change the current region settings interactively, by either outlining the new region perimeter with a mouse, unzoom or pan the region. The graphics display is updated by the module. </p>
<p> After the user types the command <code>d.zoom</code> a mouse-button menu will appear directing the user. </p>
<p> Additionally the region settings can be modified by running <i>g.region</i>.</p>
<h2>NOTES</h2>
<p> Although it is not necessary that the user display a map in the active display frame before running <i>d.zoom</i>, it is helpful to do this for reference. Using parameter <code>-f</code> integrate a pan function, <code>-h </code> facilitates the use for handhelds.</p>
<h2>SEE ALSO</h2>
<p> <i>d.erase</i><br />
 <i>d.rast</i><br />
 <i>d.vect</i><br />
 <i>g.region</i></p>
<h2>AUTHOR</h2>
<p> Michael Shapiro, U.S. Army Construction Engineering Research Laboratory<br />
 Improvements by Huidae Cho and Markus Neteler </p>
<p> <i>Last changed: $Date: 2004-08-05 14:53:21 +0200 (Thu, 05 Aug 2004) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
