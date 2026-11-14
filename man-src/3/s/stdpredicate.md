---
title: "stdpredicate(3)"
name: "stdpredicate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpredicate/"
---

std::Predicate - std::Predicate

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class F, class... Args &gt;

concept Predicate =                              (since C++20)

std::RegularInvocable&lt;F, Args...&gt; &amp;&amp;

std::Boolean&lt;std::invoke_result_t&lt;F, Args...&gt;&gt;;</code></pre> 
The concept Predicate&lt;F, Args...&gt; specifies that F is a predicate that accepts arguments whose types and value categories are encoded by Args..., i.e., it can be invoked with these arguments to produce a Boolean result. 
Note that RegularInvocable requires the invocation to not modify either the callable object or the arguments and be equality-preserving. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
