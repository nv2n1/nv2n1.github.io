---
title: "fixingdates_(3)"
name: "fixingdates_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixingdates_/"
description: "QuantLib::DiscreteAveragingAsianOption – Discrete-averaging Asian option."
---

<p>QuantLib::DiscreteAveragingAsianOption &#8211; Discrete-averaging Asian option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/asianoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Extra arguments for single-asset discrete-average Asian option. </i><br />
 class <code>engine</code><br />
 <i>Discrete-averaging Asian engine base class. </i></p>
<h3>Public Member Functions</h3>
<p><code>DiscreteAveragingAsianOption</code> (Average::Type averageType, <code>Real</code> runningAccumulator, Size pastFixings, const std::vector&lt; <code>Date</code> &gt; &amp;fixingDates, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h3>Protected Attributes</h3>
<p>Average::Type <code>averageType_</code> </p>
<p> <code>Real</code> <code>runningAccumulator_</code> </p>
<p> Size <code>pastFixings_</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixingDates_</code> </p>
<h2>Detailed Description</h2>
<p>Discrete-averaging Asian option. </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
