---
title: "quantlib_swaptionvolatilitycube(3)"
name: "quantlib_swaptionvolatilitycube"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_swaptionvolatilitycube/"
description: "QuantLib::SwaptionVolatilityCube – swaption-volatility cube"
---

<p>QuantLib::SwaptionVolatilityCube &#8211; swaption-volatility cube </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/swaption/swaptionvolcube.hpp&gt; </p>
<p> Inherits QuantLib::SwaptionVolatilityDiscrete. </p>
<p> Inherited by SwaptionVolCube1, and SwaptionVolCube2. </p>
<h3>Public Member Functions</h3>
<p><code>SwaptionVolatilityCube</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;atmVolStructure, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const std::vector&lt; <code>Spread</code> &gt; &amp;strikeSpreads, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;volSpreads, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndexBase, const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;shortSwapIndexBase, bool vegaWeightedSmileFit) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 Time <code>maxTime</code> () const<br />
 <i>the latest time for which the curve can return values </i><br />
 const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 <code>Calendar</code> <code>calendar</code> () const<br />
 <i>the calendar used for reference and/or option date calculation </i><br />
 <code>Natural</code> <code>settlementDays</code> () const<br />
 <i>the settlementDays used for reference date calculation </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Rate <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Rate <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>SwaptionVolatilityStructure interface</code> </p>
<p> const <code>Period</code> &amp; <code>maxSwapTenor</code> () const<br />
 <i>the largest length for which the term structure can return vols </i> </p>
<p> <code>Other inspectors</code> </p>
<p> Rate <code>atmStrike</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor) const </p>
<p> Rate <code>atmStrike</code> (const <code>Period</code> &amp;optionTenor, const <code>Period</code> &amp;swapTenor) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>registerWithVolatilitySpread</code> () </p>
<p> <code>Volatility</code> <code>volatilityImpl</code> (Time optionTime, Time swapLength, Rate strike) const </p>
<p> <code>Volatility</code> <code>volatilityImpl</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor, Rate strike) const </p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; <code>atmVol_</code> </p>
<p> Size <code>nStrikes_</code> </p>
<p> std::vector&lt; <code>Spread</code> &gt; <code>strikeSpreads_</code> </p>
<p> std::vector&lt; Rate &gt; <code>localStrikes_</code> </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>localSmile_</code> </p>
<p> std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; <code>volSpreads_</code> </p>
<p> boost::shared_ptr&lt; <code>SwapIndex</code> &gt; <code>swapIndexBase_</code> </p>
<p> boost::shared_ptr&lt; <code>SwapIndex</code> &gt; <code>shortSwapIndexBase_</code> </p>
<p> bool <code>vegaWeightedSmileFit_</code> </p>
<h2>Detailed Description</h2>
<p>swaption-volatility cube </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>this class is not finalized and its interface might change in subsequent releases.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
