---
title: "showfont(1)"
name: "showfont"
section: "1"
letter: "s"
url: "/docs/linux/man/1-showfont/"
description: "showfont – font dumper for X font server"
---

<h2 class="name">NAME</h2>
<p> showfont &#8211; font dumper for X font server </p>
<h2>SYNOPSIS</h2>
<p> <code>showfont</code> [ <i>-options</i> &#8230; ] <code>-fn</code> <i>pattern</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Showfont</i> displays data about a font that matches the given <i>pattern</i>. The information shown includes font information, font properties, character metrics, and character bitmaps. </p>
<p> The wildcard character &quot;*&quot; can be used to match any sequence of characters (including none) in the font name, and &quot;?&quot; can be used to match any single character. The &quot;*&quot; and &quot;?&quot; characters must be quoted to prevent them from being expanded by the shell. If no pattern is given, &quot;*&quot; is assumed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-server </code><i>servername</i></p>
<dd> The X font server to contact. <i>servername</i> must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7). If not specified, the server name in the <code>FONTSERVER</code> environment variable is used.</p>
<dt><code>-fn</code><i> name</i></p>
<dd> The font to display.</p>
<dt><code>-lsb</code></p>
<dd> The bit order of the font should be requested as LSBFirst (least significant bit first).</p>
<dt><code>-msb</code></p>
<dd> The bit order of the font should be requested as MSBFirst (most significant bit first).</p>
<dt><code>-LSB</code></p>
<dd> The byte order of the font should be requested as LSBFirst (least significant byte first).</p>
<dt><code>-MSB</code></p>
<dd> The byte order of the font should be requested as MSBFirst (most significant byte first).</p>
<dt><code>-ext</code>[ents_only]</p>
<dd> Only the character extents should be displayed, but not the bitmaps.</p>
<dt><code>-start</code><i> char</i></p>
<dd> The start of the range of the characters to display (<i>char</i> is a number).</p>
<dt><code>-end</code><i> char</i></p>
<dd> The end of the range of the characters to display (<i>char</i> is a number).</p>
<dt><code>-unit</code><i> n</i></p>
<dd> The scanline unit of the font (8, 16, 32, or 64).</p>
<dt><code>-pad</code><i> n</i></p>
<dd> The scanpad unit of the font (8, 16, 32, or 64).</p>
<dt><code>-b</code>[itmap_pad]<i> n</i></p>
<dd> The bitmap padding unit of the font (0, 1, or 2, where 0 is ImageRectMin, 1 is ImageRectMaxWidth and 2 is ImageRectMax).</p>
<dt><code>-noprops</code></p>
<dd> Do not show the font properties.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xfs/">xfs</a>(1), <a href="/docs/linux/man/1-fslsfonts/">fslsfonts</a>(1), <a href="/docs/linux/man/1-fstobdf/">fstobdf</a>(1), <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTSERVER</code></p>
<dd> the default X font server to contact. The server name must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7).</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 1991, Network Computing Devices, Inc.<br />
 See <i><a href="/docs/linux/man/7-x/">X</a></i>(7) for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Dave Lemke, Network Computing Devices, Inc. </p>
<h2>Index</h2>
