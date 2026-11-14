---
title: "stdexperimentalrangesstrictweakorder(3)"
name: "stdexperimentalrangesstrictweakorder"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesstrictweakorder/"
---

std::experimental::ranges::StrictWeakOrder - std::experimental::ranges::StrictWeakOrder

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class R, class T, class U &gt;            (1) (ranges TS)

concept bool StrictWeakOrder = Relation&lt;R, T, U&gt;;</code></pre> 
The concept StrictWeakOrder&lt;R, T, U&gt; specifies that the Relation R imposes a strict weak ordering on its arguments. A relation r is a strict weak ordering if 
* it is irreflexive: for all x, r(x, x) is false; 
* it is transitive: for all a, b and c, if r(a, b) and r(b, c) are both true then r(a, c) is true; 
* let e(a, b) be !r(a, b) &amp;&amp; !r(b, a), then e is transitive: e(a, b) &amp;&amp; e(b, c) implies e(a, c). 
Under these conditions, it can be shown that e is an equivalence relation, and r induces a strict total ordering on the equivalence classes determined by e. 

<h2>Notes</h2>

The distinction between Relation and StrictWeakOrder is purely semantic. 
