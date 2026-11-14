---
title: "quantlib_cliquetoption(3)"
name: "quantlib_cliquetoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cliquetoption/"
description: "QuantLib::CliquetOption – cliquet (Ratchet) option"
---

<p>QuantLib::CliquetOption &#8211; cliquet (Ratchet) option </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/cliquetoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for cliquet option calculation </i><br />
 class <code>engine</code><br />
 <i>Cliquet engine base class. </i></p>
<h3>Public Member Functions</h3>
<p><code>CliquetOption</code> (const boost::shared_ptr&lt; <code>PercentageStrikePayoff</code> &gt; &amp;, const boost::shared_ptr&lt; <code>EuropeanExercise</code> &gt; &amp;maturity, const std::vector&lt; <code>Date</code> &gt; &amp;resetDates) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h2>Detailed Description</h2>
<p>cliquet (Ratchet) option </p>
<p> A cliquet option, also known as Ratchet option, is a series of forward-starting (a.k.a. deferred strike) options where the strike for each forward start option is set equal to a fixed percentage of the spot price at the beginning of each period. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>add local/global caps/floors</p>
<dt>*</p>
<dd>add accrued coupon and last fixing</dl>
</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
