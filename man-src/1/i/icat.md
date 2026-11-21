---

title: "icat(1)"
name: "icat"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icat/"
description: "icat – Output the contents of a file based on its inode number."
---

<p> <code>icat [-hrsvV] [-f</code> <i>fstype</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o </code> <i>imgoffset</i> <code>] [-b dev_sector_size] </code> <i>image [images] inode </i></p>
<p> <code>icat</code> opens the named <i>image(s)</i> and copies the file with the specified <i>inode</i> number to standard output. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-f fstype</dt>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-h</dt>
<dd> Skip over holes in sparse files, so that absolute address information is lost. This option saves space when copying sparse files.</dd>
<dt>-r</dt>
<dd> Use file recovery techniques if the file is deleted.</dd>
<dt>-s</dt>
<dd> Include the slack space in the output.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-v</dt>
<dd> Enable verbose mode, output to stderr.</dd>
<dt>-V</dt>
<dd> Display version</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>inode</dt>
<dd> Inode number. <code>icat</code> concatenates the contents of all specified files. </dd>
</dl>
<h2>LICENSE</h2>
<p> This software is distributed under the IBM Public License.</p>
<h2>HISTORY</h2>
<p> First appeared in The Coroners Toolkit (TCT) 1.0 and is now in The Sleuth Kit.</p>
<h2>AUTHOR(S)</h2>
<p> Wietse Venema IBM T.J. Watson Research P.O. Box 704 Yorktown Heights, NY 10598, USA </p>
<p> This version is maintained by Brian Carrier (carrier at sleuthkit at org). </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
