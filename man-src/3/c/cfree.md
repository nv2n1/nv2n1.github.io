---
title: "cfree(3)"
name: "cfree"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfree/"
description: "cfree – free allocated memory"
---

<h2 class="name">NAME</h2>
<p> cfree &#8211; free allocated memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
/* In SunOS 4 */
int cfree(void *ptr);
/* In glibc or FreeBSD libcompat */
void cfree(void *ptr);
/* In SCO OpenServer */
void cfree(char *ptr, unsigned num, unsigned size);
/* In Solaris watchmalloc.so.1 */
void cfree(void *ptr, size_t nelem, size_t elsize);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>cfree</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> This function should never be used. Use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) instead. Starting with version 2.26, it has been removed from glibc.</p>
<h3>1-arg cfree</h3>
<p> In glibc, the function <code>cfree</code>() is a synonym for <code><a href="/docs/linux/man/3-free/">free</a></code>(3), &quot;added for compatibility with SunOS&quot;. </p>
<p> Other systems have other functions with this name. The declaration is sometimes in <i>&lt;stdlib.h&gt;</i> and sometimes in <i>&lt;malloc.h&gt;</i>.</p>
<h3>3-arg cfree</h3>
<p> Some SCO and Solaris versions have malloc libraries with a 3-argument <code>cfree</code>(), apparently as an analog to <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3). </p>
<p> If you need it while porting something, add </p>
<p> #define cfree(p, n, s) free((p)) </p>
<p> to your file. </p>
<p> A frequently asked question is &quot;Can I use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to free memory allocated with <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), or do I need <code>cfree</code>()? Answer: use <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> An SCO manual writes: &quot;The cfree routine is provided for compliance to the iBCSe2 standard and simply calls free. The num and size arguments to cfree are not used.&quot;</p>
<h2>RETURN VALUE</h2>
<p> The SunOS version of <code>cfree</code>() (which is a synonym for <code><a href="/docs/linux/man/3-free/">free</a></code>(3)) returns 1 on success and 0 on failure. In case of error, <i>errno</i> is set to <code>EINVAL</code>: the value of <i>ptr</i> was not a pointer to a block previously allocated by one of the routines in the <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) family.</p>
<h2>VERSIONS</h2>
<p> The <code>cfree</code>() function was removed from glibc in version 2.26.</p>
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
<td> <code>cfree</code>() </td>
<td>Thread safety</td>
<td>MT-Safe /* In glibc */
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The 3-argument version of <code>cfree</code>() as used by SCO conforms to the iBCSe2 standard: Intel386 Binary Compatibility Specification, Edition 2.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
