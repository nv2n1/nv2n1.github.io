---
title: "vpenable(3)"
name: "vpenable"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpenable/"
description: "vpEnable – enable or disable options"
---

<p>vpEnable &#8211; enable or disable options</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpEnable(</code><i>vpc, option, value</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>int <i>value;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>Constant that specifies the option to be adjusted.</p>
<dt><i>value</i></p>
<dd>New value for the option (boolean: 0 or 1).</dl>
<h2>Description</h2>
<p><code>vpEnable</code> is used to enable or disable boolean options in a rendering context. If the <i>value</i> option is 0 then the option is disabled; otherwise it is enabled. The following list summarizes all available options:</p>
<dl>
<dt>VP_LIGHT0</p>
<dd>
<dt>VP_LIGHT1</p>
<dd>
<dt>VP_LIGHT2</p>
<dd>
<dt>VP_LIGHT3</p>
<dd>
<dt>VP_LIGHT4</p>
<dd>
<dt>VP_LIGHT5</p>
<dd>Enable the corresponding light source (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)). Default: VP_LIGHT0 is enabled, and all others are disabled.</p>
<dt>VP_LIGHT_BOTH_SIDES</p>
<dd>Enable two-sided lighting (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)). Default: disabled</p>
<dt>VP_REVERSE_SURFACE_SIDES</p>
<dd>Reverse the definition of interior and exterior surfaces (see <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3)). Default: disabled</p>
<dt>VP_DEPTH_CUE</p>
<dd>Enable depth cueing (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)). Default: disabled</p>
<dt>VP_VIEW_X_AXIS</p>
<dd>
<dt>VP_VIEW_Y_AXIS</p>
<dd>
<dt>VP_VIEW_Z_AXIS</p>
<dd>Enable computing a preclassified volume for the corresponding major viewing axis (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)). Default: enabled</p>
<dt>VP_SHADOW</p>
<dd>Enable rendering shadows (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). Default: disabled</p>
<dt>VP_CLAMP_SHADE_TABLE</p>
<dd>Enable clamping the color components in a shade table to the range 0.0-255.0. This option affects vpShadeTable(). Default: enabled</dl>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The <i>option</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
