---
title: "sc_angularintegrator(3)"
name: "sc_angularintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_angularintegrator/"
description: "sc::AngularIntegrator –"
---

<p>sc::AngularIntegrator &#8211; </p>
<p> An abstract base class for angular integrators.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::GaussLegendreAngularIntegrator</code>, and <code>sc::LebedevLaikovIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>AngularIntegrator (const Ref&lt; KeyVal &gt; &amp;)



AngularIntegrator (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual int nw (void) const =0



virtual int num_angular_points (double r_value, int ir)=0



virtual double angular_point_cartesian (int iangular, double r, SCVector3 &amp;integration_point) const =0</code></pre>
<h2>Detailed Description</h2>
<p>An abstract base class for angular integrators.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::AngularIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::LebedevLaikovIntegrator</code>, and <code>sc::GaussLegendreAngularIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
