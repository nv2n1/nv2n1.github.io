---
title: "sc_bemsolvent(3)"
name: "sc_bemsolvent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_bemsolvent/"
description: "sc::BEMSolvent –"
---

<p>sc::BEMSolvent &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>BEMSolvent (const Ref&lt; KeyVal &gt; &amp;)



void init ()



void done (int clear_surface=1)



int ncharge ()



Ref&lt; Molecule &gt; solvent ()



double solvent_density ()



double ** alloc_charge_positions ()



void free_charge_positions (double **a)



double ** alloc_normals ()



void free_normals (double **a)



double * alloc_efield_dot_normals ()



void free_efield_dot_normals (double *a)



double * alloc_charges ()



void free_charges (double *a)



void charge_positions (double **)



void normals (double **)



void compute_charges (double *efield_dot_normals, double *charge)



void normalize_charge (double enclosed_charge, double *charges)



double nuclear_charge_interaction_energy (double *nuclear_charge, double **charge_positions, double *charge)



double nuclear_interaction_energy (double **charge_positions, double *charge)



double self_interaction_energy (double **charge_positions, double *charge)



double polarization_charge (double *charge)



double area () const



double volume () const



double computed_enclosed_charge () const



double disp ()



double rep ()



double disprep ()



void init_system_matrix ()



Ref&lt; TriangulatedImplicitSurface &gt; surface () const



Ref&lt; SCMatrixKit &gt; matrixkit ()
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
