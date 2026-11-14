---
title: "stdexperimentalrangesiterator(3)"
name: "stdexperimentalrangesiterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesiterator/"
---

std::experimental::ranges::Iterator - std::experimental::ranges::Iterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class I&gt;

concept bool Iterator =

requires(I i) {                                      (ranges TS)

    { *i } -&gt; auto&amp;&amp;; // Requires: i is dereferenceable

} &amp;&amp;

WeaklyIncrementable&lt;I&gt;;</code></pre> 
The Iterator concept forms the basis of the iterator concept taxonomy; every iterator satisfies the Iterator requirements. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>Notes</h2>

Iterator itself only specifies operations for dereferencing and incrementing an iterator. Most algorithms will require additional operations, for example: 
* comparing iterators with sentinels (see Sentinel); 
* reading values from an iterator (see Readable and InputIterator) 
* writing values to an iterator (see Writable and OutputIterator) 
* a richer set of iterator movements (see ForwardIterator, BidirectionalIterator, RandomAccessIterator) 
The -&gt; auto&amp;&amp; constraint implies that the result type of the deference cannot be void. 
