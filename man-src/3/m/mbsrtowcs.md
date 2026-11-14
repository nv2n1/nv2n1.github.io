---
title: "mbsrtowcs(3)"
name: "mbsrtowcs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbsrtowcs/"
description: "mbsrtowcs – convert a multibyte string to a wide-character string"
---

<h2 class="name">NAME</h2>
<p> mbsrtowcs &#8211; convert a multibyte string to a wide-character string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
size_t mbsrtowcs(wchar_t *dest, const char **src,
                 size_t len, mbstate_t *ps);
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>dest</i> is not NULL, the <code>mbsrtowcs</code>() function converts the multibyte string <i>*src</i> to a wide-character string starting at <i>dest</i>. At most <i>len</i> wide characters are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>mbrtowc(dest, *src, n, ps)</i> where <i>n</i> is some positive number, as long as this call succeeds, and then incrementing <i>dest</i> by one and <i>*src</i> by the number of bytes consumed. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd> An invalid multibyte sequence has been encountered. In this case, <i>*src</i> is left pointing to the invalid multibyte sequence, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>.</p>
<dt>2.</p>
<dd> <i>len</i> non-L&#8217;
