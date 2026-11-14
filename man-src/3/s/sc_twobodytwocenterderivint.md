---
title: "sc_twobodytwocenterderivint(3)"
name: "sc_twobodytwocenterderivint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_twobodytwocenterderivint/"
description: "sc::TwoBodyTwoCenterDerivInt –"
---

<p>sc::TwoBodyTwoCenterDerivInt &#8211; </p>
<p> This is an abstract base type for classes that compute two centers integrals involving two electrons.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;tbint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int nbasis () const


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


const double * buffer () const


The computed shell integrals will be put in the buffer returned by this member.


virtual void compute_shell (int, int, DerivCenters &amp;)=0


Given for shell indices, this will cause the integral buffer to be filled in.


virtual int log2_shell_bound (int=-1, int=-1)=0


Return log base 2 of the maximum magnitude of any integral in a shell block.



Protected Member Functions</code></pre>
<p> <code>TwoBodyTwoCenterDerivInt</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b2)</p>
<h3>Protected Attributes</h3>
<p><code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> double * <code>buffer_</code></p>
<h2>Detailed Description</h2>
<p>This is an abstract base type for classes that compute two centers integrals involving two electrons.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::TwoBodyTwoCenterDerivInt::compute_shell (int, int, <code>DerivCenters</code> &amp;) [pure virtual]</h3>
<p>Given for shell indices, this will cause the integral buffer to be filled in.</p>
<h3>virtual int sc::TwoBodyTwoCenterDerivInt::log2_shell_bound (int = -1, int = -1) [pure virtual]</h3>
<p>Return log base 2 of the maximum magnitude of any integral in a shell block. An index of -1 for any argument indicates any shell.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
