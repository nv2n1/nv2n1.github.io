---
title: "euidaccess(3)"
name: "euidaccess"
section: "3"
letter: "e"
url: "/docs/linux/man/3-euidaccess/"
description: "euidaccess, eaccess – check effective user’s permissions for a file"
---

<h2 class="name">NAME</h2>
<p> euidaccess, eaccess &#8211; check effective user&#8217;s permissions for a file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;unistd.h&gt;
int euidaccess(const char *pathname, int mode);
int eaccess(const char *pathname, int mode);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Like <code><a href="/docs/linux/man/2-access/">access</a></code>(2), <code>euidaccess</code>() checks permissions and existence of the file identified by its argument <i>pathname</i>. However, whereas <code><a href="/docs/linux/man/2-access/">access</a></code>(2) performs checks using the real user and group identifiers of the process, <code>euidaccess</code>() uses the effective identifiers. </p>
<p> <i>mode</i> is a mask consisting of one or more of <code>R_OK</code>, <code>W_OK</code>, <code>X_OK</code>, and <code>F_OK</code>, with the same meanings as for <code><a href="/docs/linux/man/2-access/">access</a></code>(2). </p>
<p> <code>eaccess</code>() is a synonym for <code>euidaccess</code>(), provided for compatibility with some other systems.</p>
<h2>RETURN VALUE</h2>
<p> On success (all requested permissions granted), zero is returned. On error (at least one bit in <i>mode</i> asked for a permission that is denied, or some other error occurred), -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> As for <code><a href="/docs/linux/man/2-access/">access</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> The <code>eaccess</code>() function was added to glibc in version 2.4.</p>
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
<td> <code>euidaccess</code>(), <code>eaccess</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard. Some other systems have an <code>eaccess</code>() function.</p>
<h2>NOTES</h2>
<p> <i>Warning</i>: Using this function to check a process&#8217;s permissions on a file before performing some operation based on that information leads to race conditions: the file permissions may change between the two steps. Generally, it is safer just to attempt the desired operation and handle any permission error that occurs. </p>
<p> This function always dereferences symbolic links. If you need to check the permissions on a symbolic link, use <code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2) with the flags <code>AT_EACCESS</code> and <code>AT_SYMLINK_NOFOLLOW</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-access/">access</a></code>(2), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-chown/">chown</a></code>(2), <code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-setgid/">setgid</a></code>(2), <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
