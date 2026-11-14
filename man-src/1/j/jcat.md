---
title: "jcat(1)"
name: "jcat"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jcat/"
description: "jcat – Show the contents of a block in the file system journal."
---

<h2 class="name">NAME</h2>
<p> jcat &#8211; Show the contents of a block in the file system journal. </p>
<h2>SYNOPSIS</h2>
<p> <code>jcat [-f</code> <i>fstype</i> <code>] [-vV] [-i imgtype] [-o imgoffset] [-b dev_sector_size] </code> <i>image [images]</i> <code>] [</code> <i>inode</i> <code>]</code> <i>jblk</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>jcat</code> shows the contents of a journal block in the file system journal. The inode address of the journal can be given or the default location will be used. Note that the block address is a journal block address and not a file system block. The raw output is given to STDOUT. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-f fstype</p>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-V</p>
<dd> Display version</p>
<dt>-v</p>
<dd> verbose output</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>[inode]</p>
<dd> The inode where the file system journal can be found. </p>
<dt>jblk</p>
<dd> The journal block to display. </p>
</dl>
<h2>EXAMPLES</h2>
<p> jcat -f linux-ext3 img.dd 34 | xxd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
