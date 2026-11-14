---
title: "mkfs-cramfs(8)"
name: "mkfs-cramfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkfs-cramfs/"
description: "mkfs.cramfs – make compressed ROM file system"
---

<p>mkfs.cramfs &#8211; make compressed ROM file system</p>
<h2>Synopsis</h2>
<p><code>mkfs.cramfs</code> [options] <i>directory file</i></p>
<h2>Description</h2>
<p>Files on cramfs file systems are zlib-compressed one page at a time to allow random read access. The metadata is not compressed, but is expressed in a terse representation that is more space-efficient than conventional file systems. </p>
<p> The file system is intentionally read-only to simplify its design; random write access for compressed files is difficult to implement. cramfs ships with a utility (<code><a href="/docs/linux/man/8-mkcramfs/">mkcramfs</a></code>(8)) to pack files into new cramfs images. </p>
<p> File sizes are limited to less than 16 MB. </p>
<p> Maximum file system size is a little under 272 MB. (The last file on the file system must begin before the 256 MB block, but can extend past it.)</p>
<h2>Arguments</h2>
<p>The <i>directory</i> is simply the root of the directory tree that we want to generate a compressed filesystem out of. </p>
<p> The <i>file</i> will contain the cram file system, which later can be mounted.</p>
<h2>Options</h2>
<p><code>-v</code></p>
<dl>
<dd>Enable verbose messaging.</dl>
<p> <code>-E</code></p>
<dl>
<dd>Treat all warnings as errors, which are reflected as command exit status.</dl>
<p> <code>-b</code> <i>blocksize</i></p>
<dl>
<dd>Use defined block size, which has to be divisible by page size.</dl>
<p> <code>-e</code> <i>edition</i></p>
<dl>
<dd>Use defined file system edition number in superblock.</dl>
<p> <code>-N</code> <i>big, little, host</i></p>
<dl>
<dd>Use defined endianness. Value defaults to <i>host</i>.</dl>
<p> <code>-i</code> <i>file</i></p>
<dl>
<dd>Insert a <i>file</i> to cramfs file system.</dl>
<p> <code>-n</code> <i>name</i></p>
<dl>
<dd>Set name of the cramfs file system.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Pad by 512 bytes for boot code.</dl>
<p> <code>-s</code></p>
<dl>
<dd>This option is ignored. Originally the <code>-s</code> turned on directory entry sorting.</dl>
<p> <code>-z</code></p>
<dl>
<dd>Make explicit holes.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>8</code></p>
<dl>
<dd>operation error, such as unable to allocate memory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck-cramfs/">fsck.cramfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>mkfs.cramfs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
