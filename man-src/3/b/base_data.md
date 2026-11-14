---
title: "base_data(3)"
name: "base_data"
section: "3"
letter: "b"
url: "/docs/linux/man/3-base_data/"
description: "ql/math/interpolations/multicubicspline.hpp – N-dimensional cubic spline interpolation between discrete points."
---

<h2 class="name">NAME</h2>
<p> ql/math/interpolations/multicubicspline.hpp &#8211; N-dimensional cubic spline interpolation between discrete points. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/errors.hpp&gt;<br />
 #include &lt;ql/types.hpp&gt;<br />
 #include &lt;functional&gt;<br />
 #include &lt;vector&gt; </p>
<h3>Classes</h3>
<p> class <code>MultiCubicSpline&lt; i &gt;</code><br />
 <i>N-dimensional cubic spline interpolation between discrete points. </i></p>
<h3>Typedefs</h3>
<p> typedef std::vector&lt; std::vector&lt; Real &gt; &gt; <code>SplineGrid</code> </p>
<p> typedef DataTable&lt; Real &gt; <code>base_data_table</code> </p>
<p> typedef Data&lt; std::vector&lt; Real &gt;, EmptyArg &gt; <code>base_data</code> </p>
<p> typedef Point&lt; Real, EmptyArg &gt; <code>base_arg_type</code> </p>
<p> typedef Point&lt; Real, EmptyRes &gt; <code>base_return_type</code> </p>
<p> typedef Point&lt; Size, EmptyDim &gt; <code>base_dimensions</code> </p>
<p> typedef Point&lt; base_data_table, EmptyRes &gt; <code>base_output_data</code> </p>
<p> typedef base_cubic_spline <code>cubic_spline_01</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_01 &gt; <code>cubic_spline_02</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_02 &gt; <code>cubic_spline_03</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_03 &gt; <code>cubic_spline_04</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_04 &gt; <code>cubic_spline_05</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_05 &gt; <code>cubic_spline_06</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_06 &gt; <code>cubic_spline_07</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_07 &gt; <code>cubic_spline_08</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_08 &gt; <code>cubic_spline_09</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_09 &gt; <code>cubic_spline_10</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_10 &gt; <code>cubic_spline_11</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_11 &gt; <code>cubic_spline_12</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_12 &gt; <code>cubic_spline_13</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_13 &gt; <code>cubic_spline_14</code> </p>
<p> typedef n_cubic_spline&lt; cubic_spline_14 &gt; <code>cubic_spline_15</code> </p>
<p> typedef base_cubic_splint <code>cubic_splint_01</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_01 &gt; <code>cubic_splint_02</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_02 &gt; <code>cubic_splint_03</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_03 &gt; <code>cubic_splint_04</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_04 &gt; <code>cubic_splint_05</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_05 &gt; <code>cubic_splint_06</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_06 &gt; <code>cubic_splint_07</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_07 &gt; <code>cubic_splint_08</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_08 &gt; <code>cubic_splint_09</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_09 &gt; <code>cubic_splint_10</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_10 &gt; <code>cubic_splint_11</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_11 &gt; <code>cubic_splint_12</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_12 &gt; <code>cubic_splint_13</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_13 &gt; <code>cubic_splint_14</code> </p>
<p> typedef n_cubic_splint&lt; cubic_splint_14 &gt; <code>cubic_splint_15</code> </p>
<p> typedef detail::SplineGrid <code>SplineGrid</code> </p>
<h2>Detailed Description</h2>
<p> N-dimensional cubic spline interpolation between discrete points. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
