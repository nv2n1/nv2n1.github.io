---
title: "ot2kpx(1)"
name: "ot2kpx"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ot2kpx/"
description: "ot2kpx – extract kerning information from OpenType fonts"
---

<h2 class="name">NAME</h2>
<p> ot2kpx &#8211; extract kerning information from OpenType fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>ot2kpx</code> [ <i>-afm</i> | <i>-kpx</i> | <i>-lua</i> ] <code>&lt;fontfile&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ot2kpx</code> extract the kerning data from OpenType fonts and prints it to <tt>&quot;stdout&quot;</tt>, either in Adobe&#8217;s <font SIZE="-1">KPX</font> format (for adding to an <i>afm</i> file) or as a Luatex custom feature, for use with the <tt>&quot;\directlua&quot;</tt> command.</p>
<h2>OPTIONS AND ARGUMENTS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a short help text and exit.</p>
<dt><code>-version</code></p>
<dd> Print <code>ot2kpx</code>&#8216;s version and exit.</p>
<dt><code>-afm</code>, <code>-kpx</code></p>
<dd> Output the kerning data in Adobe&#8217;s <font SIZE="-1">KPX</font> format, as used in <i>afm</i> files. This is the default output format.</p>
<dt><code>-lua</code></p>
<dd> Output the kerning data as a Luatex custom font feature, to be included in a <tt>&quot;\directlua&quot;</tt> command.</p>
<dt><code>&lt;fontfile&gt;</code></p>
<dd> The OpenType font (both <i>otf</i> and <i>ttf</i> format are supported).</dl>
<h2>RESTRICTIONS</h2>
<dl>
<dt><code>&#8211;</code></p>
<dd> <code>ot2kpx</code> doesn&#8217;t implement all of the OpenType specification. Things that are missing include: support for font files containing multiple fonts, LookupTables with LookupTypes other than 2, &#8220;kern&#8221; tables with format other than 0 and ValueRecords with other types of data than just XAdvance data. </p>
<p> Most of these limitations won&#8217;t matter, since the missing features are rare (the only fonts I know of that use them are the non-western fonts that come with Adobe Reader). Furthermore, many of these features define (according to the OpenType specification) <i>&#8220;subtle, device-dependent adjustments at specific font sizes or device resolutions&#8221;</i>; since there&#8217;s no way to express such adjustments in <i>afm</i> format, ignoring them seems to be the only option anyway.</p>
<dt><code>&#8211;</code></p>
<dd> <code>ot2kpx</code> collects kerning data first from the &#8220;kern&#8221; table, then from all LookupTables associated with the &#8220;kern&#8221; feature; if a kerning pair occurs multiple times, the first value seen is chosen. There are (or may be) several issues with this approach:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> The OpenType specification says that fonts in <i>otf</i> format shouldn&#8217;t use the &#8220;kern&#8221; table at all, just the lookups from the &#8220;<font SIZE="-1">GPOS&#8221;</font> table. Many such fonts do, however, contain a &#8220;kern&#8221; table, but no &#8220;<font SIZE="-1">GPOS&#8221;</font> table; so we use the &#8220;kern&#8221; table anyway.</p>
<dt>&#8211;</p>
<dd> Instead of reading all LookupTables, it might be better to let the user specify a script and language and process only the LookupTables for those values. However, at least in the fonts I checked, all script/language combinations eventually point to the <i>same</i> &#8220;kern&#8221; LookupTables, so this approach wouldn&#8217;t make any difference (apart from further complicating the code).</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> Marc Penninga &lt;marcpenninga [at] gmail.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2022 Marc Penninga.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. A copy of the <font SIZE="-1">GNU</font> General Public License is included with <code>ot2kpx</code>; see the file <i>GPLv2.txt</i>.</p>
<h2>DISCLAIMER</h2>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> See the <font SIZE="-1">GNU</font> General Public License for more details.</p>
<h2>VERSION</h2>
<p> This document describes <code>ot2kpx</code> version 20220124.</p>
<h2>RECENT CHANGES</h2>
<p> (See the source code for the rest of the story.)</p>
<dl>
<dt><i>2019-05-20</i></p>
<dd> Added the <i>-version</i> option.</p>
<dt><i>2019-04-15</i></p>
<dd> Added the <i>-lua</i> command-line option to get output in Luatex&#8217;s custom feature format. </p>
</dl>
<h2>Index</h2>
