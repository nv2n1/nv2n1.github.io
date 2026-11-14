---
title: "std_function_base(3)"
name: "std_function_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_function_base/"
description: "std::_Function_base –"
---

<p>std::_Function_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::function&lt; _Res(_ArgTypes&#8230;)&gt;</code> [private].</p>
<h3>Public Types</h3>
<p>typedef bool(* <code>_Manager_type</code> )(_Any_data &amp;, const _Any_data &amp;, _Manager_operation)</p>
<h3>Public Member Functions</h3>
<p>bool <code>_M_empty</code> () const</p>
<h3>Public Attributes</h3>
<p>_Any_data <code>_M_functor</code> </p>
<p> _Manager_type <code>_M_manager</code></p>
<h3>Static Public Attributes</h3>
<pre><code>static const std::size_t _M_max_align



static const std::size_t _M_max_size</code></pre>
<h2>Detailed Description</h2>
<p>Base class of all polymorphic function object wrappers. </p>
<p> Definition at line 1869 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
