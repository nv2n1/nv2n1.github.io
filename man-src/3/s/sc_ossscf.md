---
title: "sc_ossscf(3)"
name: "sc_ossscf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_ossscf/"
description: "sc::OSSSCF –"
---

<p>sc::OSSSCF &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCF</code>. Inherited by <code>sc::OSSHF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OSSSCF (StateIn &amp;)



OSSSCF (const Ref&lt; KeyVal &gt; &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


double occupation (int ir, int vectornum)


Returns the occupation.


double alpha_occupation (int irrep, int vectornum)


Returns the alpha occupation.


double beta_occupation (int irrep, int vectornum)


Returns the beta occupation.


int n_fock_matrices () const



RefSymmSCMatrix fock (int)



RefSymmSCMatrix effective_fock ()



RefSymmSCMatrix density ()


Returns the SO density.


RefSymmSCMatrix alpha_density ()


Return alpha electron densities in the SO basis.


RefSymmSCMatrix beta_density ()


Return beta electron densities in the SO basis.


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


int spin_polarized ()


Return 1 if the alpha density is not equal to the beta density.



Protected Member Functions
void set_occupations (const RefDiagSCMatrix &amp;evals)



void init_vector ()



void done_vector ()



void reset_density ()



double new_density ()



double scf_energy ()



Ref&lt; SCExtrapData &gt; extrap_data ()



void init_gradient ()



void done_gradient ()



RefSymmSCMatrix lagrangian ()



RefSymmSCMatrix gradient_density ()



void init_hessian ()



void done_hessian ()



Protected Attributes
int user_occupations_



int tndocc_



int nirrep_



int * ndocc_



int osa_



int osb_



ResultRefSymmSCMatrix cl_fock_



ResultRefSymmSCMatrix op_focka_



ResultRefSymmSCMatrix op_fockb_



RefSymmSCMatrix cl_dens_



RefSymmSCMatrix cl_dens_diff_



RefSymmSCMatrix cl_gmat_



RefSymmSCMatrix op_densa_



RefSymmSCMatrix op_densa_diff_



RefSymmSCMatrix op_gmata_



RefSymmSCMatrix op_densb_



RefSymmSCMatrix op_densb_diff_



RefSymmSCMatrix op_gmatb_



RefSymmSCMatrix cl_hcore_</code></pre>
<h2>Member Function Documentation</h2>
<h3>double sc::OSSSCF::alpha_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the alpha occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>double sc::OSSSCF::beta_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the beta occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>double sc::OSSSCF::occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::OSSSCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::OSSHF</code>.</p>
<h3>void sc::OSSSCF::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::SCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
