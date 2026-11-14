---
title: "tsk_loaddb(1)"
name: "tsk_loaddb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsk_loaddb/"
description: "tsk_loaddb – populate a SQLite database with metadata from a disk image"
---

<h2 class="name">NAME</h2>
<p> tsk_loaddb &#8211; populate a SQLite database with metadata from a disk image </p>
<h2>SYNOPSIS</h2>
<p> <code>tsk_loaddb [-ahkvV] [ -i</code> <i>imgtype</i> <code>] [ -b</code> <i>dev_sector_size</i> <code>] [ -i</code> <i>imgtype</i> <code>] [ -d</code> <i>database</i> <code>]</code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tsk_loaddb</code> loads disk information from <i>image</i> to a SQLite database. This database can then be used by tools in other languages for analysis. By default, the database is stored in the same directory as the image with &quot;.db&quot; appended to the name or the database name can be specified with &#8216;-d&#8217;. </p>
<p> The arguments are as follows:</p>
<dl>
<dt>-a</p>
<dd> Adds image to an existing database instead of creating a new one. Requires that -d be also specified.</p>
<dt>-d database</p>
<dd> Path for the database (default is the same directory as the image with name derived from image name</p>
<dt>-v</p>
<dd> verbose output to stderr</p>
<dt>-V</p>
<dd> Print version</p>
<dt>-k</p>
<dd> Don&#8217;t create block data table. This table maps each block to the file that allocated it. This option will make this program run faster.</p>
<dt>-h</p>
<dd> Calculate MD5 hash value for each file and store it in table. This option will make the program run slower.</p>
<dt>-i imgtype</p>
<dd> The format of the image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-b dev_sector_size</p>
<dd> The size (in bytes) of the device sectors. If not given, autodetection methods are used.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To load image data from image.dd to image.dd.db: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># tsk_loaddb ./image.dd</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
