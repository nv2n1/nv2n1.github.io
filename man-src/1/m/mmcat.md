---

title: "mmcat(1)"
name: "mmcat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmcat/"
description: "mmcat – Output the contents of a partition to stdout"
---

<p> <code>mmcat [-t</code> <i>mmtype </i> <code>] [-o</code> <i>offset</i> <code>] [ -i</code> <i>imgtype</i> <code>] [-b dev_sector_size] [-vV] </code> <i>image [images] part_num</i></p>
<p> <code>mmcat</code> outputs the contents of a specific volume to stdout. This allows you to extract the contents of a partition to a separate file. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-t mmtype</dt>
<dd> Specify the media management type. Use &#8216;-t list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o offset</dt>
<dd> Specify the offset into the image where the volume containing the partition system starts. The relative offset of the partition system will be added to this value.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-v</dt>
<dd> Verbose output of debugging statements to stderr</dd>
<dt>-V</dt>
<dd> Display version</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>part_num</dt>
<dd> Address of partition to process. See the mmls output to determine the address of the partitions. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
