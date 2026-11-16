---
title: "vpgeterror(3)"
name: "vpgeterror"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgeterror/"
description: "vpGetError, vpGetErrorString – retrieve error codes"
---

<p>vpGetError, vpGetErrorString &#8211; retrieve error codes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetError(</code><i>vpc</i><code>)</code></dt>
<dd>
</dd><dd>vpContext *<i>vpc;</i> </dd>
<pre><code>
char *
vpGetErrorString(code)
vpResult code;</code></pre>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></dt>
<dd>VolPack context from <code>vpCreateContext.</code></dd>
<dt><i>code</i></dt>
<dd>A VolPack error result code.</dd></dl>
<h2>Description</h2>
<p>These routines are used for error handling. <code>vpGetError</code> return the error code from the first function call that failed since the last call to <code>vpGetError</code>. <code>vpGetErrorString</code> returns a descriptive string corresponding to an error code. The string is stored in a global array so it does not need to be copied to separate memory.</p>
<h2>Errors</h2>
<p><code>vpGetError</code> cannot fail. A return value not equal to VP_OK means that some previous function call has failed. <code>vpGetErrorString</code> returns NULL if <i>code</i><code> is invalid. </code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
</dl>