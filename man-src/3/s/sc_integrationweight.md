---
title: "sc_integrationweight(3)"
name: "sc_integrationweight"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_integrationweight/"
description: "sc::IntegrationWeight –"
---

<p>sc::IntegrationWeight &#8211; </p>
<p> An abstract base class for computing grid weights.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::BeckeIntegrationWeight</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>IntegrationWeight (const Ref&lt; KeyVal &gt; &amp;)



IntegrationWeight (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void test (int icenter, SCVector3 &amp;point)



void test ()



virtual void init (const Ref&lt; Molecule &gt; &amp;, double tolerance)


Initialize the integration weight object.


virtual void done ()


Called when finished with the integration weight object.


virtual double w (int center, SCVector3 &amp;point, double *grad_w=0)=0


Computes the weight for a given center at a given point in space.



Protected Member Functions
void fd_w (int icenter, SCVector3 &amp;point, double *fd_grad_w)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>mol_</code> </p>
<p> double <code>tol_</code></p>
<h2>Detailed Description</h2>
<p>An abstract base class for computing grid weights.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::IntegrationWeight::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::BeckeIntegrationWeight</code>.</p>
<h3>virtual double sc::IntegrationWeight::w (int center, <code>SCVector3</code> &amp; point, double * grad_w = 0) [pure virtual]</h3>
<p>Computes the weight for a given center at a given <code>point</code> in space. Derivatives of the weigth with respect to nuclear coordinates are optionally returned in grad_w. This must be called after init, but before done. It must also be thread-safe. </p>
<p> Implemented in <code>sc::BeckeIntegrationWeight</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
