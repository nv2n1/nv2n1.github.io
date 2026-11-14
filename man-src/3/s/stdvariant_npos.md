---
title: "stdvariant_npos(3)"
name: "stdvariant_npos"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariant_npos/"
---

std::variant_npos - std::variant_npos

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;variant&gt;

inline constexpr std::size_t variant_npos = -1;  (since C++17)</code></pre> 
This is a special value equal to the largest value representable by the type std::size_t, used as the return type of index() when valueless_by_exception() is true 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the zero-based index of the alternative held by the variant 
index <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the variant is in the invalid state 
valueless_by_exception <i>(public member function)</i> 
