---
title: "vpsetimage(3)"
name: "vpsetimage"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetimage/"
description: "vpSetImage – specify an image array"
---

<p>vpSetImage &#8211; specify an image array</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetImage(</code><i>vpc, image, width, height, scan_bytes, pixel_type</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>unsigned char *<i>image;</i></p>
<dd>int <i>width, height;</i></p>
<dd>int <i>scan_bytes;</i></p>
<dd>int <i>pixel_type;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>image</i></p>
<dd>2D array for storing result images.</p>
<dt><i>width</i></p>
<dd>Width of image in pixels.</p>
<dt><i>height</i></p>
<dd>Height of image in pixels.</p>
<dt><i>scan_bytes</i></p>
<dd>Number of bytes per scanline in image array.</p>
<dt><i>pixel_type</i></p>
<dd>Code indicating the format of each pixel in the array.</dl>
<h2>Description</h2>
<p><code>vpSetImage</code> is used to specify a buffer for storing the result image during rendering. The <i>width</i> and <i>height</i> parameters specify the size of the result image. The clipping window (see <a href="/docs/linux/man/3-vpwindow/">vpWindow</a>(3) or <a href="/docs/linux/man/3-vpwindowphigs/">vpWindowPHIGS</a>(3)) is scaled to exactly match the specified size. The <i>scan_bytes</i> argument specifies the size of a scanline in the image array, in bytes. This argument can be used to add padding to the end of each scanline to satisfy alignment restrictions (e.g. raster operations sometimes require the beginning of each scanline to lie on a word boundary). The <i>pixel_type</i> argument specifies the format of a pixel. The following formats are supported:</p>
<dl>
<dt>VP_ALPHA</p>
<dd>Each pixel is one byte and contains an 8-bit alpha channel (containing an opacity or coverage value for the pixel).</p>
<dt>VP_LUMINANCE</p>
<dd>Each pixel is one byte and contains an 8-bit grayscale intensity.</p>
<dt>VP_LUMINANCEA</p>
<dd>Each pixel is two bytes and contains an 8-bit grayscale intensity followed by an 8-bit alpha channel.</p>
<dt>VP_RGB</p>
<dd>Each pixel is three bytes and contains an RGB color (8 bits/channel). The R channel is stored first, followed by G and then B.</p>
<dt>VP_RGBA</p>
<dd>Each pixel is four bytes and contains an RGBA color with an alpha channel (8 bits/channel). The R channel is stored first, followed by G, B and A.</p>
<dt>VP_BGR</p>
<dd>Each pixel is three bytes and contains an RGB color (8 bits/channel). The B channel is stored first, follow by G and then R.</p>
<dt>VP_ABGR</p>
<dd>Each pixel is four bytes and contains an RGBA color with an alpha channel (8 bits/channel). The A channel is stored first, followed by B, G and R.</dl>
<p> The formats VP_LUMINANCE and VP_LUMINANCEA may only be used with grayscale shaders (the <i>color_channels</i> argument to <code>vpSetLookupShader</code> must be 1, or if you are using a callback function for shading you must use the VP_GRAY_SHADE_FUNC argument to <code>vpSetCallback</code>). The formats VP_RGB, VP_RGBA, VP_BGR and VP_ABGR may only be used with color shaders. The format VP_ALPHA may be used with either type of shader. The size of the <i>image</i> array must be:</p>
<dl>
<dd>unsigned char <i>image[height][scan_bytes];</i></dl>
<p> The <i>scan_bytes</i> argument must be at least <i>width</i> times the number of bytes per pixel. Pixels in a horizontal scanline are packed next to each other, regardless of the size of the pixel. Any extra padding bytes at the end of a scanline are not modified. The alpha channel may be used to composite the rendered image against a background image. Alpha gives the fraction of the background that is visible through the rendered image (0 for fully visible, 255 for fully obscured). As an example, to change the background color of the image to a solid color C, modify the color of each pixel in the image according to the formula:</p>
<dl>
<dd>color(x,y) += C * (1 &#8211; alpha(x,y)/255)</dl>
<h2>State Variables</h2>
<p>The current image array properties can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_IMAGE, VP_IMAGE_WIDTH, VP_IMAGE_HEIGHT, VP_IMAGE_SCAN_SIZE, VP_PIXEL_TYPE.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3) </p>
