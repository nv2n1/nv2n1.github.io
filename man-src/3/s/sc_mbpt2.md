---
title: "sc_mbpt2(3)"
name: "sc_mbpt2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mbpt2/"
description: "sc::MBPT2 –"
---

<p>sc::MBPT2 &#8211; </p>
<p> The <code>MBPT2</code> class implements several second-order perturbation theory methods.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mbpt.h&gt;</code></pre>
<p> Inherits <code>sc::Wavefunction</code>. Inherited by <code>sc::MBPT2_R12</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MBPT2 (StateIn &amp;)



MBPT2 (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


Ref&lt; SCF &gt; ref ()



double ref_energy ()



double corr_energy ()



RefSCVector ref_energy_gradient ()



RefSCVector corr_energy_gradient ()



int nelectron ()


Returns the number of electrons.


int nfzcore () const



int nfzvirt () const



RefSymmSCMatrix density ()


Returns the SO density.


int spin_polarized ()


Return 1 if the alpha density is not equal to the beta density.


int gradient_implemented () const



int value_implemented () const


Information about the availability of values, gradients, and hessians.


void symmetry_changed ()


Call this if you have changed the molecular symmetry of the molecule contained by this MolecularEnergy.


void obsolete ()


Marks all results as being out of date.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.



Protected Member Functions
void init_variables ()



void compute ()


Recompute at least the results that have compute true and are not already computed.


void eigen (RefDiagSCMatrix &amp;vals, RefSCMatrix &amp;vecs, RefDiagSCMatrix &amp;occs)



void compute_hsos_v1 ()



distsize_t compute_v2_memory (int ni, int nfuncmax, int nbfme, int nshell, int ndocc, int nsocc, int nvir, int nproc)



void compute_hsos_v2 ()



void compute_hsos_v2_lb ()



int compute_cs_batchsize (size_t mem_static, int nocc_act)



distsize_t compute_cs_dynamic_memory (int ni, int nocc_act)



int make_cs_gmat (RefSymmSCMatrix &amp;Gmat, double *DPmat)



int make_cs_gmat_new (RefSymmSCMatrix &amp;Gmat, const RefSymmSCMatrix &amp;DPmat)



void form_max_dens (double *DPmat, signed char *maxp)



int init_cs_gmat ()



void done_cs_gmat ()



int make_g_d_nor (RefSymmSCMatrix &amp;Gmat, double *DPmat, const double *mgdbuff)



void cs_cphf (double **scf_vector, double *Laj, double *eigval, RefSCMatrix &amp;P2aj)



void s2pdm_contrib (const double *intderbuf, double *PHF, double *P2AO, double **hf_ginter, double **ginter)



void hcore_cs_grad (double *PHF, double *PMP2, double **hf_ginter, double **ginter)



void overlap_cs_grad (double *WHF, double *WMP2, double **hf_ginter, double **ginter)



void compute_cs_grad ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCF</code> &gt; <code>reference_</code> </p>
<p> <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; <code>mem</code> </p>
<p> int <code>nfzc</code> </p>
<p> int <code>nfzv</code> </p>
<p> size_t <code>mem_alloc</code> </p>
<p> double <code>cphf_epsilon_</code> </p>
<p> int <code>eliminate_in_gmat_</code> </p>
<p> const double * <code>intbuf_</code> </p>
<p> <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; <code>tbint_</code> </p>
<p> <code>Ref</code>&lt; <code>TwoBodyInt</code> &gt; * <code>tbints_</code> </p>
<p> <code>Ref</code>&lt; <code>TwoBodyDerivInt</code> &gt; * <code>tbintder_</code> </p>
<p> int <code>nbasis</code> </p>
<p> int <code>noso</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>msg_</code> </p>
<p> int <code>nvir</code> </p>
<p> int <code>nocc</code> </p>
<p> int <code>nsocc</code> </p>
<p> <code>Ref</code>&lt; <code>ThreadGrp</code> &gt; <code>thr_</code> </p>
<p> int <code>dynamic_</code> </p>
<p> double <code>print_percent_</code> </p>
<p> int <code>max_norb_</code> </p>
<p> int * <code>symorb_irrep_</code> </p>
<p> int * <code>symorb_num_</code> </p>
<p> char * <code>method_</code> </p>
<p> char * <code>algorithm_</code> </p>
<p> int <code>do_d1_</code> </p>
<p> int <code>do_d2_</code> </p>
<p> int <code>nfuncmax</code> </p>
<p> double <code>hf_energy_</code> </p>
<p> <code>RefSCVector</code> <code>hf_gradient_</code> </p>
<p> double <code>restart_ecorr_</code> </p>
<p> int <code>restart_orbital_v1_</code> </p>
<p> int <code>restart_orbital_memgrp_</code></p>
<h2>Detailed Description</h2>
<p>The <code>MBPT2</code> class implements several second-order perturbation theory methods.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MBPT2::MBPT2 (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;reference&quot; 1c This gives the reference wavefunction. It must be an object of type <code>CLSCF</code> for closed-shell molecules and <code>HSOSSCF</code> for open-shell molecules. The is no default. </p>
<dl>
<dt>nfzc</p>
<dd>The number of frozen core orbitals. The default is 0. If no atoms have an atomic number greater than 30, then the number of orbitals to be frozen can be automatically determined by specifying nfzc = auto.</dl>
<dl>
<dt>nfzv</p>
<dd>The number of frozen virtual orbitals. The default is 0.</dl>
<dl>
<dt>memory</p>
<dd>The amount of memory, in bytes, that each processor may use.</dl>
<dl>
<dt>method</p>
<dd>This gives a string that must take on one of the values below. The default is mp for closed-shell systems and zapt for open-shell systems.</dl>
<dl>
<dt>mp</p>
<dd>Use Moller-Plesset perturbation theory. This is only valid for closed-shell systems. Energies and gradients can be computed with this method.</dl>
<dl>
<dt>opt1</p>
<dd>Use the OPT1 variant of open-shell perturbation theory. Only energies can be computed for open-shell systems.</dl>
<dl>
<dt>opt2</p>
<dd>Use the OPT2 variant of open-shell perturbation theory. Only energies can be computed for open-shell systems.</dl>
<dl>
<dt>zapt</p>
<dd>Use the ZAPT variant of open-shell perturbation theory. Only energies can be computed for open-shell systems.</dl>
<dl>
<dt>algorithm</p>
<dd>This gives a string that must take on one of the values given below. The default is memgrp for closed-shell systems. For open-shell systems v1 is used for a small number of processors and v2 is used otherwise.</dl>
<dl>
<dt>memgrp</p>
<dd>Use the distributed shared memory algorithm (which uses a <code>MemoryGrp</code> object). This is only valid for MP2 energies and gradients.</dl>
<dl>
<dt>v1</p>
<dd>Use algorithm V1. Only energies can be computed. The maximum number of processors that can be utilized is the number of virtual orbitals. This algorithm computes few integrals than the others, but has higher communication requirements.</dl>
<dl>
<dt>v2</p>
<dd>Use algorithm V2. Only energies can be computed. The maximum number of processors that can be utilized is the number of shells.</dl>
<dl>
<dt>v2lb</p>
<dd>Use a modified V2 algorithm that may compute more two electron integrals, but may get better load balance on the $O(n_mathrm{basis}^5)$ part of the calculation. Only energies can be computed. This is recommended only for computations involving large molecules (where the transformation is dominant) on very many processors (approaching the number of shells).</dl>
<p> The v1 and v2 algorithms are discussed in Ida M. B. Nielsen and Edward T. Seidl, J. Comp. Chem. 16, 1301 (1995). The memgrp algorithm is discussed in Ida M. B. Nielsen, Chem. Phys. Lett. 255, 210 (1996). </p>
<dl>
<dt>memorygrp</p>
<dd>A <code>MemoryGrp</code> object is used by the memgrp algorithm. If this is not given the program will try to find an appropriate default.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::MBPT2::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Implements <code>sc::Compute</code>. </p>
<p> Reimplemented in <code>sc::MBPT2_R12</code>.</p>
<h3>void sc::MBPT2::obsolete () [virtual]</h3>
<p>Marks all results as being out of date. Any subsequent access to results will cause <code>Compute::compute()</code> to be called. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>. </p>
<p> Reimplemented in <code>sc::MBPT2_R12</code>.</p>
<h3>void sc::MBPT2::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>. </p>
<p> Reimplemented in <code>sc::MBPT2_R12</code>.</p>
<h3>void sc::MBPT2::symmetry_changed () [virtual]</h3>
<p>Call this if you have changed the molecular symmetry of the molecule contained by this <code>MolecularEnergy</code>. </p>
<p> Reimplemented from <code>sc::Wavefunction</code>.</p>
<h3>int sc::MBPT2::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>. </p>
<p> Reimplemented in <code>sc::MBPT2_R12</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
