---
title: "sc_hsosv1erep1qtr(3)"
name: "sc_hsosv1erep1qtr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_hsosv1erep1qtr/"
description: "sc::HSOSV1Erep1Qtr –"
---

<p>sc::HSOSV1Erep1Qtr &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Thread</code>.</p>
<h3>Public Member Functions</h3>
<p><code>HSOSV1Erep1Qtr</code> (int mythread_a, int nthread_a, int me_a, int nproc_a, const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp;lock_a, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;basis_a, const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;tbint_a, int ni_a, double **scf_vector_a, double tol_a, int debug_a) </p>
<p> void <code>run</code> ()<br />
 <i>This is called with the </i><code>Thread</code> is run from a <code>ThreadGrp</code>.<br />
 void <code>accum_buffer</code> (double *buffer) </p>
<p> void <code>set_data</code> (int R_a, int nr_a, int S_a, int ns_a, int ni_a, int ioffset_a) </p>
<p> double <code>aoint_computed</code> () </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
