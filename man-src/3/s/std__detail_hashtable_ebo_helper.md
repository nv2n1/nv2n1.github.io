---
title: "std__detail_hashtable_ebo_helper(3)"
name: "std__detail_hashtable_ebo_helper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_hashtable_ebo_helper/"
---

std::__detail::_Hashtable_ebo_helper&lt; _Nm, _Tp, __use_ebo &gt; -

<h2>Synopsis</h2>



<h2>Detailed Description</h2>

<h3>template&lt;int _Nm, typename _Tp, bool __use_ebo = !__is_final(_Tp) &amp;&amp; __is_empty(_Tp)&gt;struct std::__detail::_Hashtable_ebo_helper&lt; _Nm, _Tp, __use_ebo &gt;</h3>

Primary class template _Hashtable_ebo_helper. 

 Helper class using EBO when it is not forbidden, type is not final, and when it worth it, type is empty. 

 Definition at line 831 of file hashtable_policy.h.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
