---
title: "vpbruteforcerender(3)"
name: "vpbruteforcerender"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpbruteforcerender/"
description: "vpBruteForceRender – render using a simple brute-force method"
---

<p>vpBruteForceRender &#8211; render using a simple brute-force method</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpBruteForceRender(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p>This function is for debugging purposes only. It performs the same function as <code>vpRenderRawVolume</code>, but uses a simpler, very inefficient algorithm. The two functions should produce identical results.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3) </p>
