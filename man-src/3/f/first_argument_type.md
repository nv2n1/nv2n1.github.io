---
title: "first_argument_type(3)"
name: "first_argument_type"
section: "3"
letter: "f"
url: "/docs/linux/man/3-first_argument_type/"
description: "QuantLib::Interpolation2D – base class for 2-D interpolations."
---

<h2 class="name">NAME</h2>
<p> QuantLib::Interpolation2D &#8211; base class for 2-D interpolations. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/interpolations/interpolation2d.hpp&gt; </p>
<p> Inherits <code>QuantLib::Extrapolator</code>. </p>
<p> Inherited by <code>BicubicSpline</code>, <code>BilinearInterpolation</code>, and FlatExtrapolator2D. </p>
<h3>Classes</h3>
<p> class <code>Impl</code><br />
 <i>abstract base class for 2-D interpolation implementations </i><br />
 class <code>templateImpl</code><br />
 <i>basic template implementation </i></p>
<h3>Public Types</h3>
<p> typedef <code>Real</code> <code>first_argument_type</code> </p>
<p> typedef <code>Real</code> <code>second_argument_type</code> </p>
<p> typedef <code>Real</code> <code>result_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>Real</code> <code>operator()</code> (<code>Real</code> x, <code>Real</code> y, bool allowExtrapolation=false) const </p>
<p> <code>Real</code> <code>xMin</code> () const </p>
<p> <code>Real</code> <code>xMax</code> () const </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>xValues</code> () const </p>
<p> Size <code>locateX</code> (<code>Real</code> x) const </p>
<p> <code>Real</code> <code>yMin</code> () const </p>
<p> <code>Real</code> <code>yMax</code> () const </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>yValues</code> () const </p>
<p> Size <code>locateY</code> (<code>Real</code> y) const </p>
<p> const <code>Matrix</code> &amp; <code>zData</code> () const </p>
<p> bool <code>isInRange</code> (<code>Real</code> x, <code>Real</code> y) const </p>
<p> void <code>update</code> () </p>
<h3>Protected Member Functions</h3>
<p> void <code>checkRange</code> (<code>Real</code> x, <code>Real</code> y, bool extrapolate) const </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>Impl</code> &gt; <code>impl_</code> </p>
<h2>Detailed Description</h2>
<p> base class for 2-D interpolations. </p>
<p> Classes derived from this class will provide interpolated values from two sequences of length $ N $ and $ M $, representing the discretized values of the $ x $ and $ y $ variables, and a $ N imes M $ matrix representing the tabulated function values. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
