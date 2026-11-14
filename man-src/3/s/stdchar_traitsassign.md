---
title: "stdchar_traitsassign(3)"
name: "stdchar_traitsassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitsassign/"
---

std::char_traits&lt;CharT&gt;::assign - std::char_traits&lt;CharT&gt;::assign

<h2>Synopsis</h2>

<pre><code>static void assign(char_type &amp;r, const char_type &amp;a);
(until C++ 11)

    static void assign(char_type &amp;r, const char_type &amp;a) noexcept;
(since C++ 11)(until C++ 17)

    static constexpr void assign(char_type &amp;r, const char_type &amp;a) noexcept;
(1)(since C++ 17)

    static char_type *assign(char_type *p, std::size_t count, char_type a);
(until C++ 20)

    static constexpr char_type *assign(char_type *p, (2)(since C++ 20)

                                                         std::size_t count,
                                       char_type a);</code></pre> 
Assigns a character. 
1) Assigns character a to character r. 
2) Assigns character a to each character in count characters in the character sequence pointed to by p. 

<h2>Parameters</h2>

a - character value to assign 
r - character to assign to 
p - pointer to a character sequence to assign to 
count - the length of the character sequence

<h2>Return value</h2>

1) <i>(none)</i> 
2) p 

<h2>Complexity</h2>

1) Constant. 
2) Linear in count
