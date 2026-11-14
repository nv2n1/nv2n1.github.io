---
title: "sc_onebodyonecenterderivint(3)"
name: "sc_onebodyonecenterderivint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyonecenterderivint/"
description: "sc::OneBodyOneCenterDerivInt –"
---

<p>sc::OneBodyOneCenterDerivInt &#8211; </p>
<p> <code>OneBodyOneCenterDerivInt</code> is an abstract base class for objects that compute one body derivative integrals on a single center.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OneBodyOneCenterDerivInt (Integral *, const Ref&lt; GaussianBasisSet &gt; &amp;b)



int nbasis () const


Return the number of basis functions on center one.


int nbasis1 () const


Return the number of basis functions on center one.


int nshell () const


Return the number of shells on center one.


int nshell1 () const


Return the number of shells on center one.


Ref&lt; GaussianBasisSet &gt; basis ()


Return the basis set on center one.


Ref&lt; GaussianBasisSet &gt; basis1 ()


Return the basis set on center one.


const double * buffer () const


The computed shell integrals will be put in the buffer returned by this member.


virtual void compute_shell (int ish, DerivCenters &amp;)=0


Compute the derivative integrals and place the result in the buffer returned by buffer().


virtual void compute_shell (int ish, int center)=0


Compute the derivative integrals with respect to the given center and place the result in the buffer returned by buffer().



Protected Attributes</code></pre>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1</code> </p>
<p> double * <code>buffer_</code></p>
<h2>Detailed Description</h2>
<p><code>OneBodyOneCenterDerivInt</code> is an abstract base class for objects that compute one body derivative integrals on a single center.</p>
<h2>Member Function Documentation</h2>
<h3>const double* sc::OneBodyOneCenterDerivInt::buffer () const</h3>
<p>The computed shell integrals will be put in the buffer returned by this member.</p>
<h3>virtual void sc::OneBodyOneCenterDerivInt::compute_shell (int ish, int center) [pure virtual]</h3>
<p><code>Compute</code> the derivative integrals with respect to the given center and place the result in the buffer returned by <code>buffer()</code>.</p>
<h3>virtual void sc::OneBodyOneCenterDerivInt::compute_shell (int ish, <code>DerivCenters</code> &amp;) [pure virtual]</h3>
<p><code>Compute</code> the derivative integrals and place the result in the buffer returned by <code>buffer()</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
