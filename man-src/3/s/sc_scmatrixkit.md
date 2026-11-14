---
title: "sc_scmatrixkit(3)"
name: "sc_scmatrixkit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixkit/"
description: "sc::SCMatrixKit –"
---

<p>sc::SCMatrixKit &#8211; </p>
<p> The <code>SCMatrixKit</code> abstract class acts as a factory for producing matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;abstract.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::BlockedSCMatrixKit</code>, <code>sc::DistSCMatrixKit</code>, <code>sc::LocalSCMatrixKit</code>, and <code>sc::ReplSCMatrixKit</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCMatrixKit (const Ref&lt; KeyVal &gt; &amp;)



Ref&lt; MessageGrp &gt; messagegrp () const



virtual SCMatrix * matrix (const RefSCDimension &amp;, const RefSCDimension &amp;)=0


Given the dimensions, create matrices or vectors.


virtual SymmSCMatrix * symmmatrix (const RefSCDimension &amp;)=0



virtual DiagSCMatrix * diagmatrix (const RefSCDimension &amp;)=0



virtual SCVector * vector (const RefSCDimension &amp;)=0



SCMatrix * restore_matrix (StateIn &amp;, const RefSCDimension &amp;, const RefSCDimension &amp;)


Given the dimensions and a StateIn object, restore matrices or vectors.


SymmSCMatrix * restore_symmmatrix (StateIn &amp;, const RefSCDimension &amp;)



DiagSCMatrix * restore_diagmatrix (StateIn &amp;, const RefSCDimension &amp;)



SCVector * restore_vector (StateIn &amp;, const RefSCDimension &amp;)



Static Public Member Functions
static SCMatrixKit * default_matrixkit ()


This returns a LocalSCMatrixKit, unless the default has been changed with set_default_matrixkit.


static void set_default_matrixkit (const Ref&lt; SCMatrixKit &gt; &amp;)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>grp_</code></p>
<h2>Detailed Description</h2>
<p>The <code>SCMatrixKit</code> abstract class acts as a factory for producing matrices. </p>
<p> By using one of these, the program makes sure that all of the matrices are consistent.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>SCMatrixKit</code>* sc::SCMatrixKit::default_matrixkit () [static]</h3>
<p>This returns a <code>LocalSCMatrixKit</code>, unless the default has been changed with set_default_matrixkit.</p>
<h3><code>SCMatrix</code>* sc::SCMatrixKit::restore_matrix (<code>StateIn</code> &amp;, const <code>RefSCDimension</code> &amp;, const <code>RefSCDimension</code> &amp;)</h3>
<p>Given the dimensions and a <code>StateIn</code> object, restore matrices or vectors.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
