---
title: "convexitybias(3)"
name: "convexitybias"
section: "3"
letter: "c"
url: "/docs/linux/man/3-convexitybias/"
description: "QuantLib::HullWhite – Single-factor Hull-White (extended Vasicek) model class."
---

<p>QuantLib::HullWhite &#8211; Single-factor Hull-White (extended Vasicek) model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/hullwhite.hpp&gt; </p>
<p> Inherits <code>QuantLib::Vasicek</code>, and <code>QuantLib::TermStructureConsistentModel</code>. </p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Short-rate dynamics in the Hull-White model. </i><br />
 class <code>FittingParameter</code><br />
 <i>Analytical term-structure fitting parameter $ ndle</i>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01)&quot;</p>
<h3>Public Member Functions</h3>
<p><code>HullWhite</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real a=0.1, Real sigma=0.01) </p>
<p> boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Return by default a trinomial recombining tree. </i><br />
 boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>returns the short-rate dynamics </i><br />
 Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Rate</code> <code>convexityBias</code> (Real futurePrice, Time t, Time T, Real sigma, Real a) </p>
<h3>Protected Member Functions</h3>
<p>void <code>generateArguments</code> () </p>
<p> Real <code>A</code> (Time t, Time T) const </p>
<h2>Detailed Description</h2>
<p>Single-factor Hull-White (extended Vasicek) model class. </p>
<p> This class implements the standard single-factor Hull-White model defined by [ dr_t = ( heta(t) &#8211; lpha r_t)dt + igma dW_t ] where $ lpha $ and $ igma $ are constants. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calibration results are tested against cached values</dl>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>When the term structure is relinked, the r0 parameter of the underlying <code>Vasicek</code> model is not updated.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, and <code>CallableBonds.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>Rate</code> convexityBias (Real futurePrice, Time t, Time T, Real sigma, Real a) [static]</h3>
<p>Futures convexity bias (i.e., the difference between futures implied rate and forward rate) calculated as in G. Kirikos, D. Novak, &#8216;Convexity Conundrums&#8217;, Risk Magazine, March 1997. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>t and T should be expressed in yearfraction using deposit day counter, F_quoted is futures&#8217; market price.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
