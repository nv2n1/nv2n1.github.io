---
title: "sc_psiuhf(3)"
name: "sc_psiuhf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiuhf/"
description: "sc::PsiUHF –"
---

<p>sc::PsiUHF &#8211; </p>
<p> <code>PsiUHF</code> is a concrete implementation of Psi <code>UHF</code> wave function.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiwfn.h&gt;</code></pre>
<p> Inherits <code>sc::PsiSCF</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PsiUHF</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PsiUHF</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>write_basic_input</code> (int conv)<br />
 <i>Writes out Psi input file entries specific to this </i><code>PsiWavefunction</code>.<br />
 int <code>spin_polarized</code> ()<br />
 <i>Return 1 if the alpha density is not equal to the beta density. </i><br />
 int <code>gradient_implemented</code> () const </p>
<p> PsiSCF::RefType <code>reftype</code> () const<br />
 <i>Returns the PsiSCF::RefType of this particular Psi </i><code>SCF</code> wave function.</p>
<h3>Protected Member Functions</h3>
<p>void <code>write_input</code> (int conv)<br />
 <i>Prepares a complete Psi input file. The input file is assumed to have been opened. </i></p>
<h2>Detailed Description</h2>
<p><code>PsiUHF</code> is a concrete implementation of Psi <code>UHF</code> wave function.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PsiUHF::write_basic_input (int conv) [virtual]</h3>
<p>Writes out Psi input file entries specific to this <code>PsiWavefunction</code>. The input file is assumed to have been opened. </p>
<p> Reimplemented from <code>sc::PsiWavefunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
