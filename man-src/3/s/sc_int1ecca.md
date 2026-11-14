---
title: "sc_int1ecca(3)"
name: "sc_int1ecca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int1ecca/"
description: "sc::Int1eCCA –"
---

<p>sc::Int1eCCA &#8211; </p>
<p> <code>Int1eCCA</code> adapts CCA integrals components for use within SC.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;int1e.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Int1eCCA</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, int order, IntegralEvaluatorFactory, std::string, bool) </p>
<p> double * <code>buffer</code> () </p>
<p> void <code>overlap</code> (int ish, int jsh) </p>
<p> void <code>overlap_1der</code> (int ish, int jsh, Chemistry_QC_GaussianBasis_DerivCenters &amp;dc) </p>
<p> void <code>kinetic</code> (int ish, int jsh) </p>
<p> void <code>kinetic_1der</code> (int ish, int jsh, Chemistry_QC_GaussianBasis_DerivCenters &amp;dc) </p>
<p> void <code>nuclear</code> (int ish, int jsh) </p>
<p> void <code>nuclear_1der</code> (int ish, int jsh, Chemistry_QC_GaussianBasis_DerivCenters &amp;dc) </p>
<p> void <code>hcore</code> (int ish, int jsh) </p>
<p> void <code>hcore_1der</code> (int ish, int jsh, Chemistry_QC_GaussianBasis_DerivCenters &amp;dc)</p>
<h3>Protected Attributes</h3>
<p><code>Integral</code> * <code>integral_</code></p>
<h2>Detailed Description</h2>
<p><code>Int1eCCA</code> adapts CCA integrals components for use within SC. </p>
<p> It is used by <code>OneBodyIntCCA</code> and <code>OneBodyDerivIntCCA</code> to implement the <code>IntegralCCA</code> class.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
