---
title: "std_fwd_list_base(3)"
name: "std_fwd_list_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_fwd_list_base/"
description: "std::_Fwd_list_base< _Tp, _Alloc > –"
---

<p>std::_Fwd_list_base&lt; _Tp, _Alloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::forward_list&lt; _Tp, _Alloc &gt;</code> [private].</p>
<h3>Public Types</h3>
<p>typedef <code>_Fwd_list_node</code>&lt; _Tp &gt; <code>_Node</code> </p>
<p> typedef<br />
 <code>_Fwd_list_const_iterator</code>&lt; _Tp &gt; <code>const_iterator</code>&quot; </p>
<p> typedef <code>_Fwd_list_iterator</code>&lt; _Tp &gt; <code>iterator</code></p>
<h3>Public Member Functions</h3>
<p><code>_Fwd_list_base</code> (const _Node_alloc_type &amp;__a) </p>
<p> <code>_Fwd_list_base</code> (<code>_Fwd_list_base</code> &amp;&amp;__lst, const _Node_alloc_type &amp;__a) </p>
<p> <code>_Fwd_list_base</code> (<code>_Fwd_list_base</code> &amp;&amp;__lst) </p>
<p> _Node_alloc_type &amp; <code>_M_get_Node_allocator</code> () noexcept </p>
<p> const _Node_alloc_type &amp; <code>_M_get_Node_allocator</code> () const noexcept</p>
<h3>Protected Types</h3>
<p>typedef<br />
 <code>__gnu_cxx::__alloc_traits</code><br />
 &lt; _Alloc &gt; <code>_Alloc_traits</code>&quot; </p>
<p> typedef<br />
 <code>__gnu_cxx::__alloc_traits</code><br />
 &lt; _Node_alloc_type &gt; <code>_Node_alloc_traits</code>&quot; </p>
<p> typedef<br />
 _Alloc_traits::template rebind<br />
 &lt; <code>_Fwd_list_node</code>&lt; _Tp &gt; </p>
<p>&nbsp;<wbr>&gt;::other&nbsp;<wbr><code>_Node_alloc_type</code>&quot; </p>
<p> typedef<br />
 _Alloc_traits::template rebind<br />
 &lt; _Tp &gt;::other <code>_Tp_alloc_type</code>&quot;</p>
<h3>Protected Member Functions</h3>
<p>template&lt;typename&#8230; _Args&gt; <code>_Node</code> * <code>_M_create_node</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> <code>_Fwd_list_node_base</code> * <code>_M_erase_after</code> (<code>_Fwd_list_node_base</code> *__pos) </p>
<p> <code>_Fwd_list_node_base</code> * <code>_M_erase_after</code> (<code>_Fwd_list_node_base</code> *__pos, <code>_Fwd_list_node_base</code> *__last) </p>
<p> <code>_Node</code> * <code>_M_get_node</code> () </p>
<p> template&lt;typename&#8230; _Args&gt; <code>_Fwd_list_node_base</code> * <code>_M_insert_after</code> (<code>const_iterator</code> __pos, _Args &amp;&amp;&#8230;__args) </p>
<p> void <code>_M_put_node</code> (<code>_Node</code> *__p)</p>
<h3>Protected Attributes</h3>
<p>_Fwd_list_impl <code>_M_impl</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename _Alloc&gt;struct std::_Fwd_list_base&lt; _Tp, _Alloc &gt;</h3>
<p>Base class for forward_list. </p>
<p> Definition at line 275 of file forward_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
