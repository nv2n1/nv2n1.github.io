---
title: "std__detail_list_node_base(3)"
name: "std__detail_list_node_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_list_node_base/"
description: "std::__detail::_List_node_base –"
---

<p>std::__detail::_List_node_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::_List_node&lt; _Tp &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void _M_hook (_List_node_base *const __position) noexcept



void _M_reverse () noexcept



void _M_transfer (_List_node_base *const __first, _List_node_base *const __last) noexcept



void _M_unhook () noexcept



Static Public Member Functions
static void swap (_List_node_base &amp;__x, _List_node_base &amp;__y) noexcept



Public Attributes</code></pre>
<p> <code>_List_node_base</code> * <code>_M_next</code> </p>
<p> <code>_List_node_base</code> * <code>_M_prev</code></p>
<h2>Detailed Description</h2>
<p>Common part of a node in the list. </p>
<p> Definition at line 77 of file stl_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
