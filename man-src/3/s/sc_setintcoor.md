---
title: "sc_setintcoor(3)"
name: "sc_setintcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_setintcoor/"
description: "sc::SetIntCoor –"
---

<p>sc::SetIntCoor &#8211; </p>
<p> The <code>SetIntCoor</code> class describes a set of internal coordinates.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SetIntCoor</code> (<code>StateIn</code> &amp;) </p>
<p> <code>SetIntCoor</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>add</code> (const <code>Ref</code>&lt; <code>IntCoor</code> &gt; &amp;)<br />
 <i>Adds an internal coordinate to the set. </i><br />
 void <code>add</code> (const <code>Ref</code>&lt; <code>SetIntCoor</code> &gt; &amp;)<br />
 <i>Adds all the elements of another set to this one. </i><br />
 void <code>pop</code> ()<br />
 <i>Removes the last coordinate from this set. </i><br />
 void <code>clear</code> ()<br />
 <i>Removes all coordinates from the set. </i><br />
 int <code>n</code> () const<br />
 <i>Returns the number of coordinates in the set. </i><br />
 <code>Ref</code>&lt; <code>IntCoor</code> &gt; <code>coor</code> (int i) const<br />
 <i>Returns a reference to the i&#8217;th coordinate in the set. </i><br />
 virtual void <code>fd_bmat</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCMatrix</code> &amp;)<br />
 <i></i><code>Compute</code> the B matrix by finite displacements.<br />
 virtual void <code>bmat</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSCMatrix</code> &amp;)<br />
 <i></i><code>Compute</code> the B matrix the old-fashioned way.<br />
 virtual void <code>guess_hessian</code> (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSymmSCMatrix</code> &amp;)<br />
 <i>Create an approximate Hessian for this set of coordinates. </i><br />
 virtual void <code>print_details</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, std::ostream &amp;=ExEnv::out0()) const<br />
 <i>Print the coordinates in the set. </i><br />
 virtual void <code>update_values</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;)<br />
 <i>Recalculate the values of the internal coordinates in the set. </i><br />
 virtual void <code>values_to_vector</code> (const <code>RefSCVector</code> &amp;)<br />
 <i>Copy the values of the internal coordinates to a vector. </i></p>
<h2>Detailed Description</h2>
<p>The <code>SetIntCoor</code> class describes a set of internal coordinates. </p>
<p> It can automatically generate these coordinates using a integral coordinate generator object (see the <code>IntCoorGen</code> class) or the internal coordinates can be explicity given. </p>
<p> The following is a sample <code>ParsedKeyVal</code> input for a <code>SetIntCoor</code> object. </p>
<pre> setintcoor&lt;SetIntCoor&gt;: [
 &lt;<code>SumIntCoor</code>&gt;: (
 coor: [
 &lt;<code>StreSimpleCo</code>&gt;:( atoms = [ 1 2 ] )
 &lt;<code>StreSimpleCo</code>&gt;:( atoms = [ 2 3 ] )
 ]
 coef = [ 1.0 1.0 ]
 )
 &lt;<code>BendSimpleCo</code>&gt;:( atoms = [ 1 2 3 ] )
 ]</pre>
<p>&nbsp;<wbr></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::SetIntCoor::SetIntCoor (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. .IP &quot;generator&quot; 1c A <code>IntCoorGen</code> object that will be used to generate the internal coordinates. </p>
<dl>
<dt>i</p>
<dd>A sequence of integer keywords, all $i$ for $0 </p>
<hr>
<p> assigned to <code>IntCoor</code> objects.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SetIntCoor::guess_hessian (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;, <code>RefSymmSCMatrix</code> &amp;) [virtual]</h3>
<p>Create an approximate Hessian for this set of coordinates. This Hessian is a symmetric matrix whose i&#8217;th diagonal is the force constant for the i&#8217;th coordinate in the set.</p>
<h3>void sc::SetIntCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
