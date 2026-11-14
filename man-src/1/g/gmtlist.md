---
title: "gmtlist(1)"
name: "gmtlist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtlist/"
description: "gmtlist – A data-extractor for <legid>.gmt files"
---

<h2>NAME</h2>
<p> gmtlist &#8211; A data-extractor for &lt;legid&gt;.gmt files</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtlist</code> <i>leg-ids</i> [ <code>-C</code><i>correctionfile</i> ] [ <code>-Da</code><i>startdate</i> ] [ <code>-Db</code><i>stopdate</i> ] [ <code>-F</code><i>flags</i> ] [ <code>-G</code> ] [ <code>-H</code>[<code>i</code>][<i>nrec</i>] ] [ <code>-R</code><i>west</i>/<i>east</i>/<i>south</i>/<i>north</i>[<code>r</code>] ] [ <code>-Sa</code><i>startdist</i> ] [ <code>-Sb</code><i>stopdist</i> ] [ <code>-V</code> ] [ <code>-W</code><i>weight</i> ] [ <code>-bo</code>[<code>s</code>|<code>S</code>|<code>d</code>|<code>D</code>[<i>ncol</i>]|<code>c</code>[<i>var1</i><code>/</code><i>&#8230;</i>]] ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmtlist</code> reads &lt;legid&gt;.gmt files and produces an ASCII [or binary] table. The &lt;legid&gt;.gmt files contain time(<code>s</code>), latitude(<code>y</code>), longitude(<code>x</code>), gravity(<code>g/G</code>), magnetics(<code>m/M</code>), and bathymetry(<code>t/T</code>), and the user may extract any combination of these 6 parameters + distance(<code>d</code>), heading (<code>h</code>), velocity (<code>v</code>), and weight (<code>w</code>, see <code>-W</code>). A sub-section can be specified by passing time- or distance-intervals along track or by selecting a region.</p>
<dl>
<dt><i>leg-ids</i></p>
<dd> Can be one or more cruisenames. To give a list of names, use `cat list_of_legs`.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments</p>
<dl>
<dt><code>-C</code></p>
<dd> Apply crossover Corrections to the data. If no correction file is given, gmtlist reads the default correction file. (See <code>XSYSTEM</code> for how to set up your own correction file).</p>
<dt><code>-Da</code></p>
<dd> Do not list data collected before <i>startdate</i> (mm/dd/yyyy/hh:mm) [Default is first day].</p>
<dt><code>-Db</code></p>
<dd> Do not list data collected after <i>stopdate</i> (mm/dd/yyyy/hh:mm). [Default is last day].</p>
<dt><code>-F</code></p>
<dd> Can be any combination of <code>syxgmtdhv</code> to indicate the desired output data. The data will appear in the order indicated by flags. If <code>G</code>, <code>M</code>, or <code>T</code> is substituted for <code>g</code>, <code>m</code>, <code>t</code>, only records that have that combination of data are written out. If <code>s</code> is followed by <code>c</code> (calendar), then yyyy/mm/dd/hh/mm/ss is written out, if <code>s</code> is followed by <code>j</code> (julian), then yyyy/jd/hh/mm/ss is written out. Default is seconds from start of year.</p>
<dt><code>-G</code></p>
<dd> Force Geographical longitudes (-180/+180) rather than geodetic (0-360) [Default].</p>
<dt><code>-H</code></p>
<dd> Issue a header record with names for each data field.</p>
<dt><code>-R</code></p>
<dd> <i>west, east, south,</i> and <i>north</i> specify the Region of interest, and you may specify them in decimal degrees or in [+-]dd:mm[:ss.xxx][W|E|S|N] format. Append <code>r</code> if lower left and upper right map coordinates are given instead of w/e/s/n. The two shorthands <code>-Rg</code> and <code>-Rd</code> stand for global domain (0/360 and -180/+180 in longitude respectively, with -90/+90 in latitude). Alternatively, specify the name of an existing grid file and the <code>-R</code> settings (and grid spacing, if applicable) are copied from the grid.</p>
<dt><code>-Sa</code></p>
<dd> Do not list data that are less than <i>startdist</i> km along track from port of departure. [Default is 0].</p>
<dt><code>-Sb</code></p>
<dd> Do not list data that are more than <i>stopdist</i> km along track from port of departure. [Default is length of track].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</p>
<dt><code>-W</code></p>
<dd> Set the weight for these data. Weight output option must be set in <code>-F</code>. This is useful if the data are to be processed with the weighted averaging techniques offered by <code>blockmean</code>, <code>blockmedian</code>, and <code>blockmode</code>.</p>
<dt><code>-b</code></p>
<dd> Selects binary output mode (in double precision) [Default is ASCII]. <code>-H</code> is ignored if <code>-b</code> is selected. Julian and calendar dates are not supported for binary time output (i.e., you get seconds from start of year).</dl>
<h2>EXAMPLES</h2>
<p> To get a (distance, heading, crossover-corrected gravity, bathymetry) listing from c2104.gmt, starting at June 3 1971 20:45 and ending at distance = 5000 km, use the following command: </p>
<p> <code>gmtlist</code> c2104 <code>-Da</code>6/3/1971/20:45 <code>-Sb</code>5000 <code>-F</code>dhgt <code>-C</code> &gt; myfile </p>
<p> To make input for <code>blockmean</code> and <code>surface</code> using all the cruises listed in the file gmt.list, but only the data that are inside the specified area, and make output binary: </p>
<p> <code>gmtlist</code> `cat gmt.list` <code>-F</code>xyg <code>-R</code>-40/-30/25/35 <code>-b</code> &gt; allgrav.xyg</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-x_system/">x_system</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
