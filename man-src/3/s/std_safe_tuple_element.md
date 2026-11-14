---
title: "std_safe_tuple_element(3)"
name: "std_safe_tuple_element"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_safe_tuple_element/"
description: "std::_Safe_tuple_element< __i, _Tuple > –"
---

<p>std::_Safe_tuple_element&lt; __i, _Tuple &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::_Safe_tuple_element_impl&lt; __i, _Tuple,(__i&lt; tuple_size&lt; _Tuple &gt;::value)&gt;</code>.</p>
<h2>Detailed Description</h2>
<h3>template&lt;std::size_t __i, typename _Tuple&gt;struct std::_Safe_tuple_element&lt; __i, _Tuple &gt;</h3>
<p>Like tuple_element, but returns _No_tuple_element when tuple_element would return an error. </p>
<p> Definition at line 1084 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
