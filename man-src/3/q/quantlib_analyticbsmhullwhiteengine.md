---
title: "quantlib_analyticbsmhullwhiteengine(3)"
name: "quantlib_analyticbsmhullwhiteengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_analyticbsmhullwhiteengine/"
description: "QuantLib::AnalyticBSMHullWhiteEngine – analytic european option pricer including stochastic interest rates"
---

<p>QuantLib::AnalyticBSMHullWhiteEngine &#8211; analytic european option pricer including stochastic interest rates </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/analyticbsmhullwhiteengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; HullWhite, VanillaOption::arguments, VanillaOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticBSMHullWhiteEngine</code> (<code>Real</code> equityShortRateCorrelation, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, const boost::shared_ptr&lt; <code>HullWhite</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>analytic european option pricer including stochastic interest rates </p>
<p> References: </p>
<p> Brigo, Mercurio, Interest Rate Models </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
