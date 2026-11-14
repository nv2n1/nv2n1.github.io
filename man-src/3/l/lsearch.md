---
title: "lsearch(3)"
name: "lsearch"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lsearch/"
description: "lfind, lsearch – linear search of an array"
---

<h2 class="name">NAME</h2>
<p> lfind, lsearch &#8211; linear search of an array </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;search.h&gt;
void *lfind(const void *key, const void *base, size_t *nmemb,
            size_t size, int (*compar)(const void *, const void *));
void *lsearch(const void *key, void *base, size_t *nmemb,
              size_t size, int (*compar)(const void *, const void *));
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>lfind</code>() and <code>lsearch</code>() perform a linear search for <i>key</i> in the array <i>base</i> which has <i>*nmemb</i> elements of <i>size</i> bytes each. The comparison function referenced by <i>compar</i> is expected to have two arguments which point to the <i>key</i> object and to an array member, in that order, and which returns zero if the <i>key</i> object matches the array member, and nonzero otherwise. </p>
<p> If <code>lsearch</code>() does not find a matching element, then the <i>key</i> object is inserted at the end of the table, and <i>*nmemb</i> is incremented. In particular, one should know that a matching element exists, or that more room is available.</p>
<h2>RETURN VALUE</h2>
<p> <code>lfind</code>() returns a pointer to a matching member of the array, or NULL if no match is found. <code>lsearch</code>() returns a pointer to a matching member of the array, or to the newly added member if no match is found.</p>
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
<td> <code>lfind</code>(), <code>lsearch</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. Present in libc since libc-4.6.27.</p>
<h2>BUGS</h2>
<p> The naming is unfortunate.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bsearch/">bsearch</a></code>(3), <code><a href="/docs/linux/man/3-hsearch/">hsearch</a></code>(3), <code><a href="/docs/linux/man/3-tsearch/">tsearch</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
