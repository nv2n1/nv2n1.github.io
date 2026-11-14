---
title: "sc_clscf(3)"
name: "sc_clscf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_clscf/"
description: "sc::CLSCF –"
---

<p>sc::CLSCF &#8211; </p>
<p> The <code>CLSCF</code> class is a base for classes implementing a self-consistent procedure for closed-shell molecules.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;clscf.h&gt;</code></pre>
<p> Inherits <code>sc::SCF</code>. Inherited by <code>sc::CLHF</code>, and <code>sc::CLKS</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CLSCF (StateIn &amp;)



CLSCF (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor:.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


double occupation (int irrep, int vectornum)


Returns the occupation.


int n_fock_matrices () const



RefSymmSCMatrix fock (int i)


Returns closed-shell Fock matrix in AO basis (excluding XC contribution in KS DFT).


RefSymmSCMatrix effective_fock ()


Returns closed-shell Fock matrix in MO basis (including XC contribution for KS DFT).


RefSymmSCMatrix density ()


Returns the SO density.


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



void two_body_deriv_hf (double *grad, double exchange_fraction)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>PointGroup</code> &gt; <code>most_recent_pg_</code> </p>
<p> int <code>user_occupations_</code> </p>
<p> int <code>tndocc_</code> </p>
<p> int <code>nirrep_</code> </p>
<p> int * <code>initial_ndocc_</code> </p>
<p> int * <code>ndocc_</code> </p>
<p> <code>ResultRefSymmSCMatrix</code> <code>cl_fock_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_dens_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_dens_diff_</code> </p>
<p> <code>RefSymmSCMatrix</code> <code>cl_gmat_</code></p>
<h2>Detailed Description</h2>
<p>The <code>CLSCF</code> class is a base for classes implementing a self-consistent procedure for closed-shell molecules.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::CLSCF::CLSCF (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor:. .IP &quot;total_charge&quot; 1c This floating <code>point</code> number gives the total charge of the molecule. The default is 0. </p>
<dl>
<dt>docc</p>
<dd>This vector of integers gives the total number of doubly occupied orbitals of each irreducible representation. By default, this will be chosen to make the molecule uncharged and the electrons will be distributed among the irreducible representations according to the orbital energies.</dl>
<h2>Member Function Documentation</h2>
<h3><code>RefSymmSCMatrix</code> sc::CLSCF::effective_fock () [virtual]</h3>
<p>Returns closed-shell Fock matrix in MO basis (including XC <code>contribution</code> for KS DFT). </p>
<p> Implements <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::CLKS</code>.</p>
<h3><code>RefSymmSCMatrix</code> sc::CLSCF::fock (int i) [virtual]</h3>
<p>Returns closed-shell Fock matrix in AO basis (excluding XC <code>contribution</code> in KS DFT). Use <code>effective_fock()</code> if you want the full KS Fock matrix. Argument i must be 0. </p>
<p> Implements <code>sc::SCF</code>.</p>
<h3>double sc::CLSCF::occupation (int irrep, int vectornum) [virtual]</h3>
<p>Returns the occupation. The irreducible representation and the vector number within that representation are given as arguments. </p>
<p> Implements <code>sc::OneBodyWavefunction</code>.</p>
<h3>void sc::CLSCF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCF</code>. </p>
<p> Reimplemented in <code>sc::CLKS</code>, and <code>sc::CLHF</code>.</p>
<h3>void sc::CLSCF::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::SCF</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
