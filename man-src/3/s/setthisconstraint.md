---
title: "setthisconstraint(3)"
name: "setthisconstraint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setthisconstraint/"
description: "QuantLib::ConstrainedEvolver – Constrained market-model evolver."
---

<p>QuantLib::ConstrainedEvolver &#8211; Constrained market-model evolver. </p>
<h2>Synopsis</h2>
<pre><code>virtual void setConstraintType (const std::vector&lt; Size &gt; &amp;startIndexOfSwapRate, const std::vector&lt; Size &gt; &amp;EndIndexOfSwapRate)=0


call once


virtual void setThisConstraint (const std::vector&lt; Rate &gt; &amp;rateConstraints, const std::vector&lt; bool &gt; &amp;isConstraintActive)=0


call before each path</code></pre>
<p> Inherits <code>QuantLib::MarketModelEvolver</code>. Inherited by <code>LogNormalFwdRateEulerConstrained</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual void setConstraintType (const std::vector&lt; Size &gt; &amp;startIndexOfSwapRate, const std::vector&lt; Size &gt; &amp;EndIndexOfSwapRate)=0


call once


virtual void setThisConstraint (const std::vector&lt; Rate &gt; &amp;rateConstraints, const std::vector&lt; bool &gt; &amp;isConstraintActive)=0


call before each path</code></pre>
<h2>Detailed Description</h2>
<p>Constrained market-model evolver. </p>
<p> Abstract base class. Requires extra methods above that of marketmodelevolver to let you fix rates via importance sampling. </p>
<p> The evolver does the actual gritty work of evolving the forward rates from one time to the next. </p>
<p> This is intended to be used for the Fries-Joshi proxy simulation approach to <code>Greeks</code></p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
