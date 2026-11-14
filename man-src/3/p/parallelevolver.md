---
title: "parallelevolver(3)"
name: "parallelevolver"
section: "3"
letter: "p"
url: "/docs/linux/man/3-parallelevolver/"
description: "ql/methods/finitedifferences/parallelevolver.hpp – Parallel evolver for multiple arrays."
---

<p>ql/methods/finitedifferences/parallelevolver.hpp &#8211; Parallel evolver for multiple arrays. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/methods/finitedifferences/finitedifferencemodel.hpp&gt;

#include &lt;ql/methods/finitedifferences/stepcondition.hpp&gt;

#include &lt;ql/numericalmethod.hpp&gt;

#include &lt;vector&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>StepConditionSet&lt; array_type &gt;</code><br />
 <i>Parallel evolver for multiple arrays. </i></p>
<h2>Detailed Description</h2>
<p>Parallel evolver for multiple arrays. </p>
<p> This class takes the evolver class and creates a new class which evolves each of the evolvers in parallel. Part of what this does is to take the types for each evolver class and then wrapper them so that they create new types which are sets of the old types. </p>
<p> This class is intended to be run in situations where there are parallel differential equations such as with some convertible bond models.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
