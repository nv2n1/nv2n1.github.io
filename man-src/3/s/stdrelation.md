---
title: "stdrelation(3)"
name: "stdrelation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrelation/"
---

std::Relation - std::Relation

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt;class R, class T, class U&gt;

concept Relation =                                    (1) (since C++20)

std::Predicate&lt;R, T, T&gt; &amp;&amp; std::Predicate&lt;R, U, U&gt; &amp;&amp;

std::Predicate&lt;R, T, U&gt; &amp;&amp; std::Predicate&lt;R, U, T&gt;;</code></pre> 
The concept Relation&lt;R, T, U&gt; specifies that R defines a binary relation over the set of expressions whose type and value category are those encoded by either T or U. 
