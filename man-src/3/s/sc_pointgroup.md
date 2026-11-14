---
title: "sc_pointgroup(3)"
name: "sc_pointgroup"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pointgroup/"
description: "sc::PointGroup –"
---

<p>sc::PointGroup &#8211; </p>
<p> The <code>PointGroup</code> class is really a place holder for a <code>CharacterTable</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pointgrp.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PointGroup</code> (const char *)<br />
 <i>This constructor takes a string containing the Schoenflies symbol of the </i><code>point</code> group as its only argument.<br />
 <code>PointGroup</code> (const char *, <code>SymmetryOperation</code> &amp;)<br />
 <i>Like the above, but this constructor also takes a frame of reference as an argument. </i><br />
 <code>PointGroup</code> (const char *, <code>SymmetryOperation</code> &amp;, const <code>SCVector3</code> &amp;)<br />
 <i>Like the above, but this constructor also takes a </i><code>point</code> of origin as an argument.<br />
 <code>PointGroup</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>PointGroup</code> <code>KeyVal</code> constructor looks for three keywords: symmetry, symmetry_frame, and origin.<br />
 <code>PointGroup</code> (<code>StateIn</code> &amp;) </p>
<p> <code>PointGroup</code> (const <code>PointGroup</code> &amp;) </p>
<p> <code>PointGroup</code> (const <code>Ref</code>&lt; <code>PointGroup</code> &gt; &amp;) </p>
<p> <code>PointGroup</code> &amp; <code>operator=</code> (const <code>PointGroup</code> &amp;) </p>
<p> int <code>equiv</code> (const <code>Ref</code>&lt; <code>PointGroup</code> &gt; &amp;, double tol=1.0e-6) const<br />
 <i>Returns 1 if the </i><code>point</code> groups are equivalent, 0 otherwise.<br />
 <code>CharacterTable</code> <code>char_table</code> () const<br />
 <i>Returns the </i><code>CharacterTable</code> for this <code>point</code> group.<br />
 const char * <code>symbol</code> () const<br />
 <i>Returns the Schoenflies symbol for this </i><code>point</code> group.<br />
 <code>SymmetryOperation</code> &amp; <code>symm_frame</code> ()<br />
 <i>Returns the frame of reference for this </i><code>point</code> group.<br />
 const <code>SymmetryOperation</code> &amp; <code>symm_frame</code> () const<br />
 <i>A const version of the above. </i><br />
 <code>SCVector3</code> &amp; <code>origin</code> ()<br />
 <i>Returns the origin of the symmetry frame. </i><br />
 const <code>SCVector3</code> &amp; <code>origin</code> () const </p>
<p> void <code>set_symbol</code> (const char *)<br />
 <i>Sets (or resets) the Schoenflies symbol. </i><br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;so)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Print the object. </i></p>
<h2>Detailed Description</h2>
<p>The <code>PointGroup</code> class is really a place holder for a <code>CharacterTable</code>. </p>
<p> It contains a string representation of the Schoenflies symbol of a <code>point</code> group, a frame of reference for the symmetry operation transformation matrices, and a <code>point</code> of origin. The origin is not respected by the symmetry operations, so if you want to use a <code>point</code> group with a nonzero origin, first translate all your coordinates to the origin and then set the origin to zero.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::PointGroup::PointGroup (const char *)</h3>
<p>This constructor takes a string containing the Schoenflies symbol of the <code>point</code> group as its only argument.</p>
<h3>sc::PointGroup::PointGroup (const char *, <code>SymmetryOperation</code> &amp;)</h3>
<p>Like the above, but this constructor also takes a frame of reference as an argument.</p>
<h3>sc::PointGroup::PointGroup (const char *, <code>SymmetryOperation</code> &amp;, const <code>SCVector3</code> &amp;)</h3>
<p>Like the above, but this constructor also takes a <code>point</code> of origin as an argument.</p>
<h3>sc::PointGroup::PointGroup (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>PointGroup</code> <code>KeyVal</code> constructor looks for three keywords: symmetry, symmetry_frame, and origin. symmetry is a string containing the Schoenflies symbol of the <code>point</code> group. origin is an array of doubles which gives the x, y, and z coordinates of the origin of the symmetry frame. symmetry_frame is a 3 by 3 array of arrays of doubles which specify the principal axes for the transformation matrices as a unitary rotation. </p>
<p> For example, a simple input which will use the default origin and symmetry_frame ((0,0,0) and the unit matrix, respectively), might look like this: </p>
<pre> pointgrp&lt;PointGroup&gt;: (
 symmetry = 'c2v'
 )</pre>
<p>By default, the principal rotation axis is taken to be the z axis. If you already have a set of coordinates which assume that the rotation axis is the x axis, then you&#8217;ll have to rotate your frame of reference with symmetry_frame: </p>
<pre> pointgrp&lt;PointGroup&gt;: (
 symmetry = 'c2v'
 symmetry_frame = [
 [ 0 0 1 ]
 [ 0 1 0 ]
 [ 1 0 0 ]
 ]
 )</pre>
<p>&nbsp;<wbr></p>
<h2>Member Function Documentation</h2>
<h3>void sc::PointGroup::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
