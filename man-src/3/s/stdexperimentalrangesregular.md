---
title: "stdexperimentalrangesregular(3)"
name: "stdexperimentalrangesregular"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesregular/"
---

std::experimental::ranges::Regular - std::experimental::ranges::Regular

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt;class T&gt;                                               (ranges TS)

concept bool Regular = Semiregular&lt;T&gt; &amp;&amp; EqualityComparable&lt;T&gt;;</code></pre> 
The Regular concept specifies that a type is regular, that is, it is copyable, default constructible, and equality comparable. It is satisfied by types that behave similarly to built-in types like int, and that are comparable with ==. 
