---
title: "stdexperimentalrangessizedsentinel(3)"
name: "stdexperimentalrangessizedsentinel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessizedsentinel/"
---

std::experimental::ranges::SizedSentinel - std::experimental::ranges::SizedSentinel

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class S, class I&gt;

    concept bool SizedSentinel =

        Sentinel&lt;S, I&gt; &amp;&amp;

        !ranges::disable_sized_sentinel&lt;std::remove_cv_t&lt;S&gt;, std::remove_cv_t&lt;I&gt;&gt; &amp;&amp; (1)(ranges TS)

                                                                                         requires(const I &amp;i, const S &amp;s)
{

    {
        s - i
        } -&gt; Same&lt;ranges::difference_type_t&lt;I&gt;&gt; &amp;&amp;;

    {
        i - s
        } -&gt; Same&lt;ranges::difference_type_t&lt;I&gt;&gt; &amp;&amp;;
};

template &lt;class S, class I&gt;
(1)(ranges TS)

    constexpr bool disable_sized_sentinel = false;</code></pre> 
The SizedSentinel concept specifies that an object of the iterator type I and an object of the sentinel type S can be subtracted to compute the distance between them in constant time. 
Let i be an iterator of type I, and s a sentinel of type S such that [i, s) denotes a range. Let N be the smallest number of applications of ++i necessary to make bool(i == s) be true. Then SizedSentinel&lt;S, I&gt; is satisfied only if: 
* If N is representable by ranges::difference_type_t&lt;I&gt;, then s - i is well-defined and equals N; and 
* If -N is representable by ranges::difference_type_t&lt;I&gt;, then i - s is well-defined and equals -N. 
The variable template disable_sized_sentinel provides a mechanism for iterators and sentinels that can be subtracted but do not meet the semantic requirements of SizedSentinel to opt out of the concept by specializing the variable template to have the value true. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 
