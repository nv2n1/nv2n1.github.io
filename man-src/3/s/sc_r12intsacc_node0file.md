---
title: "sc_r12intsacc_node0file(3)"
name: "sc_r12intsacc_node0file"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intsacc_node0file/"
description: "sc::R12IntsAcc_Node0File –"
---

<p>sc::R12IntsAcc_Node0File &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::R12IntsAcc</code>.</p>
<h3>Classes</h3>
<pre><code>struct PairBlkInfo



Public Member Functions
R12IntsAcc_Node0File (Ref&lt; MemoryGrp &gt; &amp;mem, const char *filename, int num_te_types, int ni, int nj, int nx, int ny)



R12IntsAcc_Node0File (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void store_memorygrp (Ref&lt; MemoryGrp &gt; &amp;mem, int ni, const size_t blksize=0)


Stores all pair block of integrals held in mem.


void store_pair_block (int i, int j, double *ints)


Stores an ij pair block of integrals to the file.


void commit ()


Commit the content of the accumulator for reading - deactivate the associated MemoryGrp and activate the accumulator.


void activate ()


Call when ready to start reading content.


void deactivate ()


Done reading content - activate the associated MemoryGrp This is a collective operation.


double * retrieve_pair_block (int i, int j, tbint_type oper_type)


Retrieves an ij pair block of integrals from the file.


void release_pair_block (int i, int j, tbint_type oper_type)


Releases an ij pair block of integrals.


bool is_local (int i, int j) const


Is this block stored locally?


bool is_avail (int i, int j) const


In this implementation blocks are available only on node 0.


bool has_access (int proc) const


Does this task have access to all the integrals?


bool can_restart () const


Can restart Node0File-based accumulator.


int ij_index (int i, int j) const



int ij_proc (int i, int j) const</code></pre>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntsAcc_Node0File::commit () [virtual]</h3>
<p>Commit the content of the accumulator for reading &#8211; deactivate the associated <code>MemoryGrp</code> and activate the accumulator. This is a collective operation. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>.</p>
<h3>void sc::R12IntsAcc_Node0File::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>.</p>
<h3>void sc::R12IntsAcc_Node0File::store_memorygrp (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp; mem, int ni, const size_t blksize = 0) [virtual]</h3>
<p>Stores all pair block of integrals held in mem. By default blocks are appended to the end of the same file, i.e. they are assumed to have come from consecutive passes of the same transformation. This is a collective operation. See documentation for <code>R12IntsAcc::store_memorygrp()</code> for more info. </p>
<p> Implements <code>sc::R12IntsAcc</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
