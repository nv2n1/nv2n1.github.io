---
title: "tsk_comparedir(1)"
name: "tsk_comparedir"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsk_comparedir/"
description: "tsk_comparedir – compare the contents of a directory with the contents of an image or local device."
---

<h2 class="name">NAME</h2>
<p> tsk_comparedir &#8211; compare the contents of a directory with the contents of an image or local device. </p>
<h2>SYNOPSIS</h2>
<p> <code>tsk_comparedir [-vV] [-n</code> <i>start_inum</i> <code>] [ -f</code> <i>fstype</i> <code>] [ -i</code> <i>imgtype</i> <code>] [ -b</code> <i>dev_sector_size</i> <code>] [ -o</code> <i>sector_offset</i> <code>]</code> <i>image [images] comparison_directory</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tsk_comparedir </code> compares the contents of <i>image</i> to the contents of <i>comparison_directory.</i> This can be useful for detecting rootkits and when testing. Rootkits can be detected by comparing the contents of a local directory and a local raw device. The rootkits typically don&#8217;t hide data when it is read directly from the raw device. </p>
<p> The arguments are as follows:</p>
<dl>
<dt>-o sector_offset</p>
<dd> Sector offset for a partition in the image or device to compare with.</p>
<dt>-n start_inum</p>
<dd> Starting inum for a directory in the image to start the comparison at.</p>
<dt>-v</p>
<dd> verbose output to stderr</p>
<dt>-V</p>
<dd> Print version</p>
<dt>-f fstype</p>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-i imgtype</p>
<dd> The format of the image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-b dev_sector_size</p>
<dd> The size (in bytes) of the device sectors. If not given, autodetection methods are used.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To compare the directories in image.dd to those in directory: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># tsk_comparedir ./image.dd ./directory</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
