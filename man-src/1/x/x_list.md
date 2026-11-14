---
title: "x_list(1)"
name: "x_list"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_list/"
description: "x_list – Extract Cross-Over Information from the Data Base."
---

<h2>NAME</h2>
<p> <code>x_list</code> &#8211; Extract Cross-Over Information from the Data Base.</p>
<h2>SYNOPSIS</h2>
<p> <code>x_list</code> [ <i>leg1</i> ] [ <i>leg2</i> ] [ <code>&#8211;</code><i>dataflags</i> ] [ <code>-R</code><i>west/east/south/north</i> ] [ <code>-X</code><i>xbase</i> ] [ <code>-H</code> ] [ <code>-I</code> ] [ <code>-V</code> ] [ <code>-C</code><i>corrfile</i> ] [ <code>-Z</code><i>ignorefile</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>x_list</code> will allow the user to extract information from the xx_base.b and xx_legs.b files. Several options can be passed on the command line in order to specify which parameters to extract. They are:</p>
<dl>
<dt><i>leg1 leg2</i></p>
<dd> If two legs are specified, the cross-overs they have in common are returned. If one leg is specified, all the external cross-overs involving this leg are returned, OR only its internal cross-overs if -I is selected. If no legs are given, all the external (or internal with -I) cross-overs are returned. This program is useful if one wants to look at, say, gravity COEs versus time from port for a particular leg, etc.</p>
<dt><i>dataflags</i></p>
<dd> This is a string of any combination of the following:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>l</code> means list both legnames.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>t</code> means list time.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>x</code> means list longitude.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>y</code> means list latitude.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>g</code> means list gravity COEs.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>m</code> means list magnetics COEs.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>b</code> means list bathymetry COEs.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>G</code> means list average gravity at cross-over.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>M</code> means list average magnetic anomaly at cross-over.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>B</code> means list average bathymetry at cross-over.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>h</code> means list heading of ship at cross-over.</p>
<p> The components are written out in the order they appear in <i>dataflags</i>. The default output is <code>-txygmbGMBhl</code>. When internal COEs are desired, the time reported is the elapsed time since the ship first occupied the cross-over point. For external COEs the time means time from the start of the year in seconds.</p>
<dt><code>-R</code></p>
<dd> Only return cross-overs inside the specified region <i>west, east, south, </i>and <i>north</i>. [Default is world].</p>
<dt><code>-X</code></p>
<dd> Indicate alternate <i>xx_base.b</i> file.</p>
<dt><code>-H</code></p>
<dd> Issue one header record on output.</p>
<dt><code>-I</code></p>
<dd> Report on internal COEs [Default is external COEs].</p>
<dt><code>-C</code></p>
<dd> Apply cross-over correction to the data (i.e. reports the cross-over value after the best-fitting corrections have been applied to both legs). If no <i>corrfile</i> is given, the default correction file is assumed.</p>
<dt><code>-Z</code></p>
<dd> Ignore those legs that appear in the <i>ignorefile</i>.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
