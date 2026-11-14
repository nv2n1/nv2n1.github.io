---
title: "minor(3)"
name: "minor"
section: "3"
letter: "m"
url: "/docs/linux/man/3-minor/"
description: "makedev, major, minor – manage a device number"
---

<h2 class="name">NAME</h2>
<p> makedev, major, minor &#8211; manage a device number </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/sysmacros.h&gt;
dev_t makedev(unsigned int maj, unsigned int min);
unsigned int major(dev_t dev);
unsigned int minor(dev_t dev);
</code></pre>
<h2>DESCRIPTION</h2>
<p> A device ID consists of two parts: a major ID, identifying the class of the device, and a minor ID, identifying a specific instance of a device in that class. A device ID is represented using the type <i>dev_t</i>. </p>
<p> Given major and minor device IDs, <code>makedev</code>() combines these to produce a device ID, returned as the function result. This device ID can be given to <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), for example. </p>
<p> The <code>major</code>() and <code>minor</code>() functions perform the converse task: given a device ID, they return, respectively, the major and minor components. These macros can be useful to, for example, decompose the device IDs in the structure returned by <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2).</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>makedev</code>(), <code>major</code>(), <code>minor</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The <code>makedev</code>(), <code>major</code>(), and <code>minor</code>() functions are not specified in POSIX.1, but are present on many other systems.</p>
<h2>NOTES</h2>
<p> These interfaces are defined as macros. Since glibc 2.3.3, they have been aliases for three GNU-specific functions: <code>gnu_dev_makedev</code>(), <code>gnu_dev_major</code>(), and <code>gnu_dev_minor</code>(). The latter names are exported, but the traditional names are more portable. </p>
<p> The BSDs expose the definitions for these macros via <i>&lt;sys/types.h&gt;</i>. Depending on the version, glibc also exposes definitions for these macros from that header file if suitable feature test macros are defined. However, this behavior was deprecated in glibc 2.25, and since glibc 2.28, <i>&lt;sys/types.h&gt;</i> no longer provides these definitions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
