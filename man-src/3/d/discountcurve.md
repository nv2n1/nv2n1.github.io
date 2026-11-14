---
title: "discountcurve(3)"
name: "discountcurve"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discountcurve/"
description: "ql/termstructures/yield/discountcurve.hpp – interpolated discount factor structure"
---

<h2 class="name">NAME</h2>
<p> ql/termstructures/yield/discountcurve.hpp &#8211; interpolated discount factor structure </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/termstructures/yieldtermstructure.hpp&gt;<br />
 #include &lt;ql/math/interpolations/loginterpolation.hpp&gt;<br />
 #include &lt;ql/math/comparison.hpp&gt;<br />
 #include &lt;boost/noncopyable.hpp&gt;<br />
 #include &lt;vector&gt;<br />
 #include &lt;utility&gt; </p>
<h3>Classes</h3>
<p> class <code>InterpolatedDiscountCurve&lt; Interpolator &gt;</code><br />
 <i>Term structure based on interpolation of discount factors. </i></p>
<h3>Typedefs</h3>
<p> typedef InterpolatedDiscountCurve&lt; LogLinear &gt; <code>DiscountCurve</code><br />
 <i>Term structure based on log-linear interpolation of discount factors. </i></p>
<h2>Detailed Description</h2>
<p> interpolated discount factor structure </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
