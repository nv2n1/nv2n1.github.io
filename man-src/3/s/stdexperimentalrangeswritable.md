---
title: "stdexperimentalrangeswritable(3)"
name: "stdexperimentalrangeswritable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangeswritable/"
---

std::experimental::ranges::Writable - std::experimental::ranges::Writable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;class Out, class T&gt;

    concept bool Writable =

        requires(Out &amp;&amp; o, T &amp;&amp;t)
{

    *o = std::forward&lt;T&gt;(t);

    *std::forward&lt;Out&gt;(o) = std::forward&lt;T&gt;(t);

    const_cast&lt;const ranges::reference_t&lt;Out&gt; &amp;&amp;&gt;(*o) = (ranges TS)

        std::forward&lt;T&gt;(t);

    const_cast&lt;const ranges::reference_t&lt;Out&gt; &amp;&amp;&gt;(*std::forward&lt;Out&gt;(o)) =

        std::forward&lt;T&gt;(t);
};

/* none of the four expressions above are required to be equality-preserving */</code></pre> 
The concept Writable&lt;Out, T&gt; specifies the requirements for writing a value whose type and value category are encoded by T into an iterator Out's referenced object. 
Let E be an expression such that decltype((E)) is T, and o be a dereferenceable object of type Out, then Writable&lt;Out, T&gt; is satisfied only if: 
* If Readable&lt;Out&gt; &amp;&amp; Same&lt;ranges::value_type_t&lt;Out&gt;, std::decay_t&lt;T&gt;&gt; is satisfied, then *o after any above assignment is equal to the value of E before the assignment. 
o is not required to be dereferenceable after evaluating any of the assignment expressions above. If E is an xvalue, the resulting state of the object it denotes is valid but unspecified. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>Notes</h2>

The only valid use of operator* is on the left side of an assignment expression. Assignment through the same value of a writable type may happen only once. 
The required expressions with const_cast prevent Readable objects with prvalue reference types from satisfying the syntactic requirements of Writable by accident, while permitting proxy references to continue to work as long as their constness is shallow. See Ranges_TS_issue_381. 
