---
title: "sc_onebodyint(3)"
name: "sc_onebodyint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyint/"
description: "sc::OneBodyInt –"
---

<p>sc::OneBodyInt &#8211; </p>
<p> <code>OneBodyInt</code> is an abstract base class for objects that compute integrals between two basis functions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::DipoleIntV3</code>, <code>sc::EfieldDotVectorIntV3</code>, <code>sc::OneBodyIntCCA</code>, <code>sc::OneBodyIntCints</code>, <code>sc::OneBodyIntV3</code>, and <code>sc::PointChargeIntV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int nbasis () const


Returns the number of basis functions on center one.


int nbasis1 () const


Returns the number of basis functions on the center one.


int nbasis2 () const


Returns the number of basis functions on the center two.


int nshell () const


Return the number of shells on center one.


int nshell1 () const


Return the number of shells on the center one.


int nshell2 () const


Return the number of shells on the center two.


Ref&lt; GaussianBasisSet &gt; basis ()


Return the basis set on center one.


Ref&lt; GaussianBasisSet &gt; basis1 ()


Return the basis set on the center one.


Ref&lt; GaussianBasisSet &gt; basis2 ()


Return the basis set on the center two.


const double * buffer () const


Returns the buffer where the integrals are placed.


virtual void compute_shell (int, int)=0


Computes the integrals between basis functions in the given shell pair.


virtual void reinitialize ()


This is called for one body integrals that take data to let them know that the data they reference has changed.


virtual bool cloneable ()


Return true if the clone member can be called.


virtual Ref&lt; OneBodyInt &gt; clone ()


Returns a clone of this.


Integral * integral () const



Protected Member Functions
OneBodyInt (Integral *integral, const Ref&lt; GaussianBasisSet &gt; &amp;b1, const Ref&lt; GaussianBasisSet &gt; &amp;b2=0)



Protected Attributes</code></pre>
<p> <code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs2_</code> </p>
<p> double * <code>buffer_</code></p>
<h2>Detailed Description</h2>
<p><code>OneBodyInt</code> is an abstract base class for objects that compute integrals between two basis functions.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyInt</code>&gt; sc::OneBodyInt::clone () [virtual]</h3>
<p>Returns a clone of this. The default implementation throws an exception. </p>
<p> Reimplemented in <code>sc::OneBodyIntCints</code>, <code>sc::OneBodyIntCCA</code>, and <code>sc::OneBodyIntV3</code>.</p>
<h3>virtual bool sc::OneBodyInt::cloneable () [virtual]</h3>
<p>Return true if the clone member can be called. The default implementation returns false. </p>
<p> Reimplemented in <code>sc::OneBodyIntCints</code>, <code>sc::OneBodyIntCCA</code>, and <code>sc::OneBodyIntV3</code>.</p>
<h3>virtual void sc::OneBodyInt::compute_shell (int, int) [pure virtual]</h3>
<p>Computes the integrals between basis functions in the given shell pair. </p>
<p> Implemented in <code>sc::OneBodyIntCints</code>, <code>sc::OneBodyIntCCA</code>, <code>sc::OneBodyIntV3</code>, <code>sc::PointChargeIntV3</code>, <code>sc::EfieldDotVectorIntV3</code>, and <code>sc::DipoleIntV3</code>.</p>
<h3>virtual void sc::OneBodyInt::reinitialize () [virtual]</h3>
<p>This is called for one body integrals that take data to let them know that the data they reference has changed.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
