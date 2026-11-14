---
title: "sc_mp2r12energy(3)"
name: "sc_mp2r12energy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mp2r12energy/"
description: "sc::MP2R12Energy –"
---

<p>sc::MP2R12Energy &#8211; </p>
<p> Class <code>MP2R12Energy</code> is the object that computes and maintains MP2-R12 energies.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mp2r12_energy.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MP2R12Energy</code> (<code>StateIn</code> &amp;) </p>
<p> <code>MP2R12Energy</code> (<code>Ref</code>&lt; <code>R12IntEval</code> &gt; &amp;r12eval, LinearR12::StandardApproximation stdapp, int debug) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>obsolete</code> () </p>
<p> void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Print the object. </i><br />
 void <code>print_pair_energies</code> (bool spinadapted, std::ostream &amp;so=ExEnv::out0()) </p>
<p> <code>Ref</code>&lt; <code>R12IntEval</code> &gt; <code>r12eval</code> () const </p>
<p> LinearR12::StandardApproximation <code>stdapp</code> () const </p>
<p> bool <code>gbc</code> () const<br />
 <i>Returns whether Generalized Brillouin Condition (GBC) was used in evaluation of the MP2-R12 intermediates. </i><br />
 bool <code>ebc</code> () const<br />
 <i>Returns whether Extended Brillouin Condition (EBC) was used in evaluation of the MP2-R12 intermediates and the MP2-R12 energy. </i><br />
 void <code>set_debug</code> (int debug) </p>
<p> int <code>get_debug</code> () const </p>
<p> <code>RefSCDimension</code> <code>dim_aa</code> () const </p>
<p> <code>RefSCDimension</code> <code>dim_ab</code> () const </p>
<p> <code>RefSCDimension</code> <code>dim_s</code> () const </p>
<p> <code>RefSCDimension</code> <code>dim_t</code> () const </p>
<p> void <code>compute</code> ()<br />
 <i>Computes the first-order R12 wave function and MP2-R12 energy. </i><br />
 double <code>compute_pair_function_aa</code> (int ij, const <code>SCVector3</code> &amp;r1, const <code>SCVector3</code> &amp;r2)<br />
 <i>Computes the value of the alpha-alpha pair function ij when electrons 1 and 2 reside at r1 and r2. </i><br />
 double <code>compute_pair_function_ab</code> (int ij, const <code>SCVector3</code> &amp;r1, const <code>SCVector3</code> &amp;r2)<br />
 <i>Computes the value of the alpha-beta pair function ij when electrons 1 and 2 reside at r1 and r2. </i><br />
 void <code>compute_pair_function_aa</code> (int ij, const <code>Ref</code>&lt; <code>TwoBodyGrid</code> &gt; &amp;tbgrid)<br />
 <i>Computes values of the alpha-alpha pair function ij on tbgrid. </i><br />
 void <code>compute_pair_function_ab</code> (int ij, const <code>Ref</code>&lt; <code>TwoBodyGrid</code> &gt; &amp;tbgrid)<br />
 <i>Computes values of the alpha-beta pair function ij on tbgrid. </i><br />
 <code>RefSCVector</code> <code>emp2_aa</code> () const<br />
 <i>Returns the vector of MP2 alpha-alpha pair energies. </i><br />
 <code>RefSCVector</code> <code>emp2_ab</code> () const<br />
 <i>Returns the vector of MP2 alpha-beta pair energies. </i><br />
 <code>RefSCVector</code> <code>er12_aa</code> () const<br />
 <i>Returns the vector of R12 corrections to MP2-R12 alpha-alpha pair energies. </i><br />
 <code>RefSCVector</code> <code>er12_ab</code> () const<br />
 <i>Returns the vector of R12 correction to MP2-R12 alpha-beta pair energies. </i><br />
 <code>RefSCVector</code> <code>emp2r12_aa</code> () const<br />
 <i>Returns the vector of MP2-R12 alpha-alpha pair energies. </i><br />
 <code>RefSCVector</code> <code>emp2r12_ab</code> () const<br />
 <i>Returns the vector of MP2-R12 alpha-beta pair energies. </i><br />
 double <code>energy</code> ()<br />
 <i>Returns total MP2-R12 correlation energy. </i><br />
 <code>RefSCMatrix</code> <code>C_aa</code> ()<br />
 <i>Returns the matrix of amplitudes of alpha-alpha r12-multiplied occupied orbital pairs in the first-order pair function. </i><br />
 <code>RefSCMatrix</code> <code>C_ab</code> ()<br />
 <i>Returns the matrix of amplitudes of alpha-beta r12-multiplied occupied orbital pairs in the first-order pair function. </i><br />
 <code>RefSCMatrix</code> <code>T2_aa</code> ()<br />
 <i>Returns the matrix of amplitudes of alpha-alpha virtuals orbital pairs in the first-order pair function. </i><br />
 <code>RefSCMatrix</code> <code>T2_ab</code> ()<br />
 <i>Returns the matrix of amplitudes of alpha-beta virtuals orbital pairs in the first-order pair function. </i></p>
<h2>Detailed Description</h2>
<p>Class <code>MP2R12Energy</code> is the object that computes and maintains MP2-R12 energies.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MP2R12Energy::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
