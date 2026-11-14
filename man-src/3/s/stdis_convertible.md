---
title: "stdis_convertible(3)"
name: "stdis_convertible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_convertible/"
description: "std::is_convertible< _From, _To > –"
---

<p>std::is_convertible&lt; _From, _To &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::integral_constant&lt; bool, __is_convertible_helper&lt; _From, _To &gt;::value &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>integral_constant</code><br />
 &lt; bool, __v &gt; <code>type</code>&quot; </p>
<p> typedef bool <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>constexpr <code>operator value_type</code> ()</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr bool value</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _From, typename _To&gt;struct std::is_convertible&lt; _From, _To &gt;</h3>
<p>is_convertible </p>
<p> Definition at line 1317 of file type_traits.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
