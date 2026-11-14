---
title: "sc_distshellpair(3)"
name: "sc_distshellpair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distshellpair/"
description: "sc::DistShellPair –"
---

<p>sc::DistShellPair &#8211; </p>
<p> Distributes shell pairs either statically or dynamically.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;distshpair.h&gt;

Classes</code></pre>
<p> class <code>SharedData</code><br />
 <i>This is used to store data that must be shared between all cooperating shell pairs. </i></p>
<h3>Public Member Functions</h3>
<pre><code>DistShellPair (const Ref&lt; MessageGrp &gt; &amp;, int nthread, int mythread, const Ref&lt; ThreadLock &gt; &amp;lock, const Ref&lt; GaussianBasisSet &gt; &amp;bs1, const Ref&lt; GaussianBasisSet &gt; &amp;bs2, bool dynamic, SharedData *shared=0)


The DistShellPair class is used to distribute shell pair indices among tasks.


void init ()


Resets to the first shell pair.


void set_debug (int d)


How much stuff to print out.


void set_print_percent (double p)


How often to print status from node 0.


int get_task (int &amp;P, int &amp;Q)


Puts the current PQ shell pair into P and Q and returns 1.</code></pre>
<h2>Detailed Description</h2>
<p>Distributes shell pairs either statically or dynamically.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::DistShellPair::DistShellPair (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;, int nthread, int mythread, const <code>Ref</code>&lt; <code>ThreadLock</code> &gt; &amp; lock, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; bs1, const <code>Ref</code>&lt; <code>GaussianBasisSet</code> &gt; &amp; bs2, bool dynamic, <code>SharedData</code> * shared = 0)</h3>
<p>The <code>DistShellPair</code> class is used to distribute shell pair indices among tasks. Both static (round-robin) and dynamic methods are supported.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::DistShellPair::get_task (int &amp; P, int &amp; Q)</h3>
<p>Puts the current PQ shell pair into P and Q and returns 1. When there are no more shell pairs to be processed by this processor, 0 is returned. Once we start doing get_tasks, we have to go to the end if dynamic load balancing is used. </p>
<p> P belongs to bs1, and Q belongs to bs2. If (bs1 == bs2) then P is greater or equal to Q.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
