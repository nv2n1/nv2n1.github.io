---
title: "cdsoption(3)"
name: "cdsoption"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdsoption/"
description: "QuantLib::CdsOption – CDS option."
---

<p>QuantLib::CdsOption &#8211; CDS option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/cdsoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p><code>CdsOption</code> (const <code>Date</code> &amp;expiry, <code>Rate</code> strike, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const Issuer &amp;issuer, Protection::Side side, Real nominal, const <code>Schedule</code> &amp;premiumSchedule, const <code>DayCounter</code> &amp;dayCounter, bool settlePremiumAccrual, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> Real <code>forward</code> () const </p>
<p> Real <code>riskyAnnuity</code> () const </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i></p>
<h2>Detailed Description</h2>
<p>CDS option. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>the current implementation does not take premium accrual into account</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>the current implementation quietly assumes that the expiry equals the start date of the underlying CDS</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>take premium accrual into account</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>allow expiry to be different from CDS start date</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
