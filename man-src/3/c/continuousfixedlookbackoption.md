---
title: "continuousfixedlookbackoption(3)"
name: "continuousfixedlookbackoption"
section: "3"
letter: "c"
url: "/docs/linux/man/3-continuousfixedlookbackoption/"
description: "QuantLib::ContinuousFixedLookbackOption – Continuous-fixed lookback option."
---

<p>QuantLib::ContinuousFixedLookbackOption &#8211; Continuous-fixed lookback option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/lookbackoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for continuous fixed lookback option calculation </i><br />
 class <code>engine</code><br />
 <i>Continuous fixed lookback engine base class </i></p>
<h3>Public Member Functions</h3>
<p><code>ContinuousFixedLookbackOption</code> (<code>Real</code> currentMinmax, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>minmax_</code> </p>
<h2>Detailed Description</h2>
<p>Continuous-fixed lookback option. </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
