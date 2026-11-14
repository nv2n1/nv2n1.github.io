---
title: "quantlib_multicubicspline(3)"
name: "quantlib_multicubicspline"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_multicubicspline/"
description: "QuantLib::MultiCubicSpline – N-dimensional cubic spline interpolation between discrete points."
---

<p>QuantLib::MultiCubicSpline &#8211; N-dimensional cubic spline interpolation between discrete points. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/multicubicspline.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef c_splint::argument_type <code>argument_type</code> </p>
<p> typedef c_splint::result_type <code>result_type</code> </p>
<p> typedef c_splint::data_table <code>data_table</code> </p>
<p> typedef c_splint::return_type <code>return_type</code> </p>
<p> typedef c_splint::output_data <code>output_data</code> </p>
<p> typedef c_splint::dimensions <code>dimensions</code> </p>
<p> typedef c_splint::data <code>data</code> </p>
<h3>Public Member Functions</h3>
<p><code>MultiCubicSpline</code> (const SplineGrid &amp;grid, const data_table &amp;y, const std::vector&lt; bool &gt; &amp;ae=std::vector&lt; bool &gt;(20, false)) </p>
<p> result_type <code>operator()</code> (const argument_type &amp;x) const </p>
<p> void <code>set_shared_increments</code> () const </p>
<p> void <code>set_shared_coefficients</code> (const argument_type &amp;x) const </p>
<h2>Detailed Description</h2>
<h3>template&lt;Size i&gt; class QuantLib::MultiCubicSpline&lt; i &gt;</h3>
<p>N-dimensional cubic spline interpolation between discrete points. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>interpolated values are checked against the original function.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>allow extrapolation as for the other interpolations</p>
<dt>*</p>
<dd>investigate if and how to implement Hyman filters and different boundary conditions</dl>
</dl>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>cannot interpolate at the grid points on the boundary surface of the N-dimensional region</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
