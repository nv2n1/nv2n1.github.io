---
title: "marketvalue(3)"
name: "marketvalue"
section: "3"
letter: "m"
url: "/docs/linux/man/3-marketvalue/"
description: "QuantLib::CalibrationHelper – liquid market instrument used during calibration"
---

<p>QuantLib::CalibrationHelper &#8211; liquid market instrument used during calibration </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/calibrationhelper.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>CapHelper</code>, <code>HestonModelHelper</code>, and <code>SwaptionHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CalibrationHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, bool calibrateVolatility=false) </p>
<p> void <code>update</code> () </p>
<p> <code>Real</code> <code>marketValue</code> () const<br />
 <i>returns the actual price of the instrument (from volatility) </i><br />
 virtual <code>Real</code> <code>modelValue</code> () const =0<br />
 <i>returns the price of the instrument according to the model </i><br />
 virtual <code>Real</code> <code>calibrationError</code> ()<br />
 <i>returns the error resulting from the model valuation </i><br />
 virtual void <code>addTimesTo</code> (std::list&lt; Time &gt; &amp;times) const =0 </p>
<p> Volatility <code>impliedVolatility</code> (<code>Real</code> targetValue, <code>Real</code> accuracy, Size maxEvaluations, Volatility minVol, Volatility maxVol) const<br />
 <i>Black volatility implied by the model. </i><br />
 virtual <code>Real</code> <code>blackPrice</code> (Volatility volatility) const =0<br />
 <i>Black price given a volatility. </i><br />
 void <code>setPricingEngine</code> (const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp;engine) </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>marketValue_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>volatility_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>termStructure_</code> </p>
<p> boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>engine_</code> </p>
<h2>Detailed Description</h2>
<p>liquid market instrument used during calibration</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
