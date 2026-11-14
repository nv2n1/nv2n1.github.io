---
title: "sc_clhf(3)"
name: "sc_clhf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_clhf/"
description: "sc::CLHF –"
---

<p>sc::CLHF &#8211; </p>
<p> <code>CLHF</code> is a Hartree-Fock specialization of <code>CLSCF</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;clhf.h&gt;</code></pre>
<p> Inherits <code>sc::CLSCF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CLHF (StateIn &amp;)



CLHF (const Ref&lt; KeyVal &gt; &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void print (std::ostream &amp;o=ExEnv::out0()) const


Print information about the object.


void two_body_energy (double &amp;ec, double &amp;ex)



int value_implemented () const


Information about the availability of values, gradients, and hessians.


int gradient_implemented () const



Protected Member Functions
void ao_fock (double accuracy)



void two_body_deriv (double *)</code></pre>
<h2>Detailed Description</h2>
<p><code>CLHF</code> is a Hartree-Fock specialization of <code>CLSCF</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::CLHF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::CLSCF</code>.</p>
<h3>int sc::CLHF::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
