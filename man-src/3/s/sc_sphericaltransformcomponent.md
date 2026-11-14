---
title: "sc_sphericaltransformcomponent(3)"
name: "sc_sphericaltransformcomponent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sphericaltransformcomponent/"
description: "sc::SphericalTransformComponent –"
---

<p>sc::SphericalTransformComponent &#8211; </p>
<p> This is a base class for a container for a component of a sparse Cartesian to solid harmonic basis function transformation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform.h&gt;</code></pre>
<p> Inherited by <code>sc::SphericalTransformComponentCCA</code>, <code>sc::SphericalTransformComponentCints</code>, and <code>sc::SphericalTransformComponentV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int a () const


Returns the exponent of x.


int b () const


Returns the exponent of y.


int c () const


Returns the exponent of z.


int cartindex () const


Returns the index of the Cartesian basis function.


int pureindex () const


Returns the index solid harmonic basis function.


double coef () const


Returns the coefficient of this component of the transformation.


virtual void init (int a, int b, int c, double coef, int pureindex)=0


Initialize this object.



Protected Attributes
double coef_



int a_



int b_



int c_



int cartindex_



int pureindex_</code></pre>
<h2>Detailed Description</h2>
<p>This is a base class for a container for a component of a sparse Cartesian to solid harmonic basis function transformation.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SphericalTransformComponent::init (int a, int b, int c, double coef, int pureindex) [pure virtual]</h3>
<p>Initialize this object. This must be provided in all specializations of this class to establish the ordering between a, b and c and the index of the Cartesian basis function. Other things such as adjustment of the coefficient to account for normalization differences can be done as well. The default <code>SphericalTransform::init()</code> implementation requires that only the xl , yl and zl basis functions are normalized to unity. </p>
<p> Implemented in <code>sc::SphericalTransformComponentCints</code>, <code>sc::SphericalTransformComponentCCA</code>, and <code>sc::SphericalTransformComponentV3</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
