---
title: "addpart(8)"
name: "addpart"
section: "8"
letter: "a"
url: "/docs/linux/man/8-addpart/"
description: "addpart – tell the kernel about the existence of a partition"
---

<p>addpart &#8211; tell the kernel about the existence of a partition</p>
<h2>Synopsis</h2>
<p><code>addpart</code> <i>device partition start length</i></p>
<h2>Description</h2>
<p><code>addpart</code> tells the Linux kernel about the existence of the specified partition. The command is a simple wrapper around the &quot;add partition&quot; ioctl. </p>
<p> This command doesn&#8217;t manipulate partitions on a block device.</p>
<h2>Parameters</h2>
<p><i>device</i></p>
<dl>
<dd>The disk device.</dl>
<p> <i>partition</i></p>
<dl>
<dd>The partition number.</dl>
<p> <i>start</i></p>
<dl>
<dd>The beginning of the partition (in 512-byte sectors).</dl>
<p> <i>length</i></p>
<dl>
<dd>The length of the partition (in 512-byte sectors).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-delpart/">delpart</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>addpart</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
