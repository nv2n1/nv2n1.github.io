---
title: "remove(3)"
name: "remove"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remove/"
description: "remove – remove a file or directory"
---

<p>remove &#8211; remove a file or directory</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
int remove(const char *pathname);</code></pre>
<h2>Description</h2>
<p><code>remove</code>() deletes a name from the filesystem. It calls <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2) for files, and <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2) for directories. </p>
<p> If the removed name was the last link to a file and no processes have the file open, the file is deleted and the space it was using is made available for reuse. </p>
<p> If the name was the last link to a file, but any processes still have the file open, the file will remain in existence until the last file descriptor referring to it is closed. </p>
<p> If the name referred to a symbolic link, the link is removed. </p>
<p> If the name referred to a socket, FIFO, or device, the name is removed, but processes which have the object open may continue to use it.</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<p>The errors that occur are those for <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2) and <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2).</p>
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
<td> <code>remove</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99, 4.3BSD.</p>
<h2>Bugs</h2>
<p>Infelicities in the protocol underlying NFS can cause the unexpected disappearance of files which are still being used.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rm/">rm</a></code>(1), <code><a href="/docs/linux/man/1-unlink/">unlink</a></code>(1), <code><a href="/docs/linux/man/2-link/">link</a></code>(2), <code><a href="/docs/linux/man/2-mknod/">mknod</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2), <code><a href="/docs/linux/man/2-rmdir/">rmdir</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
