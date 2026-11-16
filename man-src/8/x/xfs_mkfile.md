---
title: "xfs_mkfile(8)"
name: "xfs_mkfile"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_mkfile/"
description: "xfs_mkfile – create an XFS file"
---

<p>xfs_mkfile &#8211; create an XFS file</p>
<h2>Synopsis</h2>
<p><code>xfs_mkfile</code> [ <code>-v</code> ] [ <code>-n</code> ] [ <code>-p</code> ] <i>size</i>[<code>k</code>|<code>b</code>|<code>m</code>|<code>g</code>] <i>filename</i> &#8230;<br />
 <code>xfs_mkfile -V</code></p>
<h2>Description</h2>
<p><code>xfs_mkfile</code> creates one or more files. The file is padded with zeroes by default. The default size is in bytes, but it can be flagged as kilobytes, blocks, megabytes, or gigabytes with the <code>k</code>, <code>b</code>, <code>m</code>, or <code>g</code> suffixes, respectively.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></dt>
<dd>Verbose. Report the names and sizes of created files.</dd>
<dt><code>-n</code></dt>
<dd>No bytes. Create a holey file &#8211; that is, do not write out any data, just seek to end of file and write a block.</dd>
<dt><code>-p</code></dt>
<dd>Preallocate. The file is preallocated, then overwritten with zeroes, then truncated to the desired size.</dd>
<dt><code>-V</code></dt>
<dd>Prints the version number and exits. </dd>
</dl>
