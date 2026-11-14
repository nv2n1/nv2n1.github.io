---
title: "std_maybe_wrap_member_pointer(3)"
name: "std_maybe_wrap_member_pointer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_maybe_wrap_member_pointer/"
description: "std::_Maybe_wrap_member_pointer< _Tp > –"
---

<p>std::_Maybe_wrap_member_pointer&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef _Tp <code>type</code></p>
<h3>Static Public Member Functions</h3>
<pre><code>static const _Tp &amp; __do_wrap (const _Tp &amp;__x)



static _Tp &amp;&amp; __do_wrap (_Tp &amp;&amp;__x)</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::_Maybe_wrap_member_pointer&lt; _Tp &gt;</h3>
<p>Maps member pointers into instances of _Mem_fn but leaves all other function objects untouched. Used by tr1::bind(). The primary template handles the non&#8211;member-pointer case. </p>
<p> Definition at line 1223 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
