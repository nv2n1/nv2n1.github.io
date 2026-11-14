---
title: "stdis_default_constructible(3)"
name: "stdis_default_constructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_default_constructible/"
description: "std::is_default_constructible< _Tp > –"
---

<p>std::is_default_constructible&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::integral_constant&lt; bool,(__is_default_constructible_safe&lt; _Tp &gt;::value)&gt;</code>. Inherited by std::__is_constructible_impl&lt; _Tp &gt;.</p>
<h3>Public Types</h3>
<p>typedef <code>integral_constant</code><br />
 &lt; bool, __v &gt; <code>type</code>&quot; </p>
<p> typedef bool <code>value_type</code></p>
<h3>Public Member Functions</h3>
<p>constexpr <code>operator value_type</code> ()</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr bool value</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;struct std::is_default_constructible&lt; _Tp &gt;</h3>
<p>is_default_constructible </p>
<p> Definition at line 748 of file type_traits.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
