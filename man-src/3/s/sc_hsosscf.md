---
title: "sc_hsosscf(3)"
name: "sc_hsosscf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_hsosscf/"
description: "sc::HSOSSCF –"
---

<p>sc::HSOSSCF &#8211; </p>
<p> The <code>HSOSSCF</code> class is a base for classes implementing a self-consistent procedure for high-spin open-shell molecules.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;hsosscf.h&gt;</code></pre>
<p> Inherits <code>sc::SCF</code>. Inherited by <code>sc::HSOSHF</code>, and <code>sc::HSOSKS</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>HSOSSCF (StateIn &amp;)



HSOSSCF (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


double occupation (int irrep, int vectornum)


Returns the occupation.


double alpha_occupation (int irrep, int vectornum)


Returns the alpha occupation.


double beta_occupation (int irrep, int vectornum)


Returns the beta occupation.


int n_fock_matrices () const



RefSymmSCMatrix fock (int i)


Returns closed-shell (i==0) or open-shell (i==1) Fock matrix in AO basis (excluding XC contribution in KS DFT).


RefSymmSCMatrix effective_fock ()


Returns effective Fock matrix in MO basis (including XC contribution for KS DFT).


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


int spin_polarized ()


Return 1 if the alpha density is not equal to the beta density.


RefSymmSCMatrix density ()


Returns the SO density.


RefSymmSCMatrix alpha_density ()


Return alpha electron densities in the SO basis.


RefSymmSCMatrix beta_density ()


Return beta electron densities in the SO basis.



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



void two_body_deriv_hf (double *grad, double exchange_fraction)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>most_recent_pg_</code> </p>
<p> int <code>user_occupations_</code> </p>
<p> int <code>tndocc_</code> </p>
<p> int <code>tnsocc_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int * <code>initial_ndocc_</code> </p>
<p> int * <code>initial_nsocc_</code> </p>
<p> int * <code>ndocc_</code> </p>
<p> int * <code>nsocc_</code> </p>
<p> <code>ResultRefSymmSCMatrix</code> <code>cl_fock_</code> </p>
<p> <code>ResultRefSymmSCMatrix</code> <code>op_fock_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_dens_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_dens_diff_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_gmat_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>op_dens_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>op_dens_diff_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>op_gmat_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_hcore_</code></p>
<h2>Detailed Description</h2>
<p>The <code>HSOSSCF</code> class is a base for classes implementing a self-consistent procedure for high-spin open-shell molecules.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::HSOSSCF::HSOSSCF (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;total_charge&quot; 1c This floating <code>point</code> number gives the total charge, $c$, of the molecule. The default is 0. </p>
<dl>
<dt>nsocc</p>
<dd>This integer gives the total number of singly occupied orbitals, $n_mathrm{socc}$. If this is not given, then multiplicity will be read.</dl>
<dl>
<dt>multiplicity</p>
<dd>This integer gives the multiplicity, $m$, of the molecule. The number of singly occupied orbitals is then $n_mathrm{socc} = m &#8211; 1$. If neither nsocc nor multiplicity is given, then if, in consideration of total_charge, the number of electrons is even, the default $n_mathrm{socc}$ is 2. Otherwise, it is 1.</dl>
<dl>
<dt>ndocc</p>
<dd>This integer gives the total number of doubly occupied orbitals $n_mathrm{docc}$. The default $n_mathrm{docc} = (c &#8211; n_mathrm{socc})/2$.</dl>
<dl>
<dt>socc</p>
<dd>This vector of integers gives the total number of singly occupied orbitals of each irreducible representation. By default, the $n_mathrm{socc}$ singly occupied orbitals will be distributed according to orbital eigenvalues. If socc is given, then docc must be given and they override nsocc, multiplicity, ndocc, and total_charge.</dl>
<dl>
<dt>docc</p>
<dd>This vector of integers gives the total number of doubly occupied orbitals of each irreducible representation. By default, the $n_mathrm{docc}$ singly occupied orbitals will be distributed according to orbital eigenvalues. If docc is given, then socc must be given and they override nsocc, multiplicity, ndocc, and total_charge.</dl>
<dl>
<dt>maxiter</p>
<dd>This has the same meaning as in the parent class, <code>SCF</code>; however, the default value is 100.</dl>
<dl>
<dt>level_shift</p>
<dd>This has the same meaning as in the parent class, <code>SCF</code>; however, the default value is 1.0.</dl>
<h2>Member Function Documentation</h2>
<h3>double sc::HSOSSCF::alpha_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the alpha occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3>double sc::HSOSSCF::beta_occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the beta occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Reimplemented from <code>sc::OneBodyWavefunction</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::HSOSSCF::effective_fock () [virtual]</h3>
<p>Returns effective Fock matrix in MO basis (including XC <code>contribution</code> for KS DFT). </p>
<p> Implements <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::HSOSKS</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::HSOSSCF::fock (int i) [virtual]</h3>
<p>Returns closed-shell (i==0) or open-shell (i==1) Fock matrix in AO basis (excluding XC <code>contribution</code> in KS DFT). Use <code>effective_fock()</code> if you want the full KS Fock matrix. </p>
<p> Implements <code>sc::SCF</code>.</p>
<h3>double sc::HSOSSCF::occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::HSOSSCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::HSOSKS</code>, and <code>sc::HSOSHF</code>.</p>
<h3>void sc::HSOSSCF::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::SCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
