---
title: "sc_scf(3)"
name: "sc_scf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scf/"
description: "sc::SCF –"
---

<p>sc::SCF &#8211; </p>
<p> The <code>SCF</code> class is the base for all classes that use a self-consistent field procedure to solve an effective one body problem.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scf.h&gt;</code></pre>
<p> Inherits <code>sc::OneBodyWavefunction</code>. Inherited by <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::TCSCF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h3>Public Member Functions</h3>
<p>SCF (StateIn &amp;)</p>
<p>SCF (const Ref&lt; KeyVal &gt; &amp;)</p>
<p>The KeyVal constructor.</p>
<p>void save_data_state (StateOut &amp;)</p>
<p>Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.</p>
<p>RefSCMatrix oso_eigenvectors ()</p>
<p>Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix.</p>
<p>RefDiagSCMatrix eigenvalues ()</p>
<p>Returns the MO basis eigenvalues.</p>
<p>int spin_unrestricted ()</p>
<p>Return 1 if the alpha orbitals are not equal to the beta orbitals.</p>
<p>virtual int n_fock_matrices () const =0</p>
<p>virtual RefSymmSCMatrix fock (int)=0</p>
<p>virtual RefSymmSCMatrix effective_fock ()=0</p>
<p>virtual double one_body_energy ()</p>
<p>virtual void two_body_energy (double &amp;ec, double &amp;ex)</p>
<p>void symmetry_changed ()</p>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.</p>
<p>void obsolete ()</p>
<p>Marks all results as being out of date.</p>
<p>void print (std::ostream &amp;o=ExEnv::out0()) const</p>
<p>Print information about the object.</p>
<p>Protected Types<br />
 enum <code>Access</code> { <code>Read</code>, <code>Write</code>, <code>Accum</code> }</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual void init_threads ()



virtual void done_threads ()



virtual void compute ()


Recompute at least the results that have compute true and are not already computed.


virtual double compute_vector (double &amp;, double enuclear)



virtual Ref&lt; SCExtrapError &gt; extrap_error ()



virtual void compute_gradient (const RefSCVector &amp;)



virtual void compute_hessian (const RefSymmSCMatrix &amp;)



virtual void savestate_iter (int)



virtual void savestate_to_file (const std::string &amp;filename)



signed char * init_pmax (double *)



RefSymmSCMatrix get_local_data (const RefSymmSCMatrix &amp;, double *&amp;, Access)



virtual void initial_vector (int needv=1)



void init_mem (int)



void so_density (const RefSymmSCMatrix &amp;d, double occ, int alp=1)



int * read_occ (const Ref&lt; KeyVal &gt; &amp;, const char *name, int nirrep)



virtual void set_occupations (const RefDiagSCMatrix &amp;)=0



virtual void init_vector ()=0



virtual void done_vector ()=0



virtual double new_density ()=0



virtual void reset_density ()=0



virtual double scf_energy ()=0



virtual Ref&lt; SCExtrapData &gt; extrap_data ()=0



virtual void ao_fock (double accuracy)=0



virtual void init_gradient ()=0



virtual void done_gradient ()=0



virtual RefSymmSCMatrix lagrangian ()=0



virtual RefSymmSCMatrix gradient_density ()=0



virtual void two_body_deriv (double *)=0



virtual void init_hessian ()=0



virtual void done_hessian ()=0



Protected Attributes
int need_vec_



int compute_guess_



int keep_guess_wfn_



Ref&lt; OneBodyWavefunction &gt; guess_wfn_



int always_use_guess_wfn_



Ref&lt; SelfConsistentExtrapolation &gt; extrap_



Ref&lt; AccumH &gt; accumdih_



Ref&lt; AccumH &gt; accumddh_



int maxiter_



int dens_reset_freq_



int reset_occ_



int local_dens_



size_t storage_



int print_all_evals_



int print_occ_evals_



double level_shift_



Ref&lt; MessageGrp &gt; scf_grp_



Ref&lt; ThreadGrp &gt; threadgrp_



int local_



Ref&lt; TwoBodyInt &gt; * tbis_



std::string previous_savestate_file_



RefSCMatrix oso_scf_vector_



RefSCMatrix oso_scf_vector_beta_



RefSymmSCMatrix hcore_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCF</code> class is the base for all classes that use a self-consistent field procedure to solve an effective one body problem.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SCF::SCF (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;maxiter&quot; 1c This integer specifies the maximum number of <code>SCF</code> iterations. The default is 40. </p>
<dl>
<dt>density_reset_frequency</p>
<dd>This integer specifies how often, in term of <code>SCF</code> iterations, $Delta D$ will be reset to $D$. The default is 10.</dl>
<dl>
<dt>reset_occuptions</p>
<dd>Reassign the occupations after each iteration based on the eigenvalues. This only has an effect for molecules with higher than $C_1$ symmetry. The default is false.</dl>
<dl>
<dt>level_shift</p>
<dd>The default is 0.</dl>
<dl>
<dt>extrap</p>
<dd>This specifies an object of type <code>SelfConsistentExtrapolation</code>. The default is a <code>DIIS</code> object.</dl>
<dl>
<dt>memory</p>
<dd>The amount of memory that each processor may use. The default is 0 (minimal memory use).</dl>
<dl>
<dt>local_density</p>
<dd>If this is true, a local copy of the density and $G$ matrix will be made on all nodes, even if a distributed matrix specialization is used. The default is true.</dl>
<dl>
<dt>guess_wavefunction</p>
<dd>This specifies the initial guess for the solution to the <code>SCF</code> equations. This can be either a <code>OneBodyWavefunction</code> object or the name of file that contains the saved state of a <code>OneBodyWavefunction</code> object. By default the one-electron hamiltonian will be diagonalized to obtain the initial guess.</dl>
<dl>
<dt>keep_guess_wavefunction</p>
<dd>The guess wavefunction is normally discarded after it is projected. Setting this boolean variable to true will cause the guess to be kept. This is useful when doing frequencies of symmetric molecules by finite displacements, because the wavefunction is lost whenever the molecule is displaced into lower symmetry.</dl>
<dl>
<dt>always_use_guess_wavefunction</p>
<dd>If the orbitals must be recomputed after they have already been computed once, then the old orbitals are used as the initial guess by default. However, if this option is true, then the guess wavefunction will be used, if available. If a guess wavefunction is not available, then a core Hamiltonian guess will be used. If this option is set to true, then keep_guess_wavefunction should also be set to true.</dl>
<dl>
<dt>print_evals</p>
<dd>Takes a boolean value. If true, print all eigenvalues after the <code>SCF</code> procedure converges. Takes a boolean value. The default is false.</dl>
<dl>
<dt>print_occ_evals</p>
<dd>Takes a boolean value. If true, print the occupied eigenvalues after the <code>SCF</code> procedure converges. The default is false.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SCF::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>.</p>
<h3><code>RefDiagSCMatrix</code> sc::SCF::eigenvalues () [virtual]</h3>
<p>Returns the MO basis eigenvalues. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>. </p>
<p> Reimplemented in <code>sc::UnrestrictedSCF</code>.</p>
<h3>void sc::SCF::obsolete () [virtual]</h3>
<p>Marks all results as being out of date. Any subsequent access to results will cause <code>Compute::compute()</code> to be called. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>.</p>
<h3><code>RefSCMatrix</code> sc::SCF::oso_eigenvectors () [virtual]</h3>
<p>Returns the orthogonal MO (columns) to orthogonal-SO (rows) transformation matrix. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::SCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>. </p>
<p> Reimplemented in <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h3>void sc::SCF::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>. </p>
<p> Reimplemented in <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::TCSCF</code>, and <code>sc::UnrestrictedSCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
