---
title: "sc_beckeintegrationweight(3)"
name: "sc_beckeintegrationweight"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_beckeintegrationweight/"
description: "sc::BeckeIntegrationWeight –"
---

<p>sc::BeckeIntegrationWeight &#8211; </p>
<p> Implements Becke&#8217;s integration weight scheme.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;integrator.h&gt;</code></pre>
<p> Inherits <code>sc::IntegrationWeight</code>.</p>
<h3>Public Member Functions</h3>
<p><code>BeckeIntegrationWeight</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>BeckeIntegrationWeight</code> (<code>StateIn</code> &amp;) </p>
<p> void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>init</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, double tolerance)<br />
 <i>Initialize the integration weight object. </i><br />
 void <code>done</code> ()<br />
 <i>Called when finished with the integration weight object. </i><br />
 double <code>w</code> (int center, <code>SCVector3</code> &amp;<code>point</code>, double *grad_w=0)<br />
 <i>Computes the weight for a given center at a given </i><code>point</code> in space.</p>
<h2>Detailed Description</h2>
<p>Implements Becke&#8217;s integration weight scheme.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::BeckeIntegrationWeight::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::IntegrationWeight</code>.</p>
<h3>double sc::BeckeIntegrationWeight::w (int center, <code>SCVector3</code> &amp; point, double * grad_w = 0) [virtual]</h3>
<p>Computes the weight for a given center at a given <code>point</code> in space. Derivatives of the weigth with respect to nuclear coordinates are optionally returned in grad_w. This must be called after init, but before done. It must also be thread-safe. </p>
<p> Implements <code>sc::IntegrationWeight</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
