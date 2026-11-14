---
title: "lsdvd(1)"
name: "lsdvd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsdvd/"
description: "lsdvd – read the content info of a DVD"
---

<h2 class="name">NAME</h2>
<p> lsdvd &#8211; read the content info of a DVD </p>
<h2>SYNOPSIS</h2>
<p> <code>lsdvd</code> [ <code>options</code> ] [-t track_number] [dvd path] </p>
<h2>DESCRIPTION</h2>
<p> An application for reading the contents of a DVD and printing the contents to your terminal and dump for further processing in external applications.</p>
<h2>OPTIONS FOR EXTRA INFORMATION</h2>
<dl>
<dt><code>-a </code></p>
<dd> Dump information about audio streams.</p>
<dt><code>-d </code></p>
<dd> Dump information about cells.</p>
<dt><code>-n </code></p>
<dd> Dump information about angles (video layers).</p>
<dt><code>-c </code></p>
<dd> Dump chapter information.</p>
<dt><code>-s </code></p>
<dd> Dump subpicture information (e.g. subtitles).</p>
<dt><code>-P </code></p>
<dd> Dump palette information.</p>
<dt><code>-v </code></p>
<dd> Dump video information.</p>
<dt><code>-x </code></p>
<dd> Dump all information. </p>
</dl>
<h2>FORMATTING OPTIONS</h2>
<dl>
<dt><code>-Oh </code></p>
<dd> Dump output human readable (default setting). </p>
<dt><code>-Op </code></p>
<dd> Dump output as a Perl hash. (Using -p is deprecated). </p>
<dt><code>-Oy </code></p>
<dd> Dump output as Python. </p>
<dt><code>-Or </code></p>
<dd> Dump output in Ruby format. </p>
<dt><code>-Ox </code></p>
<dd> Dump output in XML. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-h </code></p>
<dd> Display help. </p>
<dt><code>-q </code></p>
<dd> Quiet output &#8211; do not summarize output. </p>
<dt><code>-V </code></p>
<dd> Display version information. </p>
</dl>
<h2>LICENSE</h2>
<p> lsdvd is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.</p>
<h2>AUTHORS</h2>
<p> <code>lsdvd</code> was written by Chris Philips. &lt;acid_kewpie [at] users.sourceforge.net&gt; </p>
<p> This manual page was written by Moritz Muehlenhoff &lt;jmm [at] inutil.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
