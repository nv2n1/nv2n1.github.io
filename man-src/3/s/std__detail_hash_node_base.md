---
title: "std__detail_hash_node_base(3)"
name: "std__detail_hash_node_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_hash_node_base/"
description: "std::__detail::_Hash_node_base –"
---

<p>std::__detail::_Hash_node_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::__detail::_Hash_node&lt; _Value, false &gt;</code>, and <code>std::__detail::_Hash_node&lt; _Value, true &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>_Hash_node_base</code> (<code>_Hash_node_base</code> *__next)</p>
<h3>Public Attributes</h3>
<p><code>_Hash_node_base</code> * <code>_M_nxt</code></p>
<h2>Detailed Description</h2>
<p>struct _Hash_node_base </p>
<p> Nodes, used to wrap elements stored in the hash table. A policy template parameter of class template _Hashtable controls whether nodes also store a hash code. In some cases (e.g. strings) this may be a performance win. </p>
<p> Definition at line 149 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
