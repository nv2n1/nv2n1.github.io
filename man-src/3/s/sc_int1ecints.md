---
title: "sc_int1ecints(3)"
name: "sc_int1ecints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int1ecints/"
description: "sc::Int1eCints –"
---

<p>sc::Int1eCints &#8211; </p>
<p> <code>Int1eCints</code> is used by <code>OneBodyIntCints</code> and OneBodyDerivIntCints to implement <code>IntegralCints</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;int1e.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Int1eCints</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, int order, bool need_overlap, bool need_coulomb, int ntypes) </p>
<p> void <code>set_multipole_origin</code> (const <code>Ref</code>&lt; <code>DipoleData</code> &gt; &amp;) </p>
<p> void <code>set_EdotV_origin</code> (const <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; &amp;) </p>
<p> void <code>set_Q_origin</code> (const <code>Ref</code>&lt; <code>PointChargeData</code> &gt; &amp;) </p>
<p> <code>Ref</code>&lt; <code>DipoleData</code> &gt; <code>multipole_origin</code> () </p>
<p> <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; <code>EdotV_origin</code> () </p>
<p> <code>Ref</code>&lt; <code>PointChargeData</code> &gt; <code>Q_origin</code> () </p>
<p> double * <code>buffer</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis1</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis2</code> () </p>
<p> void <code>kinetic</code> (int ish, int jsh) </p>
<p> void <code>nuclear</code> (int ish, int jsh) </p>
<p> void <code>overlap</code> (int ish, int jsh) </p>
<p> void <code>hcore</code> (int ish, int jsh) </p>
<p> void <code>edipole</code> (int ish, int jsh) </p>
<p> void <code>equadrupole</code> (int ish, int jsh)</p>
<h3>Protected Member Functions</h3>
<pre><code>void AI_OSrecurs_ (double ***AI0, double PA[3], double PB[3], double PC[3], double gamma, int iang, int jang)



void OI_OSrecurs_ (double **OIX, double **OIY, double **OIZ, double PA[3], double PB[3], double gamma, int lmaxi, int lmaxj)



void compute_doublet_info_ (int, int)



void zero_buffers_ ()



void transform_contrquartets_ (double *, double *)



void sort_contrdoublets_to_shelldoublet_ (double *, double *)



void zero_buffers_vec_ (const int)



void transform_contrquartets_vec_ (const int, double *, double *)



void sort_contrdoublets_to_shelldoublet_vec_ (const int, double *, double *)



void overlap_full_general_ ()



void overlap_sameam_general_ ()



void kinetic_full_general_ ()



void kinetic_sameam_general_ ()



void nuclear_full_general_ ()



void nuclear_sameam_general_ ()



void hcore_full_general_ ()



void hcore_sameam_general_ ()



void edipole_full_general_ ()



void equadrupole_full_general_ ()



double ** init_block_ (int, int)



void free_block_ (double **)



double *** init_box_ (int, int, int)



void free_box_ (double ***)



Protected Attributes</code></pre>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> <code>Ref</code>&lt; <code>DipoleData</code> &gt; <code>multipole_origin_</code> </p>
<p> <code>Ref</code>&lt; <code>EfieldDotVectorData</code> &gt; <code>EdotV_origin_</code> </p>
<p> <code>Ref</code>&lt; <code>PointChargeData</code> &gt; <code>Q_origin_</code> </p>
<p> bool <code>need_overlap_</code> </p>
<p> bool <code>need_coulomb_</code> </p>
<p> int <code>ntypes_</code> </p>
<p> double * <code>target_ints_buffer_</code> </p>
<p> int <code>max_doublet_size_</code> </p>
<p> double * <code>cart_ints_</code> </p>
<p> double * <code>sphharm_ints_</code> </p>
<p> double * <code>tformbuf_</code> </p>
<p> int <code>max_cart_doublet_size_</code> </p>
<p> double * <code>prim_ints_</code> </p>
<p> double * <code>contr_doublets_</code> </p>
<p> double * <code>shell_doublet_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell1_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell2_</code> </p>
<p> struct { </p>
<p> double <code>A</code> [3] </p>
<p> double <code>B</code> [3] </p>
<p> double <code>AB2</code> </p>
<p> int <code>gc1</code> </p>
<p> int <code>gc2</code> </p>
<p> int <code>p1</code> </p>
<p> int <code>p2</code> </p>
<p> int <code>am</code> </p>
<p> } <code>doublet_info_</code> </p>
<p> double ** <code>OIX_</code> </p>
<p> double ** <code>OIY_</code> </p>
<p> double ** <code>OIZ_</code> </p>
<p> double *** <code>AI0_</code> </p>
<p> int <code>indmax_</code> </p>
<p> <code>Ref</code>&lt; <code>FJT</code> &gt; <code>Fm_Eval_</code></p>
<h2>Detailed Description</h2>
<p><code>Int1eCints</code> is used by <code>OneBodyIntCints</code> and OneBodyDerivIntCints to implement <code>IntegralCints</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
