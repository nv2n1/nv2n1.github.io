---
title: "sc_scmatrixblock(3)"
name: "sc_scmatrixblock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixblock/"
description: "sc::SCMatrixBlock –"
---

<p>sc::SCMatrixBlock &#8211; </p>
<p> <code>SCMatrixBlock</code> is the base clase for all types of blocks that comprise matrices and vectors.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;block.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::SCMatrixDiagBlock</code>, <code>sc::SCMatrixDiagSubBlock</code>, <code>sc::SCMatrixLTriBlock</code>, <code>sc::SCMatrixLTriSubBlock</code>, <code>sc::SCMatrixRectBlock</code>, <code>sc::SCMatrixRectSubBlock</code>, <code>sc::SCVectorSimpleBlock</code>, and <code>sc::SCVectorSimpleSubBlock</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCMatrixBlock (StateIn &amp;s)



void save_data_state (StateOut &amp;s)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual SCMatrixBlock * deepcopy () const


Return of copy of this.


virtual double * dat ()


Return a pointer to the block's data and the number of elements in the block.


virtual int ndat () const



virtual void process (SCElementOp *)=0



virtual void process (SCElementOp2 *, SCMatrixBlock *)=0



virtual void process (SCElementOp3 *, SCMatrixBlock *, SCMatrixBlock *)=0



Public Attributes
int blocki



int blockj</code></pre>
<h2>Detailed Description</h2>
<p><code>SCMatrixBlock</code> is the base clase for all types of blocks that comprise matrices and vectors.</p>
<h2>Member Function Documentation</h2>
<h3>virtual double* sc::SCMatrixBlock::dat () [virtual]</h3>
<p>Return a pointer to the block&#8217;s data and the number of elements in the block. Some blocks cannot provide this information and a runtime error will be generated if these members are called. These routines are only used internally in the matrix library. </p>
<p> Reimplemented in <code>sc::SCVectorSimpleBlock</code>, <code>sc::SCMatrixRectBlock</code>, <code>sc::SCMatrixLTriBlock</code>, and <code>sc::SCMatrixDiagBlock</code>.</p>
<h3>virtual <code>SCMatrixBlock</code>* sc::SCMatrixBlock::deepcopy () const [virtual]</h3>
<p>Return of copy of this. A runtime error will be generated for blocks that cannot do a deepcopy. These routines are only used internally in the matrix library. </p>
<p> Reimplemented in <code>sc::SCVectorSimpleBlock</code>, <code>sc::SCMatrixRectBlock</code>, <code>sc::SCMatrixLTriBlock</code>, and <code>sc::SCMatrixDiagBlock</code>.</p>
<h3>void sc::SCMatrixBlock::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::SCVectorSimpleBlock</code>, <code>sc::SCVectorSimpleSubBlock</code>, <code>sc::SCMatrixRectBlock</code>, <code>sc::SCMatrixRectSubBlock</code>, <code>sc::SCMatrixLTriBlock</code>, <code>sc::SCMatrixLTriSubBlock</code>, <code>sc::SCMatrixDiagBlock</code>, and <code>sc::SCMatrixDiagSubBlock</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
