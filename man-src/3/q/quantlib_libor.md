---
title: "quantlib_libor(3)"
name: "quantlib_libor"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_libor/"
description: "QuantLib::Libor – base class for all BBA LIBOR indexes but the EUR, O/N, and S/N ones"
---

<p>QuantLib::Libor &#8211; base class for all BBA LIBOR indexes but the EUR, O/N, and S/N ones </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/ibor/libor.hpp&gt; </p>
<p> Inherits <code>QuantLib::IborIndex</code>. </p>
<p> Inherited by <code>AUDLibor</code>, <code>CADLibor</code>, <code>CHFLibor</code>, <code>DKKLibor</code>, <code>GBPLibor</code>, <code>JPYLibor</code>, <code>NZDLibor</code>, <code>SEKLibor</code>, and <code>USDLibor</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Libor</code> (const std::string &amp;familyName, const <code>Period</code> &amp;tenor, <code>Natural</code> settlementDays, const <code>Currency</code> &amp;currency, const <code>Calendar</code> &amp;financialCenterCalendar, const <code>DayCounter</code> &amp;dayCounter, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> <code>Date calculations</code><br />
 see <a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1412 </p>
<p> <code>Date</code> <code>valueDate</code> (const <code>Date</code> &amp;fixingDate) const </p>
<p> <code>Date</code> <code>maturityDate</code> (const <code>Date</code> &amp;valueDate) const </p>
<p> <code>Other methods</code> </p>
<p> boost::shared_ptr&lt; <code>IborIndex</code> &gt; <code>clone</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h) const<br />
 <i>returns a copy of itself linked to a different forecast curve </i></p>
<h2>Detailed Description</h2>
<p>base class for all BBA LIBOR indexes but the EUR, O/N, and S/N ones </p>
<p> LIBOR fixed by BBA. </p>
<p> See &lt;<a rel="nofollow" href="http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225">http://www.bba.org.uk/bba/jsp/polopoly.jsp?d=225</a>&amp;a=1414&gt;. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
