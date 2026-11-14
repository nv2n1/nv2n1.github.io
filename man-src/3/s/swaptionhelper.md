---
title: "swaptionhelper(3)"
name: "swaptionhelper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swaptionhelper/"
description: "QuantLib::SwaptionHelper – calibration helper for ATM swaption"
---

<p>QuantLib::SwaptionHelper &#8211; calibration helper for ATM swaption </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/calibrationhelpers/swaptionhelper.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibrationHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SwaptionHelper</code> (const <code>Period</code> &amp;maturity, const <code>Period</code> &amp;length, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const <code>Period</code> &amp;fixedLegTenor, const <code>DayCounter</code> &amp;fixedLegDayCounter, const <code>DayCounter</code> &amp;floatingLegDayCounter, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, bool calibrateVolatility=false) </p>
<p> virtual void <code>addTimesTo</code> (std::list&lt; Time &gt; &amp;times) const </p>
<p> virtual Real <code>modelValue</code> () const<br />
 <i>returns the price of the instrument according to the model </i><br />
 virtual Real <code>blackPrice</code> (Volatility volatility) const<br />
 <i>Black price given a volatility. </i></p>
<h2>Detailed Description</h2>
<p>calibration helper for ATM swaption </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM exercise rate is not recalculated when any of its observables change.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
