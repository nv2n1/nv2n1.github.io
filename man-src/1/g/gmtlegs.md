---
title: "gmtlegs(1)"
name: "gmtlegs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtlegs/"
description: "gmtlegs – Find cruises in a given region"
---

<h2>NAME</h2>
<p> gmtlegs &#8211; Find cruises in a given region</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtlegs</code> <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] [ <code>-G</code> ] [ <code>-M</code> ] [ <code>-T</code> ] [ <code>-L</code> ] [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtlegs</code> will report the name of all the cruises that happened to be wholly or partially inside the specified region. As an option, only those cruises that collected a certain type of data can be reported.</p>
<dl>
<dt><code>-R</code></p>
<dd> <i>west, east, south,</i> and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments</p>
<dl>
<dt><code>-G</code></p>
<dd> Report cruises that collected Gravity data. [Default is any data].</p>
<dt><code>-M</code></p>
<dd> Report cruises that collected Magnetics. [Default is any data].</p>
<dt><code>-T</code></p>
<dd> Report cruises that collected Topography. [Default is any data].</p>
<dt><code>-L</code></p>
<dd> Long output, i.e. cruisenames and data types available. [Default is cruisenames only].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>EXAMPLES</h2>
<p> To find all cruises around Hawaii that collected gravity and topography: </p>
<p> <code>gmtlegs</code> <code>-R</code>-162/-152/18/25 <code>-G</code> <code>-T</code> &gt; hawaii_gt.legs </p>
<p> To find all cruises with magnetics: </p>
<p> <code>gmtlegs</code> <code>-R</code>0/360/-90/90 <code>-M</code> &gt; all_m.legs</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gmt2bin/">gmt2bin</a></i>(1), <i><a href="/docs/linux/man/1-binlegs/">binlegs</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
