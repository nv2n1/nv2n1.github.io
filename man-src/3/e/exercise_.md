---
title: "exercise_(3)"
name: "exercise_"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exercise_/"
description: "QuantLib::Option – base option class"
---

<h2 class="name">NAME</h2>
<p> QuantLib::Option &#8211; base option class </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/option.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<p> Inherited by <code>MultiAssetOption</code>, <code>OneAssetOption</code>, and <code>Swaption</code>. </p>
<h3>Classes</h3>
<p> class <code>arguments</code><br />
 <i>basic option arguments </i></p>
<h3>Public Types</h3>
<p> enum <code>Type</code> { <code>Put</code> = -1, <code>Call</code> = 1 } </p>
<h3>Public Member Functions</h3>
<p> <code>Option</code> (const boost::shared_ptr&lt; <code>Payoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff</code> () </p>
<p> boost::shared_ptr&lt; <code>Exercise</code> &gt; <code>exercise</code> () </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff_</code> </p>
<p> boost::shared_ptr&lt; <code>Exercise</code> &gt; <code>exercise_</code> </p>
<h3>Related Functions</h3>
<p> (Note that these are not member functions.)<br />
 std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, Option::Type) </p>
<h2>Detailed Description</h2>
<p> base option class</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p> When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<p> Reimplemented in <code>DividendBarrierOption</code>, <code>ContinuousAveragingAsianOption</code>, <code>DiscreteAveragingAsianOption</code>, <code>BarrierOption</code>, <code>CliquetOption</code>, <code>DividendVanillaOption</code>, <code>ForwardVanillaOption</code>, <code>HimalayaOption</code>, <code>ContinuousFloatingLookbackOption</code>, <code>ContinuousFixedLookbackOption</code>, <code>MultiAssetOption</code>, <code>PagodaOption</code>, and <code>Swaption</code>.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, Option::Type) [related]</h3>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
