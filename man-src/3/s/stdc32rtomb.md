---
title: "stdc32rtomb(3)"
name: "stdc32rtomb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdc32rtomb/"
description: "std::c32rtomb – std::c32rtomb"
---

<p>std::c32rtomb &#8211; std::c32rtomb</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cuchar&gt;<br />
std::size_t c32rtomb( char* s, char32_t c32, std::mbstate_t* ps ); <i>(since C++11)</i><br />
Converts a UTF-32 character to its narrow multibyte representation.<br />
If s is not a null pointer, the function determines the number of bytes necessary to store the multibyte character representation of c32 (including any shift sequences, and taking into account the current multibyte conversion state *ps), and stores the multibyte character representation in the character array whose first element is pointed to by s, updating *ps as necessary. At most MB_CUR_MAX bytes can be written by this function.<br />
If s is a null pointer, the call is equivalent to std::c32rtomb(buf, U&#8217;
