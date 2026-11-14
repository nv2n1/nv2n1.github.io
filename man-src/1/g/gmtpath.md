---
title: "gmtpath(1)"
name: "gmtpath"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmtpath/"
description: "gmtpath – Get full pathname for gmt files"
---

<h2>NAME</h2>
<p> gmtpath &#8211; Get full pathname for gmt files</p>
<h2>SYNOPSIS</h2>
<p> <code>gmtpath</code> <i>leg-ids</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gmtpath</code> returns the full pathname to one or more gmt-files. The pathname returned for a given cruise may change with time due to reshuffling of disks/subdirectories.</p>
<dl>
<dt><i>leg-ids</i></p>
<dd> Can be one or more gmtleg-names, like c2610. Use `cat list_of_legs` to pass all the legnames in the file list_of_legs.</dl>
<h2>EXAMPLES</h2>
<p> To obtain pathnames for cruises c2603 and v2819, run </p>
<p> <code>gmtpath</code> c2603 v2819</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gmt/">GMT</a></i>(1)</p>
<h2>REFERENCES</h2>
<p> Wessel, P., and W. H. F. Smith, 2009, The Generic Mapping Tools (GMT) version 4.5.0 Technical Reference &amp; Cookbook, SOEST/NOAA.<br />
 Wessel, P., and W. H. F. Smith, 1998, New, Improved Version of Generic Mapping Tools Released, EOS Trans., AGU, 79 (47), p. 579.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, EOS Trans., AGU, 76 (33), p. 329.<br />
 Wessel, P., and W. H. F. Smith, 1995, New Version of the Generic Mapping Tools Released, <a rel="nofollow" href="http://www.agu.org/eos_elec/95154e.html,">http://www.agu.org/eos_elec/95154e.html,</a> Copyright 1995 by the American Geophysical Union.<br />
 Wessel, P., and W. H. F. Smith, 1991, Free Software Helps Map and Display Data, EOS Trans., AGU, 72 (41), p. 441. </p>
<h2>Index</h2>
