---
title: "hestonmodelhelper(3)"
name: "hestonmodelhelper"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hestonmodelhelper/"
description: "QuantLib::HestonModelHelper – calibration helper for Heston model"
---

<p>QuantLib::HestonModelHelper &#8211; calibration helper for Heston model </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/equity/hestonmodelhelper.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibrationHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>HestonModelHelper</code> (const <code>Period</code> &amp;maturity, const <code>Calendar</code> &amp;calendar, const Real s0, const Real strikePrice, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendYield, bool calibrateVolatility=false) </p>
<p> void <code>addTimesTo</code> (std::list&lt; Time &gt; &amp;) const </p>
<p> Real <code>modelValue</code> () const<br />
 <i>returns the price of the instrument according to the model </i><br />
 Real <code>blackPrice</code> (Real volatility) const </p>
<p> Time <code>maturity</code> () const </p>
<h2>Detailed Description</h2>
<p>calibration helper for Heston model </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
