---

title: "istat(1)"
name: "istat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-istat/"
description: "istat – Display details of a meta-data structure (i.e. inode)"
---

<p> <code>istat [-B </code> <i>num</i> <code>] [-f</code> <i>fstype </i> <code>] [-i imgtype] [-o imgoffset] [-b dev_sector_size] [-vV] [-z</code> <i>zone</i> <code>] [-s</code> <i>seconds</i> <code>]</code> <i>image [images] inode</i></p>
<p> <code>istat</code> displays the uid, gid, mode, size, link number, modified, accessed, changed times, and all the disk units a structure has allocated. </p>
<p> The options are as follows:</p>
<dl>
<dt>-B num</dt>
<dd> Display the addresses of num disk units. Useful when the inode is unallocated with size 0, but still has block pointers.</dd>
<dt>-f fstype</dt>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-s seconds</dt>
<dd> The time skew of the original system in seconds. For example, if the original system was 100 seconds slow, this value would be -100.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-v</dt>
<dd> Verbose output of debugging statements to stderr</dd>
<dt>-V</dt>
<dd> Display version</dd>
<dt>-z zone</dt>
<dd> An ASCII string of the original system&#8217;s time zone. For example, EST5EDT or GMT. These strings are defined by the operating system and may vary. NOTE: This has changed since TCTUTILs.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>inode</dt>
<dd> Meta-data number to display stats on </dd>
</dl>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
