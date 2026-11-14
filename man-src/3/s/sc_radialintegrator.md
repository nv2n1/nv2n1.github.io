---
title: "sc_radialintegrator(3)"
name: "sc_radialintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_radialintegrator/"
description: "sc::RadialIntegrator –"
---

<p>sc::RadialIntegrator &#8211; </p>
<p> An abstract base class for radial integrators.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::EulerMaclaurinRadialIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RadialIntegrator (const Ref&lt; KeyVal &gt; &amp;)



RadialIntegrator (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


virtual int nr () const =0



virtual double radial_value (int ir, int nr, double radii, double &amp;multiplier)=0



Protected Attributes
int nr_</code></pre>
<h2>Detailed Description</h2>
<p>An abstract base class for radial integrators.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::RadialIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::EulerMaclaurinRadialIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
