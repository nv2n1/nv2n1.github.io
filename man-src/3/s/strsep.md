---
title: "strsep(3)"
name: "strsep"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strsep/"
description: "strsep – extract token from string"
---

<p>strsep &#8211; extract token from string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strsep(char **stringp, const char *delim);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strsep</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>If <i>*stringp</i> is NULL, the <code>strsep</code>() function returns NULL and does nothing else. Otherwise, this function finds the first token in the string <i>*stringp</i>, that is delimited by one of the bytes in the string <i>delim</i>. This token is terminated by overwriting the delimiter with a null byte (&#8216;\0&#8217;), and <i>*stringp</i> is updated to point past the token. In case no delimiter was found, the token is taken to be the entire string <i>*stringp</i>, and <i>*stringp</i> is made NULL.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strsep</code>() function returns a pointer to the token, that is, it returns the original value of <i>*stringp</i>.  </p>
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
<td> <code>strsep</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.4BSD.  </p>
<h2>NOTES</h2>
<p> The <code>strsep</code>() function was introduced as a replacement for <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), since the latter cannot handle empty fields. However, <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3) conforms to C89/C99 and hence is more portable.  </p>
<h2>BUGS</h2>
<p> Be cautious when using this function. If you do use it, note that: </p>
<dl>
<dt>*</dt>
<dd> <p> This function modifies its first argument. </p>
 </dd>
<dt>*</dt>
<dd> <p> This function cannot be used on constant strings. </p>
 </dd>
<dt>*</dt>
<dd> <p> The identity of the delimiting character is lost. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
