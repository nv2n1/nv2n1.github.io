---
title: "blkstat(1)"
name: "blkstat"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blkstat/"
description: "blkstat – Display details of a file system data unit (i.e. block or sector)"
---

<h2 class="name">NAME</h2>
<p> blkstat &#8211; Display details of a file system data unit (i.e. block or sector) </p>
<h2>SYNOPSIS</h2>
<p> <code>blkstat [-f</code> <i>fstype </i> <code>] [-i imgtype] [-o imgoffset] [-b dev_sector_size] [-vV] </code> <i>image [images] addr</i></p>
<h2>DESCRIPTION</h2>
<p> <code>blkstat</code> displays the allocation status of the given data unit. <code>blkstat</code> was called <code>dstat</code> in TSK versions prior to 3.0.0. </p>
<h2>ARGUMENTS</h2>
<dl>
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
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>addr</dt>
<dd> Address to display stats on. This is a fragment for UNIX file systems or a sector for FAT. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
