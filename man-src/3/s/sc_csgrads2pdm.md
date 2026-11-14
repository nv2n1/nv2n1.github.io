---
title: "sc_csgrads2pdm(3)"
name: "sc_csgrads2pdm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_csgrads2pdm/"
description: "sc::CSGradS2PDM –"
---

<p>sc::CSGradS2PDM &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Thread</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CSGradS2PDM</code> (int mythread_a, int nthread_a, int me_a, int nproc_a, const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp;lock_a, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;basis_a, const <code>Ref</code>&lt; <code>TwoBodyDerivInt</code> &gt; &amp;tbintder_a, const double *PHF_a, const double *P2AO_a, int tol_a, int debug_a, int dynamic_a) </p>
<p> void <code>accum_mp2_contrib</code> (double **ginter) </p>
<p> void <code>accum_hf_contrib</code> (double **hf_ginter) </p>
<p> void <code>run</code> ()<br />
 <i>This is called with the </i><code>Thread</code> is run from a <code>ThreadGrp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
