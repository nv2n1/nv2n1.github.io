---
title: "pbmtoibm23xx(1)"
name: "pbmtoibm23xx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbmtoibm23xx/"
description: "pbmtoibm23xx – convert a PBM image to IBM 23XX printer stream"
---

<h2 class="name">NAME</h2>
<p> pbmtoibm23xx &#8211; convert a PBM image to IBM 23XX printer stream</p>
<h2>SYNOPSIS</h2>
<p> <code>pbmtoibm23xxx</code> [<code>-xres=</code><i>dpi</i>] [<code>-yres=</code><i>dpi</i>] [<i>pbmfile</i> &#8230;] </p>
<p> Minimum unique abbreviation of option is acceptable. You may use double hyphens instead of single hyphen to denote options. You may use white space in place of the equals sign to separate an option name from its value. </p>
<h2>DESCRIPTION</h2>
<p> This program is part of <code><a href="/docs/linux/man/1-netpbm/">Netpbm</a></code>(1) </p>
<p> <code>pbmtoibm23xx</code> reads one or more PBM files as input and writes an IBM 23XX printer command stream to generate all the images in all the files to Standard Output. </p>
<p> If you don&#8217;t specify any file names, <code>pbmtoibm23xx</code> reads from Standard Input. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-xres=</code><i>dpi</i></p>
<dd> This option specifies the horizontal resolution in dots per inch. Valid values are 60, 120, and 240. </p>
<dt><code>-yres=</code><i>dpi</i></p>
<dd> This option specifies the vertical resolution in dots per inch. Valid values are 60, 120, and 240. </p>
<dt><code>-slow</code></p>
<dd> Use the slower printing mode where two modes with the same resolution are available. This usually produces better quality prints. This affects only modes with horizontal resolution 120, but might affect other modes in future versions of the program.<br />
&nbsp;<wbr>&nbsp;<wbr> </p>
</dl>
<h2>LIMITATIONS</h2>
<p> There are probably better ways to control the IBM 23XX printers. Let me know if you find any. </p>
<h2>HISTORY</h2>
<p> <code>pbmtoibm23xx</code> was new in Netpbm 10.25 (October 2004). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pbm/">pbm</a></code>(1) , Ghostscript (<code>gs</code>). </p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2004 Jorrit Fahlke &lt;jorrit [at] jorrit.de&gt;. Copying policy: GNU GPL version 2 </p>
<h2>Index</h2>
