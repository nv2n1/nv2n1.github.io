---
title: "sc_nonlineartransform(3)"
name: "sc_nonlineartransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_nonlineartransform/"
description: "sc::NonlinearTransform –"
---

<p>sc::NonlinearTransform &#8211; </p>
<p> The <code>NonlinearTransform</code> class transforms between two nonlinear coordinate systems.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/transform.h">transform.h</a>&gt; </p>
<p> Inherits <code>sc::RefCount</code>. </p>
<p> Inherited by <code>sc::IdentityTransform</code>.</p>
<h3>Public Member Functions</h3>
<p> virtual void <code>transform_coordinates</code> (const <code>RefSCVector</code> &amp;x)=0<br />
 <i></i><code>Transform</code> the coordinates.<br />
 virtual void <code>transform_gradient</code> (const <code>RefSCVector</code> &amp;g)<br />
 <i></i><code>Transform</code> the gradient at a <code>point</code> in the new coordinate system.<br />
 virtual void <code>transform_hessian</code> (const <code>RefSymmSCMatrix</code> &amp;h)<br />
 <i></i><code>Transform</code> the hessian to the new coordinate system.<br />
 virtual void <code>transform_ihessian</code> (const <code>RefSymmSCMatrix</code> &amp;ih)<br />
 <i></i><code>Transform</code> the inverse of the hessian.</p>
<h3>Protected Attributes</h3>
<p> <code>RefSCMatrix</code> <code>linear_transform_</code> </p>
<h2>Detailed Description</h2>
<p> The <code>NonlinearTransform</code> class transforms between two nonlinear coordinate systems. </p>
<p> It is needed when a change of coordinates occurs in the middle of an optimization.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::NonlinearTransform::transform_gradient (const <code>RefSCVector</code> &amp; g) [virtual]</h3>
<p> <code>Transform</code> the gradient at a <code>point</code> in the new coordinate system. transform_coordinates must be called first to give the <code>point</code>. </p>
<p> Reimplemented in <code>sc::IdentityTransform</code>.</p>
<h3>virtual void sc::NonlinearTransform::transform_hessian (const <code>RefSymmSCMatrix</code> &amp; h) [virtual]</h3>
<p> <code>Transform</code> the hessian to the new coordinate system. transform_gradient must be called first to initialize this routine. </p>
<p> Reimplemented in <code>sc::IdentityTransform</code>.</p>
<h3>virtual void sc::NonlinearTransform::transform_ihessian (const <code>RefSymmSCMatrix</code> &amp; ih) [virtual]</h3>
<p> <code>Transform</code> the inverse of the hessian. transform_gradient must be called first to initialize this routine. </p>
<p> Reimplemented in <code>sc::IdentityTransform</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
