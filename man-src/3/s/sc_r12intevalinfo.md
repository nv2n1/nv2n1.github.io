---
title: "sc_r12intevalinfo(3)"
name: "sc_r12intevalinfo"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intevalinfo/"
description: "sc::R12IntEvalInfo –"
---

<p>sc::R12IntEvalInfo &#8211; </p>
<p> Class <code>R12IntEvalInfo</code> contains information necessary for R12 intermediate evaluators.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;vxb_eval_info.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<p>enum StoreMethod { mem_posix =  0, posix =  1, mem_mpi =  2, mpi =  3, mem_only =  4 }</p>
<p>Describes the method of storing transformed MO integrals. See MBPT2_R12.</p>
<p>Public Member Functions<br />
 <code>R12IntEvalInfo</code> (<code>StateIn</code> &amp;) </p>
<p> <code>R12IntEvalInfo</code> (<code>MBPT2_R12</code> *)<br />
 <i>Constructs an </i><code>R12IntEvalInfo</code> object using data from the <code>MBPT2_R12</code> object.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>set_dynamic</code> (bool dynamic)<br />
 <i>Sets whether to use dynamic load balancing in parallel MO transformations. </i><br />
 void <code>set_print_percent</code> (double print_percent)<br />
 <i>Sets how frequently updates of progress are printed out. Default is 10%. </i><br />
 void <code>set_debug_level</code> (int debug)<br />
 <i>Set debug level. Default is 0. </i><br />
 void <code>set_ints_method</code> (const <code>StoreMethod</code> method)<br />
 <i>Sets the method of storing transformed MO integrals. </i><br />
 void <code>set_ints_file</code> (const std::string &amp;filename)<br />
 <i>Sets name of the file used to store transformed integrals. </i><br />
 void <code>set_memory</code> (const size_t nbytes)<br />
 <i>Sets the amount of memory to use for the calculation. </i><br />
 void <code>set_absmethod</code> (LinearR12::ABSMethod abs_method)<br />
 <i>Sets the ABS approach to be used (ABS or CABS). </i><br />
 <code>Wavefunction</code> * <code>wfn</code> () const </p>
<p> <code>Ref</code>&lt; <code>SCF</code> &gt; <code>ref</code> () const </p>
<p> <code>Ref</code>&lt; <code>Integral</code> &gt; <code>integral</code> () const </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () const<br />
 <i>Returns the orbital basis set (OBS) object. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis_vir</code> () const<br />
 <i>Returns the virtuals basis set (VBS) object. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis_ri</code> () const<br />
 <i>Returns the resolution-of-the-identity basis set (RIBS) object. </i><br />
 <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit</code> () const </p>
<p> <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; <code>mem</code> () const </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>msg</code> () const </p>
<p> <code>Ref</code>&lt; <code>ThreadGrp</code> &gt; <code>thr</code> () const </p>
<p> bool <code>dynamic</code> () const </p>
<p> double <code>print_percent</code> () const </p>
<p> int <code>debug_level</code> () const </p>
<p> const <code>StoreMethod</code> <code>ints_method</code> () const </p>
<p> const std::string &amp; <code>ints_file</code> () const </p>
<p> const size_t <code>memory</code> () const </p>
<p> const int <code>nocc</code> () const </p>
<p> const int <code>nocc_act</code> () const </p>
<p> const int <code>nfzc</code> () const </p>
<p> const int <code>nvir</code> () const </p>
<p> const int <code>nvir_act</code> () const </p>
<p> const int <code>nfzv</code> () const </p>
<p> LinearR12::ABSMethod <code>abs_method</code> () const </p>
<p> <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>mo_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for symmetry-blocked MOs in OBS.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>obs_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for energy-sorted MOs in OBS.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>act_occ_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for the active occupied MOs.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>act_vir_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for the active unoccupied MOs.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>occ_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for all occupied MOs sorted by energy.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>occ_space_symblk</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for all occupied MOs symmetry-blocked.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>vir_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for all unoccupied MOs ordered by energy.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>vir_space_symblk</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for all unoccupied MOs ordered by symmetry.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>abs_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for ABS.<br />
 <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; <code>ribs_space</code> () const<br />
 <i>Returns the </i><code>MOIndexSpace</code> object for RI-BS.<br />
 <code>Ref</code>&lt; <code>MOIntsTransformFactory</code> &gt; <code>tfactory</code> () const<br />
 <i>Returns the </i><code>MOIntsTransformFactory</code> object.</p>
<h3>Static Public Member Functions</h3>
<pre><code>static Ref&lt; MOIndexSpace &gt; orthog_comp (const Ref&lt; MOIndexSpace &gt; &amp;space1, const Ref&lt; MOIndexSpace &gt; &amp;space2, const std::string &amp;name, double lindep_tol)


Compute subspace of space2 which is orthogonal complement to space1.


static Ref&lt; MOIndexSpace &gt; orthogonalize (const std::string &amp;name, const Ref&lt; GaussianBasisSet &gt; &amp;bs, const Ref&lt; Integral &gt; &amp;integral, OverlapOrthog::OrthogMethod orthog_method, double lindep_tol, int &amp;nlindep)


Compute span of bs and create corresponding mospace referred to by name.


static Ref&lt; MOIndexSpace &gt; gen_project (const Ref&lt; MOIndexSpace &gt; &amp;space1, const Ref&lt; MOIndexSpace &gt; &amp;space2, const std::string &amp;name, double lindep_tol)


Project space1 on space2.


static void compute_overlap_ints (const Ref&lt; MOIndexSpace &gt; &amp;space1, const Ref&lt; MOIndexSpace &gt; &amp;space2, RefSCMatrix &amp;S)


Compute overlap matrices in the basis of space1 and space2.


static void compute_multipole_ints (const Ref&lt; MOIndexSpace &gt; &amp;space1, const Ref&lt; MOIndexSpace &gt; &amp;space2, RefSCMatrix &amp;MX, RefSCMatrix &amp;MY, RefSCMatrix &amp;MZ, RefSCMatrix &amp;MXX, RefSCMatrix &amp;MYY, RefSCMatrix &amp;MZZ)


Compute electric dipole and quadrupole moment matrices in the basis of space1 and space2.</code></pre>
<h2>Detailed Description</h2>
<p>Class <code>R12IntEvalInfo</code> contains information necessary for R12 intermediate evaluators.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>Ref</code>&lt;<code>MOIndexSpace</code>&gt; sc::R12IntEvalInfo::gen_project (const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp; space1, const <code>Ref</code>&lt; <code>MOIndexSpace</code> &gt; &amp; space2, const std::string &amp; name, double lindep_tol) [static]</h3>
<p>Project space1 on space2. This routine computes X2 such that C1.S12.X2 = I, where I is identity matrix and X2 spans subspace of space2. X2 is returned.</p>
<h3>static <code>Ref</code>&lt;<code>MOIndexSpace</code>&gt; sc::R12IntEvalInfo::orthogonalize (const std::string &amp; name, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; bs, const <code>Ref</code>&lt; <code>Integral</code> &gt; &amp; integral, <code>OverlapOrthog::OrthogMethod</code> orthog_method, double lindep_tol, int &amp; nlindep) [static]</h3>
<p><code>Compute</code> span of bs and create corresponding mospace referred to by name. Number linear dependencies is returned in nlindep</p>
<h3>void sc::R12IntEvalInfo::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>void sc::R12IntEvalInfo::set_absmethod (LinearR12::ABSMethod abs_method)</h3>
<p>Sets the ABS approach to be used (ABS or CABS). Default depends on how the object was constructed.</p>
<h3>void sc::R12IntEvalInfo::set_dynamic (bool dynamic) [inline]</h3>
<p>Sets whether to use dynamic load balancing in parallel MO transformations. Default is no</p>
<h3>void sc::R12IntEvalInfo::set_ints_file (const std::string &amp; filename) [inline]</h3>
<p>Sets name of the file used to store transformed integrals. Default depends on how the object was constructed.</p>
<h3>void sc::R12IntEvalInfo::set_ints_method (const <code>StoreMethod</code> method) [inline]</h3>
<p>Sets the method of storing transformed MO integrals. Default depends on how the object was constructed.</p>
<h3>void sc::R12IntEvalInfo::set_memory (const size_t nbytes)</h3>
<p>Sets the amount of memory to use for the calculation. Default is determined by DEFAULT_SC_MEMORY.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
