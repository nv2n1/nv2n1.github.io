---
title: "quantlib_onefactoraffinemodel(3)"
name: "quantlib_onefactoraffinemodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_onefactoraffinemodel/"
description: "QuantLib::OneFactorAffineModel – Single-factor affine base class."
---

<p>QuantLib::OneFactorAffineModel &#8211; Single-factor affine base class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorModel</code>, and <code>QuantLib::AffineModel</code>. </p>
<p> Inherited by <code>CoxIngersollRoss</code>, and <code>Vasicek</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OneFactorAffineModel</code> (Size nArguments) </p>
<p> virtual <code>Real</code> <code>discountBond</code> (Time now, Time maturity, <code>Array</code> factors) const </p>
<p> <code>Real</code> <code>discountBond</code> (Time now, Time maturity, Rate rate) const </p>
<p> <code>DiscountFactor</code> <code>discount</code> (Time t) const<br />
 <i>Implied discount curve. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Real</code> <code>A</code> (Time t, Time T) const =0 </p>
<p> virtual <code>Real</code> <code>B</code> (Time t, Time T) const =0 </p>
<h2>Detailed Description</h2>
<p>Single-factor affine base class. </p>
<p> Single-factor models with an analytical formula for discount bonds should inherit from this class. They must then implement the functions $ A(t,T) $ and $ B(t,T) $ such that [ P(t, T, r_t) = A(t,T)e^{ -B(t,T) r_t}. ] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
