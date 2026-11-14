---
title: "sc_scvector(3)"
name: "sc_scvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scvector/"
description: "sc::SCVector –"
---

<p>sc::SCVector &#8211; </p>
<p> The <code>SCVector</code> class is the abstract base class for double valued vectors.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;abstract.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::BlockedSCVector</code>, <code>sc::DistSCVector</code>, <code>sc::LocalSCVector</code>, and <code>sc::ReplSCVector</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCVector (const RefSCDimension &amp;, SCMatrixKit *)



virtual void save (StateOut &amp;)


Save and restore this in an implementation independent way.


virtual void restore (StateIn &amp;)



Ref&lt; SCMatrixKit &gt; kit () const


Return the SCMatrixKit used to create this object.


virtual SCVector * copy ()


Return a vector with the same dimension and same elements.


virtual SCVector * clone ()


Return a vector with the same dimension but uninitialized memory.


int n () const


Return the length of the vector.


virtual double maxabs () const


Return the maximum absolute value element of this vector.


virtual void normalize ()


Normalize this.


virtual void randomize ()


Assign each element to a random number between -1 and 1.


void assign (double val)


Assign all elements of this to val.


void assign (const double *v)


Assign element i to v[i] for all i.


void assign (SCVector *v)


Make this have the same elements as v.


virtual void assign_val (double val)


Overridden to implement the assign functions.


virtual void assign_p (const double *v)



virtual void assign_v (SCVector *v)



virtual void convert (double *v) const


Assign v[i] to element i for all i.


virtual void convert (SCVector *)


Convert an SCVector of a different specialization to this specialization and possibly accumulate the data.


virtual void convert_accumulate (SCVector *)



virtual void scale (double val)


Multiply each element by val.


RefSCDimension dim () const


Return the RefSCDimension corresponding to this vector.


virtual void set_element (int i, double val)=0


Set element i to val.


virtual void accumulate_element (int, double)=0


Add val to element i.


virtual double get_element (int i) const =0


Return the value of element i.


void accumulate_product (SymmSCMatrix *m, SCVector *v)


Sum the result of m times v into this.


void accumulate_product (SCMatrix *m, SCVector *v)



virtual void accumulate_product_sv (SymmSCMatrix *m, SCVector *v)



virtual void accumulate_product_rv (SCMatrix *m, SCVector *v)=0



virtual void accumulate (const SCVector *v)=0


Sum v into this.


virtual void accumulate (const SCMatrix *m)=0


Sum m into this. One of m's dimensions must be 1.


virtual double scalar_product (SCVector *)=0


Return the dot product.


virtual void element_op (const Ref&lt; SCElementOp &gt; &amp;)=0


Perform the element operation op on each element of this.


virtual void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SCVector *)=0



virtual void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SCVector *, SCVector *)=0



void print (std::ostream &amp;o=ExEnv::out0()) const


Print out the vector.


void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



virtual void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const =0



Ref&lt; MessageGrp &gt; messagegrp () const


Returns the message group used by the matrix kit.


virtual Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the local (rapidly accessible) blocks used in this vector.


virtual Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the all blocks used in this vector.



Protected Attributes</code></pre>
<p> <code>RefSCDimension</code> <code>d</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>kit_</code></p>
<h2>Detailed Description</h2>
<p>The <code>SCVector</code> class is the abstract base class for double valued vectors.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SCVector::assign (<code>SCVector</code> * v) [inline]</h3>
<p>Make this have the same elements as v. The dimensions must match.</p>
<h3>virtual void sc::SCVector::convert (<code>SCVector</code> *) [virtual]</h3>
<p>Convert an <code>SCVector</code> of a different specialization to this specialization and possibly accumulate the data.</p>
<h3>virtual <code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::SCVector::local_blocks (SCMatrixSubblockIter::Access) [pure virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this vector. Only one iterator is allowed for a matrix is it has Accum or Write access is allowed. Multiple Read iterators are permitted. </p>
<p> Implemented in <code>sc::BlockedSCVector</code>, <code>sc::DistSCVector</code>, <code>sc::LocalSCVector</code>, and <code>sc::ReplSCVector</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
