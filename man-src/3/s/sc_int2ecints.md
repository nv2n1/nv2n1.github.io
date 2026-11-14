---
title: "sc_int2ecints(3)"
name: "sc_int2ecints"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_int2ecints/"
description: "sc::Int2eCints –"
---

<p>sc::Int2eCints &#8211; </p>
<p> <code>Int2eCints</code> is an interface to various specializations of two-electron integral evaluators implemented in Cints.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/int2e.h">int2e.h</a>&gt; </p>
<p> Inherits <code>sc::RefCount</code>. </p>
<p> Inherited by <code>sc::EriCints</code>, and <code>sc::GRTCints</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>Int2eCints</code> (<code>Integral</code> *, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;, size_t storage) </p>
<p> void <code>init_storage</code> (size_t)<br />
 <i>Sets storage limit and starts storage tracking. </i><br />
 void <code>done_storage</code> ()<br />
 <i>Finishes storage tracking. </i><br />
 size_t <code>storage_used</code> () const<br />
 <i>Reports how much storage is actually used at a given time. </i><br />
 int <code>redundant</code> () const<br />
 <i>Whether redundant integrals are returned. </i><br />
 void <code>set_redundant</code> (int flag)<br />
 <i>Set redundant flag. </i><br />
 int <code>permute</code> () const<br />
 <i>Whether shells can be permuted. </i><br />
 void <code>set_permute</code> (int flag)<br />
 <i>Set shell permutation flag. </i><br />
 virtual void <code>compute_quartet</code> (int *, int *, int *, int *)=0<br />
 <i>Evaluate the target quartet of integrals. </i><br />
 virtual double * <code>buffer</code> (<code>TwoBodyInt::tbint_type</code>=TwoBodyInt::eri) const =0<br />
 <i>Returns the location of the buffer with target integrals. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis1</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis2</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis3</code> () </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis4</code> () </p>
<h3>Protected Member Functions</h3>
<p> void <code>check_storage_</code> () const </p>
<p> void <code>transform_contrquartets_</code> (double *, double *) </p>
<p> void <code>sort_contrquartets_to_shellquartet_</code> (double *, double *) </p>
<p> void <code>permute_target_</code> (double *, double *, int, int, int) </p>
<p> void <code>permute_1234_to_1243_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_2134_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_2143_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_3412_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_3421_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_4312_</code> (double *, double *) </p>
<p> void <code>permute_1234_to_4321_</code> (double *, double *) </p>
<p> void <code>get_nonredundant_ints_</code> (double *, double *, int, int, int) </p>
<h3>Static Protected Member Functions</h3>
<p> static size_t <code>storage_required_</code> (const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b3=0, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b4=0) </p>
<h3>Protected Attributes</h3>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs3_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs4_</code> </p>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell1_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell2_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell3_</code> </p>
<p> <code>GaussianShell</code> * <code>int_shell4_</code> </p>
<p> int <code>permute_</code> </p>
<p> int <code>redundant_</code> </p>
<p> size_t <code>storage_</code> </p>
<p> size_t <code>storage_used_</code> </p>
<p> double * <code>tformbuf_</code> </p>
<h2>Detailed Description</h2>
<p> <code>Int2eCints</code> is an interface to various specializations of two-electron integral evaluators implemented in Cints. </p>
<p> It is used by <code>TwoBodyIntCints</code> and <code>TwoBodyDerivIntCints</code> to implement <code>IntegralCints</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
