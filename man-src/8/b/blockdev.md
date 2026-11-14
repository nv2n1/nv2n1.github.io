---
title: "blockdev(8)"
name: "blockdev"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blockdev/"
description: "blockdev – call block device ioctls from the command line"
---

<p>blockdev &#8211; call block device ioctls from the command line</p>
<h2>Synopsis</h2>
<p><code>blockdev</code> [<code>-q</code>] [<code>-v</code>] <i>command</i> [<i>command</i>&#8230;] <i>device</i> [<i>device</i>&#8230;] </p>
<p> <code>blockdev</code> <code>&#8211;report</code> [<i>device</i>&#8230;] </p>
<p> <code>blockdev</code> <code>-h</code>|<code>-V</code></p>
<h2>Description</h2>
<p>The utility <code>blockdev</code> allows one to call block device ioctls from the command line.</p>
<h2>Options</h2>
<p><code>-q</code></p>
<dl>
<dd>Be quiet.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Be verbose.</dl>
<p> <code>&#8211;report</code></p>
<dl>
<dd>Print a report for the specified device. It is possible to give multiple devices. If none is given, all devices which appear in <i>/proc/partitions</i> are shown. Note that the partition StartSec is in 512-byte sectors.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print version and exit.</dl>
<h2>Commands</h2>
<p>It is possible to give multiple devices and multiple commands. </p>
<p> <code>&#8211;flushbufs</code></p>
<dl>
<dd>Flush buffers.</dl>
<p> <code>&#8211;getalignoff</code></p>
<dl>
<dd>Get alignment offset.</dl>
<p> <code>&#8211;getbsz</code></p>
<dl>
<dd>Print the blocksize in bytes. This size does not describe device topology. It&#8217;s the size used internally by the kernel and it may be modified (for example) by filesystem driver on mount.</dl>
<p> <code>&#8211;getdiscardzeroes</code></p>
<dl>
<dd>Get discard zeroes support status.</dl>
<p> <code>&#8211;getfra</code></p>
<dl>
<dd>Get filesystem readahead in 512-byte sectors.</dl>
<p> <code>&#8211;getiomin</code></p>
<dl>
<dd>Get minimum I/O size.</dl>
<p> <code>&#8211;getioopt</code></p>
<dl>
<dd>Get optimal I/O size.</dl>
<p> <code>&#8211;getmaxsect</code></p>
<dl>
<dd>Get max sectors per request.</dl>
<p> <code>&#8211;getpbsz</code></p>
<dl>
<dd>Get physical block (sector) size.</dl>
<p> <code>&#8211;getra</code></p>
<dl>
<dd>Print readahead (in 512-byte sectors).</dl>
<p> <code>&#8211;getro</code></p>
<dl>
<dd>Get read-only. Print 1 if the device is read-only, 0 otherwise.</dl>
<p> <code>&#8211;getsize64</code></p>
<dl>
<dd>Print device size in bytes.</dl>
<p> <code>&#8211;getsize</code></p>
<dl>
<dd>Print device size (32-bit!) in sectors. Deprecated in favor of the <code>&#8211;getsz</code> option.</dl>
<p> <code>&#8211;getss</code></p>
<dl>
<dd>Print logical sector size in bytes &#8211; usually 512.</dl>
<p> <code>&#8211;getsz</code></p>
<dl>
<dd>Get size in 512-byte sectors.</dl>
<p> <code>&#8211;rereadpt</code></p>
<dl>
<dd>Reread partition table</dl>
<p> <code>&#8211;setbsz</code> <i>bytes</i></p>
<dl>
<dd>Set blocksize. Note that the block size is specific to the current file descriptor opening the block device, so the change of block size only persists for as long as <code>blockdev</code> has the device open, and is lost once <code>blockdev</code> exits.</dl>
<p> <code>&#8211;setfra</code> <i>sectors</i></p>
<dl>
<dd>Set filesystem readahead (same as <code>&#8211;setra</code> on 2.6 kernels).</dl>
<p> <code>&#8211;setra</code> <i>sectors</i></p>
<dl>
<dd>Set readahead (in 512-byte sectors).</dl>
<p> <code>&#8211;setro</code></p>
<dl>
<dd>Set read-only. The currently active access to the device may not be affected by the change. For example, a filesystem already mounted in read-write mode will not be affected. The change applies after remount.</dl>
<p> <code>&#8211;setrw</code></p>
<dl>
<dd>Set read-write.</dl>
<h2>Authors</h2>
<p><code>blockdev</code> was written by Andries E. Brouwer and rewritten by Karel Zak.</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>blockdev</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
