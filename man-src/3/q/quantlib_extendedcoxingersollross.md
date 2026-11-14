---
title: "quantlib_extendedcoxingersollross(3)"
name: "quantlib_extendedcoxingersollross"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedcoxingersollross/"
description: "QuantLib::ExtendedCoxIngersollRoss – Extended Cox-Ingersoll-Ross model class."
---

<p>QuantLib::ExtendedCoxIngersollRoss &#8211; Extended Cox-Ingersoll-Ross model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/extendedcoxingersollross.hpp&gt; </p>
<p> Inherits <code>QuantLib::CoxIngersollRoss</code>, and <code>QuantLib::TermStructureConsistentModel</code>. </p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Short-rate dynamics in the extended Cox-Ingersoll-Ross model. </i><br />
 class <code>FittingParameter</code><br />
 <i>Analytical term-structure fitting parameter $ ndle</i>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real theta=0.1, Real k=0.1, Real sigma=0.1, Real x0=0.05)&quot;</p>
<h3>Public Member Functions</h3>
<p><code>ExtendedCoxIngersollRoss</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, Real theta=0.1, Real k=0.1, Real sigma=0.1, Real x0=0.05) </p>
<p> boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Return by default a trinomial recombining tree. </i><br />
 boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>returns the short-rate dynamics </i><br />
 Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>generateArguments</code> () </p>
<p> Real <code>A</code> (Time t, Time T) const </p>
<h2>Detailed Description</h2>
<p>Extended Cox-Ingersoll-Ross model class. </p>
<p> This class implements the extended Cox-Ingersoll-Ross model defined by [ dr_t = ( heta(t) &#8211; lpha r_t)dt + qrt{r_t}igma dW_t . ] </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>this class was not tested enough to guarantee its functionality.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
