---
title: "std_fwd_list_node_base(3)"
name: "std_fwd_list_node_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_fwd_list_node_base/"
description: "std::_Fwd_list_node_base –"
---

<p>std::_Fwd_list_node_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::_Fwd_list_node&lt; _Tp &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void _M_reverse_after () noexcept



_Fwd_list_node_base * _M_transfer_after (_Fwd_list_node_base *__begin, _Fwd_list_node_base *__end)



Public Attributes</code></pre>
<p> <code>_Fwd_list_node_base</code> * <code>_M_next</code></p>
<h2>Detailed Description</h2>
<p>A helper basic node class for forward_list. This is just a linked list with nothing inside it. There are purely list shuffling utility methods here. </p>
<p> Definition at line 49 of file forward_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
