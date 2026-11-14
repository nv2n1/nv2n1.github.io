---
title: "sc_isphericaltransform-2(3)"
name: "sc_isphericaltransform-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_isphericaltransform-2/"
description: "sc::ISphericalTransform –"
---

<p>sc::ISphericalTransform &#8211; </p>
<p> This describes a solid harmonic to Cartesian transform.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform.h&gt;</code></pre>
<p> Inherits <code>sc::SphericalTransform</code>. Inherited by <code>sc::ISphericalTransformCCA</code>, <code>sc::ISphericalTransformCints</code>, and <code>sc::ISphericalTransformV3</code>.</p>
<h3>Protected Member Functions</h3>
<p><code>ISphericalTransform</code> (int l, int subl=-1) </p>
<p> void <code>init</code> ()<br />
 <i>This determines all of the components of the transformation. </i></p>
<h2>Detailed Description</h2>
<p>This describes a solid harmonic to Cartesian transform.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ISphericalTransform::init () [protected, virtual]</h3>
<p>This determines all of the components of the transformation. It should be possible to implement the <code>SphericalTransformComponent::init</code> specialization in such a way that the default <code>SphericalTransform::init</code> can be used. </p>
<p> Reimplemented from <code>sc::SphericalTransform</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
