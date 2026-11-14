---
title: "std_reference_wrapper_base(3)"
name: "std_reference_wrapper_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_reference_wrapper_base/"
description: "std::_Reference_wrapper_base< _Tp > –"
---

<p>std::_Reference_wrapper_base&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::_Reference_wrapper_base_impl&lt; __has_argument_type&lt; _Tp &gt;::value, __has_first_argument_type&lt; _Tp &gt;::value &amp;&amp;__has_second_argument_type&lt; _Tp &gt;::value, _Tp &gt;</code>.</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::_Reference_wrapper_base&lt; _Tp &gt;</h3>
<p>Derives from unary_function or binary_function when it can. Specializations handle all of the easy cases. The primary template determines what to do with a class type, which may derive from both unary_function and binary_function. </p>
<p> Definition at line 315 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
