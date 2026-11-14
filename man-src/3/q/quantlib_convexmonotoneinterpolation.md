---
title: "quantlib_convexmonotoneinterpolation(3)"
name: "quantlib_convexmonotoneinterpolation"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_convexmonotoneinterpolation/"
description: "QuantLib::ConvexMonotoneInterpolation – Convex monotone yield-curve interpolation method."
---

<p>QuantLib::ConvexMonotoneInterpolation &#8211; Convex monotone yield-curve interpolation method. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/convexmonotoneinterpolation.hpp&gt; </p>
<p> Inherits <code>QuantLib::Interpolation</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ConvexMonotoneInterpolation</code> (const I1 &amp;xBegin, const I1 &amp;xEnd, const I2 &amp;yBegin, <code>Real</code> quadraticity, <code>Real</code> monotonicity, bool forcePositive, bool flatFinalPeriod=false, const helper_map &amp;preExistingHelpers=helper_map()) </p>
<p> <code>ConvexMonotoneInterpolation</code> (<code>Interpolation</code> &amp;interp) </p>
<p> std::map&lt; <code>Real</code>, boost::shared_ptr&lt; detail::SectionHelper &gt; &gt; <code>getExistingHelpers</code> () </p>
<h2>Detailed Description</h2>
<h3>template&lt;class I1, class I2&gt; class QuantLib::ConvexMonotoneInterpolation&lt; I1, I2 &gt;</h3>
<p>Convex monotone yield-curve interpolation method. </p>
<p> Enhances implementation of the convex monotone method described in &#8216;Interpolation Methods for Curve Construction&#8217; by Hagan &amp; West AMF Vol 13, No2 2006. </p>
<p> A setting of monotonicity = 1 and quadraticity = 0 will reproduce the basic Hagan/West method. However, this can produce excessive gradients which can mean P&amp;L swings for some curves. Setting monotonicity &lt; 1 and/or quadraticity &gt; 0 produces smoother curves. Extra enhancement to avoid negative values (if required) is in place. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
