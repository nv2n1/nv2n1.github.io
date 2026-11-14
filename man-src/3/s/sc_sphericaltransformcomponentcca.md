---
title: "sc_sphericaltransformcomponentcca(3)"
name: "sc_sphericaltransformcomponentcca"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sphericaltransformcomponentcca/"
description: "sc::SphericalTransformComponentCCA –"
---

<p>sc::SphericalTransformComponentCCA &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SphericalTransformComponent</code>.</p>
<h3>Public Member Functions</h3>
<p>void <code>init</code> (int a, int b, int c, double coef, int pureindex)<br />
 <i>Initialize this object. </i></p>
<h2>Member Function Documentation</h2>
<h3>void sc::SphericalTransformComponentCCA::init (int a, int b, int c, double coef, int pureindex) [inline, virtual]</h3>
<p>Initialize this object. This must be provided in all specializations of this class to establish the ordering between a, b and c and the index of the Cartesian basis function. Other things such as adjustment of the coefficient to account for normalization differences can be done as well. The default <code>SphericalTransform::init()</code> implementation requires that only the xl , yl and zl basis functions are normalized to unity. </p>
<p> Implements <code>sc::SphericalTransformComponent</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
