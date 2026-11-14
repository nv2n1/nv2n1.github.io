---
title: "project(3)"
name: "project"
section: "3"
letter: "p"
url: "/docs/linux/man/3-project/"
description: "QuantLib::ProjectedCostFunction – Parameterized cost function."
---

<p>QuantLib::ProjectedCostFunction &#8211; Parameterized cost function. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/optimization/projectedcostfunction.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::CostFunction</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ProjectedCostFunction</code> (const <code>CostFunction</code> &amp;costFunction, const <code>Array</code> &amp;parametersValues, const std::vector&lt; bool &gt; &amp;parametersFreedoms) </p>
<p> virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>project</code> (const <code>Array</code> &amp;parameters) const<br />
 <i>returns the subset of free parameters corresponding </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>include</code> (const <code>Array</code> &amp;projectedParameters) const<br />
 <i>returns whole set of parameters corresponding to the set </i> <code>CostFunction interface</code> </p>
<p> virtual <code>Real</code> <code>value</code> (const <code>Array</code> &amp;freeParameters) const<br />
 <i>method to overload to compute the cost function value in x </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>values</code> (const <code>Array</code> &amp;freeParameters) const<br />
 <i>method to overload to compute the cost function values in x </i></p>
<h2>Detailed Description</h2>
<p>Parameterized cost function. </p>
<p> This class creates a proxy cost function which can depend on any arbitrary subset of parameters (the other being fixed)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
