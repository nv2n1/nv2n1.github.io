---
title: "quantlib_assetswap(3)"
name: "quantlib_assetswap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_assetswap/"
description: "QuantLib::AssetSwap – Bullet bond vs Libor swap."
---

<p>QuantLib::AssetSwap &#8211; Bullet bond vs Libor swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/assetswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::Swap</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for asset swap calculation </i><br />
 class <code>results</code><br />
 <i>Results from simple swap calculation </i></p>
<h3>Public Member Functions</h3>
<p><code>AssetSwap</code> (bool payFixedRate, const boost::shared_ptr&lt; <code>Bond</code> &gt; &amp;bond, Real bondCleanPrice, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, <code>Spread</code> spread, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve, const <code>Schedule</code> &amp;floatSchedule=<code>Schedule</code>(), const <code>DayCounter</code> &amp;floatingDayCount=<code>DayCounter</code>(), bool parAssetSwap=true) </p>
<p> <code>Spread</code> <code>fairSpread</code> () const </p>
<p> Real <code>floatingLegBPS</code> () const </p>
<p> Real <code>fairPrice</code> () const </p>
<p> <code>Spread</code> <code>spread</code> () const </p>
<p> Real <code>nominal</code> () const </p>
<p> bool <code>payFixedRate</code> () const </p>
<p> const Leg &amp; <code>bondLeg</code> () const </p>
<p> const Leg &amp; <code>floatingLeg</code> () const </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<h2>Detailed Description</h2>
<p>Bullet bond vs Libor swap. </p>
<p> for mechanics of par asset swap and market asset swap, refer to &#8216;Introduction to Asset Swap&#8217;, Lehman Brothers European Fixed Income Research &#8211; January 2000, D. O&#8217;Kane </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>fair prices are not calculated correctly when using indexed coupons.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
