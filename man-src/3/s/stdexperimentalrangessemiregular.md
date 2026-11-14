---
title: "stdexperimentalrangessemiregular(3)"
name: "stdexperimentalrangessemiregular"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessemiregular/"
---

std::experimental::ranges::Semiregular - std::experimental::ranges::Semiregular

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt;class T&gt;                                                  (ranges TS)

concept bool Semiregular = Copyable&lt;T&gt; &amp;&amp; DefaultConstructible&lt;T&gt;;</code></pre> 
The Semiregular concept specifies that a type is both copyable and default constructible. It is satisfied by types that behave similarly to built-in types like int, except that they need not support comparison with ==. 
