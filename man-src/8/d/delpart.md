---
title: "delpart(8)"
name: "delpart"
section: "8"
letter: "d"
url: "/docs/linux/man/8-delpart/"
description: "delpart – tell the kernel to forget about a partition"
---

<p>delpart &#8211; tell the kernel to forget about a partition</p>
<h2>Synopsis</h2>
<p><code>delpart</code> <i>device partition</i></p>
<h2>Description</h2>
<p><code>delpart</code> asks the Linux kernel to forget about the specified <i>partition</i> (a number) on the specified <i>device</i>. The command is a simple wrapper around the &quot;del partition&quot; ioctl. </p>
<p> This command doesn&#8217;t manipulate partitions on a block device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-addpart/">addpart</a></code>(8), <code><a href="/docs/linux/man/8-fdisk/">fdisk</a></code>(8), <code><a href="/docs/linux/man/8-parted/">parted</a></code>(8), <code><a href="/docs/linux/man/8-partprobe/">partprobe</a></code>(8), <code><a href="/docs/linux/man/8-partx/">partx</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>delpart</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
