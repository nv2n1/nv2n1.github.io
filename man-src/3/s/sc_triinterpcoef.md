---
title: "sc_triinterpcoef(3)"
name: "sc_triinterpcoef"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_triinterpcoef/"
description: "sc::TriInterpCoef –"
---

<p>sc::TriInterpCoef &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TriInterpCoef</code> (const <code>TriInterpCoefKey</code> &amp;key) </p>
<p> double &amp; <code>coef</code> (int i, int j, int k) </p>
<p> double &amp; <code>rderiv</code> (int i, int j, int k) </p>
<p> double &amp; <code>sderiv</code> (int i, int j, int k)</p>
<h3>Static Public Member Functions</h3>
<pre><code>static int ijk_to_index (int i, int j, int k)



static int order_to_nvertex (int order)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
