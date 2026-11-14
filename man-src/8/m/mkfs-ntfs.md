---
title: "mkfs-ntfs(8)"
name: "mkfs-ntfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-ntfs/"
description: "mkntfs – create an NTFS file system"
---

<p>mkntfs &#8211; create an NTFS file system</p>
<h2>Synopsis</h2>
<p><code>mkntfs</code> [<i>options</i>] <i>device </i>[<i>number-of-sectors</i>] </p>
<p> <code>mkntfs</code> [ <code>-C</code> ] [ <code>-c</code> <i>cluster-size</i> ] [ <code>-F</code> ] [ <code>-f</code> ] [ <code>-H</code> <i>heads</i> ] [ <code>-h</code> ] [ <code>-I</code> ] [ <code>-L</code> <i>volume-label</i> ] [ <code>-l</code> ] [ <code>-n</code> ] [ <code>-p</code> <i>part-start-sect</i> ] [ <code>-Q</code> ] [ <code>-q</code> ] [ <code>-S</code> <i>sectors-per-track</i> ] [ <code>-s</code> <i>sector-size</i> ] [ <code>-T</code> ] [ <code>-U</code> ] [ <code>-V</code> ] [ <code>-v</code> ] [ <code>-z</code> <i>mft-zone-multiplier</i> ] [ <code>&#8211;debug</code> ] <i>device</i> [ <i>number-of-sectors</i> ]</p>
<h2>Description</h2>
<p><code>mkntfs</code> is used to create an NTFS file system on a device (usually a disk partition) or file. <i>device</i> is the special file corresponding to the device (e.g <i>/dev/hdXX</i>). <i>number-of-sectors</i> is the number of sectors on the device. If omitted, <code>mkntfs</code> automagically figures the file system size.</p>
<h2>Options</h2>
<p>Below is a summary of all the options that <code>mkntfs</code> accepts. Nearly all options have two equivalent names. The short name is preceded by <code>&#8211;</code> and the long name is preceded by <code>&#8212;</code>. Any single letter options, that don&#8217;t take an argument, can be combined into a single command, e.g. <code>-fv</code> is equivalent to <code>-f -v</code>. Long named options can be abbreviated to any unique prefix of their name.</p>
<h3>Basic options</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;fast</code>, <code>-Q</code>, <code>&#8211;quick</code></p>
<dd>Perform quick (fast) format. This will skip both zeroing of the volume and bad sector checking.</p>
<dt><code>-L</code>, <code>&#8211;label</code> STRING</p>
<dd>Set the volume label for the filesystem.</p>
<dt><code>-C</code>, <code>&#8211;enable-compression</code></p>
<dd>Enable compression on the volume.</p>
<dt><code>-n</code>, <code>&#8211;no-action</code></p>
<dd>Causes <code>mkntfs</code> to not actually create a filesystem, but display what it would do if it were to create a filesystem. All steps of the format are carried out except the actual writing to the device.</dl>
<h3>Advanced options</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;cluster-size</code> BYTES</p>
<dd>Specify the size of clusters in bytes. Valid cluster size values are powers of two, with at least 256, and at most 2097152 bytes (2MB) per cluster. If omitted, <code>mkntfs</code> uses 4096 bytes as the default cluster size. </p>
<p> Note that the default cluster size is set to be at least equal to the sector size as a cluster cannot be smaller than a sector. Also, note that values greater than 4096 have the side effect that compression is disabled on the volume (due to limitations in the NTFS compression algorithm currently in use by Windows).</p>
<dt><code>-s</code>, <code>&#8211;sector-size</code> BYTES</p>
<dd>Specify the size of sectors in bytes. Valid sector size values are 256, 512, 1024, 2048 and 4096 bytes per sector. If omitted, <code>mkntfs</code> attempts to determine the <i>sector-size</i> automatically and if that fails a default of 512 bytes per sector is used.</p>
<dt><code>-p</code>, <code>&#8211;partition-start</code> SECTOR</p>
<dd>Specify the partition start sector. The maximum is 4294967295 (2^32-1). If omitted, <code>mkntfs</code> attempts to determine <i>part-start-sect</i> automatically and if that fails or the value is oversized, a default of 0 is used. The partition is usable despite a wrong value, however note that a correct <i>part-start-sect</i> is required for Windows to be able to boot from the created volume.</p>
<dt><code>-H</code>, <code>&#8211;heads</code> NUM</p>
<dd>Specify the number of heads. The maximum is 65535 (0xffff). If omitted, <code>mkntfs</code> attempts to determine the number of <i>heads</i> automatically and if that fails a default of 0 is used. Note that <i>heads</i> is required for Windows to be able to boot from the created volume.</p>
<dt><code>-S</code>, <code>&#8211;sectors-per-track</code> NUM</p>
<dd>Specify the number of sectors per track. The maximum is 65535 (0xffff). If omitted, <code>mkntfs</code> attempts to determine the number of <i>sectors-per-track</i> automatically and if that fails a default of 0 is used. Note that <i>sectors-per-track</i> is required for Windows to be able to boot from the created volume.</p>
<dt><code>-z</code>, <code>&#8211;mft-zone-multiplier</code> NUM</p>
<dd>Set the MFT zone multiplier, which determines the size of the MFT zone to use on the volume. The MFT zone is the area at the beginning of the volume reserved for the master file table (MFT), which stores the on disk inodes (MFT records). It is noteworthy that small files are stored entirely within the inode; thus, if you expect to use the volume for storing large numbers of very small files, it is useful to set the zone multiplier to a higher value. Note, that the MFT zone is resized on the fly as required during operation of the NTFS driver but choosing a good value will reduce fragmentation. Valid values are 1, 2, 3 and 4. The values have the following meaning: </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>MFT zone</code></td>
<td><code>MFT zone size</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>multiplier</code></td>
<td><code>(% of volume size)</code>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>1</td>
<td>12.5% (default)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2</td>
<td>25.0%
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>3</td>
<td>37.5%
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td>50.0%
</td>
</tr>
</table>
</table>
<dt><code>-T</code>, <code>&#8211;zero-time</code></p>
<dd>Fake the time to be 00:00:00 UTC, Jan 1, 1970 instead of the current system time. This is only really useful for debugging purposes.</p>
<dt><code>-U</code>, <code>&#8211;with-uuid</code></p>
<dd>Generate a random volume UUID.</p>
<dt><code>-I</code>, <code>&#8211;no-indexing</code></p>
<dd>Disable content indexing on the volume. (This is only meaningful on Windows 2000 and later. Windows NT 4.0 and earlier ignore this as they do not implement content indexing at all.)</p>
<dt><code>-F</code>, <code>&#8211;force</code></p>
<dd>Force <code>mkntfs</code> to run, even if the specified <i>device</i> is not a block special device, or appears to be mounted.</dl>
<h3>Output options</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Quiet execution; only errors are written to stderr, no output to stdout occurs at all. Useful if <code>mkntfs</code> is run in a script.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose execution.</p>
<dt><code>&#8211;debug</code></p>
<dd>Really verbose execution; includes the verbose output from the <code>-v</code> option as well as additional output useful for debugging <code>mkntfs.</code></dl>
<h3>Help options</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print the version number of <code>mkntfs</code> and exit.</p>
<dt><code>-l</code>, <code>&#8211;license</code></p>
<dd>Print the licensing information of <code>mkntfs</code> and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a list of options with a brief description of each one.</dl>
<h2>Known Issues</h2>
<p>When applying chkdsk to a file system, it sometimes throws a warning &quot;Correcting errors in the uppercase file.&quot; The uppercase file is created while formatting and it defines the mapping of lower case characters to upper case ones, as needed to sort file names in directories. The warning means that the uppercase file defined on the file system is not the same as the one used by the Windows OS on which chkdsk is running, and this may happen because newer versions of Windows take into account new characters defined by the Unicode consortium. </p>
<p> Currently, mkntfs creates the uppercase table so that no warning is thrown by Windows Vista, Windows 7 or Windows 8. A warning may be thrown by other Windows versions, or if chkdsk is applied in succession on different Windows versions.</p>
<h2>Bugs</h2>
<p>If you find a bug please send an email describing the problem to the development team:<br />
 ntfs-3g-devel [at] lists.sf.net</p>
<h2>Authors</h2>
<p><code>mkntfs</code> was written by Anton Altaparmakov, Richard Russon, Erik Sornes and Szabolcs Szakacsits. It was ported to ntfs-3g by Erik Larsson and Jean-Pierre Andre.</p>
<h2>Availability</h2>
<p><code>mkntfs</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-badblocks/">badblocks</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
