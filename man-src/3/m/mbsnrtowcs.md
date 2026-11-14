---
title: "mbsnrtowcs(3)"
name: "mbsnrtowcs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbsnrtowcs/"
description: "mbsnrtowcs – convert a multibyte string to a wide-character string"
---

<h2 class="name">NAME</h2>
<p> mbsnrtowcs &#8211; convert a multibyte string to a wide-character string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
size_t mbsnrtowcs(wchar_t *dest, const char **src,
                  size_t nms, size_t len, mbstate_t *ps);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mbsnrtowcs</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>mbsnrtowcs</code>() function is like the <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3) function, except that the number of bytes to be converted, starting at <i>*src</i>, is limited to at most <i>nms</i> bytes. </p>
<p> If <i>dest</i> is not NULL, the <code>mbsnrtowcs</code>() function converts at most <i>nms</i> bytes from the multibyte string <i>*src</i> to a wide-character string starting at <i>dest</i>. At most <i>len</i> wide characters are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>mbrtowc(dest, *src, n, ps)</i> where <i>n</i> is some positive number, as long as this call succeeds, and then incrementing <i>dest</i> by one and <i>*src</i> by the number of bytes consumed. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd> An invalid multibyte sequence has been encountered. In this case, <i>*src</i> is left pointing to the invalid multibyte sequence, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>.</p>
<dt>2.</p>
<dd> The <i>nms</i> limit forces a stop, or <i>len</i> non-L&#8217;
