---
title: "mbstowcs(3)"
name: "mbstowcs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbstowcs/"
description: "mbstowcs – convert a multibyte string to a wide-character string"
---

<h2 class="name">NAME</h2>
<p> mbstowcs &#8211; convert a multibyte string to a wide-character string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
size_t mbstowcs(wchar_t *dest, const char *src, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>dest</i> is not NULL, the <code>mbstowcs</code>() function converts the multibyte string <i>src</i> to a wide-character string starting at <i>dest</i>. At most <i>n</i> wide characters are written to <i>dest</i>. The sequence of characters in the string <i>src</i> shall begin in the initial shift state. The conversion can stop for three reasons:</p>
<dl>
<dt>1.</p>
<dd> An invalid multibyte sequence has been encountered. In this case, <i>(size_t)&nbsp;-1</i> is returned.</p>
<dt>2.</p>
<dd> <i>n</i> non-L&#8217;
