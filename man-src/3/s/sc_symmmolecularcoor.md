---
title: "sc_symmmolecularcoor(3)"
name: "sc_symmmolecularcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmmolecularcoor/"
description: "sc::SymmMolecularCoor –"
---

<p>sc::SymmMolecularCoor &#8211; </p>
<p> The <code>SymmMolecularCoor</code> class derives from <code>IntMolecularCoor</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::IntMolecularCoor</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SymmMolecularCoor (Ref&lt; Molecule &gt; &amp;mol)



SymmMolecularCoor (StateIn &amp;)



SymmMolecularCoor (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


void form_coordinates (int keep_variable=0)


Actually form the variable and constant internal coordinates from simple internal coordinates.


void guess_hessian (RefSymmSCMatrix &amp;hessian)


Form the approximate hessian.


RefSymmSCMatrix inverse_hessian (RefSymmSCMatrix &amp;)


Invert the hessian.


Ref&lt; NonlinearTransform &gt; change_coordinates ()


This overrides MoleculeCoor's change_coordinates and might transform to a new set of coordinates.


void print (std::ostream &amp;=ExEnv::out0()) const


Print the coordinate.



Protected Member Functions
void init ()


This is called by the constructors of classes derived from IntMolecularCoor.



Protected Attributes
int change_coordinates_



int transform_hessian_



double max_kappa2_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SymmMolecularCoor</code> class derives from <code>IntMolecularCoor</code>. </p>
<p> It provides a unique set of totally symmetric internal coordinates. Giving an <code>MolecularEnergy</code> object a coor is usually the best way to optimize a molecular structure. However, for some classes of molecules <code>SymmMolecularCoor</code> doesn&#8217;t work very well. For example, enediyne can cause problems. In these cases, cartesian coordinates (obtained by not giving the <code>MolecularEnergy</code> object the coor keyword) might be better or you can manually specify the coordinates that the <code>SymmMolecularCoor</code> object uses with the variable keyword (see the <code>IntMolecularCoor</code> class description).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SymmMolecularCoor::SymmMolecularCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;change_coordinates&quot; 1c If true, the quality of the internal coordinates will be checked periodically and if they are beginning to become linearly dependent a new set of internal coordinates will be computed. The default is false. </p>
<dl>
<dt>max_kappa2</p>
<dd>A measure of the quality of the internal coordinates. Values of the 2-norm condition, $ppa_2$, larger than max_kappa2 are considered linearly dependent. The default is 10.0.</dl>
<dl>
<dt>transform_hessian</p>
<dd>If true, the hessian will be transformed every time the internal coordinates are formed. The default is true.</dl>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>NonlinearTransform</code>&gt; sc::SymmMolecularCoor::change_coordinates () [virtual]</h3>
<p>This overrides MoleculeCoor&#8217;s change_coordinates and might transform to a new set of coordinates. </p>
<p> Reimplemented from <code>sc::MolecularCoor</code>.</p>
<h3>void sc::SymmMolecularCoor::form_coordinates (int keep_variable = 0) [virtual]</h3>
<p>Actually form the variable and constant internal coordinates from simple internal coordinates. </p>
<p> Implements <code>sc::IntMolecularCoor</code>.</p>
<h3>void sc::SymmMolecularCoor::init () [protected, virtual]</h3>
<p>This is called by the constructors of classes derived from <code>IntMolecularCoor</code>. It initialized the lists of simple internal coordinates, and then calls the <code>form_coordinates()</code> member. </p>
<p> Reimplemented from <code>sc::IntMolecularCoor</code>.</p>
<h3>void sc::SymmMolecularCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::IntMolecularCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
