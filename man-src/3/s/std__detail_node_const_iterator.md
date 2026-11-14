---
title: "std__detail_node_const_iterator(3)"
name: "std__detail_node_const_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_node_const_iterator/"
description: "std::__detail::_Node_const_iterator< _Value, __constant_iterators, __cache > –"
---

<p>std::__detail::_Node_const_iterator&lt; _Value, __constant_iterators, __cache &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Node_iterator_base&lt; _Value, __cache &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef std::ptrdiff_t <code>difference_type</code> </p>
<p> typedef <code>std::forward_iterator_tag</code> <code>iterator_category</code> </p>
<p> typedef const _Value * <code>pointer</code> </p>
<p> typedef const _Value &amp; <code>reference</code> </p>
<p> typedef _Value <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Node_const_iterator</code> (__node_type *__p) </p>
<p> <code>_Node_const_iterator</code> (const <code>_Node_iterator</code>&lt; _Value, __constant_iterators, __cache &gt; &amp;__x) </p>
<p> void <code>_M_incr</code> () </p>
<p> reference <code>operator*</code> () const </p>
<p> <code>_Node_const_iterator</code> &amp; <code>operator++</code> () </p>
<p> <code>_Node_const_iterator</code> <code>operator++</code> (int) </p>
<p> pointer <code>operator-&gt;</code> () const</p>
<h3>Public Attributes</h3>
<p>__node_type * <code>_M_cur</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Value, bool __constant_iterators, bool __cache&gt;struct std::__detail::_Node_const_iterator&lt; _Value, __constant_iterators, __cache &gt;</h3>
<p>Node const_iterators, used to iterate through all the hashtable. </p>
<p> Definition at line 282 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
