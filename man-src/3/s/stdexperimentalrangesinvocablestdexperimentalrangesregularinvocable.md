---
title: "stdexperimentalrangesinvocablestdexperimentalrangesregularinvocable(3)"
name: "stdexperimentalrangesinvocablestdexperimentalrangesregularinvocable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesinvocablestdexperimentalrangesregularinvocable/"
---

std::experimental::ranges::Invocable,std::experimental::ranges::RegularInvocable - std::experimental::ranges::Invocable,std::experimental::ranges::RegularInvocable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class F, class... Args &gt;

concept bool Invocable =

requires(F&amp;&amp; f, Args&amp;&amp;... args) {                                  (ranges TS)

    ranges::invoke(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)...);

    /* not required to be equality preserving */

};

template &lt; class F, class... Args &gt;                                (ranges TS)

concept bool RegularInvocable = Invocable&lt;F, Args...&gt;;</code></pre> 
The Invocable concept specifies that a callable type F can be called with a set of argument types Args... using the function template ranges::invoke. 
The RegularInvocable concept adds to the Invocable concept by requiring the invoke expression to be equality preserving and not modify either the function object or the arguments. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>Notes</h2>

The distinction between Invocable and RegularInvocable is purely semantic. 
A random number generator may satisfy Invocable but cannot satisfy RegularInvocable (comical ones excluded). 
