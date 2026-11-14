---
title: "vpresample(3)"
name: "vpresample"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpresample/"
description: "vpResample, vpResample2D, vpResample3D – resample an array"
---

<p>vpResample, vpResample2D, vpResample3D &#8211; resample an array</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpResample(</code><i>vpc, num_dimens, src_dimens, dst_dimens, src_strides,</p>
<dd>dst_strides, element_type, src_array, dst_array</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>num_dimens;</i></p>
<dd>int <i>*src_dimens, *dst_dimens;</i></p>
<dd>int <i>*src_strides, *dst_strides;</i></p>
<dd>int <i>element_type;</i></p>
<dd>void <i>*src_array, *dst_array;</i>  vpResult</p>
<dl>
<dt> <code>vpResample2D(</code><i>src_array, src_x, src_y, dst_array,</p>
<dd>dst_x, dst_y, element_type, filter_type</i><code>)</code></p>
<dd>void *<i>src_array;</i></p>
<dd>int <i>src_x, src_y;</i></p>
<dd>void *<i>dst_array;</i></p>
<dd>int <i>dst_x, dst_y;</i></p>
<dd>int <i>element_type;</i></p>
<dd>int <i>filter_type;</i>  vpResult</p>
<dl>
<dt> <code>vpResample3D(</code><i>src_array, src_x, src_y, src_z, dst_array,</p>
<dd>dst_x, dst_y, dst_z, element_type, filter_type</i><code>)</code></p>
<dd>void *<i>src_array;</i></p>
<dd>int <i>src_x, src_y, src_z;</i></p>
<dd>void *<i>dst_array;</i></p>
<dd>int <i>dst_x, dst_y, dst_z;</i></p>
<dd>int <i>element_type;</i></p>
<dd>int <i>filter_type;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>num_dimens</i></p>
<dd>Number of dimensions in the input and output arrays.</p>
<dt><i>src_dimens</i></p>
<dd>Array containing the dimensions of the input array.</p>
<dt><i>dst_dimens</i></p>
<dd>Array containing the dimensions of the output array.</p>
<dt><i>src_strides</i></p>
<dd>Array containing the strides for each dimension of the input array.</p>
<dt><i>dst_strides</i></p>
<dd>Array containing the strides for each dimension of the output array.</p>
<dt><i>element_type</i></p>
<dd>Constant specifying the data type of the array elements (VP_UCHAR, VP_USHORT, VP_FLOAT).</p>
<dt><i>src_array</i></p>
<dd>Input array containing input data.</p>
<dt><i>dst_array</i></p>
<dd>Output array for result data.</p>
<dt><i>src_x, src_y, src_z</i></p>
<dd>Dimensions of the input array.</p>
<dt><i>dst_x, dst_y, dst_z</i></p>
<dd>Dimensions of the result array.</p>
<dt><i>filter_type</i></p>
<dd>Constant specifying one of the predefined filters (VP_BOX_FILTER, VP_LINEAR_FILTER, VP_GAUSSIAN_FILTER, VP_BSPLINE_FILTER, VP_MITCHELL_FILTER).</dl>
<h2>Description</h2>
<p><code>vpResample</code> is used to resample an array to a new grid with a different resolution. It can be used to scale up or decimate an array of volume data, for instance. An arbitrary separable space-invariant resampling filter can be specified via a lookup table containing filter weights. The input array may have an arbitrary number of dimensions, but on each call to <code>vpResample</code> only one dimension of the array is resampled. To scale all dimensions call the routine once for each dimension. Transformations other than scales (e.g. rotations and shears) are not supported by these routines. </p>
<p> The routines <code>vpResample2D</code> and <code>vpResample3D</code> provide a simpler (but less flexible) interface to <code>vpResample</code>. They take as arguments an input array with its dimensions, an output array with its dimensions, and a constant specifying a filter. The input array is resampled once for each dimension and then stored in the output array. These two routines automatically create a filter weight table and arrays for temporary results. </p>
<p> The remainder of this man page describe <code>vpResample</code>. The <i>vpc</i> argument is a VolPack context that contains a description of the resampling filter. Use <code>vpSetFilter</code> to define the filter. The volume data and rendering parameters currently stored in the context are not affected by calls to <code>vpResample</code>. </p>
<p> The remaining arguments to <code>vpResample</code> describe the size and layout of the input and output arrays. The two arrays must have the same number of dimensions, specified by <i>num_dimens.</i> The sizes of the dimensions are specified by <i>src_dimens</i> and <i>dst_dimens</i> which are 1D arrays with <i>num_dimens</i> elements in each array. <i>src_dimens[0]</i> is the size of the input dimension to be resampled. <i>dst_dimens[0]</i> is the size of the output dimension after resampling, so the scale factor is dst_dimens[0] / src_dimens[0]. The remaining elements of <i>src_dimens</i> give the sizes of the other input array dimensions in any order (although some orderings result in faster execution due to lower memory overhead). The other output array dimensions are ignored (although they should be the same as the corresponding input array dimensions since only one dimensions is resampled). </p>
<p> The <i>src_strides</i> and <i>dst_stride</i> arguments are 1D arrays that contain a stride in bytes for each dimension of the input and output arrays, stored in the same order as the dimensions sizes in <i>src_dimens</i>. </p>
<p> The <i>element_type</i> argument specifies the data type of each element of the input and output data arrays. The supported types are:</p>
<dl>
<dt>VP_UCHAR</p>
<dd>Unsigned character (1 byte per element).</p>
<dt>VP_USHORT</p>
<dd>Unsigned short (2 bytes per element).</p>
<dt>VP_FLOAT</p>
<dd>Single-precision floating point (4 bytes per element).</dl>
<p> Finally, the last two arguments to <code>vpResample</code> are pointers to the first elements of the input and output arrays.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SIZE</p>
<dd>No filter weight table has been specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpsetfilter/">vpSetFilter</a>(3) </p>
