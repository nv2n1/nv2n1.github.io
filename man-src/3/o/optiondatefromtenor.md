---
title: "optiondatefromtenor(3)"
name: "optiondatefromtenor"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optiondatefromtenor/"
description: "QuantLib::CallableBondVolatilityStructure – Callable-bond volatility structure."
---

<p>QuantLib::CallableBondVolatilityStructure &#8211; Callable-bond volatility structure. </p>
<h2>Synopsis</h2>
<pre><code>virtual const Period &amp; maxBondTenor () const =0


the largest length for which the term structure can return vols


virtual Time maxBondLength () const


the largest bondLength for which the term structure can return vols


virtual Rate minStrike () const =0


the minimum strike for which the term structure can return vols


virtual Rate maxStrike () const =0


the maximum strike for which the term structure can return vols




Protected Member Functions
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const =0


return smile section


virtual Volatility volatilityImpl (Time optionTime, Time bondLength, Rate strike) const =0


implements the actual volatility calculation in derived classes


virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike) const



void checkRange (Time, Time, Rate strike, bool extrapolate) const



void checkRange (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike, bool extrapolate) const</code></pre>
<p> Inherits <code>QuantLib::TermStructure</code>. Inherited by <code>CallableBondConstantVolatility</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual std::pair&lt; Time, Time &gt; <code>convertDates</code> (const <code>Date</code> &amp;optionDate, const <code>Period</code> &amp;bondTenor) const<br />
 <i>implements the conversion between dates and times </i><br />
 virtual <code>BusinessDayConvention</code> <code>businessDayConvention</code> () const<br />
 <i>the business day convention used for option date calculation </i><br />
 <code>Date</code> <code>optionDateFromTenor</code> (const <code>Period</code> &amp;optionTenor) const<br />
 <i>implements the conversion between optionTenors and optionDates </i> <code>Constructors</code><br />
 See the <code>TermStructure</code> documentation for issues regarding constructors. virtual const Period &amp; maxBondTenor () const =0</p>
<p>the largest length for which the term structure can return vols</p>
<p>virtual Time maxBondLength () const</p>
<p>the largest bondLength for which the term structure can return vols</p>
<p>virtual Rate minStrike () const =0</p>
<p>the minimum strike for which the term structure can return vols</p>
<p>virtual Rate maxStrike () const =0</p>
<p>the maximum strike for which the term structure can return vols</p>
<p>Protected Member Functions<br />
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const =0</p>
<p>return smile section</p>
<p>virtual Volatility volatilityImpl (Time optionTime, Time bondLength, Rate strike) const =0</p>
<p>implements the actual volatility calculation in derived classes</p>
<p>virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike) const</p>
<p>void checkRange (Time, Time, Rate strike, bool extrapolate) const</p>
<p>void checkRange (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike, bool extrapolate) const <code>Volatility, variance and smile</code><br />
 virtual const Period &amp; maxBondTenor () const =0</p>
<p>the largest length for which the term structure can return vols</p>
<p>virtual Time maxBondLength () const</p>
<p>the largest bondLength for which the term structure can return vols</p>
<p>virtual Rate minStrike () const =0</p>
<p>the minimum strike for which the term structure can return vols</p>
<p>virtual Rate maxStrike () const =0</p>
<p>the maximum strike for which the term structure can return vols</p>
<p>Protected Member Functions<br />
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const =0</p>
<p>return smile section</p>
<p>virtual Volatility volatilityImpl (Time optionTime, Time bondLength, Rate strike) const =0</p>
<p>implements the actual volatility calculation in derived classes</p>
<p>virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike) const</p>
<p>void checkRange (Time, Time, Rate strike, bool extrapolate) const</p>
<p>void checkRange (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike, bool extrapolate) const <code>Limits</code> </p>
<pre><code>virtual const Period &amp; maxBondTenor () const =0


the largest length for which the term structure can return vols


virtual Time maxBondLength () const


the largest bondLength for which the term structure can return vols


virtual Rate minStrike () const =0


the minimum strike for which the term structure can return vols


virtual Rate maxStrike () const =0


the maximum strike for which the term structure can return vols




Protected Member Functions
virtual boost::shared_ptr&lt; SmileSection &gt; smileSectionImpl (Time optionTime, Time bondLength) const =0


return smile section


virtual Volatility volatilityImpl (Time optionTime, Time bondLength, Rate strike) const =0


implements the actual volatility calculation in derived classes


virtual Volatility volatilityImpl (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike) const



void checkRange (Time, Time, Rate strike, bool extrapolate) const



void checkRange (const Date &amp;optionDate, const Period &amp;bondTenor, Rate strike, bool extrapolate) const</code></pre>
<h2>Detailed Description</h2>
<p>Callable-bond volatility structure. </p>
<p> This class is purely abstract and defines the interface of concrete callable-bond volatility structures which will be derived from this one.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CallableBondVolatilityStructure</code> (const <code>DayCounter</code> &amp; dc = <code>DayCounter</code>(), <code>BusinessDayConvention</code> bdc = Following)</h3>
<p>default constructor </p>
<p> <code>Warning</code></p>
<dl>
<dd>term structures initialized by means of this constructor must manage their own reference date by overriding the <code>referenceDate()</code> method.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
