---
title: "fsstat(1)"
name: "fsstat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fsstat/"
description: "fsstat – Display general details of a file system"
---

<h2 class="name">NAME</h2>
<p> fsstat &#8211; Display general details of a file system </p>
<h2>SYNOPSIS</h2>
<p> <code>fsstat [-f </code> <i>fstype </i> <code>] [-i imgtype] [-o imgoffset] [-b dev_sector_size] [-tvV] </code> <i>image [images] </i></p>
<h2>DESCRIPTION</h2>
<p> <code>fsstat</code> displays the details associated with a file system. The output of this command is file system specific. At a minimum, the range of meta-data values (inode numbers) and content units (blocks or clusters) are given. Also given are details from the Super Block, such as mount times and and features. For file systems that use groups (FFS and EXT2FS), the layout of each group is listed. </p>
<p> For a FAT file system, the FAT table is displayed in a condensed format. Note that the data is in sectors and not in clusters. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-t type</dt>
<dd> Print the file system type only.</dd>
<dt>-f fstype</dt>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-v</dt>
<dd> Verbose output of debugging statements to stderr</dd>
<dt>-V</dt>
<dd> Display version</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
