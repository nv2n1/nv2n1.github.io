---
title: "std__detail_rehash_base(3)"
name: "std__detail_rehash_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_rehash_base/"
description: "std::__detail::_Rehash_base< _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits > –"
---

<p>std::__detail::_Rehash_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::_Hashtable&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;</code>, <code>std::_Hashtable&lt; _Value, _Hash, _Pred, _Alloc &gt;</code>, and <code>std::_Hashtable&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>.</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _Alloc, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _RehashPolicy, typename _Traits&gt;struct std::__detail::_Rehash_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</h3>
<p>Primary class template _Rehash_base. </p>
<p> Give hashtable the max_load_factor functions and reserve iff the rehash policy is _Prime_rehash_policy. </p>
<p> Definition at line 788 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
