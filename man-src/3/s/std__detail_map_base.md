---
title: "std__detail_map_base(3)"
name: "std__detail_map_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_map_base/"
description: "std::__detail::_Map_base< _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys > –"
---

<p>std::__detail::_Map_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::_Hashtable&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;</code>, and <code>std::_Hashtable&lt; _Value, _Hash, _Pred, _Alloc &gt;</code>.</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _Alloc, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _RehashPolicy, typename _Traits, bool _Unique_keys = _Traits::__unique_keys::value&gt;struct std::__detail::_Map_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys &gt;</h3>
<p>Primary class template _Map_base. </p>
<p> If the hashtable has a value type of the form pair&lt;T1, T2&gt; and a key extraction policy (_ExtractKey) that returns the first part of the pair, the hashtable gets a mapped_type typedef. If it satisfies those criteria and also has unique keys, then it also gets an operator[]. </p>
<p> Definition at line 424 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
