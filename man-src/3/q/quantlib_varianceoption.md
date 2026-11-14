---
title: "quantlib_varianceoption(3)"
name: "quantlib_varianceoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_varianceoption/"
description: "QuantLib::VarianceOption – Variance option."
---

<p>QuantLib::VarianceOption &#8211; Variance option. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/varianceoption/varianceoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for forward fair-variance calculation </i><br />
 class <code>engine</code><br />
 <i>base class for variance-option engines </i><br />
 class <code>results</code><br />
 <i>Results from variance-option calculation </i></p>
<h3>Public Member Functions</h3>
<p><code>VarianceOption</code> (const boost::shared_ptr&lt; <code>Payoff</code> &gt; &amp;payoff, <code>Real</code> notional, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;maturityDate) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<p> <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> </p>
<p> <code>Inspectors</code> </p>
<p> <code>Date</code> <code>startDate</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> () const </p>
<p> <code>Real</code> <code>notional</code> () const </p>
<p> boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Payoff</code> &gt; <code>payoff_</code> </p>
<p> <code>Real</code> <code>notional_</code> </p>
<p> <code>Date</code> <code>startDate_</code> </p>
<p> <code>Date</code> <code>maturityDate_</code> </p>
<h2>Detailed Description</h2>
<p>Variance option. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>This class does not manage seasoned variance options.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
