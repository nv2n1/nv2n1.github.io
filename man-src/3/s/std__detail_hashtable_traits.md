---
title: "std__detail_hashtable_traits(3)"
name: "std__detail_hashtable_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_hashtable_traits/"
description: "std::__detail::_Hashtable_traits< _Cache_hash_code, _Constant_iterators, _Unique_keys > –"
---

<p>std::__detail::_Hashtable_traits&lt; _Cache_hash_code, _Constant_iterators, _Unique_keys &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<pre><code>template&lt;bool _Cond&gt; using __bool_constant = integral_constant&lt; bool, _Cond &gt;



using __constant_iterators = __bool_constant&lt; _Constant_iterators &gt;



using __hash_cached = __bool_constant&lt; _Cache_hash_code &gt;



using __unique_keys = __bool_constant&lt; _Unique_keys &gt;</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;bool _Cache_hash_code, bool _Constant_iterators, bool _Unique_keys&gt;struct std::__detail::_Hashtable_traits&lt; _Cache_hash_code, _Constant_iterators, _Unique_keys &gt;</h3>
<p>struct _Hashtable_traits </p>
<p> Important traits for hash tables. </p>
<p> <code>Template Parameters:</code></p>
<dl>
<dd><i>_Cache_hash_code</i> Boolean value. True if the value of the hash function is stored along with the value. This is a time-space tradeoff. Storing it may improve lookup speed by reducing the number of times we need to call the _Equal function.<br />
 <i>_Constant_iterators</i> Boolean value. True if iterator and const_iterator are both constant iterator types. This is true for unordered_set and unordered_multiset, false for unordered_map and unordered_multimap.<br />
 <i>_Unique_keys</i> Boolean value. True if the return value of _Hashtable::count(k) is always at most one, false if it may be an arbitrary number. This is true for unordered_set and unordered_map, false for unordered_multiset and unordered_multimap.</dl>
<p> Definition at line 131 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
