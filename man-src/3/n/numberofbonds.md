---
title: "numberofbonds(3)"
name: "numberofbonds"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numberofbonds/"
description: "QuantLib::FittedBondDiscountCurve – Discount curve fitted to a set of fixed-coupon bonds."
---

<p>QuantLib::FittedBondDiscountCurve &#8211; <code>Discount</code> curve fitted to a set of fixed-coupon bonds. </p>
<h2>Synopsis</h2>
<pre><code>void update ()



Friends</code></pre>
<p> Inherits <code>QuantLib::YieldTermStructure</code>, and <code>QuantLib::LazyObject</code>.</p>
<h3>Classes</h3>
<p>class <code>FittingMethod</code><br />
 <i>Base fitting method used to construct a fitted bond discount curve. </i></p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code><br />
 void update ()</p>
<p>Friends <code>Inspectors</code><br />
 void update ()</p>
<p>Friends <code>Observer interface</code> </p>
<pre><code>void update ()



Friends</code></pre>
<p> class <code>FittingMethod</code></p>
<h2>Detailed Description</h2>
<p><code>Discount</code> curve fitted to a set of fixed-coupon bonds. </p>
<p> This class fits a discount function $ d(t) $ over a set of bonds, using a user defined fitting method. The discount function is fit in such a way so that all cashflows of all input bonds, when discounted using $ d(t) $, will reproduce the set of input bond prices in an optimized sense. Minimized price errors are weighted by the inverse of their respective bond duration. </p>
<p> The <code>FittedBondDiscountCurve</code> class acts as a generic wrapper, while its inner class <code>FittingMethod</code> provides the implementation details. Developers thus need only derive new fitting methods from the latter. </p>
<p> <code> Example: </code> <code>compares various bond discount curve fitting methodologies </code> </p>
<p> <code>Warning</code></p>
<dl>
<dd>The method can be slow if there are many bonds to fit. Speed also depends on the particular choice of fitting method chosen and its convergence properties under optimization. See also todo list for BondDiscountCurveFittingMethod.</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>refactor the bond helper class so that it is pure virtual and returns a generic bond or its cash flows. Derived classes would include helpers for fixed-rate and zero-coupon bonds. In this way, both bonds and bills can be used to fit a discount curve using the exact same machinery. At present, only fixed-coupon bonds are supported. An even better way to move forward might be to get rate helpers to return cashflows, in which case this class could be used to fit any set of cash flows, not just bonds.</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add more fitting diagnostics: smoothness, standard deviation, student-t test, etc. Generic smoothness method may be useful for smoothing splines fitting. See Fisher, M., D. Nychka and D. Zervos: &#8216;Fitting the term structure of interest rates with smoothing splines.&#8217; Board of Governors of the Federal Reserve System, Federal Resere Board Working Paper, 95-1.</dl>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>add extrapolation routines</dl>
<p> <code>Examples: </code> </p>
<p> <code>FittedBondCurve.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
