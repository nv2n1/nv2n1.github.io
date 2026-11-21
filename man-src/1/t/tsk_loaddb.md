---
title: "tsk_loaddb(1)"
name: "tsk_loaddb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsk_loaddb/"
description: "tsk_loaddb – populate a SQLite database with metadata from a disk image"
---

<h2>SYNOPSIS</h2>
<p> <code>tsk_loaddb [-ahkvV] [ -i</code> <i>imgtype</i> <code>] [ -b</code> <i>dev_sector_size</i> <code>] [ -i</code> <i>imgtype</i> <code>] [ -d</code> <i>database</i> <code>]</code> <i>image [images]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>tsk_loaddb</code> loads disk information from <i>image</i> to a SQLite database. This database can then be used by tools in other languages for analysis. By default, the database is stored in the same directory as the image with &quot;.db&quot; appended to the name or the database name can be specified with &#8216;-d&#8217;. </p>
<p> The arguments are as follows:</p>
<dl>
<dt>-a</dt>
<dd> Adds image to an existing database instead of creating a new one. Requires that -d be also specified.</dd>
<dt>-d database</dt>
<dd> Path for the database (default is the same directory as the image with name derived from image name</dd>
<dt>-v</dt>
<dd> verbose output to stderr</dd>
<dt>-V</dt>
<dd> Print version</dd>
<dt>-k</dt>
<dd> Don&#8217;t create block data table. This table maps each block to the file that allocated it. This option will make this program run faster.</dd>
<dt>-h</dt>
<dd> Calculate MD5 hash value for each file and store it in table. This option will make the program run slower.</dd>
<dt>-i imgtype</dt>
<dd> The format of the image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size (in bytes) of the device sectors. If not given, autodetection methods are used.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> To load image data from image.dd to image.dd.db: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt># tsk_loaddb ./image.dd</p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
