---
title: "vpsetclientdata(3)"
name: "vpsetclientdata"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetclientdata/"
description: "vpSetClientData – define a client data pointer"
---

<p>vpSetClientData &#8211; define a client data pointer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetClientData(</code><i>vpc, client_data</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>void *<i>client_data;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>client_data</i></p>
<dd>Pointer to application-specific client data.</dl>
<h2>Description</h2>
<p><code>vpSetClientData</code> is used to store a pointer to application-specific client data in the VolPack context. This pointer is passed to some of the callback routines (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)) to allow the application to define its own state variables. The pointer is not used by VolPack.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3) </p>
