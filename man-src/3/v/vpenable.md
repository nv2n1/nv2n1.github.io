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
<dt> <code>vpEnable(</code><i>vpc, option, value</i><code>)</code></dt>
<dd>
</dd><dd>vpContext *<i>vpc;</i></dd>
<dd>int <i>option;</i></dd>
<dd>int <i>value;</i></dd></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></dt>
<dd>VolPack context from <code>vpCreateContext.</code></dd>
<dt><i>option</i></dt>
<dd>Constant that specifies the option to be adjusted.</dd>
<dt><i>value</i></dt>
<dd>New value for the option (boolean: 0 or 1).</dd></dl>
<h2>Description</h2>
<p><code>vpEnable</code> is used to enable or disable boolean options in a rendering context. If the <i>value</i> option is 0 then the option is disabled; otherwise it is enabled. The following list summarizes all available options:</p>
<dl>
<dt>VP_LIGHT0</dt>
<dd>
</dd><dt>VP_LIGHT1</dt>
<dd>
</dd><dt>VP_LIGHT2</dt>
<dd>
</dd><dt>VP_LIGHT3</dt>
<dd>
</dd><dt>VP_LIGHT4</dt>
<dd>
</dd><dt>VP_LIGHT5</dt>
<dd>Enable the corresponding light source (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)). Default: VP_LIGHT0 is enabled, and all others are disabled.</dd>
<dt>VP_LIGHT_BOTH_SIDES</dt>
<dd>Enable two-sided lighting (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)). Default: disabled</dd>
<dt>VP_REVERSE_SURFACE_SIDES</dt>
<dd>Reverse the definition of interior and exterior surfaces (see <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3)). Default: disabled</dd>
<dt>VP_DEPTH_CUE</dt>
<dd>Enable depth cueing (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)). Default: disabled</dd>
<dt>VP_VIEW_X_AXIS</dt>
<dd>
</dd><dt>VP_VIEW_Y_AXIS</dt>
<dd>
</dd><dt>VP_VIEW_Z_AXIS</dt>
<dd>Enable computing a preclassified volume for the corresponding major viewing axis (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)). Default: enabled</dd>
<dt>VP_SHADOW</dt>
<dd>Enable rendering shadows (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)). Default: disabled</dd>
<dt>VP_CLAMP_SHADE_TABLE</dt>
<dd>Enable clamping the color components in a shade table to the range 0.0-255.0. This option affects vpShadeTable(). Default: enabled</dd></dl>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</dt>
<dd>The <i>option</i> argument is invalid.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
