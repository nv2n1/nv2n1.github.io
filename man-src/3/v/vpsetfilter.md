---
title: "vpsetfilter(3)"
name: "vpsetfilter"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetfilter/"
description: "vpSetFilter – define a resampling filter"
---

<p>vpSetFilter &#8211; define a resampling filter</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetFilter(</code><i>vpc, num_taps, num_phases, weights</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>num_taps, num_phases;</i></p>
<dd>float *<i>weights;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>num_taps</i></p>
<dd>Number of filter taps.</p>
<dt><i>num_phases</i></p>
<dd>Number of filter phases.</p>
<dt><i>weights</i></p>
<dd>Array containing filter weights.</dl>
<h2>Description</h2>
<p><code>vpSetFilter</code> is used to specify a table of filter weights before resampling an array with <code>vpResample</code>. The table can be used to specify an arbitrary separable space-invariant filter. </p>
<p> The <i>vpc</i> argument is a VolPack context for storing a description of the resampling filter. The volume data and rendering parameters currently stored in the context are not affected by calls to <code>vpSetFilter</code> or <code>vpResample</code>. </p>
<p> The <i>num_taps</i> argument specifies the number of filter taps. When an array is resampled, the number of filter taps is equal to the number of input array elements that contribute to one element of the output array. A filter weight is associated with each tap and determines the contribution of the corresponding input array element to the output array element. Note that when upsampling the number of taps depends only on the support of the filter kernel. When downsampling, the number of taps should also depend on the scale factor (since the filter kernel must also be scaled). </p>
<p> The <i>num_phases</i> argument specifies the number of filter phases, which is equal to the number of times the filter kernel is sampled. The more filter phases, the more accurate the filtering operation. However, there is a point of diminishing returns where increasing the number of phases results in very little increase in accuracy, and has the disadvantages of increased storage requirements and potentially poor cache performance. To allow for an efficient implementation, <i>num_phases</i> must be a power of two. </p>
<p> The <i>weights</i> array contains the filter weights themselves. The array should have dimensions:</p>
<dl>
<dd>float weights[num_phases][num_taps];</dl>
<p> Each element should normally be a number between 0.0 and 1.0 (negative values are also possible but can lead to ringing), and for any particular phase the entries for all of the taps should sum to 1.0 (or else ripple is introduced into constant regions of the filtered array). </p>
<p> The easiest way to initialize the weight table is to call one of the predefined routines described in the <a href="/docs/linux/man/3-vpboxfilter/">vpBoxFilter</a>(3) man page.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>Either <i>num_taps</i> is non-positive or <i>num_phases</i> is not a positive power of two.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpboxfilter/">vpBoxFilter</a>(3), <a href="/docs/linux/man/3-vpresample/">vpResample</a>(3) </p>
