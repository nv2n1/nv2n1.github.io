---
title: "sc_twobodytwocenterint(3)"
name: "sc_twobodytwocenterint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodytwocenterint/"
description: "sc::TwoBodyTwoCenterInt –"
---

<p>sc::TwoBodyTwoCenterInt &#8211; </p>
<p> This is an abstract base type for classes that compute integrals involving two electrons in two Gaussian functions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::TwoBodyTwoCenterIntV3</code>.</p>
<h3>Public Types</h3>
<pre><code>enum tbint_type { eri = 0, r12 = 1, r12t1 = 2, r12t2 = 3 }


Types of two-body integrals that TwoBodyInt understands: eri stands for electron repulsion integral, r12 stands for integrals of r12 operator, r12t1 and r12t2 are integrals of [r12,T1] and [r12,T2] operators.



Public Member Functions
int nbasis () const


Return the number of basis functions on center one.


int nbasis1 () const


Return the number of basis functions on center one.


int nbasis2 () const


Return the number of basis functions on center two.


int nshell () const


Return the number of shells on center one.


int nshell1 () const


Return the number of shells on center one.


int nshell2 () const


Return the number of shells on center two.


Ref&lt; GaussianBasisSet &gt; basis ()


Return the basis set on center one.


Ref&lt; GaussianBasisSet &gt; basis1 ()


Return the basis set on center one.


Ref&lt; GaussianBasisSet &gt; basis2 ()


Return the basis set on center two.


virtual const double * buffer (tbint_type type=eri) const


The computed shell integrals will be put in the buffer returned by this member.


virtual void compute_shell (int, int)=0


Given four shell indices, integrals will be computed and placed in the buffer.


virtual int log2_shell_bound (int=-1, int=-1)=0


Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell.


int redundant () const


If redundant is true, then keep redundant integrals in the buffer.


void set_redundant (int i)


See redundant().


virtual void set_integral_storage (size_t storage)


This storage is used to cache computed integrals.


Integral * integral () const


Return the integral factory that was used to create this object.



Static Public Attributes
static const int num_tbint_types = 4


The total number of such types.



Protected Member Functions</code></pre>
<p> <code>TwoBodyTwoCenterInt</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;bs2)</p>
<h3>Protected Attributes</h3>
<p><code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> double * <code>buffer_</code> </p>
<p> int <code>redundant_</code></p>
<h2>Detailed Description</h2>
<p>This is an abstract base type for classes that compute integrals involving two electrons in two Gaussian functions.</p>
<h2>Member Function Documentation</h2>
<h3>virtual const double* sc::TwoBodyTwoCenterInt::buffer (<code>tbint_type</code> type = eri) const [virtual]</h3>
<p>The computed shell integrals will be put in the buffer returned by this member. Some <code>TwoBodyInt</code> specializations have more than one buffer: The type arguments selects which buffer is returned. If the requested type is not supported, then 0 is returned.</p>
<h3>virtual void sc::TwoBodyTwoCenterInt::compute_shell (int, int) [pure virtual]</h3>
<p>Given four shell indices, integrals will be computed and placed in the buffer. The first index corresponds to electron 1 and the second index corresponds to electron 2. </p>
<p> Implemented in <code>sc::TwoBodyTwoCenterIntV3</code>.</p>
<h3>virtual int sc::TwoBodyTwoCenterInt::log2_shell_bound (int = -1, int = -1) [pure virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block obtained from compute_shell. An index of -1 for any argument indicates any shell. </p>
<p> Implemented in <code>sc::TwoBodyTwoCenterIntV3</code>.</p>
<h3>int sc::TwoBodyTwoCenterInt::redundant () const [inline]</h3>
<p>If redundant is true, then keep redundant integrals in the buffer. The default is true.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
