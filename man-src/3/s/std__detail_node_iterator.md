---
title: "std__detail_node_iterator(3)"
name: "std__detail_node_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_node_iterator/"
description: "std::__detail::_Node_iterator< _Value, __constant_iterators, __cache > –"
---

<p>std::__detail::_Node_iterator&lt; _Value, __constant_iterators, __cache &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Node_iterator_base&lt; _Value, __cache &gt;</code>.</p>
<h3>Public Types</h3>
<pre><code>typedef std::ptrdiff_t difference_type



typedef std::forward_iterator_tag iterator_category



using pointer = typename std::conditional&lt; __constant_iterators, const _Value *, _Value * &gt;::type



using reference = typename std::conditional&lt; __constant_iterators, const _Value &amp;, _Value &amp; &gt;::type



typedef _Value value_type



Public Member Functions</code></pre>
<p> <code>_Node_iterator</code> (__node_type *__p) </p>
<p> void <code>_M_incr</code> () </p>
<p> reference <code>operator*</code> () const </p>
<p> <code>_Node_iterator</code> &amp; <code>operator++</code> () </p>
<p> <code>_Node_iterator</code> <code>operator++</code> (int) </p>
<p> pointer <code>operator-&gt;</code> () const</p>
<h3>Public Attributes</h3>
<p>__node_type * <code>_M_cur</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Value, bool __constant_iterators, bool __cache&gt;struct std::__detail::_Node_iterator&lt; _Value, __constant_iterators, __cache &gt;</h3>
<p>Node iterators, used to iterate through all the hashtable. </p>
<p> Definition at line 231 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
