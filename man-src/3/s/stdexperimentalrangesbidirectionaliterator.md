---
title: "stdexperimentalrangesbidirectionaliterator(3)"
name: "stdexperimentalrangesbidirectionaliterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesbidirectionaliterator/"
---

std::experimental::ranges::BidirectionalIterator - std::experimental::ranges::BidirectionalIterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt; class I &gt;

concept bool BidirectionalIterator =

ForwardIterator&lt;I&gt; &amp;&amp;

DerivedFrom&lt;ranges::iterator_category_t&lt;I&gt;, ranges::bidirectional_iterator_tag&gt; &amp;&amp;  (ranges TS)

requires(I i) {

    { --i } -&gt; Same&lt;I&gt;&amp;;

    { i-- } -&gt; Same&lt;I&gt;&amp;&amp;;

};</code></pre> 
The concept BidirectionalIterator&lt;I&gt; refines ForwardIterator by adding the ability to move an iterator backward. 
A bidirectional iterator r is said to be decrementable if and only if there exists some s such that ++s == r. All decrementable iterators r shall be in the domain of the expressions --r and r--. 
Let a and b be decrementable objects of type I. BidirectionalIterator&lt;I&gt; is satisfied only if: 
* Pre-decrement yields an lvalue that refers to the operand: std::addressof(--a) == std::addressof(a); 
* Post-decrement yields the previous value of the operand: if bool(a == b), then bool(a-- == b). 
* Post-decrement and pre-decrement perform the same modification on its operand: If bool(a == b), then after evaluating both a-- and --b, bool(a == b) still holds. 
* Increment and decrement are inverses of each other: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If a is incrementable and bool(a == b), then bool(--(++a) == b). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If bool(a == b), then bool(++(--a) == b). 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
