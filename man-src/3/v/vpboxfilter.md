---
title: "vpboxfilter(3)"
name: "vpboxfilter"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpboxfilter/"
description: "vpBoxFilter, vpLinearFilter, vpBicubicFilter, vpGaussianFilter – initialize a filter weight table"
---

<p>vpBoxFilter, vpLinearFilter, vpBicubicFilter, vpGaussianFilter &#8211; initialize a filter weight table</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpBoxFilter(</code><i>num_taps, num_phases, weights, weights_bytes</i><code>)</code></p>
<dd>
<dd>int <i>num_taps, num_phases</i>;</p>
<dd>float *<i>weights</i>;</p>
<dd>int <i>weights_bytes</i>;  vpResult</p>
<dl>
<dt> <code>vpLinearFilter(</code><i>num_taps, num_phases, weights, weights_bytes</i><code>)</code></p>
<dd>
<dd>int <i>num_taps, num_phases</i>;</p>
<dd>float *<i>weights</i>;</p>
<dd>int <i>weights_bytes</i>;  vpResult</p>
<dl>
<dt> <code>vpBicubicFilter(</code><i>b_value, c_value, num_taps, num_phases, weights,</p>
<dd>weights_bytes</i><code>)</code></p>
<dd>double <i>b_value, c_value</i>;</p>
<dd>int <i>num_taps, num_phases</i>;</p>
<dd>float *<i>weights</i>;</p>
<dd>int <i>weights_bytes</i>;  vpResult</p>
<dl>
<dt> <code>vpGaussianFilter(</code><i>sigma, num_taps, num_phases, weights,</p>
<dd>weights_bytes</i><code>)</code></p>
<dd>double <i>sigma</i>;</p>
<dd>int <i>num_taps, num_phases</i>;</p>
<dd>float *<i>weights</i>;</p>
<dd>int <i>weights_bytes</i>;</dl>
<h2>Arguments</h2>
<dl>
<dt><i>num_taps</i></p>
<dd>Number of filter taps.</p>
<dt><i>num_phases</i></p>
<dd>Number of filter phases.</p>
<dt><i>weights</i></p>
<dd>Array containing filter weights.</p>
<dt><i>weights_bytes</i></p>
<dd>Size (in bytes) of array containing filter weights.</p>
<dt><i>b_value</i></p>
<dd>&quot;B&quot; parameter in the formula for a Mitchell bicubic.</p>
<dt><i>c_value</i></p>
<dd>&quot;C&quot; parameter in the formula for a Mitchell bicubic.</p>
<dt><i>sigma</i></p>
<dd>Standard deviation for a Gaussian.</dl>
<h2>Description</h2>
<p>These routines can be used to initialize filter weight tables for use with <code>vpSetFilter</code> and <code>vpResample</code>. See the <code>vpSetFilter</code> man page for information on the <i>num_taps</i> and <i>num_phases</i> arguments. </p>
<p> <code>vpBoxFilter</code> creates a filter table for a box filter (a zero-order filter). With <i>num_taps</i> equal to 1 the filter is a nearest-neighbor filter, suitable for low-quality upsampling. To create a decimation filter that averages down, the number of taps should equal the decimation factor (as nearly as possible). </p>
<p> <code>vpLinearFilter</code> creates a filter table for a linear filter (a first-order or tent filter). With <i>num_taps</i> equal to 2 the filter performs linear interpolation. </p>
<p> <code>vpBicubicFilter</code> creates a filter table for a Mitchell bicubic filter. The first two arguments can be used to modify the shape of the filter kernel. Some standard parameter values are:</p>
<dl>
<dt><i>b_value</i> = 1, <i>c_value = 0</i></p>
<dd>Cubic B-spline.</p>
<dt><i>b_value</i> = 0, <i>c_value = 0.5</i></p>
<dd>Catmull-Rom spline.</dl>
<p> With four filter taps the cubic B-spline filter is suitable for upsampling. For more details, see the following paper: Mitchell, D.P. and Netravali, A.N., &quot;Reconstruction filters in computer graphics,&quot; Proc. SIGGRAPH &#8217;88 (Computer Graphics V22 N4), p. 221-8. </p>
<p> <code>vpGaussianFilter</code> creates a filter table for a gaussian filter. The first argument is the standard deviation of the gaussian.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SIZE</p>
<dd>The filter weight table size is invalid.</p>
<dt>VPERROR_BAD_VALUE</p>
<dd>The number of phases is not a positive power of two.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpresample/">vpResample</a>(3), <a href="/docs/linux/man/3-vpsetfilter/">vpSetFilter</a>(3) </p>
