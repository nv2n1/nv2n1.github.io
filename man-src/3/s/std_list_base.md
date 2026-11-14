---
title: "std_list_base(3)"
name: "std_list_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_list_base/"
description: "std::_List_base< _Tp, _Alloc > –"
---

<p>std::_List_base&lt; _Tp, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::list&lt; _Tp, _Alloc &gt;</code> [protected].</p>
<h3>Public Types</h3>
<p>typedef _Alloc <code>allocator_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_List_base</code> (const _Node_alloc_type &amp;__a) </p>
<p> <code>_List_base</code> (<code>_List_base</code> &amp;&amp;__x) </p>
<p> void <code>_M_clear</code> () </p>
<p> _Node_alloc_type &amp; <code>_M_get_Node_allocator</code> () noexcept </p>
<p> const _Node_alloc_type &amp; <code>_M_get_Node_allocator</code> () const noexcept </p>
<p> _Tp_alloc_type <code>_M_get_Tp_allocator</code> () const noexcept </p>
<p> void <code>_M_init</code> () </p>
<p> allocator_type <code>get_allocator</code> () const noexcept</p>
<h3>Protected Types</h3>
<p>typedef _Alloc::template<br />
 rebind&lt; <code>_List_node</code>&lt; _Tp &gt; </p>
<p>&nbsp;<wbr>&gt;::other&nbsp;<wbr><code>_Node_alloc_type</code>&quot; </p>
<p> typedef _Alloc::template<br />
 rebind&lt; _Tp &gt;::other <code>_Tp_alloc_type</code>&quot;</p>
<h3>Protected Member Functions</h3>
<p><code>_List_node</code>&lt; _Tp &gt; * <code>_M_get_node</code> () </p>
<p> void <code>_M_put_node</code> (<code>_List_node</code>&lt; _Tp &gt; *__p)</p>
<h3>Protected Attributes</h3>
<p>_List_impl <code>_M_impl</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Alloc&gt;class std::_List_base&lt; _Tp, _Alloc &gt;</h3>
<p>See bits/stl_deque.h&#8217;s _Deque_base for an explanation. </p>
<p> Definition at line 289 of file stl_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
