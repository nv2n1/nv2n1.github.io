---
title: "stdsemiregular(3)"
name: "stdsemiregular"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsemiregular/"
---

std::Semiregular - std::Semiregular

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt;class T&gt;                                                       (since C++20)

concept Semiregular = std::Copyable&lt;T&gt; &amp;&amp; std::DefaultConstructible&lt;T&gt;;</code></pre> 
The Semiregular concept specifies that a type is both copyable and default constructible. It is satisfied by types that behave similarly to built-in types like int, except that they need not support comparison with ==. 
