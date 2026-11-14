---
title: "sc_onebodyonecenterint(3)"
name: "sc_onebodyonecenterint"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_onebodyonecenterint/"
description: "sc::OneBodyOneCenterInt –"
---

<p>sc::OneBodyOneCenterInt &#8211; </p>
<p> <code>OneBodyOneCenterInt</code> is an abstract base class for objects that compute integrals between two basis functions.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;obint.h&gt;</code></pre>
<p> Inherits <code>sc::RefCount</code>. Inherited by <code>sc::OneBodyOneCenterWrapper</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int nbasis () const


Returns the number of basis functions on center one.


int nbasis1 () const


Returns the number of basis functions on the center one.


int nshell () const


Return the number of shells on center one.


int nshell1 () const


Return the number of shells on the center one.


Ref&lt; GaussianBasisSet &gt; basis ()


Return the basis set on center one.


Ref&lt; GaussianBasisSet &gt; basis1 ()


Return the basis set on the center one.


const double * buffer () const


Returns the buffer where the integrals are placed.


virtual void compute_shell (int)=0


Computes the integrals for basis functions on the given shell.


virtual void reinitialize ()


This is called for one body integrals that take data to let them know that the data they reference has changed.


virtual bool cloneable ()


Return true if the clone member can be called.


virtual Ref&lt; OneBodyOneCenterInt &gt; clone ()


Returns a clone of this.


Integral * integral () const



Protected Member Functions</code></pre>
<p> <code>OneBodyOneCenterInt</code> (<code>Integral</code> *integral, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp;b1)</p>
<h3>Protected Attributes</h3>
<p><code>Integral</code> * <code>integral_</code> </p>
<p> <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; <code>bs1_</code> </p>
<p> double * <code>buffer_</code></p>
<h2>Detailed Description</h2>
<p><code>OneBodyOneCenterInt</code> is an abstract base class for objects that compute integrals between two basis functions.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Ref</code>&lt;<code>OneBodyOneCenterInt</code>&gt; sc::OneBodyOneCenterInt::clone () [virtual]</h3>
<p>Returns a clone of this. The default implementation throws an exception.</p>
<h3>virtual bool sc::OneBodyOneCenterInt::cloneable () [virtual]</h3>
<p>Return true if the clone member can be called. The default implementation returns false.</p>
<h3>virtual void sc::OneBodyOneCenterInt::compute_shell (int) [pure virtual]</h3>
<p>Computes the integrals for basis functions on the given shell. </p>
<p> Implemented in <code>sc::OneBodyOneCenterWrapper</code>.</p>
<h3>virtual void sc::OneBodyOneCenterInt::reinitialize () [virtual]</h3>
<p>This is called for one body integrals that take data to let them know that the data they reference has changed.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
