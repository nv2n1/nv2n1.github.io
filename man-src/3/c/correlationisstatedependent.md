---
title: "correlationisstatedependent(3)"
name: "correlationisstatedependent"
section: "3"
letter: "c"
url: "/docs/linux/man/3-correlationisstatedependent/"
description: "QuantLib::HybridHestonHullWhiteProcess – Hybrid Heston Hull-White stochastic process."
---

<p>QuantLib::HybridHestonHullWhiteProcess &#8211; Hybrid Heston Hull-White stochastic process. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/hybridhestonhullwhiteprocess.hpp&gt; </p>
<p> Inherits QuantLib::JointStochasticProcess. </p>
<h3>Public Member Functions</h3>
<p><code>HybridHestonHullWhiteProcess</code> (const boost::shared_ptr&lt; <code>HestonProcess</code> &gt; &amp;hestonProcess, const boost::shared_ptr&lt; <code>HullWhiteForwardProcess</code> &gt; &amp;hullWhiteProcess, Real corrEquityShortRate, Size factors) </p>
<p> void <code>preEvolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>postEvolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw, const <code>Array</code> &amp;y0) const </p>
<p> <code>DiscountFactor</code> <code>numeraire</code> (Time t, const <code>Array</code> &amp;x) const </p>
<p> bool <code>correlationIsStateDependent</code> () const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>crossModelCorrelation</code> (Time t0, const <code>Array</code> &amp;x0) const </p>
<p> boost::shared_ptr&lt; <code>HestonProcess</code> &gt; <code>hestonProcess</code> () const </p>
<p> boost::shared_ptr&lt; <code>HullWhiteForwardProcess</code> &gt; <code>hullWhiteProcess</code> () const </p>
<p> void <code>update</code> () </p>
<p> Real <code>correlation</code> () const </p>
<h3>Protected Attributes</h3>
<p>const boost::shared_ptr&lt; <code>HullWhite</code> &gt; <code>hullWhiteModel_</code> </p>
<p> const Real <code>corrEquityShortRate_</code> </p>
<p> const Time <code>T_</code> </p>
<p> <code>DiscountFactor</code> <code>endDiscount_</code> </p>
<h2>Detailed Description</h2>
<p>Hybrid Heston Hull-White stochastic process. </p>
<p> This class implements a three factor Heston Hull-White model </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>This class was not tested enough to guarantee its functionality&#8230; work in progress</dl>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
