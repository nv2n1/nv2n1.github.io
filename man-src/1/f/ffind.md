---
title: "ffind(1)"
name: "ffind"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffind/"
description: "ffind – Finds the name of the file or directory using a given inode"
---

<h2 class="name">NAME</h2>
<p> ffind &#8211; Finds the name of the file or directory using a given inode </p>
<h2>SYNOPSIS</h2>
<p> <code>ffind [-aduvV] [-f fstype] [-i imgtype] [-o imgoffset] [-b dev_sector_size] </code> <i>image [images] inode</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ffind</code> finds the names of files or directories that are allocated to <i>inode</i> on disk image <i>image.</i> By default it only will only return the first name it finds. With some file systems, this will find deleted file names. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-a</p>
<dd> Find all occurrences of inode.</p>
<dt>-d</p>
<dd> Find deleted entries only.</p>
<dt>-f fstype</p>
<dd> Identify the file system type of the image. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-u</p>
<dd> Find undeleted entries only.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-v</p>
<dd> Verbose output to stderr.</p>
<dt>-V</p>
<dd> Display version.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>inode</p>
<dd> Integer of inode to find. </p>
</dl>
<p> This program searches all directory entries looking for the given inode. This is useful when an inode has been identified from a disk unit address using <code><a href="/docs/linux/man/1-ifind/">ifind</a>(1).</code> </p>
<h2>EXAMPLE</h2>
<p> # ffind -a image 212</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ifind/">ifind</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
