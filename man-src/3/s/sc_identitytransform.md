---
title: "sc_identitytransform(3)"
name: "sc_identitytransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_identitytransform/"
description: "sc::IdentityTransform –"
---

<p>sc::IdentityTransform &#8211; </p>
<p> The <code>IdentityTransform</code> is a special case of <code>NonlinearTransform</code> were no transformation takes place.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;transform.h&gt;</code></pre>
<p> Inherits <code>sc::NonlinearTransform</code>.</p>
<h3>Public Member Functions</h3>
<p>void <code>transform_coordinates</code> (const <code>RefSCVector</code> &amp;x)<br />
 <i>These override the tranformation members of </i><code>NonlinearTransform</code> and do nothing.<br />
 void <code>transform_gradient</code> (const <code>RefSCVector</code> &amp;g)<br />
 <i></i><code>Transform</code> the gradient at a <code>point</code> in the new coordinate system.<br />
 void <code>transform_hessian</code> (const <code>RefSymmSCMatrix</code> &amp;h)<br />
 <i></i><code>Transform</code> the hessian to the new coordinate system.<br />
 void <code>transform_ihessian</code> (const <code>RefSymmSCMatrix</code> &amp;ih)<br />
 <i></i><code>Transform</code> the inverse of the hessian.</p>
<h2>Detailed Description</h2>
<p>The <code>IdentityTransform</code> is a special case of <code>NonlinearTransform</code> were no transformation takes place.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::IdentityTransform::transform_coordinates (const <code>RefSCVector</code> &amp; x) [virtual]</h3>
<p>These override the tranformation members of <code>NonlinearTransform</code> and do nothing. </p>
<p> Implements <code>sc::NonlinearTransform</code>.</p>
<h3>void sc::IdentityTransform::transform_gradient (const <code>RefSCVector</code> &amp; g) [virtual]</h3>
<p><code>Transform</code> the gradient at a <code>point</code> in the new coordinate system. transform_coordinates must be called first to give the <code>point</code>. </p>
<p> Reimplemented from <code>sc::NonlinearTransform</code>.</p>
<h3>void sc::IdentityTransform::transform_hessian (const <code>RefSymmSCMatrix</code> &amp; h) [virtual]</h3>
<p><code>Transform</code> the hessian to the new coordinate system. transform_gradient must be called first to initialize this routine. </p>
<p> Reimplemented from <code>sc::NonlinearTransform</code>.</p>
<h3>void sc::IdentityTransform::transform_ihessian (const <code>RefSymmSCMatrix</code> &amp; ih) [virtual]</h3>
<p><code>Transform</code> the inverse of the hessian. transform_gradient must be called first to initialize this routine. </p>
<p> Reimplemented from <code>sc::NonlinearTransform</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
