---
title: "mmls(1)"
name: "mmls"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmls/"
description: "mmls – Display the partition layout of a volume system (partition tables)"
---

<h2 class="name">NAME</h2>
<p> mmls &#8211; Display the partition layout of a volume system (partition tables) </p>
<h2>SYNOPSIS</h2>
<p> <code>mmls [-t</code> <i>mmtype </i> <code>] [-o</code> <i>offset</i> <code>] [ -i</code> <i>imgtype</i> <code>] [-b dev_sector_size] [-BrvV] [-aAmM]</code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mmls</code> displays the layout of the partitions in a volume system, which include partition tables and disk labels. </p>
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
<dt>-B</p>
<dd> Include a column with the partition sizes in bytes</p>
<dt>-r</p>
<dd> Recurse into DOS partitions and look for other partition tables. This setup frequently occurs when Unix is installed on x86 systems.</p>
<dt>-v</p>
<dd> Verbose output of debugging statements to stderr</p>
<dt>-V</p>
<dd> Display version</p>
<dt>-a</p>
<dd> Show allocated volumes</p>
<dt>-A</p>
<dd> Show unallocated volumes</p>
<dt>-m</p>
<dd> Show metadata volumes</p>
<dt>-M</p>
<dd> Hide metadata volumes</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<p> &#8216;mmls&#8217; is similar to &#8216;fdisk -lu&#8217; in Linux with a few differences. Namely, it will show which sectors are not being used so that those can be searched for hidden data. It also gives the length value so that it can be plugged into &#8216;dd&#8217; more easily for extracting the partitions. It also will show BSD disk labels for Free, Open, and NetBSD and will display the output in sectors and not cylinders. Lastly, it works on non-Linux systems. </p>
<p> If none of -a, -A, -m, or -M are given then all volume types will be listed. If any of them are given, then only the types specified on the command line will be listed. </p>
<p> Allocated volumes are those that are listed in a partition table in the volume system AND can store data. Unallocated volumes are virtually created by mmls to show you which sectors have not been allocated to a volume. The metadata volumes overlap the allocated and unallocated volumes and describe where the partition tables and other metadata structures are located. In some volume systems, these structures are in allocated space and in others they are in unallocated space. In some volume systems, their location is explicitly given in the partition tables and in others they are not. </p>
<h2>EXAMPLES</h2>
<p> To list the partition table of a Windows system using autodetect: </p>
<p> # mmls disk_image.dd </p>
<p> To list the contents of a BSD system that starts in sector 12345 of a split image: </p>
<p> # mmls -t bsd -o 12345 -i split disk-1.dd disk-2.dd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<h2>Index</h2>
