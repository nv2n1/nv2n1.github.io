---
title: "getdirentries(3)"
name: "getdirentries"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdirentries/"
description: "getdirentries – get directory entries in a filesystem-independent format"
---

<h2 class="name">NAME</h2>
<p> getdirentries &#8211; get directory entries in a filesystem-independent format </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;dirent.h&gt;</code> </p>
<p> <code>ssize_t getdirentries(int </code><i>fd</i><code>, char *</code><i>buf</i><code>, size_t </code><i>nbytes</i> <code>, off_t *</code><i>basep</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getdirentries</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> Read directory entries from the directory specified by <i>fd</i> into <i>buf</i>. At most <i>nbytes</i> are read. Reading starts at offset <i>*basep</i>, and <i>*basep</i> is updated with the new position after reading.</p>
<h2>RETURN VALUE</h2>
<p> <code>getdirentries</code>() returns the number of bytes read or zero when at the end of the directory. If an error occurs, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> See the Linux library source code for details.</p>
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
<td> <code>getdirentries</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs, and a few other systems. Use <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3) and <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
