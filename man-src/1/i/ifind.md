---
title: "ifind(1)"
name: "ifind"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifind/"
description: "ifind – Find the meta-data structure that has allocated a given disk unit or file name."
---

<h2 class="name">NAME</h2>
<p> ifind &#8211; Find the meta-data structure that has allocated a given disk unit or file name. </p>
<h2>SYNOPSIS</h2>
<p> <code>ifind [-avVl] [-f fstype] [-d data_unit] </code> <code>[-n file] [-p par_inode] [-z ZONE] [-i imgtype] [-o imgoffset] [-b dev_sector_size] </code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ifind</code> finds the meta-data structure that has <i>data_unit</i> allocated a data unit or has a given file name. In some cases any of the structures can be unallocated and this will still find the results. </p>
<h2>ARGUMENTS</h2>
<p> There are several required and optional arguments. The image file names must be specified each time:</p>
<dl>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<p> You must also specify what you are looking for and include one of the following:</p>
<dl>
<dt>-d data_unit</p>
<dd> Finds the meta data structure that has allocated a given data unit (block, cluster, etc.) </p>
<dt>-n file</p>
<dd> Finds the meta data structure that is pointed to by the given file name. </p>
<dt>-p par_inode</p>
<dd> Finds the unallocated MFT entries in an NTFS image that have the given inode as the parent. Can be used with &#8216;-l and -z&#8217;. </p>
</dl>
<p> There are also several optional arguments:</p>
<dl>
<dt>-a</p>
<dd> Find all meta-data structures (only works when looking with a data_unit).</p>
<dt>-f fstype</p>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-l</p>
<dd> List the details of each file found with &#8216;-p&#8217;, like &#8216;fls -l&#8217;.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-v</p>
<dd> Verbose output to stderr.</p>
<dt>-V</p>
<dd> Display version.</p>
<dt>-z ZONE</p>
<dd> If &#8216;-p -l&#8217; were given, this will set the timezone for the correct times. </p>
</dl>
<h2>EXAMPLES</h2>
<p> # ifind -f fat -d 456 fat-img.dd </p>
<p> # ifind -f linux-ext2 -n &quot;/etc/&quot; linux-img.dd </p>
<p> # ifind -f ntfs -p 5 -l -z EST5EDT ntfs-img.dd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
