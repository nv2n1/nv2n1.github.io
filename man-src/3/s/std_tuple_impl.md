---
title: "std_tuple_impl(3)"
name: "std_tuple_impl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_tuple_impl/"
---

std::_Tuple_impl&lt; _Idx, _Elements &gt; -

<h2>Synopsis</h2>



<h2>Detailed Description</h2>

<h3>template&lt;std::size_t _Idx, typename... _Elements&gt;struct std::_Tuple_impl&lt; _Idx, _Elements &gt;</h3>

Contains the actual implementation of the tuple template, stored as a recursive inheritance hierarchy from the first element (most derived class) to the last (least derived class). The Idx parameter gives the 0-based index of the element stored at this point in the hierarchy; we use it to implement a constant-time get() operation. 

 Definition at line 186 of file tuple.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
