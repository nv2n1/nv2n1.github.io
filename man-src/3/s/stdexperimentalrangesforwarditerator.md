---
title: "stdexperimentalrangesforwarditerator(3)"
name: "stdexperimentalrangesforwarditerator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesforwarditerator/"
---

std::experimental::ranges::ForwardIterator - std::experimental::ranges::ForwardIterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class I &gt;

concept bool ForwardIterator =

InputIterator&lt;I&gt; &amp;&amp;                                                           (ranges TS)

DerivedFrom&lt;ranges::iterator_category_t&lt;I&gt;, ranges::forward_iterator_tag&gt; &amp;&amp;

Incrementable&lt;I&gt; &amp;&amp;

Sentinel&lt;I, I&gt;;</code></pre> 
The concept ForwardIterator&lt;I&gt; refines InputIterator by adding equality comparison and the multi-pass guarantee. 
The domain of == for forward iterators is that of iterators over the same underlying sequence, except that value-initialized iterators of the same type may be compared with each other and shall compare equal. 
Pointers and references obtained from a forward iterator into a range [i, s) must remain valid while [i, s) continues to denote a range. 
Let a and b be two deferenceable iterators of type I. ForwardIterator&lt;I&gt; is satisfied only if: 
* a == b implies ++a == ++b; and 
* The expression ([](X x){++x;}(a), *a) is equivalent to *a, i.e., incrementing a copy of a has no effect on the result of dereferencing a. 
This is known as the multi-pass guarantee. 

<h2>Notes</h2>

A forward iterator cannot be &quot;stashing&quot;: it cannot return a reference to an object within itself, because such references would be invalidated by the destruction of the forward iterator. 
