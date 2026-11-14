---
title: "sc_simpleco(3)"
name: "sc_simpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_simpleco/"
description: "sc::SimpleCo –"
---

<p>sc::SimpleCo &#8211; </p>
<p> The <code>SimpleCo</code> abstract class describes a simple internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;simple.h&gt;</code></pre>
<p> Inherits <code>sc::IntCoor</code>. Inherited by <code>sc::BendSimpleCo</code>, <code>sc::LinIPSimpleCo</code>, <code>sc::LinOPSimpleCo</code>, <code>sc::OutSimpleCo</code>, <code>sc::ScaledTorsSimpleCo</code>, <code>sc::StreSimpleCo</code>, and <code>sc::TorsSimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SimpleCo (int, const char *=0)


This constructor takes an integer argument which is the number of atoms needed to describe the coordinate.


SimpleCo (const Ref&lt; KeyVal &gt; &amp;, int natom)


The KeyVal constructor requires the number of atoms.


int natoms () const


Returns the number of atoms in the coordinate.


int operator[] (int i) const


Returns the index of the i'th atom in the coordinate.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


SimpleCo (StateIn &amp;)



virtual int operator== (SimpleCo &amp;)



int operator!= (SimpleCo &amp;u)



double force_constant (Ref&lt; Molecule &gt; &amp;)


Returns an approximate force constant (a la Almlof).


void update_value (const Ref&lt; Molecule &gt; &amp;)


Recalculates the value of the coordinate based on the geometry in the Molecule.


void bmat (const Ref&lt; Molecule &gt; &amp;, RefSCVector &amp;bmat, double coef=1.0)


Fill in a row of the B matrix.


virtual double calc_force_con (Molecule &amp;)=0


Calculates an approximate force constant and returns it's value.


virtual double calc_intco (Molecule &amp;, double *=0, double=1)=0


Calculate the value of the coordinate based on what's in Molecule.


void print_details (const Ref&lt; Molecule &gt; &amp;, std::ostream &amp;=ExEnv::out0()) const


Print the coordinate.


int equivalent (Ref&lt; IntCoor &gt; &amp;)


Tests to see if two coordinates are equivalent to each other.



Protected Attributes
int natoms_



int * atoms</code></pre>
<h2>Detailed Description</h2>
<p>The <code>SimpleCo</code> abstract class describes a simple internal coordinate of a molecule. </p>
<p> The number atoms involved can be 2, 3 or 4 and is determined by the specialization of <code>SimpleCo</code>. </p>
<p> There are three ways to specify the atoms involved in the internal coordinate. The first way is a shorthand notation, just a vector of a label followed by the atom numbers (starting at 1) is given. For example, a stretch between two atoms, 1 and 2, is given, in the <code>ParsedKeyVal</code> format, as </p>
<pre> stretch&lt;StreSimpleCo&gt;: [ R12 1 2 ]</pre>
<p>The other two ways to specify the atoms are more general. With them, it is possible to give parameters for the <code>IntCoor</code> base class (and thus give the value of the coordinate). In the first of these input formats, a vector associated with the keyword atoms gives the atom numbers. The following specification for stretch is equivalent to that above: </p>
<pre> stretch&lt;StreSimpleCo&gt;:( label = R12 atoms = [ 1 2 ] )</pre>
<p>In the second, a vector, atom_labels, is given along with a <code>Molecule</code> object. The atom labels are looked up in the <code>Molecule</code> object to find the atom numbers. The following specification for stretch is equivalent to those above: </p>
<pre> molecule&lt;Molecule&gt;: (
 { atom_labels atoms geometry } = {
 H1 H [ 1.0 0.0 0.0 ]
 H2 H [-1.0 0.0 0.0 ] } )
 stretch&lt;StreSimpleCo&gt;:( label = R12
 atom_labels = [ H1 H2 ]
 molecule = $:molecule )</pre>
<p>&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SimpleCo::SimpleCo (int, const char * = 0)</h3>
<p>This constructor takes an integer argument which is the number of atoms needed to describe the coordinate. A second optional char* argument is a label for the coordinate. This argument is passed on to the <code>IntCoor</code> constructor.</p>
<h2>Member Function Documentation</h2>
<h3>virtual double sc::SimpleCo::calc_intco (<code>Molecule</code> &amp;, double * = 0, double = 1) [pure virtual]</h3>
<p>Calculate the value of the coordinate based on what&#8217;s in <code>Molecule</code>. If given a double*, fill in that part of the B matrix. If the bmatrix is to be calculated, the third argument gives the coefficient.</p>
<h3>int sc::SimpleCo::equivalent (<code>Ref</code>&lt; <code>IntCoor</code> &gt; &amp;)</h3>
<p>Tests to see if two coordinates are equivalent to each other. This is false if the atoms don&#8217;t match.</p>
<h3>void sc::SimpleCo::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::IntCoor</code>.</p>
<h3>void sc::SimpleCo::update_value (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;) [virtual]</h3>
<p>Recalculates the value of the coordinate based on the geometry in the <code>Molecule</code>. </p>
<p> Implements <code>sc::IntCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
