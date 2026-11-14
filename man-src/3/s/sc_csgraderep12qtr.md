---
title: "sc_csgraderep12qtr(3)"
name: "sc_csgraderep12qtr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_csgraderep12qtr/"
description: "sc::CSGradErep12Qtr –"
---

<p>sc::CSGradErep12Qtr &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::Thread</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CSGradErep12Qtr</code> (int mythread_a, int nthread_a, int me_a, int nproc_a, const <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem_a, const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;msg_a, const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp;lock_a, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;basis_a, const <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; &amp;tbint_a, int nocc_a, double **scf_vector_a, double tol_a, int debug_a, int dynamic_a, double print_percent_a, <code>DistShellPair::SharedData</code> *shellpair_shared_data, int usep4) </p>
<p> void <code>set_i_offset</code> (int ioff) </p>
<p> void <code>set_ni</code> (int nivalue) </p>
<p> void <code>run</code> ()<br />
 <i>This is called with the </i><code>Thread</code> is run from a <code>ThreadGrp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
