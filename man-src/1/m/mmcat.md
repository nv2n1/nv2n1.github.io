---
title: "mmcat(1)"
name: "mmcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmcat/"
description: "mmcat – Output the contents of a partition to stdout"
---

<h2 class="name">NAME</h2>
<p> mmcat &#8211; Output the contents of a partition to stdout </p>
<h2>SYNOPSIS</h2>
<p> <code>mmcat [-t</code> <i>mmtype </i> <code>] [-o</code> <i>offset</i> <code>] [ -i</code> <i>imgtype</i> <code>] [-b dev_sector_size] [-vV] </code> <i>image [images] part_num</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mmcat</code> outputs the contents of a specific volume to stdout. This allows you to extract the contents of a partition to a separate file. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-t mmtype</p>
<dd> Specify the media management type. Use &#8216;-t list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o offset</p>
<dd> Specify the offset into the image where the volume containing the partition system starts. The relative offset of the partition system will be added to this value.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-v</p>
<dd> Verbose output of debugging statements to stderr</p>
<dt>-V</p>
<dd> Display version</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>part_num</p>
<dd> Address of partition to process. See the mmls output to determine the address of the partitions. </p>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
