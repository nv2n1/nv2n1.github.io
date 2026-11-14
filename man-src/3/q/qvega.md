---
title: "qvega(3)"
name: "qvega"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qvega/"
description: "QuantLib::QuantoBarrierOption – Quanto version of a barrier option."
---

<p>QuantLib::QuantoBarrierOption &#8211; Quanto version of a barrier option. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/instruments/quantobarrieroption.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::BarrierOption</code>.</p>
<h3>Public Types</h3>
<p>typedef <code>BarrierOption::arguments</code> <code>arguments</code> </p>
<p> typedef <code>QuantoOptionResults</code>&lt; BarrierOption::results &gt; <code>results</code></p>
<h3>Public Member Functions</h3>
<p><code>QuantoBarrierOption</code> (Barrier::Type barrierType, <code>Real</code> barrier, <code>Real</code> rebate, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise) </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const<br />
 <code>greeks</code> </p>
<p> <code>Real</code> <code>qvega</code> () const </p>
<p> <code>Real</code> <code>qrho</code> () const </p>
<p> <code>Real</code> <code>qlambda</code> () const</p>
<h2>Detailed Description</h2>
<p>Quanto version of a barrier option.</p>
<h2>Member Function Documentation</h2>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>OneAssetOption</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
