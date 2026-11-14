---
title: "quantlib_coxingersollross(3)"
name: "quantlib_coxingersollross"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_coxingersollross/"
description: "QuantLib::CoxIngersollRoss – Cox-Ingersoll-Ross model class."
---

<p>QuantLib::CoxIngersollRoss &#8211; Cox-Ingersoll-Ross model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/coxingersollross.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorAffineModel</code>. </p>
<p> Inherited by <code>ExtendedCoxIngersollRoss</code>. </p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Dynamics of the short-rate under the Cox-Ingersoll-Ross model </i></p>
<h3>Public Member Functions</h3>
<p><code>CoxIngersollRoss</code> (<code>Rate</code> r0=0.05, Real theta=0.1, Real k=0.1, Real sigma=0.1) </p>
<p> virtual Real <code>discountBondOption</code> (Option::Type type, Real strike, Time maturity, Time bondMaturity) const </p>
<p> virtual boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>returns the short-rate dynamics </i><br />
 boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Return by default a trinomial recombining tree. </i></p>
<h3>Protected Member Functions</h3>
<p>Real <code>A</code> (Time t, Time T) const </p>
<p> Real <code>B</code> (Time t, Time T) const </p>
<p> Real <code>theta</code> () const </p>
<p> Real <code>k</code> () const </p>
<p> Real <code>sigma</code> () const </p>
<p> Real <code>x0</code> () const </p>
<h2>Detailed Description</h2>
<p>Cox-Ingersoll-Ross model class. </p>
<p> This class implements the Cox-Ingersoll-Ross model defined by [ dr_t = k( heta &#8211; r_t)dt + qrt{r_t}igma dW_t . ] </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>this class was not tested enough to guarantee its functionality.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
