---
title: "afm2afm(1)"
name: "afm2afm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afm2afm/"
description: "afm2afm – reencode an afm file"
---

<h2 class="name">NAME</h2>
<p> afm2afm &#8211; reencode an afm file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>afm2afm</code></p>
<dd> [<code>-help</code>] [<code>-version</code>] [<code>-encoding</code>=<i>&lt;encodingfile&gt;</i>] [<code>-kpx</code>=<i>&lt;kpxfile&gt;</i>] [<code>-output</code>=<i>&lt;outputfile&gt;</i>] <code>&lt;afmfile&gt;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>afm2afm</code> re-encodes an <i>afm</i> file. </p>
<p> Metrics (including kerning data) for characters not present in the chosen encoding are excluded from the output, which resuls in (potentially much) smaller files. </p>
<p> Additional kerning pairs can be added to the output file. If you don&#8217;t specify an encoding file, the <i>afm</i> file isn&#8217;t re-encoded; however, all unused (unencoded) data is still pruned. </p>
<p> The program also generates an entry for a <i>dvips</i>-style map file, but only if the <i>afm</i> file has been re-encoded and the output was written to file (i.e., if both the <i>-encoding</i> and <i>-output</i> options were specified).</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a short description of the syntax</p>
<dt><code>-version</code></p>
<dd> Print version number and exit</p>
<dt><code>-encoding</code>=<i>&lt;encodingfile&gt;</i></p>
<dd> Re-encode to the enconding in <i>&lt;encodingfile&gt;</i></p>
<dt><code>-kpx</code>=<i>&lt;kpxfile&gt;</i></p>
<dd> Read additional kerning pairs from <i>&lt;kpxfile&gt;</i> and add these to the output. This option cannot be used to override values from the input <i>afm</i> file, since <code>afm2afm</code> will write both old and new values to the output! </p>
<p> The <i>&lt;kpxfile&gt;</i> should contain kerning data in standard <i>afm</i> format, i.e. for each kerning pair there should be a line </p>
<pre>
    KPX &lt;left_glyph&gt; &lt;right_glyph&gt; &lt;amount&gt;
</pre>
<p> All other lines in the <i>&lt;kpxfile&gt;</i> are ignored.</p>
<dt><code>-output</code>=<i>&lt;outputfile&gt;</i></p>
<dd> Write the result to <i>&lt;outputfile&gt;</i> instead of <tt>&quot;stdout&quot;</tt>.</p>
<dt><code>&lt;afmfile&gt;</code></p>
<dd> The <i>afm</i> file to be re-encoded.</dl>
<p> You may use either one or two dashes before options, and option names may be shortened to a unique prefix.</p>
<h2>AUTHOR</h2>
<p> Marc Penninga &lt;marcpenninga [at] gmail.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2022 Marc Penninga.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. A copy of the <font SIZE="-1">GNU</font> General Public License is included with <code>afm2afm</code>; see the file <i>GPLv2.txt</i>.</p>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> General Public License for more details.</p>
<h2>VERSION</h2>
<p> This document describes <code>afm2afm</code> version 20220124.</p>
<h2>RECENT CHANGES</h2>
<p> (See the source code for the rest of the story.)</p>
<dl>
<dt><i>2019-05-20</i></p>
<dd> Added the <i>-version</i> option. </p>
</dl>
<h2>Index</h2>
