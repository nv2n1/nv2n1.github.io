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
<dt><code>-B</code></p>
<dd>Force the use of the older FIBMAP ioctl instead of the FIEMAP ioctl for testing purposes.</p>
<dt><code>-b</code><i>blocksize</i></p>
<dd>Use <i>blocksize</i> in bytes, or with [KMG] suffix, up to 1GB for output instead of the file system blocksize. For compatibility with earlier versions of <code>filefrag</code>, if <i>blocksize</i> is unspecified it defaults to 1024 bytes. Since <i>blocksize</i> is an optional argument, it must be added without any space after <code>-b</code>.</p>
<dt><code>-e</code></p>
<dd>Print output in extent format, even for block-mapped files.</p>
<dt><code>-E</code></p>
<dd>Display the contents of ext4&#8217;s extent status cache. This feature is not supported on all kernels, and is only supported on ext4 file systems.</p>
<dt><code>-k</code></p>
<dd>Use 1024-byte blocksize for output (identical to &#8216;-b1024&#8217;).</p>
<dt><code>-P</code></p>
<dd>Pre-load the ext4 extent status cache for the file. This is not supported on all kernels, and is only supported on ext4 file systems.</p>
<dt><code>-s</code></p>
<dd>Sync the file before requesting the mapping.</p>
<dt><code>-v</code></p>
<dd>Be verbose when checking for file fragmentation.</p>
<dt><code>-V</code></p>
<dd>Print version number of program and library. If given twice, also print the FIEMAP flags that are understood by the current version.</p>
<dt><code>-x</code></p>
<dd>Display mapping of extended attributes.</p>
<dt><code>-X</code></p>
<dd>Display extent block numbers in hexadecimal format.</dl>
<h2>Author</h2>
<p><code>filefrag</code> was written by Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;.</p>
