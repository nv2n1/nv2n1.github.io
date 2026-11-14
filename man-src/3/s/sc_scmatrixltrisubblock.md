---
title: "sc_scmatrixltrisubblock(3)"
name: "sc_scmatrixltrisubblock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixltrisubblock/"
description: "sc::SCMatrixLTriSubBlock –"
---

<p>sc::SCMatrixLTriSubBlock &#8211; </p>
<p> The <code>SCMatrixLTriSubBlock</code> describes a triangular subblock of a matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;block.h&gt;</code></pre>
<p> Inherits <code>sc::SCMatrixBlock</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SCMatrixLTriSubBlock</code> (int is, int ie, int js, int je, double *data) </p>
<p> <code>SCMatrixLTriSubBlock</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>process</code> (<code>SCElementOp</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp2</code> *, <code>SCMatrixBlock</code> *) </p>
<p> void <code>process</code> (<code>SCElementOp3</code> *, <code>SCMatrixBlock</code> *, <code>SCMatrixBlock</code> *)</p>
<h3>Public Attributes</h3>
<pre><code>int istart



int iend



int jstart



int jend



double * data</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SCMatrixLTriSubBlock</code> describes a triangular subblock of a matrix. </p>
<p> The following bit of code illustrates the data layout: fill(double **matrix, SCMatrixLTriSubBlock &amp;b) { int offset=(b.istart*(b.istart+1)&gt;&gt;1) + b.jstart; for (int i=b.start; i&lt;b.end; i++) { for (int j=b.start; j&lt;=i &amp;&amp; j&lt;b.jend; j++,offset++) { matrix[i][j] = b.data[offset]; } if (j&gt;i) offset += b.istart; else offset += i + b.jstart &#8211; b.jend; } }</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SCMatrixLTriSubBlock::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SCMatrixBlock</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
