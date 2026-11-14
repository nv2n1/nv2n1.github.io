---
title: "mkdiskimage(1)"
name: "mkdiskimage"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkdiskimage/"
description: "mkdiskimage – Create a blank MS-DOS formatted hard disk image"
---

<h2 class="name">NAME</h2>
<p> <code>mkdiskimage</code> &#8211; Create a blank MS-DOS formatted hard disk image</p>
<h2>SYNOPSIS</h2>
<p> <code>mkdiskimage</code> [-doFMz4] [-i id] file cyl head sect </p>
<h2>DESCRIPTION</h2>
<p> This is a convenient tool to generate a hard disk image, pre-formatted according to the MS-DOS specification, and having stated properties. </p>
<p> A disk image named <i>file</i> will be created, large enough to have <i>cyl</i> cylinders, <i>head</i> heads, and <i>sect</i> sectors. Using <code>-M</code>, the value of <i>cyl</i> will instead be interpreted as size in MBytes. </p>
<p> Additional settings include ZIP type disks, FAT32 formatting, and the inclusion of an emulation header. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> Use the fourth partition table entry. This is the standard for ZIP-disks.</p>
<dt><code>-F</code></p>
<dd> Format the partition using a FAT32 file system.</p>
<dt><code>-M</code></p>
<dd> The argument <i>cyl</i> is given in Megabytes. Recalculate this to get the count in cylinders.</p>
<dt><code>-d</code></p>
<dd> Add a DOSEMU header.</p>
<dt><code>-i</code> <i>id</i></p>
<dd> Specify the MBR identity field as <i>id</i>.</p>
<dt><code>-o</code></p>
<dd> Print to stdout the file system offset.</p>
<dt><code>-z</code></p>
<dd> Use a ZIP-disk geometry. This needs <i>heads</i>=64 and <i>sect</i>=32. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-syslinux/">syslinux</a></i>(1) </p>
<h2>HOMEPAGE</h2>
<p> More information about the Syslinux project can be found on the homepage at &lt;<i><a rel="nofollow" href="http://syslinux.zytor.com/">http://syslinux.zytor.com/</a></i>&gt;. </p>
<h2>AUTHOR</h2>
<p> mkdiskimage was written by H. Peter Anvin &lt;<i>hpa [at] zytor.com</i>&gt;. </p>
<p> This manual page was written by Mats Erik Andersson &lt;<i>debian [at] gisladisker.se</i>&gt;. </p>
<h2>Index</h2>
