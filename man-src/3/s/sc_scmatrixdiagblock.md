---
title: "sc_scmatrixdiagblock(3)"
name: "sc_scmatrixdiagblock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixdiagblock/"
description: "sc::SCMatrixDiagBlock –"
---

<p>sc::SCMatrixDiagBlock &#8211; </p>
<p> The <code>SCMatrixDiagBlock</code> describes a diagonal piece of a matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;block.h&gt;</code></pre>
<p> Inherits <code>sc::SCMatrixBlock</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixDiagBlock</code> (int istart, int iend, int jstart) </p>
<p> <code>SCMatrixDiagBlock</code> (int istart, int iend) </p>
<p> <code>SCMatrixDiagBlock</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 <code>SCMatrixBlock</code> * <code>deepcopy</code> () const<br />
 <i>Return of copy of this. </i><br />
 void <code>process</code> (<code>SCElementOp</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp2</code> *, <code>SCMatrixBlock</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp3</code> *, <code>SCMatrixBlock</code> *, <code>SCMatrixBlock</code> *) </p>
<p> double * <code>dat</code> ()<br />
 <i>Return a pointer to the block&#8217;s data and the number of elements in the block. </i><br />
 int <code>ndat</code> () const</p>
<h3>Public Attributes</h3>
<pre><code>int istart



int jstart



int iend



double * data</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCMatrixDiagBlock</code> describes a diagonal piece of a matrix. </p>
<p> The following bit of code illustrates the data layout: fill(double **matrix, SCMatrixDiagBlock &amp;b) { int i,j,offset=0; for (i=b.istart,j=b.jstart; i&lt;b.iend; i++,j++,offset++) { matrix[i][j] = b.data[offset]; } }</p>
<h2>Member Function Documentation</h2>
<h3>double* sc::SCMatrixDiagBlock::dat () [virtual]</h3>
<p>Return a pointer to the block&#8217;s data and the number of elements in the block. Some blocks cannot provide this information and a runtime error will be generated if these members are called. These routines are only used internally in the matrix library. </p>
<p> Reimplemented from <code>sc::SCMatrixBlock</code>.</p>
<h3><code>SCMatrixBlock</code>* sc::SCMatrixDiagBlock::deepcopy () const [virtual]</h3>
<p>Return of copy of this. A runtime error will be generated for blocks that cannot do a deepcopy. These routines are only used internally in the matrix library. </p>
<p> Reimplemented from <code>sc::SCMatrixBlock</code>.</p>
<h3>void sc::SCMatrixDiagBlock::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCMatrixBlock</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
