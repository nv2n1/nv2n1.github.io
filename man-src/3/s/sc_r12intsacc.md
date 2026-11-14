---
title: "sc_r12intsacc(3)"
name: "sc_r12intsacc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intsacc/"
description: "sc::R12IntsAcc –"
---

<p>sc::R12IntsAcc &#8211; </p>
<p> <code>R12IntsAcc</code> accumulates transformed (MO) integrals stored as (ijxy) where i, j, x, and, y lie in spaces I, J, <code>X</code>, and <code>Y</code>, respectively.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;r12ia.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::R12IntsAcc_MemoryGrp</code>, <code>sc::R12IntsAcc_MPIIOFile</code>, and <code>sc::R12IntsAcc_Node0File</code>.</p>
<h3>Public Types</h3>
<pre><code>enum tbint_type { eri = 0, r12 = 1, r12t1 = 2, r12t2 = 3 }


Types of two-body operators that R12IntsAcc understands.



Public Member Functions
R12IntsAcc (int num_te_types, int ni, int nj, int nx, int ny)



R12IntsAcc (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int num_te_types () const


The number of types of integrals that are being handled together.


int ni () const


Rank of index space i.


int nj () const


Rank of index space j.


int nx () const


Rank of index space x.


int ny () const


Rank of index space y.


size_t blocksize () const


Size of each block of the integrals of one type, in double words.


int next_orbital () const


The index of the first orbital in the next integrals batch to be stored.


virtual void store_memorygrp (Ref&lt; MemoryGrp &gt; &amp;mem, int ni, const size_t blksize=0)=0


Stores all pair block of integrals held in mem in a layout assumed throughout MBPT2_R12.


virtual void store_pair_block (int i, int j, double *ints)=0


All member functions of this class and its children indices i and j don't include frozen orbitals Stores an ij pair block of integrals (assumes the block resides locally).


virtual void commit ()


Commit the content of the accumulator for reading.


bool is_committed ()


Has the content of the accumulator been commited for reading?


virtual void activate ()


Call before starting to read content.


virtual void deactivate ()


Call when done reading content.


const bool is_active ()


Check if can read content.


virtual double * retrieve_pair_block (int i, int j, tbint_type oper_type)=0


Retrieves an ij pair block of integrals.


virtual void release_pair_block (int i, int j, tbint_type oper_type)=0


Releases an ij pair block of integrals (if needed).


virtual bool is_local (int i, int j) const =0


Is this block stored locally?


virtual bool is_avail (int i, int j) const =0


Is this block available to this task?


virtual bool has_access (int proc) const =0


Does this task have access to all the integrals?


int tasks_with_access (vector&lt; int &gt; &amp;twa_map) const


Returns the total number of tasks with access to integrals.


virtual bool can_restart () const =0


Can this specialization be used in restarts?



Static Public Attributes
static const int max_num_te_types_ = 4



Protected Member Functions
virtual int ntasks () const =0


total number of tasks


virtual int taskid () const =0


ID of this task.


void inc_next_orbital (int ni)


The index of the first orbital in the next integrals batch to be stored.



Protected Attributes
int ni_



int nj_



int nx_



int ny_



size_t nxy_



size_t blksize_



size_t blocksize_



int next_orbital_



bool committed_



bool active_</code></pre>
<h2>Detailed Description</h2>
<p><code>R12IntsAcc</code> accumulates transformed (MO) integrals stored as (ijxy) where i, j, x, and, y lie in spaces I, J, <code>X</code>, and <code>Y</code>, respectively. </p>
<p> ijxy is only the storage format, the actual type may be (ix|jy), (ij|xy), etc. </p>
<p> Transformed integrals are usually computed using a parallel MO integrals transformation procedure. In general, such transformations will require multiple passes through AO integrals. Each pass produces a batch of transformed integrals. For example, a batch in direct parallel MP2 energy algorithm is a set of integrals {(ix|jy)} in which i indices are in a finite subrange of O and x, j, and y take any of their allowed values. For example, if batch I contains all integrals (ix|jy) with i greater than or equal m but less than n, then batch I+1 contains integrals (ix|jy) with i greater than n. Integrals in batch 0 have indices i greater than or equal to 0. </p>
<p> After each pass the MO integrals are contained in a <code>MemoryGrp</code> object. The object is &#8216;stored&#8217; in accumulator using store_memorygrp(Ref&lt;MemoryGrp&gt;&amp; mem, int ni). After all batches have been stored, the content of <code>R12IntsAcc</code> needs to be &#8216;committed&#8217; using <code>commit()</code>. After that blocks of MO integrals can be accessed using retrieve_pair_block.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntsAcc::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::R12IntsAcc_MemoryGrp</code>, <code>sc::R12IntsAcc_MPIIOFile</code>, <code>sc::R12IntsAcc_MPIIOFile_Ind</code>, and <code>sc::R12IntsAcc_Node0File</code>.</p>
<h3>virtual void sc::R12IntsAcc::store_memorygrp (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp; mem, int ni, const size_t blksize = 0) [pure virtual]</h3>
<p>Stores all pair block of integrals held in mem in a layout assumed throughout <code>MBPT2_R12</code>. Let&#8217;s suppose the number of tasks is nproc, nj is the number of j indices, ni is the number of i indices of integrals held in mem at the moment. Then all integrals with a given i and j are stored on task (i*nj+j)/nproc and this ij block is (i*nj+j)nproc -th block on this task. Each ij block contains num_te_types_ subblocks of integrals. Each subblock of integrals has blksize bytes allocated for it. Note that blksize may be larger than blksize_ because an ij-block of partially transformed integrals may be larger than the block of fully transformed integrals. </p>
<p> Implemented in <code>sc::R12IntsAcc_MemoryGrp</code>, <code>sc::R12IntsAcc_MPIIOFile_Ind</code>, and <code>sc::R12IntsAcc_Node0File</code>.</p>
<h3>int sc::R12IntsAcc::tasks_with_access (vector&lt; int &gt; &amp; twa_map) const</h3>
<p>Returns the total number of tasks with access to integrals. If task i has access to the integrals, then twa_map[i] is its index among the tasks with access, -1 otherwise.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
