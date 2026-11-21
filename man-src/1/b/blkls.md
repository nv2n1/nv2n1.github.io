---
title: "blkls(1)"
name: "blkls"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blkls/"
description: "blkls – List or output file system data units."
---

<h2 class="name">NAME</h2>
<p> blkls &#8211; List or output file system data units. </p>
<h2>SYNOPSIS</h2>
<p> <code>blkls [-aAelsvV] [-f </code> <i>fstype</i> <code>] [-i </code> <i>imgtype</i> <code>] [-o </code> <i>imgoffset</i> <code>]</code> <i>[-b dev_sector_size] image [images] [start-stop]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>blkls</code> opens the named <i>image(s)</i> and copies file system data units (blocks). By default, <code>blkls</code> copies the contents of unallocated data blocks. <code>blkls </code> was called <code>dls</code> in TSK versions prior to 3.0.0. <code>blkls </code> was called <code>unrm</code> in TCT. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-e</dt>
<dd> Copy every block, including file system metadata blocks. The output is the entire file system.</dd>
<dt>-a</dt>
<dd> Display all allocated blocks (same as -e if -A is also given).</dd>
<dt>-A</dt>
<dd> Display all unallocated blocks (same as -e if -a is also given). This is the default behavior.</dd>
<dt>-f fstype</dt>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt>-l</dt>
<dd> List the data information in time machine format.</dd>
<dt>-s</dt>
<dd> Copy only the slack space of the image.</dd>
<dt>-v</dt>
<dd> Turn on verbose mode, output to stderr.</dd>
<dt>-V</dt>
<dd> Display version.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt>start-stop &#8230;</dt>
<dd> Examine the specified block number or number range.</dd></dl>
<h2>LICENSE</h2>
<p> This software is distributed under the IBM Public License.</p>
<h2>HISTORY</h2>
<p> First appeared in The Coroners Toolkit (TCT) 1.0 (Wietse Venema). Now maintained by Brian Carrier &lt;carrier at sleuthkit dot org&gt;. </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
