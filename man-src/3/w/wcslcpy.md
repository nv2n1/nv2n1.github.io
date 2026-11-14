---
title: "wcslcpy(3)"
name: "wcslcpy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcslcpy/"
description: "wcslcat wcslcpy – wide character string manipulation operations"
---

<p><code>wcslcat</code> <code>wcslcpy</code> &#8211; wide character string manipulation operations</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/wchar.h Ft size_t Fn wcslcat wchar_t *s1 const wchar_t *s2 size_t n Ft size_t Fn wcslcpy wchar_t *s1 const wchar_t *s2 size_t n</p>
<h2>Description</h2>
<p>The functions implement string manipulation operations over wide character strings. For a detailed description, refer to documents for the respective single-byte counterpart, such as <a href="/docs/linux/man/3-strlcpy/">strlcpy</a>(3).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-strlcat/">strlcat</a>(3), <a href="/docs/linux/man/3-strlcpy/">strlcpy</a>(3),</p>
<h2>Standards</h2>
<p>Fn wcslcat and Fn wcslcpy , which are BSD extensions.</p>
