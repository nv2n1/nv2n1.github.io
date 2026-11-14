---
title: "payfixedrate(3)"
name: "payfixedrate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-payfixedrate/"
description: "QuantLib::AssetSwap – Bullet bond vs Libor swap."
---

<p>QuantLib::AssetSwap &#8211; Bullet bond vs Libor swap. </p>
<h2>Synopsis</h2>
<pre><code>AssetSwap (bool payFixedRate, const boost::shared_ptr&lt; Bond &gt; &amp;bond, Real bondCleanPrice, const boost::shared_ptr&lt; IborIndex &gt; &amp;index, Spread spread, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, const Schedule &amp;floatSchedule=Schedule(), const DayCounter &amp;floatingDayCount=DayCounter(), bool parAssetSwap=true)



Spread fairSpread () const



Real floatingLegBPS () const



Real fairPrice () const



Spread spread () const



Real nominal () const



bool payFixedRate () const



const Leg &amp; bondLeg () const



const Leg &amp; floatingLeg () const



void setupArguments (PricingEngine::arguments *args) const



void fetchResults (const PricingEngine::results *) const</code></pre>
<p> Inherits <code>QuantLib::Swap</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for asset swap calculation </i><br />
 class <code>results</code><br />
 <i>Results from simple swap calculation </i></p>
<h3>Public Member Functions</h3>
<pre><code>AssetSwap (bool payFixedRate, const boost::shared_ptr&lt; Bond &gt; &amp;bond, Real bondCleanPrice, const boost::shared_ptr&lt; IborIndex &gt; &amp;index, Spread spread, const Handle&lt; YieldTermStructure &gt; &amp;discountCurve, const Schedule &amp;floatSchedule=Schedule(), const DayCounter &amp;floatingDayCount=DayCounter(), bool parAssetSwap=true)



Spread fairSpread () const



Real floatingLegBPS () const



Real fairPrice () const



Spread spread () const



Real nominal () const



bool payFixedRate () const



const Leg &amp; bondLeg () const



const Leg &amp; floatingLeg () const



void setupArguments (PricingEngine::arguments *args) const



void fetchResults (const PricingEngine::results *) const</code></pre>
<h2>Detailed Description</h2>
<p>Bullet bond vs Libor swap. </p>
<p> for mechanics of par asset swap and market asset swap, refer to &#8216;Introduction to Asset Swap&#8217;, Lehman Brothers European Fixed Income Research &#8211; January 2000, D. O&#8217;Kane </p>
<p> <code>Bug</code></p>
<dl>
<dd>fair prices are not calculated correctly when using indexed coupons.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Swap</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
