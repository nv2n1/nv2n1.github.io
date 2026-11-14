---
title: "sc_r12intsacc_mpiiofile(3)"
name: "sc_r12intsacc_mpiiofile"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intsacc_mpiiofile/"
description: "sc::R12IntsAcc_MPIIOFile –"
---

<p>sc::R12IntsAcc_MPIIOFile &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::R12IntsAcc</code>. Inherited by <code>sc::R12IntsAcc_MPIIOFile_Ind</code>.</p>
<h3>Classes</h3>
<pre><code>struct PairBlkInfo



Public Member Functions</code></pre>
<p> <code>R12IntsAcc_MPIIOFile</code> (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem, const char *filename, int num_te_types, int ni, int nj, int nx, int ny) </p>
<p> <code>R12IntsAcc_MPIIOFile</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>store_pair_block</code> (int i, int j, double *ints)<br />
 <i>Stores an ij pair block of integrals to the file. </i><br />
 void <code>commit</code> ()<br />
 <i>Commit the content of the accumulator for reading &#8211; deactivate the associated </i><code>MemoryGrp</code> and activate the accumulator.<br />
 void <code>activate</code> ()<br />
 <i>Call when ready to read content. </i><br />
 void <code>deactivate</code> ()<br />
 <i>Done reading content &#8211; activate the associated </i><code>MemoryGrp</code> This is a collective operation.<br />
 void <code>release_pair_block</code> (int i, int j, <code>tbint_type</code> oper_type)<br />
 <i>Releases an ij pair block of integrals. </i><br />
 bool <code>is_local</code> (int i, int j) const<br />
 <i>Is this block stored locally? </i><br />
 bool <code>is_avail</code> (int i, int j) const<br />
 <i>In this implementation blocks are available everywhere. </i><br />
 bool <code>has_access</code> (int proc) const<br />
 <i>Does this task have access to all the integrals? </i><br />
 bool <code>can_restart</code> () const<br />
 <i>Can restart MPI-IO-based accumulator. </i><br />
 int <code>ij_index</code> (int i, int j) const</p>
<h3>Protected Member Functions</h3>
<pre><code>void check_error_code_ (int errcod) const


Utility function to check MPI I/O error codes.


void init (bool restart)



int ntasks () const


total number of tasks


int taskid () const


ID of this task.



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; <code>mem_</code> </p>
<p> int <code>nproc_</code> </p>
<p> size_t <code>nints_per_block_</code> </p>
<p> char * <code>filename_</code> </p>
<p> MPI_File <code>datafile_</code> </p>
<p> struct <code>sc::R12IntsAcc_MPIIOFile::PairBlkInfo</code> * <code>pairblk_</code></p>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntsAcc_MPIIOFile::commit () [virtual]</h3>
<p>Commit the content of the accumulator for reading &#8211; deactivate the associated <code>MemoryGrp</code> and activate the accumulator. This is a collective operation. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>.</p>
<h3>void sc::R12IntsAcc_MPIIOFile::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::R12IntsAcc</code>. </p>
<p> Reimplemented in <code>sc::R12IntsAcc_MPIIOFile_Ind</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
