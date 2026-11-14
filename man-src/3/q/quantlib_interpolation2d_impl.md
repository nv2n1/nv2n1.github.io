---
title: "quantlib_interpolation2d_impl(3)"
name: "quantlib_interpolation2d_impl"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_interpolation2d_impl/"
description: "QuantLib::Interpolation2D::Impl – abstract base class for 2-D interpolation implementations"
---

<p>QuantLib::Interpolation2D::Impl &#8211; abstract base class for 2-D interpolation implementations </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/interpolations/interpolation2d.hpp&gt; </p>
<p> Inherited by FlatExtrapolator2DImpl, <code>templateImpl&lt; I1, I2, M &gt;</code>, and <code>templateImpl&lt; I1, I2, M &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>calculate</code> ()=0 </p>
<p> virtual Real <code>xMin</code> () const =0 </p>
<p> virtual Real <code>xMax</code> () const =0 </p>
<p> virtual std::vector&lt; Real &gt; <code>xValues</code> () const =0 </p>
<p> virtual Size <code>locateX</code> (Real x) const =0 </p>
<p> virtual Real <code>yMin</code> () const =0 </p>
<p> virtual Real <code>yMax</code> () const =0 </p>
<p> virtual std::vector&lt; Real &gt; <code>yValues</code> () const =0 </p>
<p> virtual Size <code>locateY</code> (Real y) const =0 </p>
<p> virtual const <code>Matrix</code> &amp; <code>zData</code> () const =0 </p>
<p> virtual bool <code>isInRange</code> (Real x, Real y) const =0 </p>
<p> virtual Real <code>value</code> (Real x, Real y) const =0 </p>
<h2>Detailed Description</h2>
<p>abstract base class for 2-D interpolation implementations </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
