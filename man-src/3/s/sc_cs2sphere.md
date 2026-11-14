---
title: "sc_cs2sphere(3)"
name: "sc_cs2sphere"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_cs2sphere/"
---

sc::CS2Sphere -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>CS2Sphere (const SCVector3 &amp;v, double rad)



CS2Sphere (double x, double y, double z, double rad)



void initialize (SCVector3 &amp;v, double rad)



CS2Sphere &amp; operator= (const CS2Sphere &amp;s)



double distance (CS2Sphere &amp;asphere)



double common_radius (CS2Sphere &amp;asphere)



const SCVector3 &amp; center (void) const



double x () const



double y () const



double z () const



SCVector3 center_vec (const CS2Sphere &amp;asphere)



double radius (void) const



void recenter (const SCVector3 &amp;v)



void print (std::ostream &amp;os=ExEnv::out0()) const



int intersect (CS2Sphere *s, int n_spheres) const



Static Public Member Functions
static void print_counts (std::ostream &amp;=ExEnv::out0())



Static Public Attributes
static int n_no_spheres_



static int n_probe_enclosed_by_a_sphere_



static int n_probe_center_not_enclosed_



static int n_surface_of_s0_not_covered_



static int n_plane_totally_covered_



static int n_internal_edge_not_covered_



static int n_totally_covered_
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
