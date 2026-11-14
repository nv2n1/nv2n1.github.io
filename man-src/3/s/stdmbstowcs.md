---
title: "stdmbstowcs(3)"
name: "stdmbstowcs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmbstowcs/"
description: "std::mbstowcs – std::mbstowcs"
---

<p>std::mbstowcs &#8211; std::mbstowcs</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;cstdlib&gt;

    std::size_t mbstowcs(wchar_t *dst, const char *src, std::size_t len);</code></pre>
<p>Converts a multibyte character string from the array whose first element is pointed to by src to its wide character representation. Converted characters are stored in the successive elements of the array pointed to by dst. No more than len wide characters are written to the destination array.<br />
Each character is converted as if by a call to std::mbtowc, except that the mbtowc conversion state is unaffected. The conversion stops if:<br />
* The multibyte null character was converted and stored.<br />
* An invalid (in the current C locale) multibyte character was encountered.<br />
* The next wide character to be stored would exceed len. </p>
<h2>Notes</h2>
<p>In most implementations, this function updates a global static object of type std::mbstate_t as it processes through the string, and cannot be called simultaneously by two threads, std::mbsrtowcs should be used in such cases.<br />
POSIX specifies a common extension: if dst is a null pointer, this function returns the number of wide characters that would be written to dst, if converted. Similar behavior is standard for std::mbsrtowcs. </p>
<h2>Parameters</h2>
<p>dst &#8211; pointer to wide character array where the wide string will be stored<br />
src &#8211; pointer to the first element of a null-terminated multibyte string to convert<br />
len &#8211; number of wide characters available in the array pointed to by dst</p>
<h2>Return value</h2>
<p>On success, returns the number of wide characters, excluding the terminating L&#8217;
