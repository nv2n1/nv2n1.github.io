---
title: "sc_psiscf(3)"
name: "sc_psiscf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_psiscf/"
description: "sc::PsiSCF –"
---

<p>sc::PsiSCF &#8211; </p>
<p> <code>PsiSCF</code> is an abstract base for all Psi <code>SCF</code> wave functions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;psiwfn.h&gt;</code></pre>
<p> Inherits <code>sc::PsiWavefunction</code>. Inherited by <code>sc::PsiCLHF</code>, <code>sc::PsiHSOSHF</code>, and <code>sc::PsiUHF</code>.</p>
<h3>Public Types</h3>
<p>enum <code>RefType</code> { <code>rhf</code>, <code>hsoshf</code>, <code>uhf</code> }</p>
<h3>Public Member Functions</h3>
<p><code>PsiSCF</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>PsiSCF</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual PsiSCF::RefType <code>reftype</code> () const =0<br />
 <i>Returns the PsiSCF::RefType of this particular Psi </i><code>SCF</code> wave function.</p>
<h2>Detailed Description</h2>
<p><code>PsiSCF</code> is an abstract base for all Psi <code>SCF</code> wave functions.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PsiSCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::PsiWavefunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
