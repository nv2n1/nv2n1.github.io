---
title: "quantlib_swaptionvolatilitymatrix(3)"
name: "quantlib_swaptionvolatilitymatrix"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_swaptionvolatilitymatrix/"
description: "QuantLib::SwaptionVolatilityMatrix – At-the-money swaption-volatility matrix."
---

<p>QuantLib::SwaptionVolatilityMatrix &#8211; At-the-money swaption-volatility matrix. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/swaption/swaptionvolmatrix.hpp&gt; </p>
<p> Inherits QuantLib::SwaptionVolatilityDiscrete, and boost::noncopyable. </p>
<h3>Public Member Functions</h3>
<p><code>SwaptionVolatilityMatrix</code> (const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;vols, const <code>DayCounter</code> &amp;dayCounter)<br />
 <i>floating reference date, floating market data </i><br />
 <code>SwaptionVolatilityMatrix</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;vols, const <code>DayCounter</code> &amp;dayCounter)<br />
 <i>fixed reference date, floating market data </i><br />
 <code>SwaptionVolatilityMatrix</code> (const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const <code>Matrix</code> &amp;volatilities, const <code>DayCounter</code> &amp;dayCounter)<br />
 <i>floating reference date, fixed market data </i><br />
 <code>SwaptionVolatilityMatrix</code> (const <code>Date</code> &amp;referenceDate, const <code>Calendar</code> &amp;calendar, <code>BusinessDayConvention</code> bdc, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const <code>Matrix</code> &amp;volatilities, const <code>DayCounter</code> &amp;dayCounter)<br />
 <i>fixed reference date, fixed market data </i><br />
 <code>SwaptionVolatilityMatrix</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; <code>Date</code> &gt; &amp;optionDates, const std::vector&lt; <code>Period</code> &gt; &amp;swapTenors, const <code>Matrix</code> &amp;volatilities, const <code>DayCounter</code> &amp;dayCounter) </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>performCalculations</code> () const </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Rate <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Rate <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>SwaptionVolatilityStructure interface</code> </p>
<p> const <code>Period</code> &amp; <code>maxSwapTenor</code> () const<br />
 <i>the largest length for which the term structure can return vols </i> </p>
<p> <code>Other inspectors</code> </p>
<p> std::pair&lt; Size, Size &gt; <code>locate</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;swapTenor) const<br />
 <i>returns the lower indexes of surrounding volatility matrix corners </i><br />
 std::pair&lt; Size, Size &gt; <code>locate</code> (Time optionTime, Time swapLength) const<br />
 <i>returns the lower indexes of surrounding volatility matrix corners </i></p>
<h3>Protected Member Functions</h3>
<p>boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time, Time) const </p>
<p> <code>Volatility</code> <code>volatilityImpl</code> (Time optionTime, Time swapLength, Rate strike) const </p>
<h2>Detailed Description</h2>
<p>At-the-money swaption-volatility matrix. </p>
<p> This class provides the at-the-money volatility for a given swaption by interpolating a volatility matrix whose elements are the market volatilities of a set of swaption with given option date and swapLength. </p>
<p> The volatility matrix M must be defined so that:</p>
<dl COMPACT>
<dt>*</p>
<dd>the number of rows equals the number of option dates;</p>
<dt>*</p>
<dd>the number of columns equals the number of swap tenors;</p>
<dt>*</p>
<dd>M[i][j] contains the volatility corresponding to the i-th option and j-th tenor.</dl>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
