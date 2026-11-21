---
title: "strnstr(3)"
name: "strnstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strnstr/"
description: "strnstr – locate a substring in a string"
---

<p><code>strnstr</code> &#8211; locate a substring in a string</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/string.h Ft char * Fn strnstr const char *big const char *little size_t len</p>
<h2>Description</h2>
<p>The Fn strnstr function locates the first occurrence of the null-terminated string Fa little in the string Fa big , where not more than Fa len characters are searched. Characters that appear after a `\0&#8217; character are not searched. Since the Fn strnstr function is a Fx specific API, it should only be used when portability is not a concern.  </p>
<h2>RETURN VALUES</h2>
<p> If Fa little is an empty string, Fa big is returned; if Fa little occurs nowhere in Fa big , <code>NULL</code> is returned; otherwise a pointer to the first character of the first occurrence of Fa little is returned.  </p>
<h2>EXAMPLES</h2>
<p> The following sets the pointer <i>ptr</i> to <code>NULL</code> because only the first 4 characters of <i>largestring</i> are searched: <blockquote> </p>
<pre><code>const char *largestring = &quot;Foo Bar Baz&quot;;
const char *smallstring = &quot;Bar&quot;;
char *ptr;
ptr = strnstr(largestring, smallstring, 4);
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-strstr/">strstr</a>(3), <a href="/docs/linux/man/3-strcasestr/">strcasestr</a>(3), <a href="/docs/linux/man/3-memchr/">memchr</a>(3), <a href="/docs/linux/man/3-memmem/">memmem</a>(3), <a href="/docs/linux/man/3-strchr/">strchr</a>(3), <a href="/docs/linux/man/3-strcspn/">strcspn</a>(3), <a href="/docs/linux/man/3-strpbrk/">strpbrk</a>(3), <a href="/docs/linux/man/3-strrchr/">strrchr</a>(3), <a href="/docs/linux/man/3-strsep/">strsep</a>(3), <a href="/docs/linux/man/3-strspn/">strspn</a>(3), <a href="/docs/linux/man/3-strtok/">strtok</a>(3), <a href="/docs/linux/man/3-wcsstr/">wcsstr</a>(3) </p>
<h2>Index</h2>
