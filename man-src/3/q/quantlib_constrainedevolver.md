---
title: "quantlib_constrainedevolver(3)"
name: "quantlib_constrainedevolver"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_constrainedevolver/"
description: "QuantLib::ConstrainedEvolver – Constrained market-model evolver."
---

<p>QuantLib::ConstrainedEvolver &#8211; Constrained market-model evolver. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/constrainedevolver.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelEvolver</code>. </p>
<p> Inherited by <code>LogNormalFwdRateEulerConstrained</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>setConstraintType</code> (const std::vector&lt; Size &gt; &amp;startIndexOfSwapRate, const std::vector&lt; Size &gt; &amp;EndIndexOfSwapRate)=0<br />
 <i>call once </i><br />
 virtual void <code>setThisConstraint</code> (const std::vector&lt; Rate &gt; &amp;rateConstraints, const std::vector&lt; bool &gt; &amp;isConstraintActive)=0<br />
 <i>call before each path </i></p>
<h2>Detailed Description</h2>
<p>Constrained market-model evolver. </p>
<p> Abstract base class. Requires extra methods above that of marketmodelevolver to let you fix rates via importance sampling. </p>
<p> The evolver does the actual gritty work of evolving the forward rates from one time to the next. </p>
<p> This is intended to be used for the Fries-Joshi proxy simulation approach to <code>Greeks</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
