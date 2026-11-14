---
title: "notifyobservers(3)"
name: "notifyobservers"
section: "3"
letter: "n"
url: "/docs/linux/man/3-notifyobservers/"
description: "QuantLib::Observable – Object that notifies its changes to a set of observables."
---

<p>QuantLib::Observable &#8211; Object that notifies its changes to a set of observables. </p>
<h2>Synopsis</h2>
<pre><code>Observable (const Observable &amp;)



Observable &amp; operator= (const Observable &amp;)



void notifyObservers ()



Friends</code></pre>
<p> Inherited by <code>BootstrapHelper&lt; DefaultProbabilityTermStructure &gt;</code>, <code>BootstrapHelper&lt; YieldTermStructure &gt;</code>, <code>BootstrapHelper&lt; YoYInflationTermStructure &gt;</code>, <code>BootstrapHelper&lt; ZeroInflationTermStructure &gt;</code>, <code>AffineModel</code> [virtual], <code>BootstrapHelper&lt; TS &gt;</code>, <code>CalibratedModel</code> [virtual], <code>CalibrationHelper</code>, <code>Claim</code>, <code>CommodityIndex</code>, <code>Event</code>, <code>FloatingRateCouponPricer</code> [virtual], Link, <code>Index</code>, <code>LazyObject</code> [virtual], <code>MarketModelFactory</code>, <code>PricingEngine</code>, <code>Quote</code> [virtual], <code>SmileSection</code> [virtual], <code>StochasticProcess</code>, <code>TermStructure</code> [virtual], and <code>TermStructureConsistentModel</code> [virtual].</p>
<h3>Public Member Functions</h3>
<pre><code>Observable (const Observable &amp;)



Observable &amp; operator= (const Observable &amp;)



void notifyObservers ()



Friends</code></pre>
<p> class <code>Observer</code></p>
<h2>Detailed Description</h2>
<p>Object that notifies its changes to a set of observables.</p>
<h2>Member Function Documentation</h2>
<h3><code>Observable</code> &amp; operator= (const <code>Observable</code> &amp; o)</h3>
<p><code>Warning</code></p>
<dl>
<dd>notification is sent before the copy constructor has a chance of actually change the data members. Therefore, observers whose update() method tries to use their observables will not see the updated values. It is suggested that the update() method just raise a flag in order to trigger a later recalculation.</dl>
<h3>void notifyObservers ()</h3>
<p>This method should be called at the end of non-const methods or when the programmer desires to notify any changes.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
