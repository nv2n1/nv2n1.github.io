---
title: "sc_onebodywavefunction(3)"
name: "sc_onebodywavefunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodywavefunction/"
description: "sc::OneBodyWavefunction –"
---

<p>sc::OneBodyWavefunction &#8211; </p>
<p> A <code>OneBodyWavefunction</code> is a <code>MolecularEnergy</code> that solves an effective one-body problem.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obwfn.h&gt;</code></pre>
<p> Inherits <code>sc::Wavefunction</code>. Inherited by <code>sc::ExtendedHuckelWfn</code>, <code>sc::HCoreWfn</code>, and <code>sc::SCF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OneBodyWavefunction (StateIn &amp;)



OneBodyWavefunction (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int nelectron ()


Returns the number of electrons.


void set_desired_value_accuracy (double eps)


Overload of Function::set_desired_value_accuracy().


RefSCMatrix so_to_mo ()


These members give metrics and basis transformations using the covariant/contravariant tensor notation.


RefSCMatrix orthog_so_to_mo ()


Returns the orthogonal-SO to MO transformation matrix.


RefSCMatrix mo_to_so ()


Returns the MO to SO transformation matrix.


RefSCMatrix mo_to_orthog_so ()


Returns the MO to orthogonal-SO transformation matrix.


RefSCMatrix eigenvectors ()


Deprecated.


virtual RefSCMatrix oso_eigenvectors ()=0


Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix.


virtual RefDiagSCMatrix eigenvalues ()=0


Returns the MO basis eigenvalues.


virtual double occupation (int irrep, int vectornum)=0


Returns the occupation.


double occupation (int vectornum)


Returns the occupation.


virtual int spin_unrestricted ()=0


Return 1 if the alpha orbitals are not equal to the beta orbitals.


virtual double alpha_occupation (int irrep, int vectornum)


Returns the alpha occupation.


virtual double beta_occupation (int irrep, int vectornum)


Returns the beta occupation.


double alpha_occupation (int vectornum)


Returns the alpha occupation.


double beta_occupation (int vectornum)


Returns the beta occupation.


virtual RefSCMatrix oso_alpha_eigenvectors ()



virtual RefSCMatrix oso_beta_eigenvectors ()



virtual RefSCMatrix alpha_eigenvectors ()



virtual RefSCMatrix beta_eigenvectors ()



virtual RefDiagSCMatrix alpha_eigenvalues ()



virtual RefDiagSCMatrix beta_eigenvalues ()



virtual RefDiagSCMatrix projected_eigenvalues (const Ref&lt; OneBodyWavefunction &gt; &amp;, int alp=1)



virtual RefSCMatrix projected_eigenvectors (const Ref&lt; OneBodyWavefunction &gt; &amp;, int alp=1)


Projects the density into the current basis set.


virtual RefSCMatrix hcore_guess ()


Return a guess vector.


virtual RefSCMatrix hcore_guess (RefDiagSCMatrix &amp;val)


Return a guess vector and the eigenvalues.


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


double orbital (const SCVector3 &amp;r, int iorb)



double orbital_density (const SCVector3 &amp;r, int iorb, double *orbval=0)



void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.



Protected Member Functions
void init_sym_info ()



int form_occupations (int *&amp;newocc, const int *oldocc)



Protected Attributes</code></pre>
<p> <code>ResultRefSymmSCMatrix</code> <code>density_</code> </p>
<p> <code>AccResultRefSCMatrix</code> <code>oso_eigenvectors_</code> </p>
<p> <code>AccResultRefDiagSCMatrix</code> <code>eigenvalues_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int * <code>nvecperirrep_</code> </p>
<p> double * <code>occupations_</code> </p>
<p> double * <code>alpha_occupations_</code> </p>
<p> double * <code>beta_occupations_</code></p>
<h2>Detailed Description</h2>
<p>A <code>OneBodyWavefunction</code> is a <code>MolecularEnergy</code> that solves an effective one-body problem.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::OneBodyWavefunction::OneBodyWavefunction (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;eigenvector_accuracy&quot; 1c Gives the accuracy to which eigenvectors are initially computed. The default 1.0e-7. Accuracies are usually adjusted as needed anyway, so it should not be necessary to change this.</p>
<h2>Member Function Documentation</h2>
<h3>double sc::OneBodyWavefunction::alpha_occupation (int vectornum)</h3>
<p>Returns the alpha occupation. The vector number in the MO basis is given as an argument.</p>
<h3>virtual double sc::OneBodyWavefunction::alpha_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the alpha occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented in <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::TCSCF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h3>double sc::OneBodyWavefunction::beta_occupation (int vectornum)</h3>
<p>Returns the beta occupation. The vector number in the MO basis is given as an argument.</p>
<h3>virtual double sc::OneBodyWavefunction::beta_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the beta occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented in <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::TCSCF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h3>virtual <code>RefDiagSCMatrix</code> sc::OneBodyWavefunction::eigenvalues () [pure virtual]</h3>
<p>Returns the MO basis eigenvalues. </p>
<p> Implemented in <code>sc::SCF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, and <code>sc::HCoreWfn</code>.</p>
<h3><code>RefSCMatrix</code> sc::OneBodyWavefunction::eigenvectors ()</h3>
<p>Deprecated. Use <code>so_to_mo()</code>.t() instead. </p>
<p> Reimplemented in <code>sc::UnrestrictedSCF</code>.</p>
<h3>virtual <code>RefSCMatrix</code> sc::OneBodyWavefunction::hcore_guess (<code>RefDiagSCMatrix</code> &amp; val) [virtual]</h3>
<p>Return a guess vector and the eigenvalues. The guess ransforms the orthogonal <code>SO</code> basis to the MO basis. Storage for the eigenvalues will be allocated.</p>
<h3>virtual <code>RefSCMatrix</code> sc::OneBodyWavefunction::hcore_guess () [virtual]</h3>
<p>Return a guess vector. The guess transforms the orthogonal <code>SO</code> basis to the MO basis.</p>
<h3><code>RefSCMatrix</code> sc::OneBodyWavefunction::mo_to_orthog_so ()</h3>
<p>Returns the MO to orthogonal-SO transformation matrix. This returns the same matrix as <code>oso_eigenvectors()</code>.</p>
<h3>double sc::OneBodyWavefunction::occupation (int vectornum)</h3>
<p>Returns the occupation. The vector number in the MO basis is given as an argument.</p>
<h3>virtual double sc::OneBodyWavefunction::occupation (int irrep, int vectornum) [pure virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implemented in <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::TCSCF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, and <code>sc::HCoreWfn</code>.</p>
<h3>virtual <code>RefSCMatrix</code> sc::OneBodyWavefunction::oso_eigenvectors () [pure virtual]</h3>
<p>Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix. </p>
<p> Implemented in <code>sc::SCF</code>, <code>sc::ExtendedHuckelWfn</code>, and <code>sc::HCoreWfn</code>.</p>
<h3>virtual <code>RefSCMatrix</code> sc::OneBodyWavefunction::projected_eigenvectors (const <code>Ref</code>&lt; <code>OneBodyWavefunction</code> &gt; &amp;, int alp = 1) [virtual]</h3>
<p>Projects the density into the current basis set. Returns an orthogonalized <code>SO</code> to MO transformation with the orbitals.</p>
<h3>void sc::OneBodyWavefunction::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>. </p>
<p> Reimplemented in <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, and <code>sc::HCoreWfn</code>.</p>
<h3>void sc::OneBodyWavefunction::set_desired_value_accuracy (double eps) [virtual]</h3>
<p>Overload of <code>Function::set_desired_value_accuracy()</code>. Must update accuracy of the eigenvectors and the eigenvalues </p>
<p> Reimplemented from <code>sc::Function</code>. </p>
<p> Reimplemented in <code>sc::UnrestrictedSCF</code>.</p>
<h3><code>RefSCMatrix</code> sc::OneBodyWavefunction::so_to_mo ()</h3>
<p>These members give metrics and basis transformations using the covariant/contravariant tensor notation. Returns the transformation matrix that converts a contravariant <code>SO</code> tensor index to a contravariant MO tensor index. Returns the transformation matrix that converts a covariant <code>SO</code> tensor index to a covariant MO tensor index. Returns the transformation matrix that converts a contravariant MO tensor index to a contravariant <code>SO</code> tensor index. Returns the transformation matrix that converts a covariant MO tensor index to a covariant <code>SO</code> tensor index. Returns the metric for converting a covariant <code>SO</code> index into a contravariant one. Returns the metric for converting a contravariant <code>SO</code> index into a covariant one. Returns the <code>SO</code> to MO transformation matrix.</p>
<h3>void sc::OneBodyWavefunction::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>. </p>
<p> Reimplemented in <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCSCF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
