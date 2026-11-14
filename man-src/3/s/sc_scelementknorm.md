---
title: "sc_scelementknorm(3)"
name: "sc_scelementknorm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scelementknorm/"
description: "sc::SCElementKNorm –"
---

<p>sc::SCElementKNorm &#8211; </p>
<p> Computed k-norm of matrix.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;elemop.h&gt;</code></pre>
<p> Inherits <code>sc::SCElementOp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SCElementKNorm (double k=2.0)


by default compute 2-norm


SCElementKNorm (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void process (SCMatrixBlockIter &amp;)


This is the fallback routine to process blocks and is called by process_spec members that are not overridden.


int has_collect ()


If duplicates of the SCElementOp exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a MessageGrp reference after all of the blocks have been processed.


void defer_collect (int)



void collect (const Ref&lt; MessageGrp &gt; &amp;)



void collect (const Ref&lt; SCElementOp &gt; &amp;)



double result ()



void init ()</code></pre>
<h2>Detailed Description</h2>
<p>Computed k-norm of matrix.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::SCElementKNorm::has_collect () [virtual]</h3>
<p>If duplicates of the <code>SCElementOp</code> exist (that is, there is more than one node), then if has_collect returns nonzero then collect is called with a <code>MessageGrp</code> reference after all of the blocks have been processed. The default return value of has_collect is 0 and collect&#8217;s default action is do nothing. If defer_collect member is called with nonzero, collect will do nothing (this is only used by the blocked matrices). </p>
<p> Reimplemented from <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementKNorm::process (<code>SCMatrixBlockIter</code> &amp;) [virtual]</h3>
<p>This is the fallback routine to process blocks and is called by process_spec members that are not overridden. </p>
<p> Implements <code>sc::SCElementOp</code>.</p>
<h3>void sc::SCElementKNorm::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
