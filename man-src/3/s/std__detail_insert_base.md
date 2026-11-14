---
title: "std__detail_insert_base(3)"
name: "std__detail_insert_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_insert_base/"
description: "std::__detail::_Insert_base< _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits > –"
---

<p>std::__detail::_Insert_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::__detail::_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, false, _Unique_keys &gt;</code>, <code>std::__detail::_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true, false &gt;</code>, and <code>std::__detail::_Insert&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits, true, true &gt;</code>.</p>
<h3>Public Types</h3>
<pre><code>using __hashtable = _Hashtable&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;



using __hashtable_base = _Hashtable_base&lt; _Key, _Value, _ExtractKey, _Equal, _H1, _H2, _Hash, _Traits &gt;



using __iconv_type = typename __hashtable_base::__iconv_type



using __ireturn_type = typename __hashtable_base::__ireturn_type



using __unique_keys = typename __hashtable_base::__unique_keys



using const_iterator = typename __hashtable_base::const_iterator



using iterator = typename __hashtable_base::iterator



using size_type = typename __hashtable_base::size_type



using value_type = typename __hashtable_base::value_type



Public Member Functions</code></pre>
<p> <code>__hashtable</code> &amp; <code>_M_conjure_hashtable</code> () </p>
<p> __ireturn_type <code>insert</code> (const value_type &amp;__v) </p>
<p> iterator <code>insert</code> (const_iterator, const value_type &amp;__v) </p>
<p> void <code>insert</code> (<code>initializer_list</code>&lt; value_type &gt; __l) </p>
<p> template&lt;typename _InputIterator &gt; void <code>insert</code> (_InputIterator __first, _InputIterator __last)</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Key, typename _Value, typename _Alloc, typename _ExtractKey, typename _Equal, typename _H1, typename _H2, typename _Hash, typename _RehashPolicy, typename _Traits&gt;struct std::__detail::_Insert_base&lt; _Key, _Value, _Alloc, _ExtractKey, _Equal, _H1, _H2, _Hash, _RehashPolicy, _Traits &gt;</h3>
<p>Primary class template _Insert_base. </p>
<p> insert member functions appropriate to all _Hashtables. </p>
<p> Definition at line 577 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
