---
title: "ntfstruncate(8)"
name: "ntfstruncate"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfstruncate/"
description: "ntfstruncate – truncate a file on an NTFS volume"
---

<p>ntfstruncate &#8211; truncate a file on an NTFS volume</p>
<h2>Synopsis</h2>
<p><code>ntfstruncate</code> [<i>options</i>] <i>device</i> <i>file</i> <i>[attr-type</i> [<i>attr-name</i>]] <i>new-length</i></p>
<h2>Description</h2>
<p><code>ntfstruncate</code> truncates (or extends) a specified attribute belonging to a file or directory, to a specified length.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfstruncate</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not using a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-l</code></p>
<dd>Display licensing information.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Simulate the truncation without actually write to device.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license of <code>ntfstruncate</code>.</p>
<dt><code>attr-type</code></p>
<dd>Define a particular attribute type to be truncated (advanced use only). By default, the unnamed $DATA attribute (the contents of a plain file) will be truncated. The attribute has to be specified by a number in decimal or hexadecimal : </p>
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
<dt><code>attr-name</code></p>
<dd>Define the name of the particular attribute type to be truncated (advanced use only). </p>
<dt><code>new-length</code></p>
<dd>Specify the target size of the file. It will be rounded up to a multiple of the cluster size. A suffix of K, M, G, T, P or E may be appended to mean a multiplicative factor of a power of 1000. Similarly a suffix of Ki, Mi, Gi, Ti, Pi or Ei may be appended to mean a multiplicative factor of a power of 1024.</dl>
<h2>Examples</h2>
<p>Resize to 100MB the file database.db located in the Data directory which is at the root of an NTFS file system.</p>
<dl>
<dd><code>ntfstruncate /dev/sda1 Data/database.db 100M</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfstruncate</code>. If you find a bug, please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfstruncate</code> was written by Anton Altaparmakov.</p>
<h2>Availability</h2>
<p><code>ntfstruncate</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8), <code><a href="/docs/linux/man/8-ntfsfallocate/">ntfsfallocate</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8). </p>
