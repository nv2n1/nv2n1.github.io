---
title: "sc_int1ev3(3)"
name: "sc_int1ev3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int1ev3/"
description: "sc::Int1eV3 –"
---

<p>sc::Int1eV3 &#8211; </p>
<p> <code>Int1eV3</code> is a class wrapper for the one body part of the C language IntV3 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;int1e.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Int1eV3</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, int order) </p>
<p> double * <code>buffer</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis1</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis2</code> () </p>
<p> void <code>kinetic</code> (int ish, int jsh) </p>
<p> void <code>nuclear_slow</code> (int ish, int jsh) </p>
<p> void <code>nuclear</code> (int ish, int jsh) </p>
<p> void <code>overlap</code> (int ish, int jsh) </p>
<p> void <code>hcore</code> (int ish, int jsh) </p>
<p> void <code>efield</code> (int ish, int jsh, double position[3]) </p>
<p> void <code>point_charge</code> (int ish, int jsh, int ncharge, const double *charge, const double *const *position) </p>
<p> void <code>dipole</code> (int ish, int jsh, double *com) </p>
<p> void <code>hcore_1der</code> (int ish, int jsh, int dercs, int centernum) </p>
<p> void <code>kinetic_1der</code> (int ish, int jsh, int dercs, int centernum) </p>
<p> void <code>nuclear_1der</code> (int ish, int jsh, int dercs, int centernum) </p>
<p> void <code>overlap_1der</code> (int ish, int jsh, int dercs, int centernum)</p>
<h3>Protected Member Functions</h3>
<pre><code>void accum_shell_1der (double *buff, int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum, double(Int1eV3::*)(int, int, int, int, int, int, int, int))



void accum_shell_block_1der (double *buff, int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum, void(Int1eV3::*shell_block_function)(int gc1, int a, int gc2, int b, int gcsize2, int gcoff1, int gcoff2, double coef, double *buffer))



double comp_shell_overlap (int gc1, int i1, int j1, int k1, int gc2, int i2, int j2, int k2)



double comp_prim_overlap (int i1, int j1, int k1, int i2, int j2, int k2)



double comp_shell_kinetic (int gc1, int i1, int j1, int k1, int gc2, int i2, int j2, int k2)



double comp_prim_kinetic (int i1, int j1, int k1, int i2, int j2, int k2)



double comp_shell_nuclear (int gc1, int i1, int j1, int k1, int gc2, int i2, int j2, int k2)



void accum_shell_efield (double *buff, int ish, int jsh)



void accum_shell_block_efield (double *buff, int ish, int jsh)



double comp_prim_nuclear (int i1, int j1, int k1, int i2, int j2, int k2, int m)



void comp_shell_efield (double *efield, int gc1, int i1, int j1, int k1, int gc2, int i2, int j2, int k2)



void comp_shell_block_efield (int gc1, int a, int gc2, int b, int gcsize2, int gcoff1, int gcoff2, double coef, double *buffer)



double comp_prim_efield (int xyz, int i1, int j1, int k1, int i2, int j2, int k2, int m)



void comp_shell_dipole (double *dipole, int gc1, int i1, int j1, int k1, int gc2, int i2, int j2, int k2)



double comp_prim_dipole (int axis, int i1, int j1, int k1, int i2, int j2, int k2)



void comp_shell_block_nuclear (int gc1, int a, int gc2, int b, int gcsize2, int gcoff1, int gcoff2, double coef, double *buffer)



void comp_prim_block_nuclear (int a, int b)



void comp_prim_block_nuclear_build_a (int a, int b, int m)



void comp_prim_block_nuclear_build_b (int b, int m)



void comp_prim_block_efield (int a, int b)



void comp_prim_block_efield_build_a (int a, int b, int m)



void comp_prim_block_efield_build_b (int b, int m)



void int_accum_shell_overlap_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_done_1e ()



void int_initialize_1e (int flags, int order)



double int_prim_overlap (shell_t *pshell1, shell_t *pshell2, double *pA, double *pB, int prim1, int prim2, int i1, int j1, int k1, int i2, int j2, int k2)



void int_accum_shell_kinetic (int ish, int jsh)



void int_accum_shell_kinetic_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_nuclear_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_nuclear_hfc_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_nuclear_hf_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_nuclear_nonhf_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_efield (int ish, int jsh, double *position)



void int_accum_shell_point_charge (int ish, int jsh, int ncharge, const double *charge, const double *const *position)



void int_shell_nuclear_hf_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_shell_nuclear_nonhf_1der (int ish, int jsh, Ref&lt; GaussianBasisSet &gt; dercs, int centernum)



void int_accum_shell_dipole (int ish, int jsh, double *com)



void int_initialize_offsets1 ()



void int_done_offsets1 ()



void transform_init ()



void transform_done ()



void source_space (int nsource)



void copy_to_source (double *integrals, int nsource)



void do_transform_1e (Integral *integ, double *integrals, GaussianShell *sh1, GaussianShell *sh2, int chunk)



void transform_1e (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2, int chunk)



void accum_transform_1e (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2, int chunk)



void transform_1e (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2)



void accum_transform_1e (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2)



void transform_1e_xyz (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2)



void accum_transform_1e_xyz (Integral *integ, double *integrals, double *target, GaussianShell *sh1, GaussianShell *sh2)



Protected Attributes</code></pre>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> double * <code>fjttable_</code> </p>
<p> <code>Ref</code>&lt; <code>FJT</code> &gt; <code>fjt_</code> </p>
<p> int <code>bs1_shell_offset_</code> </p>
<p> int <code>bs2_shell_offset_</code> </p>
<p> int <code>bs1_func_offset_</code> </p>
<p> int <code>bs2_func_offset_</code> </p>
<p> int <code>bs1_prim_offset_</code> </p>
<p> int <code>bs2_prim_offset_</code> </p>
<p> double <code>oo2zeta_a</code> </p>
<p> double <code>oo2zeta_b</code> </p>
<p> double <code>sMus</code> [3] </p>
<p> double <code>sTs</code> </p>
<p> double <code>xi</code> </p>
<p> double <code>A</code> [3] </p>
<p> double <code>B</code> [3] </p>
<p> double <code>C</code> [3] </p>
<p> double <code>ss</code> </p>
<p> double <code>PmA</code> [3] </p>
<p> double <code>PmB</code> [3] </p>
<p> double <code>PmC</code> [3] </p>
<p> double <code>zeta</code> </p>
<p> double <code>oo2zeta</code> </p>
<p> <code>GaussianShell</code> * <code>gshell1</code> </p>
<p> <code>GaussianShell</code> * <code>gshell2</code> </p>
<p> int <code>exponent_weighted</code> </p>
<p> int <code>scale_shell_result</code> </p>
<p> double <code>result_scale_factor</code> </p>
<p> int <code>three_center</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>third_centers</code> </p>
<p> int <code>third_centernum</code> </p>
<p> int <code>init_order</code> </p>
<p> double * <code>buff</code> </p>
<p> double * <code>cartesianbuffer</code> </p>
<p> double * <code>cartesianbuffer_scratch</code> </p>
<p> int <code>mu</code> </p>
<p> <code>IntV3Arraydoublep3</code> <code>inter</code> </p>
<p> <code>IntV3Arraydoublep3</code> <code>efield_inter</code> </p>
<p> double * <code>source</code> </p>
<p> int <code>nsourcemax</code></p>
<h2>Detailed Description</h2>
<p><code>Int1eV3</code> is a class wrapper for the one body part of the C language IntV3 library. </p>
<p> It is used by <code>OneBodyIntV3</code> and <code>OneBodyDerivIntV3</code> to implement <code>IntegralV3</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
