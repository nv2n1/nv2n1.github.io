---
title: "ils(1)"
name: "ils"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ils/"
description: "ils – List inode information"
---

<h2 class="name">NAME</h2>
<p> ils &#8211; List inode information </p>
<h2>SYNOPSIS</h2>
<p> <code>ils [-emOpvV] [-f </code> <i>fstype</i> <code>] [-s </code> <i>seconds</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o</code> <i>imgoffset</i> <code>] [-b dev_sector_size] </code> <i>image [images] [start-stop]</i> </p>
<p> <code>ils [-aAlLvVzZ] [-f</code> <i>fstype</i> <code>] [-s</code> <i>seconds</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o</code> <i>imgoffset</i> <code>]</code> <i>image [images] [start-stop]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ils</code> opens the named <i>image(s)</i> and lists inode information. By default, <code>ils</code> lists only the inodes of removed files. </p>
<p> Arguments:</p>
<dl>
<dt><code>-e</code></p>
<dd> List every inode in the file system.</p>
<dt><code>-f</code><i> fstype</i></p>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt><code>-s</code><i> seconds</i></p>
<dd> The time skew of the original system in seconds. For example, if the original system was 100 seconds slow, this value would be -100.</p>
<dt><code>-m</code></p>
<dd> Display the inode details in the format that the mactime program reads (replaces the ils2mac script from TCT)</p>
<dt><code>-O</code></p>
<dd> List only inodes of removed files that are still open or executing. This option is short-hand notation for <code>-aL</code> &quot;(see the <code>fine controls</code> section below). (this used to be -o).</p>
<dt><code>-p</code></p>
<dd> Display orphan inodes (unallocated with no file name)</p>
<dt><code>-r</code></p>
<dd> (default) List only inodes of removed files. This option is short-hand notation for <code>-LZ</code> (see the <code>fine controls</code> section below).</p>
<dt>-i imgtype</p>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt>-o imgoffset</p>
<dd> The sector offset where the file system starts in the image.</p>
<dt>-b dev_sector_size</p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</p>
<dt><code>-v</code></p>
<dd> Turn on verbose mode, output to stderr.</p>
<dt><code>-V</code></p>
<dd> Display Version.</p>
<dt>image [images]</p>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</p>
<dt><i>start-stop</i></p>
<dd> Examine the specified inode number or number range.</dl>
<p> Fine controls:</p>
<dl>
<dt><code>-a</code></p>
<dd> List only allocated inodes: these belong to files with at least one directory entry in the file system, and to removed files that are still open or executing.</p>
<dt><code>-A</code></p>
<dd> List only unallocated inodes: these belong to files that no longer exist.</p>
<dt><code>-l</code></p>
<dd> List only inodes with at least one hard link. These belong to files with at least one directory entry in the file system.</p>
<dt><code>-L</code></p>
<dd> List only inodes without any hard links. These belong to files that no longer exist, and to removed files that are still open or executing.</p>
<dt><code>-z</code></p>
<dd> List only inodes that were likely to have not been used.</p>
<dt><code>-Z</code></p>
<dd> List only inodes that were likely to be used.</dl>
<p> The output format is in time machine format. The output begins with a two-line header that describes the data origin, and is followed by a one-line header that lists the names of the data attributes that make up the remainder of the output:</p>
<dl>
<dt>st_ino</p>
<dd> The inode number.</p>
<dt>st_alloc</p>
<dd> Allocation status: `a&#8217; for allocated inode, `f&#8217; for free inode.</p>
<dt>st_uid</p>
<dd> Owner user ID.</p>
<dt>st_gid</p>
<dd> Owner group ID.</p>
<dt>st_mtime</p>
<dd> UNIX time (seconds) of last file modification.</p>
<dt>st_atime</p>
<dd> UNIX time (seconds) of last file access.</p>
<dt>st_ctime</p>
<dd> UNIX time (seconds) of last inode status change.</p>
<dt>st_dtime</p>
<dd> UNIX time (seconds) of file deletion (LINUX only).</p>
<dt>st_mode</p>
<dd> File type and permissions (octal).</p>
<dt>st_nlink</p>
<dd> Number of hard links.</p>
<dt>st_size</p>
<dd> File size in bytes.</p>
<dt>st_block0,st_block1</p>
<dd> The first two entries in the direct block address list.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mactime/">mactime</a>(1)</p>
<h2>LICENSE</h2>
<p> This software is distributed under the IBM Public License.</p>
<h2>HISTORY</h2>
<p> First appeared in The Coroners Toolkit (TCT) 1.0.</p>
<h2>AUTHOR(S)</h2>
<p> Wietse Venema IBM T.J. Watson Research P.O. Box 704 Yorktown Heights, NY 10598, USA </p>
<p> This version is maintained by Brian Carrier (carrier at sleuthkit dot org) </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
