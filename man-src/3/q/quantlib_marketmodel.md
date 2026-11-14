---
title: "quantlib_marketmodel(3)"
name: "quantlib_marketmodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_marketmodel/"
description: "QuantLib::MarketModel – base class for market models"
---

<p>QuantLib::MarketModel &#8211; base class for market models </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/marketmodel.hpp&gt; </p>
<p> Inherited by <code>AbcdVol</code>, CotSwapToFwdAdapter, FlatVol, FwdPeriodAdapter, FwdToCotSwapAdapter, and PseudoRootFacade. </p>
<h3>Public Member Functions</h3>
<p>virtual const std::vector&lt; <code>Rate</code> &gt; &amp; <code>initialRates</code> () const =0 </p>
<p> virtual const std::vector&lt; <code>Spread</code> &gt; &amp; <code>displacements</code> () const =0 </p>
<p> virtual const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const =0 </p>
<p> virtual Size <code>numberOfRates</code> () const =0 </p>
<p> virtual Size <code>numberOfFactors</code> () const =0 </p>
<p> virtual Size <code>numberOfSteps</code> () const =0 </p>
<p> virtual const <code>Matrix</code> &amp; <code>pseudoRoot</code> (Size i) const =0 </p>
<p> virtual const <code>Matrix</code> &amp; <code>covariance</code> (Size i) const </p>
<p> virtual const <code>Matrix</code> &amp; <code>totalCovariance</code> (Size endIndex) const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>timeDependentVolatility</code> (Size i) const </p>
<h2>Detailed Description</h2>
<p>base class for market models </p>
<p> For each time step, generates the pseudo-square root of the covariance matrix for that time step. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
