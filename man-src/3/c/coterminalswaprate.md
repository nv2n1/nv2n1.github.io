---
title: "coterminalswaprate(3)"
name: "coterminalswaprate"
section: "3"
letter: "c"
url: "/docs/linux/man/3-coterminalswaprate/"
description: "QuantLib::CurveState – Curve state for market-model simulations"
---

<p>QuantLib::CurveState &#8211; Curve state for market-model simulations </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/curvestate.hpp&gt; </p>
<p> Inherited by <code>CMSwapCurveState</code>, <code>CoterminalSwapCurveState</code>, and <code>LMMCurveState</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CurveState</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes) </p>
<p> <code>Inspectors</code> </p>
<p> Size <code>numberOfRates</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>rateTimes</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>rateTaus</code> () const </p>
<p> virtual <code>Real</code> <code>discountRatio</code> (Size i, Size j) const =0 </p>
<p> virtual <code>Rate</code> <code>forwardRate</code> (Size i) const =0 </p>
<p> virtual <code>Rate</code> <code>coterminalSwapAnnuity</code> (Size numeraire, Size i) const =0 </p>
<p> virtual <code>Rate</code> <code>coterminalSwapRate</code> (Size i) const =0 </p>
<p> virtual <code>Rate</code> <code>cmSwapAnnuity</code> (Size numeraire, Size i, Size spanningForwards) const =0 </p>
<p> virtual <code>Rate</code> <code>cmSwapRate</code> (Size i, Size spanningForwards) const =0 </p>
<p> virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>forwardRates</code> () const =0 </p>
<p> virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>coterminalSwapRates</code> () const =0 </p>
<p> virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>cmSwapRates</code> (Size spanningForwards) const =0 </p>
<p> <code>Rate</code> <code>swapRate</code> (Size begin, Size end) const </p>
<p> virtual std::auto_ptr&lt; <code>CurveState</code> &gt; <code>clone</code> () const =0 </p>
<h3>Protected Attributes</h3>
<p>Size <code>numberOfRates_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>rateTimes_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>rateTaus_</code> </p>
<h2>Detailed Description</h2>
<p>Curve state for market-model simulations </p>
<p> This class stores the state of the yield curve associated to the fixed calendar times within the simulation. This is the workhorse discounting object associated to the rate times of the simulation. It&#8217;s important to pass the rates via an object like this to the product rather than directly to make it easier to switch to other engines such as a coterminal swap rate engine. Many products will not need expired rates and others will only require the first rate. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
