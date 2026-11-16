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
<dt> <code>vpSetDebug(</code><i>vpc, flag, value</i><code>)</code></dt>
<dd>
</dd><dd>vpContext *<i>vpc;</i></dd>
<dd>int <i>flag;</i></dd>
<dd>int <i>value;</i></dd></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></dt>
<dd>VolPack context from <code>vpCreateContext.</code></dd>
<dt><i>flag</i></dt>
<dd>Constant that specifies the debugging option to be adjusted.</dd>
<dt><i>value</i></dt>
<dd>New value for the option (boolean: 0 or 1).</dd></dl>
<h2>Description</h2>
<p><code>vpSetDebug</code> is used to enable or disable a debugging option in a rendering context. The debugging options cause messages to be printed during execution. These messages are probably useless without a good understanding of the source code. If the <i>value</i> option is 0 then the option is disabled; otherwise it is enabled. The following list summarizes all available options:</p>
<dl>
<dt>VPDEBUG_VIEW</dt>
<dd>view transform calculations</dd>
<dt>VPDEBUG_RENDER</dt>
<dd>high-level rendering stages</dd>
<dt>VPDEBUG_RBUF</dt>
<dd>intermediate image (render buffer) allocation</dd>
<dt>VPDEBUG_OPCCORRECT</dt>
<dd>opacity correction</dd>
<dt>VPDEBUG_DEPTHCUE</dt>
<dd>depth cueing</dd>
<dt>VPDEBUG_PYRAMID</dt>
<dd>pyramid construction</dd>
<dt>VPDEBUG_OCTREE</dt>
<dd>octree construction</dd>
<dt>VPDEBUG_CLSFYOCTREE</dt>
<dd>octree classification</dd>
<dt>VPDEBUG_OCTREERUNS</dt>
<dd>runs computed from octree</dd>
<dt>VPDEBUG_OCTREETRAVERSE</dt>
<dd>octree traversal</dd>
<dt>VPDEBUG_TRANSPOSE</dt>
<dd>volume transposing</dd>
<dt>VPDEBUG_COMPOSITE</dt>
<dd>compositing</dd></dl>
<p> The VolPack library must be compiled with the -DDEBUG compiler option for this function to have any effect.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</dt>
<dd>The <i>flag</i> argument is invalid.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
