---
title: "std__detail_equality(3)"
name: "std__detail_equality"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_equality/"
description: "std::__detail::_Equality< _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys > –"
---

<p>std::__detail::_Equality&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::_Hashtable&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;</code>, and <code>std::_Hashtable&lt; _Value, _Hash, _Pred, _Alloc &gt;</code>.</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _Alloc, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _RehashPolicy, typename _Traits, bool _Unique_keys = _Traits::__unique_keys::value&gt;struct std::__detail::_Equality&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, _Unique_keys &gt;</h3>
<p>Primary class template _Equality. </p>
<p> This is for implementing equality comparison for unordered containers, per N3068, by John Lakos and Pablo Halpern. Algorithmically, we follow closely the reference implementations therein. </p>
<p> Definition at line 1559 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
