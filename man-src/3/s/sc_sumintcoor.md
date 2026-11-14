---
title: "sc_sumintcoor(3)"
name: "sc_sumintcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_sumintcoor/"
description: "sc::SumIntCoor –"
---

<p>sc::SumIntCoor &#8211; </p>
<p> <code>SumIntCoor</code> is used to construct linear combinations of internal coordinates.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::IntCoor</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SumIntCoor (StateIn &amp;)



SumIntCoor (const char *)


This constructor takes a string containing a label for this coordinate.


SumIntCoor (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.


int n ()


Returns the number of coordinates in this linear combination.


void add (Ref&lt; IntCoor &gt; &amp;, double coef)


Add a coordinate to the linear combination.


void normalize ()


This function normalizes all the coefficients.


double preferred_value () const


Returns the value of the coordinate in a.u. and radians.


const char * ctype () const


Always returns ``SUM''.


void print_details (const Ref&lt; Molecule &gt; &amp;, std::ostream &amp;=ExEnv::out0()) const


Print the individual coordinates in the sum with their coefficients.


double force_constant (Ref&lt; Molecule &gt; &amp;)


Returns the weighted sum of the individual force constants.


void update_value (const Ref&lt; Molecule &gt; &amp;)


Recalculate the value of the coordinate.


void bmat (const Ref&lt; Molecule &gt; &amp;, RefSCVector &amp;bmat, double coef=1.0)


Fill in a row the the B matrix.


int equivalent (Ref&lt; IntCoor &gt; &amp;)


Always returns 0.</code></pre>
<h2>Detailed Description</h2>
<p><code>SumIntCoor</code> is used to construct linear combinations of internal coordinates. </p>
<p> The following is a sample <code>ParsedKeyVal</code> input for a <code>SumIntCoor</code> object: </p>
<pre> sumintcoor&lt;<code>SumIntCoor</code>&gt;: (
 coor: [
 &lt;<code>StreSimpleCo</code>&gt;:( atoms = [ 1 2 ] )
 &lt;<code>StreSimpleCo</code>&gt;:( atoms = [ 2 3 ] )
 ]
 coef = [ 1.0 1.0 ]
 )</pre>
<p>&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SumIntCoor::SumIntCoor (const char *)</h3>
<p>This constructor takes a string containing a label for this coordinate.</p>
<h3>sc::SumIntCoor::SumIntCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;coor&quot; 1c A vector of <code>IntCoor</code> objects that define the summed coordinates. </p>
<dl>
<dt>coef</p>
<dd>A vector of floating <code>point</code> numbers that gives the coefficients of the summed coordinates.</dl>
<h2>Member Function Documentation</h2>
<h3>void sc::SumIntCoor::add (<code>Ref</code>&lt; <code>IntCoor</code> &gt; &amp;, double coef)</h3>
<p>Add a coordinate to the linear combination. coef is the coefficient for the added coordinate.</p>
<h3>void sc::SumIntCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::IntCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
