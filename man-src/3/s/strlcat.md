---
title: "strlcat(3)"
name: "strlcat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strlcat/"
description: "strlcpy strlcat – size-bounded string copying and concatenation"
---

<p><code>strlcpy</code> <code>strlcat</code> &#8211; size-bounded string copying and concatenation</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/string.h Ft size_t Fn strlcpy char *dst const char *src size_t size Ft size_t Fn strlcat char *dst const char *src size_t size</p>
<h2>Description</h2>
<p>The Fn strlcpy and Fn strlcat functions copy and concatenate strings respectively. They are designed to be safer, more consistent, and less error prone replacements for <a href="/docs/linux/man/3-strncpy/">strncpy</a>(3) and <a href="/docs/linux/man/3-strncat/">strncat</a>(3). Unlike those functions, Fn strlcpy and Fn strlcat take the full size of the buffer (not just the length) and guarantee to NUL-terminate the result (as long as Fa size is larger than 0 or, in the case of Fn strlcat , as long as there is at least one byte free in Fa dst ) . Note that a byte for the NUL should be included in Fa size . Also note that Fn strlcpy and Fn strlcat only operate on true &#8220;C&#8221; strings. This means that for Fn strlcpy Fa src must be NUL-terminated and for Fn strlcat both Fa src and Fa dst must be NUL-terminated. </p>
<p> The Fn strlcpy function copies up to Fa size &#8211; 1 characters from the NUL-terminated string Fa src to Fa dst , NUL-terminating the result. </p>
<p> The Fn strlcat function appends the NUL-terminated string Fa src to the end of Fa dst . It will append at most Fa size &#8211; strlen(dst) &#8211; 1 bytes, NUL-terminating the result.</p>
<h2>Return Values</h2>
<p>The Fn strlcpy and Fn strlcat functions return the total length of the string they tried to create. For Fn strlcpy that means the length of Fa src . For Fn strlcat that means the initial length of Fa dst plus the length of Fa src . While this may seem somewhat confusing, it was done to make truncation detection simple. </p>
<p> Note, however, that if Fn strlcat traverses Fa size characters without finding a NUL, the length of the string is considered to be Fa size and the destination string will not be NUL-terminated (since there was no space for the NUL). This keeps Fn strlcat from running off the end of a string. In practice this should not happen (as it means that either Fa size is incorrect or that Fa dst is not a proper &#8220;C&#8221; string). The check exists to prevent potential security problems in incorrect code.</p>
<h2>Examples</h2>
<p>The following code fragment illustrates the simple case: </p>
<blockquote>
<pre>char *s, *p, buf[BUFSIZ];
...
(void)strlcpy(buf, s, sizeof(buf));
(void)strlcat(buf, p, sizeof(buf));</pre>
</blockquote>
<p> To detect truncation, perhaps while building a pathname, something like the following might be used: </p>
<blockquote>
<pre>char *dir, *file, pname[MAXPATHLEN];
...
if (strlcpy(pname, dir, sizeof(pname)) &gt;= sizeof(pname))
 goto toolong;
if (strlcat(pname, file, sizeof(pname)) &gt;= sizeof(pname))
 goto toolong;</pre>
</blockquote>
<p> Since it is known how many characters were copied the first time, things can be sped up a bit by using a copy instead of an append: </p>
<blockquote>
<pre>char *dir, *file, pname[MAXPATHLEN];
size_t n;
...
n = strlcpy(pname, dir, sizeof(pname));
if (n &gt;= sizeof(pname))
 goto toolong;
if (strlcpy(pname + n, file, sizeof(pname) - n) &gt;= sizeof(pname) - n)
 goto toolong;</pre>
</blockquote>
<p> However, one may question the validity of such optimizations, as they defeat the whole purpose of Fn strlcpy and Fn strlcat . As a matter of fact, the first version of this manual page got it wrong.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-snprintf/">snprintf</a>(3), <a href="/docs/linux/man/3-strncat/">strncat</a>(3), <a href="/docs/linux/man/3-strncpy/">strncpy</a>(3)</p>
<h2>History</h2>
<p>The Fn strlcpy and Fn strlcat functions first appeared in Ox 2.4 , and made their appearance in Fx 3.3 .</p>
