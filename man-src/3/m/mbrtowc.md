---
title: "mbrtowc(3)"
name: "mbrtowc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbrtowc/"
description: "mbrtowc – convert a multibyte sequence to a wide character"
---

<h2 class="name">NAME</h2>
<p> mbrtowc &#8211; convert a multibyte sequence to a wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
size_t mbrtowc(wchar_t *pwc, const char *s, size_t n, mbstate_t *ps);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The main case for this function is when <i>s</i> is not NULL and <i>pwc</i> is not NULL. In this case, the <code>mbrtowc</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i>, extracts the next complete multibyte character, converts it to a wide character and stores it at <i>*pwc</i>. It updates the shift state <i>*ps</i>. If the converted wide character is not L&#8217;
