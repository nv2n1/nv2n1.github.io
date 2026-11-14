---
title: "stdexperimentalrangesincrementable(3)"
name: "stdexperimentalrangesincrementable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesincrementable/"
---

std::experimental::ranges::Incrementable - std::experimental::ranges::Incrementable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class I&gt;

concept bool Incrementable =

Regular&lt;I&gt; &amp;&amp;

WeaklyIncrementable&lt;I&gt; &amp;&amp;                         (ranges TS)

requires(I i) {

    { i++ } -&gt; Same&lt;I&gt;&amp;&amp;;

};</code></pre> 
The concept Incrementable&lt;I&gt; specifies the requirements on a type that can be incremented (with the pre- and post-increment operators). The increment operations (including those required by WeaklyIncrementable) are required to be equality-preserving, and the type is required to be EqualityComparable. 
Let a and b be incrementable objects of type I. Incrementable&lt;I&gt; is satisfied only if: 
* If bool(a == b) then bool(a++ == b). 
* If bool(a == b) then bool(void(a++), a) == ++b). 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>Notes</h2>

The requirement that a equals b implies ++a equals ++b allows the use of multi-pass algorithms with Incrementable types. 
