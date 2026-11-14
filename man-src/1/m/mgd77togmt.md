---
title: "mgd77togmt(1)"
name: "mgd77togmt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mgd77togmt/"
description: "mgd77togmt – Convert an MGD-77 ASCII file to a binary gmt file"
---

<h2>NAME</h2>
<p> mgd77togmt &#8211; Convert an MGD-77 ASCII file to a binary gmt file</p>
<h2>SYNOPSIS</h2>
<p> <code>mgd77togmt</code> [ <code>-L</code><i>list</i> ] [ <i>mgd77file</i> ] <code>-F</code><i>legid</i> <code>-Y</code><i>start_year</i> [ <code>-A</code><i>information</i> ] [ <code>-I</code><i>time_increment</i> ] [<code>-T</code>[<i>&lt;offset&gt;</i>]] [<code>-W</code>[<i>&lt;cable_length&gt;</i>]] [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>mgd77togmt</code> reads an ASCII MGD-77 format file [or standard input] and creates a binary gmt file. The 16 header records specified in the MGD-77 documentation may or may not be present. If two-way travel times are available, <code>mgd77togmt</code> will convert those to corrected depths using the Carter tables. Both old and new (Y2K-compliant) MGD-77 files are supported.</p>
<dl>
<dt><code>-L</code></p>
<dd> Name of file with several records of the format <i>mgd77file legid start_year</i>. For multiple files, use this option rather than the <code>-F</code> <code>-Y</code> combination.</p>
<dt><code>-Y</code></p>
<dd> The year of the first data point in the file. If not provided and -L option not used, it tries to get it from a header file. The header file must be in the same directory of the main file and must have a name equal to the main but with a .h77 extension.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments.</p>
<dl>
<dt><code>-A</code></p>
<dd> Set an optional 10 character information string to be stored in the header [Default is blank].</p>
<dt><code>-F</code></p>
<dd> Leg id that will be used in file name (<i>legid</i>.gmt). If not given, it will be constructed from the mgd77file name plus the .gmt extension.</p>
<dt><code>-I</code></p>
<dd> Used for files where time is missing. The increment is used to calculate fake times.</p>
<dt><code>-T</code></p>
<dd> Extracts Total field instead of anomaly. Since F does not hold in a 2 byte signed variable we subtract a constant [default = 40000] but you can provide another value in <i>&lt;offset&gt;</i>.</p>
<dt><code>-W</code></p>
<dd> Take into account that the magnetometer is not at ship&#8217;s position. <i>&lt;cable&gt;</i> is magnetometer tow distance [default = 200 meters]. If <code>-W</code> only is given (e.g. no &lt;cable&gt;) and like with the <code>-Y</code> option, we try to get the tow distance from the header file. Failing, defaults to 200 meters. Note that this option will throw away the first points whose accumulated. distance since the start of magnetic acquisition is less than cable. length, and likewise for the end of the mag profile.</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>EXAMPLES</h2>
<p> To create a gmt file from the ASCII file c2104.mgd77, run </p>
<p> <code>mgd77togmt</code> c2104.mgd77 <code>-Y</code>1977 </p>
<p> To create new gmt files from all the mgd77 files listed in <i>list.d</i>: </p>
<p> <code>mgd77togmt</code> <code>-L</code>list.d <code>-V</code></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dat2gmt/">dat2gmt</a></i>(1), <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<p> MGD77 Task Group, 1977, The Marine Geophysical Data Exchange Format &#8211; MGD77, Key to Geophysical Records documentation No. 10, National Geophysical and Solar-Terrestrial Data Center, Boulder, CO. </p>
<p> Carter, D. J. T., <i>Echo Sounding Correction Tables: Formerly Matthews&#8217; Tables</i>,150 pp, Hydrographic Department, Ministry of Defense, Taunton, Somerset, England, 1980. </p>
<h2>Index</h2>
