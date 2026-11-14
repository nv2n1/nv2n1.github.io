---
title: "sc_refscvector(3)"
name: "sc_refscvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refscvector/"
description: "sc::RefSCVector –"
---

<p>sc::RefSCVector &#8211; </p>
<p> The <code>RefSCVector</code> class is a smart pointer to an <code>SCVector</code> specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;matrix.h&gt;</code></pre>
<p> Inherits <code>Ref&lt; SCVector &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RefSCVector</code> ()<br />
 <i>Initializes the vector pointer to 0. </i><br />
 <code>RefSCVector</code> (const <code>RefSCVector</code> &amp;v)<br />
 <i>Make this and v refer to the same </i><code>SCVector</code>.<br />
 <code>RefSCVector</code> (<code>SCVector</code> *v)<br />
 <i>Make this refer to v. </i><br />
 <code>RefSCVector</code> &amp; <code>operator=</code> (<code>SCVector</code> *v)<br />
 <i>Make this refer to v. </i><br />
 <code>RefSCVector</code> &amp; <code>operator=</code> (const <code>RefSCVector</code> &amp;v)<br />
 <i>Make this and v refer to the same </i><code>SCVector</code>.<br />
 <code>RefSCVector</code> (const <code>RefSCDimension</code> &amp;dim, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)<br />
 <i>Create a vector with dimension dim. </i><br />
 <code>SCVectordouble</code> <code>operator()</code> (int) const<br />
 <i>Return an l-value that can be used to assign or retrieve an element. </i><br />
 <code>SCVectordouble</code> <code>operator[]</code> (int) const<br />
 <i>Return an l-value that can be used to assign or retrieve an element. </i><br />
 <code>RefSCVector</code> <code>operator+</code> (const <code>RefSCVector</code> &amp;a) const<br />
 <i>Add two vectors. </i><br />
 <code>RefSCVector</code> <code>operator-</code> (const <code>RefSCVector</code> &amp;a) const<br />
 <i>Subtract two vectors. </i><br />
 <code>RefSCVector</code> <code>operator*</code> (double) const<br />
 <i>Scale a vector. </i><br />
 <code>RefSCMatrix</code> <code>outer_product</code> (const <code>RefSCVector</code> &amp;v) const<br />
 <i>Return the outer product between this and v. </i><br />
 <code>RefSymmSCMatrix</code> <code>symmetric_outer_product</code> () const<br />
 <i>The outer product of this with itself is a symmetric matrix. </i><br />
 void <code>set_element</code> (int i, double val) const </p>
<p> void <code>accumulate_element</code> (int i, double val) const </p>
<p> double <code>get_element</code> (int) const </p>
<p> int <code>n</code> () const </p>
<p> <code>RefSCDimension</code> <code>dim</code> () const </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>kit</code> () const </p>
<p> <code>RefSCVector</code> <code>clone</code> () const </p>
<p> <code>RefSCVector</code> <code>copy</code> () const </p>
<p> double <code>maxabs</code> () const </p>
<p> double <code>scalar_product</code> (const <code>RefSCVector</code> &amp;) const </p>
<p> double <code>dot</code> (const <code>RefSCVector</code> &amp;) const </p>
<p> void <code>normalize</code> () const </p>
<p> void <code>randomize</code> () const </p>
<p> void <code>assign</code> (const <code>RefSCVector</code> &amp;v) const </p>
<p> void <code>assign</code> (double val) const </p>
<p> void <code>assign</code> (const double *v) const </p>
<p> void <code>convert</code> (double *) const </p>
<p> void <code>scale</code> (double val) const </p>
<p> void <code>accumulate</code> (const <code>RefSCVector</code> &amp;v) const </p>
<p> void <code>accumulate_product</code> (const <code>RefSymmSCMatrix</code> &amp;, const <code>RefSCVector</code> &amp;) </p>
<p> void <code>accumulate_product</code> (const <code>RefSCMatrix</code> &amp;, const <code>RefSCVector</code> &amp;) </p>
<p> void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp</code> &gt; &amp;op) const </p>
<p> void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp2</code> &gt; &amp;, const <code>RefSCVector</code> &amp;) const </p>
<p> void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp3</code> &gt; &amp;, const <code>RefSCVector</code> &amp;, const <code>RefSCVector</code> &amp;) const </p>
<p> void <code>print</code> (std::ostream &amp;out) const </p>
<p> void <code>print</code> (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int precision=10) const </p>
<p> void <code>save</code> (<code>StateOut</code> &amp;) </p>
<p> void <code>restore</code> (<code>StateIn</code> &amp;)<br />
 <i>Restores the matrix from </i><code>StateIn</code> object. The vector must have been initialized already.</p>
<h2>Detailed Description</h2>
<p>The <code>RefSCVector</code> class is a smart pointer to an <code>SCVector</code> specialization.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RefSCVector::RefSCVector ()</h3>
<p>Initializes the vector pointer to 0. The reference must be initialized before it is used.</p>
<h3>sc::RefSCVector::RefSCVector (const <code>RefSCDimension</code> &amp; dim, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)</h3>
<p>Create a vector with dimension dim. The data values are undefined.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
