---
title: "std__has_iterator_category_helper(3)"
name: "std__has_iterator_category_helper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__has_iterator_category_helper/"
description: "std::__has_iterator_category_helper< _Tp > –"
---

<p>std::__has_iterator_category_helper&lt; _Tp &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits std::__sfinae_types.</p>
<h3>Static Public Attributes</h3>
<pre><code>static constexpr bool value



Private Types</code></pre>
<p> typedef char <code>__one</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp&gt;class std::__has_iterator_category_helper&lt; _Tp &gt;</h3>
<p>Traits class for iterators. </p>
<p> This class does nothing but define nested typedefs. The general version simply <i>forwards</i> the nested typedefs from the Iterator argument. Specialized versions for pointers and pointers-to-const provide tighter, more correct semantics. </p>
<p> Definition at line 142 of file stl_iterator_base_types.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
