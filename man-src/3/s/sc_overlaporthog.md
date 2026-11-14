---
title: "sc_overlaporthog(3)"
name: "sc_overlaporthog"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_overlaporthog/"
description: "sc::OverlapOrthog –"
---

<p>sc::OverlapOrthog &#8211; </p>
<p> This class computes the orthogonalizing transform for a basis set.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;orthog.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Types</h3>
<pre><code>enum OrthogMethod { Symmetric = 1, Canonical = 2, GramSchmidt = 3 }


An enum for the types of orthogonalization.



Public Member Functions</code></pre>
<p> <code>OverlapOrthog</code> (<code>OrthogMethod</code> method, const <code>RefSymmSCMatrix</code> &amp;overlap, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;result_kit, double lindep_tolerance, int debug=0) </p>
<p> <code>OverlapOrthog</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>reinit</code> (<code>OrthogMethod</code> method, const <code>RefSymmSCMatrix</code> &amp;overlap, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;result_kit, double lindep_tolerance, int debug=0) </p>
<p> double <code>min_orthog_res</code> () const </p>
<p> double <code>max_orthog_res</code> () const </p>
<p> <code>Ref</code>&lt; <code>OverlapOrthog</code> &gt; <code>copy</code> () const </p>
<p> <code>OrthogMethod</code> <code>orthog_method</code> () const<br />
 <i>Returns the orthogonalization method. </i><br />
 double <code>lindep_tol</code> () const<br />
 <i>Returns the tolerance for linear dependencies. </i><br />
 <code>RefSCMatrix</code> <code>basis_to_orthog_basis</code> ()<br />
 <i>Returns a matrix which does the requested transform from a basis to an orthogonal basis. </i><br />
 <code>RefSCMatrix</code> <code>basis_to_orthog_basis_inverse</code> ()<br />
 <i>Returns the inverse of the transformation returned by basis_to_orthog_basis. </i><br />
 <code>RefSCDimension</code> <code>dim</code> () </p>
<p> <code>RefSCDimension</code> <code>orthog_dim</code> () </p>
<p> int <code>nlindep</code> ()<br />
 <i>Returns the number of linearly dependent functions eliminated from the orthogonal basis. </i></p>
<h2>Detailed Description</h2>
<p>This class computes the orthogonalizing transform for a basis set.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefSCMatrix</code> sc::OverlapOrthog::basis_to_orthog_basis ()</h3>
<p>Returns a matrix which does the requested transform from a basis to an orthogonal basis. This could be either the symmetric or canonical orthogonalization matrix. The row dimension is the basis dimension and the column dimension is orthogonal basis dimension. An operator $O$ in the orthogonal basis is given by $X O X^T$ where $X$ is the return value of this function.</p>
<h3>void sc::OverlapOrthog::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
