---
title: "unsquashfs(1)"
name: "unsquashfs"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unsquashfs/"
description: "unsquashfs – tool to uncompress squashfs filesystems"
---

<h2 class="name">NAME</h2>
<p> unsquashfs &#8211; tool to uncompress squashfs filesystems</p>
<h2>SYNOPSIS</h2>
<p> <code>unsquashfs</code> [<i>OPTIONS</i>] <i>FILESYSTEM</i> [<i>directories or files to extract</i>] </p>
<h2>DESCRIPTION</h2>
<p> Squashfs is a highly compressed read-only filesystem for Linux. It uses zlib compression to compress both files, inodes and directories. Inodes in the system are very small and all blocks are packed to minimize data overhead. Block sizes greater than 4K are supported up to a maximum of 64K. </p>
<p> Squashfs is intended for general read-only filesystem use, for archival use (i.e. in cases where a .tar.gz file may be used), and in constrained block device/memory systems (e.g. embedded systems) where low overhead is needed. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-v, -version</dt>
<dd> print version, licence and copyright information.</dd>
<dt>-d <i>PATHNAME</i>, -dest <i>PATHNAME</i></dt>
<dd> unsquash to <i>PATHNAME</i>, default &quot;squashfs-root&quot;.</dd>
<dt>-n, -no-progress</dt>
<dd> don&#8217;t display the progress bar.</dd>
<dt>-no, -no-xattrs</dt>
<dd> don&#8217;t extract xattrs in file system.</dd>
<dt>-x, -xattrs</dt>
<dd> extract xattrs in file system (default).</dd>
<dt>-p <i>NUMBER</i>, -processors <i>NUMBER</i></dt>
<dd> use <i>NUMBER</i> processors. By default will use number of processors available.</dd>
<dt>-i, -info</dt>
<dd> print files as they are unsquashed.</dd>
<dt>-li, -linfo</dt>
<dd> print files as they are unsquashed with file attributes (like ls -l output).</dd>
<dt>-l, -ls</dt>
<dd> list filesystem, but don&#8217;t unsquash.</dd>
<dt>-ll, -lls</dt>
<dd> list filesystem with file attributes (like ls -l output), but don&#8217;t unsquash.</dd>
<dt>-nl, -nls</dt>
<dd> list filesystem with file attributes (like ls -n output), but don&#8217;t unsquash.</dd>
<dt>-f, -force</dt>
<dd> if file already exists then overwrite.</dd>
<dt>-s, -stat</dt>
<dd> display filesystem superblock information.</dd>
<dt>-e <i>EXTRACT_FILE</i>, -ef <i>EXTRACT_FILE</i></dt>
<dd> list of directories or files to extract. One per line.</dd>
<dt>-da <i>SIZE</i>, -data-queue <i>SIZE</i></dt>
<dd> Set data queue to <i>SIZE</i> Mbytes. Default 256 Mbytes.</dd>
<dt>-fr <i>SIZE</i>, -frag-queue <i>SIZE</i></dt>
<dd> Set fragment queue to <i>SIZE</i> Mbytes. Default 256 Mbytes.</dd>
<dt>-r, -regex</dt>
<dd> treat extract names as POSIX regular expressions rather than use the default shell wildcard expansion (globbing). </dd>
</dl>
<h3>Decompressors available</h3>
<dl>
<dt>gzip</dt>
<dd>
</dd><dt>lzo</dt>
<dd>
</dd><dt>xz</dt>
<dd>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mksquashfs/">mksquashfs</a>(1) </p>
<h2>HOMEPAGE</h2>
<p> More information about unsquashfs and the squashfs filesystem can be found at &lt;<i><a rel="nofollow" href="http://squashfs.sourceforge.net/">http://squashfs.sourceforge.net/</a></i>&gt;. </p>
<h2>AUTHOR</h2>
<p> squashfs was written by Phillip Lougher &lt;<i>phillip [at] squashfs.org.uk</i>&gt;. </p>
<p> This manual page was written by Daniel Baumann &lt;<i>mail [at] daniel-baumann.ch</i>&gt;. </p>
