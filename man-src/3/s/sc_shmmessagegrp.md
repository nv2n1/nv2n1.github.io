---
title: "sc_shmmessagegrp(3)"
name: "sc_shmmessagegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shmmessagegrp/"
description: "sc::ShmMessageGrp –"
---

<p>sc::ShmMessageGrp &#8211; </p>
<p> The <code>ShmMessageGrp</code> class is an implementation of <code>MessageGrp</code> that allows multiple process to be started that communicate with shared memory.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;messshm.h&gt;</code></pre>
<p> Inherits <code>sc::intMessageGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ShmMessageGrp</code> ()<br />
 <i>Reads the number of processors from environmental variable NUMPROC. </i><br />
 <code>ShmMessageGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>ShmMessageGrp</code> <code>KeyVal</code> constructor takes a single keyword that specifies the number of processors.<br />
 <code>ShmMessageGrp</code> (int nprocs)<br />
 <i>Initialize </i><code>ShmMessageGrp</code> to use nprocs processors.<br />
 void <code>sync</code> ()<br />
 <i>Synchronize all of the processors. </i><br />
 <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>clone</code> (void)<br />
 <i>Returns a copy of this </i><code>MessageGrp</code> specialization that provides an independent communication context.</p>
<h3>Protected Member Functions</h3>
<pre><code>void basic_send (int target, int type, const void *data, int nbyte)


Must be implemented by specializations.


void basic_recv (int type, void *data, int nbyte)


Must be implemented by specializations.


int basic_probe (int type)


Must be implemented by specializations.


void initialize (int nprocs)



void initialize ()



msgbuf_t * NEXT_MESSAGE (msgbuf_t *m)



void get_change (int node)



void put_change (int node)



void wait_for_write (int node)



void release_write (int node)



void print_buffer (int node, int me)



Protected Attributes</code></pre>
<p> <code>commbuf_t</code> * <code>commbuf</code> [MAXPROCS] </p>
<p> int <code>shmid</code> </p>
<p> int <code>semid</code> </p>
<p> int <code>change_semid</code> </p>
<p> void * <code>sharedmem</code> </p>
<p> struct sembuf <code>semdec</code> </p>
<p> struct sembuf <code>seminc</code></p>
<h2>Detailed Description</h2>
<p>The <code>ShmMessageGrp</code> class is an implementation of <code>MessageGrp</code> that allows multiple process to be started that communicate with shared memory. </p>
<p> This only provides improved performance if you have multiple CPU&#8217;s in a symmetric multiprocessor configuration. Nonetheless, it is quite useful on a single CPU for tracking down bugs.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::ShmMessageGrp::ShmMessageGrp (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>ShmMessageGrp</code> <code>KeyVal</code> constructor takes a single keyword that specifies the number of processors. Here is an example of a <code>ParsedKeyVal</code> input that creates a <code>ShmMessageGrp</code> that runs on four processors: </p>
<pre> message&lt;ShmMessageGrp&gt;: n = 4</pre>
<p>&nbsp;<wbr></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>MessageGrp</code>&gt; sc::ShmMessageGrp::clone (void) [virtual]</h3>
<p>Returns a copy of this <code>MessageGrp</code> specialization that provides an independent communication context. </p>
<p> Implements <code>sc::MessageGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
