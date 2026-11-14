---
title: "telldir(3)"
name: "telldir"
section: "3"
letter: "t"
url: "/docs/linux/man/3-telldir/"
description: "telldir – return current location in directory stream"
---

<p>telldir &#8211; return current location in directory stream</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;dirent.h&gt;

long telldir(DIR *dirp);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>telldir</code>():<br />
&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>telldir</code>() function returns the current location associated with the directory stream <i>dirp</i>.</p>
<h2>Return Value</h2>
<p>On success, the <code>telldir</code>() function returns the current location in the directory stream. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd>Invalid directory stream descriptor <i>dirp</i>.</dl>
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
<td> <code>telldir</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>Notes</h2>
<p>In glibc up to version 2.1.1, the return type of <code>telldir</code>() was <i>off_t</i>. POSIX.1-2001 specifies <i>long</i>, and this is the type used since glibc 2.1.2. </p>
<p> In early filesystems, the value returned by <code>telldir</code>() was a simple file offset within a directory. Modern filesystems use tree or hash structures, rather than flat tables, to represent directories. On such filesystems, the value returned by <code>telldir</code>() (and used internally by <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)) is a &quot;cookie&quot; that is used by the implementation to derive a position within a directory. Application programs should treat this strictly as an opaque value, making <i>no</i> assumptions about its contents.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-seekdir/">seekdir</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
