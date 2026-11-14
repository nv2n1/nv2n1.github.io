---
title: "sc_regiontimer(3)"
name: "sc_regiontimer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_regiontimer/"
description: "sc::RegionTimer –"
---

<p>sc::RegionTimer &#8211; </p>
<p> The <code>RegionTimer</code> class is used to record the time spent in a section of code.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;regtime.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::ParallelRegionTimer</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RegionTimer (const char *topname='total', int cpu_time=0, int wall_time=1)



RegionTimer (const Ref&lt; KeyVal &gt; &amp;)



void enter (const char *=0)



void change (const char *newname, const char *oldname=0)



void exit (const char *=0, bool do_not_throw=false)



void set_default (const char *)



void unset_default ()



void enter_default ()



void exit_default ()



virtual void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.


void update_top () const



int nregion () const



void get_region_names (const char *names[]) const



void get_wall_times (double *) const



void get_cpu_times (double *) const



void get_flops (double *) const



void get_depth (int *) const



double get_wall_time () const



double get_cpu_time () const



double get_flops () const



void add_wall_time (const char *, double)



void add_cpu_time (const char *, double)



void add_flops (const char *, double)



Static Public Member Functions
static RegionTimer * default_regiontimer ()



static void set_default_regiontimer (const Ref&lt; RegionTimer &gt; &amp;)



Protected Attributes
int wall_time_



int cpu_time_



int flops_



TimedRegion * top_



TimedRegion * current_



TimedRegion * default_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RegionTimer</code> class is used to record the time spent in a section of code. </p>
<p> During the run of a code, enter and exit members are called to begin and end timed sections. The print member is used to display the obtained times. Multiple enter calls for a region with the same name aggregate the timings. Nested regions are supported.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
