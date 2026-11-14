---
title: "std-codecvt-4(3)"
name: "std-codecvt-4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-4/"
description: "std::mbtowc – std::mbtowc"
---

<h2 class="name">NAME</h2>
<p> std::mbtowc &#8211; std::mbtowc</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstdlib&gt;<br />
int mbtowc( wchar_t* pwc, const char* s, std::size_t n ); </p>
<p>Converts a multibyte character whose first byte is pointed to by s to a wide character, written to *pwc if pwc is not null.<br />
If s is a null pointer, resets the global conversion state and determines whether shift sequences are used. </p>
<h2>Parameters</h2>
<p>s &#8211; pointer to the multibyte character<br />
n &#8211; limit on the number of bytes in s that can be examined<br />
pwc &#8211; pointer to the wide character for output </p>
<h2>Return value</h2>
<p>If s is not a null pointer, returns the number of bytes that are contained in the multibyte character or -1 if the first bytes pointed to by s do not form a valid multibyte character or 0 if s is pointing at the null charcter &#8216;
