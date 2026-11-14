---
title: "sc_sphericaltransform(3)"
name: "sc_sphericaltransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sphericaltransform/"
description: "sc::SphericalTransform –"
---

<p>sc::SphericalTransform &#8211; </p>
<p> This is a base class for a container for a sparse Cartesian to solid harmonic basis function transformation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform.h&gt;</code></pre>
<p> Inherited by <code>sc::ISphericalTransform</code>, <code>sc::SphericalTransformCCA</code>, <code>sc::SphericalTransformCints</code>, and <code>sc::SphericalTransformV3</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void add (int a, int b, int c, double coef, int pureindex)


Adds another SphericalTransformComponent.


int cartindex (int i) const


Returns the Cartesian basis function index of component i.


int pureindex (int i) const


Returns the solid harmonic basis function index of component i.


double coef (int i) const


Returns the transform coefficient of component i.


int a (int i) const


Returns the Cartesian basis function's x exponent of component i.


int b (int i) const


Returns the Cartesian basis function's y exponent of component i.


int c (int i) const


Returns the Cartesian basis function's z exponent of component i.


int l () const


Returns the angular momentum.


int n () const


Returns the number of components in the transformation.


virtual SphericalTransformComponent * new_components ()=0


This must create SphericalTransformComponent's of the appropriate specialization.



Protected Member Functions
SphericalTransform (int l, int subl=-1)


This constructs the SphericalTransform for the given Cartesian angular momentum l and solid harmonic angular momentum subl.


virtual void init ()


This determines all of the components of the transformation.



Protected Attributes
int n_



int l_



int subl_



SphericalTransformComponent * components_</code></pre>
<h2>Detailed Description</h2>
<p>This is a base class for a container for a sparse Cartesian to solid harmonic basis function transformation.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SphericalTransform::SphericalTransform (int l, int subl = -1) [protected]</h3>
<p>This constructs the <code>SphericalTransform</code> for the given Cartesian angular momentum l and solid harmonic angular momentum subl. Usually, l and subl will be the same. They would differ when the S component of a D Cartesian shell or the P component of an F Cartesian shell is desired, for example (see the natural atomic orbital code for an example of such use). The init member must be called to complete initialization.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SphericalTransform::init () [protected, virtual]</h3>
<p>This determines all of the components of the transformation. It should be possible to implement the <code>SphericalTransformComponent::init</code> specialization in such a way that the default <code>SphericalTransform::init</code> can be used. </p>
<p> Reimplemented in <code>sc::ISphericalTransform</code>.</p>
<h3>virtual <code>SphericalTransformComponent</code>* sc::SphericalTransform::new_components () [pure virtual]</h3>
<p>This must create SphericalTransformComponent&#8217;s of the appropriate specialization. </p>
<p> Implemented in <code>sc::SphericalTransformCints</code>, <code>sc::ISphericalTransformCints</code>, <code>sc::SphericalTransformCCA</code>, <code>sc::ISphericalTransformCCA</code>, <code>sc::SphericalTransformV3</code>, and <code>sc::ISphericalTransformV3</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
