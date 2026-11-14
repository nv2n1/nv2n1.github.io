---
title: "ttys(4)"
name: "ttys"
section: "4"
letter: "t"
url: "/docs/linux/man/4-ttys/"
description: "ttyS – serial terminal lines"
---

<p>ttyS &#8211; serial terminal lines</p>
<h2>Description</h2>
<p><code>ttyS[0-3]</code> are character devices for the serial terminal lines. </p>
<p> They are typically created by: </p>
<p> mknod -m 660 /dev/ttyS0 c 4 64 # base address 0x3f8 mknod -m 660 /dev/ttyS1 c 4 65 # base address 0x2f8 mknod -m 660 /dev/ttyS2 c 4 66 # base address 0x3e8 mknod -m 660 /dev/ttyS3 c 4 67 # base address 0x2e8 chown root:tty /dev/ttyS[0-3]</p>
<h2>Files</h2>
<p><i>/dev/ttyS[0-3]</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4), <code><a href="/docs/linux/man/8-agetty/">agetty</a></code>(8), <code><a href="/docs/linux/man/8-mingetty/">mingetty</a></code>(8), <code><a href="/docs/linux/man/8-setserial/">setserial</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
