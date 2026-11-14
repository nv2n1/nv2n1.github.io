---
title: "sabrinterpolation(3)"
name: "sabrinterpolation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sabrinterpolation/"
description: "ql/math/interpolations/sabrinterpolation.hpp – SABR interpolation interpolation between discrete points."
---

<p>ql/math/interpolations/sabrinterpolation.hpp &#8211; SABR interpolation interpolation between discrete points. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/interpolation.hpp&gt;

#include &lt;ql/math/optimization/method.hpp&gt;

#include &lt;ql/math/optimization/simplex.hpp&gt;

#include &lt;ql/math/optimization/levenbergmarquardt.hpp&gt;

#include &lt;ql/pricingengines/blackformula.hpp&gt;

#include &lt;ql/utilities/null.hpp&gt;

#include &lt;ql/utilities/dataformatters.hpp&gt;

#include &lt;ql/termstructures/volatility/sabr.hpp&gt;

#include &lt;ql/math/optimization/projectedcostfunction.hpp&gt;

#include &lt;ql/math/optimization/constraint.hpp&gt;</code></pre>
<h3>Classes</h3>
<p>class <code>SABRInterpolation</code><br />
 <i>SABR smile interpolation between discrete volatility points. </i><br />
 class <code>SABR</code><br />
 <i>SABR interpolation factory and traits </i></p>
<h2>Detailed Description</h2>
<p>SABR interpolation interpolation between discrete points.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
