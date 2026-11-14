---
title: "tenor(3)"
name: "tenor"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tenor/"
description: "QuantLib::InterestRateIndex – base class for interest rate indexes"
---

<p>QuantLib::InterestRateIndex &#8211; base class for interest rate indexes </p>
<h2>Synopsis</h2>
<pre><code>virtual Date valueDate (const Date &amp;fixingDate) const



virtual Date maturityDate (const Date &amp;valueDate) const =0



Protected Member Functions
virtual Rate forecastFixing (const Date &amp;fixingDate) const =0



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Index</code>, and <code>QuantLib::Observer</code>. Inherited by <code>BMAIndex</code>, <code>IborIndex</code>, and <code>SwapIndex</code>.</p>
<h3>Public Member Functions</h3>
<p><code>InterestRateIndex</code> (const std::string &amp;familyName, const <code>Period</code> &amp;tenor, <code>Natural</code> settlementDays, const <code>Currency</code> &amp;currency, const <code>Calendar</code> &amp;fixingCalendar, const <code>DayCounter</code> &amp;dayCounter)<br />
 <code>Index interface</code><br />
 virtual Date valueDate (const Date &amp;fixingDate) const</p>
<p>virtual Date maturityDate (const Date &amp;valueDate) const =0</p>
<p>Protected Member Functions<br />
virtual Rate forecastFixing (const Date &amp;fixingDate) const =0</p>
<p>Protected Attributes <code>Observer interface</code><br />
 virtual Date valueDate (const Date &amp;fixingDate) const</p>
<p>virtual Date maturityDate (const Date &amp;valueDate) const =0</p>
<p>Protected Member Functions<br />
virtual Rate forecastFixing (const Date &amp;fixingDate) const =0</p>
<p>Protected Attributes <code>Inspectors</code><br />
 virtual Date valueDate (const Date &amp;fixingDate) const</p>
<p>virtual Date maturityDate (const Date &amp;valueDate) const =0</p>
<p>Protected Member Functions<br />
virtual Rate forecastFixing (const Date &amp;fixingDate) const =0</p>
<p>Protected Attributes <code>Date calculations</code><br />
 These method can be overridden to implement particular conventions (e.g. EurLibor) </p>
<pre><code>virtual Date valueDate (const Date &amp;fixingDate) const



virtual Date maturityDate (const Date &amp;valueDate) const =0



Protected Member Functions
virtual Rate forecastFixing (const Date &amp;fixingDate) const =0



Protected Attributes</code></pre>
<p> std::string <code>familyName_</code> </p>
<p> <code>Period</code> <code>tenor_</code> </p>
<p> <code>Natural</code> <code>fixingDays_</code> </p>
<p> <code>Calendar</code> <code>fixingCalendar_</code> </p>
<p> <code>Currency</code> <code>currency_</code> </p>
<p> <code>DayCounter</code> <code>dayCounter_</code></p>
<h2>Detailed Description</h2>
<p>base class for interest rate indexes </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add methods returning <code>InterestRate</code></dl>
<h2>Member Function Documentation</h2>
<h3>std::string name () const [virtual]</h3>
<p>Returns the name of the index. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This method is used for output and comparison between indexes. It is <code>not</code> meant to be used for writing switch-on-type code.</dl>
<p> Implements <code>Index</code>. </p>
<p> Reimplemented in <code>BMAIndex</code>.</p>
<h3><code>Rate</code> fixing (const <code>Date</code> &amp; fixingDate, bool forecastTodaysFixing = false) const [virtual]</h3>
<p>returns the fixing at the given date </p>
<p> the date passed as arguments must be the actual calendar date of the fixing; no settlement days must be used. </p>
<p> Implements <code>Index</code>.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
