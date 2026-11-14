---
title: "stdboolean(3)"
name: "stdboolean"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdboolean/"
---

std::Boolean - std::Boolean

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class B&gt;

    concept Boolean =

        std::Movable&lt;std::remove_cvref_t&lt;B&gt;&gt; &amp;&amp;

    requires(const std::remove_reference_t&lt;B&gt; &amp;b1,

             const std::remove_reference_t&lt;B&gt; &amp;b2, const bool a)
{

    requires std::ConvertibleTo &lt; const std::remove_reference_t&lt;B&gt;
    &amp;, bool &gt; ;

    !b1;
    requires std::ConvertibleTo&lt;decltype(!b1), bool&gt;;

    b1 &amp;&amp;a;
    requires std::Same&lt;decltype(b1 &amp;&amp; a), bool&gt;;

    b1 || a;
    requires std::Same&lt;decltype(b1 || a), bool&gt;;

    b1 &amp;&amp;b2;
    requires std::Same&lt;decltype(b1 &amp;&amp; b2), bool&gt;;
    (since C++ 20)

        a &amp;&amp;b2;
    requires std::Same&lt;decltype(a &amp;&amp; b2), bool&gt;;

    b1 || b2;
    requires std::Same&lt;decltype(b1 || b2), bool&gt;;

    a || b2;
    requires std::Same&lt;decltype(a || b2), bool&gt;;

    b1 == b2;
    requires std::ConvertibleTo&lt;decltype(b1 == b2), bool&gt;;

    b1 == a;
    requires std::ConvertibleTo&lt;decltype(b1 == a), bool&gt;;

    a == b2;
    requires std::ConvertibleTo&lt;decltype(a == b2), bool&gt;;

    b1 != b2;
    requires std::ConvertibleTo&lt;decltype(b1 != b2), bool&gt;;

    b1 != a;
    requires std::ConvertibleTo&lt;decltype(b1 != a), bool&gt;;

    a != b2;
    requires std::ConvertibleTo&lt;decltype(a != b2), bool&gt;;
};</code></pre> 
The concept Boolean&lt;B&gt; specifies the requirements for a type usable in Boolean contexts. For Boolean to be satisfied, the logical operators must have the usual behavior (including short-circuiting). More precisely, given 
* b1, b2, two lvalues of type const std::remove_reference_t&lt;B&gt;, 
Boolean&lt;B&gt; is satisfied only if: 
* bool(b1) == !bool(!b1) 
* b1 &amp;&amp; b2, b1 &amp;&amp; bool(b2) and bool(b1) &amp;&amp; b2 are all equal to bool(b1) &amp;&amp; bool(b2) and have the same short-circuit evaluation; 
* b1 || b2, b1 || bool(b2) and bool(b1) || b2 are all equal to bool(b1) || bool(b2) and have the same short-circuit evaluation; 
* bool(b1 == b2), bool(b1 == bool(b2)), and bool(bool(b1) == b2) are all equal to (bool(b1) == bool(b2)); 
* bool(b1 != b2), bool(b1 != bool(b2)), and bool(bool(b1) != b2) are all equal to (bool(b1) != bool(b2)). 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 
Implicit expression variations 
A requires-expression that uses an expression that is non-modifying for some constant lvalue operand also implicitly requires additional variations of that expression that accept a non-constant lvalue or (possibly constant) rvalue for the given operand unless such an expression variation is explicitly required with differing semantics. These implicit expression variations must meet the same semantic requirements of the declared expression. The extent to which an implementation validates the syntax of the variations is unspecified. 

<h2>Notes</h2>

Examples of Boolean types include bool, std::true_type, and std::bitset&lt;N&gt;::reference. Pointers are not Boolean types. 
