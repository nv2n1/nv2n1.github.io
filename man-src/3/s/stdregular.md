---
title: "stdregular(3)"
name: "stdregular"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregular/"
---

std::Regular - std::Regular

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt;class T&gt;                                                    (since C++20)

concept Regular = std::Semiregular&lt;T&gt; &amp;&amp; std::EqualityComparable&lt;T&gt;;</code></pre> 
The Regular concept specifies that a type is regular, that is, it is copyable, default constructible, and equality comparable. It is satisfied by types that behave similarly to built-in types like int, and that are comparable with ==. 
