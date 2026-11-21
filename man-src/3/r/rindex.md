---
title: "rindex(3)"
name: "rindex"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rindex/"
description: "index, rindex – locate character in string"
---

<p>index, rindex &#8211; locate character in string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;strings.h&gt;
char *index(const char *s, int c);
char *rindex(const char *s, int c);</code></pre>
<h2>Description</h2>
<p>The <code>index</code>() function returns a pointer to the first occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The <code>rindex</code>() function returns a pointer to the last occurrence of the character <i>c</i> in the string <i>s</i>. </p>
<p> The terminating null byte (&#8216;\0&#8217;) is considered to be a part of the strings.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>index</code>() and <code>rindex</code>() functions return a pointer to the matched character or NULL if the character is not found.  </p>
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
<td> <code>index</code>(), <code>rindex</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD; marked as LEGACY in POSIX.1-2001. POSIX.1-2008 removes the specifications of <code>index</code>() and <code>rindex</code>(), recommending <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3) and <code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3) instead.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
