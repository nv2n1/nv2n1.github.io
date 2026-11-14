---
title: "sc_mbpt2_r12(3)"
name: "sc_mbpt2_r12"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mbpt2_r12/"
description: "sc::MBPT2_R12 –"
---

<p>sc::MBPT2_R12 &#8211; </p>
<p> The <code>MBPT2_R12</code> class implements several linear R12 second-order perturbation theory methods.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;mbptr12.h&gt;</code></pre>
<p> Inherits <code>sc::MBPT2</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MBPT2_R12 (StateIn &amp;)



MBPT2_R12 (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


Ref&lt; GaussianBasisSet &gt; aux_basis () const



Ref&lt; GaussianBasisSet &gt; vir_basis () const



bool gbc () const



bool ebc () const



LinearR12::ABSMethod abs_method () const



LinearR12::StandardApproximation stdapprox () const



bool spinadapted () const



R12IntEvalInfo::StoreMethod r12ints_method () const



const std::string &amp; r12ints_file () const



double corr_energy ()



double r12_corr_energy ()



RefSymmSCMatrix density ()


Returns the SO density.


void obsolete ()


Marks all results as being out of date.


int gradient_implemented () const



int value_implemented () const


Information about the availability of values, gradients, and hessians.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.



Protected Member Functions</code></pre>
<p> void <code>compute</code> ()<br />
 <i>Recompute at least the results that have compute true and are not already computed. </i></p>
<h2>Detailed Description</h2>
<p>The <code>MBPT2_R12</code> class implements several linear R12 second-order perturbation theory methods.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MBPT2_R12::MBPT2_R12 (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;gbc&quot; 1c This boolean specifies whether Generalized Brillouin Condition (GBC) is assumed to hold. The default is &#8216;true&#8217;. This keyword is only valid if stdapprox=A&#8217;. The effect of setting this keyword to true is rather small &#8212; hence it is not recommended to use this keyword. </p>
<dl>
<dt>ebc</p>
<dd>This boolean specifies whether Extended Brillouin Condition (EBC) is assumed to hold. The default is &#8216;true&#8217;. This keyword is only valid if stdapprox=A&#8217;. The effect of setting this keyword to true is rather small &#8212; hence it is not recommended to use this keyword.</dl>
<dl>
<dt>stdapprox</p>
<dd>This gives a string that must take on one of the values below. The default is A&#8217;.</dl>
<dl>
<dt>A</p>
<dd>Use second order Moller-Plesset perturbation theory with linear R12 terms in standard approximation A (MP2-R12/A). Only energies can be computed with the MP2-R12/A method.</dl>
<dl>
<dt>A&#8217;</p>
<dd>Use second order Moller-Plesset perturbation theory with linear R12 terms in standard approximation A&#8217; (MP2-R12/A&#8217;). This will cause MP2-R12/A energies to be computed also. Only energies can be computed with the MP2-R12/A&#8217; method.</dl>
<dl>
<dt>B</p>
<dd>Use second order Moller-Plesset perturbation theory with linear R12 terms in standard approximation B. This method is not implemented yet.</dl>
<dl>
<dt>spinadapted</p>
<dd>This boolean specifies whether to compute spin-adapted or spin-orbital pair energies. Default is to compute spin-adapted energies.</dl>
<dl>
<dt>aux_basis</p>
<dd>This specifies the auxiliary basis to be used for the resolution of the identity. Default is to use the same basis as for the orbital expansion.</dl>
<dl>
<dt>vir_basis</p>
<dd>This specifies the basis to be used for the virtual orbitals. Default is to use the same basis as for the orbital expansion.</dl>
<dl>
<dt>include_mp1</p>
<dd>This specifies whether to compute MP1 correction to the MP2 and MP2-R12 energies. This option only has effect if vir_basis is not the same as basis. MP1 correction is a perturbative estimate of the difference between the HF energy computed in vir_basis and basis. Usually, it is a very poor estimate &#8212; therefore this keyword should be avoided by non-experts. Default is false.</dl>
<dl>
<dt>abs_method</p>
<dd>This string specifies whether the old ABS method, introduced by Klopper and Samson, or the new ABS variant, CABS, introduced by Valeev, should be used. Valid values are &#8216;ABS&#8217; (Klopper and Samson), &#8216;ABS+&#8217;, &#8216;CABS&#8217;, and &#8216;CABS+&#8217;, where the &#8216;+&#8217; labels a method where the union of OBS and ABS is used to construct the RI basis. The default is &#8216;ABS&#8217;. The default in 2.3.0 and later will be &#8216;CABS+&#8217;.</dl>
<dl>
<dt>lindep_tol</p>
<dd>The tolerance used to detect linearly dependent basis functions in the RI basis set. The precise meaning depends on the orthogonalization method. The default value is 1e-8.</dl>
<dl>
<dt>r12ints</p>
<dd>This specifies how to store transformed MO integrals. Valid values are:</dl>
<dl>
<dt>mem-posix</p>
<dd>Store integrals in memory for single-pass situations and in a binary file on task 0&#8217;s node using POSIX I/O for multipass situations. posix is usually less efficient than mpi for distributed parallel multipass runs since the I/O is performed by one task only. However, this method is guaranteed to work in all types of environments, hence mem-posix is the default.</dl>
<dl>
<dt>posix</p>
<dd>Store integrals in a binary file on task 0&#8217;s node using POSIX I/O. This method is different from mem-posix in that it forces the integrals out to disk even if they could be stored in memory. posix should only be used for benchmarking and testing purposes.</dl>
<dl>
<dt>mem-mpi</p>
<dd>Store integrals in memory for single-pass situations and in a binary file using MPI-I/O for multipass situations. This method assumes the availability of MPI-I/O. mem-mpi is the preferred choice in distributed environments which have MPI-I/O available.</dl>
<dl>
<dt>mpi</p>
<dd>Store integrals in a binary file using MPI-I/O. This method is different from mem-mpi in that it forces the integrals out to disk even if they could be stored in memory. mpi should only be used for benchmarking and testing purposes.</dl>
<dl>
<dt>mem</p>
<dd>Store integrals in memory. Can only be used with single-pass transformations for MP2-R12/A and MP2-R12/A&#8217; methods. This method should only be used for testing purposes.</dl>
<p> If r12ints is not specified, then mem-posix method will be used. If user wishes to use MPI-I/O, pending its availability, for higher parallel efficiency, r12ints should be explicitly set to mem-mpi. </p>
<dl>
<dt>r12ints_file</p>
<dd>This specifies the prefix for the transformed MO integrals file if r12ints is set to posix, mpi, mem-posix or mem-mpi is used. Default is &#8216;./&lt;i&gt;inputbasename&lt;/i&gt;.r12ints&#8217;, where <i>inputbasename</i> is the name of the input file without &#8216;.in&#8217;. If MPI-I/O is used then it is user&#8217;s responsibility to ensure that the file resides on a file system that supports MPI-I/O.</dl>
<dl>
<dt>twopdm_grid_aa</p>
<dd>This optional keyword specifies a <code>TwoBodyGrid</code> object which to use for coordinates at which to compute alpha-alpha part of 2-PDM.</dl>
<dl>
<dt>twopdm_grid_ab</p>
<dd>This optional keyword specifies a <code>TwoBodyGrid</code> object which to use for coordinates at which to compute alpha-beta part of 2-PDM.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::MBPT2_R12::compute () [protected, virtual]</h3>
<p>Recompute at least the results that have compute true and are not already computed. This should only be called by Result&#8217;s members. </p>
<p> Reimplemented from <code>sc::MBPT2</code>.</p>
<h3>void sc::MBPT2_R12::obsolete () [virtual]</h3>
<p>Marks all results as being out of date. Any subsequent access to results will cause <code>Compute::compute()</code> to be called. </p>
<p> Reimplemented from <code>sc::MBPT2</code>.</p>
<h3>void sc::MBPT2_R12::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::MBPT2</code>.</p>
<h3>int sc::MBPT2_R12::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::MBPT2</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
