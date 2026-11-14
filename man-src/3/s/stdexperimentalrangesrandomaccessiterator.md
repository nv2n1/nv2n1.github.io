---
title: "stdexperimentalrangesrandomaccessiterator(3)"
name: "stdexperimentalrangesrandomaccessiterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesrandomaccessiterator/"
---

std::experimental::ranges::RandomAccessIterator - std::experimental::ranges::RandomAccessIterator

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class I&gt;

    concept bool RandomAccessIterator =

        BidirectionalIterator&lt;I&gt; &amp;&amp;

        DerivedFrom&lt;ranges::iterator_category_t&lt;I&gt;, ranges::random_access_iterator_tag&gt; &amp;&amp;

        StrictTotallyOrdered&lt;I&gt; &amp;&amp;

        SizedSentinel&lt;I, I&gt; &amp;&amp;

        requires(I i, const I j, const ranges::difference_type_t&lt;I&gt; n)
{

    {
        i += n
        } -&gt; Same&lt;I&gt; &amp;;
    (ranges TS)

    {
        j + n
        } -&gt; Same&lt;I&gt; &amp;&amp;;

    {
        n + j
        } -&gt; Same&lt;I&gt; &amp;&amp;;

    {
        i -= n
        } -&gt; Same&lt;I&gt; &amp;;

    {
        j - n
        } -&gt; Same&lt;I&gt; &amp;&amp;;

    j[n];

    requires Same&lt;decltype(j[n]), ranges::reference_t&lt;I&gt;&gt;;
};</code></pre> 
The concept RandomAccessIterator&lt;I&gt; refines BidirectionalIterator by adding support for constant time advancement with the +=, +, -=, and - operators, constant time computation of distance with -, and array notation with subscripting. 
Let a and b be valid iterators of type I such that b is reachable from a, and let n be a value of type ranges::difference_type_t&lt;I&gt; equal to b - a. RandomAccessIterator&lt;I&gt; is satisfied only if: <pre><code>* (a += n) is equal to b.

* std::addressof(a += n) is equal to std::addressof(a).

* (a + n) is equal to (a += n).

* (a + n) is equal to (n + a).

* For any two positive integers x and y, if a + (x + y) is valid, then a + (x + y) is equal to (a + x) + y.

* a + 0 is equal to a.

* If (a + (n - 1)) is valid, then --b is equal to (a + (n - 1)).

* (b += -n) and (b -= n) are both equal to a.

* std::addressof(b -= n) is equal to std::addressof(b).

* (b - n) is equal to (b -= n).

* If b is dereferenceable, then a[n] is valid and is equal to *b.

* bool(a &lt;= b) is true .
</code></pre> 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 
