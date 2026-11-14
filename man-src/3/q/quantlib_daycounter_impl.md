---
title: "quantlib_daycounter_impl(3)"
name: "quantlib_daycounter_impl"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_daycounter_impl/"
description: "QuantLib::DayCounter::Impl – abstract base class for day counter implementations"
---

<p>QuantLib::DayCounter::Impl &#8211; abstract base class for day counter implementations </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/time/daycounter.hpp&gt; </p>
<p> Inherited by Impl, Impl, AFB_Impl, ISDA_Impl, ISMA_Impl, Impl, Impl, Impl, EU_Impl, IT_Impl, and US_Impl. </p>
<h3>Public Member Functions</h3>
<p>virtual std::string <code>name</code> () const =0 </p>
<p> virtual <code>BigInteger</code> <code>dayCount</code> (const <code>Date</code> &amp;d1, const <code>Date</code> &amp;d2) const<br />
 <i>to be overloaded by more complex day counters </i><br />
 virtual <code>Time</code> <code>yearFraction</code> (const <code>Date</code> &amp;d1, const <code>Date</code> &amp;d2, const <code>Date</code> &amp;refPeriodStart, const <code>Date</code> &amp;refPeriodEnd) const =0 </p>
<h2>Detailed Description</h2>
<p>abstract base class for day counter implementations </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
