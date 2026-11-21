---
title: "ils(1)"
name: "ils"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ils/"
description: "ils – List inode information"
---

<h2>SYNOPSIS</h2>
<p> <code>ils [-emOpvV] [-f </code> <i>fstype</i> <code>] [-s </code> <i>seconds</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o</code> <i>imgoffset</i> <code>] [-b dev_sector_size] </code> <i>image [images] [start-stop]</i> </p>
<p> <code>ils [-aAlLvVzZ] [-f</code> <i>fstype</i> <code>] [-s</code> <i>seconds</i> <code>] [-i</code> <i>imgtype</i> <code>] [-o</code> <i>imgoffset</i> <code>]</code> <i>image [images] [start-stop]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ils</code> opens the named <i>image(s)</i> and lists inode information. By default, <code>ils</code> lists only the inodes of removed files. </p>
<p> Arguments:</p>
<dl>
<dt><code>-e</code></dt>
<dd> List every inode in the file system.</dd>
<dt><code>-f</code><i> fstype</i></dt>
<dd> Specifies the file system type. Use &#8216;-f list&#8217; to list the supported file system types. If not given, autodetection methods are used.</dd>
<dt><code>-s</code><i> seconds</i></dt>
<dd> The time skew of the original system in seconds. For example, if the original system was 100 seconds slow, this value would be -100.</dd>
<dt><code>-m</code></dt>
<dd> Display the inode details in the format that the mactime program reads (replaces the ils2mac script from TCT)</dd>
<dt><code>-O</code></dt>
<dd> List only inodes of removed files that are still open or executing. This option is short-hand notation for <code>-aL</code> &quot;(see the <code>fine controls</code> section below). (this used to be -o).</dd>
<dt><code>-p</code></dt>
<dd> Display orphan inodes (unallocated with no file name)</dd>
<dt><code>-r</code></dt>
<dd> (default) List only inodes of removed files. This option is short-hand notation for <code>-LZ</code> (see the <code>fine controls</code> section below).</dd>
<dt>-i imgtype</dt>
<dd> Identify the type of image file, such as raw. Use &#8216;-i list&#8217; to list the supported types. If not given, autodetection methods are used.</dd>
<dt>-o imgoffset</dt>
<dd> The sector offset where the file system starts in the image.</dd>
<dt>-b dev_sector_size</dt>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the image format is used (if it exists) or 512-bytes is assumed.</dd>
<dt><code>-v</code></dt>
<dd> Turn on verbose mode, output to stderr.</dd>
<dt><code>-V</code></dt>
<dd> Display Version.</dd>
<dt>image [images]</dt>
<dd> The disk or partition image to read, whose format is given with &#8216;-i&#8217;. Multiple image file names can be given if the image is split into multiple segments. If only one image file is given, and its name is the first in a sequence (e.g., as indicated by ending in &#8216;.001&#8217;), subsequent image segments will be included automatically.</dd>
<dt><i>start-stop</i></dt>
<dd> Examine the specified inode number or number range.</dd></dl>
<p> Fine controls:</p>
<dl>
<dt><code>-a</code></dt>
<dd> List only allocated inodes: these belong to files with at least one directory entry in the file system, and to removed files that are still open or executing.</dd>
<dt><code>-A</code></dt>
<dd> List only unallocated inodes: these belong to files that no longer exist.</dd>
<dt><code>-l</code></dt>
<dd> List only inodes with at least one hard link. These belong to files with at least one directory entry in the file system.</dd>
<dt><code>-L</code></dt>
<dd> List only inodes without any hard links. These belong to files that no longer exist, and to removed files that are still open or executing.</dd>
<dt><code>-z</code></dt>
<dd> List only inodes that were likely to have not been used.</dd>
<dt><code>-Z</code></dt>
<dd> List only inodes that were likely to be used.</dd></dl>
<p> The output format is in time machine format. The output begins with a two-line header that describes the data origin, and is followed by a one-line header that lists the names of the data attributes that make up the remainder of the output:</p>
<dl>
<dt>st_ino</dt>
<dd> The inode number.</dd>
<dt>st_alloc</dt>
<dd> Allocation status: `a&#8217; for allocated inode, `f&#8217; for free inode.</dd>
<dt>st_uid</dt>
<dd> Owner user ID.</dd>
<dt>st_gid</dt>
<dd> Owner group ID.</dd>
<dt>st_mtime</dt>
<dd> UNIX time (seconds) of last file modification.</dd>
<dt>st_atime</dt>
<dd> UNIX time (seconds) of last file access.</dd>
<dt>st_ctime</dt>
<dd> UNIX time (seconds) of last inode status change.</dd>
<dt>st_dtime</dt>
<dd> UNIX time (seconds) of file deletion (LINUX only).</dd>
<dt>st_mode</dt>
<dd> File type and permissions (octal).</dd>
<dt>st_nlink</dt>
<dd> Number of hard links.</dd>
<dt>st_size</dt>
<dd> File size in bytes.</dd>
<dt>st_block0,st_block1</dt>
<dd> The first two entries in the direct block address list.</dd></dl>
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
