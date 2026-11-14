---
title: "ttyname_r(3)"
name: "ttyname_r"
section: "3"
letter: "t"
url: "/docs/linux/man/3-ttyname_r/"
description: "ttyname, ttyname_r – return name of a terminal"
---

<p>ttyname, ttyname_r &#8211; return name of a terminal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

char *ttyname(int fd);

int ttyname_r(int fd, char *buf, size_t buflen);</code></pre>
<h2>Description</h2>
<p>The function <code>ttyname</code>() returns a pointer to the null-terminated pathname of the terminal device that is open on the file descriptor <i>fd</i>, or NULL on error (for example, if <i>fd</i> is not connected to a terminal). The return value may point to static data, possibly overwritten by the next call. The function <code>ttyname_r</code>() stores this pathname in the buffer <i>buf</i> of length <i>buflen</i>.</p>
<h2>Return Value</h2>
<p>The function <code>ttyname</code>() returns a pointer to a pathname on success. On error, NULL is returned, and <i>errno</i> is set appropriately. The function <code>ttyname_r</code>() returns 0 on success, and an error number upon error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd>Bad file descriptor.</p>
<dd><code>ENODEV</code> <i>fd</i> refers to a slave pseudoterminal device but the corresponding pathname could not be found (see NOTES).</p>
<dt><code>ENOTTY</code></p>
<dd><i>fd</i> does not refer to a terminal device.</p>
<dt><code>ERANGE</code></p>
<dd>(<code>ttyname_r</code>()) <i>buflen</i> was too small to allow storing the pathname.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>ttyname</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ttyname
</td>
</tr>
<tr VALIGN=top>
<td> <code>ttyname_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.2BSD.</p>
<h2>Notes</h2>
<p>A process that keeps a file descriptor that refers to a <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4) device open when switching to another mount namespace that uses a different <i>/dev/ptmx</i> instance may still accidentally find that a device path of the same name for that file descriptor exists. However, this device path refers to a different device and thus can&#8217;t be used to access the device that the file descriptor refers to. Calling <code>ttyname</code>() or <code>ttyname_r</code>() on the file descriptor in the new mount namespace will cause these functions to return NULL and set <i>errno</i> to <code>ENODEV</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tty/">tty</a></code>(1), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/3-ctermid/">ctermid</a></code>(3), <code><a href="/docs/linux/man/3-isatty/">isatty</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
