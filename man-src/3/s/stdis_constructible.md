---
title: "stdis_constructible(3)"
name: "stdis_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_constructible/"
description: "std::is_constructible< _Tp, _Args > –"
---

<p>std::is_constructible&lt; _Tp, _Args &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::integral_constant&lt; bool,(__is_constructible_impl&lt; _Tp, _Args&#8230;&gt;::value)&gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>integral_constant</code><br />
 &lt; bool, __v &gt; <code>type</code>&quot; </p>
<p> typedef bool <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>constexpr <code>operator value_type</code> ()</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr bool value</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp, typename&#8230; _Args&gt;struct std::is_constructible&lt; _Tp, _Args &gt;</h3>
<p>is_constructible </p>
<p> Definition at line 955 of file type_traits.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
