---
title: "putgrent(3)"
name: "putgrent"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putgrent/"
description: "putgrent – write a group database entry to a file"
---

<p>putgrent &#8211; write a group database entry to a file</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */

#include &lt;grp.h&gt;
int putgrent(const struct group *grp, FILE *stream);</code></pre>
<h2>Description</h2>
<p>The <code>putgrent</code>() function is the counterpart for <code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3). The function writes the content of the provided <i>struct group</i> into the <i>stream</i>. The list of group members must be NULL-terminated or NULL-initialized. The <i>struct group</i> is defined as follows: </p>
<pre><code>struct group {
    char *gr_name;   /* group name */
    char *gr_passwd; /* group password */
    gid_t gr_gid;    /* group ID */
    char **gr_mem;   /* group members */
};</code></pre>
<h2>Return Value</h2>
<p>The function returns zero on success, and a nonzero value on error.</p>
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
<td> <code>putgrent</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a GNU extension.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-fgetgrent/">fgetgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
