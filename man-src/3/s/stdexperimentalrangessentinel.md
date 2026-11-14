---
title: "stdexperimentalrangessentinel(3)"
name: "stdexperimentalrangessentinel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessentinel/"
---

std::experimental::ranges::Sentinel - std::experimental::ranges::Sentinel

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class S, class I &gt;

concept bool Sentinel =                           (ranges TS)

Semiregular&lt;S&gt; &amp;&amp; Iterator&lt;I&gt; &amp;&amp;

WeaklyEqualityComparableWith&lt;S, I&gt;;</code></pre> 
The Sentinel concept specifies the relationship between an Iterator type and a Semiregular type whose values denote a range. 
Let s and i be values of type S and I, respectively, such that [i, s) denotes a range. Sentinel&lt;S, I&gt; is satisfied only if: 
* i == s is well-defined. 
* If bool(i != s) then i is dereferenceable and [++i, s) denotes a range. 
The domain of == can change over time. Given an iterator i and sentinel s such that [i, s) denotes a range and i != s, [i, s) is not required to continue to denote a range after incrementing any iterator equal to i (and so i == s is no longer required to be well-defined after such an increment). 
