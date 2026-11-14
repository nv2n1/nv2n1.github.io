---
title: "swaplength(3)"
name: "swaplength"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swaplength/"
description: "QuantLib::SwaptionVolatilityStructure – Swaption-volatility structure"
---

<p>QuantLib::SwaptionVolatilityStructure &#8211; Swaption-volatility structure </p>
<h2>Synopsis</h2>
<pre><code>virtual const Period &amp; maxSwapTenor () const =0


the largest length for which the term structure can return vols


Time maxSwapLength () const


the largest swapLength for which the term structure can return vols




Protected Member Functions
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (const Date &amp;optionDate, const Period &amp;swapTenor) const



virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time swapLength) const =0



virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const



virtual Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const =0



void checkSwapTenor (const Period &amp;swapTenor, bool extrapolate) const



void checkSwapTenor (Time swapLength, bool extrapolate) const</code></pre>
<p> Inherits <code>QuantLib::VolatilityTermStructure</code>. Inherited by <code>ConstantSwaptionVolatility</code>, SpreadedSwaptionVolatility, and SwaptionVolatilityDiscrete.</p>
<h3>Public Member Functions</h3>
<p>Time <code>swapLength</code> (const <code>Period</code> &amp;swapTenor) const<br />
 <i>implements the conversion between swap tenor and swap (time) length </i><br />
 Time <code>swapLength</code> (const <code>Date</code> &amp;start, const <code>Date</code> &amp;end) const<br />
 <i>implements the conversion between swap dates and swap (time) length </i> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. virtual const Period &amp; maxSwapTenor () const =0</p>
<p>the largest length for which the term structure can return vols</p>
<p>Time maxSwapLength () const</p>
<p>the largest swapLength for which the term structure can return vols</p>
<p>Protected Member Functions<br />
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (const Date &amp;optionDate, const Period &amp;swapTenor) const</p>
<p>virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time swapLength) const =0</p>
<p>virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const</p>
<p>virtual Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const =0</p>
<p>void checkSwapTenor (const Period &amp;swapTenor, bool extrapolate) const</p>
<p>void checkSwapTenor (Time swapLength, bool extrapolate) const <code>Volatility, variance and smile</code><br />
 virtual const Period &amp; maxSwapTenor () const =0</p>
<p>the largest length for which the term structure can return vols</p>
<p>Time maxSwapLength () const</p>
<p>the largest swapLength for which the term structure can return vols</p>
<p>Protected Member Functions<br />
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (const Date &amp;optionDate, const Period &amp;swapTenor) const</p>
<p>virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time swapLength) const =0</p>
<p>virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const</p>
<p>virtual Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const =0</p>
<p>void checkSwapTenor (const Period &amp;swapTenor, bool extrapolate) const</p>
<p>void checkSwapTenor (Time swapLength, bool extrapolate) const <code>Limits</code> </p>
<pre><code>virtual const Period &amp; maxSwapTenor () const =0


the largest length for which the term structure can return vols


Time maxSwapLength () const


the largest swapLength for which the term structure can return vols




Protected Member Functions
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (const Date &amp;optionDate, const Period &amp;swapTenor) const



virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time swapLength) const =0



virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;swapTenor, Rate strike) const



virtual Volatility volatilityImpl (Time optionTime, Time swapLength, Rate strike) const =0



void checkSwapTenor (const Period &amp;swapTenor, bool extrapolate) const



void checkSwapTenor (Time swapLength, bool extrapolate) const</code></pre>
<h2>Detailed Description</h2>
<p>Swaption-volatility structure </p>
<p> This abstract class defines the interface of concrete swaption volatility structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>SwaptionVolatilityStructure</code> (const <code>Calendar</code> &amp; calendar, <code>BusinessDayConvention</code> bdc, const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>())</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
