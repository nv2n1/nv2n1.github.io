---
title: "blkcat(1)"
name: "blkcat"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blkcat/"
description: "blkcat – Display the contents of file system data unit in a disk image."
---

<h2>SYNOPSIS</h2>
<p> <code>blkcat [-ahswvV] [-f fstype] [-u unit_size] [-i imgtype] [-o imgoffset] [-b dev_sector_size] </code> <i>image [images] unit_addr [num]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>blkcat</code> displays <code>num </code> data units (default is one) starting at the unit address <code>unit_addr</code> from <code>image</code> to stdout in different formats (default is raw). <code>blkcat</code> was called <code>dcat</code> in TSK versions prior to 3.0.0. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-a</dt>
<dd> Display the contents in ASCII</dd>
<dt>-f fstype</dt>
<dd> Specify image as a specific file type. If &#8216;swap&#8217; is given here, the image will be displayed in pages of size 4096 bytes. If &#8216;raw&#8217; is given, then 512-bytes is used as the default size. The &#8216;-u&#8217; flag can change the default size. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-h</dt>
<dd> Display the contents in hexdump</dd>
<dt>-s</dt>
<dd> Display statistics on the image (unit size, file block size, and number of fragments).</dd>
<dt>-u unit_size</dt>
<dd> Specify the size of the default data unit for raw, blkls, and swap images.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-v</dt>
<dd> Verbose output to stderr.</dd>
<dt>-V</dt>
<dd> Display version.</dd>
<dt>-w</dt>
<dd> Display the contents in an HTML table format.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>unit_addr</dt>
<dd> Address of the disk unit to display. The size of a unit on this file system can be determined using the -s option.</dd>
<dt>num</dt>
<dd> Number of data units to display. </dd>
</dl>
<p> The basic functionality of <code>blkcat</code> can also be achieved using <code>dd.</code> To determine which inode has allocated a given unit, the <code><a href="/docs/linux/man/1-ifind/">ifind</a>(1)</code> command can be used. </p>
<h2>EXAMPLES</h2>
<p> # blkcat -hw image 264 4 </p>
<p> or </p>
<p> # blkcat -hw image 264 </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ifind/">ifind</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
