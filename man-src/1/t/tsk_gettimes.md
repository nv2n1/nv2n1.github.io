---
title: "tsk_gettimes(1)"
name: "tsk_gettimes"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsk_gettimes/"
description: "tsk_gettimes – Collect MAC times from a disk image into a body file."
---

<h2 class="name">NAME</h2>
<p> tsk_gettimes &#8211; Collect MAC times from a disk image into a body file. </p>
<h2>SYNOPSIS</h2>
<p> <code>tsk_gettimes [-vV] [ -f</code> <i>fstype</i> <code>] [ -i</code> <i>imgtype</i> <code>] [ -b</code> <i>dev_sector_size</i> <code>] [ -z</code> <i>zone</i> <code>] [ -s</code> <i>seconds</i> <code>] </code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tsk_gettimes</code> examines each of the file systems in a disk image and returns the data about them in the MACtime body format (the same as running &#8216;fls -m&#8217; on each file system). The output of this can be used as input to mactime to make a timeline of file activity. The data is printed to STDOUT, which can then be redirected to a file. </p>
<p> The arguments are as follows:</p>
<dl>
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
<dt>-o sector_offset</p>
<dd> Sector offset for a volume to recover (recovers only that volume) If not given, will attempt to recover all volumes in image and save them to different folders.</p>
<dt>-s seconds</p>
<dd> The time skew of the original system in seconds. For example, if the original system was 100 seconds slow, this value would be -100.</p>
<dt>-z zone</p>
<dd> The ASCII string of the time zone of the original system. For example, EST or GMT. These strings must be defined by your operating system and may vary.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To collect data about image image.dd: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># tsk_gettimes ./image.dd &gt; body.txt</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
