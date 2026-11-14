---
title: "atmcurve(3)"
name: "atmcurve"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atmcurve/"
description: "QuantLib::SabrVolSurface – SABR volatility (smile) surface."
---

<p>QuantLib::SabrVolSurface &#8211; <code>SABR</code> volatility (smile) surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/volatility/sabrvolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::InterestRateVolSurface</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SabrVolSurface</code> (const boost::shared_ptr&lt; <code>InterestRateIndex</code> &gt; &amp;, const <code>Handle</code>&lt; <code>BlackAtmVolCurve</code> &gt; &amp;, const std::vector&lt; <code>Period</code> &gt; &amp;optionTenors, const std::vector&lt; <code>Spread</code> &gt; &amp;atmRateSpreads, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;volSpreads) </p>
<p> const <code>Handle</code>&lt; <code>BlackAtmVolCurve</code> &gt; &amp; <code>atmCurve</code> () const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>volatilitySpreads</code> (const <code>Period</code> &amp;) const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>volatilitySpreads</code> (const <code>Date</code> &amp;) const </p>
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
<p> <code>Real</code> <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 <code>Real</code> <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<p> <code>BlackVolSurface interface</code> </p>
<p> boost::shared_ptr&lt; <code>SmileSection</code> &gt; <code>smileSectionImpl</code> (Time) const </p>
<h3>Protected Member Functions</h3>
<p>boost::array&lt; <code>Real</code>, 4 &gt; <code>sabrGuesses</code> (const <code>Date</code> &amp;) const </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>performCalculations</code> () const </p>
<p> virtual void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p><code>SABR</code> volatility (smile) surface. </p>
<p> blah blah</p>
<h2>Member Function Documentation</h2>
<h3>virtual void update () [protected, virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>TermStructure</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
