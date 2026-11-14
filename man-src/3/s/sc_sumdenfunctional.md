---
title: "sc_sumdenfunctional(3)"
name: "sc_sumdenfunctional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sumdenfunctional/"
description: "sc::SumDenFunctional –"
---

<p>sc::SumDenFunctional &#8211; </p>
<p> The <code>SumDenFunctional</code> computes energies and densities using the a sum of energy density functions method.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;functional.h&gt;</code></pre>
<p> Inherits <code>sc::DenFunctional</code>. Inherited by <code>sc::StdDenFunctional</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SumDenFunctional (const Ref&lt; KeyVal &gt; &amp;)


This KeyVal constructor reads the following keywords:.


SumDenFunctional (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void set_spin_polarized (int)



void set_compute_potential (int)



int need_density_gradient ()



void point (const PointInputData &amp;, PointOutputData &amp;)



void print (std::ostream &amp;=ExEnv::out0()) const


Print the object.


double a0 () const


Override the DenFunctional::a0() member, so that a0's in contributing functionals can be added in as well.



Protected Attributes
int n_



Ref&lt; DenFunctional &gt; * funcs_



double * coefs_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SumDenFunctional</code> computes energies and densities using the a sum of energy density functions method.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SumDenFunctional::SumDenFunctional (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>This <code>KeyVal</code> constructor reads the following keywords:. .IP &quot;funcs&quot; 1c Specifies an array of <code>DenIntegrator</code> objects.</p>
<dl>
<dt>coefs</p>
<dd>Specifies the coefficient of each <code>DenIntegrator</code> object.</p>
<dt>a0</p>
<dd>Specifies the coefficient of the Hartree-Fock exchange. This is nonzero for hybrid functionals. The default is zero.</dl>
<p> For example, the B3LYP functional can be specified with the following input: </p>
<pre> functional&lt;<code>SumDenFunctional</code>&gt;: (
 a0 = 0.2
 coefs = [ 0.8 0.72 0.19 0.81 ]
 funcs: [
 &lt;<code>SlaterXFunctional</code>&gt;:()
 &lt;<code>Becke88XFunctional</code>&gt;:()
 &lt;<code>VWN1LCFunctional</code>&gt;:( rpa = 1 )
 &lt;<code>LYPCFunctional</code>&gt;:()
 ]
 )</pre>
<p>&nbsp;<wbr></p>
<h2>Member Function Documentation</h2>
<h3>double sc::SumDenFunctional::a0 () const [virtual]</h3>
<p>Override the <code>DenFunctional::a0()</code> member, so that a0&#8217;s in contributing functionals can be added in as well. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>.</p>
<h3>void sc::SumDenFunctional::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::DenFunctional</code>. </p>
<p> Reimplemented in <code>sc::StdDenFunctional</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
