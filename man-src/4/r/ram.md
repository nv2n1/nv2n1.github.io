---
title: "ram(4)"
name: "ram"
section: "4"
letter: "r"
url: "/docs/linux/man/4-ram/"
description: "ram – ram disk device"
---

<p>ram &#8211; ram disk device</p>
<h2>Description</h2>
<p>The <i>ram</i> device is a block device to access the ram disk in raw mode. </p>
<p> It is typically created by: </p>
<p> mknod -m 660 /dev/ram b 1 1 chown root:disk /dev/ram</p>
<h2>Files</h2>
<p><i>/dev/ram</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
