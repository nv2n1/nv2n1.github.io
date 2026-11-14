---
title: "stdchar_traitscopy(3)"
name: "stdchar_traitscopy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitscopy/"
description: "std::char_traits<CharT>::copy – std::char_traits<CharT>::copy"
---

<p>std::char_traits&lt;CharT&gt;::copy &#8211; std::char_traits&lt;CharT&gt;::copy</p>
<h2>Synopsis</h2>
<pre><code>static char_type *copy(char_type *dest, const char_type *src, std::size_t count);
(until C++ 20)

    static constexpr char_type *copy(char_type *dest, const char_type *src, std::size_t count);
(since C++ 20)</code></pre>
<p>Copies count character from character string pointed to by src to character string pointed to by dest.<br />
Formally, for each i in [0, count), performs assign(src[i], dest[i]).<br />
The behavior is undefined if copied character ranges overlap, i.e. src is in [dest, dest + count). </p>
<h2>Parameters</h2>
<p>dest &#8211; pointer to a character string to copy to<br />
src &#8211; pointer to a character string to copy from<br />
count &#8211; the number of characters to copy</p>
<h2>Return value</h2>
<p>dest </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Complexity</h2>
<p>Linear.</p>
<h2>See also</h2>
<p>assign assigns a character<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
