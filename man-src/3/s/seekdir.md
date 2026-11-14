---
title: "seekdir(3)"
name: "seekdir"
section: "3"
letter: "s"
url: "/docs/linux/man/3-seekdir/"
description: "seekdir – set the position of the next readdir() call in the directory stream."
---

<p>seekdir &#8211; set the position of the next readdir() call in the directory stream.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;dirent.h&gt;

void seekdir(DIR *dirp, long loc);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>seekdir</code>():<br />
&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>seekdir</code>() function sets the location in the directory stream from which the next <code><a href="/docs/linux/man/2-readdir/">readdir</a></code>(2) call will start. The <i>loc</i> argument should be a value returned by a previous call to <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3).</p>
<h2>Return Value</h2>
<p>The <code>seekdir</code>() function returns no value.</p>
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
<td> <code>seekdir</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>Notes</h2>
<p>In glibc up to version 2.1.1, the type of the <i>loc</i> argument was <i>off_t</i>. POSIX.1-2001 specifies <i>long</i>, and this is the type used since glibc 2.1.2. See <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3) for information on why you should be careful in making any assumptions about the value in this argument.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/3-closedir/">closedir</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-rewinddir/">rewinddir</a></code>(3), <code><a href="/docs/linux/man/3-scandir/">scandir</a></code>(3), <code><a href="/docs/linux/man/3-telldir/">telldir</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
