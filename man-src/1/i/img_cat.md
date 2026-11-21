---

title: "img_cat(1)"
name: "img_cat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-img_cat/"
description: "img_cat – Output contents of an image file."
---

<p> <code>img_cat [-i imgtype] [-b dev_sector_size] [-s start_sector] [-e stop_sector] [-vV] </code> <i>image [images] </i></p>
<p> <code>img_cat</code> outputs the contents of an image file. Image files that are not raw will have embedded data and metadata. img_cat will output only the data. This allows you to convert an embedded format to raw or to calculate the MD5 hash of the data by piping the output to the appropriate tool. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw or aff. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-s start_sector</dt>
<dd> The sector number to start at.</dd>
<dt>-e stop_sector</dt>
<dd> The sector number to stop at.</dd>
<dt>-v</dt>
<dd> Verbose output of debugging statements to stderr</dd>
<dt>-V</dt>
<dd> Display version</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
