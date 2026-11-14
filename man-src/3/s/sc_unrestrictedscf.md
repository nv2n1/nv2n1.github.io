---
title: "sc_unrestrictedscf(3)"
name: "sc_unrestrictedscf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_unrestrictedscf/"
description: "sc::UnrestrictedSCF –"
---

<p>sc::UnrestrictedSCF &#8211; </p>
<p> A base class for unrestricted self-consistent-field methods.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;uscf.h&gt;</code></pre>
<p> Inherits <code>sc::SCF</code>. Inherited by <code>sc::UHF</code>, and <code>sc::UKS</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>UnrestrictedSCF (StateIn &amp;)



UnrestrictedSCF (const Ref&lt; KeyVal &gt; &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


RefSCMatrix eigenvectors ()


Deprecated.


RefDiagSCMatrix eigenvalues ()


Returns the MO basis eigenvalues.


RefSCMatrix oso_alpha_eigenvectors ()



RefSCMatrix alpha_eigenvectors ()



RefDiagSCMatrix alpha_eigenvalues ()



RefSCMatrix oso_beta_eigenvectors ()



RefSCMatrix beta_eigenvectors ()



RefDiagSCMatrix beta_eigenvalues ()



RefSymmSCMatrix alpha_density ()


Return alpha electron densities in the SO basis.


RefSymmSCMatrix beta_density ()


Return beta electron densities in the SO basis.


RefSymmSCMatrix density ()


Returns the SO density.


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


double occupation (int, int)


Returns the occupation.


double alpha_occupation (int, int)


Returns the alpha occupation.


double beta_occupation (int, int)


Returns the beta occupation.


int spin_polarized ()


Return 1 if the alpha density is not equal to the beta density.


int spin_unrestricted ()


Return 1 if the alpha orbitals are not equal to the beta orbitals.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


int n_fock_matrices () const



RefSymmSCMatrix fock (int i)


Returns alpha (i==0) or beta (i==1) Fock matrix in AO basis (including XC contribution in KS DFT -- compare this to CLSCF and HSOSSCF!).


RefSymmSCMatrix effective_fock ()


Spin-unrestricted SCF methods do not define effective Fock matrix, thus this function should never be called.


void set_desired_value_accuracy (double eps)


Overload of Function::set_desired_value_accuracy().



Protected Member Functions
Ref&lt; SCExtrapError &gt; extrap_error ()



double compute_vector (double &amp;, double enuclear)



void initial_vector (int needv=1)



void set_occupations (const RefDiagSCMatrix &amp;)



void set_occupations (const RefDiagSCMatrix &amp;, const RefDiagSCMatrix &amp;)



void init_vector ()



void done_vector ()



double new_density ()



void reset_density ()



double scf_energy ()



Ref&lt; SCExtrapData &gt; extrap_data ()



void init_gradient ()



void done_gradient ()



RefSymmSCMatrix lagrangian ()



RefSymmSCMatrix gradient_density ()



void init_hessian ()



void done_hessian ()



void two_body_deriv_hf (double *grad, double exchange_fraction)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>most_recent_pg_</code> </p>
<p> int <code>user_occupations_</code> </p>
<p> int <code>tnalpha_</code> </p>
<p> int <code>tnbeta_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int * <code>nalpha_</code> </p>
<p> int * <code>nbeta_</code> </p>
<p> int * <code>initial_nalpha_</code> </p>
<p> int * <code>initial_nbeta_</code> </p>
<p> <code>AccResultRefSCMatrix</code> <code>oso_eigenvectors_beta_</code> </p>
<p> <code>AccResultRefDiagSCMatrix</code> <code>eigenvalues_beta_</code> </p>
<p> <code>ResultRefSymmSCMatrix</code> <code>focka_</code> </p>
<p> <code>ResultRefSymmSCMatrix</code> <code>fockb_</code> </p>
<p> <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>tbi_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>densa_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>densb_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>gmata_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>gmatb_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>diff_densa_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>diff_densb_</code></p>
<h2>Detailed Description</h2>
<p>A base class for unrestricted self-consistent-field methods.</p>
<h2>Member Function Documentation</h2>
<h3>double sc::UnrestrictedSCF::alpha_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the alpha occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>double sc::UnrestrictedSCF::beta_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the beta occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::UnrestrictedSCF::effective_fock () [virtual]</h3>
<p>Spin-unrestricted <code>SCF</code> methods do not define effective Fock matrix, thus this function should never be called. </p>
<p> Implements <code>sc::SCF</code>.</p>
<h3><code>RefDiagSCMatrix</code> sc::UnrestrictedSCF::eigenvalues () [virtual]</h3>
<p>Returns the MO basis eigenvalues. </p>
<p> Reimplemented from <code>sc::SCF</code>.</p>
<h3><code>RefSCMatrix</code> sc::UnrestrictedSCF::eigenvectors ()</h3>
<p>Deprecated. Use <code>so_to_mo()</code>.t() instead. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::UnrestrictedSCF::fock (int i) [virtual]</h3>
<p>Returns alpha (i==0) or beta (i==1) Fock matrix in AO basis (including XC <code>contribution</code> in KS DFT &#8212; compare this to <code>CLSCF</code> and HSOSSCF!). Argument i must be 0. </p>
<p> Implements <code>sc::SCF</code>.</p>
<h3>double sc::UnrestrictedSCF::occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::UnrestrictedSCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::UKS</code>, and <code>sc::UHF</code>.</p>
<h3>void sc::UnrestrictedSCF::set_desired_value_accuracy (double eps) [virtual]</h3>
<p>Overload of <code>Function::set_desired_value_accuracy()</code>. Must update accuracy of the eigenvalues and eigenvectors. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::UnrestrictedSCF::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::SCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
