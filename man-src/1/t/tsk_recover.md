---
title: "tsk_recover(1)"
name: "tsk_recover"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsk_recover/"
description: "tsk_recover – Export files from an image into a local directory"
---

<h2 class="name">NAME</h2>
<p> tsk_recover &#8211; Export files from an image into a local directory </p>
<h2>SYNOPSIS</h2>
<p> <code>tsk_recover [-vVae] [ -f</code> <i>fstype</i> <code>] [ -i</code> <i>imgtype</i> <code>] [ -b</code> <i>dev_sector_size</i> <code>] [ -o</code> <i>sector_offset</i> <code>] [ -d </code> <i>dir_inum</i> <code>]</code> <i>image [images] output_dir </i></p>
<h2>DESCRIPTION</h2>
<p> <code>tsk_recover</code> recovers files to the <i>output_dir</i> from the <i>image.</i> By default recovers only unallocated files. With flags, it will export all files. </p>
<p> The arguments are as follows:</p>
<dl>
<dt>-v</p>
<dd> verbose output to stderr</p>
<dt>-V</p>
<dd> Print version</p>
<dt>-a</p>
<dd> Recover allocated files only</p>
<dt>-e</p>
<dd> Recover all files (allocated and unallocated)</p>
<dt>-f fstype</p>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-i imgtype</p>
<dd> The format of the image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-b dev_sector_size</p>
<dd> The size (in bytes) of the device sectors. If not given, autodetection methods are used.</p>
<dt>-o sector_offset</p>
<dd> Sector offset for a volume to recover (recovers only that volume) If not given, will attempt to recover all volumes in image and save them to different folders.</p>
<dt>-d dir_inum</p>
<dd> Directory inum to recover from (must also specify a specific partition using -o or there must not be a volume system)</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>output_dir</p>
<dd> The directory in which to save recovered files. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To recover only unallocated files from image.dd to the recovered directory: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># tsk_recover ./image.dd ./recovered</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
