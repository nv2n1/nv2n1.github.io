---
title: "vpramp(3)"
name: "vpramp"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpramp/"
description: "vpRamp – initialize an array with a piecewise-linear ramp"
---

<p>vpRamp &#8211; initialize an array with a piecewise-linear ramp</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpRamp(</code><i>array, stride, num_points, ramp_x, ramp_y</i><code>)</code></p>
<dd>
<dd>float *<i>array;</i></p>
<dd>int <i>stride;</i></p>
<dd>int <i>num_points;</i></p>
<dd>int *<i>ramp_x;</i></p>
<dd>float *<i>ramp_y;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>array</i></p>
<dd>Output array.</p>
<dt><i>stride</i></p>
<dd>Stride from one array element to the next, in bytes.</p>
<dt><i>num_points</i></p>
<dd>Number of entries in the input arrays (<i>ramp_x</i> and <i>ramp_y</i>).</p>
<dt><i>ramp_x</i></p>
<dd>Input array containing indices into <i>array</i>.</p>
<dt><i>ramp_y</i></p>
<dd>Input array containing values to store into <i>array</i>.</dl>
<h2>Description</h2>
<p><code>vpRamp</code> is a utility routine for initializing linear arrays of floating-point numbers with piecewise-linear ramps. A ramp is defined by a set of (x, y) pairs. The X coordinates are integers that index entries in the <i>array</i> argument, and the Y coordinates are floating-point values to store into the array. Linearly-interpolated Y values are stored in array elements with indexes in between two of the X values. </p>
<p> The values in <i>ramp_x</i> most be strictly increasing. The <i>stride</i> argument may be used to skip array elements or to initialize arrays with a non-standard stride. If the output array is a simple linear array of type float then the stride should be sizeof(float). </p>
<p> This function is useful for creating lookup tables used for opacity transfer functions (see <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3)) and shading functions (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The number of points is less than one or the X values are not strictly increasing.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3) </p>
