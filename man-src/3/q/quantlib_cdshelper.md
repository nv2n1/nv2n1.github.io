---
title: "quantlib_cdshelper(3)"
name: "quantlib_cdshelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cdshelper/"
description: "QuantLib::CdsHelper – Default-probability bootstrap helper based on quoted CDS spreads."
---

<p>QuantLib::CdsHelper &#8211; Default-probability bootstrap helper based on quoted CDS spreads. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/defaultprobabilityhelpers.hpp&gt; </p>
<p> Inherits <code>BootstrapHelper&lt; DefaultProbabilityTermStructure &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CdsHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread, const <code>Period</code> &amp;tenor, <code>Integer</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Frequency</code> frequency, <code>BusinessDayConvention</code> paymentConvention, <code>DateGeneration::Rule</code> rule, const <code>DayCounter</code> &amp;dayCounter, <code>Real</code> recoveryRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, bool settlesAccrual=true, bool paysAtDefaultTime=true) </p>
<p> <code>CdsHelper</code> (<code>Rate</code> spread, const <code>Period</code> &amp;tenor, <code>Integer</code> settlementDays, const <code>Calendar</code> &amp;calendar, <code>Frequency</code> frequency, <code>BusinessDayConvention</code> paymentConvention, <code>DateGeneration::Rule</code> rule, const <code>DayCounter</code> &amp;dayCounter, <code>Real</code> recoveryRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, bool settlesAccrual=true, bool paysAtDefaultTime=true) </p>
<p> <code>Real</code> <code>impliedQuote</code> () const </p>
<p> void <code>setTermStructure</code> (<code>DefaultProbabilityTermStructure</code> *)<br />
 <i>sets the term structure to be used for pricing </i></p>
<h2>Detailed Description</h2>
<p>Default-probability bootstrap helper based on quoted CDS spreads. </p>
<p> <code>Examples: </code> </p>
<p> <code>CDS.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void setTermStructure (<code>DefaultProbabilityTermStructure</code> *) [virtual]</h3>
<p>sets the term structure to be used for pricing </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Being a pointer and not a shared_ptr, the term structure is not guaranteed to remain allocated for the whole life of the rate helper. It is responsibility of the programmer to ensure that the pointer remains valid. It is advised that this method is called only inside the term structure being bootstrapped, setting the pointer to <code>this</code>, i.e., the term structure itself.</dl>
<p> Reimplemented from <code>BootstrapHelper&lt; DefaultProbabilityTermStructure &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
