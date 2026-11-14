---
title: "sc_csgrad34qbtr(3)"
name: "sc_csgrad34qbtr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_csgrad34qbtr/"
description: "sc::CSGrad34Qbtr –"
---

<p>sc::CSGrad34Qbtr &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Thread</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CSGrad34Qbtr</code> (int mythread_a, int nthread_a, int me_a, int nproc_a, const <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem_a, const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;msg_a, const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp;lock_a, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;basis_a, const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;tbint_a, const <code>Ref</code>&lt; <code>TwoBodyDerivInt</code> &gt; &amp;tbintder_a, int nocc_a, int nfzc_a, double **scf_vector_a, double tol_a, int debug_a, int dynamic_a, double print_percent_a, <code>DistShellPair::SharedData</code> *shellpair_shared_data, int dograd_a, int natom_a) </p>
<p> void <code>set_i_offset</code> (int ioff) </p>
<p> void <code>set_ni</code> (int nivalue) </p>
<p> void <code>run</code> ()<br />
 <i>This is called with the </i><code>Thread</code> is run from a <code>ThreadGrp</code>.<br />
 double * <code>get_Lpi</code> () </p>
<p> double ** <code>get_ginter</code> () </p>
<p> int <code>get_aointder_computed</code> () </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
