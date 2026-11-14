---
title: "sc_accumh(3)"
name: "sc_accumh"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_accumh/"
description: "sc::AccumH –"
---

<p>sc::AccumH &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::AccumHNull</code>, <code>sc::BEMSolventH</code>, and <code>sc::SumAccumH</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>AccumH (StateIn &amp;)



AccumH (const Ref&lt; KeyVal &gt; &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual void init (const Ref&lt; Wavefunction &gt; &amp;)



virtual void accum (const RefSymmSCMatrix &amp;h)=0



virtual void print_summary ()



virtual void done ()



virtual double e ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Wavefunction</code> &gt; <code>wfn_</code></p>
<h2>Member Function Documentation</h2>
<h3>void sc::AccumH::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::AccumHNull</code>, <code>sc::SumAccumH</code>, and <code>sc::BEMSolventH</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
