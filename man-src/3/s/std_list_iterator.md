---
title: "std_list_iterator(3)"
name: "std_list_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_list_iterator/"
description: "std::_List_iterator< _Tp > –"
---

<p>std::_List_iterator&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef <code>_List_node</code>&lt; _Tp &gt; <code>_Node</code> </p>
<p> typedef <code>_List_iterator</code>&lt; _Tp &gt; <code>_Self</code> </p>
<p> typedef ptrdiff_t <code>difference_type</code> </p>
<p> typedef<br />
 <code>std::bidirectional_iterator_tag</code> <code>iterator_category</code>&quot; </p>
<p> typedef _Tp * <code>pointer</code> </p>
<p> typedef _Tp &amp; <code>reference</code> </p>
<p> typedef _Tp <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p><code>_List_iterator</code> (<code>__detail::_List_node_base</code> *__x) </p>
<p> bool <code>operator!=</code> (const <code>_Self</code> &amp;__x) const </p>
<p> reference <code>operator*</code> () const </p>
<p> <code>_Self</code> &amp; <code>operator++</code> () </p>
<p> <code>_Self</code> <code>operator++</code> (int) </p>
<p> <code>_Self</code> &amp; <code>operator&#8211;</code> () </p>
<p> <code>_Self</code> <code>operator&#8211;</code> (int) </p>
<p> pointer <code>operator-&gt;</code> () const </p>
<p> bool <code>operator==</code> (const <code>_Self</code> &amp;__x) const</p>
<h3>Public Attributes</h3>
<p><code>__detail::_List_node_base</code> * <code>_M_node</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::_List_iterator&lt; _Tp &gt;</h3>
<p>A list::iterator. </p>
<p> All the functions are op overloads. </p>
<p> Definition at line 125 of file stl_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
