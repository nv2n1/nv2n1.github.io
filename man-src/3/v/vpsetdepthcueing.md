---
title: "vpsetdepthcueing(3)"
name: "vpsetdepthcueing"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetdepthcueing/"
description: "vpSetDepthCueing – set depth cueing parameters"
---

<p>vpSetDepthCueing &#8211; set depth cueing parameters</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetDepthCueing(</code><i>vpc, front_factor, density</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>double <i>front_factor;</i></p>
<dd>double <i>density;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>front_factor</i></p>
<dd>Depth cueing factor at the front clipping plane.</p>
<dt><i>density</i></p>
<dd>Fog density.</dl>
<h2>Description</h2>
<p><code>vpSetDepthCueing</code> is used to set the parameters for depth cueing. Depth cueing is a simulated fog that makes objects in the distance appear darker than foreground objects. Depth cueing is independent of the shading method. It can be used with lookup-table shading or callback-function shading. Depth cueing is not stored in the shading lookup table; it is always applied to voxels at rendering time. </p>
<p> The <i>front_factor</i> argument is the transparency of the fog at the front clipping plane (see <a href="/docs/linux/man/3-vpwindow/">vpWindow</a>(3) or <a href="/docs/linux/man/3-vpwindowphigs/">vpWindowPHIGS</a>(3)). It must be a positive number and is usually less than 1.0 (although larger numbers can be used to brighten the foreground). The <i>density</i> argument controls the &quot;density&quot; of the fog. Increasing the density causes objects to recede into darkness over a shorter distance. The equation for the transparency of the fog at a particular voxel is:</p>
<dl>
<dd>T = front_factor * exp(-density * depth)</dl>
<p> where <i>depth</i> is 0 at the front clipping plane and 1 at the back clipping plane. Each voxel color component is multiplied by the fog transparency during rendering. </p>
<p> By default, depth cueing is not enabled. To enable it, call <code>vpEnable</code> with the VP_DEPTH_CUE option. </p>
<p> Depth cueing is implemented using an internal lookup table (unrelated to the shading lookup table). There are several VolPack state variables that affect the depth cueing table, although they should not usually be changed. The table contains depth cueing factors as a function of depth. The table must contain entries for depths in the range 0.0-1.0, and possibly for negative depths depending upon the current viewing parameters (the reason for this is beyond the scope of a man page). The VP_DEPTH_CUE_QUANTIZATION variable (which can be set by calling <code>vpSetd</code>) determines the depth difference between two adjacent entries in the depth cueing table. For instance, the default quantization of 1/255 specifies that each entry in the table represents 1/255 times the distance between the front and back clipping planes. Reducing the quantization increases the size and accuracy of the depth cueing table. </p>
<p> Normally the depth cueing table is resized and recomputed only when necessary. Recomputation may be required if the viewpoint changes, increasing the range of voxel depths that are encountered (recall that there is no lower bound on the depth). You can use <code>vpGeti</code> with the VP_DEPTH_CUE_TABLE_SIZE state variable code to get the current number of table entries. You can also set the value of VP_DEPTH_CUE_TABLE_SIZE_HINT (using <code>vpSeti</code>) to suggest a size for the table. This might be desirable if you plan to compute an animation loop and want to ensure that the depth cueing table does not need to be recomputed in the middle of the sequence. However, since recomputing the table is relatively inexpensive, it should not be necessary to use this option.</p>
<h2>State Variables</h2>
<p>Information about the current depth cueing properties can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_DEPTH_CUE, VP_DEPTH_CUE_FRONT, VP_DEPTH_CUE_DENSITY, VP_DEPTH_CUE_TABLE_SIZE, VP_DEPTH_CUE_SIZE_HINT, VP_DEPTH_CUE_QUANTIZATION.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The value of <i>front_factor</i> is not positive.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) </p>
