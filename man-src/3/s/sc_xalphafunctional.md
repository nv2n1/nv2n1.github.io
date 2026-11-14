---
title: "sc_xalphafunctional(3)"
name: "sc_xalphafunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_xalphafunctional/"
description: "sc::XalphaFunctional –"
---

<p>sc::XalphaFunctional &#8211; </p>
<p> Implements the Xalpha exchange functional.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>XalphaFunctional (const Ref&lt; KeyVal &gt; &amp;)



XalphaFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void point (const PointInputData &amp;, PointOutputData &amp;)



void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.



Protected Attributes
double alpha_



double factor_</code></pre>
<h2>Detailed Description</h2>
<p>Implements the Xalpha exchange functional.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::XalphaFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
