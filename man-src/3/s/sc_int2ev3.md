---
title: "sc_int2ev3(3)"
name: "sc_int2ev3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int2ev3/"
description: "sc::Int2eV3 –"
---

<p>sc::Int2eV3 &#8211; </p>
<p> <code>Int2eV3</code> is a class wrapper for the two body part of the C language IntV3 library.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/int2e.h">int2e.h</a>&gt; </p>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Classes</h3>
<p> struct <code>store_list</code> </p>
<h3>Public Types</h3>
<p> enum { <code>STORAGE_CHUNK</code> = 4096 } </p>
<h3>Public Member Functions</h3>
<p> <code>Int2eV3</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs4, int order, size_t storage) </p>
<p> void <code>init_storage</code> (int size) </p>
<p> void <code>done_storage</code> () </p>
<p> int <code>storage_used</code> () </p>
<p> void <code>init_bounds</code> () </p>
<p> void <code>init_bounds_1der</code> () </p>
<p> void <code>done_bounds</code> () </p>
<p> void <code>done_bounds_1der</code> () </p>
<p> int <code>redundant</code> () </p>
<p> void <code>set_redundant</code> (int i) </p>
<p> int <code>permute</code> () </p>
<p> void <code>set_permute</code> (int i) </p>
<p> int <code>used_storage</code> () const </p>
<p> void <code>erep</code> (int &amp;psh1, int &amp;psh2, int &amp;psh3, int &amp;psh4) </p>
<p> void <code>erep</code> (int *shells, int *sizes) </p>
<p> void <code>erep_all1der</code> (int &amp;psh1, int &amp;psh2, int &amp;psh3, int &amp;psh4, <code>der_centersv3_t</code> *der_centers) </p>
<p> void <code>erep_all1der</code> (int *shells, int *sizes, <code>der_centersv3_t</code> *dercenters) </p>
<p> void <code>erep_2center</code> (int &amp;psh1, int &amp;psh2) </p>
<p> void <code>erep_2center</code> (int *shells, int *sizes) </p>
<p> void <code>erep_3center</code> (int &amp;psh1, int &amp;psh2, int &amp;psh3) </p>
<p> void <code>erep_3center</code> (int *shells, int *sizes) </p>
<p> int <code>erep_4bound</code> (int s1, int s2, int s3, int s4) </p>
<p> int <code>erep_4bound_1der</code> (int s1, int s2, int s3, int s4) </p>
<p> double * <code>buffer</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis1</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis2</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis3</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis4</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>cs1</code> () const </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>cs2</code> () const </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>cs3</code> () const </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>cs4</code> () const </p>
<p> <code>GaussianBasisSet</code> * <code>pcs1</code> () const </p>
<p> <code>GaussianBasisSet</code> * <code>pcs2</code> () const </p>
<p> <code>GaussianBasisSet</code> * <code>pcs3</code> () const </p>
<p> <code>GaussianBasisSet</code> * <code>pcs4</code> () const </p>
<h3>Static Public Member Functions</h3>
<p> static double <code>logbound_to_bound</code> (int) </p>
<p> static int <code>bound_to_logbound</code> (double value) </p>
<h3>Protected Types</h3>
<p> enum { <code>int_bound_min</code> = SCHAR_MIN, <code>int_bound_max</code> = SCHAR_MAX } </p>
<p> typedef struct <code>store_list</code> <code>store_list_t</code> </p>
<p> typedef int(BuildIntV3::* <code>intfunc</code> )() </p>
<p> typedef signed char <code>int_bound_t</code> </p>
<h3>Protected Member Functions</h3>
<p> void <code>add_store</code> (void *p) </p>
<p> void <code>free_store</code> () </p>
<p> void <code>_free_store</code> (<code>store_list_t</code> *s, int n) </p>
<p> void <code>build_not_using_gcs</code> (int nc1, int nc2, int nc3, int nc4, int minam1, int minam3, int maxam12, int maxam34, int dam1, int dam2, int dam3, int dam4, int eAB) </p>
<p> void <code>build_using_gcs</code> (int nc1, int nc2, int nc3, int nc4, int minam1, int minam3, int maxam12, int maxam34, int dam1, int dam2, int dam3, int dam4, int eAB) </p>
<p> void <code>gen_prim_intermediates</code> (int pr1, int pr2, int pr3, int pr4, int am) </p>
<p> void <code>gen_prim_intermediates_with_norm</code> (int pr1, int pr2, int pr3, int pr4, int am, double norm) </p>
<p> void <code>gen_shell_intermediates</code> (int sh1, int sh2, int sh3, int sh4) </p>
<p> void <code>blockbuildprim</code> (int minam1, int maxam12, int minam3, int maxam34) </p>
<p> void <code>blockbuildprim_1</code> (int am12min, int am12max, int am34, int m) </p>
<p> void <code>blockbuildprim_3</code> (int am34min, int am34max, int m) </p>
<p> void <code>int_init_buildgc</code> (int order, int am1, int am2, int am3, int am4, int nc1, int nc2, int nc3, int nc4) </p>
<p> void <code>int_done_buildgc</code> () </p>
<p> void <code>int_buildgcam</code> (int minam1, int minam2, int minam3, int minam4, int maxam1, int maxam2, int maxam3, int maxam4, int dam1, int dam2, int dam3, int dam4, int sh1, int sh2, int sh3, int sh4, int eAB) </p>
<p> void <code>int_offset_print</code> (std::ostream &amp;, double *buffer, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c1, int s1, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c2, int s2, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c3, int s3, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c4, int s4) </p>
<p> void <code>int_offset_print_n</code> (std::ostream &amp;, double *buffer, int n1, int n2, int n3, int n4, int o1, int o2, int o3, int o4, int e12, int e13e24, int e34) </p>
<p> void <code>int_print</code> (std::ostream &amp;, double *buffer, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c1, int s1, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c2, int s2, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c3, int s3, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; c4, int s4) </p>
<p> void <code>int_print_n</code> (std::ostream &amp;, double *buffer, int n1, int n2, int n3, int n4, int e12, int e13e24, int e34) </p>
<p> void <code>int_print_intermediates</code> (std::ostream &amp;) </p>
<p> void <code>shiftam_12</code> (double *I0100, double *I1000, double *I0000, int am1, int am2, int am3, int am4) </p>
<p> void <code>shiftam_12eAB</code> (double *I0100, double *I1000, double *I0000, int am1, int am2, int am3, int am4) </p>
<p> void <code>shiftam_34</code> (double *I0001, double *I0010, double *I0000, int am1, int am2, int am3, int am4) </p>
<p> void <code>int_init_shiftgc</code> (int order, int am1, int am2, int am3, int am4) </p>
<p> void <code>int_done_shiftgc</code> () </p>
<p> double * <code>int_shiftgcam</code> (int gc1, int gc2, int gc3, int gc4, int tam1, int tam2, int tam3, int tam4, int peAB) </p>
<p> void <code>alloc_inter</code> (int nprim, int nshell) </p>
<p> void <code>compute_shell_1</code> (<code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; cs, int, int) </p>
<p> void <code>compute_prim_2</code> (<code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; cs1, int, int, <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; cs2, int, int) </p>
<p> double * <code>int_initialize_erep</code> (size_t storage, int order, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;cs1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;cs2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;cs3, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;cs4) </p>
<p> void <code>int_done_erep</code> () </p>
<p> void <code>transform_init</code> () </p>
<p> void <code>transform_done</code> () </p>
<p> void <code>source_space</code> (int nsource) </p>
<p> void <code>copy_to_source</code> (double *integrals, int nsource) </p>
<p> void <code>do_gencon_sparse_transform_2e</code> (<code>Integral</code> *integ, double *integrals, double *target, int index, <code>GaussianShell</code> *sh1, <code>GaussianShell</code> *sh2, <code>GaussianShell</code> *sh3, <code>GaussianShell</code> *sh4) </p>
<p> void <code>transform_2e_slow</code> (<code>Integral</code> *, double *integrals, double *target, <code>GaussianShell</code> *sh1, <code>GaussianShell</code> *sh2, <code>GaussianShell</code> *sh3, <code>GaussianShell</code> *sh4) </p>
<p> void <code>transform_2e</code> (<code>Integral</code> *, double *integrals, double *target, <code>GaussianShell</code> *sh1, <code>GaussianShell</code> *sh2, <code>GaussianShell</code> *sh3, <code>GaussianShell</code> *sh4) </p>
<p> void <code>compute_erep</code> (int flags, int *psh1, int *psh2, int *psh3, int *psh4, int dam1, int dam2, int dam3, int dam4) </p>
<p> void <code>compute_erep_1der</code> (int flags, double *buffer, int *psh1, int *psh2, int *psh3, int *psh4, int dercenter) </p>
<p> void <code>nonredundant_erep</code> (double *buffer, int e12, int e34, int e13e24, int n1, int n2, int n3, int n4, int *red_off, int *nonred_off) </p>
<p> void <code>compute_erep_bound1der</code> (int flags, double *buffer, int *psh1, int *psh2, int *psh3, int *psh4) </p>
<p> void <code>int_erep_bound1der</code> (int flags, int bsh1, int bsh2, int *size) </p>
<p> void <code>int_init_bounds_nocomp</code> () </p>
<p> void <code>int_init_bounds_1der_nocomp</code> () </p>
<p> void <code>int_bounds_comp</code> (int s1, int s2) </p>
<p> void <code>int_bounds_1der_comp</code> (int s1, int s2) </p>
<p> int <code>int_erep_2bound</code> (int s1, int s2) </p>
<p> int <code>int_erep_0bound_1der</code> () </p>
<p> int <code>int_erep_2bound_1der</code> (int s1, int s2) </p>
<p> void <code>compute_bounds</code> (int_bound_t *overall, int_bound_t *vec, int flag) </p>
<p> void <code>compute_bounds_shell</code> (int_bound_t *overall, int_bound_t *vec, int flag, int sh1, int sh2) </p>
<p> int <code>int_have_stored_integral</code> (int sh1, int sh2, int sh3, int sh4, int p12, int p34, int p13p24) </p>
<p> void <code>int_store_integral</code> (int sh1, int sh2, int sh3, int sh4, int p12, int p34, int p13p24, int size) </p>
<p> void <code>int_initialize_offsets2</code> () </p>
<p> void <code>int_done_offsets2</code> () </p>
<p> void <code>make_int_unit_shell</code> () </p>
<p> void <code>delete_int_unit_shell</code> () </p>
<h3>Protected Attributes</h3>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>BuildIntV3</code> <code>build</code> </p>
<p> <code>Ref</code>&lt; <code>IntegralStorer</code> &gt; <code>storer</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs3_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs4_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>pbs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>pbs2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>pbs3_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>pbs4_</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code> </p>
<p> int <code>bs1_shell_offset_</code> </p>
<p> int <code>bs2_shell_offset_</code> </p>
<p> int <code>bs3_shell_offset_</code> </p>
<p> int <code>bs4_shell_offset_</code> </p>
<p> int <code>bs1_func_offset_</code> </p>
<p> int <code>bs2_func_offset_</code> </p>
<p> int <code>bs3_func_offset_</code> </p>
<p> int <code>bs4_func_offset_</code> </p>
<p> int <code>bs1_prim_offset_</code> </p>
<p> int <code>bs2_prim_offset_</code> </p>
<p> int <code>bs3_prim_offset_</code> </p>
<p> int <code>bs4_prim_offset_</code> </p>
<p> int <code>n_store_last</code> </p>
<p> <code>store_list_t</code> * <code>store</code> </p>
<p> intfunc <code>build_routine</code> [4][4][4][4][2] </p>
<p> int <code>osh1</code> </p>
<p> int <code>osh2</code> </p>
<p> int <code>osh3</code> </p>
<p> int <code>osh4</code> </p>
<p> int <code>opr1</code> </p>
<p> int <code>opr2</code> </p>
<p> int <code>opr3</code> </p>
<p> int <code>opr4</code> </p>
<p> int <code>saved_am12</code> </p>
<p> int <code>saved_am34</code> </p>
<p> int <code>saved_ncon</code> </p>
<p> <code>IntV3Arrayint3</code> <code>contract_length</code> </p>
<p> int <code>g1</code> </p>
<p> int <code>g2</code> </p>
<p> int <code>g3</code> </p>
<p> int <code>g4</code> </p>
<p> double <code>AmB</code> [3] </p>
<p> double <code>CmD</code> [3] </p>
<p> int <code>eAB</code> </p>
<p> double * <code>buf34</code> </p>
<p> double * <code>buf12</code> </p>
<p> double * <code>bufshared</code> </p>
<p> int <code>redundant_</code> </p>
<p> int <code>permute_</code> </p>
<p> <code>Ref</code>&lt; <code>FJT</code> &gt; <code>fjt_</code> </p>
<p> int * <code>int_shell_to_prim</code> </p>
<p> <code>IntV3Arraydouble2</code> <code>int_shell_r</code> </p>
<p> <code>IntV3Arraydouble2</code> <code>int_prim_zeta</code> </p>
<p> <code>IntV3Arraydouble2</code> <code>int_prim_k</code> </p>
<p> <code>IntV3Arraydouble2</code> <code>int_prim_oo2zeta</code> </p>
<p> <code>IntV3Arraydouble3</code> <code>int_prim_p</code> </p>
<p> double * <code>int_buffer</code> </p>
<p> double * <code>int_derint_buffer</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>int_cs1</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>int_cs2</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>int_cs3</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>int_cs4</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell1</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell2</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell3</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell4</code> </p>
<p> <code>IntV3Arraydoublep2</code> **** <code>e0f0_con_ints_array</code> </p>
<p> int <code>int_expweight1</code> </p>
<p> int <code>int_expweight2</code> </p>
<p> int <code>int_expweight3</code> </p>
<p> int <code>int_expweight4</code> </p>
<p> int <code>int_unit2</code> </p>
<p> int <code>int_unit4</code> </p>
<p> <code>GaussianShell</code> * <code>int_unit_shell</code> </p>
<p> int <code>int_integral_storage</code> </p>
<p> int <code>int_store1</code> </p>
<p> int <code>int_store2</code> </p>
<p> int <code>int_derivative_bounds</code> </p>
<p> double * <code>source</code> </p>
<p> double * <code>target</code> </p>
<p> double * <code>scratch</code> </p>
<p> int <code>nsourcemax</code> </p>
<p> int_bound_t <code>int_Q</code> </p>
<p> int_bound_t <code>int_R</code> </p>
<p> int_bound_t * <code>int_Qvec</code> </p>
<p> int_bound_t * <code>int_Rvec</code> </p>
<p> int <code>used_storage_</code> </p>
<p> int <code>used_storage_build_</code> </p>
<p> int <code>used_storage_shift_</code> </p>
<h2>Detailed Description</h2>
<p> <code>Int2eV3</code> is a class wrapper for the two body part of the C language IntV3 library. </p>
<p> It is used by <code>TwoBodyIntV3</code> and <code>TwoBodyDerivIntV3</code> to implement <code>IntegralV3</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
