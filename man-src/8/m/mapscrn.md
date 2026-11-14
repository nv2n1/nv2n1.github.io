---
title: "mapscrn(8)"
name: "mapscrn"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mapscrn/"
description: "mapscrn – load screen output mapping table"
---

<p>mapscrn &#8211; load screen output mapping table</p>
<h2>Synopsis</h2>
<p><code>mapscrn</code> [<code>-V</code>] [<code>-v</code>] [<code>-o</code> <i>map.orig</i>] <i>mapfile</i></p>
<h2>Description</h2>
<p>The <code>mapscrn</code> command is obsolete &#8211; its function is now built-in into setfont. However, for backwards compatibility it is still available as a separate command. </p>
<p> The <i>mapscrn</i> command loads a user defined output character mapping table into the console driver. The console driver may be later put into <code>use user-defined mapping table</code> mode by outputting a special escape sequence to the console device. This sequence is <i>&lt;esc&gt;(K</i> for the <code>G0</code> character set and <i>&lt;esc&gt;)K</i> for the <code>G1</code> character set. When the <i>-o</i> option is given, the old map is saved in <i>map.orig.</i></p>
<h2>Use</h2>
<p>There are two kinds of mapping tables: direct-to-font tables, that give a font position for each user byte value, and user-to-unicode tables that give a unicode value for each user byte. The corresponding glyph is now found using the unicode index of the font. The command</p>
<dl>
<dd>mapscrn trivial</dl>
<p> sets up a one-to-one direct-to-font table where user bytes directly address the font. This is useful for fonts that are in the same order as the character set one uses. A command like</p>
<dl>
<dd>mapscrn 8859-2</dl>
<p> sets up a user-to-unicode table that assumes that the user uses ISO 8859-2.</p>
<h2>Input Format</h2>
<p>The <i>mapscrn</i> command can read the map in either of two formats:<br />
 1. 256 or 512 bytes binary data<br />
 2. two-column text file<br />
 Format (1) is a direct image of the translation <i>table. The 256-bytes tables are direct-to-font,</i> the 512-bytes tables are user-to-unicode tables. Format (2) is used to fill the <i>table</i> as follows: cell with offset mentioned in the first column is filled with the value mentioned in the second column. When values larger than 255 occur, or values are written using the U+xxxx notation, the table is assumed to be a user-to-unicode table, otherwise it is a direct-to-font table. </p>
<p> Values in the file may be specified in one of several <code>formats:</code><br />
 <code>1. Decimal:</code> String of decimal digits not starting with &#8216;0&#8217;<br />
 <code>2. Octal:</code> String of octal digits beginning with &#8216;0&#8217;.<br />
 <code>3. Hexadecimal:</code> String of hexadecimal digits preceded by &quot;0x&quot;.<br />
 <code>4. Unicode:</code> String of four hexadecimal digits preceded by &quot;U+&quot;.<br />
 <code>5. Character:</code> Single character enclosed in single quotes. (And the binary value is used.) Note that blank, comma, tab character and &#8216;#&#8217; cannot be specified with this format.<br />
 <code>6. UTF-8 Character:</code> Single (possibly multi-byte) UTF-8 character, enclosed in single quotes. </p>
<p> Note that control characters (with codes &lt; 32) cannot be re-mapped with <i>mapscrn</i> because they have special meaning for the driver.</p>
<h2>Other Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>Prints version number and exits.</p>
<dt><code>-v</code></p>
<dd>Be verbose.</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/consoletrans</i></p>
<dd>The default directory for screen mappings.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-setfont/">setfont</a></i>(8)</p>
<h2>Author</h2>
<p>Copyright (C) 1993 Eugene G. Crosser<br />
 &lt;crosser [at] pccross.msk.su&gt;<br />
 This software and documentation may be distributed freely.</p>
