---
title: "sc_mpimessagegrp(3)"
name: "sc_mpimessagegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mpimessagegrp/"
description: "sc::MPIMessageGrp –"
---

<p>sc::MPIMessageGrp &#8211; </p>
<p> The <code>MPIMessageGrp</code> class is an concrete implementation of <code>MessageGrp</code> that uses the MPI 1 library.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;messmpi.h&gt;</code></pre>
<p> Inherits <code>sc::MessageGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MPIMessageGrp (MPI_Comm comm)


Use an MPI communicator to create a MessageGrp.


MPIMessageGrp (int *argc, char ***argv)


Use argc and argv to create a MPIMessageGrp.


MPIMessageGrp (const Ref&lt; KeyVal &gt; &amp;)


Construction MPIMessageGrp given a KeyVal input object.


Ref&lt; MessageGrp &gt; clone (void)


Clones (dups) an MPIMessageGrp from MPI_COMM_WORLD.


void raw_send (int target, const void *data, int nbyte)



void raw_recv (int sender, void *data, int nbyte)



void raw_sendt (int target, int type, const void *data, int nbyte)



void raw_recvt (int type, void *data, int nbyte)



int probet (int type)


Ask if a given typed message has been received.


void sync ()


Synchronize all of the processors.


void sum (double *, int n, double *scratch=0, int target=-1)


Global sum reduction.


void sum (int *, int n, int *scratch=0, int target=-1)



void reduce (double *, int n, GrpReduce&lt; double &gt; &amp;, double *scratch=0, int target=-1)


Global generic reduction.


void reduce (unsigned int *, int n, GrpReduce&lt; unsigned int &gt; &amp;, unsigned int *scratch=0, int target=-1)



void reduce (int *, int n, GrpReduce&lt; int &gt; &amp;, int *scratch=0, int target=-1)



void reduce (char *, int n, GrpReduce&lt; char &gt; &amp;, char *scratch=0, int target=-1)



void reduce (unsigned char *, int n, GrpReduce&lt; unsigned char &gt; &amp;, unsigned char *scratch=0, int target=-1)



void reduce (signed char *, int n, GrpReduce&lt; signed char &gt; &amp;, signed char *scratch=0, int target=-1)



void reduce (short *, int n, GrpReduce&lt; short &gt; &amp;, short *scratch=0, int target=-1)



void reduce (float *, int n, GrpReduce&lt; float &gt; &amp;, float *scratch=0, int target=-1)



void reduce (long *, int n, GrpReduce&lt; long &gt; &amp;, long *scratch=0, int target=-1)



void raw_bcast (void *data, int nbyte, int from)



Protected Member Functions
void init (MPI_Comm comm, int *argc=0, char ***argv=0)


Not thread-safe due to race condition on nmpi_grps variable.



Protected Attributes
void * buf



int bufsize



int rnode



int rtag



int rlen



bool use_messagegrp_collectives_


If true use the generic collective routines in the base class.


Ref&lt; ThreadGrp &gt; threadgrp



MPI_Comm commgrp


Currently each commgrp is a dup of MPI_COMM_WORLD.



Static Protected Attributes
static int nmpi_grps


Number of MPIMessageGrp's currently in use.


static Ref&lt; ThreadLock &gt; grplock


lock to access nmpi_grps variable</code></pre>
<h2>Detailed Description</h2>
<p>The <code>MPIMessageGrp</code> class is an concrete implementation of <code>MessageGrp</code> that uses the MPI 1 library.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MPIMessageGrp::MPIMessageGrp (MPI_Comm comm)</h3>
<p>Use an MPI communicator to create a <code>MessageGrp</code>. The comm argument could be a subset of MPI_COMM_WORLD, for example.</p>
<h3>sc::MPIMessageGrp::MPIMessageGrp (int * argc, char *** argv)</h3>
<p>Use argc and argv to create a <code>MPIMessageGrp</code>. This would have to be used for implementations of MPI that have MPI_Init fill in argc and argv.</p>
<h3>sc::MPIMessageGrp::MPIMessageGrp (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construction <code>MPIMessageGrp</code> given a <code>KeyVal</code> input object.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MPIMessageGrp::reduce (double *, int n, <code>GrpReduce</code>&lt; double &gt; &amp;, double * scratch = 0, int target = -1) [virtual]</h3>
<p>Global generic reduction. Similar members exist for each of the basic types. </p>
<p> Reimplemented from <code>sc::MessageGrp</code>.</p>
<h3>void sc::MPIMessageGrp::sum (double * data, int n, double * = 0, int target = -1) [virtual]</h3>
<p>Global sum reduction. Similar members exist for each of the basic types. </p>
<p> Reimplemented from <code>sc::MessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
