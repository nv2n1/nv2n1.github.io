---
title: "std_fwd_list_node(3)"
name: "std_fwd_list_node"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_fwd_list_node/"
description: "std::_Fwd_list_node< _Tp > –"
---

<p>std::_Fwd_list_node&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::_Fwd_list_node_base</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void _M_reverse_after () noexcept



_Fwd_list_node_base * _M_transfer_after (_Fwd_list_node_base *__begin, _Fwd_list_node_base *__end)



_Tp * _M_valptr () noexcept



const _Tp * _M_valptr () const noexcept



Public Attributes
_Fwd_list_node_base * _M_next



aligned_storage&lt; sizeof(_Tp),


alignment_of&lt; _Tp &gt;::value &gt;

::type _M_storage&quot;</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::_Fwd_list_node&lt; _Tp &gt;</h3>
<p>A helper node class for forward_list. This is just a linked list with uninitialized storage for a data value in each node. There is a sorting utility method. </p>
<p> Definition at line 94 of file forward_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
