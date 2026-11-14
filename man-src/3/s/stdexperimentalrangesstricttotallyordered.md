---
title: "stdexperimentalrangesstricttotallyordered(3)"
name: "stdexperimentalrangesstricttotallyordered"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesstricttotallyordered/"
---

std::experimental::ranges::StrictTotallyOrdered,std::experimental::ranges::StrictTotallyOrderedWith - std::experimental::ranges::StrictTotallyOrdered,std::experimental::ranges::StrictTotallyOrderedWith

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T&gt;

    concept bool StrictTotallyOrdered =

        EqualityComparable&lt;T&gt; &amp;&amp;

        requires(const std::remove_reference_t&lt;T&gt; &amp;a,

                 const std::remove_reference_t&lt;T&gt; &amp;b)
{
    (1)(ranges TS)

    {
        a &lt; b
        } -&gt; Boolean &amp;&amp;;

    {
        a &gt; b
        } -&gt; Boolean &amp;&amp;;

    {
        a &lt;= b
        } -&gt; Boolean &amp;&amp;;

    {
        a &gt;= b
        } -&gt; Boolean &amp;&amp;;
};

template &lt;class T, class U&gt;

concept bool StrictTotallyOrderedWith =

    StrictTotallyOrdered&lt;T&gt; &amp;&amp;

        StrictTotallyOrdered&lt;U&gt; &amp;&amp;

            CommonReference&lt;

                const std::remove_reference_t&lt;T&gt; &amp;,

                const std::remove_reference_t&lt;U&gt; &amp;&gt; &amp;&amp;

                StrictTotallyOrdered&lt;

                    ranges::common_reference_t&lt;

                        const std::remove_reference_t&lt;T&gt; &amp;,

                        const std::remove_reference_t&lt;U&gt; &amp;&gt;&gt; &amp;&amp;

                    EqualityComparableWith&lt;T, U&gt; &amp;&amp;
    (2)(ranges TS)

        requires(const std::remove_reference_t&lt;T&gt; &amp;t,

                 const std::remove_reference_t&lt;U&gt; &amp;u)
{

    {
        t &lt; u
        } -&gt; Boolean &amp;&amp;;

    {
        t &gt; u
        } -&gt; Boolean &amp;&amp;;

    {
        t &lt;= u
        } -&gt; Boolean &amp;&amp;;

    {
        t &gt;= u
        } -&gt; Boolean &amp;&amp;;

    {
        u &lt; t
        } -&gt; Boolean &amp;&amp;;

    {
        u &gt; t
        } -&gt; Boolean &amp;&amp;;

    {
        u &lt;= t
        } -&gt; Boolean &amp;&amp;;

    {
        u &gt;= t
        } -&gt; Boolean &amp;&amp;;
};</code></pre> 
1) The concept StrictTotallyOrdered&lt;T&gt; specifies that the comparison operators ==,!=,&lt;,&gt;,&lt;=,&gt;= on T yield results consistent with a strict_total_order on T. 
StrictTotallyOrdered&lt;T&gt; is satisfied only if, given lvalues a, b and c of type const std::remove_reference_t&lt;T&gt;: 
* Exactly one of bool(a &lt; b), bool(a &gt; b) and bool(a == b) is true; 
* If bool(a &lt; b) and bool(b &lt; c) are both true, then bool(a &lt; c) is true; 
* bool(a &gt; b) == bool(b &lt; a) 
* bool(a &gt;= b) == !bool(a &lt; b) 
* bool(a &lt;= b) == !bool(b &lt; a) 
2) The concept StrictTotallyOrderedWith&lt;T, U&gt; specifies that the comparison operators ==,!=,&lt;,&gt;,&lt;=,&gt;= on (possibly mixed) T and U operands yield results consistent with a strict total order. Comparing mixed operands yields results equivalent to comparing the operands converted to their common type. 
Formally, StrictTotallyOrderedWith&lt;T, U&gt; is satisfied only if, given any lvalue t of type const std::remove_reference_t&lt;T&gt; and any lvalue u of type const std::remove_reference_t&lt;U&gt;, and let C be ranges::common_reference_t&lt;const std::remove_reference_t&lt;T&gt;&amp;, const std::remove_reference_t&lt;U&gt;&amp;&gt; : 
* bool(t &lt; u) == bool(C(t) &lt; C(u)) 
* bool(t &gt; u) == bool(C(t) &gt; C(u)) 
* bool(t &lt;= u) == bool(C(t) &lt;= C(u)) 
* bool(t &gt;= u) == bool(C(t) &gt;= C(u)) 
* bool(u &lt; t) == bool(C(u) &lt; C(t)) 
* bool(u &gt; t) == bool(C(u) &gt; C(t)) 
* bool(u &lt;= t) == bool(C(u) &lt;= C(t)) 
* bool(u &gt;= t) == bool(C(u) &gt;= C(t)) 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 
