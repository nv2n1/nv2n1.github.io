---
title: "sc_localscmatrixkit(3)"
name: "sc_localscmatrixkit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_localscmatrixkit/"
description: "sc::LocalSCMatrixKit –"
---

<p>sc::LocalSCMatrixKit &#8211; </p>
<p> The <code>LocalSCMatrixKit</code> produces matrices that work in a single processor environment.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;local.h&gt;</code></pre>
<p> Inherits <code>sc::SCMatrixKit</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LocalSCMatrixKit</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>SCMatrix</code> * <code>matrix</code> (const <code>RefSCDimension</code> &amp;, const <code>RefSCDimension</code> &amp;)<br />
 <i>Given the dimensions, create matrices or vectors. </i><br />
 <code>SymmSCMatrix</code> * <code>symmmatrix</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>DiagSCMatrix</code> * <code>diagmatrix</code> (const <code>RefSCDimension</code> &amp;) </p>
<p> <code>SCVector</code> * <code>vector</code> (const <code>RefSCDimension</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>The <code>LocalSCMatrixKit</code> produces matrices that work in a single processor environment.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
