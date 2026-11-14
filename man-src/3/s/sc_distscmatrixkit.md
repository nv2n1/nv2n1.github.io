---
title: "sc_distscmatrixkit(3)"
name: "sc_distscmatrixkit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distscmatrixkit/"
description: "sc::DistSCMatrixKit –"
---

<p>sc::DistSCMatrixKit &#8211; </p>
<p> The <code>DistSCMatrixKit</code> produces matrices that work in a many processor environment.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;dist.h&gt;</code></pre>
<p> Inherits <code>sc::SCMatrixKit</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DistSCMatrixKit (const Ref&lt; MessageGrp &gt; &amp;grp=0)



DistSCMatrixKit (const Ref&lt; KeyVal &gt; &amp;)



SCMatrix * matrix (const RefSCDimension &amp;, const RefSCDimension &amp;)


Given the dimensions, create matrices or vectors.


SymmSCMatrix * symmmatrix (const RefSCDimension &amp;)



DiagSCMatrix * diagmatrix (const RefSCDimension &amp;)



SCVector * vector (const RefSCDimension &amp;)</code></pre>
<h2>Detailed Description</h2>
<p>The <code>DistSCMatrixKit</code> produces matrices that work in a many processor environment. </p>
<p> The matrix is distributed across all nodes.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
