---
title: "sc_accumeffectiveh(3)"
name: "sc_accumeffectiveh"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_accumeffectiveh/"
description: "sc::AccumEffectiveH –"
---

<p>sc::AccumEffectiveH &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::BlockedSCElementOp2</code>. Inherited by <code>sc::GSGeneralEffH</code>, <code>sc::GSHighSpinEffH</code>, <code>sc::PsiEffH</code>, and <code>sc::TestEffH</code>.</p>
<h3>Public Member Functions</h3>
<p><code>AccumEffectiveH</code> (<code>SCF</code> *) </p>
<p> virtual void <code>process</code> (<code>SCMatrixBlockIter</code> &amp;, <code>SCMatrixBlockIter</code> &amp;)</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual void init ()=0



int index (int hindex, int shelli, int shellj)



int shell (double)



double &amp; coef (int i, int j, int k)



Protected Attributes</code></pre>
<p> <code>SCF</code> * <code>scf_</code> </p>
<p> double <code>coef_</code> [18] </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
