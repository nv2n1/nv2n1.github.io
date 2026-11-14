---
title: "stdexperimentalrangesassignable(3)"
name: "stdexperimentalrangesassignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesassignable/"
---

std::experimental::ranges::Assignable - std::experimental::ranges::Assignable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T, class U&gt;

    concept bool Assignable =

        std::is_lvalue_reference&lt;T&gt;::value &amp;&amp;

        CommonReference&lt;

            const std::remove_reference_t&lt;T&gt; &amp;, (ranges TS)

                                                    const std::remove_reference_t&lt;U&gt; &amp;&gt; &amp;&amp;

        requires(T t, U &amp;&amp;u)
{

    {
        t = std::forward&lt;U&gt;(u)
        } -&gt; Same&lt;T&gt; &amp;&amp;;
};</code></pre> 
The concept Assignable&lt;T, U&gt; specifies that an expression of the type and value category specified by U can be assigned to an lvalue expression whose type is specified by T. 
Given 
* t, an lvalue of type std::remove_reference_t&lt;T&gt; that refers to an object o, 
* u, an expression such that decltype((u)) is U, 
* u2, a distinct object that is equal to u, 
Assignable&lt;T, U&gt; is satisfied only if * std::addressof(t = u) == std::addressof(o) (i.e., the assignment expression yields an lvalue referring to the left operand);

* After evaluating t = u: 
&nbsp;<wbr>&nbsp;o t is equal to u2, unless u is a non-const xvalue that refers to o (i.e., the assignment is a self-move-assignment), 
&nbsp;<wbr>&nbsp;o if u is a glvalue: <pre><code>#If it is a non - const xvalue, the object to which it refers is in a valid but unspecified state;
#Otherwise, the object it refers to is not modified;
</code></pre> 
There need not be any subsumption relationship between Assignable&lt;T, U&gt; and std::is_lvalue_reference&lt;T&gt;::value. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>Notes</h2>

A deduction constraint of the form { expression } -&gt; Same&lt;T&gt;&amp;&amp; effectively requires decltype((expression))&amp;&amp; to be the exact same type as T&amp;&amp;. This constrains both the expression's type and its value category. 
Assignment need not be a total function. In particular, if assigning to some object x can cause some other object y to be modified, then x = y is likely not in the domain of =. This typically happens if the right operand is owned directly or indirectly by the left operand (e.g., with smart pointers to nodes in an node-based data structure, or with something like std::vector&lt;std::any&gt;). 
