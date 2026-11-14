---
title: "binlegs(1)"
name: "binlegs"
section: "1"
letter: "b"
url: "/docs/linux/man/1-binlegs/"
description: "binlegs – Maintain the GMT index files for mgg supplement"
---

<h2>NAME</h2>
<p> binlegs &#8211; Maintain the <code>GMT</code> index files for mgg supplement</p>
<h2>SYNOPSIS</h2>
<p> <code>binlegs </code><i>leglistfile</i> [ <code>-R</code> ] [ <code>-D</code> ] [ <code>-P</code><i>path</i> ] [ <code>-V</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>binlegs</code> will make changes to the <code>mgg</code> supplement data base files <i>gmt_legs.d</i> and <i>gmt_index.b</i> for the legs listed in the <i>leglistfile</i>. Normally, only the data archivist will need to be concerned with these operations.</p>
<dl>
<dt><i>leglistfile</i></p>
<dd> Contains the list of legs to be worked on.</dl>
<h2>OPTIONS</h2>
<p> No space between the option flag and the associated arguments </p>
<dl>
<dt><code>-R</code></p>
<dd> Replace the current information if a leg already is in the system. [Default is append].</p>
<dt><code>-D</code></p>
<dd> Delete information for these legs from the system index files.</p>
<dt>
<dt><code>-V</code></p>
<dd>
<dd> Selects verbose mode, which will send progress reports to stderr [Default runs &quot;silently&quot;].</dl>
<h2>EXAMPLES</h2>
<p> To add new cruises to the system: </p>
<p> <code>binlegs</code> <i>newlegs.lis</i> <code>-V</code> <code>-P</code><i>/usr/lib/gmt</i> </p>
<p> To remove bad legs from the system: </p>
<p> <code>binlegs</code> <i>badlegs.lis</i> <code>-D</code> <code>-V</code> <code>-P</code><i>/usr/lib/gmt</i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1), <i><a href="/docs/linux/man/1-gmtlegs/">gmtlegs</a></i>(1), <i><a href="/docs/linux/man/1-gmt2bin/">gmt2bin</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
