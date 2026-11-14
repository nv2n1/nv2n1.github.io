---
title: "compose(3)"
name: "compose"
section: "3"
letter: "c"
url: "/docs/linux/man/3-compose/"
description: "ql/math/functional.hpp – functionals and combinators not included in the STL"
---

<h2 class="name">NAME</h2>
<p> ql/math/functional.hpp &#8211; functionals and combinators not included in the STL </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/types.hpp&gt;<br />
 #include &lt;cmath&gt;<br />
 #include &lt;functional&gt; </p>
<h3>Functions</h3>
<p> template&lt;class F , class R &gt; clipped_function&lt; F, R &gt; <code>clip</code> (const F &amp;f, const R &amp;r) </p>
<p> template&lt;class F , class G &gt; composed_function&lt; F, G &gt; <code>compose</code> (const F &amp;f, const G &amp;g) </p>
<p> template&lt;class F , class G , class H &gt; binary_compose3_function&lt; F, G, H &gt; <code>compose3</code> (const F &amp;f, const G &amp;g, const H &amp;h) </p>
<h2>Detailed Description</h2>
<p> functionals and combinators not included in the STL </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
