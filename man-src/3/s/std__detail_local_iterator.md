---
title: "std__detail_local_iterator(3)"
name: "std__detail_local_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_local_iterator/"
description: "std::__detail::_Local_iterator< _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __constant_iterators, __cache > –"
---

<p>std::__detail::_Local_iterator&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __constant_iterators, __cache &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Local_iterator_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef std::ptrdiff_t <code>difference_type</code> </p>
<p> typedef <code>std::forward_iterator_tag</code> <code>iterator_category</code> </p>
<p> typedef <code>std::conditional</code><br />
 &lt; __constant_iterators, const<br />
 _Value *, _Value * &gt;::type <code>pointer</code>&quot; </p>
<p> typedef <code>std::conditional</code><br />
 &lt; __constant_iterators, const<br />
 _Value &amp;, _Value &amp; &gt;::type <code>reference</code>&quot; </p>
<p> typedef _Value <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_Local_iterator</code> (const __hash_code_base &amp;__base, <code>_Hash_node</code>&lt; _Value, __cache &gt; *__p, std::size_t __bkt, std::size_t __bkt_count) </p>
<p> reference <code>operator*</code> () const </p>
<p> <code>_Local_iterator</code> &amp; <code>operator++</code> () </p>
<p> <code>_Local_iterator</code> <code>operator++</code> (int) </p>
<p> pointer <code>operator-&gt;</code> () const</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _ExtractKey, typename _H1, typename _H2, typename _Hash, bool __constant_iterators, bool __cache&gt;struct std::__detail::_Local_iterator&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __constant_iterators, __cache &gt;</h3>
<p>local iterators </p>
<p> Definition at line 1279 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
