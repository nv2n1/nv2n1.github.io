---
title: "sc_distscvector(3)"
name: "sc_distscvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distscvector/"
description: "sc::DistSCVector –"
---

<p>sc::DistSCVector &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCVector</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DistSCVector (const RefSCDimension &amp;, DistSCMatrixKit *)



void assign_p (const double *)



void assign_v (SCVector *a)



void convert (double *v) const


Assign v[i] to element i for all i.


void convert (SCVector *)



void set_element (int, double)


Set element i to val.


void accumulate_element (int, double)


Add val to element i.


double get_element (int) const


Return the value of element i.


void accumulate (const SCVector *)



void accumulate (const SCMatrix *m)


Sum m into this. One of m's dimensions must be 1.


double scalar_product (SCVector *)



void accumulate_product_rv (SCMatrix *, SCVector *)



void element_op (const Ref&lt; SCElementOp &gt; &amp;)


Perform the element operation op on each element of this.


void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SCVector *)



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SCVector *, SCVector *)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this vector.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this vector.


Ref&lt; DistSCMatrixKit &gt; skit ()



Protected Member Functions
void init_blocklist ()



double * find_element (int i) const



int element_to_node (int i) const



int block_to_node (int) const



Ref&lt; SCMatrixBlock &gt; block_to_block (int) const



void error (const char *)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>blocklist</code></p>
<h3>Friends</h3>
<p>class <code>DistSCMatrix</code> </p>
<p> class <code>DistSymmSCMatrix</code> </p>
<p> class <code>DistDiagSCMatrix</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::DistSCVector::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this vector. Only one iterator is allowed for a matrix is it has Accum or Write access is allowed. Multiple Read iterators are permitted. </p>
<p> Implements <code>sc::SCVector</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
