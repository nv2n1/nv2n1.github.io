---
title: "ioctl(2)"
name: "ioctl"
section: "2"
letter: "i"
url: "/docs/linux/man/2-ioctl/"
description: "ioctl – control device"
---

<h2 class="name">NAME</h2>
<p> ioctl &#8211; control device </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ioctl.h&gt;</code> </p>
<p> <code>int ioctl(int </code><i>fd</i><code>, unsigned long </code><i>request</i><code>, &#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ioctl</code>() system call manipulates the underlying device parameters of special files. In particular, many operating characteristics of character special files (e.g., terminals) may be controlled with <code>ioctl</code>() requests. The argument <i>fd</i> must be an open file descriptor. </p>
<p> The second argument is a device-dependent request code. The third argument is an untyped pointer to memory. It&#8217;s traditionally <code>char *</code><i>argp</i> (from the days before <code>void *</code> was valid C), and will be so named for this discussion. </p>
<p> An <code>ioctl</code>() <i>request</i> has encoded in it whether the argument is an <i>in</i> parameter or <i>out</i> parameter, and the size of the argument <i>argp</i> in bytes. Macros and defines used in specifying an <code>ioctl</code>() <i>request</i> are located in the file <i>&lt;sys/ioctl.h&gt;</i>. See NOTES.</p>
<h2>RETURN VALUE</h2>
<p> Usually, on success zero is returned. A few <code>ioctl</code>() requests use the return value as an output parameter and return a nonnegative value on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>argp</i> references an inaccessible memory area.</p>
<dt><code>EINVAL</code></p>
<dd> <i>request</i> or <i>argp</i> is not valid.</p>
<dt><code>ENOTTY</code></p>
<dd> <i>fd</i> is not associated with a character special device.</p>
<dt><code>ENOTTY</code></p>
<dd> The specified request does not apply to the kind of object that the file descriptor <i>fd</i> references.</dl>
<h2>CONFORMING TO</h2>
<p> No single standard. Arguments, returns, and semantics of <code>ioctl</code>() vary according to the device driver in question (the call is used as a catch-all for operations that don&#8217;t cleanly fit the UNIX stream I/O model). </p>
<p> The <code>ioctl</code>() system call appeared in Version 7 AT&amp;T UNIX.</p>
<h2>NOTES</h2>
<p> In order to use this call, one needs an open file descriptor. Often the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) call has unwanted side effects, that can be avoided under Linux by giving it the <code>O_NONBLOCK</code> flag.</p>
<h3>ioctl structure</h3>
<p> Ioctl command values are 32-bit constants. In principle these constants are completely arbitrary, but people have tried to build some structure into them. </p>
<p> The old Linux situation was that of mostly 16-bit constants, where the last byte is a serial number, and the preceding byte(s) give a type indicating the driver. Sometimes the major number was used: 0x03 for the <code>HDIO_*</code> ioctls, 0x06 for the <code>LP*</code> ioctls. And sometimes one or more ASCII letters were used. For example, <code>TCGETS</code> has value 0x00005401, with 0x54 = &#8216;T&#8217; indicating the terminal driver, and <code>CYGETTIMEOUT</code> has value 0x00435906, with 0x43 0x59 = &#8216;C&#8217; &#8216;Y&#8217; indicating the cyclades driver. </p>
<p> Later (0.98p5) some more information was built into the number. One has 2 direction bits (00: none, 01: write, 10: read, 11: read/write) followed by 14 size bits (giving the size of the argument), followed by an 8-bit type (collecting the ioctls in groups for a common purpose or a common driver), and an 8-bit serial number. </p>
<p> The macros describing this structure live in <i>&lt;asm/ioctl.h&gt;</i> and are <code>_IO(type,nr)</code> and <code>{_IOR,_IOW,_IOWR}(type,nr,size)</code>. They use <i>sizeof(size)</i> so that size is a misnomer here: this third argument is a data type. </p>
<p> Note that the size bits are very unreliable: in lots of cases they are wrong, either because of buggy macros using <i>sizeof(sizeof(struct))</i>, or because of legacy values. </p>
<p> Thus, it seems that the new structure only gave disadvantages: it does not help in checking, but it causes varying values for the various architectures.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_console/">ioctl_console</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_fat/">ioctl_fat</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_ficlonerange/">ioctl_ficlonerange</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_fideduperange/">ioctl_fideduperange</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_fslabel/">ioctl_fslabel</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_getfsmap/">ioctl_getfsmap</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_ns/">ioctl_ns</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2), <code><a href="/docs/linux/man/2-ioctl_userfaultfd/">ioctl_userfaultfd</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/4-sd/">sd</a></code>(4), <code><a href="/docs/linux/man/4-tty/">tty</a></code>(4)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
