---
title: "sc_scmatrixdiagsubblock(3)"
name: "sc_scmatrixdiagsubblock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixdiagsubblock/"
description: "sc::SCMatrixDiagSubBlock –"
---

<p>sc::SCMatrixDiagSubBlock &#8211; </p>
<p> The <code>SCMatrixDiagSubBlock</code> describes a diagonal subblock of a matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;block.h&gt;</code></pre>
<p> Inherits <code>sc::SCMatrixBlock</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixDiagSubBlock</code> (int istart, int iend, int jstart, int offset, double *data) </p>
<p> <code>SCMatrixDiagSubBlock</code> (int istart, int iend, int offset, double *data) </p>
<p> <code>SCMatrixDiagSubBlock</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>process</code> (<code>SCElementOp</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp2</code> *, <code>SCMatrixBlock</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp3</code> *, <code>SCMatrixBlock</code> *, <code>SCMatrixBlock</code> *)</p>
<h3>Public Attributes</h3>
<pre><code>int istart



int jstart



int iend



int offset



double * data</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCMatrixDiagSubBlock</code> describes a diagonal subblock of a matrix. </p>
<p> The following bit of code illustrates the data layout: fill(double **matrix, SCMatrixDiagSubBlock &amp;b) { int i,j,offset=b.offset; for (i=b.istart,j=b.jstart; i&lt;b.iend; i++,j++,offset++) { matrix[i][j] = b.data[offset]; } }</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SCMatrixDiagSubBlock::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCMatrixBlock</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
