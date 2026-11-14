---
title: "setoncoterminalswaprates(3)"
name: "setoncoterminalswaprates"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setoncoterminalswaprates/"
description: "QuantLib::CoterminalSwapCurveState – Curve state for coterminal-swap market models"
---

<p>QuantLib::CoterminalSwapCurveState &#8211; Curve state for coterminal-swap market models </p>
<h2>Synopsis</h2>
<pre><code>void setOnCoterminalSwapRates (const std::vector&lt; Rate &gt; &amp;swapRates, Size firstValidIndex=0)</code></pre>
<p> Inherits <code>QuantLib::CurveState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CoterminalSwapCurveState</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes) </p>
<p> std::auto_ptr&lt; <code>CurveState</code> &gt; <code>clone</code> () const<br />
 <code>Modifiers</code> </p>
<pre><code>void setOnCoterminalSwapRates (const std::vector&lt; Rate &gt; &amp;swapRates, Size firstValidIndex=0)</code></pre>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>discountRatio</code> (Size i, Size j) const </p>
<p> <code>Rate</code> <code>forwardRate</code> (Size i) const </p>
<p> <code>Rate</code> <code>coterminalSwapRate</code> (Size i) const </p>
<p> <code>Rate</code> <code>coterminalSwapAnnuity</code> (Size numeraire, Size i) const </p>
<p> <code>Rate</code> <code>cmSwapRate</code> (Size i, Size spanningForwards) const </p>
<p> <code>Rate</code> <code>cmSwapAnnuity</code> (Size numeraire, Size i, Size spanningForwards) const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>forwardRates</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>coterminalSwapRates</code> () const </p>
<p> const std::vector&lt; <code>Rate</code> &gt; &amp; <code>cmSwapRates</code> (Size spanningForwards) const</p>
<h2>Detailed Description</h2>
<p>Curve state for coterminal-swap market models </p>
<p> This class stores the state of the yield curve associated to the fixed calendar times within the simulation. This is the workhorse discounting object associated to the rate times of the simulation. It&#8217;s important to pass the rates via an object like this to the product rather than directly to make it easier to switch to other engines such as a coterminal swap rate engine. Many products will not need expired rates and others will only require the first rate.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
