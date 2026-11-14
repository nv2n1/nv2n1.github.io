---
title: "stdc16rtomb(3)"
name: "stdc16rtomb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdc16rtomb/"
description: "std::c16rtomb – std::c16rtomb"
---

<p>std::c16rtomb &#8211; std::c16rtomb</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cuchar&gt;<br />
std::size_t c16rtomb( char* s, char16_t c16, std::mbstate_t* ps ); <i>(since C++11)</i><br />
Converts a single code point from variable-length 16-bit character representation (typically, UTF-16) to a narrow multibyte character representation.<br />
If s is not a null pointer and c16 is the last 16-bit code unit in a valid variable-length encoding of a code point, the function determines the number of bytes necessary to store the multibyte character representation of that code point (including any shift sequences, and taking into account the current multibyte conversion state *ps), and stores the multibyte character representation in the character array whose first element is pointed to by s, updating *ps as necessary. At most MB_CUR_MAX bytes can be written by this function.<br />
If s is a null pointer, the call is equivalent to std::c16rtomb(buf, u&#8217;
