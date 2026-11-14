---
title: "std__detail_before_begin(3)"
name: "std__detail_before_begin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_before_begin/"
description: "std::__detail::_Before_begin< _NodeAlloc > –"
---

<p>std::__detail::_Before_begin&lt; _NodeAlloc &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits _NodeAlloc.</p>
<h3>Public Member Functions</h3>
<pre><code>_Before_begin (const _Before_begin &amp;)=default



_Before_begin (_Before_begin &amp;&amp;)=default



template&lt;typename _Alloc &gt; _Before_begin (_Alloc &amp;&amp;__a)



Public Attributes</code></pre>
<p> <code>_Hash_node_base</code> <code>_M_node</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _NodeAlloc&gt;struct std::__detail::_Before_begin&lt; _NodeAlloc &gt;</h3>
<p>This type is to combine a _Hash_node_base instance with an allocator instance through inheritance to benefit from EBO when possible. </p>
<p> Definition at line 1652 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
