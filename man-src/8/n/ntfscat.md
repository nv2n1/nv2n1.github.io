---
title: "ntfscat(8)"
name: "ntfscat"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfscat/"
description: "ntfscat – print NTFS files and streams on the standard output"
---

<p>ntfscat &#8211; print NTFS files and streams on the standard output</p>
<h2>Synopsis</h2>
<p>[<i>options</i>] <i>device </i>[<i>file</i>]</p>
<h2>Description</h2>
<p><code>ntfscat</code> will read a file or stream from an NTFS volume and display the contents on the standard output. </p>
<p> The case of the filename passed to <code>ntfscat</code> is ignored.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfscat</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;attribute</code> TYPE</p>
<dd>Display the contents of a particular attribute type. By default, the unnamed $DATA attribute will be shown. The attribute can be specified by a number in decimal or hexadecimal, or by name. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Hex</code></td>
<td><code>Decimal</code></td>
<td><code>Name</code>
</td>
</tr>
<tr VALIGN=top>
<td>0x10</td>
<td>16</td>
<td>&quot;$STANDARD_INFORMATION&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x20</td>
<td>32</td>
<td>&quot;$ATTRIBUTE_LIST&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x30</td>
<td>48</td>
<td>&quot;$FILE_NAME&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x40</td>
<td>64</td>
<td>&quot;$OBJECT_ID&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x50</td>
<td>80</td>
<td>&quot;$SECURITY_DESCRIPTOR&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x60</td>
<td>96</td>
<td>&quot;$VOLUME_NAME&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x70</td>
<td>112</td>
<td>&quot;$VOLUME_INFORMATION&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x80</td>
<td>128</td>
<td>&quot;$DATA&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x90</td>
<td>144</td>
<td>&quot;$INDEX_ROOT&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xA0</td>
<td>160</td>
<td>&quot;$INDEX_ALLOCATION&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xB0</td>
<td>176</td>
<td>&quot;$BITMAP&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xC0</td>
<td>192</td>
<td>&quot;$REPARSE_POINT&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xD0</td>
<td>208</td>
<td>&quot;$EA_INFORMATION&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xE0</td>
<td>224</td>
<td>&quot;$EA&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0xF0</td>
<td>240</td>
<td>&quot;$PROPERTY_SET&quot;
</td>
</tr>
<tr VALIGN=top>
<td>0x100</td>
<td>256</td>
<td>&quot;$LOGGED_UTILITY_STREAM&quot;
</td>
</tr>
</table>
</table>
<p> <code>Notes</code> The attribute names may be given without the leading $ symbol.<br />
 If you use the $ symbol, you must quote the name to prevent the shell interpreting the name.</p>
<dt><code>-n</code>, <code>&#8211;attribute-name</code> NAME</p>
<dd>Display this named attribute, stream.</p>
<dt><code>-i</code>, <code>&#8211;inode</code> NUM</p>
<dd>Specify a file by its inode number instead of its name.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not using a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license <code>ntfscat</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</dl>
<h2>Examples</h2>
<p>Display the contents of a file in the root of an NTFS volume.</p>
<dl>
<dd><code>ntfscat /dev/hda1 boot.ini</code></dl>
<p> Display the contents of a file in a subdirectory of an NTFS volume.</p>
<dl>
<dd><code>ntfscat /dev/hda1 /winnt/system32/drivers/etc/hosts</code></dl>
<p> Display the contents of the $INDEX_ROOT attribute of the root directory (inode 5).</p>
<dl>
<dd><code>ntfscat /dev/hda1 -a INDEX_ROOT -i 5 | hexdump -C</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfscat</code>. If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfscat</code> was written by Richard Russon, Anton Altaparmakov and Szabolcs Szakacsits. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfscat</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p>Read <code><a href="/docs/linux/man/8-libntfs/">libntfs</a></code>(8) for details how to access encrypted files. <code><a href="/docs/linux/man/8-libntfs/">libntfs</a></code>(8), <code><a href="/docs/linux/man/8-ntfsls/">ntfsls</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
