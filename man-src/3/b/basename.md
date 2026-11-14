---
title: "basename(3)"
name: "basename"
section: "3"
letter: "b"
url: "/docs/linux/man/3-basename/"
description: "basename, dirname – parse pathname components"
---

<h2 class="name">NAME</h2>
<p> basename, dirname &#8211; parse pathname components </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libgen.h&gt;
char *dirname(char *path);
char *basename(char *path);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Warning: there are two different functions <code>basename</code>() &#8211; see below. </p>
<p> The functions <code>dirname</code>() and <code>basename</code>() break a null-terminated pathname string into directory and filename components. In the usual case, <code>dirname</code>() returns the string up to, but not including, the final &#8216;/&#8217;, and <code>basename</code>() returns the component following the final &#8216;/&#8217;. Trailing &#8216;/&#8217; characters are not counted as part of the pathname. </p>
<p> If <i>path</i> does not contain a slash, <code>dirname</code>() returns the string &quot;.&quot; while <code>basename</code>() returns a copy of <i>path</i>. If <i>path</i> is the string &quot;/&quot;, then both <code>dirname</code>() and <code>basename</code>() return the string &quot;/&quot;. If <i>path</i> is a null pointer or points to an empty string, then both <code>dirname</code>() and <code>basename</code>() return the string &quot;.&quot;. </p>
<p> Concatenating the string returned by <code>dirname</code>(), a &quot;/&quot;, and the string returned by <code>basename</code>() yields a complete pathname. </p>
<p> Both <code>dirname</code>() and <code>basename</code>() may modify the contents of <i>path</i>, so it may be desirable to pass a copy when calling one of these functions. </p>
<p> These functions may return pointers to statically allocated memory which may be overwritten by subsequent calls. Alternatively, they may return a pointer to some part of <i>path</i>, so that the string referred to by <i>path</i> should not be modified or freed until the pointer returned by the function is no longer required. </p>
<p> The following list of examples (taken from SUSv2) shows the strings returned by <code>dirname</code>() and <code>basename</code>() for different paths:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><code>path </code></td>
<td><code>dirname</code></td>
<td><code>basename</code>
</td>
</tr>
<tr VALIGN=top>
<td>/usr/lib</td>
<td>/usr</td>
<td>lib
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>/usr/ </td>
<td>/</td>
<td>usr
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>usr </td>
<td>.</td>
<td>usr
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>/ </td>
<td>/</td>
<td>/
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>. </td>
<td>.</td>
<td>.
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>.. </td>
<td>.</td>
<td>..
</td>
<td>
</td>
</tr>
</table>
</dl>
<h2>RETURN VALUE</h2>
<p> Both <code>dirname</code>() and <code>basename</code>() return pointers to null-terminated strings. (Do not pass these pointers to <code><a href="/docs/linux/man/3-free/">free</a></code>(3).)</p>
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
<td> <code>basename</code>(), <code>dirname</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> There are two different versions of <code>basename</code>() &#8211; the POSIX version described above, and the GNU version, which one gets after </p>
<p> <code> #define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */ <code> #include &lt;string.h&gt;</code> </p>
<p> The GNU version never modifies its argument, and returns the empty string when <i>path</i> has a trailing slash, and in particular also when it is &quot;/&quot;. There is no GNU version of <code>dirname</code>(). </p>
<p> With glibc, one gets the POSIX version of <code>basename</code>() when <i>&lt;libgen.h&gt;</i> is included, and the GNU version otherwise.</p>
<h2>BUGS</h2>
<p> In the glibc implementation, the POSIX versions of these functions modify the <i>path</i> argument, and segfault when called with a static string such as &quot;/usr/&quot;. </p>
<p> Before glibc 2.2.1, the glibc version of <code>dirname</code>() did not correctly handle pathnames with trailing &#8216;/&#8217; characters, and generated a segfault if given a NULL argument.</p>
<h2>EXAMPLES</h2>
<p> The following code snippet demonstrates the use of <code>basename</code>() and <code>dirname</code>(): char *dirc, *basec, *bname, *dname; char *path = &quot;/etc/passwd&quot;; </p>
<p> dirc = strdup(path); basec = strdup(path); dname = dirname(dirc); bname = basename(basec); printf(&quot;dirname=%s, basename=%s
&quot;, dname, bname);</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-basename/">basename</a></code>(1), <code><a href="/docs/linux/man/1-dirname/">dirname</a></code>(1)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
