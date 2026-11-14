---
title: "prices_(3)"
name: "prices_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-prices_/"
description: "QuantLib::FDStepConditionEngine – Finite-differences pricing engine for American-style vanilla options."
---

<p>QuantLib::FDStepConditionEngine &#8211; Finite-differences pricing engine for American-style vanilla options. </p>
<h2>Synopsis</h2>
<pre><code>FDStepConditionEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Size timeSteps, Size gridPoints, bool timeDependent=false)



Protected Member Functions
virtual void initializeStepCondition () const =0



virtual void calculate (PricingEngine::results *) const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::FDVanillaEngine</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>FDStepConditionEngine (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Size timeSteps, Size gridPoints, bool timeDependent=false)



Protected Member Functions
virtual void initializeStepCondition () const =0



virtual void calculate (PricingEngine::results *) const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>StandardStepCondition</code> &gt; <code>stepCondition_</code> </p>
<p> <code>SampledCurve</code> <code>prices_</code> </p>
<p> <code>TridiagonalOperator</code> <code>controlOperator_</code> </p>
<p> std::vector&lt; boost::shared_ptr&lt; <code>bc_type</code> &gt; &gt; <code>controlBCs_</code> </p>
<p> <code>SampledCurve</code> <code>controlPrices_</code></p>
<h2>Detailed Description</h2>
<p>Finite-differences pricing engine for American-style vanilla options.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
