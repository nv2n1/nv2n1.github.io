---
title: "x_over(1)"
name: "x_over"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_over/"
description: "x_over – Find and compute Cross-Over Errors"
---

<h2>NAME</h2>
<p> <code>x_over</code> &#8211; Find and compute Cross-Over Errors</p>
<h2>SYNOPSIS</h2>
<p> <code>x_over</code> <i>leg_1</i> [ <i>leg_2</i> ] [ <code>-A</code> ] [ <code>-C</code> ] [ <code>-L</code> ] [ <code>-V</code> ] [ <code>-W</code><i>timegap</i> ] [ <code>-G</code><i>fact</i> ] [ <code>-M</code><i>fact</i> ] [ <code>-T</code><i>fact</i> ] [ <code>-N</code><i>np_int</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>x_over</code> is used to inspect two cruises to see if they intersect, and if so report the time, position, discrepancies in gravity/magnetics/bathymetry, heading for each track segment, and the average values of the geophysical observables at the cross-over point. The names of the legs are passed on the command line. If they are identical or only one name is passed, then <code>x_over</code> looks for internal cross-overs. The optional parameters are:</p>
<dl>
<dt><code>-A</code></p>
<dd> Use an Akima spline to interpolate the geophysical field at the cross-over point.</p>
<dt><code>-C</code></p>
<dd> Use a Natural Cubic spline function instead.</p>
<dt><code>-L</code></p>
<dd> Use a linear interpolant [Default].</p>
<dt><code>-W</code></p>
<dd> Do not compute cross-overs if the 2 nearest points are more than <i>timegap</i> minutes apart.</p>
<dt><code>-G</code></p>
<dd> Scale gravity by <i>fact</i> [Default is 0.1 since gmt-files store gravity in g.u.]</p>
<dt><code>-M</code></p>
<dd> Scale magnetic anomaly by <i>fact</i> [1.0].</p>
<dt><code>-T</code></p>
<dd> Scale bathymetry by <i>fact</i> [1.0].</p>
<dt><code>-N</code></p>
<dd> Specify how many points to use in the interpolation [Default is 6].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;]. Report the number of cross-overs for this pair of legs.
</dl>
<h2>BEWARE</h2>
<p> The COEs found are printed out to standard output in ASCII format. The first record contains the leg names and their start year, whereas subsequent records have the data for each COE encountered. The fields written out are lat, lon, time along track #1, time along track #2, x_gravity, x_magnetics, x_bathymetry, average gravity, average magnetics, average bathymetry, heading along track #1, and heading along track #2. Sign convention: If lega and legb are passed on the command line, then the COE value is Value (lega) &#8211; Value (legb). It is recommended that the Akima spline is used instead of the natural cubic spline, since it is less sensitive to outliers that tend to introduce wild oscillations in the interpolation.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
