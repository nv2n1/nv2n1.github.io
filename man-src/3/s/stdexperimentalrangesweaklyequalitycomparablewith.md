---
title: "stdexperimentalrangesweaklyequalitycomparablewith(3)"
name: "stdexperimentalrangesweaklyequalitycomparablewith"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesweaklyequalitycomparablewith/"
---

std::experimental::ranges::WeaklyEqualityComparableWith - std::experimental::ranges::WeaklyEqualityComparableWith

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T, class U&gt;

    concept bool WeaklyEqualityComparableWith =

        requires(const std::remove_reference_t&lt;T&gt; &amp;t,

                 const std::remove_reference_t&lt;U&gt; &amp;u)
{

    {
        t == u
        } -&gt; Boolean &amp;&amp;;
    (ranges TS)

    {
        t != u
        } -&gt; Boolean &amp;&amp;;

    {
        u == t
        } -&gt; Boolean &amp;&amp;;

    {
        u != t
        } -&gt; Boolean &amp;&amp;;
};</code></pre> 
The concept WeaklyEqualityComparableWith&lt;T, U&gt; specifies that an object of type T and an object of type U can be compared for equality with each other (in either order) using both == and !=, and the results of the comparisons are consistent. More formally, WeaklyEqualityComparableWith&lt;T, U&gt; is satisfied only if given 
* t, an lvalue of type const std::remove_reference_t&lt;T&gt; and 
* u, an lvalue of type const std::remove_reference_t&lt;U&gt;, 
the following are true: 
* t == u, u == t, t != u,u != t have the same domain; 
* bool(u == t) == bool(t == u); 
* bool(t != u) == !bool(t == u); and 
* bool(u != t) == bool(t != u). 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that operator == is an equivalence relation 
EqualityComparable (concept) 
EqualityComparableWith 
