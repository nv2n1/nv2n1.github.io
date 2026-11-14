---
title: "vpcreatecontext(3)"
name: "vpcreatecontext"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpcreatecontext/"
description: "vpCreateContext, vpDestroyContext – create/destroy a rendering context"
---

<p>vpCreateContext, vpDestroyContext &#8211; create/destroy a rendering context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpContext *</p>
<dl>
<dt> <code>vpCreateContext()</code> </p>
<pre><code>
void

    vpDestroyContext(vpc)

        vpContext *vpc;</code></pre>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p><code>vpCreateContext</code> returns a handle for a new rendering context. It contains default values for most of the rendering parameters. </p>
<p> <code>vpDestroyContext</code> destroys a rendering context and frees the associated memory. Only data structures allocated by the library are freed; application-defined data structures that are referenced in the rendering context through a pointer are not freed (e.g. arrays of volume data and shading lookup tables). The application is responsible for keeping track of such data structures and freeing them when appropriate.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3) </p>
