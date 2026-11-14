---
title: "x_solve_dc_drift(1)"
name: "x_solve_dc_drift"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_solve_dc_drift/"
description: "x_solve_dc_drift – Find Best-fitting D.C.-shift and Drift Estimates"
---

<h2>NAME</h2>
<p> <code>x_solve_dc_drift</code> &#8211; Find Best-fitting D.C.-shift and Drift Estimates</p>
<h2>SYNOPSIS</h2>
<p> <code>x_solve_dc_drift</code> [ <code>-X</code><i>xbase</i> ] [ <code>-L</code><i>lbase</i> ] [ <code>-I</code><i>ignorefile</i> ] [ <code>-S</code> ] [ <code>-C</code><i>iteration</i> ] [ <code>-M</code><i>min_nx</i> ] [ <code>-R</code><i>west/east/south/north</i> ] [ <code>-U</code><i>uselegsfile</i> ] [ <code>-V</code> ] [ <code>-B</code><i>binfile</i> ] [ <code>-A</code><i>ASCIIfile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>x_solve_dc_drift</code> will read the database files and, by iterating, find the best-fitting regression line to the &lt;time,COE&gt; points for each leg that minimizes the overall standard deviation of the data set in a least squares sense. Finally, correction file(s) are created.</p>
<dl>
<dt><code>-X</code></p>
<dd> Indicate an alternate database to read. [Default is <i>xx_base.b</i>].</p>
<dt><code>-L</code></p>
<dd> Indicate an alternate legbase to read. [Default is <i>xx_legs.b</i>].</p>
<dt><code>-I</code></p>
<dd> Ignore information for certain legs (that might be bad, etc).</p>
<dt><code>-S</code></p>
<dd> Reset the old d.c.-shift and drift estimates to zero before iterating.</p>
<dt><code>-C</code></p>
<dd> Specify how many iterations to do. Default is interactive session.</p>
<dt><code>-M</code></p>
<dd> Solve for drift only if the leg has more than <i>min_nx</i> cross-overs.</p>
<dt><code>-R</code></p>
<dd> Only take COEs inside this region into account. [Default is world].</p>
<dt><code>-U</code></p>
<dd> Solve for corrections involving COEs from legs in the <i>uselegsfile</i> only.</p>
<dt><code>-B</code></p>
<dd> Create a binary correction file (which can be read by <code>x_list</code> and <code>gmtlist</code>).</p>
<dt><code>-A</code></p>
<dd> Create an ASCII correction table. At least one of <code>-A</code> and <code>-B</code> must be specified.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>BEWARE</h2>
<p> The reason for the <code>-M</code> option is that if the COEs are few, then a stable estimate of the slope may not be obtained (e.g. when most of the COEs occur midway between ports). However, in most cases the bulk of the COEs do occur near the ports so that a drift estimate can be computed. Conventional wisdom recommends plotting the time-series and the computed regression line to see if it makes sense.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
