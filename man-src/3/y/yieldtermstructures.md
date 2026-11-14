---
title: "yieldtermstructures(3)"
name: "yieldtermstructures"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yieldtermstructures/"
description: "Term structures –"
---

<p>Term structures &#8211;</p>
<h3>Classes</h3>
<p>class <code>InterpolatedDiscountCurve&lt; Interpolator &gt;</code><br />
 <i>Term structure based on interpolation of discount factors. </i><br />
 class <code>FittedBondDiscountCurve</code><br />
 <i></i><code>Discount</code> curve fitted to a set of fixed-coupon bonds.<br />
 class <code>FlatForward</code><br />
 <i>Flat interest-rate curve. </i><br />
 class <code>InterpolatedForwardCurve&lt; Interpolator &gt;</code><br />
 <i>Term structure based on interpolation of forward rates. </i><br />
 class <code>ForwardSpreadedTermStructure</code><br />
 <i>Term structure with added spread on the instantaneous forward rate. </i><br />
 class <code>ForwardRateStructure</code><br />
 <i>Forward-rate term structure </i><br />
 class <code>ImpliedTermStructure</code><br />
 <i>Implied term structure at a given date in the future. </i><br />
 class <code>PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</code><br />
 <i>Piecewise yield term structure. </i><br />
 class <code>PiecewiseZeroSpreadedTermStructure</code><br />
 <i>Term structure with an added vector of spreads on the zero-yield rate. </i><br />
 class <code>InterpolatedZeroCurve&lt; Interpolator &gt;</code><br />
 <i>Term structure based on interpolation of zero yields. </i><br />
 class <code>ZeroSpreadedTermStructure</code><br />
 <i>Term structure with an added spread on the zero yield rate. </i><br />
 class <code>ZeroYieldStructure</code><br />
 <i>Zero-yield term structure. </i><br />
 class <code>YieldTermStructure</code><br />
 <i>Interest-rate term structure. </i></p>
<h3>Typedefs</h3>
<p>typedef InterpolatedDiscountCurve&lt; LogLinear &gt; <code>DiscountCurve</code><br />
 <i>Term structure based on log-linear interpolation of discount factors. </i><br />
 typedef InterpolatedForwardCurve&lt; BackwardFlat &gt; <code>ForwardCurve</code><br />
 <i>Term structure based on flat interpolation of forward rates. </i><br />
 typedef InterpolatedZeroCurve&lt; Linear &gt; <code>ZeroCurve</code><br />
 <i>Term structure based on linear interpolation of zero yields. </i></p>
<h2>Detailed Description</h2>
<p>The abstract class <code>QuantLib::YieldTermStructure</code> provides the common interface to concrete yield-rate term structure models. Among others, methods are declared which return instantaneous forward rate, discount factor, and zero rate at a given date. Adapter classes are provided which already implement part of the required methods, thus allowing the programmer to define only the non-redundant part.</p>
<h2>Typedef Documentation</h2>
<h3>typedef InterpolatedDiscountCurve&lt;LogLinear&gt; DiscountCurve</h3>
<p>Term structure based on log-linear interpolation of discount factors. </p>
<p> Log-linear interpolation guarantees piecewise-constant forward rates.</p>
<h3>typedef InterpolatedForwardCurve&lt;BackwardFlat&gt; ForwardCurve</h3>
<p>Term structure based on flat interpolation of forward rates.</p>
<h3>typedef InterpolatedZeroCurve&lt;Linear&gt; ZeroCurve</h3>
<p>Term structure based on linear interpolation of zero yields.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
