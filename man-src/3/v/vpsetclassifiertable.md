---
title: "vpsetclassifiertable(3)"
name: "vpsetclassifiertable"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetclassifiertable/"
description: "vpSetClassifierTable – specify an opacity transfer function"
---

<p>vpSetClassifierTable &#8211; specify an opacity transfer function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetClassifierTable(</code><i>vpc, param_num, param_field, table,</p>
<dd>table_size</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>param_num, param_field;</i></p>
<dd>float *<i>table;</i></p>
<dd>int <i>table_size;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>param_num</i></p>
<dd>Parameter number identifying one parameter of the opacity transfer function.</p>
<dt><i>param_field</i></p>
<dd>Field number identifying a voxel field that contains the parameter.</p>
<dt><i>table</i></p>
<dd>Lookup table that defines the mapping from the voxel field value to the opacity.</p>
<dt><i>table_size</i></p>
<dd>Size of <i>table</i> in bytes.</dl>
<h2>Description</h2>
<p><code>vpSetClassifierTable</code> is used to specify lookup tables that define an opacity transfer function. The opacity transfer function must be of the form:</p>
<dl>
<dd>opacity = f0(param0) * f1(param1) * &#8230; * fN(paramN)</dl>
<p> where each of the factors is a function of one voxel field (see below for implementing more general classification models). <code>vpSetClassifierTable</code> must be called once for each factor to specify a lookup table that defines the factor. After the function has been specified, opacities are computed by calling one of the classification functions: <code>vpClassifyScalars, vpClassifyVolume,</code> or <code>vpClassifyScanline.</code> To classify a voxel, these functions use the values in the fields of the voxel as indexes into the opacity transfer function tables, retrieve one value from each table, and multiply the values together to compute the opacity for the voxel. The opacity should be a number in the range 0.0-1.0, so normally each table contains numbers that are also in this range. </p>
<p> The parameters of the opacity transfer function are numbered from zero, and the total number of parameters must be specified using <code>vpSetVoxelSize</code> before calling <code>vpSetClassifierTable</code>. The number of parameters is independent of the number of voxel fields: some fields may not be used as parameters, and one field could be used multiple times (although this is inefficient since all of the tables indexed by the same parameter could be merged into one table). </p>
<p> Each table should be a 1D array of numbers with one entry for each possible value of the corresponding voxel field. The voxel field must contain an unsigned integer quantity. Normally each table would be declared:</p>
<dl>
<dd>float table[MAX_FIELD_VALUE + 1];</dl>
<p> where MAX_FIELD_VALUE is the maximum possible value in the voxel field as specified with <code>vpSetVoxelField.</code> The table may also be dynamically allocated. Note that VolPack will never free the table, even if the VolPack context is destroyed with <code>vpDestroyContext,</code> so the application is responsible for freeing the memory when appropriate. The values in the table may be initialized or modified at any time before or after calling <code>vpSetClassifierTable,</code> but before calling one of the classification routines. See the function <code>vpRamp</code> for a convenient way to initialize tables with piece-wise linear ramps. </p>
<p> Classification functions that are not expressible in the form above can be handled as follows. First, write your own routine that computes the opacity for each voxel. Next, quantize the opacities using somewhere between 8 and 16 bits per voxel, and store the quantized values in one field of each voxel. Finally, define an opacity transfer function table that maps the quantized opacities into a floating point number in the range 0.0-1.0 and use the table to define a single-parameter opacity transfer function by calling <code>vpSetClassifierTable.</code> </p>
<p> The minimum opacity threshold should be set at the same time as the opacity transfer function. See the VP_MIN_VOXEL_OPACITY argument to <code>vpSetd</code>.</p>
<h2>State Variables</h2>
<p>The current classification function parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CLASSIFY_FIELD_COUNT, VP_CLASSIFY_FIELDS, VP_CLASSIFY_TABLES, VP_CLASSIFY_TABLE_SIZES, VP_MIN_VOXEL_OPACITY</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>Either <i>param_num</i> or <i>field_num</i> is out of range.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpclassifyscanline/">vpClassifyScanline</a>(3), <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3), <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3), <a href="/docs/linux/man/3-vpramp/">vpRamp</a>(3) </p>
