---
title: "sc_messagegrp(3)"
name: "sc_messagegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_messagegrp/"
description: "sc::MessageGrp –"
---

<p>sc::MessageGrp &#8211; </p>
<p> The <code>MessageGrp</code> abstract class provides a mechanism for moving data and objects between nodes in a parallel machine.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;message.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::intMessageGrp</code>, <code>sc::MPIMessageGrp</code>, and <code>sc::ProcMessageGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MessageGrp (const Ref&lt; KeyVal &gt; &amp;)



int n ()


Returns the number of processors.


int me ()


Returns my processor number. In the range [0,n()).


virtual Ref&lt; MessageGrp &gt; clone (void)=0


Returns a copy of this MessageGrp specialization that provides an independent communication context.


virtual void send (int target, const double *data, int ndata)


Send messages sequentially to the target processor.


virtual void send (int target, const unsigned int *data, int ndata)



virtual void send (int target, const int *data, int ndata)



virtual void send (int target, const char *data, int nbyte)



virtual void send (int target, const unsigned char *data, int nbyte)



virtual void send (int target, const signed char *data, int nbyte)



virtual void send (int target, const short *data, int ndata)



virtual void send (int target, const long *data, int ndata)



virtual void send (int target, const float *data, int ndata)



void send (int target, double data)



void send (int target, int data)



virtual void raw_send (int target, const void *data, int nbyte)=0



virtual void sendt (int target, int type, const double *data, int ndata)


Send typed messages to the target processor.


virtual void sendt (int target, int type, const unsigned int *data, int ndata)



virtual void sendt (int target, int type, const int *data, int ndata)



virtual void sendt (int target, int type, const char *data, int nbyte)



virtual void sendt (int target, int type, const unsigned char *data, int nbyte)



virtual void sendt (int target, int type, const signed char *data, int nbyte)



virtual void sendt (int target, int type, const short *data, int ndata)



virtual void sendt (int target, int type, const long *data, int ndata)



virtual void sendt (int target, int type, const float *data, int ndata)



void sendt (int target, int type, double data)



void sendt (int target, int type, int data)



virtual void raw_sendt (int target, int type, const void *data, int nbyte)=0



virtual void recv (int sender, double *data, int ndata)


Receive messages sent sequentually from the sender.


virtual void recv (int sender, unsigned int *data, int ndata)



virtual void recv (int sender, int *data, int ndata)



virtual void recv (int sender, char *data, int nbyte)



virtual void recv (int sender, unsigned char *data, int nbyte)



virtual void recv (int sender, signed char *data, int nbyte)



virtual void recv (int sender, short *data, int ndata)



virtual void recv (int sender, long *data, int ndata)



virtual void recv (int sender, float *data, int ndata)



void recv (int sender, double &amp;data)



void recv (int sender, int &amp;data)



virtual void raw_recv (int sender, void *data, int nbyte)=0



virtual void recvt (int type, double *data, int ndata)


Receive messages sent by type.


virtual void recvt (int type, unsigned int *data, int ndata)



virtual void recvt (int type, int *data, int ndata)



virtual void recvt (int type, char *data, int nbyte)



virtual void recvt (int type, unsigned char *data, int nbyte)



virtual void recvt (int type, signed char *data, int nbyte)



virtual void recvt (int type, short *data, int ndata)



virtual void recvt (int type, long *data, int ndata)



virtual void recvt (int type, float *data, int ndata)



void recvt (int type, double &amp;data)



void recvt (int type, int &amp;data)



virtual void raw_recvt (int type, void *data, int nbyte)=0



virtual int probet (int type)=0


Ask if a given typed message has been received.


virtual void bcast (double *data, int ndata, int from=0)


Do broadcasts of various types of data.


virtual void bcast (unsigned int *data, int ndata, int from=0)



virtual void bcast (int *data, int ndata, int from=0)



virtual void bcast (char *data, int nbyte, int from=0)



virtual void bcast (unsigned char *data, int nbyte, int from=0)



virtual void bcast (signed char *data, int nbyte, int from=0)



virtual void bcast (short *data, int ndata, int from=0)



virtual void bcast (long *data, int ndata, int from=0)



virtual void bcast (float *data, int ndata, int from=0)



virtual void raw_bcast (void *data, int nbyte, int from=0)



void bcast (double &amp;data, int from=0)



void bcast (int &amp;data, int from=0)



virtual void raw_collect (const void *part, const int *lengths, void *whole, int bytes_per_datum=1)


Collect data distributed on the nodes to a big array replicated on each node.


void collect (const double *part, const int *lengths, double *whole)



virtual void sum (double *data, int n, double *=0, int target=-1)


Global sum reduction.


virtual void sum (unsigned int *data, int n, unsigned int *=0, int target=-1)



virtual void sum (int *data, int n, int *=0, int target=-1)



virtual void sum (char *data, int n, char *=0, int target=-1)



virtual void sum (unsigned char *data, int n, unsigned char *=0, int target=-1)



virtual void sum (signed char *data, int n, signed char *=0, int target=-1)



void sum (double &amp;data)



void sum (int &amp;data)



virtual void max (double *data, int n, double *=0, int target=-1)


Global maximization.


virtual void max (int *data, int n, int *=0, int target=-1)



virtual void max (unsigned int *data, int n, unsigned int *=0, int target=-1)



virtual void max (char *data, int n, char *=0, int target=-1)



virtual void max (unsigned char *data, int n, unsigned char *=0, int target=-1)



virtual void max (signed char *data, int n, signed char *=0, int target=-1)



void max (double &amp;data)



void max (int &amp;data)



virtual void min (double *data, int n, double *=0, int target=-1)


Global minimization.


virtual void min (int *data, int n, int *=0, int target=-1)



virtual void min (unsigned int *data, int n, unsigned int *=0, int target=-1)



virtual void min (char *data, int n, char *=0, int target=-1)



virtual void min (unsigned char *data, int n, unsigned char *=0, int target=-1)



virtual void min (signed char *data, int n, signed char *=0, int target=-1)



void min (double &amp;data)



void min (int &amp;data)



virtual void reduce (double *, int n, GrpReduce&lt; double &gt; &amp;, double *scratch=0, int target=-1)


Global generic reduction.


virtual void reduce (int *, int n, GrpReduce&lt; int &gt; &amp;, int *scratch=0, int target=-1)



virtual void reduce (unsigned int *, int n, GrpReduce&lt; unsigned int &gt; &amp;, unsigned int *scratch=0, int target=-1)



virtual void reduce (char *, int n, GrpReduce&lt; char &gt; &amp;, char *scratch=0, int target=-1)



virtual void reduce (unsigned char *, int n, GrpReduce&lt; unsigned char &gt; &amp;, unsigned char *scratch=0, int target=-1)



virtual void reduce (signed char *, int n, GrpReduce&lt; signed char &gt; &amp;, signed char *scratch=0, int target=-1)



virtual void reduce (short *, int n, GrpReduce&lt; short &gt; &amp;, short *scratch=0, int target=-1)



virtual void reduce (float *, int n, GrpReduce&lt; float &gt; &amp;, float *scratch=0, int target=-1)



virtual void reduce (long *, int n, GrpReduce&lt; long &gt; &amp;, long *scratch=0, int target=-1)



void reduce (double &amp;data, GrpReduce&lt; double &gt; &amp;r)



void reduce (int &amp;data, GrpReduce&lt; int &gt; &amp;r)



virtual void sync ()


Synchronize all of the processors.


Ref&lt; MachineTopology &gt; topology ()


Return the MachineTopology object.


int classdesc_to_index (const ClassDesc *)


Each message group maintains an association of ClassDesc with a global index so SavableState information can be sent between nodes without needing to send the classname and look up the ClassDesc with each transfer.


const ClassDesc * index_to_classdesc (int)



int nclass () const



Static Public Member Functions
static void set_default_messagegrp (const Ref&lt; MessageGrp &gt; &amp;)


The default message group contains the primary message group to be used by an application.


static MessageGrp * get_default_messagegrp ()


Returns the default message group.


static MessageGrp * initial_messagegrp (int &amp;argc, char **&amp;argv)


Create a message group.



Protected Member Functions
void initialize (int me, int n)


The classdesc_to_index_ and index_to_classdesc_ arrays cannot be initialized by the MessageGrp CTOR, because the MessageGrp specialization has not yet been initialized and communication is not available.



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MachineTopology</code> &gt; <code>topology_</code> </p>
<p> int <code>debug_</code></p>
<h2>Detailed Description</h2>
<p>The <code>MessageGrp</code> abstract class provides a mechanism for moving data and objects between nodes in a parallel machine.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::MessageGrp::bcast (double * data, int ndata, int from = 0) [virtual]</h3>
<p>Do broadcasts of various types of data. Similar members exist for each of the basic types.</p>
<h3>int sc::MessageGrp::classdesc_to_index (const <code>ClassDesc</code> *)</h3>
<p>Each message group maintains an association of <code>ClassDesc</code> with a global index so <code>SavableState</code> information can be sent between nodes without needing to send the classname and look up the <code>ClassDesc</code> with each transfer. These routines return information about that mapping.</p>
<h3>virtual <code>Ref</code>&lt;<code>MessageGrp</code>&gt; sc::MessageGrp::clone (void) [pure virtual]</h3>
<p>Returns a copy of this <code>MessageGrp</code> specialization that provides an independent communication context. </p>
<p> Implemented in <code>sc::ProcMessageGrp</code>, <code>sc::MPIMessageGrp</code>, and <code>sc::ShmMessageGrp</code>.</p>
<h3>static <code>MessageGrp</code>* sc::MessageGrp::initial_messagegrp (int &amp; argc, char **&amp; argv) [static]</h3>
<p>Create a message group. This routine looks for a -messagegrp argument, then the environmental variable MESSAGEGRP to decide which specialization of <code>MessageGrp</code> would be appropriate. The argument to -messagegrp should be either string for a <code>ParsedKeyVal</code> constructor or a classname. If this returns null, it is up to the programmer to create a <code>MessageGrp</code>.</p>
<h3>void sc::MessageGrp::initialize (int me, int n) [protected]</h3>
<p>The classdesc_to_index_ and index_to_classdesc_ arrays cannot be initialized by the <code>MessageGrp</code> CTOR, because the <code>MessageGrp</code> specialization has not yet been initialized and communication is not available. CTOR&#8217;s of specializations of <code>MessageGrp</code> must call the initialize member in their body to complete the initialization process.</p>
<h3>virtual void sc::MessageGrp::max (double * data, int n, double * = 0, int target = -1) [virtual]</h3>
<p>Global maximization. Similar members exist for each of the basic types.</p>
<h3>virtual void sc::MessageGrp::min (double * data, int n, double * = 0, int target = -1) [virtual]</h3>
<p>Global minimization. Similar members exist for each of the basic types.</p>
<h3>virtual void sc::MessageGrp::raw_collect (const void * part, const int * lengths, void * whole, int bytes_per_datum = 1) [virtual]</h3>
<p>Collect data distributed on the nodes to a big array replicated on each node.</p>
<h3>virtual void sc::MessageGrp::recv (int sender, double * data, int ndata) [virtual]</h3>
<p>Receive messages sent sequentually from the sender. Similar members exist for each of the basic types.</p>
<h3>virtual void sc::MessageGrp::recvt (int type, double * data, int ndata) [virtual]</h3>
<p>Receive messages sent by type. Similar members exist for each of the basic types.</p>
<h3>virtual void sc::MessageGrp::reduce (double *, int n, <code>GrpReduce</code>&lt; double &gt; &amp;, double * scratch = 0, int target = -1) [virtual]</h3>
<p>Global generic reduction. Similar members exist for each of the basic types. </p>
<p> Reimplemented in <code>sc::MPIMessageGrp</code>.</p>
<h3>virtual void sc::MessageGrp::send (int target, const double * data, int ndata) [virtual]</h3>
<p>Send messages sequentially to the target processor. Similar members exist for each of the basic types.</p>
<h3>virtual void sc::MessageGrp::sendt (int target, int type, const double * data, int ndata) [virtual]</h3>
<p>Send typed messages to the target processor. Similar members exist for each of the basic types.</p>
<h3>static void sc::MessageGrp::set_default_messagegrp (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;) [static]</h3>
<p>The default message group contains the primary message group to be used by an application.</p>
<h3>virtual void sc::MessageGrp::sum (double * data, int n, double * = 0, int target = -1) [virtual]</h3>
<p>Global sum reduction. Similar members exist for each of the basic types. </p>
<p> Reimplemented in <code>sc::MPIMessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
