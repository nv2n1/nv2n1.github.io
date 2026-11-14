---
title: "sc_lsdacfunctional(3)"
name: "sc_lsdacfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_lsdacfunctional/"
description: "sc::LSDACFunctional –"
---

<p>sc::LSDACFunctional &#8211; </p>
<p> An abstract base class for local correlation functionals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>. Inherited by <code>sc::PW92LCFunctional</code>, <code>sc::PZ81LCFunctional</code>, and <code>sc::VWNLCFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LSDACFunctional (const Ref&lt; KeyVal &gt; &amp;)



LSDACFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void point (const PointInputData &amp;, PointOutputData &amp;)



virtual void point_lc (const PointInputData &amp;, PointOutputData &amp;, double &amp;ec_local, double &amp;decrs, double &amp;deczeta)=0</code></pre>
<h2>Detailed Description</h2>
<p>An abstract base class for local correlation functionals.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::LSDACFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>. </p>
<p> Reimplemented in <code>sc::VWNLCFunctional</code>, <code>sc::VWN1LCFunctional</code>, <code>sc::VWN2LCFunctional</code>, <code>sc::VWN3LCFunctional</code>, <code>sc::VWN4LCFunctional</code>, <code>sc::VWN5LCFunctional</code>, <code>sc::PW92LCFunctional</code>, and <code>sc::PZ81LCFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
