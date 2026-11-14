---
title: "stdexperimentalrangesoutputiterator(3)"
name: "stdexperimentalrangesoutputiterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesoutputiterator/"
---

std::experimental::ranges::OutputIterator - std::experimental::ranges::OutputIterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class I, class T&gt;

concept bool OutputIterator =

Iterator&lt;I&gt; &amp;&amp; Writable&lt;I, T&gt; &amp;&amp;                                      (ranges TS)

requires(I i, T&amp;&amp; t) {

    *i++ = std::forward&lt;T&gt;(t); // not required to be equality preserving

};</code></pre> 
The OutputIterator concept is a refinement of Iterator, adding the requirement that it can be used to write values of values of type and value category encoded by T (via Writable). EqualityComparable is not required. 
Let E be an expression such that decltype((E)) is T, and i be a dereferenceable object of type I. OutputIterator&lt;I, T&gt; is satisfied only if *i++ = E; has effects equivalent to *i = E; ++i;. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>Notes</h2>

Unlike the output iterator requirements in the C++ standard, OutputIterator in the Ranges TS does not require that the iterator category tag be defined. 
Algorithms on output iterators should be single pass. 
