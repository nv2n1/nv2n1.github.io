---
title: "termio(7)"
name: "termio"
section: "7"
letter: "t"
url: "/docs/linux/man/7-termio/"
description: "termio – System V terminal driver interface"
---

<p>termio &#8211; System V terminal driver interface</p>
<h2>Description</h2>
<p><code>termio</code> is the name of the old System V terminal driver interface. This interface defined a <i>termio</i> structure used to store terminal settings, and a range of <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations to get and set terminal attributes. </p>
<p> The <code>termio</code> interface is now obsolete: POSIX.1-1990 standardized a modified version of this interface, under the name <code>termios</code>. The POSIX.1 data structure differs slightly from the System V version, and POSIX.1 defined a suite of functions to replace the various <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operations that existed in System V. (This was done because <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) was unstandardized, and its variadic third argument does not allow argument type checking.) </p>
<p> If you&#8217;re looking for a page called &quot;termio&quot;, then you can probably find most of the information that you seek in either <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) or <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-reset/">reset</a></code>(1), <code><a href="/docs/linux/man/1-setterm/">setterm</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
