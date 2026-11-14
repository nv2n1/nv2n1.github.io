---
title: "lseek64(3)"
name: "lseek64"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lseek64/"
description: "lseek64 – reposition 64-bit read/write file offset"
---

<h2 class="name">NAME</h2>
<p> lseek64 &#8211; reposition 64-bit read/write file offset </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _LARGEFILE64_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>off64_t lseek64(int </code><i>fd</i><code>, off64_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>lseek</code>() family of functions reposition the offset of the open file associated with the file descriptor <i>fd</i> to <i>offset</i> bytes relative to the start, current position, or end of the file, when <i>whence</i> has the value <code>SEEK_SET</code>, <code>SEEK_CUR</code>, or <code>SEEK_END</code>, respectively. </p>
<p> For more details, return value, and errors, see <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). </p>
<p> Four interfaces are available: <code>lseek</code>(), <code>lseek64</code>(), <code>llseek</code>(), and <code>_llseek</code>().</p>
<h3>lseek()</h3>
<p> Prototype: </p>
<p> <code>off_t lseek(int </code><i>fd</i><code>, off_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code> </p>
<p> The C library&#8217;s <code>lseek</code>() wrapper function uses the type <i>off_t</i>. This is a 32-bit signed type on 32-bit architectures, unless one compiles with </p>
<p> #define _FILE_OFFSET_BITS 64 </p>
<p> in which case it is a 64-bit signed type.</p>
<h3>lseek64()</h3>
<p> Prototype: </p>
<p> <code>off64_t lseek64(int </code><i>fd</i><code>, off64_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code> </p>
<p> The <code>lseek64</code>() library function uses a 64-bit type even when <i>off_t</i> is a 32-bit type. Its prototype (and the type <i>off64_t</i>) is available only when one compiles with </p>
<p> #define _LARGEFILE64_SOURCE </p>
<p> The function <code>lseek64</code>() is available since glibc 2.1.</p>
<h3>llseek()</h3>
<p> Prototype: </p>
<p> <code>loff_t llseek(int </code><i>fd</i><code>, loff_t </code><i>offset</i><code>, int </code><i>whence</i><code>);</code> </p>
<p> The type <i>loff_t</i> is a 64-bit signed type. The <code>llseek</code>() library function is available in glibc and works without special defines. However, the glibc headers do not provide a prototype. Users should add the above prototype, or something equivalent, to their own source. When users complained about data loss caused by a miscompilation of <code><a href="/docs/linux/man/8-e2fsck/">e2fsck</a></code>(8), glibc 2.1.3 added the link-time warning </p>
<p> &quot;the `llseek&#8217; function may be dangerous; use `lseek64&#8242; instead.&quot; </p>
<p> This makes this function unusable if one desires a warning-free compilation. </p>
<p> Since glibc 2.28, this function symbol is no longer available to newly linked applications.</p>
<h3>_llseek()</h3>
<p> On 32-bit architectures, this is the system call that is used (by the C library wrapper functions) to implement all of the above functions. The prototype is: </p>
<p> <code>int _llseek(int </code><i>fd</i><code>, off_t </code><i>offset_hi</i><code>, off_t </code><i>offset_lo</i><code>,</code> <code> loff_t *</code><i>result</i><code>, int </code><i>whence</i><code>);</code> </p>
<p> For more details, see <code><a href="/docs/linux/man/2-llseek/">llseek</a></code>(2). </p>
<p> 64-bit systems don&#8217;t need an <code>_llseek</code>() system call. Instead, they have an <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) system call that supports 64-bit file offsets.</p>
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
<td> <code>lseek64</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>NOTES</h2>
<p> <code>lseek64</code>() is one of the functions that was specified in the Large File Summit (LFS) specification that was completed in 1996. The purpose of the specification was to provide transitional support that allowed applications on 32-bit systems to access files whose size exceeds that which can be represented with a 32-bit <i>off_t</i> type. As noted above, this symbol is exposed by header files if the <code>_LARGEFILE64_SOURCE</code> feature test macro is defined. ALternatively, on a 32-bit system, the symbol <i>lseek</i> is aliased to <i>lseek64</i> if the macro <code>_FILE_OFFSET_BITS</code> is defined with the value 64.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-llseek/">llseek</a></code>(2), <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
