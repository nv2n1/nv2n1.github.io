---
title: "quantlib_caphelper(3)"
name: "quantlib_caphelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_caphelper/"
description: "QuantLib::CapHelper – calibration helper for ATM cap"
---

<p>QuantLib::CapHelper &#8211; calibration helper for ATM cap </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/calibrationhelpers/caphelper.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibrationHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CapHelper</code> (const <code>Period</code> &amp;length, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, <code>Frequency</code> fixedLegFrequency, const <code>DayCounter</code> &amp;fixedLegDayCounter, bool includeFirstSwaplet, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, bool calibrateVolatility=false) </p>
<p> virtual void <code>addTimesTo</code> (std::list&lt; Time &gt; &amp;times) const </p>
<p> virtual <code>Real</code> <code>modelValue</code> () const<br />
 <i>returns the price of the instrument according to the model </i><br />
 virtual <code>Real</code> <code>blackPrice</code> (Volatility volatility) const<br />
 <i>Black price given a volatility. </i></p>
<h2>Detailed Description</h2>
<p>calibration helper for ATM cap </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>This helper does not register with the passed IBOR index and with the evaluation date. Furthermore, the ATM strike rate is not recalculated when any of its observables change.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
