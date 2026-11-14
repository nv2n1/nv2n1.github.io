---
title: "discountfunction(3)"
name: "discountfunction"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discountfunction/"
description: "QuantLib::FittedBondDiscountCurve::FittingMethod – Base fitting method used to construct a fitted bond discount curve."
---

<p>QuantLib::FittedBondDiscountCurve::FittingMethod &#8211; Base fitting method used to construct a fitted bond discount curve. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/fittedbonddiscountcurve.hpp&gt; </p>
<p> Inherited by <code>CubicBSplinesFitting</code>, <code>ExponentialSplinesFitting</code>, <code>NelsonSiegelFitting</code>, and <code>SimplePolynomialFitting</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual Size <code>size</code> () const =0<br />
 <i>total number of coefficients to fit/solve for </i><br />
 <code>Array</code> <code>solution</code> () const<br />
 <i>output array of results of optimization problem </i><br />
 <code>Integer</code> <code>numberOfIterations</code> () const<br />
 <i>final number of iterations used in the optimization problem </i><br />
 <code>Real</code> <code>minimumCostValue</code> () const<br />
 <i>final value of cost function after optimization </i><br />
 virtual std::auto_ptr&lt; <code>FittingMethod</code> &gt; <code>clone</code> () const =0<br />
 <i>clone of the current object </i></p>
<h3>Protected Member Functions</h3>
<p><code>FittingMethod</code> (bool constrainAtZero=true)<br />
 <i>constructor </i><br />
 void <code>init</code> ()<br />
 <i>rerun every time instruments/referenceDate changes </i><br />
 virtual <code>DiscountFactor</code> <code>discountFunction</code> (const <code>Array</code> &amp;x, Time t) const =0<br />
 <i>derived classes must set this </i></p>
<h3>Protected Attributes</h3>
<p>bool <code>constrainAtZero_</code><br />
 <i>constrains discount function to unity at $ T=0 $, if true </i><br />
 <code>FittedBondDiscountCurve</code> * <code>curve_</code><br />
 <i>internal reference to the </i><code>FittedBondDiscountCurve</code> instance<br />
 <code>Array</code> <code>solution_</code><br />
 <i>solution array found from optimization, set in calculate() </i><br />
 <code>Array</code> <code>guessSolution_</code><br />
 <i>optional guess solution to be passed into constructor. </i><br />
 boost::shared_ptr&lt; FittingCost &gt; <code>costFunction_</code><br />
 <i>base class sets this cost function used in the optimization routine </i></p>
<h3>Friends</h3>
<p>class <code>FittedBondDiscountCurve</code> </p>
<h2>Detailed Description</h2>
<p>Base fitting method used to construct a fitted bond discount curve. </p>
<p> This base class provides the specific methodology/strategy used to construct a <code>FittedBondDiscountCurve</code>. Derived classes need only define the virtual function <code>discountFunction()</code> based on the particular fitting method to be implemented, as well as <code>size()</code>, the number of variables to be solved for/optimized. The generic fitting methodology implemented here can be termed nonlinear, in contrast to (typically faster, computationally) linear fitting method. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>derive the special-case class LinearFittingMethods from <code>FittingMethod</code>. A linear fitting to a set of basis functions $ b_i(t) $ is any fitting of the form [ d(t) = um_{i=0} c_i b_i(t) ] i.e., linear in the unknown coefficients $ c_i $. Such a fitting can be reduced to a linear algebra problem $ Ax = b $, and for large numbers of bonds, would typically be much faster computationally than the generic non-linear fitting method.</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>some parameters to the <code>Simplex</code> optimization method may need to be tweaked internally to the class, depending on the fitting method used, in order to get proper/reasonable/faster convergence.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual <code>DiscountFactor</code> discountFunction (const <code>Array</code> &amp; x, Time t) const [protected, pure virtual]</h3>
<p>derived classes must set this </p>
<p> user-defined discount curve, as a function of time and an array of unknown fitting coefficients $ x_i $.</p>
<h2>Member Data Documentation</h2>
<h3><code>Array</code> <code>guessSolution_</code> [protected]</h3>
<p>optional guess solution to be passed into constructor. </p>
<p> The idea is to use a previous solution as a guess solution to the discount curve, in an attempt to speed up calculations. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
