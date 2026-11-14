---
title: "sc_r12intsacc_mpiiofile_ind(3)"
name: "sc_r12intsacc_mpiiofile_ind"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_r12intsacc_mpiiofile_ind/"
description: "sc::R12IntsAcc_MPIIOFile_Ind –"
---

<p>sc::R12IntsAcc_MPIIOFile_Ind &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::R12IntsAcc_MPIIOFile</code>.</p>
<h3>Public Member Functions</h3>
<p><code>R12IntsAcc_MPIIOFile_Ind</code> (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem, const char *filename, int num_te_types, int ni, int nj, int nx, int ny) </p>
<p> <code>R12IntsAcc_MPIIOFile_Ind</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>store_memorygrp</code> (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;mem, int ni, const size_t blksize=0)<br />
 <i>Stores all pair block of integrals held in mem. </i><br />
 double * <code>retrieve_pair_block</code> (int i, int j, <code>tbint_type</code> oper_type)<br />
 <i>Retrieves an ij pair block of integrals from the file. </i></p>
<h2>Member Function Documentation</h2>
<h3>void sc::R12IntsAcc_MPIIOFile_Ind::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::R12IntsAcc_MPIIOFile</code>.</p>
<h3>void sc::R12IntsAcc_MPIIOFile_Ind::store_memorygrp (<code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp; mem, int ni, const size_t blksize = 0) [virtual]</h3>
<p>Stores all pair block of integrals held in mem. By default blocks are appended to the end of the same file, i.e. they are assumed to have come from consecutive passes of the same transformation. This is a collective operation. See documentation for <code>R12IntsAcc::store_memorygrp()</code> for more info. </p>
<p> Implements <code>sc::R12IntsAcc</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
