---
title: "ftok(3)"
name: "ftok"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ftok/"
description: "ftok – convert a pathname and a project identifier to a System V IPC key"
---

<h2 class="name">NAME</h2>
<p> ftok &#8211; convert a pathname and a project identifier to a System V IPC key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/types.h&gt;
</code></pre>
<p> <code>key_t ftok(const char *</code><i>pathname</i><code>, int </code><i>proj_id</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ftok</code>() function uses the identity of the file named by the given <i>pathname</i> (which must refer to an existing, accessible file) and the least significant 8 bits of <i>proj_id</i> (which must be nonzero) to generate a <i>key_t</i> type System V IPC key, suitable for use with <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), or <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2). </p>
<p> The resulting value is the same for all pathnames that name the same file, when the same value of <i>proj_id</i> is used. The value returned should be different when the (simultaneously existing) files or the project IDs differ.</p>
<h2>RETURN VALUE</h2>
<p> On success, the generated <i>key_t</i> value is returned. On failure -1 is returned, with <i>errno</i> indicating the error as for the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) system call.</p>
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
<td> <code>ftok</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> On some ancient systems, the prototype was: </p>
<p> <code>key_t ftok(char *</code><i>pathname</i><code>, char </code><i>proj_id</i><code>);</code> </p>
<p> Today, <i>proj_id</i> is an <i>int</i>, but still only 8 bits are used. Typical usage has an ASCII character <i>proj_id</i>, that is why the behavior is said to be undefined when <i>proj_id</i> is zero. </p>
<p> Of course, no guarantee can be given that the resulting <i>key_t</i> is unique. Typically, a best-effort attempt combines the given <i>proj_id</i> byte, the lower 16 bits of the inode number, and the lower 8 bits of the device number into a 32-bit result. Collisions may easily happen, for example between files on <i>/dev/hda1</i> and files on <i>/dev/sda1</i>.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
