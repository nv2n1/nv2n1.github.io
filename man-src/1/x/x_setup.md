---
title: "x_setup(1)"
name: "x_setup"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_setup/"
description: "x_setup – Determine Pairs of Legs that need Cross-Over Checking"
---

<h2>NAME</h2>
<p> <code>x_setup</code> &#8211; Determine Pairs of Legs that need Cross-Over Checking</p>
<h2>SYNOPSIS</h2>
<p> <code>x_setup</code> [ <code>-L</code><i>legfile</i> ] [ <code>-R</code><i>west/east/south/north</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>x_setup</code> scans the <i>gmtindex.b</i> file that contains information on which legs occupy each 1 by 1 degree bin and reports all the pairs of legs that may overlap. Each pair is only reported once, even if the two legs involved are found in other bins also.</p>
<dl>
<dt><code>-L</code></p>
<dd> Only report pairs where at least one of the legs are present in the <i>legfile</i>.</p>
<dt><code>-R</code></p>
<dd> The region of interest. [Default is world]</dl>
<h2>BEWARE</h2>
<p> The <code>-L</code> option is useful when one wants to check out a handful of new cruises. Obviously we only need to compute COEs for the pairs that involve one or two of the new cruises, since all the other combinations have already been done.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
