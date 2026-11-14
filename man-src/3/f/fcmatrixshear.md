---
title: "fcmatrixshear(3)"
name: "fcmatrixshear"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcmatrixshear/"
description: "FcMatrixShear – Shear a matrix"
---

<p>FcMatrixShear &#8211; Shear a matrix </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcMatrixShear (FcMatrix *</code><i>matrix</i><code>, double </code><i>sh</i><code>, double </code><i>sv</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcMatrixShare</code> shears <i>matrix</i> horizontally by <i>sh</i> and vertically by <i>sv</i>. This is done by multiplying by the matrix: </p>
<pre> 1 sh
 sv 1</pre>
