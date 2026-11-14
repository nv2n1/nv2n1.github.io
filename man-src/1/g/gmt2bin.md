---
title: "gmt2bin(1)"
name: "gmt2bin"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmt2bin/"
description: "gmt2bin – Create bin-index files from gmt files"
---

<h2>NAME</h2>
<p> gmt2bin &#8211; Create bin-index files from gmt files</p>
<h2>SYNOPSIS</h2>
<p> <code>gmt2bin</code> <i>listfile</i> [ <code>-P</code><i>path</i> ] [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gmt2bin</code> reads a file with a list of leg ids, opens each gmt file, and creates a bin-index file for each leg called &lt;legid&gt;.bix. These are used by <code>binlegs</code> to update the system files read by <code>gmtlegs</code>. Normally, only the data archivist will need to be concerned with these operations.</p>
<dl>
<dt><i>listfile</i></p>
<dd> This is a one column ASCII file with one leg id pr line.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-P</code></p>
<dd> Sets full path to directory with gmtfiles. [Default is current directory].</p>
<dt><code>-V</code></p>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-binlegs/">binlegs</a></i>(1), <i><a href="/docs/linux/man/1-dat2gmt/">dat2gmt</a></i>(1), <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
