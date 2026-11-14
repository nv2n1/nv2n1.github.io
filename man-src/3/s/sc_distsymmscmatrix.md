---
title: "sc_distsymmscmatrix(3)"
name: "sc_distsymmscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distsymmscmatrix/"
description: "sc::DistSymmSCMatrix –"
---

<p>sc::DistSymmSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SymmSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DistSymmSCMatrix</code> (const <code>RefSCDimension</code> &amp;, <code>DistSCMatrixKit</code> *) </p>
<p> double <code>get_element</code> (int, int) const<br />
 <i>Return or modify an element. </i><br />
 void <code>set_element</code> (int, int, double) </p>
<p> void <code>accumulate_element</code> (int, int, double) </p>
<p> <code>SCMatrix</code> * <code>get_subblock</code> (int, int, int, int)<br />
 <i>Return a subblock of this. </i><br />
 <code>SymmSCMatrix</code> * <code>get_subblock</code> (int, int) </p>
<p> void <code>assign_subblock</code> (<code>SCMatrix</code> *, int, int, int, int)<br />
 <i>Assign m to a subblock of this. </i><br />
 void <code>assign_subblock</code> (<code>SymmSCMatrix</code> *, int, int) </p>
<p> void <code>accumulate_subblock</code> (<code>SCMatrix</code> *, int, int, int, int)<br />
 <i>Sum m into a subblock of this. </i><br />
 void <code>accumulate_subblock</code> (<code>SymmSCMatrix</code> *, int, int) </p>
<p> <code>SCVector</code> * <code>get_row</code> (int i)<br />
 <i>Return a row of this. </i><br />
 void <code>assign_row</code> (<code>SCVector</code> *v, int i)<br />
 <i>Assign v to a row of this. </i><br />
 void <code>accumulate_row</code> (<code>SCVector</code> *v, int i)<br />
 <i>Sum v to a row of this. </i><br />
 void <code>accumulate_product_rr</code> (<code>SCMatrix</code> *, <code>SCMatrix</code> *) </p>
<p> void <code>accumulate</code> (const <code>SymmSCMatrix</code> *) </p>
<p> double <code>invert_this</code> ()<br />
 <i>Invert this. </i><br />
 double <code>solve_this</code> (<code>SCVector</code> *) </p>
<p> double <code>trace</code> ()<br />
 <i>Return the trace. </i><br />
 double <code>determ_this</code> ()<br />
 <i>Return the determinant of this. this is overwritten. </i><br />
 void <code>gen_invert_this</code> () </p>
<p> void <code>diagonalize</code> (<code>DiagSCMatrix</code> *, <code>SCMatrix</code> *)<br />
 <i>Diagonalize this, placing the eigenvalues in d and the eigenvectors in m. </i><br />
 void <code>accumulate_symmetric_sum</code> (<code>SCMatrix</code> *)<br />
 <i>Sum into this the products of various vectors or matrices. </i><br />
 void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp</code> &gt; &amp;)<br />
 <i>Perform the element operation op on each element of this. </i><br />
 void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp2</code> &gt; &amp;, <code>SymmSCMatrix</code> *) </p>
<p> void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp3</code> &gt; &amp;, <code>SymmSCMatrix</code> *, <code>SymmSCMatrix</code> *) </p>
<p> virtual void <code>convert_accumulate</code> (<code>SymmSCMatrix</code> *) </p>
<p> <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; <code>local_blocks</code> (SCMatrixSubblockIter::Access)<br />
 <i>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </i><br />
 <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; <code>all_blocks</code> (SCMatrixSubblockIter::Access)<br />
 <i>Returns iterators for the all blocks used in this matrix. </i><br />
 <code>Ref</code>&lt; <code>DistSCMatrixKit</code> &gt; <code>skit</code> ()</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_blocklist ()



double * find_element (int i, int j) const



int element_to_node (int i, int j) const



int block_to_node (int, int) const



Ref&lt; SCMatrixBlock &gt; block_to_block (int, int) const



void error (const char *msg)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>blocklist</code></p>
<h3>Friends</h3>
<p>class <code>DistSCMatrix</code> </p>
<p> class <code>DistDiagSCMatrix</code> </p>
<p> class <code>DistSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3>void sc::DistSymmSCMatrix::diagonalize (<code>DiagSCMatrix</code> * d, <code>SCMatrix</code> * m) [virtual]</h3>
<p>Diagonalize this, placing the eigenvalues in d and the eigenvectors in m. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h3><code>SCMatrix</code>* sc::DistSymmSCMatrix::get_subblock (int br, int er, int bc, int ec) [virtual]</h3>
<p>Return a subblock of this. The subblock is defined as the rows starting at br and ending at er, and the columns beginning at bc and ending at ec. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::DistSymmSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
