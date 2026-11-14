---
title: "usnjls(1)"
name: "usnjls"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usnjls/"
description: "usnjls – List the contents of a NTFS Update Sequence Number journal"
---

<h2 class="name">NAME</h2>
<p> usnjls &#8211; List the contents of a NTFS Update Sequence Number journal </p>
<h2>SYNOPSIS</h2>
<p> <code>usnjls [-f</code> <i>fstype</i> <code>] [-vV] [-i imgtype] [-o imgoffset] [-b dev_sector_size]</code> <i>image [images] [inode]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>usnjls</code> lists the records in a NTFS Update Sequence Number Journal. If inode is given, then it will look there for a journal. Otherwise, it will use the default location. The output lists the USN journal records. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-f fstype</p>
<dd> Specify the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw or split. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-l</p>
<dd> Print the output in long format describing the field values and unpacking the data into human readable strings.</p>
<dt>-m</p>
<dd> Print the output in mactime format.</p>
<dt>-V</p>
<dd> Display version</p>
<dt>-v</p>
<dd> verbose output</p>
<dt>image [images]</p>
<dd> One (or more if split) disk or partition images whose format is given with &#8216;-i&#8217;.</p>
<dt>[inode]</p>
<dd> The inode where the Update Sequence Number Journal can be found. </p>
</dl>
<h2>EXAMPLES</h2>
<p> usnjls -f ntfs img.dd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
