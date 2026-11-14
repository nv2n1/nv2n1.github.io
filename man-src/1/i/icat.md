---
title: "icat(1)"
name: "icat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icat/"
description: "icat – Output the contents of a file based on its inode number."
---

<h2 class="name">NAME</h2>
<p> icat &#8211; Output the contents of a file based on its inode number. </p>
<h2>SYNOPSIS</h2>
<p> <code>icat [-hrsvV] [-f</code> <i>fstype</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o </code> <i>imgoffset</i> <code>] [-b dev_sector_size] </code> <i>image [images] inode </i></p>
<h2>DESCRIPTION</h2>
<p> <code>icat</code> opens the named <i>image(s)</i> and copies the file with the specified <i>inode</i> number to standard output. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-f fstype</p>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-h</p>
<dd> Skip over holes in sparse files, so that absolute address information is lost. This option saves space when copying sparse files.</p>
<dt>-r</p>
<dd> Use file recovery techniques if the file is deleted.</p>
<dt>-s</p>
<dd> Include the slack space in the output.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-v</p>
<dd> Enable verbose mode, output to stderr.</p>
<dt>-V</p>
<dd> Display version</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>inode</p>
<dd> Inode number. <code>icat</code> concatenates the contents of all specified files. </p>
</dl>
<h2>LICENSE</h2>
<p> This software is distributed under the IBM Public License.</p>
<h2>HISTORY</h2>
<p> First appeared in The Coroners Toolkit (TCT) 1.0 and is now in The Sleuth Kit.</p>
<h2>AUTHOR(S)</h2>
<p> Wietse Venema IBM T.J. Watson Research P.O. Box 704 Yorktown Heights, NY 10598, USA </p>
<p> This version is maintained by Brian Carrier (carrier at sleuthkit at org). </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
