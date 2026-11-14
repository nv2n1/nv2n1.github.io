---
title: "memfrob(3)"
name: "memfrob"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memfrob/"
description: "memfrob – frobnicate (encrypt) a memory area"
---

<h2 class="name">NAME</h2>
<p> memfrob &#8211; frobnicate (encrypt) a memory area </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;
void *memfrob(void *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>memfrob</code>() function encrypts the first <i>n</i> bytes of the memory area <i>s</i> by exclusive-ORing each character with the number 42. The effect can be reversed by using <code>memfrob</code>() on the encrypted memory area. </p>
<p> Note that this function is not a proper encryption routine as the XOR constant is fixed, and is suitable only for hiding strings.</p>
<h2>RETURN VALUE</h2>
<p> The <code>memfrob</code>() function returns a pointer to the encrypted memory area.</p>
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
<td> <code>memfrob</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The <code>memfrob</code>() function is unique to the GNU C Library.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bstring/">bstring</a></code>(3), <code><a href="/docs/linux/man/3-strfry/">strfry</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
