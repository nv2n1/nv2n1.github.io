---
title: "mkfs-bfs(8)"
name: "mkfs-bfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-bfs/"
description: "mkfs.bfs – make an SCO bfs filesystem"
---

<p>mkfs.bfs &#8211; make an SCO bfs filesystem</p>
<h2>Synopsis</h2>
<p><code>mkfs.bfs</code> [options] <i>device</i> [<i>block-count</i>]</p>
<h2>Description</h2>
<p><code>mkfs.bfs</code> creates an SCO bfs filesystem on a block device (usually a disk partition or a file accessed via the loop device). </p>
<p> The <i>block-count</i> parameter is the desired size of the filesystem, in blocks. If nothing is specified, the entire partition will be used.</p>
<h2>Options</h2>
<p><code>-N</code>, <code>&#8211;inodes</code> <i>number</i></p>
<dl>
<dd>Specify the desired <i>number</i> of inodes (at most 512). If nothing is specified, some default number in the range 48-512 is picked depending on the size of the partition.</dl>
<p> <code>-V</code>, <code>&#8211;vname</code> <i>label</i></p>
<dl>
<dd>Specify the volume <i>label</i>. I have no idea if/where this is used.</dl>
<p> <code>-F</code>, <code>&#8211;fname</code> <i>name</i></p>
<dl>
<dd>Specify the filesystem <i>name</i>. I have no idea if/where this is used.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Explain what is being done.</dl>
<p> <code>-c</code></p>
<dl>
<dd>This option is silently ignored.</dl>
<p> <code>-l</code></p>
<dl>
<dd>This option is silently ignored.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit. Option <code>-V</code> only works as <code>&#8211;version</code> when it is the only option.</dl>
<h2>Exit Status</h2>
<p>The exit status returned by <code>mkfs.bfs</code> is 0 when all went well, and 1 when something went wrong.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs/">mkfs</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mkfs.bfs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
