---
title: "stdrangesrange(3)"
name: "stdrangesrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesrange/"
---

std::ranges::Range - std::ranges::Range

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;ranges&gt;

    template &lt;class T&gt;
    (1)

        concept Range = __RangeImpl&lt;T &amp;&gt;; // exposition-only definition

// exposition-only helper concept

template &lt;class T&gt;

concept __RangeImpl = requires(T &amp;&amp;t)
{
    (2)

        ranges::begin(std::forward&lt;T&gt;(t)); // equality-preserving for forward iterators

    ranges::end(std::forward&lt;T&gt;(t));
};

// exposition-only helper concept

template &lt;class T&gt;
(3)

    concept __ForwardingRange = Range&lt;T&gt; &amp;&amp; __RangeImpl&lt;T&gt;;</code></pre> 
1) The Range concept defines the requirements of a type that allows iteration over its elements by providing an iterator and sentinel that denote the elements of the range. 
Formally, given an expression E such that decltype((E)) is T, T models Range only if 
* [ranges::begin(E), ranges::end(E)) denotes a range, and 
* both ranges::begin(E) and ranges::end(E) are amortized constant time and non-modifying, and 
* if the type of ranges::begin(E) models ForwardIterator, ranges::begin(E) is equality-preserving (in other words, forward iterators support multi-pass algorithms) 
Note: In the exposition-only definition above, the required expressions ranges::begin(std::forward&lt;T&gt;(t)) and ranges::end(std::forward&lt;T&gt;(t)) do not require implicit_expression_variations. 
3) The exposition-only concept __ForwardingRange defines the requirements of a range such that a function can take it by value and return iterators obtained from it without danger of dangling. 
Formally, given an expression E such that decltype((E)) is T and an lvalue t that denotes the same object as E, T models __ForwardingRange only if 
* ranges::begin(E) and ranges::begin(t) are expression-equivalent (have the same effect when evaluated, and both or neither are potentially-throwing, both or neither are constant subexpressions), and 
* ranges::end(E) and ranges::end(t) are expression-equivalent, and 
* the validity of iterators obtained from the object denoted by E is not tied to the lifetime of that object. 
