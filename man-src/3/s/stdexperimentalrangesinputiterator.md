---
title: "stdexperimentalrangesinputiterator(3)"
name: "stdexperimentalrangesinputiterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesinputiterator/"
---

std::experimental::ranges::InputIterator - std::experimental::ranges::InputIterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class I &gt;

concept bool InputIterator =

Iterator&lt;I&gt; &amp;&amp; Readable&lt;I&gt; &amp;&amp;                                             (ranges TS)

requires { typename ranges::iterator_category_t&lt;I&gt;; } &amp;&amp;

DerivedFrom&lt;ranges::iterator_category_t&lt;I&gt;, ranges::input_iterator_tag&gt;;</code></pre> 
The InputIterator concept is a refinement of Iterator, adding the requirement that the referenced values can be read (via Readable) and the requirement that the iterator category tag be present. 

<h2>Notes</h2>

Unlike the input iterator requirements in the C++ standard, InputIterator in the Ranges TS does not require EqualityComparable. 
