---
title: "img_stat(1)"
name: "img_stat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img_stat/"
description: "img_stat – Display details of an image file"
---

<h2 class="name">NAME</h2>
<p> img_stat &#8211; Display details of an image file </p>
<h2>SYNOPSIS</h2>
<p> <code>img_stat [-i imgtype] [-b dev_sector_size] [-tvV] </code> <i>image [images] </i></p>
<h2>DESCRIPTION</h2>
<p> <code>img_stat</code> displays the details associated with an image file. The output of this command is image format specific. At a minimum, the size will be given and the byte range of each file will be given for split image formats. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-t</p>
<dd> Print the image type only.</p>
<dt>-v</p>
<dd> Verbose output of debugging statements to stderr</p>
<dt>-V</p>
<dd> Display version</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
