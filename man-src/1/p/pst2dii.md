---
title: "pst2dii(1)"
name: "pst2dii"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pst2dii/"
description: "pst2dii – extract email messages from a MS Outlook .pst file in DII load format"
---

<h2 class="name">NAME</h2>
<p> pst2dii &#8211; extract email messages from a MS Outlook .pst file in DII load format </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pst2dii</code> [<code>-B&nbsp;<wbr></code><i>bates-prefix</i>] [<code>-O&nbsp;<wbr></code><i>dii-output-file</i>] [<code>-V</code>] [<code>-b&nbsp;<wbr></code><i>bates-number</i>] [<code>-c&nbsp;<wbr></code><i>bates-color</i>] [<code>-d&nbsp;<wbr></code><i>debug-file</i>] -f&nbsp;<wbr><i>ttf-font-file</i> [<code>-h</code>] [<code>-o&nbsp;<wbr></code><i>output-directory</i>] pstfilename</dl>
<h2>OPTIONS</h2>
<p> -B <i>bates-prefix</i></p>
<dl>
<dt>
<dd>
<dd>Sets the bates prefix string. The bates sequence number is appended to this string, and printed on each page.</dl>
<p> -O <i>dii-output-file</i></p>
<dl>
<dt>
<dd> Name of the output DII load file.</dl>
<p> -V</p>
<dl>
<dt>
<dd> Show program version. Subsequent options are then ignored.</dl>
<p> -b <i>bates-number</i></p>
<dl>
<dt>
<dd> Starting bates sequence number. The default is zero.</dl>
<p> -c <i>bates-color</i></p>
<dl>
<dt>
<dd> Font color for the bates stamp on each page, specified as 6 hex digits as rrggbb values. The default is ff0000 for bright red.</dl>
<p> -d <i>debug-file</i></p>
<dl>
<dt>
<dd> Specify name of debug log file. The log file is now an ascii file, instead of the binary file used in previous versions.</dl>
<p> -f <i>ttf-font-file</i></p>
<dl>
<dt>
<dd> Specify name of a true type font file. This should be a fixed pitch font.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Show summary of options. Subsequent options are then ignored.</dl>
<p> -o <i>output-directory</i></p>
<dl>
<dt>
<dd> Specifies the output directory. The directory must already exist.</dl>
<h2>DESCRIPTION</h2>
<p> <code>pst2dii</code> reads the email messages from a MS Outlook .pst file and produces a DII load file that may be used to import message summaries into a Summation DII system. The DII output file contains references to the image and attachment files in the output directory.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008 by 510 Software Group &lt;carl [at] five-ten-sg.com&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> You should have received a copy of the GNU General Public License along with this program; see the file COPYING. If not, please write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>VERSION</h2>
<p> 0.6.59 </p>
<h2>Index</h2>
