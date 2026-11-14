---
title: "sc_molecularhessian(3)"
name: "sc_molecularhessian"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molecularhessian/"
description: "sc::MolecularHessian –"
---

<p>sc::MolecularHessian &#8211; </p>
<p> <code>MolecularHessian</code> is an abstract class that computes a molecule&#8217;s second derivatives of the energy with respect to changes in the nuclear coordinates.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;hess.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>. Inherited by <code>sc::DiagMolecularHessian</code>, <code>sc::FinDispMolecularHessian</code>, <code>sc::GuessMolecularHessian</code>, and <code>sc::ReadMolecularHessian</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MolecularHessian (const Ref&lt; KeyVal &gt; &amp;)


The MolecularHessian KeyVal constructor is used to generate a MolecularHessian derivative object from the input.


MolecularHessian (StateIn &amp;)



void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


RefSCDimension d3natom ()



Ref&lt; SCMatrixKit &gt; matrixkit () const



virtual RefSymmSCMatrix cartesian_hessian ()=0


Return the cartesian hessian.


virtual void set_energy (const Ref&lt; MolecularEnergy &gt; &amp;energy)


Some MolecularHessian specializations require a molecular energy object.


virtual MolecularEnergy * energy () const


This returns a MolecularEnergy object, if used by this specialization.



Static Public Member Functions
static RefSCMatrix cartesian_to_symmetry (const Ref&lt; Molecule &gt; &amp;m, Ref&lt; PointGroup &gt; pg=0, Ref&lt; SCMatrixKit &gt; kit=0)


Find transformation matrix from cartesian to symmetry coordinates.


static void write_cartesian_hessian (const char *filename, const Ref&lt; Molecule &gt; &amp;m, const RefSymmSCMatrix &amp;hess)


Write the hessian in a simple text format.


static void read_cartesian_hessian (const char *filename, const Ref&lt; Molecule &gt; &amp;m, const RefSymmSCMatrix &amp;hess)


Read the hessian from a simple text format.



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>mol_</code> </p>
<p> <code>RefSCDimension</code> <code>d3natom_</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>matrixkit_</code></p>
<h2>Detailed Description</h2>
<p><code>MolecularHessian</code> is an abstract class that computes a molecule&#8217;s second derivatives of the energy with respect to changes in the nuclear coordinates.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MolecularHessian::MolecularHessian (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>MolecularHessian</code> <code>KeyVal</code> constructor is used to generate a <code>MolecularHessian</code> derivative object from the input. It reads the keywords below. </p>
<p> KeywordTypeDefaultDescription molecule<code>Molecule</code>noneThe <code>Molecule</code> object.</p>
<h2>Member Function Documentation</h2>
<h3>static <code>RefSCMatrix</code> sc::MolecularHessian::cartesian_to_symmetry (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp; m, <code>Ref</code>&lt; <code>PointGroup</code> &gt; pg = 0, <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; kit = 0) [static]</h3>
<p>Find transformation matrix from cartesian to symmetry coordinates.</p>
<h3>virtual <code>MolecularEnergy</code>* sc::MolecularHessian::energy () const [virtual]</h3>
<p>This returns a <code>MolecularEnergy</code> object, if used by this specialization. Otherwise null is returned. </p>
<p> Reimplemented in <code>sc::FinDispMolecularHessian</code>.</p>
<h3>void sc::MolecularHessian::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::FinDispMolecularHessian</code>, <code>sc::ReadMolecularHessian</code>, <code>sc::GuessMolecularHessian</code>, and <code>sc::DiagMolecularHessian</code>.</p>
<h3>virtual void sc::MolecularHessian::set_energy (const <code>Ref</code>&lt; <code>MolecularEnergy</code> &gt; &amp; energy) [virtual]</h3>
<p>Some <code>MolecularHessian</code> specializations require a molecular energy object. The default implementations of this ignores the argument. </p>
<p> Reimplemented in <code>sc::FinDispMolecularHessian</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
