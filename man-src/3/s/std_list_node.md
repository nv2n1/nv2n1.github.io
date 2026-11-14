---
title: "std_list_node(3)"
name: "std_list_node"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_list_node/"
description: "std::_List_node< _Tp > –"
---

<p>std::_List_node&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::__detail::_List_node_base</code>.</p>
<h3>Public Member Functions</h3>
<p>template&lt;typename&#8230; _Args&gt; <code>_List_node</code> (_Args &amp;&amp;&#8230;__args) </p>
<p> void <code>_M_hook</code> (_List_node_base *const __position) noexcept </p>
<p> void <code>_M_reverse</code> () noexcept </p>
<p> void <code>_M_transfer</code> (_List_node_base *const __first, _List_node_base *const __last) noexcept </p>
<p> void <code>_M_unhook</code> () noexcept</p>
<h3>Static Public Member Functions</h3>
<pre><code>static void swap (_List_node_base &amp;__x, _List_node_base &amp;__y) noexcept



Public Attributes</code></pre>
<p> _Tp <code>_M_data</code> </p>
<p> _List_node_base * <code>_M_next</code> </p>
<p> _List_node_base * <code>_M_prev</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::_List_node&lt; _Tp &gt;</h3>
<p>An actual node in the list. </p>
<p> Definition at line 106 of file stl_list.h.</p>
<h2>Member Data Documentation</h2>
<h3>template&lt;typename _Tp&gt; _Tp <code>std::_List_node</code>&lt; _Tp &gt;::_M_data</h3>
<p>&lt; User&#8217;s data. </p>
<p> Definition at line 109 of file stl_list.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
