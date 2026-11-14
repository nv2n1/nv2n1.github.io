---
title: "blkdiscard(8)"
name: "blkdiscard"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkdiscard/"
description: "blkdiscard – discard sectors on a device"
---

<p>blkdiscard &#8211; discard sectors on a device</p>
<h2>Synopsis</h2>
<p><code>blkdiscard</code> [options] [<code>-o</code> <i>offset</i>] [<code>-l</code> <i>length</i>] <i>device</i></p>
<h2>Description</h2>
<p><code>blkdiscard</code> is used to discard device sectors. This is useful for solid-state drivers (SSDs) and thinly-provisioned storage. Unlike <code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8), this command is used directly on the block device. </p>
<p> By default, <code>blkdiscard</code> will discard all blocks on the device. Options may be used to modify this behavior based on range or size, as explained below. </p>
<p> The <i>device</i> argument is the pathname of the block device. </p>
<p> <code>WARNING: All data in the discarded region on the device will be lost!</code></p>
<h2>Options</h2>
<p>The <i>offset</i> and <i>length</i> arguments may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, TiB, PiB, EiB, ZiB and YiB (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, TB, PB, EB, ZB and YB. </p>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dd>Disable all checking. Since v2.36 the block device is open in exclusive mode (O_EXCL) by default to avoid collision with mounted filesystem or another kernel subsystem. The <code>&#8211;force</code> option disables the exclusive access mode.</dl>
<p> <code>-o</code>, <code>&#8211;offset</code> <i>offset</i></p>
<dl>
<dd>Byte offset into the device from which to start discarding. The provided value must be aligned to the device sector size. The default value is zero.</dl>
<p> <code>-l</code>, <code>&#8211;length</code> <i>length</i></p>
<dl>
<dd>The number of bytes to discard (counting from the starting point). The provided value must be aligned to the device sector size. If the specified value extends past the end of the device, <code>blkdiscard</code> will stop at the device size boundary. The default value extends to the end of the device.</dl>
<p> <code>-p</code>, <code>&#8211;step</code> <i>length</i></p>
<dl>
<dd>The number of bytes to discard within one iteration. The default is to discard all by one ioctl call.</dl>
<p> <code>-s</code>, <code>&#8211;secure</code></p>
<dl>
<dd>Perform a secure discard. A secure discard is the same as a regular discard except that all copies of the discarded blocks that were possibly created by garbage collection must also be erased. This requires support from the device.</dl>
<p> <code>-z</code>, <code>&#8211;zeroout</code></p>
<dl>
<dd>Zero-fill rather than discard.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Display the aligned values of <i>offset</i> and <i>length</i>. If the <code>&#8211;step</code> option is specified, it prints the discard progress every second.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fstrim/">fstrim</a></code>(8)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>blkdiscard</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
