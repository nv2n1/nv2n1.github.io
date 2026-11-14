---
title: "fcmatrixrotate(3)"
name: "fcmatrixrotate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcmatrixrotate/"
description: "FcMatrixRotate – Rotate a matrix"
---

<p>FcMatrixRotate &#8211; Rotate a matrix </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcMatrixRotate (FcMatrix *</code><i>matrix</i><code>, double </code><i>cos</i><code>, double </code><i>sin</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcMatrixRotate</code> rotates <i>matrix</i> by the angle who&#8217;s sine is <i>sin</i> and cosine is <i>cos</i>. This is done by multiplying by the matrix: </p>
<pre> cos -sin
 sin cos</pre>
