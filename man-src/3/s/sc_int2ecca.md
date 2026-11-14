---
title: "sc_int2ecca(3)"
name: "sc_int2ecca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int2ecca/"
description: "sc::Int2eCCA –"
---

<p>sc::Int2eCCA &#8211; </p>
<p> <code>Int2eCCA</code> adapts CCA integrals components for use within SC.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/int2e.h">int2e.h</a>&gt; </p>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>Int2eCCA</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4, int order, size_t storage, IntegralEvaluatorFactory, bool, string) </p>
<p> double * <code>buffer</code> () </p>
<p> void <code>compute_erep</code> (int is, int js, int ks, int ls) </p>
<p> void <code>compute_erep_1der</code> (int is, int js, int ks, int ls, Chemistry::QC::GaussianBasis::DerivCenters &amp;dc) </p>
<p> int <code>redundant</code> () const </p>
<p> void <code>set_redundant</code> (int i) </p>
<h3>Protected Attributes</h3>
<p> <code>Integral</code> * <code>integral_</code> </p>
<h2>Detailed Description</h2>
<p> <code>Int2eCCA</code> adapts CCA integrals components for use within SC. </p>
<p> It is used by <code>TwoBodyIntCCA</code> and <code>TwoBodyDerivIntCCA</code> to implement the <code>IntegralCCA</code> class. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
