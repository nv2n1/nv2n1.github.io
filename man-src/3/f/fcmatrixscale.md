---
title: "fcmatrixscale(3)"
name: "fcmatrixscale"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcmatrixscale/"
description: "FcMatrixScale – Scale a matrix"
---

<p>FcMatrixScale &#8211; Scale a matrix </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcMatrixScale (FcMatrix *</code><i>matrix</i><code>, double </code><i>sx</i><code>, double </code><i>dy</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcMatrixScale</code> multiplies <i>matrix</i> x values by <i>sx</i> and y values by <i>dy</i>. This is done by multiplying by the matrix: </p>
<pre> sx 0
 0 dy</pre>
