---
title: "ntfsfallocate(8)"
name: "ntfsfallocate"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfsfallocate/"
description: "ntfsfallocate – preallocate space to a file on an NTFS volume"
---

<p>ntfsfallocate &#8211; preallocate space to a file on an NTFS volume</p>
<h2>Synopsis</h2>
<p><code>ntfsfallocate</code> [<i>options</i>] -l <i>length</i> <i>device</i> <i>file</i> <i>[attr-type</i> [<i>attr-name</i>]]</p>
<h2>Description</h2>
<p><code>ntfsfallocate</code> preallocates space for any attribute of a file or directory, thus reserving space before actual contents is written. This is similar to <a href="/docs/linux/man/1-fallocate/">fallocate</a>(1).</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>ntfsfallocate</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>This will override some sensible defaults, such as not using a mounted volume. Use this option with caution.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</p>
<dt><code>-l</code>, <code>&#8211;length</code> LENGTH</p>
<dd>This is a mandatory option to specify the number of bytes to preallocate. It will be rounded up to a multiple of the cluster size. A suffix of K, M, G, T, P or E may be appended to mean a multiplicative factor of a power of 1000. Similarly a suffix of Ki, Mi, Gi, Ti, Pi or Ei may be appended to mean a multiplicative factor of a power of 1024.</p>
<dt><code>-n</code>, <code>&#8211;no-size-change</code></p>
<dd>Do not change the apparent size of the file. The space allocated beyond the apparent size is not zeroed, but subsequent writing beyond the apparent end of file will force zeroing the inner allocated space as it cannot be considered as a hole any more, and this may take significant time.</p>
<dt><code>-N</code>, <code>&#8211;no-action</code></p>
<dd>Simulate the allocation without actually write to device.</p>
<dt><code>-o</code>, <code>&#8211;offset</code> OFFSET</p>
<dd>Specify the offset in the file where preallocation starts. By default, the preallocation is counted from the beginning of the file. Space already allocated in the area defined by offset and length is preserved.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress some debug/warning/error messages.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Display more debug/warning/error messages.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show the version number, copyright and license of <code>ntfsfallocate</code>.</p>
<dt><code>attr-type</code></p>
<dd>Define a particular attribute type to be preallocated (advanced use only). By default, the unnamed $DATA attribute (the contents of a plain file) will be preallocated. The attribute has to be specified by a number in decimal or hexadecimal : </p>
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
<dd>Define the name of the particular attribute type to be preallocated (advanced use only).</dl>
<h2>Examples</h2>
<p>Preallocate 100MB to the file database.db located in the Data directory which is at the root of an NTFS file system.</p>
<dl>
<dd><code>ntfsfallocate -l 100M /dev/sda1 Data/database.db</code> </p>
<h2>Bugs</h2>
<p>There are no known problems with <code>ntfsfallocate</code>, however it can lead to configurations not supported by Windows and Windows may crash (BSOD) when writing to preallocated clusters which were not written to earlier. Files with preallocated space should be fully be written to before they are updated by Windows. </p>
<p> If you find a bug in <code>ntfsfallocate</code> proper, please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>ntfsfallocate</code> was written by Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>ntfsfallocate</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfs-3g/">ntfs-3g</a></code>(8), <code><a href="/docs/linux/man/8-ntfstruncate/">ntfstruncate</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8), <code><a href="/docs/linux/man/1-fallocate/">fallocate</a></code>(1) </p>
