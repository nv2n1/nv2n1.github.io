---
title: "fgetgrent(3)"
name: "fgetgrent"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetgrent/"
description: "fgetgrent – get group file entry"
---

<h2 class="name">NAME</h2>
<p> fgetgrent &#8211; get group file entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;grp.h&gt;
#include &lt;stdio.h&gt;
#include &lt;sys/types.h&gt;
struct group *fgetgrent(FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fgetgrent</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>fgetgrent</code>() function returns a pointer to a structure containing the group information from the file referred to by <i>stream</i>. The first time it is called it returns the first entry; thereafter, it returns successive entries. The file referred to by <i>stream</i> must have the same format as <i>/etc/group</i> (see <code><a href="/docs/linux/man/5-group/">group</a></code>(5)). </p>
<p> The <i>group</i> structure is defined in <i>&lt;grp.h&gt;</i> as follows: </p>
<p> struct group {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;*gr_passwd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group password&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gr_gid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;**gr_mem;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NULL-terminated array of pointers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to names of group members&nbsp;*/ };</p>
<h2>RETURN VALUE</h2>
<p> The <code>fgetgrent</code>() function returns a pointer to a <i>group</i> structure, or NULL if there are no more entries or an error occurs. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to allocate <i>group</i> structure.</dl>
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
<td> <code>fgetgrent</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:fgetgrent
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SVr4.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-endgrent/">endgrent</a></code>(3), <code><a href="/docs/linux/man/3-fgetgrent_r/">fgetgrent_r</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/3-getgrgid/">getgrgid</a></code>(3), <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a></code>(3), <code><a href="/docs/linux/man/3-putgrent/">putgrent</a></code>(3), <code><a href="/docs/linux/man/3-setgrent/">setgrent</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
