---
title: "hd(4)"
name: "hd"
section: "4"
letter: "h"
url: "/docs/linux/man/4-hd/"
description: "hd – MFM/IDE hard disk devices"
---

<p>hd &#8211; MFM/IDE hard disk devices</p>
<h2>Description</h2>
<p>The <code>hd*</code> devices are block devices to access MFM/IDE hard disk drives in raw mode. The master drive on the primary IDE controller (major device number 3) is <code>hda</code>; the slave drive is <code>hdb</code>. The master drive of the second controller (major device number 22) is <code>hdc</code> and the slave is <code>hdd</code>. </p>
<p> General IDE block device names have the form <code>hd</code><i>X</i>, or <code>hd</code><i>XP</i>, where <i>X</i> is a letter denoting the physical drive, and <i>P</i> is a number denoting the partition on that physical drive. The first form, <code>hd</code><i>X</i>, is used to address the whole drive. Partition numbers are assigned in the order the partitions are discovered, and only nonempty, nonextended partitions get a number. However, partition numbers 1-4 are given to the four partitions described in the MBR (the &quot;primary&quot; partitions), regardless of whether they are unused or extended. Thus, the first logical partition will be <code>hd</code><i>X</i><code>5</code>. Both DOS-type partitioning and BSD-disklabel partitioning are supported. You can have at most 63 partitions on an IDE disk. </p>
<p> For example, <i>/dev/hda</i> refers to all of the first IDE drive in the system; and <i>/dev/hdb3</i> refers to the third DOS &quot;primary&quot; partition on the second one. </p>
<p> They are typically created by: </p>
<p> mknod -m 660 /dev/hda b 3 0 mknod -m 660 /dev/hda1 b 3 1 mknod -m 660 /dev/hda2 b 3 2 &#8230; mknod -m 660 /dev/hda8 b 3 8 mknod -m 660 /dev/hdb b 3 64 mknod -m 660 /dev/hdb1 b 3 65 mknod -m 660 /dev/hdb2 b 3 66 &#8230; mknod -m 660 /dev/hdb8 b 3 72 chown root:disk /dev/hd*</p>
<h2>Files</h2>
<p><i>/dev/hd*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/4-sd/">sd</a></code>(4), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
