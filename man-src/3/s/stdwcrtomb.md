---
title: "stdwcrtomb(3)"
name: "stdwcrtomb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcrtomb/"
description: "std::wcrtomb – std::wcrtomb"
---

<p>std::wcrtomb &#8211; std::wcrtomb</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cwchar&gt;

    std::size_t wcrtomb(char *s, wchar_t wc, std::mbstate_t *ps);</code></pre>
<p>Converts a wide character to its narrow multibyte representation.<br />
If s is not a null pointer, the function determines the number of bytes necessary to store the multibyte character representation of wc (including any shift sequences, and taking into account the current multibyte conversion state *ps), and stores the multibyte character representation in the character array whose first element is pointed to by s, updating *ps as necessary. At most MB_CUR_MAX bytes can be written by this function.<br />
If s is a null pointer, the call is equivalent to std::wcrtomb(buf, L&#8217;
