---
title: "x_init(1)"
name: "x_init"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x_init/"
description: "x_init – Initialization of Cross-Over Data Bases."
---

<h2>NAME</h2>
<p> <code>x_init</code> &#8211; Initialization of Cross-Over Data Bases.</p>
<h2>SYNOPSIS</h2>
<p> <code>x_init</code> <code>-I</code></p>
<h2>DESCRIPTION</h2>
<p> The purpose of <code>x_init</code> is to create two key files that will be holding all the cross-over information for all the cruises tested. These files are called <i>xx_base.b</i> and <i>xx_legs.b</i>, and they will contain data for each cross-over and totals for each leg, respectively. <code>x_init</code> will create these two files in the current directory, and write out the fileheader with a 1 as the next record number in the case of xx_base.b. NB! Any previous files with the same names in the current directory will be erased, so use with caution.</p>
<dl>
<dt><code>-I</code></p>
<dd> Must be present form initialization to take effect.</dl>
<h2>BEWARE</h2>
<p> Both files are binary and have fixed record lengths. The formats of the files are as follows: </p>
<dl>
<dt><code>xx_base.b:</code></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Record length = 40 bytes.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Rec # 1:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fileheader</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Rec # 2:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pairheader</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Next n recs:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>crossover-structure</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Rec # n+3:<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pairheader etc.</p>
<p> The fileheader is a 40 byte character string where the last 10 bytes contains the record number of the last record in the file. The pairheader is a 40 byte character string which contains the names of the two legs in question and the number of COEs generated between them. The crossover-structure contains all the information for one COE, that is lat, lon, time along leg values of gravity, magnetics, and bathymetry at the cross-over point, the heading of track #1, and the heading of track #2. See program listing for more details on formats. The file is sequential in that new data are appended at the end of the file.</p>
<dt><code>xx_legs.b:</code></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Record length = 204 bytes.</p>
<p> Each record contains the complete information for each leg that has been checked. The leg-structure contains fields like year of cruise, number of internal/external COEs for gravity, magnetics, and bathymetry, their means and standard deviations, and the best fitting regression lines, i.e. the dc-shifts and drift-rates computed from the time/error data points. See program listing for complete description of record format.
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P. XOVER: A Cross-over Error Detector for Track Data, <i>Computers &amp; Geosciences, 15</i>, 333-346. </p>
<h2>Index</h2>
