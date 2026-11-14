---
title: "sc_eulermaclaurinradialintegrator(3)"
name: "sc_eulermaclaurinradialintegrator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_eulermaclaurinradialintegrator/"
description: "sc::EulerMaclaurinRadialIntegrator –"
---

<p>sc::EulerMaclaurinRadialIntegrator &#8211; </p>
<p> An implementation of a radial integrator using the Euler-Maclaurin weights and grid points.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::RadialIntegrator</code>.</p>
<h3>Public Member Functions</h3>
<p><code>EulerMaclaurinRadialIntegrator</code> (int i) </p>
<p> <code>EulerMaclaurinRadialIntegrator</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>Constructs a </i><code>EulerMaclaurinRadialIntegrator</code> from <code>KeyVal</code> input.<br />
 <code>EulerMaclaurinRadialIntegrator</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 int <code>nr</code> () const </p>
<p> double <code>radial_value</code> (int ir, int nr, double radii, double &amp;multiplier) </p>
<p> void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the object. </i></p>
<h2>Detailed Description</h2>
<p>An implementation of a radial integrator using the Euler-Maclaurin weights and grid points.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::EulerMaclaurinRadialIntegrator::EulerMaclaurinRadialIntegrator (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Constructs a <code>EulerMaclaurinRadialIntegrator</code> from <code>KeyVal</code> input. The nr keyword gives the number of radial integration points. The default is 75.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::EulerMaclaurinRadialIntegrator::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::RadialIntegrator</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
