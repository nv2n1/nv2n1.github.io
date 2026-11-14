---
title: "strfry(3)"
name: "strfry"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strfry/"
description: "strfry – randomize a string"
---

<p>strfry &#8211; randomize a string</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;

char *strfry(char *string);</code></pre>
<h2>Description</h2>
<p>The <code>strfry</code>() function randomizes the contents of <i>string</i> by randomly swapping characters in the string. The result is an anagram of <i>string</i>.</p>
<h2>Return Value</h2>
<p>The <code>strfry</code>() functions returns a pointer to the randomized string.</p>
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
<td> <code>strfry</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The <code>strfry</code>() function is unique to the GNU C Library.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-memfrob/">memfrob</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
