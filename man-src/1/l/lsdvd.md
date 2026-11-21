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
<dt><code>-a </code></dt>
<dd> Dump information about audio streams.</dd>
<dt><code>-d </code></dt>
<dd> Dump information about cells.</dd>
<dt><code>-n </code></dt>
<dd> Dump information about angles (video layers).</dd>
<dt><code>-c </code></dt>
<dd> Dump chapter information.</dd>
<dt><code>-s </code></dt>
<dd> Dump subpicture information (e.g. subtitles).</dd>
<dt><code>-P </code></dt>
<dd> Dump palette information.</dd>
<dt><code>-v </code></dt>
<dd> Dump video information.</dd>
<dt><code>-x </code></dt>
<dd> Dump all information. </dd>
</dl>
<h2>FORMATTING OPTIONS</h2>
<dl>
<dt><code>-Oh </code></dt>
<dd> Dump output human readable (default setting). </dd>
<dt><code>-Op </code></dt>
<dd> Dump output as a Perl hash. (Using -p is deprecated). </dd>
<dt><code>-Oy </code></dt>
<dd> Dump output as Python. </dd>
<dt><code>-Or </code></dt>
<dd> Dump output in Ruby format. </dd>
<dt><code>-Ox </code></dt>
<dd> Dump output in XML. </dd>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-h </code></dt>
<dd> Display help. </dd>
<dt><code>-q </code></dt>
<dd> Quiet output &#8211; do not summarize output. </dd>
<dt><code>-V </code></dt>
<dd> Display version information. </dd>
</dl>
<h2>LICENSE</h2>
<p> lsdvd is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; version 2 of the License.</p>
<h2>AUTHORS</h2>
<p> <code>lsdvd</code> was written by Chris Philips. &lt;acid_kewpie [at] users.sourceforge.net&gt; </p>
<p> This manual page was written by Moritz Muehlenhoff &lt;jmm [at] inutil.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
