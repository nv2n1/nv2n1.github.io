---
title: "sc_nelfunctional(3)"
name: "sc_nelfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_nelfunctional/"
description: "sc::NElFunctional –"
---

<p>sc::NElFunctional &#8211; </p>
<p> The <code>NElFunctional</code> computes the number of electrons.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/functional.h">functional.h</a>&gt; </p>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>NElFunctional</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>NElFunctional</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>point</code> (const <code>PointInputData</code> &amp;, <code>PointOutputData</code> &amp;) </p>
<h2>Detailed Description</h2>
<p> The <code>NElFunctional</code> computes the number of electrons. </p>
<p> It is primarily for testing the integrator.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::NElFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p> Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
