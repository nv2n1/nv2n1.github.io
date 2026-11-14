---
title: "sc_extendedhuckelwfn(3)"
name: "sc_extendedhuckelwfn"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_extendedhuckelwfn/"
description: "sc::ExtendedHuckelWfn –"
---

<p>sc::ExtendedHuckelWfn &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::OneBodyWavefunction</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ExtendedHuckelWfn</code> (<code>StateIn</code> &amp;) </p>
<p> <code>ExtendedHuckelWfn</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 double <code>occupation</code> (int irrep, int vectornum)<br />
 <i>Returns the occupation. </i><br />
 <code>RefSCMatrix</code> <code>oso_eigenvectors</code> ()<br />
 <i>Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix. </i><br />
 <code>RefDiagSCMatrix</code> <code>eigenvalues</code> ()<br />
 <i>Returns the MO basis eigenvalues. </i><br />
 <code>RefSymmSCMatrix</code> <code>density</code> ()<br />
 <i>Returns the </i><code>SO</code> density.<br />
 int <code>spin_polarized</code> ()<br />
 <i>Return 1 if the alpha density is not equal to the beta density. </i><br />
 int <code>spin_unrestricted</code> ()<br />
 <i>Return 1 if the alpha orbitals are not equal to the beta orbitals. </i><br />
 int <code>value_implemented</code> () const<br />
 <i>Information about the availability of values, gradients, and hessians. </i></p>
<h2>Member Function Documentation</h2>
<h3><code>RefDiagSCMatrix</code> sc::ExtendedHuckelWfn::eigenvalues () [virtual]</h3>
<p>Returns the MO basis eigenvalues. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>double sc::ExtendedHuckelWfn::occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3><code>RefSCMatrix</code> sc::ExtendedHuckelWfn::oso_eigenvectors () [virtual]</h3>
<p>Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::ExtendedHuckelWfn::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>int sc::ExtendedHuckelWfn::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
