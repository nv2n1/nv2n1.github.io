---
title: "quantlib_interpolation_impl(3)"
name: "quantlib_interpolation_impl"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolation_impl/"
description: "QuantLib::Interpolation::Impl – abstract base class for interpolation implementations"
---

<p>QuantLib::Interpolation::Impl &#8211; abstract base class for interpolation implementations </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolation.hpp&gt; </p>
<p> Inherited by <code>templateImpl&lt; I1, I2 &gt;</code>, and <code>templateImpl&lt; I1, I2 &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>update</code> ()=0 </p>
<p> virtual Real <code>xMin</code> () const =0 </p>
<p> virtual Real <code>xMax</code> () const =0 </p>
<p> virtual std::vector&lt; Real &gt; <code>xValues</code> () const =0 </p>
<p> virtual std::vector&lt; Real &gt; <code>yValues</code> () const =0 </p>
<p> virtual bool <code>isInRange</code> (Real) const =0 </p>
<p> virtual Real <code>value</code> (Real) const =0 </p>
<p> virtual Real <code>primitive</code> (Real) const =0 </p>
<p> virtual Real <code>derivative</code> (Real) const =0 </p>
<p> virtual Real <code>secondDerivative</code> (Real) const =0 </p>
<h2>Detailed Description</h2>
<p>abstract base class for interpolation implementations </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
