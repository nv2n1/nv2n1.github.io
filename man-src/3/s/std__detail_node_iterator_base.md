---
title: "std__detail_node_iterator_base(3)"
name: "std__detail_node_iterator_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_node_iterator_base/"
description: "std::__detail::_Node_iterator_base< _Value, _Cache_hash_code > –"
---

<p>std::__detail::_Node_iterator_base&lt; _Value, _Cache_hash_code &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<pre><code>using __node_type = _Hash_node&lt; _Value, _Cache_hash_code &gt;



Public Member Functions</code></pre>
<p> <code>_Node_iterator_base</code> (<code>__node_type</code> *__p) </p>
<p> void <code>_M_incr</code> ()</p>
<h3>Public Attributes</h3>
<p><code>__node_type</code> * <code>_M_cur</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Value, bool _Cache_hash_code&gt;struct std::__detail::_Node_iterator_base&lt; _Value, _Cache_hash_code &gt;</h3>
<p>Base class for node iterators. </p>
<p> Definition at line 203 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
