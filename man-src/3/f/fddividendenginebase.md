---
title: "fddividendenginebase(3)"
name: "fddividendenginebase"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fddividendenginebase/"
description: "QuantLib::FDDividendEngineBase – Abstract base class for dividend engines."
---

<p>QuantLib::FDDividendEngineBase &#8211; Abstract base class for dividend engines. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/fddividendengine.hpp&gt; </p>
<p> Inherits QuantLib::FDMultiPeriodEngine. </p>
<p> Inherited by <code>FDDividendEngineMerton73</code>, and <code>FDDividendEngineShiftScale</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FDDividendEngineBase</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps=100, Size gridPoints=100, bool timeDependent=false) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>setupArguments</code> (const PricingEngine::arguments *) const </p>
<p> void <code>setGridLimits</code> () const =0 </p>
<p> void <code>executeIntermediateStep</code> (Size step) const =0 </p>
<p> <code>Real</code> <code>getDividendAmount</code> (Size i) const </p>
<p> <code>Real</code> <code>getDiscountedDividend</code> (Size i) const </p>
<h2>Detailed Description</h2>
<p>Abstract base class for dividend engines. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>The dividend class really needs to be made more sophisticated to distinguish between fixed dividends and fractional dividends</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
