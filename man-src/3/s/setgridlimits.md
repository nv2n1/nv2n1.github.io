---
title: "setgridlimits(3)"
name: "setgridlimits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setgridlimits/"
description: "QuantLib::FDDividendEngineBase – Abstract base class for dividend engines."
---

<p>QuantLib::FDDividendEngineBase &#8211; Abstract base class for dividend engines. </p>
<h2>Synopsis</h2>
<pre><code>FDDividendEngineBase (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Size timeSteps=100, Size gridPoints=100, bool timeDependent=false)



Protected Member Functions
virtual void setupArguments (const PricingEngine::arguments *) const



void setGridLimits () const =0



void executeIntermediateStep (Size step) const =0



Real getDividendAmount (Size i) const



Real getDiscountedDividend (Size i) const</code></pre>
<p> Inherits QuantLib::FDMultiPeriodEngine. Inherited by <code>FDDividendEngineMerton73</code>, and <code>FDDividendEngineShiftScale</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>FDDividendEngineBase (const boost::shared_ptr&lt; GeneralizedBlackScholesProcess &gt; &amp;process, Size timeSteps=100, Size gridPoints=100, bool timeDependent=false)



Protected Member Functions
virtual void setupArguments (const PricingEngine::arguments *) const



void setGridLimits () const =0



void executeIntermediateStep (Size step) const =0



Real getDividendAmount (Size i) const



Real getDiscountedDividend (Size i) const</code></pre>
<h2>Detailed Description</h2>
<p>Abstract base class for dividend engines. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>The dividend class really needs to be made more sophisticated to distinguish between fixed dividends and fractional dividends</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
