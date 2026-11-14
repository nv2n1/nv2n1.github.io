---
title: "sc_r12intsacc_memorygrp(3)"
name: "sc_r12intsacc_memorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intsacc_memorygrp/"
description: "sc::R12IntsAcc_MemoryGrp –"
---

<p>sc::R12IntsAcc_MemoryGrp &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::R12IntsAcc</code>.</p>
<h3>Classes</h3>
<pre><code>struct PairBlkInfo



Public Member Functions</code></pre>
<p> <code>R12IntsAcc_MemoryGrp</code> (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;, int num_te_types, int ni, int nj, int nx, int ny) </p>
<p> <code>R12IntsAcc_MemoryGrp</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>store_memorygrp</code> (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem, int ni, const size_t blksize)<br />
 <i>Stores all pair block of integrals held in mem mem must be the same as mem_ used to construct this This is a collective operation. </i><br />
 void <code>store_pair_block</code> (int i, int j, double *ints)<br />
 <i>Stores an ij pair block of integrals (assumes the block resides locally). </i><br />
 void <code>deactivate</code> ()<br />
 <i>Done reading content &#8211; call set_localsize(0) on the associated </i><code>MemoryGrp</code> This is a collective operation.<br />
 double * <code>retrieve_pair_block</code> (int i, int j, <code>tbint_type</code> oper_type)<br />
 <i>Retrieves an ij pair block of integrals. </i><br />
 void <code>release_pair_block</code> (int i, int j, <code>tbint_type</code> oper_type)<br />
 <i>Releases an ij pair block of integrals (if needed). </i><br />
 bool <code>is_local</code> (int i, int j) const<br />
 <i>Is this block stored locally? </i><br />
 bool <code>is_avail</code> (int i, int j) const<br />
 <i>In this implementation all blocks are globally available. </i><br />
 bool <code>has_access</code> (int proc) const<br />
 <i>Does this task have access to all the integrals? </i><br />
 bool <code>can_restart</code> () const<br />
 <i>Cannot restart MemoryGrp-based accumulator. </i><br />
 int <code>ij_index</code> (int i, int j) const </p>
<p> int <code>ij_proc</code> (int i, int j) const</p>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntsAcc_MemoryGrp::deactivate () [virtual]</h3>
<p>Done reading content &#8211; call set_localsize(0) on the associated <code>MemoryGrp</code> This is a collective operation. This accumulator cannot be activated again. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>.</p>
<h3>void sc::R12IntsAcc_MemoryGrp::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>.</p>
<h3>void sc::R12IntsAcc_MemoryGrp::store_memorygrp (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp; mem, int ni, const size_t blksize) [virtual]</h3>
<p>Stores all pair block of integrals held in mem mem must be the same as mem_ used to construct this This is a collective operation. See documentation for <code>R12IntsAcc::store_memorygrp()</code> for more info. </p>
<p> Implements <code>sc::R12IntsAcc</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
