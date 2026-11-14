---
title: "shortswapindexbase_(3)"
name: "shortswapindexbase_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shortswapindexbase_/"
description: "QuantLib::SwaptionVolatilityCube – swaption-volatility cube"
---

<p>QuantLib::SwaptionVolatilityCube &#8211; swaption-volatility cube </p>
<h2>Synopsis</h2>
<pre><code>void registerWithVolatilitySpread ()



Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const



Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const



Protected Attributes</code></pre>
<p> Inherits QuantLib::SwaptionVolatilityDiscrete. Inherited by SwaptionVolCube1, and SwaptionVolCube2.</p>
<h3>Public Member Functions</h3>
<p><code>SwaptionVolatilityCube</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;atmVolStructure, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const std::vector&lt; <code>Spread</code> &gt; &amp;strikeSpreads, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;volSpreads, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndexBase, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;shortSwapIndexBase, bool vegaWeightedSmileFit)<br />
 <code>TermStructure interface</code><br />
 void registerWithVolatilitySpread ()</p>
<p>Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const</p>
<p>Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const</p>
<p>Protected Attributes <code>VolatilityTermStructure interface</code> </p>
<p> Rate <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Rate <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> <code>SwaptionVolatilityStructure interface</code><br />
 void registerWithVolatilitySpread ()</p>
<p>Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const</p>
<p>Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const</p>
<p>Protected Attributes <code>Other inspectors</code> </p>
<p> Rate <code>atmStrike</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor) const </p>
<p> Rate <code>atmStrike</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;swapTenor) const</p>
<h3>Protected Member Functions</h3>
<pre><code>void registerWithVolatilitySpread ()



Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const



Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const



Protected Attributes</code></pre>
<p> <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; <code>atmVol_</code> </p>
<p> Size <code>nStrikes_</code> </p>
<p> std::vector&lt; <code>Spread</code> &gt; <code>strikeSpreads_</code> </p>
<p> std::vector&lt; Rate &gt; <code>localStrikes_</code> </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>localSmile_</code> </p>
<p> std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; <code>volSpreads_</code> </p>
<p> boost::shared_ptr&lt; <code>SwapIndex</code> &gt; <code>swapIndexBase_</code> </p>
<p> boost::shared_ptr&lt; <code>SwapIndex</code> &gt; <code>shortSwapIndexBase_</code> </p>
<p> bool <code>vegaWeightedSmileFit_</code></p>
<h2>Detailed Description</h2>
<p>swaption-volatility cube </p>
<p> <code>Warning</code></p>
<dl>
<dd>this class is not finalized and its interface might change in subsequent releases.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
