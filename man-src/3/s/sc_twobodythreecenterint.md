---
title: "sc_twobodythreecenterint(3)"
name: "sc_twobodythreecenterint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodythreecenterint/"
description: "sc::TwoBodyThreeCenterInt –"
---

<p>sc::TwoBodyThreeCenterInt &#8211; </p>
<p> This is an abstract base type for classes that compute integrals involving two electrons in three Gaussian functions.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/tbint.h">tbint.h</a>&gt; </p>
<p> Inherits <code>sc::RefCount</code>. </p>
<p> Inherited by <code>sc::TwoBodyThreeCenterIntV3</code>.</p>
<h3>Public Types</h3>
<p> enum <code>tbint_type</code> { <code>eri</code> = 0, <code>r12</code> = 1, <code>r12t1</code> = 2, <code>r12t2</code> = 3 }<br />
 <i>Types of two-body integrals that </i><code>TwoBodyInt</code> understands: eri stands for electron repulsion integral, r12 stands for integrals of r12 operator, r12t1 and r12t2 are integrals of [r12,T1] and [r12,T2] operators.</p>
<h3>Public Member Functions</h3>
<p> int <code>nbasis</code> () const<br />
 <i>Return the number of basis functions on center one. </i><br />
 int <code>nbasis1</code> () const<br />
 <i>Return the number of basis functions on center one. </i><br />
 int <code>nbasis2</code> () const<br />
 <i>Return the number of basis functions on center two. </i><br />
 int <code>nbasis3</code> () const<br />
 <i>Return the number of basis functions on center three. </i><br />
 int <code>nshell</code> () const<br />
 <i>Return the number of shells on center one. </i><br />
 int <code>nshell1</code> () const<br />
 <i>Return the number of shells on center one. </i><br />
 int <code>nshell2</code> () const<br />
 <i>Return the number of shells on center two. </i><br />
 int <code>nshell3</code> () const<br />
 <i>Return the number of shells on center three. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis</code> ()<br />
 <i>Return the basis set on center one. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis1</code> ()<br />
 <i>Return the basis set on center one. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis2</code> ()<br />
 <i>Return the basis set on center two. </i><br />
 <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>basis3</code> ()<br />
 <i>Return the basis set on center three. </i><br />
 virtual const double * <code>buffer</code> (<code>tbint_type</code> type=eri) const<br />
 <i>The computed shell integrals will be put in the buffer returned by this member. </i><br />
 virtual void <code>compute_shell</code> (int, int, int)=0<br />
 <i>Given three shell indices, integrals will be computed and placed in the buffer. </i><br />
 virtual int <code>log2_shell_bound</code> (int=-1, int=-1, int=-1)=0<br />
 <i>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. </i><br />
 int <code>redundant</code> () const<br />
 <i>If redundant is true, then keep redundant integrals in the buffer. </i><br />
 void <code>set_redundant</code> (int i)<br />
 <i>See </i><code>redundant()</code>.<br />
 virtual void <code>set_integral_storage</code> (size_t storage)<br />
 <i>This storage is used to cache computed integrals. </i><br />
 <code>Integral</code> * <code>integral</code> () const<br />
 <i>Return the integral factory that was used to create this object. </i></p>
<h3>Static Public Attributes</h3>
<p> static const int <code>num_tbint_types</code> = 4<br />
 <i>The total number of such types. </i></p>
<h3>Protected Member Functions</h3>
<p> <code>TwoBodyThreeCenterInt</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs2, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs3) </p>
<h3>Protected Attributes</h3>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs3_</code> </p>
<p> double * <code>buffer_</code> </p>
<p> int <code>redundant_</code> </p>
<h2>Detailed Description</h2>
<p> This is an abstract base type for classes that compute integrals involving two electrons in three Gaussian functions.</p>
<h2>Member Function Documentation</h2>
<h3>virtual const double* sc::TwoBodyThreeCenterInt::buffer (<code>tbint_type</code> type = eri) const [virtual]</h3>
<p> The computed shell integrals will be put in the buffer returned by this member. Some <code>TwoBodyInt</code> specializations have more than one buffer: The type arguments selects which buffer is returned. If the requested type is not supported, then 0 is returned.</p>
<h3>virtual void sc::TwoBodyThreeCenterInt::compute_shell (int, int, int) [pure virtual]</h3>
<p> Given three shell indices, integrals will be computed and placed in the buffer. The first two indices correspond to electron 1 and the second index corresponds to electron 2. </p>
<p> Implemented in <code>sc::TwoBodyThreeCenterIntV3</code>.</p>
<h3>virtual int sc::TwoBodyThreeCenterInt::log2_shell_bound (int = -1, int = -1, int = -1) [pure virtual]</h3>
<p> Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. An index of -1 for any argument indicates any shell. </p>
<p> Implemented in <code>sc::TwoBodyThreeCenterIntV3</code>.</p>
<h3>int sc::TwoBodyThreeCenterInt::redundant () const [inline]</h3>
<p> If redundant is true, then keep redundant integrals in the buffer. The default is true. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
