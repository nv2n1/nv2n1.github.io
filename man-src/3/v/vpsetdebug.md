---
title: "vpsetdebug(3)"
name: "vpsetdebug"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetdebug/"
description: "vpSetDebug – enable/disable debugging options"
---

<p>vpSetDebug &#8211; enable/disable debugging options</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetDebug(</code><i>vpc, flag, value</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>flag;</i></p>
<dd>int <i>value;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>flag</i></p>
<dd>Constant that specifies the debugging option to be adjusted.</p>
<dt><i>value</i></p>
<dd>New value for the option (boolean: 0 or 1).</dl>
<h2>Description</h2>
<p><code>vpSetDebug</code> is used to enable or disable a debugging option in a rendering context. The debugging options cause messages to be printed during execution. These messages are probably useless without a good understanding of the source code. If the <i>value</i> option is 0 then the option is disabled; otherwise it is enabled. The following list summarizes all available options:</p>
<dl>
<dt>VPDEBUG_VIEW</p>
<dd>view transform calculations</p>
<dt>VPDEBUG_RENDER</p>
<dd>high-level rendering stages</p>
<dt>VPDEBUG_RBUF</p>
<dd>intermediate image (render buffer) allocation</p>
<dt>VPDEBUG_OPCCORRECT</p>
<dd>opacity correction</p>
<dt>VPDEBUG_DEPTHCUE</p>
<dd>depth cueing</p>
<dt>VPDEBUG_PYRAMID</p>
<dd>pyramid construction</p>
<dt>VPDEBUG_OCTREE</p>
<dd>octree construction</p>
<dt>VPDEBUG_CLSFYOCTREE</p>
<dd>octree classification</p>
<dt>VPDEBUG_OCTREERUNS</p>
<dd>runs computed from octree</p>
<dt>VPDEBUG_OCTREETRAVERSE</p>
<dd>octree traversal</p>
<dt>VPDEBUG_TRANSPOSE</p>
<dd>volume transposing</p>
<dt>VPDEBUG_COMPOSITE</p>
<dd>compositing</dl>
<p> The VolPack library must be compiled with the -DDEBUG compiler option for this function to have any effect.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>flag</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
