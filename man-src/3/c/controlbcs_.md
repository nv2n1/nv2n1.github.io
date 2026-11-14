---
title: "controlbcs_(3)"
name: "controlbcs_"
section: "3"
letter: "c"
url: "/docs/linux/man/3-controlbcs_/"
description: "QuantLib::FDStepConditionEngine – Finite-differences pricing engine for American-style vanilla options."
---

<p>QuantLib::FDStepConditionEngine &#8211; Finite-differences pricing engine for American-style vanilla options. </p>
<h2>Synopsis</h2>
<p> #include &lt;ql/pricingengines/vanilla/fdstepconditionengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::FDVanillaEngine</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>FDStepConditionEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps, Size gridPoints, bool timeDependent=false) </p>
<h3>Protected Member Functions</h3>
<p> virtual void <code>initializeStepCondition</code> () const =0 </p>
<p> virtual void <code>calculate</code> (PricingEngine::results *) const </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>StandardStepCondition</code> &gt; <code>stepCondition_</code> </p>
<p> <code>SampledCurve</code> <code>prices_</code> </p>
<p> <code>TridiagonalOperator</code> <code>controlOperator_</code> </p>
<p> std::vector&lt; boost::shared_ptr&lt; <code>bc_type</code> &gt; &gt; <code>controlBCs_</code> </p>
<p> <code>SampledCurve</code> <code>controlPrices_</code> </p>
<h2>Detailed Description</h2>
<p> Finite-differences pricing engine for American-style vanilla options. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code.</p>
