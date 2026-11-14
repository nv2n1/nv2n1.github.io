---
title: "sc_timedregion(3)"
name: "sc_timedregion"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_timedregion/"
---

sc::TimedRegion -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>TimedRegion (const char *name)



const char * name () const



TimedRegion * findinsubregion (const char *)



void cpu_enter (double)



void wall_enter (double)



void flops_enter (double)



void cpu_exit (double)



void wall_exit (double)



void flops_exit (double)



void cpu_add (double t)



void wall_add (double t)



void flops_add (double t)



TimedRegion * up () const



TimedRegion * subregions () const



TimedRegion * next () const



TimedRegion * prev () const



int nregion ()



void get_region_names (const char *names[])



void get_wall_times (double *)



void get_cpu_times (double *)



void get_flops (double *)



void get_depth (int *, int depth=0)
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
