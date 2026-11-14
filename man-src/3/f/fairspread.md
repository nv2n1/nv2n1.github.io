---
title: "fairspread(3)"
name: "fairspread"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fairspread/"
description: "QuantLib::RiskyAssetSwap – Risky asset-swap instrument."
---

<p>QuantLib::RiskyAssetSwap &#8211; Risky asset-swap instrument. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/riskyassetswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p><code>RiskyAssetSwap</code> (bool fixedPayer, Real nominal, const <code>Schedule</code> &amp;fixedSchedule, const <code>Schedule</code> &amp;floatSchedule, const <code>DayCounter</code> &amp;fixedDayCounter, const <code>DayCounter</code> &amp;floatDayCounter, <code>Rate</code> spread, <code>Rate</code> recoveryRate_, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS, const <code>Handle</code>&lt; <code>DefaultProbabilityTermStructure</code> &gt; &amp;defaultTS, <code>Rate</code> coupon=<code>Null</code>&lt; <code>Rate</code> &gt;()) </p>
<p> Real <code>fairSpread</code> () </p>
<p> Real <code>floatAnnuity</code> () const </p>
<p> Real <code>nominal</code> () </p>
<p> <code>Rate</code> <code>spread</code> () </p>
<p> bool <code>fixedPayer</code> () </p>
<h2>Detailed Description</h2>
<p>Risky asset-swap instrument. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
