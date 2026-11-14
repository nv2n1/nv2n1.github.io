---
title: "sc_onebodyderivint(3)"
name: "sc_onebodyderivint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyderivint/"
description: "sc::OneBodyDerivInt –"
---

<p>sc::OneBodyDerivInt &#8211; </p>
<p> <code>OneBodyDerivInt</code> is an abstract base class for objects that compute one body derivative integrals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::OneBodyDerivIntCCA</code>, and <code>sc::OneBodyDerivIntV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OneBodyDerivInt (Integral *, const Ref&lt; GaussianBasisSet &gt; &amp;b)



OneBodyDerivInt (Integral *, const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2)



int nbasis () const


Return the number of basis functions on center one.


int nbasis1 () const


Return the number of basis functions on the center one.


int nbasis2 () const


Return the number of basis functions on the center two.


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


virtual void compute_shell (int ish, int jsh, DerivCenters &amp;)=0


Compute the derivative integrals and place the result in the buffer returned by buffer().


virtual void compute_shell (int ish, int jsh, int center)=0


Compute the derivative integrals with respect to the given center and place the result in the buffer returned by buffer().



Protected Attributes</code></pre>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2</code> </p>
<p> double * <code>buffer_</code></p>
<h2>Detailed Description</h2>
<p><code>OneBodyDerivInt</code> is an abstract base class for objects that compute one body derivative integrals.</p>
<h2>Member Function Documentation</h2>
<h3>const double* sc::OneBodyDerivInt::buffer () const</h3>
<p>The computed shell integrals will be put in the buffer returned by this member.</p>
<h3>virtual void sc::OneBodyDerivInt::compute_shell (int ish, int jsh, int center) [pure virtual]</h3>
<p><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implemented in <code>sc::OneBodyDerivIntCCA</code>, and <code>sc::OneBodyDerivIntV3</code>.</p>
<h3>virtual void sc::OneBodyDerivInt::compute_shell (int ish, int jsh, <code>DerivCenters</code> &amp;) [pure virtual]</h3>
<p><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>. </p>
<p> Implemented in <code>sc::OneBodyDerivIntCCA</code>, and <code>sc::OneBodyDerivIntV3</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
