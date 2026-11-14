---
title: "sc_diagscmatrix(3)"
name: "sc_diagscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_diagscmatrix/"
description: "sc::DiagSCMatrix –"
---

<p>sc::DiagSCMatrix &#8211; </p>
<p> The <code>SymmSCMatrix</code> class is the abstract base class for diagonal double valued matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;abstract.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::BlockedDiagSCMatrix</code>, <code>sc::DistDiagSCMatrix</code>, <code>sc::LocalDiagSCMatrix</code>, and <code>sc::ReplDiagSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DiagSCMatrix (const RefSCDimension &amp;, SCMatrixKit *)



Ref&lt; SCMatrixKit &gt; kit () const


Return the SCMatrixKit used to create this object.


virtual void save (StateOut &amp;)


Save and restore this in an implementation independent way.


virtual void restore (StateIn &amp;)



virtual double maxabs () const


Return the maximum absolute value element of this vector.


virtual void randomize ()


Assign each element to a random number between -1 and 1.


void assign (double val)


Set all elements to val.


void assign (const double *p)


Assign element i, i to m[i].


void assign (DiagSCMatrix *d_a)


Make this have the same elements as m.


virtual void assign_val (double val)


Overridden to implement the assign members.


virtual void assign_p (const double *)



virtual void assign_d (DiagSCMatrix *)



virtual void convert (double *) const


Like the assign member, but this writes values to the argument.


virtual void convert (DiagSCMatrix *)


Convert an SCDiagSCMatrix of a different specialization to this specialization and possibly accumulate the data.


virtual void convert_accumulate (DiagSCMatrix *)



virtual void scale (double)


Multiply all elements by val.


int n () const


Return the dimension.


virtual DiagSCMatrix * copy ()


Return a matrix with the same dimension and same elements.


virtual DiagSCMatrix * clone ()


Return a matrix with the same dimension but uninitialized memory.


RefSCDimension dim () const


Return the dimension.


virtual double get_element (int) const =0


Return or modify an element.


virtual void set_element (int, double)=0



virtual void accumulate_element (int, double)=0



virtual void accumulate (const DiagSCMatrix *m)=0


Sum m into this.


virtual double trace ()=0


Return the trace.


virtual double determ_this ()=0


Return the determinant of this. this is overwritten.


virtual double invert_this ()=0


Invert this.


virtual void gen_invert_this ()=0


Do a generalized inversion of this.


virtual void element_op (const Ref&lt; SCElementOp &gt; &amp;)=0


Perform the element operation op on each element of this.


virtual void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, DiagSCMatrix *)=0



virtual void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, DiagSCMatrix *, DiagSCMatrix *)=0



void print (std::ostream &amp;o=ExEnv::out0()) const


Print out the matrix.


void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



virtual void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



Ref&lt; MessageGrp &gt; messagegrp () const


Returns the message group used by the matrix kit.


virtual Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


virtual Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the all blocks used in this matrix.



Protected Attributes</code></pre>
<p> <code>RefSCDimension</code> <code>d</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>kit_</code></p>
<h2>Detailed Description</h2>
<p>The <code>SymmSCMatrix</code> class is the abstract base class for diagonal double valued matrices.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::DiagSCMatrix::assign (<code>DiagSCMatrix</code> * d_a) [inline]</h3>
<p>Make this have the same elements as m. The dimensions must match.</p>
<h3>virtual void sc::DiagSCMatrix::convert (<code>DiagSCMatrix</code> *) [virtual]</h3>
<p>Convert an SCDiagSCMatrix of a different specialization to this specialization and possibly accumulate the data.</p>
<h3>virtual <code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::DiagSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [pure virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implemented in <code>sc::BlockedDiagSCMatrix</code>, <code>sc::DistDiagSCMatrix</code>, <code>sc::LocalDiagSCMatrix</code>, and <code>sc::ReplDiagSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
