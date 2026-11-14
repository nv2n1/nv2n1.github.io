---
title: "quantlib_localbootstrap(3)"
name: "quantlib_localbootstrap"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_localbootstrap/"
description: "QuantLib::LocalBootstrap – Localised-term-structure bootstrapper for most curve types."
---

<p>QuantLib::LocalBootstrap &#8211; Localised-term-structure bootstrapper for most curve types. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/localbootstrap.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>LocalBootstrap</code> (Size localisation=2, bool forcePositive=true) </p>
<p> void <code>setup</code> (<code>Curve</code> *ts) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Curve&gt; class QuantLib::LocalBootstrap&lt; Curve &gt;</h3>
<p>Localised-term-structure bootstrapper for most curve types. </p>
<p> This algorithm enables a localised fitting for non-local interpolation methods. </p>
<p> As in the similar class (<code>IterativeBootstrap</code>) the input term structure is solved on a number of market instruments which are passed as a vector of handles to <code>BootstrapHelper</code> instances. Their maturities mark the boundaries of the interpolated segments. </p>
<p> Unlike the <code>IterativeBootstrap</code> class, the solution for each interpolated segment is derived using a local approximation. This restricts the risk profile s.t. the risk is localised. Therefore, we obtain a local IR risk profile whilst using a smoother interpolation method. Particularly good for the convex-monotone spline method. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
