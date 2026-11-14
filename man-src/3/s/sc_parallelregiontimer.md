---
title: "sc_parallelregiontimer(3)"
name: "sc_parallelregiontimer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_parallelregiontimer/"
description: "sc::ParallelRegionTimer –"
---

<p>sc::ParallelRegionTimer &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RegionTimer</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ParallelRegionTimer (const Ref&lt; MessageGrp &gt; &amp;, const char *topname='total', int cpu_time=0, int wall_time=1)



ParallelRegionTimer (const Ref&lt; KeyVal &gt; &amp;)



void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.



Protected Member Functions
void send_subregions (int node, const TimedRegion *r) const



void recv_subregions (int node, TimedRegion *r) const



void all_reduce_regions () const



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>MessageGrp</code> &gt; <code>msg_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
