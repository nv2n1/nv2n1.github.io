---
title: "mbtowc(3)"
name: "mbtowc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbtowc/"
description: "mbtowc – convert a multibyte sequence to a wide character"
---

<h2 class="name">NAME</h2>
<p> mbtowc &#8211; convert a multibyte sequence to a wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int mbtowc(wchar_t *pwc, const char *s, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The main case for this function is when <i>s</i> is not NULL and <i>pwc</i> is not NULL. In this case, the <code>mbtowc</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i>, extracts the next complete multibyte character, converts it to a wide character and stores it at <i>*pwc</i>. It updates an internal shift state known only to the <code>mbtowc</code>() function. If <i>s</i> does not point to a null byte (&#8216;
