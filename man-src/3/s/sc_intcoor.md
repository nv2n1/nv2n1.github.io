---
title: "sc_intcoor(3)"
name: "sc_intcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_intcoor/"
description: "sc::IntCoor –"
---

<p>sc::IntCoor &#8211; </p>
<p> The <code>IntCoor</code> abstract class describes an internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<p> #include &lt;<a href="file:/usr/include/coor.h">coor.h</a>&gt; </p>
<p> Inherits <code>sc::SavableState</code>. </p>
<p> Inherited by <code>sc::SimpleCo</code>, and <code>sc::SumIntCoor</code>.</p>
<h3>Public Member Functions</h3>
<p> <code>IntCoor</code> (<code>StateIn</code> &amp;) </p>
<p> <code>IntCoor</code> (const <code>IntCoor</code> &amp;) </p>
<p> <code>IntCoor</code> (const char *label=0)<br />
 <i>This constructor takes a string containing a label for the internal coordinate. </i><br />
 <code>IntCoor</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 virtual const char * <code>label</code> () const<br />
 <i>Returns the string containing the label for the internal coordinate. </i><br />
 virtual double <code>value</code> () const<br />
 <i>Returns the value of the coordinate in atomic units or radians. </i><br />
 virtual void <code>set_value</code> (double)<br />
 <i>Sets the value of the coordinate in atomic units or radians. </i><br />
 virtual double <code>preferred_value</code> () const<br />
 <i>Returns the value of the coordinate in more familiar units. </i><br />
 virtual const char * <code>ctype</code> () const =0<br />
 <i>Returns a string representation of the type of coordinate this is. </i><br />
 virtual void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Print information about the coordinate. </i><br />
 virtual void <code>print_details</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, std::ostream &amp;=ExEnv::out0()) const </p>
<p> virtual double <code>force_constant</code> (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;)=0<br />
 <i>Returns the value of the force constant associated with this coordinate. </i><br />
 virtual void <code>update_value</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;)=0<br />
 <i>Recalculate the value of the coordinate. </i><br />
 virtual void <code>bmat</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCVector</code> &amp;bmat, double coef=1.0)=0<br />
 <i>Fill in a row the the B matrix. </i><br />
 virtual int <code>equivalent</code> (<code>Ref</code>&lt; <code>IntCoor</code> &gt; &amp;)=0<br />
 <i>Test to see if this internal coordinate is equivalent to that one. </i></p>
<h3>Protected Attributes</h3>
<p> char * <code>label_</code> </p>
<p> double <code>value_</code> </p>
<h3>Static Protected Attributes</h3>
<p> static double <code>bohr_conv</code> </p>
<p> static double <code>radian_conv</code> </p>
<h2>Detailed Description</h2>
<p> The <code>IntCoor</code> abstract class describes an internal coordinate of a molecule. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::IntCoor::IntCoor (const char * label = 0)</h3>
<p> This constructor takes a string containing a label for the internal coordinate. The string is copied.</p>
<h3>sc::IntCoor::IntCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p> The <code>KeyVal</code> constructor. .IP &quot;label&quot; 1c A label for the coordinate using only to identify the coordinate to the user in printouts. The default is no label. </p>
<dl COMPACT>
<dt>value</p>
<dd> A value for the coordinate. In the way that coordinates are usually used, the default is to compute a value from the cartesian coordinates in a <code>Molecule</code> object.</dl>
<dl COMPACT>
<dt>unit</p>
<dd> The unit in which the value is given. This can be bohr, anstrom, radian, and degree. The default is bohr for lengths and radian for angles.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual int sc::IntCoor::equivalent (<code>Ref</code>&lt; <code>IntCoor</code> &gt; &amp;) [pure virtual]</h3>
<p> Test to see if this internal coordinate is equivalent to that one. The definition of equivalence is left up to the individual coordinates.</p>
<h3>virtual double sc::IntCoor::force_constant (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;) [pure virtual]</h3>
<p> Returns the value of the force constant associated with this coordinate. </p>
<p> Implemented in <code>sc::SumIntCoor</code>, and <code>sc::SimpleCo</code>.</p>
<h3>void sc::IntCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p> Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>. </p>
<p> Reimplemented in <code>sc::SumIntCoor</code>, and <code>sc::SimpleCo</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for MPQC from the source code.</p>
