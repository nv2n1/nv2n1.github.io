---
title: "swap_(3)"
name: "swap_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swap_/"
description: "QuantLib::ForwardSwapQuote – Quote for a forward starting swap."
---

<p>QuantLib::ForwardSwapQuote &#8211; <code>Quote</code> for a forward starting swap. </p>
<h2>Synopsis</h2>
<pre><code>void update ()



Protected Member Functions
void initializeDates ()



void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::LazyObject</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ForwardSwapQuote</code> (const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;spread, const <code>Period</code> &amp;fwdStart) </p>
<p> const <code>Date</code> &amp; <code>valueDate</code> () const </p>
<p> const <code>Date</code> &amp; <code>startDate</code> () const </p>
<p> const <code>Date</code> &amp; <code>fixingDate</code> () const<br />
 <code>Quote interface</code> </p>
<p> Real <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value <code>Observer interface</code> </p>
<pre><code>void update ()



Protected Member Functions
void initializeDates ()



void performCalculations () const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>SwapIndex</code> &gt; <code>swapIndex_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>spread_</code> </p>
<p> <code>Period</code> <code>fwdStart_</code> </p>
<p> <code>Date</code> <code>evaluationDate_</code> </p>
<p> <code>Date</code> <code>valueDate_</code> </p>
<p> <code>Date</code> <code>startDate_</code> </p>
<p> <code>Date</code> <code>fixingDate_</code> </p>
<p> boost::shared_ptr&lt; <code>VanillaSwap</code> &gt; <code>swap_</code> </p>
<p> <code>Rate</code> <code>result_</code></p>
<h2>Detailed Description</h2>
<p><code>Quote</code> for a forward starting swap.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
