---
title: "dumpseg(8)"
name: "dumpseg"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dumpseg/"
description: "dumpseg – print segment information of NILFS2"
---

<p>dumpseg &#8211; print segment information of NILFS2</p>
<h2>Synopsis</h2>
<p><code>dumpseg</code> [<i>device</i>] <i>segment-number</i> &#8230; </p>
<p> <code>dumpseg -h</code></p>
<h2>Description</h2>
<p>The <code>dumpseg</code> program is an analysis tool for on-disk logs of a NILFS2 file system found in <i>device</i>. It displays the configuration of every log stored in the segments specified by one or more <i>segment-numbers</i>. The term segment here means a contiguous lump of disk blocks giving an allocation unit of NILFS2 disk space. When <i>device</i> is omitted, it tries to find an active NILFS2 file system from <i>/proc/mounts</i>. </p>
<p> <code>dumpseg</code> is a tool for debugging rather than administration. To list a summary of segments, <code><a href="/docs/linux/man/1-lssu/">lssu</a></code>(1) is available instead.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>Display help message and exit.</dd></dl>
<h2>Field Description</h2>
<p><code>dumpseg</code> shows the configuration of each log with the following fields, where each field is printed in the style of &#8220;<i>field-name</i> <code>=</code> <i>value</i>&#8221;.</p>
<dl>
<dt><code>creation time</code></dt>
<dd>Creation date and time of the log.</dd>
<dt><code>nfinfo</code></dt>
<dd>Number of file information summaries.</dd>
<dt><code>finfo</code></dt>
<dd>File information summary. This information starts with the following fields:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ino</code></dt>
<dd>Inode number of the file.</dd>
<dt><code>cno</code></dt>
<dd>Number of the checkpoint that the blocks included in the file belong to. For normal writings, this is equal to the latest checkpoint number. For the writings involved in garbage collection, this indicates a past checkpoint number.</dd>
<dt><code>nblocks</code></dt>
<dd>Number of blocks of the file written in the log. This number is a sum of the number of data blocks and B-tree node blocks. The contents of these blocks are written serially in the payload part of the log. Only modified or newly created blocks are written to each log.</dd>
<dt><code>ndatblk</code></dt>
<dd>Number of data blocks of the file written in the log.</dd></dl>
</dl>
<dd>Then, for each update block in the file, the following information will follow these headings.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>vblocknr</code></dt>
<dd>Virtual block number. Not printed for data blocks of the Disk Address Translation file (DAT file).</dd>
<dt><code>blkoff</code></dt>
<dd>Block offset number. Not printed for B-tree node blocks except for the DAT file.</dd>
<dt><code>level</code></dt>
<dd>Level of B-tree node block. Printed only for the DAT file.</dd>
<dt><code>blocknr</code></dt>
<dd>Block address on the <i>device</i>. This is not an actual field in the summary but is calculated from the disk address of each log.</dd></dl>
</dl>
</dl>
<h2>Author</h2>
<p>Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>Availability</h2>
<p><code>dumpseg</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/1-lssu/">lssu</a></code>(1). </p>
