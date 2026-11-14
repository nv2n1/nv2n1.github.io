---
title: "ratetimes_(3)"
name: "ratetimes_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-ratetimes_/"
description: "QuantLib::CurveState – Curve state for market-model simulations"
---

<p>QuantLib::CurveState &#8211; Curve state for market-model simulations </p>
<h2>Synopsis</h2>
<pre><code>Size numberOfRates () const



const std::vector&lt; Time &gt; &amp; rateTimes () const



const std::vector&lt; Time &gt; &amp; rateTaus () const



virtual Real discountRatio (Size i, Size j) const =0



virtual Rate forwardRate (Size i) const =0



virtual Rate coterminalSwapAnnuity (Size numeraire, Size i) const =0



virtual Rate coterminalSwapRate (Size i) const =0



virtual Rate cmSwapAnnuity (Size numeraire, Size i, Size spanningForwards) const =0



virtual Rate cmSwapRate (Size i, Size spanningForwards) const =0



virtual const std::vector&lt; Rate &gt; &amp; forwardRates () const =0



virtual const std::vector&lt; Rate &gt; &amp; coterminalSwapRates () const =0



virtual const std::vector&lt; Rate &gt; &amp; cmSwapRates (Size spanningForwards) const =0



Rate swapRate (Size begin, Size end) const



virtual std::auto_ptr&lt; CurveState &gt; clone () const =0



Protected Attributes</code></pre>
<p> Inherited by <code>CMSwapCurveState</code>, <code>CoterminalSwapCurveState</code>, and <code>LMMCurveState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CurveState</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes)<br />
 <code>Inspectors</code> </p>
<pre><code>Size numberOfRates () const



const std::vector&lt; Time &gt; &amp; rateTimes () const



const std::vector&lt; Time &gt; &amp; rateTaus () const



virtual Real discountRatio (Size i, Size j) const =0



virtual Rate forwardRate (Size i) const =0



virtual Rate coterminalSwapAnnuity (Size numeraire, Size i) const =0



virtual Rate coterminalSwapRate (Size i) const =0



virtual Rate cmSwapAnnuity (Size numeraire, Size i, Size spanningForwards) const =0



virtual Rate cmSwapRate (Size i, Size spanningForwards) const =0



virtual const std::vector&lt; Rate &gt; &amp; forwardRates () const =0



virtual const std::vector&lt; Rate &gt; &amp; coterminalSwapRates () const =0



virtual const std::vector&lt; Rate &gt; &amp; cmSwapRates (Size spanningForwards) const =0



Rate swapRate (Size begin, Size end) const



virtual std::auto_ptr&lt; CurveState &gt; clone () const =0



Protected Attributes</code></pre>
<p> Size <code>numberOfRates_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>rateTimes_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>rateTaus_</code></p>
<h2>Detailed Description</h2>
<p>Curve state for market-model simulations </p>
<p> This class stores the state of the yield curve associated to the fixed calendar times within the simulation. This is the workhorse discounting object associated to the rate times of the simulation. It&#8217;s important to pass the rates via an object like this to the product rather than directly to make it easier to switch to other engines such as a coterminal swap rate engine. Many products will not need expired rates and others will only require the first rate.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
