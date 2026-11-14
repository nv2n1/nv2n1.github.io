---
title: "readdir_r(3)"
name: "readdir_r"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readdir_r/"
description: "readdir_r – read a directory"
---

<p>readdir_r &#8211; read a directory</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;dirent.h&gt;

int readdir_r(DIR *dirp, struct dirent *entry, struct dirent **result);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>readdir_r</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>This function is deprecated; use <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) instead. </p>
<p> The <code>readdir_r</code>() function was invented as a reentrant version of <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3). It reads the next directory entry from the directory stream <i>dirp</i>, and returns it in the caller-allocated buffer pointed to by <i>entry</i>. For details of the <i>dirent</i> structure, see <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3). </p>
<p> A pointer to the returned buffer is placed in <i>*result</i>; if the end of the directory stream was encountered, then NULL is instead returned in <i>*result</i>. </p>
<p> It is recommended that applications use <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) instead of <code>readdir_r</code>(). Furthermore, since version 2.24, glibc deprecates <code>readdir_r</code>(). The reasons are as follows:</p>
<dl>
<dt>*</p>
<dd>On systems where <code>NAME_MAX</code> is undefined, calling <code>readdir_r</code>() may be unsafe because the interface does not allow the caller to specify the length of the buffer used for the returned directory entry.</p>
<dt>*</p>
<dd>On some systems, <code>readdir_r</code>() can&#8217;t read directory entries with very long names. When the glibc implementation encounters such a name, <code>readdir_r</code>() fails with the error <code>ENAMETOOLONG</code> <i>after the final directory entry has been read</i>. On some other systems, <code>readdir_r</code>() may return a success status, but the returned <i>d_name</i> field may not be null terminated or may be truncated.</p>
<dt>*</p>
<dd>In the current POSIX.1 specification (POSIX.1-2008), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) is not required to be thread-safe. However, in modern implementations (including the glibc implementation), concurrent calls to <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) that specify different directory streams are thread-safe. Therefore, the use of <code>readdir_r</code>() is generally unnecessary in multithreaded programs. In cases where multiple threads must read from the same directory stream, using <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) with external synchronization is still preferable to the use of <code>readdir_r</code>(), for the reasons given in the points above.</p>
<dt>*</p>
<dd>It is expected that a future version of POSIX.1 will make <code>readdir_r</code>() obsolete, and require that <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) be thread-safe when concurrently employed on different directory streams.</dl>
<h2>Return Value</h2>
<p>The <code>readdir_r</code>() function returns 0 on success. On error, it returns a positive error number (listed under ERRORS). If the end of the directory stream is reached, <code>readdir_r</code>() returns 0, and returns NULL in <i>*result</i>.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd>Invalid directory stream descriptor <i>dirp</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd>A directory entry whose name was too long to be read was encountered.</dl>
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
<td> <code>readdir_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
