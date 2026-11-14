---
title: "std__detail_hashtable_base(3)"
name: "std__detail_hashtable_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_hashtable_base/"
description: "std::__detail::_Hashtable_base< _Key, _Value, _ExtractKey, _Equal, _H1, _H2, _Hash, _Traits > –"
---

<p>std::__detail::_Hashtable_base&lt; _Key, _Value, _ExtractKey, _Equal, _H1, _H2, _Hash, _Traits &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, _Traits::__hash_cached::value &gt;</code>, and <code>std::__detail::_Hashtable_ebo_helper&lt; 0, _Equal &gt;</code>. Inherited by <code>std::_Hashtable&lt; _Key, _Tp, _Hash, _Pred, _Alloc &gt;</code>, <code>std::_Hashtable&lt; _Value, _Hash, _Pred, _Alloc &gt;</code>, and <code>std::_Hashtable&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</code>.</p>
<h3>Public Types</h3>
<pre><code>using __constant_iterators = typename __traits_type::__constant_iterators



using __hash_cached = typename __traits_type::__hash_cached



using __hash_code = typename __hash_code_base::__hash_code



using __hash_code_base = _Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __hash_cached::value &gt;



using __iconv_type = typename std::conditional&lt; __unique_keys::value, _Select1st, _Identity &gt;::type



using __ireturn_type = typename std::conditional&lt; __unique_keys::value, std::pair&lt; iterator, bool &gt;, iterator &gt;::type



using __node_type = typename __hash_code_base::__node_type



using __traits_type = _Traits



using __unique_keys = typename __traits_type::__unique_keys



using const_iterator = __detail::_Node_const_iterator&lt; value_type, __constant_iterators::value, __hash_cached::value &gt;



using const_local_iterator = __detail::_Local_const_iterator&lt; key_type, value_type, _ExtractKey, _H1, _H2, _Hash, __constant_iterators::value, __hash_cached::value &gt;



typedef std::ptrdiff_t difference_type



using iterator = __detail::_Node_iterator&lt; value_type, __constant_iterators::value, __hash_cached::value &gt;



typedef _Equal key_equal



typedef _Key key_type



using local_iterator = __detail::_Local_iterator&lt; key_type, value_type, _ExtractKey, _H1, _H2, _Hash, __constant_iterators::value, __hash_cached::value &gt;



typedef std::size_t size_type



typedef _Value value_type



Protected Types
using __bucket_type = __node_base *



using __node_base = __detail::_Hash_node_base



Protected Member Functions</code></pre>
<p> <code>_Hashtable_base</code> (const _ExtractKey &amp;__ex, const _H1 &amp;__h1, const _H2 &amp;__h2, const _Hash &amp;__hash, const _Equal &amp;__eq) </p>
<p> const _Equal &amp; <code>_M_eq</code> () const </p>
<p> _Equal &amp; <code>_M_eq</code> () </p>
<p> bool <code>_M_equals</code> (const _Key &amp;__k, __hash_code __c, __node_type *__n) const </p>
<p> void <code>_M_swap</code> (<code>_Hashtable_base</code> &amp;__x)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _Traits&gt;struct std::__detail::_Hashtable_base&lt; _Key, _Value, _ExtractKey, _Equal, _H1, _H2, _Hash, _Traits &gt;</h3>
<p>Primary class template _Hashtable_base. </p>
<p> Helper class adding management of _Equal functor to _Hash_code_base type. </p>
<p> Base class templates are:</p>
<dl>
<dt>&bull;</p>
<dd>__detail::_Hash_code_base</p>
<dt>&bull;</p>
<dd>__detail::_Hashtable_ebo_helper</dl>
<p> Definition at line 58 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
