---
title: "x_report(1)"
name: "x_report"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_report/"
description: "x_report – Report Cross-Over Error Statistics for Cruises"
---

<h2>NAME</h2>
<p> <code>x_report</code> &#8211; Report Cross-Over Error Statistics for Cruises</p>
<h2>SYNOPSIS</h2>
<p> <code>x_report</code> [ <i>leg</i> ] [ <code>-X</code><i>legbase</i> ] [ <code>-G</code> ] [ <code>-M</code> ] [ <code>-T</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>x_report</code> reads the x_system data base file and prints out statistics for each leg. The statistics are the number of, means, and standard deviations of COEs for both the internal and external cases. One or more data types (GMT) may be specified.</p>
<dl>
<dt><i>leg</i></p>
<dd> Report on <i>leg</i> only. [Default is all legs].</p>
<dt><code>-X</code></p>
<dd> Specify alternate leg data base [Default is <i>xx_legs.b</i>].</p>
<dt><code>-G</code></p>
<dd> Give information for Gravity cross-overs only. [Default is G, M, and T].</p>
<dt><code>-M</code></p>
<dd> Give information for Magnetics cross-overs only. [Default is G, M, and T].</p>
<dt><code>-T</code></p>
<dd> Give information for Topography cross-overs only. [Default is G, M, and T].</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
