---
title: "sc_tchf(3)"
name: "sc_tchf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_tchf/"
description: "sc::TCHF –"
---

<p>sc::TCHF &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::TCSCF</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>TCHF (StateIn &amp;)



TCHF (const Ref&lt; KeyVal &gt; &amp;)



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
<h2>Member Function Documentation</h2>
<h3>void sc::TCHF::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::TCSCF</code>.</p>
<h3>int sc::TCHF::value_implemented () const [virtual]</h3>
<p>Information about the availability of values, gradients, and hessians. </p>
<p> Reimplemented from <code>sc::Function</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
