---
title: "quantlib_flatforward(3)"
name: "quantlib_flatforward"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_flatforward/"
description: "QuantLib::FlatForward – Flat interest-rate curve."
---

<p>QuantLib::FlatForward &#8211; Flat interest-rate curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/flatforward.hpp&gt; </p>
<p> Inherits <code>QuantLib::YieldTermStructure</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FlatForward</code> (const <code>Date</code> &amp;referenceDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;forward, const <code>DayCounter</code> &amp;dayCounter, Compounding compounding=Continuous, <code>Frequency</code> frequency=Annual) </p>
<p> <code>FlatForward</code> (const <code>Date</code> &amp;referenceDate, Rate forward, const <code>DayCounter</code> &amp;dayCounter, Compounding compounding=Continuous, <code>Frequency</code> frequency=Annual) </p>
<p> <code>FlatForward</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;forward, const <code>DayCounter</code> &amp;dayCounter, Compounding compounding=Continuous, <code>Frequency</code> frequency=Annual) </p>
<p> <code>FlatForward</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, Rate forward, const <code>DayCounter</code> &amp;dayCounter, Compounding compounding=Continuous, <code>Frequency</code> frequency=Annual) </p>
<p> Compounding <code>compounding</code> () const </p>
<p> <code>Frequency</code> <code>compoundingFrequency</code> () const </p>
<p> virtual void <code>performCalculations</code> () const </p>
<p> <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i><br />
 void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p>Flat interest-rate curve. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, <code>Replication.cpp</code>, and <code>Repo.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
