---
title: "vpgetimage(3)"
name: "vpgetimage"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgetimage/"
description: "vpGetImage – get a field of the intermediate image"
---

<p>vpGetImage &#8211; get a field of the intermediate image</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetImage(</code><i>vpc, image, width, height, scan_bytes,</p>
<dd>pixel_type, image_type</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>void *<i>image;</i></p>
<dd>int <i>width, height;</i></p>
<dd>int <i>scan_bytes;</i></p>
<dd>int <i>pixel_type, image_type;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>image</i></p>
<dd>2D array for storing result image.</p>
<dt><i>width</i></p>
<dd>Width of array in pixels.</p>
<dt><i>height</i></p>
<dd>Height of array in pixels.</p>
<dt><i>scan_bytes</i></p>
<dd>Number of bytes per scanline in array.</p>
<dt><i>pixel_type</i></p>
<dd>Code indicating the format of each pixel in the array.</p>
<dt><i>image_type</i></p>
<dd>Code indicating the source of the image data (VP_IMAGE_BUFFER or VP_SHADOW_BUFFER).</dl>
<h2>Description</h2>
<p>This is a debugging function. It is used to retrieve the contents of one of the temporary rendering buffers used during rendering, namely the intermediate image or the shadow buffer. Rendering consists of two stages: the volume is resampled and composited into the intermediate image to produce a distorted volume rendering, and then the intermediate image is warped into the final image. If shadows are enabled then the shadow buffer is used during the first stage to incrementally compute which voxels are illuminated by the light source. This function returns images produced during the first stage, before the final warp. </p>
<p> This function may be called after a call to one of the rendering routines (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)). If the <i>image_type</i> argument is VP_IMAGE_BUFFER then data will be copied from the intermediate image. The <i>pixel_type</i> argument specifies what information to copy and the format for storing the data in the output array. The possible values for <i>pixel_type</i> are the same as for the <i>pixel_type</i> argument to <code>vpSetImage.</code> For instance, use VP_LUMINANCE to extract the grayscale intensity (assuming the current shader produces grayscale pixels). </p>
<p> If the <i>image_type</i> argument is VP_SHADOW_BUFFER then data will be copied from the shadow buffer. The only valid option for <i>pixel_type</i> is VP_ALPHA, since no color information is stored in the shadow buffer. </p>
<p> See <code>vpSetImage</code> for details on the pixel formats, the layout of the output array, and the remaining arguments. </p>
<p> To find the required size for the result array, use <code>vpGeti</code> with the VP_INTERMEDIATE_WIDTH and VP_INTERMEDIATE_HEIGHT options (when <i>image_type</i> is VP_IMAGE_BUFFER) or the VP_SHADOW_WIDTH and VP_SHADOW_HEIGHT options (when <i>image_type</i> is VP_SHADOW_BUFFER).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SIZE</p>
<dd>The destination array size is incorrect or there is no intermediate image.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>field</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3), <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3) </p>
