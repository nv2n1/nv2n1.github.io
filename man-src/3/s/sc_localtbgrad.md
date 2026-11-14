---
title: "sc_localtbgrad(3)"
name: "sc_localtbgrad"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_localtbgrad/"
description: "sc::LocalTBGrad –"
---

<p>sc::LocalTBGrad &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::TBGrad&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LocalTBGrad (T &amp;t, const Ref&lt; TwoBodyDerivInt &gt; &amp;tbdi, const Ref&lt; PetiteList &gt; &amp;pl, const Ref&lt; GaussianBasisSet &gt; &amp;bs, const Ref&lt; MessageGrp &gt; &amp;g, double *tbg, double pm, double a, int nt=1, int tn=0, double exchange_fraction=1.0)



void run ()


This is called with the Thread is run from a ThreadGrp.



Public Attributes
double * tbgrad



Protected Attributes</code></pre>
<p> <code>MessageGrp</code> * <code>grp_</code> </p>
<p> <code>TwoBodyDerivInt</code> * <code>tbi_</code> </p>
<p> <code>GaussianBasisSet</code> * <code>gbs_</code> </p>
<p> <code>PetiteList</code> * <code>rpl_</code> </p>
<p> <code>Molecule</code> * <code>mol_</code> </p>
<p> double <code>pmax_</code> </p>
<p> double <code>accuracy_</code> </p>
<p> int <code>threadno_</code> </p>
<p> int <code>nthread_</code></p>
<h3>template&lt;class T&gt; class sc::LocalTBGrad&lt; T &gt;</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
