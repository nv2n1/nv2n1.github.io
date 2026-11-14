---
title: "std_vector_base(3)"
name: "std_vector_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_vector_base/"
description: "std::_Vector_base< _Tp, _Alloc > –"
---

<p>std::_Vector_base&lt; _Tp, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::vector&lt; _Tp, _Alloc &gt;</code> [protected].</p>
<h3>Public Types</h3>
<p>typedef<br />
 <code>__gnu_cxx::__alloc_traits</code><br />
 &lt; _Alloc &gt;::template rebind<br />
 &lt; _Tp &gt;::other <code>_Tp_alloc_type</code>&quot; </p>
<p> typedef _Alloc <code>allocator_type</code> </p>
<p> typedef<br />
 <code>__gnu_cxx::__alloc_traits</code><br />
 &lt; _Tp_alloc_type &gt;::pointer <code>pointer</code>&quot;</p>
<h3>Public Member Functions</h3>
<p><code>_Vector_base</code> (const allocator_type &amp;__a) </p>
<p> <code>_Vector_base</code> (size_t __n) </p>
<p> <code>_Vector_base</code> (size_t __n, const allocator_type &amp;__a) </p>
<p> <code>_Vector_base</code> (_Tp_alloc_type &amp;&amp;__a) </p>
<p> <code>_Vector_base</code> (<code>_Vector_base</code> &amp;&amp;__x) </p>
<p> <code>_Vector_base</code> (<code>_Vector_base</code> &amp;&amp;__x, const allocator_type &amp;__a) </p>
<p> pointer <code>_M_allocate</code> (size_t __n) </p>
<p> void <code>_M_deallocate</code> (pointer __p, size_t __n) </p>
<p> _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () noexcept </p>
<p> const _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () const noexcept </p>
<p> allocator_type <code>get_allocator</code> () const noexcept</p>
<h3>Public Attributes</h3>
<p>_Vector_impl <code>_M_impl</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Alloc&gt;struct std::_Vector_base&lt; _Tp, _Alloc &gt;</h3>
<p>See bits/stl_deque.h&#8217;s _Deque_base for an explanation. </p>
<p> Definition at line 72 of file stl_vector.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
