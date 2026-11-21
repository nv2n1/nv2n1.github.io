---

title: "showfont(1)"
name: "showfont"
section: "1"
letter: "s"
url: "/docs/linux/man/1-showfont/"
description: "showfont – font dumper for X font server"
---

<p> <code>showfont</code> [ <i>-options</i> &#8230; ] <code>-fn</code> <i>pattern</i></p>
<p> <i>Showfont</i> displays data about a font that matches the given <i>pattern</i>. The information shown includes font information, font properties, character metrics, and character bitmaps. </p>
<p> The wildcard character &quot;*&quot; can be used to match any sequence of characters (including none) in the font name, and &quot;?&quot; can be used to match any single character. The &quot;*&quot; and &quot;?&quot; characters must be quoted to prevent them from being expanded by the shell. If no pattern is given, &quot;*&quot; is assumed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-server </code><i>servername</i></dt>
<dd> The X font server to contact. <i>servername</i> must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7). If not specified, the server name in the <code>FONTSERVER</code> environment variable is used.</dd>
<dt><code>-fn</code><i> name</i></dt>
<dd> The font to display.</dd>
<dt><code>-lsb</code></dt>
<dd> The bit order of the font should be requested as LSBFirst (least significant bit first).</dd>
<dt><code>-msb</code></dt>
<dd> The bit order of the font should be requested as MSBFirst (most significant bit first).</dd>
<dt><code>-LSB</code></dt>
<dd> The byte order of the font should be requested as LSBFirst (least significant byte first).</dd>
<dt><code>-MSB</code></dt>
<dd> The byte order of the font should be requested as MSBFirst (most significant byte first).</dd>
<dt><code>-ext</code>[ents_only]</dt>
<dd> Only the character extents should be displayed, but not the bitmaps.</dd>
<dt><code>-start</code><i> char</i></dt>
<dd> The start of the range of the characters to display (<i>char</i> is a number).</dd>
<dt><code>-end</code><i> char</i></dt>
<dd> The end of the range of the characters to display (<i>char</i> is a number).</dd>
<dt><code>-unit</code><i> n</i></dt>
<dd> The scanline unit of the font (8, 16, 32, or 64).</dd>
<dt><code>-pad</code><i> n</i></dt>
<dd> The scanpad unit of the font (8, 16, 32, or 64).</dd>
<dt><code>-b</code>[itmap_pad]<i> n</i></dt>
<dd> The bitmap padding unit of the font (0, 1, or 2, where 0 is ImageRectMin, 1 is ImageRectMaxWidth and 2 is ImageRectMax).</dd>
<dt><code>-noprops</code></dt>
<dd> Do not show the font properties.</dd></dl>
<h2>SEE ALSO</h2>
<p> xfs(1), <a href="/docs/linux/man/1-fslsfonts/">fslsfonts</a>(1), <a href="/docs/linux/man/1-fstobdf/">fstobdf</a>(1), <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTSERVER</code></dt>
<dd> the default X font server to contact. The server name must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7).</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright 1991, Network Computing Devices, Inc.<br />
 See <i><a href="/docs/linux/man/7-x/">X</a></i>(7) for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Dave Lemke, Network Computing Devices, Inc. </p>
