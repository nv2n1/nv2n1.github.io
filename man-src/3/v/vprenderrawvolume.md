---
title: "vprenderrawvolume(3)"
name: "vprenderrawvolume"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vprenderrawvolume/"
description: "vpRenderRawVolume, vpRenderClassifiedVolume – render a volume"
---

<p>vpRenderRawVolume, vpRenderClassifiedVolume &#8211; render a volume</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpRenderRawVolume(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i>  vpResult</p>
<dl>
<dt> <code>vpRenderClassifiedVolume(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p>These routines are used to render a volume using the parameters in a rendering context. <code>vpRenderRawVolume</code> renders the data in the current voxel array and stores the result in the current image array. If an octree is present in the context (see <a href="/docs/linux/man/3-vpcreateminmaxoctree/">vpCreateMinMaxOctree</a>(3)) then it is used to accelerate rendering. <code>vpRenderClassifiedVolume</code> is identical in function except that it renders the current preclassified volume (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)) instead of the voxel array, and the octree is not used. </p>
<p> <code>vpRenderClassifiedVolume</code> should be used when the same volume is rendered multiple times with the same opacity transfer function. This rendering mode is the fastest. The opacity transfer function must not change because the voxel opacities must be fixed to compute a preclassified volume. </p>
<p> <code>vpRenderRawVolume</code> should be used when the volume data or the opacity transfer function changes in between renderings. If the volume data remains fixed then a min-max octree should be computed to accelerate rendering. Rendering is significantly faster with an octree than without, although it is still slower than rendering with <code>vpRenderClassifiedVolume</code>. </p>
<p> Before the rendering routines are called the rendering context must be initialized to set the volume parameters, classification parameters (<code>vpRenderRawVolume</code> only), viewing parameters, shading and lighting parameters, and image array. See <a href="/docs/linux/man/3-volpack/">VolPack</a>(3) for a list of relevant functions. </p>
<p> One important state variable should be adjusted before calling the rendering routines: the maximum opacity threshold. This number specifies a threshold value for the opacity of an image pixel. If the opacity of the pixel reaches the threshold then no more voxels are composited into the pixel. The threshold should be a number slightly less than one (0.95 is a good value); numbers closer to 1.0 result in longer rendering times, but less error. The value of the threshold is changed by calling <code>vpSetd</code> with the VP_MAX_RAY_OPACITY option. The default value is 1.0. </p>
<p> There are two additional state variables that can be adjusted to set the size of an internal data structure. During rendering, a work buffer called the intermediate image is used to hold temporary results. The size of this data structure depends on the size of the volume and the current view transformation matrix. Over the course of an animation sequence the intermediate image may have to be enlarged multiple times, resulting in many calls to the memory allocator. Normally the overhead of reallocating the data structure is negligible and can be ignored. However, this overhead can be eliminated by specifying hints for the maximum size of the intermediate image. The data structure will then be allocated once, and will never be reallocated unless an even larger intermediate image is required. To set the size hints, call <code>vpSeti</code> with the VP_INT_WIDTH_HINT and VP_INT_HEIGHT_HINT state variable codes. If the viewing transformation does not include any scaling, then the maximum possible size of each dimension of the intermediate image is twice the size of the largest dimension of the volume. To get a more precise bound, the intermediate image size required for rendering a volume with the current viewing parameters can be found by calling <code>vpGeti</code> with the VP_INTERMEDIATE_WIDTH and VP_INTERMEDIATE_HEIGHT state variable codes.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SHADER</p>
<dd>The shading lookup tables are sized incorrectly, or one of the voxel fields used to index the tables is invalid, or the number of material types is invalid.</p>
<dt>VPERROR_SINGULAR</p>
<dd>One of the current view transformation matrices is singular.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume size has not been set or is invalid, or there is no volume data.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function tables have invalid sizes or are associated with invalid voxel fields or have been incorrectly specified. (<code>vpRenderRawVolume</code> only)</p>
<dt>VPERROR_BAD_SHADOW</p>
<dd>The angle between the shadow light vector and the viewing direction is too large (must be less than 45 degrees). Either change the light direction or disable shadows (see vpSetShadowLookupShader).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
