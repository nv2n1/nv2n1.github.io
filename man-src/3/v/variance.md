---
title: "variance(3)"
name: "variance"
section: "3"
letter: "v"
url: "/docs/linux/man/3-variance/"
description: "QuantLib::VarianceSwap – Variance swap."
---

<p>QuantLib::VarianceSwap &#8211; Variance swap. </p>
<h2>Synopsis</h2>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for forward fair-variance calculation </i><br />
 class <code>engine</code><br />
 <i>base class for variance-swap engines </i><br />
 class <code>results</code><br />
 <i>Results from variance-swap calculation </i></p>
<h3>Public Member Functions</h3>
<p><code>VarianceSwap</code> (Position::Type position, <code>Real</code> strike, <code>Real</code> notional, const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;maturityDate) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *args) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const<br />
 <code>Instrument interface</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i> <code>Additional interface</code> </p>
<p> <code>Real</code> <code>strike</code> () const </p>
<p> Position::Type <code>position</code> () const </p>
<p> <code>Date</code> <code>startDate</code> () const </p>
<p> <code>Date</code> <code>maturityDate</code> () const </p>
<p> <code>Real</code> <code>notional</code> () const </p>
<p> <code>Real</code> <code>variance</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>void setupExpired () const



Protected Attributes</code></pre>
<p> Position::Type <code>position_</code> </p>
<p> <code>Real</code> <code>strike_</code> </p>
<p> <code>Real</code> <code>notional_</code> </p>
<p> <code>Date</code> <code>startDate_</code> </p>
<p> <code>Date</code> <code>maturityDate_</code> </p>
<p> <code>Real</code> <code>variance_</code></p>
<h2>Detailed Description</h2>
<p>Variance swap. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This class does not manage seasoned variance swaps.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
