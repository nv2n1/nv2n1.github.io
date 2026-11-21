---
title: "ifind(1)"
name: "ifind"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ifind/"
description: "ifind – Find the meta-data structure that has allocated a given disk unit or file name."
---

<h2>SYNOPSIS</h2>
<p> <code>ifind [-avVl] [-f fstype] [-d data_unit] </code> <code>[-n file] [-p par_inode] [-z ZONE] [-i imgtype] [-o imgoffset] [-b dev_sector_size] </code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ifind</code> finds the meta-data structure that has <i>data_unit</i> allocated a data unit or has a given file name. In some cases any of the structures can be unallocated and this will still find the results. </p>
<h2>ARGUMENTS</h2>
<p> There are several required and optional arguments. The image file names must be specified each time:</p>
<dl>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </dd>
</dl>
<p> You must also specify what you are looking for and include one of the following:</p>
<dl>
<dt>-d data_unit</dt>
<dd> Finds the meta data structure that has allocated a given data unit (block, cluster, etc.) </dd>
<dt>-n file</dt>
<dd> Finds the meta data structure that is pointed to by the given file name. </dd>
<dt>-p par_inode</dt>
<dd> Finds the unallocated MFT entries in an NTFS image that have the given inode as the parent. Can be used with &#8216;-l and -z&#8217;. </dd>
</dl>
<p> There are also several optional arguments:</p>
<dl>
<dt>-a</dt>
<dd> Find all meta-data structures (only works when looking with a data_unit).</dd>
<dt>-f fstype</dt>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-l</dt>
<dd> List the details of each file found with &#8216;-p&#8217;, like &#8216;fls -l&#8217;.</dd>
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
<dt>-z ZONE</dt>
<dd> If &#8216;-p -l&#8217; were given, this will set the timezone for the correct times. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> # ifind -f fat -d 456 fat-img.dd </p>
<p> # ifind -f linux-ext2 -n &quot;/etc/&quot; linux-img.dd </p>
<p> # ifind -f ntfs -p 5 -l -z EST5EDT ntfs-img.dd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
