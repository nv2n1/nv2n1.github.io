---
title: "quantlib_event(3)"
name: "quantlib_event"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_event/"
description: "QuantLib::Event – Base class for event."
---

<p>QuantLib::Event &#8211; Base class for event. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/event.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>Callability</code>, <code>CashFlow</code>, and <code>DefaultEvent</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Event interface</code> </p>
<p> virtual <code>Date</code> <code>date</code> () const =0<br />
 <i>returns the date at which the event occurs </i><br />
 bool <code>hasOccurred</code> (const <code>Date</code> &amp;d, bool includeToday=false) const<br />
 <i>returns true if an event has already occurred before a date </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Base class for event. </p>
<p> This class acts as a base class for the actual event implementations.</p>
<h2>Member Function Documentation</h2>
<h3>bool hasOccurred (const <code>Date</code> &amp; d, bool includeToday = false) const</h3>
<p>returns true if an event has already occurred before a date </p>
<p> If QL_TODAYS_PAYMENT is true, then a payment event has not occurred if the input date is the same as the event date, and so includeToday should be defaulted to true. </p>
<p> This should be the only place in the code that is affected directly by QL_TODAYS_PAYMENT </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
