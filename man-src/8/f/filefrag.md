---
title: "filefrag(8)"
name: "filefrag"
section: "8"
letter: "f"
url: "/docs/linux/man/8-filefrag/"
description: "filefrag – report on file fragmentation"
---

<p>filefrag &#8211; report on file fragmentation</p>
<h2>Synopsis</h2>
<p><code>filefrag</code> [ <code>-b</code><i>blocksize</i> ] [ <code>-BeEkPsvVxX</code> ] [ <i>files&#8230;</i> ]</p>
<h2>Description</h2>
<p><code>filefrag</code> reports on how badly fragmented a particular file might be. It makes allowances for indirect blocks for ext2 and ext3 file systems, but can be used on files for any file system. </p>
<p> The <code>filefrag</code> program initially attempts to get the extent information using FIEMAP ioctl which is more efficient and faster. If FIEMAP is not supported then filefrag will fall back to using FIBMAP.</p>
<h2>Options</h2>
<dl>
<dt><code>-B</code></dt>
<dd>Force the use of the older FIBMAP ioctl instead of the FIEMAP ioctl for testing purposes.</dd>
<dt><code>-b</code><i>blocksize</i></dt>
<dd>Use <i>blocksize</i> in bytes, or with [KMG] suffix, up to 1GB for output instead of the file system blocksize. For compatibility with earlier versions of <code>filefrag</code>, if <i>blocksize</i> is unspecified it defaults to 1024 bytes. Since <i>blocksize</i> is an optional argument, it must be added without any space after <code>-b</code>.</dd>
<dt><code>-e</code></dt>
<dd>Print output in extent format, even for block-mapped files.</dd>
<dt><code>-E</code></dt>
<dd>Display the contents of ext4&#8217;s extent status cache. This feature is not supported on all kernels, and is only supported on ext4 file systems.</dd>
<dt><code>-k</code></dt>
<dd>Use 1024-byte blocksize for output (identical to &#8216;-b1024&#8217;).</dd>
<dt><code>-P</code></dt>
<dd>Pre-load the ext4 extent status cache for the file. This is not supported on all kernels, and is only supported on ext4 file systems.</dd>
<dt><code>-s</code></dt>
<dd>Sync the file before requesting the mapping.</dd>
<dt><code>-v</code></dt>
<dd>Be verbose when checking for file fragmentation.</dd>
<dt><code>-V</code></dt>
<dd>Print version number of program and library. If given twice, also print the FIEMAP flags that are understood by the current version.</dd>
<dt><code>-x</code></dt>
<dd>Display mapping of extended attributes.</dd>
<dt><code>-X</code></dt>
<dd>Display extent block numbers in hexadecimal format.</dd></dl>
<h2>Author</h2>
<p><code>filefrag</code> was written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;.</p>
