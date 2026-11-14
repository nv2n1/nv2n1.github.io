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
<dt>-e</p>
<dd> Copy every block, including file system metadata blocks. The output is the entire file system.</p>
<dt>-a</p>
<dd> Display all allocated blocks (same as -e if -A is also given).</p>
<dt>-A</p>
<dd> Display all unallocated blocks (same as -e if -a is also given). This is the default behavior.</p>
<dt>-f fstype</p>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt>-l</p>
<dd> List the data information in time machine format.</p>
<dt>-s</p>
<dd> Copy only the slack space of the image.</p>
<dt>-v</p>
<dd> Turn on verbose mode, output to stderr.</p>
<dt>-V</p>
<dd> Display version.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt>start-stop &#8230;</p>
<dd> Examine the specified block number or number range.</dl>
<h2>LICENSE</h2>
<p> This software is distributed under the IBM Public License.</p>
<h2>HISTORY</h2>
<p> First appeared in The Coroners Toolkit (TCT) 1.0 (Wietse Venema). Now maintained by Brian Carrier &lt;carrier at sleuthkit dot org&gt;. </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
