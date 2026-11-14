---
title: "vpseti(3)"
name: "vpseti"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpseti/"
description: "vpSeti, vpSetd – set the value of an option"
---

<p>vpSeti, vpSetd &#8211; set the value of an option</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSeti(</code><i>vpc, option, value</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>int <i>value;</i>  vpResult</p>
<dl>
<dt> <code>vpSetd(</code><i>vpc, option, value</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>double <i>value;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>Constant that specifies the option to be set.</p>
<dt><i>value</i></p>
<dd>New value for the option.</dl>
<h2>Description</h2>
<p>These functions are used to set the values of integer- or double-valued options in a rendering context. The following list summarizes the integer-valued options that can be set with <code>vpSeti</code>:</p>
<dl>
<dt>VP_CONCAT_MODE</p>
<dd>Choose whether transformation matrices are premultiplied or postmultiplied. If <i>value</i> is VP_CONCAT_LEFT then matrices are premultiplied. If <i>value</i> is VP_CONCAT_RIGHT then matrices are postmultiplied. Default: VP_CONCAT_RIGHT.</p>
<dt>VP_DEPTH_CUE_SIZE_HINT</p>
<dd>Set the suggested number of entries in the depth cueing lookup table. See <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3). Default: none</p>
<dt>VP_INT_WIDTH_HINT</p>
<dd>Set the suggested width (in pixels) of the intermediate image work buffer. See <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3). Default: none</p>
<dt>VP_INT_HEIGHT_HINT</p>
<dd>Set the suggested height (in pixels) of the intermediate image work buffer. See <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3). Default: none</p>
<dt>VP_SHADOW_LIGHT</p>
<dd>Get the current shadow light (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). Legal values are VP_LIGHT0, VP_LIGHT1, &#8230;, VP_LIGHT5. Default: VP_LIGHT0</p>
<dt>VP_SHADOW_WIDTH_HINT</p>
<dd>Set the suggested width (in pixels) of the shadow buffer (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). Default: none</p>
<dt>VP_SHADOW_HEIGHT_HINT</p>
<dd>Set the suggested height (in pixels) of the shadow buffer (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). Default: none</p>
<dt>VP_SHADOW_BIAS</p>
<dd>Set the current shadow bias value (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). The value is an integral distance in units of voxels. Default: 4</p>
<dt>VP_AXIS_OVERRIDE</p>
<dd>Force the rendering routine to composite along a particular principle viewing axis, regardless of the current viewing direction. Legal values are VP_X_AXIS, VP_Y_AXIS or VP_Z_AXIS. Set the value to VP_NO_AXIS to let VolPack choose the optimal axis automatically (the default). This option is normally used only for debugging.</p>
<dt>VP_TRACE_SHADOW_K</p>
<dd>When pixel tracing is enabled (see <a href="/docs/linux/man/3-vptracepixel/">vpTracePixel</a>(3)) and shadows are enabled (the VP_SHADOW option to <a href="/docs/linux/man/3-vpenable/">vpEnable</a>(3)), this option is used to choose one shadow buffer pixel to trace. The value must be a voxel slice number. The shadow buffer pixel that gets traced is the shadow pixel that affects the traced image pixel at the indicated slice.</dl>
<p> The following list summarizes the double-valued options that can be set with <code>vpSetd</code>:</p>
<dl>
<dt>VP_DEPTH_CUE_QUANTIZATION</p>
<dd>Set the difference in depth between two adjacent entries in the depth cueing lookup table (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)). Must be greater than 0.0 and less than 1.0. Default: 1/255</p>
<dt>VP_MAX_RAY_OPACITY</p>
<dd>Set the maximum opacity threshold. During rendering, when a pixel&#8217;s opacity reaches this threshold no more voxels are composited into the pixel. To maximize performance, the value should be as low as possible without adversely affecting image quality. Must be in the range 0.0-1.0 (1.0 is the default and 0.95 is the suggested value). Default: 1.0</p>
<dt>VP_MIN_VOXEL_OPACITY</p>
<dd>Set the minimum opacity threshold. During classification, if a voxel&#8217;s opacity is less than or equal to this threshold then the voxel is discarded before rendering. To maximize performance, the value should be as high as possible without adversely affecting image quality. Must be in the range 0.0-1.0 (0.0 is the default and 0.05 is the suggested value). Default: 0.0</dl>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>option</i> argument is invalid.</p>
<dt>VPERROR_BAD_VALUE</p>
<dd>The <i>value</i> argument is invalid or out of range.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3) </p>
