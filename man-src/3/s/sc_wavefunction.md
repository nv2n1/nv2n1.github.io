---
title: "sc_wavefunction(3)"
name: "sc_wavefunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_wavefunction/"
description: "sc::Wavefunction –"
---

<p>sc::Wavefunction &#8211; </p>
<p> A <code>Wavefunction</code> is a <code>MolecularEnergy</code> that utilizies a <code>GaussianBasisSet</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wfn.h&gt;</code></pre>
<p> Inherits <code>sc::MolecularEnergy</code>. Inherited by <code>sc::MBPT2</code>, <code>sc::OneBodyWavefunction</code>, and <code>sc::PsiWavefunction</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Wavefunction (StateIn &amp;)



Wavefunction (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


double density (const SCVector3 &amp;)



double density_gradient (const SCVector3 &amp;, double *)



double natural_orbital (const SCVector3 &amp;r, int iorb)



double natural_orbital_density (const SCVector3 &amp;r, int orb, double *orbval=0)



double orbital (const SCVector3 &amp;r, int iorb, const RefSCMatrix &amp;orbs)



double orbital_density (const SCVector3 &amp;r, int iorb, const RefSCMatrix &amp;orbs, double *orbval=0)



double charge ()


Returns the charge.


virtual int nelectron ()=0


Returns the number of electrons.


virtual RefSymmSCMatrix density ()=0


Returns the SO density.


virtual RefSymmSCMatrix ao_density ()


Returns the AO density.


virtual RefSCMatrix natural_orbitals ()


Returns the natural orbitals.


virtual RefDiagSCMatrix natural_density ()


Returns the natural density (a diagonal matrix).


virtual int spin_polarized ()=0


Return 1 if the alpha density is not equal to the beta density.


virtual RefSymmSCMatrix alpha_density ()


Return alpha electron densities in the SO basis.


virtual RefSymmSCMatrix beta_density ()


Return beta electron densities in the SO basis.


virtual RefSymmSCMatrix alpha_ao_density ()


Return alpha electron densities in the AO basis.


virtual RefSymmSCMatrix beta_ao_density ()


Return beta electron densities in the AO basis.


virtual RefSCMatrix nao (double *atom_charges=0)


returns the ao to nao transformation matrix


virtual RefSymmSCMatrix overlap ()


Returns the SO overlap matrix.


virtual RefSymmSCMatrix core_hamiltonian ()


Returns the SO core Hamiltonian.


virtual double nuclear_repulsion_energy ()


Returns the nuclear repulsion energy.


void nuclear_repulsion_energy_gradient (double *g)


Computes the nuclear repulsion gradient.


virtual void nuclear_repulsion_energy_gradient (double **g)


Computes the nuclear repulsion gradient.


RefSCDimension ao_dimension ()


Atomic orbital dimension.


RefSCDimension so_dimension ()


Symmetry adapted orbital dimension.


RefSCDimension oso_dimension ()


Orthogonalized symmetry adapted orbital dimension.


Ref&lt; SCMatrixKit &gt; basis_matrixkit ()


Matrix kit for AO, SO, orthogonalized SO, and MO dimensioned matrices.


Ref&lt; Molecule &gt; molecule () const


Returns the Molecule.


Ref&lt; GaussianBasisSet &gt; basis () const


Returns the basis set.


Ref&lt; GaussianBasisSet &gt; atom_basis () const


Returns the basis set describing the nuclear charge distributions.


const double * atom_basis_coef () const


Returns the coefficients of the nuclear charge distribution basis functions.


Ref&lt; Integral &gt; integral ()


Returns the integral evaluator.


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


RefSCMatrix so_to_orthog_so ()


Returns a matrix which does the default transform from SO's to orthogonal SO's.


RefSCMatrix so_to_orthog_so_inverse ()


Returns the inverse of the transformation returned by so_to_orthog_so.


OverlapOrthog::OrthogMethod orthog_method () const


Returns the orthogonalization method.


void set_orthog_method (const OverlapOrthog::OrthogMethod &amp;)


(Re)Sets the orthogonalization method and makes this obsolete


double lindep_tol () const


Returns the tolerance for linear dependencies.


void set_lindep_tol (double)


Re(Sets) the tolerance for linear dependencies.


void obsolete ()


Marks all results as being out of date.


void print (std::ostream &amp;=ExEnv::out0()) const


Print information about the object.



Protected Member Functions
double min_orthog_res ()



double max_orthog_res ()



void copy_orthog_info (const Ref&lt; Wavefunction &gt; &amp;)



Protected Attributes
int debug_</code></pre>
<h2>Detailed Description</h2>
<p>A <code>Wavefunction</code> is a <code>MolecularEnergy</code> that utilizies a <code>GaussianBasisSet</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Wavefunction::Wavefunction (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;basis&quot; 1c Specifies a <code>GaussianBasisSet</code> object. There is no default. </p>
<dl>
<dt>integral</p>
<dd>Specifies an <code>Integral</code> object that computes the two electron integrals. The default is a <code>IntegralV3</code> object.</dl>
<dl>
<dt>orthog_method</p>
<dd>This is a string that specifies the orthogonalization method to be used. It can be one one canonical, gramschmidt, or symmetric. The default is symmetric.</dl>
<dl>
<dt>lindep_tol</p>
<dd>The tolerance used to detect linearly dependent basis functions. The precise meaning depends on the orthogonalization method. The default value is 1e-8.</dl>
<dl>
<dt>print_nao</p>
<dd>This specifies a boolean value. If true the natural atomic orbitals will be printed. Not all wavefunction will be able to do this. The default is false.</dl>
<dl>
<dt>print_npa</p>
<dd>This specifies a boolean value. If true the natural population analysis will be printed. Not all wavefunction will be able to do this. The default is true if print_nao is true, otherwise it is false.</dl>
<dl>
<dt>debug</p>
<dd>This integer can be used to produce output for debugging. The default is 0.</dl>
<h2>Member Function Documentation</h2>
<h3>const double* sc::Wavefunction::atom_basis_coef () const</h3>
<p>Returns the coefficients of the nuclear charge distribution basis functions.</p>
<h3>virtual double sc::Wavefunction::nuclear_repulsion_energy () [virtual]</h3>
<p>Returns the nuclear repulsion energy. This must be used instead of <code>Molecule::nuclear_repulsion_energy()</code> since there may be diffuse atomic charges.</p>
<h3>virtual void sc::Wavefunction::nuclear_repulsion_energy_gradient (double ** g) [virtual]</h3>
<p>Computes the nuclear repulsion gradient. This must be used instead of <code>Molecule::nuclear_repulsion_1der()</code> since there may be diffuse atomic charges. The gradient, g, is first zeroed. Its dimensions are g[natom][3].</p>
<h3>void sc::Wavefunction::nuclear_repulsion_energy_gradient (double * g)</h3>
<p>Computes the nuclear repulsion gradient. This must be used instead of <code>Molecule::nuclear_repulsion_1der()</code> since there may be diffuse atomic charges. The gradient, g, is zeroed and set to x_0, y_0, z_0, x_1, &#8230; .</p>
<h3>void sc::Wavefunction::obsolete () [virtual]</h3>
<p>Marks all results as being out of date. Any subsequent access to results will cause <code>Compute::compute()</code> to be called. </p>
<p> Reimplemented from <code>sc::Compute</code>. </p>
<p> Reimplemented in <code>sc::MBPT2</code>, <code>sc::MBPT2_R12</code>, and <code>sc::SCF</code>.</p>
<h3>void sc::Wavefunction::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MolecularEnergy</code>. </p>
<p> Reimplemented in <code>sc::CLKS</code>, <code>sc::HSOSKS</code>, <code>sc::UKS</code>, <code>sc::MBPT2</code>, <code>sc::MBPT2_R12</code>, <code>sc::PsiWavefunction</code>, <code>sc::PsiSCF</code>, <code>sc::PsiCCSD</code>, <code>sc::PsiCCSD_T</code>, <code>sc::CLHF</code>, <code>sc::CLSCF</code>, <code>sc::HSOSHF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSHF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCHF</code>, <code>sc::TCSCF</code>, <code>sc::UHF</code>, <code>sc::UnrestrictedSCF</code>, <code>sc::ExtendedHuckelWfn</code>, <code>sc::OneBodyWavefunction</code>, and <code>sc::HCoreWfn</code>.</p>
<h3><code>RefSCMatrix</code> sc::Wavefunction::so_to_orthog_so ()</h3>
<p>Returns a matrix which does the default transform from SO&#8217;s to orthogonal SO&#8217;s. This could be either the symmetric or canonical orthogonalization matrix. The row dimension is <code>SO</code> and the column dimension is ortho <code>SO</code>. An operator $O$ in the ortho <code>SO</code> basis is given by $X O X^T$ where $X$ is the return value of this function.</p>
<h3>void sc::Wavefunction::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::MolecularEnergy</code>. </p>
<p> Reimplemented in <code>sc::MBPT2</code>, <code>sc::CLSCF</code>, <code>sc::HSOSSCF</code>, <code>sc::OSSSCF</code>, <code>sc::SCF</code>, <code>sc::TCSCF</code>, <code>sc::UnrestrictedSCF</code>, and <code>sc::OneBodyWavefunction</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
