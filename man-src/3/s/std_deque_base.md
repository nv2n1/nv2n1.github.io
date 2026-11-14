---
title: "std_deque_base(3)"
name: "std_deque_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_deque_base/"
description: "std::_Deque_base< _Tp, _Alloc > –"
---

<p>std::_Deque_base&lt; _Tp, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::deque&lt; _Tp, _Alloc &gt;</code> [protected].</p>
<h3>Public Types</h3>
<p>typedef _Alloc <code>allocator_type</code> </p>
<p> typedef <code>_Deque_iterator</code>&lt; _Tp,<br />
 const _Tp &amp;, const _Tp * &gt; <code>const_iterator</code>&quot; </p>
<p> typedef <code>_Deque_iterator</code>&lt; _Tp,<br />
 _Tp &amp;, _Tp * &gt; <code>iterator</code>&quot;</p>
<h3>Public Member Functions</h3>
<p><code>_Deque_base</code> (size_t __num_elements) </p>
<p> <code>_Deque_base</code> (const allocator_type &amp;__a, size_t __num_elements) </p>
<p> <code>_Deque_base</code> (const allocator_type &amp;__a) </p>
<p> <code>_Deque_base</code> (<code>_Deque_base</code> &amp;&amp;__x) </p>
<p> allocator_type <code>get_allocator</code> () const noexcept</p>
<h3>Protected Types</h3>
<p>enum { <code>_S_initial_map_size</code> } </p>
<p> typedef _Alloc::template<br />
 rebind&lt; _Tp * &gt;::other <code>_Map_alloc_type</code>&quot; </p>
<p> typedef _Alloc::template<br />
 rebind&lt; _Tp &gt;::other <code>_Tp_alloc_type</code>&quot;</p>
<h3>Protected Member Functions</h3>
<p>_Tp ** <code>_M_allocate_map</code> (size_t __n) </p>
<p> _Tp * <code>_M_allocate_node</code> () </p>
<p> void <code>_M_create_nodes</code> (_Tp **__nstart, _Tp **__nfinish) </p>
<p> void <code>_M_deallocate_map</code> (_Tp **__p, size_t __n) </p>
<p> void <code>_M_deallocate_node</code> (_Tp *__p) </p>
<p> void <code>_M_destroy_nodes</code> (_Tp **__nstart, _Tp **__nfinish) </p>
<p> _Map_alloc_type <code>_M_get_map_allocator</code> () const noexcept </p>
<p> _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () noexcept </p>
<p> const _Tp_alloc_type &amp; <code>_M_get_Tp_allocator</code> () const noexcept </p>
<p> void <code>_M_initialize_map</code> (size_t)</p>
<h3>Protected Attributes</h3>
<p>_Deque_impl <code>_M_impl</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Alloc&gt;class std::_Deque_base&lt; _Tp, _Alloc &gt;</h3>
<p>Deque base class. This class provides the unified face for deque&#8217;s allocation. This class&#8217;s constructor and destructor allocate and deallocate (but do not initialize) storage. This makes exception safety easier. </p>
<p> Nothing in this class ever constructs or destroys an actual Tp element. (Deque handles that itself.) Only/All memory management is performed here. </p>
<p> Definition at line 439 of file stl_deque.h.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;typename _Tp , typename _Alloc &gt; void <code>std::_Deque_base</code>&lt; _Tp, _Alloc &gt;::_M_initialize_map (size_t__num_elements) [protected]</h3>
<p>Layout storage. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__num_elements</i> The count of T&#8217;s for which to allocate space at first.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Nothing.</dl>
<p> The initial underlying memory layout is a bit complicated&#8230; </p>
<p> Definition at line 582 of file stl_deque.h. </p>
<p> References std::max().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
