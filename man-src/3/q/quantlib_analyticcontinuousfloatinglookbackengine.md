---
title: "quantlib_analyticcontinuousfloatinglookbackengine(3)"
name: "quantlib_analyticcontinuousfloatinglookbackengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticcontinuousfloatinglookbackengine/"
description: "QuantLib::AnalyticContinuousFloatingLookbackEngine – Pricing engine for European continuous floating-strike lookback."
---

<p>QuantLib::AnalyticContinuousFloatingLookbackEngine &#8211; Pricing engine for European continuous floating-strike lookback. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/lookback/analyticcontinuousfloatinglookback.hpp&gt; </p>
<p> Inherits <code>QuantLib::ContinuousFloatingLookbackOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticContinuousFloatingLookbackEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Pricing engine for European continuous floating-strike lookback. </p>
<p> Formula from &#8216;Option Pricing Formulas&#8217;, E.G. Haug, McGraw-Hill, 1998, p.61-62 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>returned values verified against results from literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
