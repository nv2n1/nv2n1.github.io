---
title: "resizepart(8)"
name: "resizepart"
section: "8"
letter: "r"
url: "/docs/linux/man/8-resizepart/"
description: "resizepart – tell the kernel about the new size of a partition"
---

<p>resizepart &#8211; tell the kernel about the new size of a partition</p>
<h2>Synopsis</h2>
<p><code>resizepart</code> <i>device partition length</i></p>
<h2>Description</h2>
<p><code>resizepart</code> tells the Linux kernel about the new size of the specified partition. The command is a simple wrapper around the &quot;resize partition&quot; ioctl. </p>
<p> This command doesn&#8217;t manipulate partitions on a block device.</p>
<h2>Parameters</h2>
<p><i>device</i></p>
<dl>
<dd>The disk device.</dl>
<p> <i>partition</i></p>
<dl>
<dd>The partition number.</dl>
<p> <i>length</i></p>
<dl>
<dd>The new length of the partition (in 512-byte sectors).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-addpart/">addpart</a></code>(8), <code><a href="/docs/linux/man/8-delpart/">delpart</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>resizepart</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
