---
title: "fsck-cramfs(8)"
name: "fsck-cramfs"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-cramfs/"
description: "fsck.cramfs – fsck compressed ROM file system"
---

<p>fsck.cramfs &#8211; fsck compressed ROM file system</p>
<h2>Synopsis</h2>
<p><code>fsck.cramfs</code> [options] <i>file</i></p>
<h2>Description</h2>
<p><code>fsck.cramfs</code> is used to check the cramfs file system.</p>
<h2>Options</h2>
<p><code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Enable verbose messaging.</dl>
<p> <code>-b</code>, <code>&#8211;blocksize</code> <i>blocksize</i></p>
<dl>
<dd>Use this blocksize, defaults to page size. Must be equal to what was set at creation time. Only used for <code>&#8211;extract</code>.</dl>
<p> <code>&#8211;extract</code>[=<i>directory</i>]</p>
<dl>
<dd>Test to uncompress the whole file system. Optionally extract contents of the <i>file</i> to <i>directory</i>.</dl>
<p> <code>-a</code></p>
<dl>
<dd>This option is silently ignored.</dl>
<p> <code>-y</code></p>
<dl>
<dd>This option is silently ignored.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Exit Status</h2>
<p><code>0</code></p>
<dl>
<dd>success</dl>
<p> <code>4</code></p>
<dl>
<dd>file system was left uncorrected</dl>
<p> <code>8</code></p>
<dl>
<dd>operation error, such as unable to allocate memory</dl>
<p> <code>16</code></p>
<dl>
<dd>usage information was printed</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-mkfs-cramfs/">mkfs.cramfs</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>fsck.cramfs</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
