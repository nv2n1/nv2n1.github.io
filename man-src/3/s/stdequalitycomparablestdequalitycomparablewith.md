---
title: "stdequalitycomparablestdequalitycomparablewith(3)"
name: "stdequalitycomparablestdequalitycomparablewith"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdequalitycomparablestdequalitycomparablewith/"
---

std::EqualityComparable,std::EqualityComparableWith - std::EqualityComparable,std::EqualityComparableWith

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class T, class U&gt;

    concept __WeaklyEqualityComparableWith = // exposition only

    requires(const std::remove_reference_t&lt;T&gt; &amp;t,

             const std::remove_reference_t&lt;U&gt; &amp;u)
{

    t == u;
    requires std::Boolean&lt;decltype(t == u)&gt;;
    (1)

            t != u;
    requires std::Boolean&lt;decltype(t != u)&gt;;

    u == t;
    requires std::Boolean&lt;decltype(u == t)&gt;;

    u != t;
    requires std::Boolean&lt;decltype(u != t)&gt;;
};

template &lt;class T&gt;
(2)(since C++ 20)

    concept EqualityComparable = __WeaklyEqualityComparableWith&lt;T, T&gt;;

template &lt;class T, class U&gt;

concept EqualityComparableWith =

    std::EqualityComparable&lt;T&gt; &amp;&amp;

    std::EqualityComparable&lt;U&gt; &amp;&amp;

    std::CommonReference &lt;

    const std::remove_reference_t&lt;T&gt;
&amp;, (3)(since C++ 20)

           const std::remove_reference_t&lt;U&gt; &amp; &gt; &amp;&amp;

                                                std::EqualityComparable&lt;

                                                    std::common_reference_t&lt;

                                                        const std::remove_reference_t&lt;T&gt; &amp;,

                                                        const std::remove_reference_t&lt;U&gt; &amp;&gt;&gt; &amp;&amp;

                                                __WeaklyEqualityComparableWith&lt;T, U&gt;;</code></pre> 
1) The exposition-only concept __WeaklyEqualityComparableWith&lt;T, U&gt; specifies that an object of type T and an object of type U can be compared for equality with each other (in either order) using both == and !=, and the results of the comparisons are consistent. 
More formally, __WeaklyEqualityComparableWith&lt;T, U&gt; is satisfied only if given 
* t, an lvalue of type const std::remove_reference_t&lt;T&gt; and 
* u, an lvalue of type const std::remove_reference_t&lt;U&gt;, 
the following are true: 
* t == u, u == t, t != u,u != t have the same domain; 
* bool(u == t) == bool(t == u); 
* bool(t != u) == !bool(t == u); and 
* bool(u != t) == bool(t != u). 
2) The concept EqualityComparable&lt;T&gt; specifies that the comparison operators == and != on T reflects equality: == yields true if and only if the operands are equal. 
EqualityComparable&lt;T&gt; is satisfied only if, given objects a and b of type T, bool(a == b) is true if and only if a and b are equal. Together with the requirement that a == b is equality preserving, this implies that == is symmetric and transitive, and further that == is reflexive for all objects a that are equal to at least one other object. 
3) The concept EqualityComparableWith&lt;T, U&gt; specifies that the comparison operators == and != on (possibly mixed) T and U operands yield results consistent with equality. Comparing mixed operands yields results equivalent to comparing the operands converted to their common type. 
Formally, EqualityComparableWith&lt;T, U&gt; is satisfied only if, given any lvalue t of type const std::remove_reference_t&lt;T&gt; and any lvalue u of type const std::remove_reference_t&lt;U&gt;, and let C be std::common_reference_t&lt;const std::remove_reference_t&lt;T&gt;&amp;, const std::remove_reference_t&lt;U&gt;&amp;&gt;, bool(t == u) == bool(C(t) == C(u)). 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 
