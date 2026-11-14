---
title: "sc_localscvector(3)"
name: "sc_localscvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_localscvector/"
description: "sc::LocalSCVector –"
---

<p>sc::LocalSCVector &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCVector</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LocalSCVector (const RefSCDimension &amp;, LocalSCMatrixKit *)



void assign_val (double)


Overridden to implement the assign functions.


void assign_v (SCVector *)



void assign_p (const double *)



void set_element (int, double)


Set element i to val.


void accumulate_element (int, double)


Add val to element i.


double get_element (int) const


Return the value of element i.


void accumulate_product_sv (SymmSCMatrix *, SCVector *)



void accumulate_product_rv (SCMatrix *, SCVector *)



void accumulate (const SCVector *)



void accumulate (const SCMatrix *)


Sum m into this. One of m's dimensions must be 1.


double scalar_product (SCVector *)



void element_op (const Ref&lt; SCElementOp &gt; &amp;)


Perform the element operation op on each element of this.


void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SCVector *)



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SCVector *, SCVector *)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



double * get_data ()



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this vector.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this vector.



Friends</code></pre>
<p> class <code>LocalSCMatrix</code> </p>
<p> class <code>LocalSymmSCMatrix</code> </p>
<p> class <code>LocalDiagSCMatrix</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::LocalSCVector::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this vector. Only one iterator is allowed for a matrix is it has Accum or Write access is allowed. Multiple Read iterators are permitted. </p>
<p> Implements <code>sc::SCVector</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
