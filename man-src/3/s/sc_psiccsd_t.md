---
title: "sc_psiccsd_t(3)"
name: "sc_psiccsd_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiccsd_t/"
description: "sc::PsiCCSD_T –"
---

<p>sc::PsiCCSD_T &#8211; </p>
<p> <code>PsiCCSD_T</code> is a concrete implementation of Psi CCSD(T) wave function.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiwfn.h&gt;</code></pre>
<p> Inherits <code>sc::PsiWavefunction</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PsiCCSD_T</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PsiCCSD_T</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>spin_polarized</code> ()<br />
 <i>Return 1 if the alpha density is not equal to the beta density. </i><br />
 int <code>gradient_implemented</code> () const</p>
<h3>Protected Member Functions</h3>
<p>void <code>write_input</code> (int conv)<br />
 <i>Prepares a complete Psi input file. The input file is assumed to have been opened. </i></p>
<h2>Detailed Description</h2>
<p><code>PsiCCSD_T</code> is a concrete implementation of Psi CCSD(T) wave function.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PsiCCSD_T::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::PsiWavefunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
