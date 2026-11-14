---
title: "stdexperimentalrangesweaklyincrementable(3)"
name: "stdexperimentalrangesweaklyincrementable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesweaklyincrementable/"
---

std::experimental::ranges::WeaklyIncrementable - std::experimental::ranges::WeaklyIncrementable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class I&gt;

concept bool WeaklyIncrementable =

Semiregular&lt;I&gt; &amp;&amp;

requires(I i) {

    typename ranges::difference_type_t&lt;I&gt;;                             (ranges TS)

    requires SignedIntegral&lt;ranges::difference_type_t&lt;I&gt;&gt;;

    { ++i } -&gt; Same&lt;I&gt;&amp;; /* not required to be equality preserving */

    i++; /* not required to be equality preserving */

};</code></pre> 
The concept WeaklyIncrementable&lt;I&gt; specifies the requirements on a type that can be incremented (with the pre- and post-increment operators). The increment operations need not be equality-preserving, and the type need not be EqualityComparable. 
Let i be an object of type I. i is said to be incrementable if it is in the domain of both pre- and post-increment. WeaklyIncrementable&lt;I&gt; is satisfied only if: 
* ++i and i++ have the same domain; 
* If i is incrementable, then: 
&nbsp;<wbr>&nbsp;o ++i and i++ both advance i to the next element; and 
&nbsp;<wbr>&nbsp;o ++i refers to the same object as i. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>Notes</h2>

For WeaklyIncrementable types, a equals b does not imply that ++a equals ++b. Algorithms on such types should be single pass and never attempt to pass through the same value twice. 
